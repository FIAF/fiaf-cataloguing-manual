"""
MkDocs hook: generate a PDF table of contents and prepend it to the
aggregated PDF produced by mkdocs-exporter.

Only active when the CI_PDF environment variable is set.

The TOC is rendered as a separate PDF page by Playwright and prepended to
the main aggregated PDF using pypdf.  A second Playwright overlay pass then
stamps unified sequential Arabic page numbers (1, 2, 3 …) across all pages,
covering the per-section Paged.js numbers that would otherwise restart at 1
for each individually-rendered section.

Execution order: this hook's on_post_build fires before mkdocs-exporter's
aggregation completes, so we cannot act immediately in on_post_build.
Instead we register an atexit handler from on_post_build; by the time the
Python interpreter exits, the exporter has finished writing the aggregated
PDF and it is safe to prepend the TOC.

This hook must be listed AFTER hooks/heading_numbers.py in mkdocs.yml so
that on_nav receives section titles that are already prefixed with chapter
numbers ("2. Works", "A. Titles and Title Types", etc.).
"""

import io
import os
import re
from pathlib import Path

from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page

# ---------------------------------------------------------------------------
# Module-level state (accumulated during the build, reset on on_nav)
# ---------------------------------------------------------------------------

# Ordered list of dicts in TOC display order:
#   title    – display title (from nav, already prefixed by heading_numbers.py)
#   depth    – nesting level (0 = chapter, 1 = section, 2 = subsection)
#   src_path – page src_path for page-number lookup; None for non-linked headers
#   number   – section number to prepend in the TOC ("2.1", "A.3", …);
#              None when the title already contains the number or has no number
_nav_entries: list[dict] = []

# src_path → Path to the individual PDF rendered for that page
_page_pdfs: dict[str, Path] = {}

# src_path → list of (section_number_or_None, heading_text) for h2 headings on that page
_page_headings: dict[str, list[tuple]] = {}

# Absolute path to the docs/ directory (needed for font file URIs)
_docs_dir: str = ""

# Absolute path to the site output directory
_site_dir: str = ""


# ---------------------------------------------------------------------------
# Hook: on_nav
# Capture the nav structure AFTER heading_numbers.py has prefixed titles.
# ---------------------------------------------------------------------------

def on_nav(nav, config, **kwargs):
    global _docs_dir, _site_dir, _nav_entries, _page_pdfs, _page_headings
    _docs_dir = config["docs_dir"]
    _site_dir = config["site_dir"]
    _nav_entries = []
    _page_pdfs = {}
    _page_headings = {}

    # The entire manual is nested under a single top-level "Home" section.
    home = next(
        (item for item in nav.items if isinstance(item, Section) and item.title == "Home"),
        None,
    )
    if home is None:
        # Fallback: treat all top-level items as the nav root.
        _traverse(nav.items, depth=0)
    else:
        _traverse(home.children, depth=0)

    return nav


def _chapter_prefix(title: str) -> str | None:
    """Extract the leading number/letter from a prefixed title.

    "2. Works"              → "2"
    "A. Titles and Title…"  → "A"
    "Dedication"            → None
    """
    m = re.match(r'^([A-Z0-9]+)\.\s', title)
    return m.group(1) if m else None


