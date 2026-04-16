"""
MkDocs hook: inline SVG diagrams during PDF builds.

Chromium (used by mkdocs-exporter/Playwright) does not render <object> elements
when printing to PDF.  This hook replaces <object type="image/svg+xml"> tags with
the SVG file content inlined directly into the HTML, which Chromium renders reliably.

Important: mkdocs-exporter captures page.html at event priority 100 (before hooks
run at priority 0) and uses that snapshot for PDF rendering.  We therefore update
both the return value AND page.html so the renderer sees the modified HTML.

Only active when the CI_PDF environment variable is set.
"""

import os
import re
from pathlib import Path

# Page content area dimensions in mm, matching @page margins in print.css
# (25 mm top/bottom, 20 mm left/right on 210 × 297 mm paper).
_PAGE_W_MM = 170.0
# Use 220 mm (not the full 247 mm content height) as the SVG height cap.
# Setting it to exactly the content height causes Paged.js to loop when it
# encounters a full-page diagram — it can't tell whether the element fits and
# keeps retrying on successive pages.  220 mm leaves 27 mm of headroom so
# Paged.js can always place the diagram on a fresh page without looping.
_PAGE_H_MM = 220.0
_MM_TO_PX  = 96 / 25.4          # CSS px per mm at 96 dpi

# SVGs are scaled to this fraction of the content width.  Using less than
# 100% means the proportional height is also reduced, preventing diagrams
# that appear mid-page (after a heading or paragraph) from overflowing the
# bottom of the page.
_SVG_WIDTH_SCALE = 0.80


def _svg_dimensions(tag_attrs: str, requested_width: str) -> str:
    """Return the CSS width value that keeps the SVG on one page.

    The effective width is capped at _SVG_WIDTH_SCALE of the content area so
    the proportional height always has headroom for mid-page placement.
    The height attribute is always removed by the caller (letting the SVG scale
    proportionally from its viewBox), so only width is returned.
    """
    vb_match = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', tag_attrs, re.I)
    if not vb_match:
        # No viewBox — scale down any percentage width and leave height to CSS.
        if requested_width.endswith("%"):
            pct = float(requested_width[:-1]) * _SVG_WIDTH_SCALE
            return f"{pct:.1f}%"
        return requested_width

    vb_w = float(vb_match.group(1))
    vb_h = float(vb_match.group(2))
    aspect = vb_h / vb_w                # height per unit of width

    # Resolve the requested width as a fraction of the content width,
    # then apply the global scale factor.
    w_frac = 1.0
    if requested_width.endswith("%"):
        w_frac = float(requested_width[:-1]) / 100.0
    w_frac *= _SVG_WIDTH_SCALE

    natural_w_mm = _PAGE_W_MM * w_frac
    natural_h_mm = natural_w_mm * aspect

    if natural_h_mm <= _PAGE_H_MM:
        return f"{w_frac * 100:.1f}%"

    # Still too tall even after scaling: shrink further so height == page height.
    scale = _PAGE_H_MM / natural_h_mm
    final_w_mm = natural_w_mm * scale
    return f"{final_w_mm:.1f}mm"


def _inline_svgs(html: str, docs_dir: Path) -> str:
    """Replace <object type="image/svg+xml"> tags with inlined SVG content."""

    def replace_object(m):
        attrs = m.group(1)
        data_match  = re.search(r'data=["\']([^"\']+)["\']',  attrs)
        width_match = re.search(r'width=["\']([^"\']+)["\']', attrs)

        if not data_match:
            return m.group(0)

        src   = data_match.group(1)
        width = width_match.group(1) if width_match else "100%"

        file_path = docs_dir / src.lstrip("/")
        if not file_path.exists():
            return m.group(0)

        svg = file_path.read_text(encoding="utf-8")

        # Strip XML declaration and DOCTYPE — invalid inside HTML documents
        svg = re.sub(r"<\?xml[^?]*\?>", "", svg)
        svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
        svg = svg.strip()

        def patch_svg_tag(sm):
            tag_attrs = sm.group(1)

            final_w = _svg_dimensions(tag_attrs, width)

            # Set requested width; remove any explicit height attribute so
            # the SVG scales proportionally from its viewBox.  An explicit
            # height in mm would overflow the page when the SVG appears
            # mid-page with content above it.
            tag_attrs = re.sub(r'width="[^"]*"', f'width="{final_w}"', tag_attrs)
            tag_attrs = re.sub(r'\s*height="[^"]*"', '', tag_attrs)

            # Strip color-scheme so Playwright doesn't apply dark-mode colours.
            tag_attrs = re.sub(
                r'(style="[^"]*?)color-scheme:[^;]*;?\s*',
                r"\1",
                tag_attrs,
            )

            # Inject CSS constraints: height:auto keeps proportional scaling;
            # max-height caps the SVG at the full page content area so it can
            # never overflow the page even if it appears at the top of a page.
            constraint = f"height:auto;max-height:{_PAGE_H_MM:.1f}mm;"
            if 'style="' in tag_attrs:
                tag_attrs = tag_attrs.replace('style="', f'style="{constraint}', 1)
            else:
                tag_attrs += f' style="{constraint}"'

            return f"<svg{tag_attrs}>"

        svg = re.sub(r"<svg([^>]*?)>", patch_svg_tag, svg, count=1)

        return svg

    return re.sub(
        r"<object([^>]+)>.*?</object>",
        replace_object,
        html,
        flags=re.DOTALL,
    )


def on_post_page(output: str, page, config, **kwargs) -> str:
    if not os.environ.get("CI_PDF"):
        return output

    docs_dir = Path(config["docs_dir"])
    modified = _inline_svgs(output, docs_dir)

    # mkdocs-exporter's on_post_page runs at priority 100 (higher = earlier in
    # MkDocs), so it captures page.html before this hook (priority 0) runs.
    # We retroactively patch page.html so the exporter's renderer sees the
    # inlined SVGs when it generates the per-page PDF.
    if hasattr(page, "html") and page.html:
        page.html = _inline_svgs(page.html, docs_dir)

    return modified