def _traverse(items, depth: int, max_depth: int = 2, parent_prefix: str | None = None) -> None:
    """Recursively walk nav items and populate _nav_entries.

    depth levels:  0 = top-level chapter/appendix
                   1 = section within a chapter
                   2 = subsection (deepest level shown in TOC)

    max_depth=2 keeps the TOC to three visible levels.  Deeper nav items
    (depth > 2) exist in the site but are omitted from the printed TOC.

    parent_prefix is the chapter/section number inherited from the parent
    section (e.g. "2" for Works, "A" for Appendix A).  Sub-items at
    depth > 0 receive sequential numbers built on this prefix.
    """
    if depth > max_depth:
        return

    sub_idx = 0  # sequential counter for numbered sections at this level

    for item in items:
        if isinstance(item, Page):
            if item.file.src_path == "index.md":
                continue
            _nav_entries.append({
                "title": item.title or item.file.src_path,
                "depth": depth,
                "src_path": item.file.src_path,
                "number": None,
            })

        elif isinstance(item, Section):
            children = item.children or []
            has_index = (
                children
                and isinstance(children[0], Page)
                and children[0].file.dest_uri.endswith("index.html")
            )

            # Compute the prefix that THIS section passes down to its children,
            # and the number to display next to this entry in the TOC.
            if depth == 0:
                # Depth-0 titles already carry the number ("2. Works", "A. Titles").
                # Extract it to build children's numbers; don't display separately.
                own_prefix = _chapter_prefix(item.title)
                display_number = None
            elif parent_prefix is not None:
                # Parent has a numeric prefix → auto-number this section.
                sub_idx += 1
                own_prefix = f"{parent_prefix}.{sub_idx}"
                display_number = own_prefix
            else:
                # No parent prefix.  The title may already carry a letter prefix
                # (e.g. "A. Titles and Title Types" at depth 1 under "Appendices").
                own_prefix = _chapter_prefix(item.title)
                display_number = None   # letter already in title

            if has_index:
                index_page = children[0]
                _nav_entries.append({
                    "title": item.title,
                    "depth": depth,
                    "src_path": index_page.file.src_path,
                    "number": display_number,
                })
                _traverse(children[1:], depth + 1, max_depth, own_prefix)
            else:
                _nav_entries.append({
                    "title": item.title,
                    "depth": depth,
                    "src_path": None,
                    "number": display_number,
                })
                _traverse(children, depth + 1, max_depth, own_prefix)


# ---------------------------------------------------------------------------
# Hook: on_post_page
# Record each page's individual PDF path as set by mkdocs-exporter.
# ---------------------------------------------------------------------------

def on_post_page(output: str, page, config, **kwargs) -> str:
    if not os.environ.get("CI_PDF"):
        return output

    src = page.file.src_path.replace("\\", "/")

    # Prefer the path registered by mkdocs-exporter; fall back to a computed path.
    pdf_path: Path | None = None
    if hasattr(page, "formats") and isinstance(page.formats, dict):
        pdf_info = page.formats.get("pdf")
        if isinstance(pdf_info, dict):
            raw = pdf_info.get("path")
            if raw:
                pdf_path = Path(raw)

    if pdf_path is None:
        # Compute from dest_uri: "works/index.html" → "<site_dir>/works/index.pdf"
        pdf_path = Path(config["site_dir"]) / page.file.dest_uri.replace(".html", ".pdf")

    _page_pdfs[src] = pdf_path

    # Extract h2 headings for use as depth-2 TOC entries on pages that have
    # no nav children.  heading_numbers.py (listed before this hook) has already
    # injected <span class="section-number">2.1.1</span> into each heading.
    headings = []
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', output, re.DOTALL):
        inner = m.group(1)
        # Strip headerlink anchors (including their ¶ / &para; content).
        inner = re.sub(r'<a[^>]+class="headerlink"[^>]*>.*?</a>', '', inner, flags=re.DOTALL)
        # Strip footnote reference superscripts whole (tag + content) so the
        # footnote number doesn't appear as a stray digit in TOC entries,
        # e.g. "Events (e.g., ...)1" → "Events (e.g., ...)".
        inner = re.sub(r'<sup[^>]*>.*?</sup>', '', inner, flags=re.DOTALL)
        num_m = re.search(r'class="section-number"[^>]*>([^<]+)</span>', inner)
        num = num_m.group(1).strip() if num_m else None
        # Strip all remaining tags, leaving only text nodes.
        plain = re.sub(r'<[^>]+>', '', inner).strip()
        # Remove any leftover attr_list / curly-brace artifacts, e.g. "{ #id }".
        plain = re.sub(r'\s*\{[^}]*\}', '', plain).strip()
        # The plain text is "2.1.1 Title text"; strip the leading number.
        if num and plain.startswith(num):
            title = plain[len(num):].strip()
        else:
            title = plain
        if title:
            headings.append((num, title))
    _page_headings[src] = headings

    return output


# ---------------------------------------------------------------------------
# Hook: on_post_build
# Count pages, generate TOC HTML, render to PDF, prepend to aggregated PDF.
# ---------------------------------------------------------------------------

def on_post_build(config, **kwargs) -> None:
    """Register atexit handler to generate the TOC after the full build completes.

    This hook's on_post_build fires before mkdocs-exporter's aggregation step,
    so we cannot act immediately.  An atexit handler runs after the Python
    interpreter has finished all MkDocs processing, by which point the
    aggregated PDF exists.
    """
    if not os.environ.get("CI_PDF"):
        return

    import atexit
    atexit.register(_generate_toc)


def _generate_toc() -> None:
    """Generate the TOC PDF and prepend it to the aggregated PDF.

    Called via atexit, after mkdocs-exporter has finished writing
    site/assets/fiaf-cataloguing-manual.pdf.
    """
    import pypdf
    from playwright.sync_api import sync_playwright

    site_dir = Path(_site_dir)
    agg_pdf = site_dir / "assets" / "fiaf-cataloguing-manual.pdf"

    if not agg_pdf.exists():
        print(f"[pdf_toc] aggregated PDF not found at {agg_pdf}, skipping TOC")
        return

    # 1. Count pages in each individual section PDF.
    page_counts: dict[str, int] = {}
    for src, pdf_path in _page_pdfs.items():
        try:
            reader = pypdf.PdfReader(str(pdf_path))
            page_counts[src] = len(reader.pages)
        except Exception:
            pass  # page omitted from TOC if its PDF cannot be read

    # 2. Build TOC rows with cumulative start pages (Arabic, starting at 1).
    #
    # index.md (the site home page) is included in the aggregated PDF by
    # mkdocs-exporter but is intentionally skipped in _traverse (it has no
    # place in the TOC).  Seed the cursor with its page count so every
    # subsequent TOC reference lands on the correct physical page.
    toc_rows: list[dict] = []
    cursor = 1 + page_counts.get("index.md", 0)
    for entry in _nav_entries:
        title    = entry["title"]
        depth    = entry["depth"]
        src_path = entry["src_path"]
        number   = entry["number"]
        if src_path is None:
            toc_rows.append({"title": title, "depth": depth, "src_path": None, "page": None, "number": number})
        elif src_path in page_counts:
            toc_rows.append({"title": title, "depth": depth, "src_path": src_path, "page": cursor, "number": number})
            cursor += page_counts[src_path]

    if not toc_rows:
        print("[pdf_toc] no TOC rows generated, skipping")
        return

    # 2b. Read actual content page dimensions now so the TOC can use the same
    #     page size.  print.css does not declare @page { size: … }, so Playwright
    #     defaults to Letter (215.9 × 279.4 mm).  Reading from agg_pdf here —
    #     before we prepend the TOC — gives us the true content page dimensions.
    _content_reader   = pypdf.PdfReader(str(agg_pdf))
    _first_content    = _content_reader.pages[0]
    _content_w_pts    = float(_first_content.mediabox.width)
    _content_h_pts    = float(_first_content.mediabox.height)
    content_w_mm      = _content_w_pts * 25.4 / 72
    content_h_mm      = _content_h_pts * 25.4 / 72

    # 2c. For depth-1 rows with no nav children at depth 2, inject h2 headings
    #     from page content as depth-2 entries (gives chapters a third TOC level).
    enriched: list[dict] = []
    for i, row in enumerate(toc_rows):
        enriched.append(row)
        if row["depth"] == 1 and row["src_path"] is not None:
            next_depth = toc_rows[i + 1]["depth"] if i + 1 < len(toc_rows) else -1
            if next_depth != 2:
                for num, title in _page_headings.get(row["src_path"], []):
                    enriched.append({
                        "title": title,
                        "depth": 2,
                        "src_path": row["src_path"],
                        "page": row["page"],
                        "number": num,
                    })
    toc_rows = enriched

    # 3. Render the cover page and TOC in a single Playwright session.
    #
    #    TOC uses two passes:
    #      Pass 1 — render draft to measure the TOC page count.
    #      Pass 2 — shift every page reference by that count (content starts
    #               after the TOC pages) and render the final TOC.
    #
    #    The cover is a full-bleed image page prepended before the TOC.
    #    It is excluded from the page count (no page number stamped on it).
    toc_pdf   = site_dir / "assets" / "toc.pdf"
    cover_pdf = site_dir / "assets" / "cover.pdf"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()

        # Pass 1 — measure TOC page count.
        draft_html = _build_toc_html(toc_rows, Path(_docs_dir), content_w_mm, content_h_mm)
        pg.set_content(draft_html, wait_until="domcontentloaded")
        draft_bytes = pg.pdf(prefer_css_page_size=True, print_background=True)
        toc_page_count = len(pypdf.PdfReader(io.BytesIO(draft_bytes)).pages)

        # Pass 2 — shift all page references and render the final TOC.
        for row in toc_rows:
            if row["page"] is not None:
                row["page"] += toc_page_count

        final_html = _build_toc_html(toc_rows, Path(_docs_dir), content_w_mm, content_h_mm)
        pg.set_content(final_html, wait_until="domcontentloaded")
        pdf_bytes = pg.pdf(prefer_css_page_size=True, print_background=True)

        # Cover page — full-bleed image, no margins.
        cover_html = _build_cover_html(Path(_docs_dir), content_w_mm, content_h_mm)
        pg.set_content(cover_html, wait_until="domcontentloaded")
        cover_bytes = pg.pdf(prefer_css_page_size=True, print_background=True)

        browser.close()

    toc_pdf.write_bytes(pdf_bytes)
    cover_pdf.write_bytes(cover_bytes)

    # 4. Prepend cover and TOC to the aggregated PDF (cover first).
    writer = pypdf.PdfWriter()
    for pdf_file in (cover_pdf, toc_pdf, agg_pdf):
        reader = pypdf.PdfReader(str(pdf_file))
        for p in reader.pages:
            writer.add_page(p)

    tmp = agg_pdf.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as fh:
        writer.write(fh)
    tmp.replace(agg_pdf)
    toc_pdf.unlink(missing_ok=True)
    cover_pdf.unlink(missing_ok=True)

    # 5. Stamp sequential page numbers across the whole PDF via an overlay.
    #    Each section is rendered independently by Paged.js, so counter(page)
    #    resets to 1 per section.  We cover the old bottom-center numbers with a
    #    white box and draw the correct unified number on top.
    #    The cover page (1 page) is skipped — it carries no page number.
    #    toc_page_count was computed in step 3 (pass 1 render).
    combined_reader = pypdf.PdfReader(str(agg_pdf))
    total_pages     = len(combined_reader.pages)
    # Reuse content_w_mm / content_h_mm from step 2b — both TOC and content
    # pages were rendered at the same dimensions.
    page_width_pts  = content_w_mm  * 72 / 25.4
    page_height_pts = content_h_mm  * 72 / 25.4

    overlay_html = _build_page_numbers_overlay_html(
        total_pages, toc_page_count, page_width_pts, page_height_pts, Path(_docs_dir),
        cover_pages=1,
    )
    overlay_pdf = site_dir / "assets" / "page_numbers_overlay.pdf"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()
        pg.set_content(overlay_html, wait_until="networkidle")
        overlay_bytes = pg.pdf(prefer_css_page_size=True, print_background=True)
        browser.close()

    overlay_pdf.write_bytes(overlay_bytes)

    overlay_reader = pypdf.PdfReader(str(overlay_pdf))
    merged_writer  = pypdf.PdfWriter()
    for i, main_page in enumerate(combined_reader.pages):
        if i < len(overlay_reader.pages):
            main_page.merge_page(overlay_reader.pages[i])
        merged_writer.add_page(main_page)

    with open(tmp, "wb") as fh:
        merged_writer.write(fh)
    tmp.replace(agg_pdf)
    overlay_pdf.unlink(missing_ok=True)

    print(f"[pdf_toc] TOC prepended ({len(toc_rows)} entries, {cursor - 1} content pages, "
          f"{total_pages} total pages)")

    # 6. Optimise the final PDF with Ghostscript.
    #    pypdf's merge_page() duplicates font programs and content streams on
    #    every pass; gs deduplicates resources and recompresses streams without
    #    changing the visual output.
    _optimise_pdf(agg_pdf)


def _optimise_pdf(pdf_path: Path) -> None:
    """Run Ghostscript to deduplicate fonts and recompress the PDF in-place."""
    import shutil
    import subprocess

    gs = shutil.which("gs")
    if not gs:
        print("[pdf_toc] Ghostscript not found — skipping PDF optimisation")
        return

    tmp = pdf_path.with_suffix(".opt.pdf")
    result = subprocess.run(
        [
            gs,
            "-q",                       # quiet
            "-dBATCH",
            "-dNOPAUSE",
            "-dSAFER",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.7",
            "-dPDFSETTINGS=/ebook",     # deduplicate fonts, recompress streams
            "-dEmbedAllFonts=true",
            "-dSubsetFonts=true",
            f"-sOutputFile={tmp}",
            str(pdf_path),
        ],
        capture_output=True,
    )
    if result.returncode != 0:
        print(f"[pdf_toc] Ghostscript optimisation failed: {result.stderr.decode()}")
        tmp.unlink(missing_ok=True)
        return

    before = pdf_path.stat().st_size
    after  = tmp.stat().st_size
    tmp.replace(pdf_path)
    print(f"[pdf_toc] PDF optimised: {before // 1024} KB → {after // 1024} KB "
          f"({100 * (before - after) // before}% reduction)")


# ---------------------------------------------------------------------------
# Cover page HTML generation
# ---------------------------------------------------------------------------

def _build_cover_html(docs_dir: Path, page_w_mm: float, page_h_mm: float) -> str:
    """Return a standalone HTML document that renders as a full-bleed cover page.

    The cover image (markdown/assets/front.png) is embedded as a base64 data
    URI so that Chromium's file-origin restrictions cannot prevent it loading
    when the page is created via Playwright's set_content().
    """
    import base64
    cover_path = docs_dir / "assets" / "front.png"
    cover_b64  = base64.b64encode(cover_path.read_bytes()).decode()
    cover_src  = f"data:image/png;base64,{cover_b64}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
@page {{
  size: {page_w_mm:.4f}mm {page_h_mm:.4f}mm;
  margin: 0;
}}
html, body {{
  margin: 0;
  padding: 0;
}}
img {{
  display: block;
  width: {page_w_mm:.4f}mm;
  height: {page_h_mm:.4f}mm;
  object-fit: contain;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
</style>
</head>
<body>
<img src="{cover_src}" alt="">
</body>
</html>"""


# ---------------------------------------------------------------------------
# TOC HTML generation
# ---------------------------------------------------------------------------

def _build_toc_html(toc_rows: list[dict], docs_dir: Path, page_w_mm: float = 210.0, page_h_mm: float = 297.0) -> str:
    """Return a complete standalone HTML document for the TOC page.

    page_w_mm / page_h_mm should match the actual content PDF page dimensions
    so the TOC pages are identical in size to the rest of the document.
    """
    fonts_dir = docs_dir / "assets" / "fonts"

    def font_uri(filename: str) -> str:
        return (fonts_dir / filename).as_uri()

    rows_html: list[str] = []
    for row in toc_rows:
        depth  = row["depth"]
        page   = row["page"]
        number = row.get("number")
        indent = depth * 1.5  # em units

        # If the entry has an auto-generated number ("2.1", "A.3" …) prepend it.
        title_text = _escape(row["title"])
        if number is not None:
            title_text = f'<span class="toc-num">{_escape(number)}</span> {title_text}'

        if page is None:
            # Non-linked chapter/section header — no dot leader or page number.
            rows_html.append(
                f'<div class="toc-header d{depth}" style="padding-left:{indent}em">'
                f'<span class="toc-title">{title_text}</span>'
                f'</div>'
            )
        else:
            rows_html.append(
                f'<div class="toc-row d{depth}" style="padding-left:{indent}em">'
                f'<span class="toc-title">{title_text}</span>'
                f'<span class="toc-dots"></span>'
                f'<span class="toc-page">{page}</span>'
                f'</div>'
            )

    rows_str = "\n".join(rows_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Table of Contents</title>
<style>
@font-face {{
  font-family: "Brown";
  src: url("{font_uri('BrownStdRegular.otf')}") format("opentype");
  font-weight: 400;
  font-style: normal;
}}
@font-face {{
  font-family: "Brown";
  src: url("{font_uri('BrownStdBold.otf')}") format("opentype");
  font-weight: 700;
  font-style: normal;
}}
@font-face {{
  font-family: "Brown";
  src: url("{font_uri('BrownStdLight.otf')}") format("opentype");
  font-weight: 300;
  font-style: normal;
}}

@page {{
  size: {page_w_mm:.4f}mm {page_h_mm:.4f}mm;
  margin: 25mm 20mm;
}}

body {{
  font-family: "Brown", sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #1a1a1a;
  margin: 0;
}}

h1.toc-heading {{
  font-size: 16pt;
  font-weight: 700;
  margin: 0 0 16pt 0;
  padding-bottom: 5pt;
  border-bottom: 0.75pt solid #1a1a1a;
  letter-spacing: 0.02em;
}}

/* Non-linked section headers (chapters without an index page) */
.toc-header {{
  display: block;
  margin: 9pt 0 2pt 0;
  font-weight: 700;
  font-size: 10.5pt;
}}

/* Linked rows with dot leader */
.toc-row {{
  display: flex;
  align-items: baseline;
  margin: 2pt 0;
}}

.toc-row.d0 {{
  font-weight: 700;
  font-size: 10.5pt;
  margin-top: 7pt;
}}

.toc-row.d1 {{
  font-weight: 400;
  font-size: 9.5pt;
  color: #333;
}}

.toc-row.d2 {{
  font-weight: 400;
  font-size: 9pt;
  color: #555;
}}

.toc-title {{
  flex-shrink: 0;
  max-width: 82%;
}}

/* Section number prefix ("2.1", "A.3" …) — monospaced width so titles align */
.toc-num {{
  font-variant-numeric: tabular-nums;
  margin-right: 0.15em;
}}

/* Dot leader: a baseline-aligned spacer between title and page number */
.toc-dots {{
  flex: 1;
  overflow: hidden;
  height: 1em;
  border-bottom: 1px dotted #aaa;
  margin: 0 0.5em 2pt 0.5em;
  min-width: 0.8em;
}}

.toc-page {{
  flex-shrink: 0;
  font-variant-numeric: tabular-nums;
  min-width: 2.2em;
  text-align: right;
}}
</style>
</head>
<body>
<h1 class="toc-heading">Contents</h1>
{rows_str}
</body>
</html>"""


def _build_page_numbers_overlay_html(
    total_pages: int,
    toc_page_count: int,
    page_width_pts: float,
    page_height_pts: float,
    docs_dir: Path,
    cover_pages: int = 0,
) -> str:
    """Return HTML that renders as a PDF overlay with one page per physical page.

    Each overlay page contains only a white rectangle covering the bottom of
    the page (where Paged.js bakes its counter(page) number) and the correct
    sequential Arabic page number centred within it.

    cover_pages: number of leading pages (e.g. 1 for the cover) that receive
    an empty overlay — no white box, no number.  Numbering starts at 1 on the
    first non-cover page.
    """
    fonts_dir = docs_dir / "assets" / "fonts"

    def font_uri(filename: str) -> str:
        return (fonts_dir / filename).as_uri()

    # Convert pts → mm for CSS (1pt = 25.4/72 mm)
    w_mm = page_width_pts  * 25.4 / 72
    h_mm = page_height_pts * 25.4 / 72
    # The full @page bottom margin is 25 mm, but the Paged.js @bottom-center
    # counter is vertically centred within it — 9pt text (~3.2 mm) centred in
    # 25 mm sits roughly 11–14 mm from the bottom edge.  Covering only 14 mm
    # erases the baked-in number while leaving the upper part of the margin
    # free for any footnote content that legitimately extends near the bottom.
    bottom_margin_mm = 14

    pages_html: list[str] = []
    for i in range(total_pages):
        if i < cover_pages:
            # Cover page — no white box, no number.
            pages_html.append('<div class="pg"></div>')
        else:
            page_num = i - cover_pages + 1  # Arabic counter starting at 1 after cover
            pages_html.append(
                f'<div class="pg">'
                f'<div class="num-cover">{page_num}</div>'
                f'</div>'
            )

    pages_str = "\n".join(pages_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Page Numbers Overlay</title>
<style>
@font-face {{
  font-family: "Brown";
  src: url("{font_uri('BrownStdRegular.otf')}") format("opentype");
  font-weight: 400;
  font-style: normal;
}}

@page {{
  size: {w_mm:.4f}mm {h_mm:.4f}mm;
  margin: 0;
}}

html, body {{
  margin: 0;
  padding: 0;
}}

/* Each div maps to exactly one PDF page. */
.pg {{
  width: {w_mm:.4f}mm;
  height: {h_mm:.4f}mm;
  position: relative;
  break-after: page;
}}

/* White cover box over the old Paged.js bottom-center number, with the
   correct sequential number centred inside.
   -webkit-print-color-adjust ensures the white background renders in print. */
.num-cover {{
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: {bottom_margin_mm}mm;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Brown", sans-serif;
  font-size: 9pt;
  color: #666;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
</style>
</head>
<body>
{pages_str}
</body>
</html>"""


def _escape(text: str) -> str:
    """Minimal HTML escaping for text content."""
    return (
        text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
