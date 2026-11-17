"""Build a print/PDF edition of the manual from the built MkDocs site.

The PDF is derived from MkDocs' HTML output rather than from the Markdown, so
section numbering, admonitions, footnotes and anchors are exactly what the
website shows. Pipeline:

1. ``mkdocs build`` into a temporary directory (or reuse ``--site-dir``).
2. Rasterise the draw.io diagrams with headless Chromium. Their labels are
   HTML inside ``<foreignObject>``, which only browsers render; non-browser
   engines show "Text is not SVG - cannot display". PNGs are cached by content
   hash in ``pdf/.cache/``.
3. Join the pages in ``nav:`` order into one HTML document, rewriting links
   and ids so they stay unique, and turning footnotes into page-bottom notes.
4. Lay out with WeasyPrint using ``pdf/print.css`` (CSS Paged Media).

This is a standalone script, not a MkDocs plugin, so it only depends on the
generated HTML.

Notes:
- Only pages in ``nav:`` are printed (plus the home page as the Preface).
  Links to other pages are reported and unwrapped.
- Every id is prefixed per page, because ``sec-`` anchors repeat across pages
  (e.g. Work and Variant both define ``sec-country_of_reference``).
- Diagrams are rasterised because a PDF -> SVG vector round trip was tried
  and left black boxes behind draw.io shadows and misplaced glyphs.

Usage:
    python pdf/build_pdf.py                    # 168x240 mm book
    python pdf/build_pdf.py --paper a4
    python pdf/build_pdf.py --html out.html    # also keep the joined HTML
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from bs4 import BeautifulSoup, Comment, NavigableString

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "pdf"
CACHE_DIR = PDF_DIR / ".cache" / "diagrams"
DEFAULT_OUT = PDF_DIR / "out" / "fiaf-cataloguing-manual.pdf"

TITLE = "The FIAF Moving Image Cataloguing Manual"
EDITION = "Second edition"
PUBLISHER = "International Federation of Film Archives (FIAF)"
COMMISSION = "FIAF Cataloguing and Documentation Commission"
LICENSE = "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)"

# Nav groups rendered as unnumbered front matter (roman page numbers).
FRONT_MATTER_GROUPS = {"Dedication", "Acknowledgements"}
# The site home page is not in nav; in print it becomes the preface.
PREFACE = ("Preface", "index.md")

# Device scale for diagram rasters. Diagrams are ~600 CSS px wide and print
# at ~125 mm, so 3x gives roughly 360 dpi.
DIAGRAM_SCALE = 3

PAPER = {
    # 2016 edition trim size
    "book": "@page { size: 168mm 240mm; }",
    "a4": """
        @page { size: A4; margin: 22mm 24mm 24mm 24mm; }
        @page :left { margin-left: 24mm; margin-right: 24mm; }
        html { font-size: 10pt; }
    """,
}

CHROMIUM_CANDIDATES = [
    "chromium",
    "chromium-browser",
    "google-chrome",
    "google-chrome-stable",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


# --------------------------------------------------------------------------
# Navigation


@dataclass
class Page:
    key: str  # unique id prefix in the joined document
    title: str  # nav title
    md: str  # path relative to docs_dir
    group: str | None  # top-level nav group title
    depth: int  # nesting depth in nav (1 = directly under a top-level group)
    first_in_group: bool = False

    @property
    def url(self) -> str:
        """Site-root-relative directory URL, e.g. ``/works/``."""
        return "/" + self.md[: -len("index.md")]

    @property
    def front(self) -> bool:
        return self.group in FRONT_MATTER_GROUPS or self.md == PREFACE[1]


def load_nav() -> list[Page]:
    cfg = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
    pages: list[Page] = []

    def walk(items, depth, group):
        for entry in items:
            ((title, val),) = entry.items()
            if isinstance(val, str):
                pages.append(Page(f"p{len(pages)}", title, val, group, depth))
            else:
                walk(val, depth + 1, group if group is not None else title)

    walk(cfg["nav"], 0, None)
    seen = set()
    for p in pages:
        p.first_in_group = p.group not in seen
        seen.add(p.group)

    # Preface goes after the last front-matter page.
    preface = Page("preface", PREFACE[0], PREFACE[1], PREFACE[0], 1, True)
    last_front = max(i for i, p in enumerate(pages) if p.group in FRONT_MATTER_GROUPS)
    pages.insert(last_front + 1, preface)
    return pages


# --------------------------------------------------------------------------
# Diagrams


def find_chromium(explicit: str | None) -> str | None:
    for cand in [explicit, os.environ.get("CHROMIUM")] + CHROMIUM_CANDIDATES:
        if not cand:
            continue
        found = shutil.which(cand) or (cand if Path(cand).is_file() else None)
        if found:
            return found
    return None


def svg_size(svg: Path) -> tuple[int, int]:
    head = svg.read_text(errors="ignore")[:4000]
    w = re.search(r'\bwidth="([\d.]+)(?:px)?"', head)
    h = re.search(r'\bheight="([\d.]+)(?:px)?"', head)
    if not (w and h):
        raise ValueError(f"{svg.name}: no width/height on root <svg>")
    return round(float(w.group(1))), round(float(h.group(1)))


def rasterise(svg: Path, chromium: str) -> Path:
    digest = hashlib.sha256(svg.read_bytes() + f"@{DIAGRAM_SCALE}".encode()).hexdigest()[:16]
    out = CACHE_DIR / f"{svg.stem}.{digest}.png"
    if out.exists():
        return out
    w, h = svg_size(svg)
    with tempfile.TemporaryDirectory() as td:
        wrapper = Path(td) / "wrap.html"
        wrapper.write_text(
            "<!doctype html><style>html,body{margin:0;background:#fff}"
            f"img{{display:block;width:{w}px;height:{h}px}}</style>"
            f'<img src="{svg.resolve().as_uri()}">'
        )
        tmp_png = Path(td) / "out.png"
        subprocess.run(
            [
                chromium,
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--hide-scrollbars",
                f"--user-data-dir={Path(td) / 'profile'}",
                f"--force-device-scale-factor={DIAGRAM_SCALE}",
                f"--window-size={w},{h}",
                f"--screenshot={tmp_png}",
                wrapper.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
        if not tmp_png.exists():
            raise RuntimeError(f"Chromium produced no image for {svg.name}")
        shutil.move(tmp_png, out)
    return out


def rasterise_all(svgs: list[Path], chromium: str) -> dict[str, Path]:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    result: dict[str, Path] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(rasterise, s, chromium): s for s in svgs}
        for fut in concurrent.futures.as_completed(futures):
            result[futures[fut].name] = fut.result()
    # drop stale cache entries
    keep = set(result.values())
    for f in CACHE_DIR.glob("*.png"):
        if f not in keep:
            f.unlink()
    return result


# --------------------------------------------------------------------------
# Assembly


@dataclass
class Report:
    unresolved_links: list[tuple[str, str]]


def collapse_whitespace(root) -> None:
    """Collapse whitespace runs outside <pre>/<code>.

    Besides being harmless for rendering, this avoids a WeasyPrint line-split
    assertion ("Got ' \\n' between two lines") seen with Python-Markdown output.
    """
    for t in root.find_all(string=True):
        if isinstance(t, Comment) or t.find_parent(["pre", "code"]) is not None:
            continue
        new = re.sub(r"\s+", " ", str(t))
        if new != str(t):
            t.replace_with(NavigableString(new))


def strip_number(text: str) -> str:
    return re.sub(r"^\s*\d+(\.\d+)*\s+", "", text)


def heading_number(text: str) -> str | None:
    m = re.match(r"^\s*(\d+(?:\.\d+)*)\s", text)
    return m.group(1) if m else None


class Assembler:
    def __init__(self, pages: list[Page], site: Path, diagrams: dict[str, Path]):
        self.pages = pages
        self.site = site
        self.diagrams = diagrams
        self.url2key = {p.url: p.key for p in pages}
        self.report = Report([])

    def resolve(self, page: Page, href: str) -> str | None:
        """Map an href to an internal ``#id``; None for external links.

        Returns "" for internal links whose target is not part of the print
        edition (e.g. pages that exist but are not in nav).
        """
        parts = urlsplit(href)
        if parts.scheme or parts.netloc:
            return None
        if not parts.path:
            target = page.url
        else:
            target = posixpath.normpath(posixpath.join(page.url, parts.path))
            target = re.sub(r"/index\.html$", "", target).rstrip("/") + "/"
        key = self.url2key.get(target)
        if key is None:
            return ""
        return f"#{key}-{parts.fragment}" if parts.fragment else f"#{key}"

    def page_article(self, page: Page):
        html_file = self.site / page.url.lstrip("/") / "index.html"
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        art = soup.select_one("article.md-content__inner")
        if art is None:
            raise RuntimeError(f"{html_file}: no article.md-content__inner")
        for junk in art.select(".md-content__button, a.headerlink, .md-source-file"):
            junk.decompose()
        for c in art.find_all(string=lambda s: isinstance(s, Comment)):
            c.extract()
        return soup, art

    def convert_footnotes(self, art) -> None:
        notes = {}
        block = art.select_one("div.footnote")
        if block is None:
            return
        for li in block.select("li[id]"):
            for b in li.select("a.footnote-backref"):
                b.decompose()
            # unwrap a single <p> so the note flows inline
            ps = li.find_all("p", recursive=False)
            if len(ps) == 1:
                ps[0].unwrap()
            notes[li["id"]] = li.decode_contents().strip()
        block.decompose()
        for sup in art.select("sup[id^=fnref]"):
            a = sup.find("a")
            fid = a["href"].lstrip("#") if a and a.has_attr("href") else None
            if fid in notes:
                sup.replace_with(
                    BeautifulSoup(f'<span class="fn">{notes[fid]}</span>', "html.parser")
                )

    def rewrite_links(self, page: Page, soup, art) -> None:
        for el in art.select("[id]"):
            el["id"] = f"{page.key}-{el['id']}"
        for a in art.select("a[href]"):
            href = a["href"]
            target = self.resolve(page, href)
            if target is None:
                a["class"] = a.get("class", []) + ["ext"]
                # print the URL: as a footnote, or inline when already in one
                shown = href.removeprefix("mailto:")
                if a.get_text(strip=True) not in (href, shown):
                    if a.find_parent(class_="fn"):
                        a.insert_after(f" <{shown}>")
                    else:
                        note = soup.new_tag("span", attrs={"class": "fn url"})
                        note.string = shown
                        a.insert_after(note)
            elif target == "":
                self.report.unresolved_links.append((page.md, href))
                a.unwrap()
            else:
                a["href"] = target
                a["class"] = a.get("class", []) + ["xref"]

    def rewrite_images(self, page: Page, soup, art) -> None:
        for obj in art.select("object[data]"):
            img = soup.new_tag("img", attrs={"class": "diagram", "src": obj["data"]})
            obj.replace_with(img)
        for img in art.select("img[src]"):
            src = img["src"]
            if urlsplit(src).scheme:
                continue
            path = posixpath.normpath(posixpath.join(page.url, src)).lstrip("/")
            name = Path(path).name
            if name in self.diagrams:
                img["src"] = self.diagrams[name].as_uri()
            else:
                img["src"] = (self.site / path).as_uri()

    def render_page(self, page: Page) -> tuple[str, str, str | None]:
        """Return (html, toc_title, chapter number) for one nav page."""
        soup, art = self.page_article(page)
        self.convert_footnotes(art)
        self.rewrite_links(page, soup, art)
        self.rewrite_images(page, soup, art)
        collapse_whitespace(art)

        h1 = art.find("h1")
        if h1 is not None and page.md == PREFACE[1]:
            h1.decompose()  # the home page h1 is the site name
            h1 = None
        if h1 is None:
            h1 = soup.new_tag("h1")
            h1.string = page.title
            art.insert(0, h1)
        if page.front:
            for t in h1.find_all(string=True):
                t.replace_with(strip_number(str(t)))
        plain = BeautifulSoup(str(h1), "html.parser")
        for f in plain.select(".fn"):
            f.decompose()
        title = plain.get_text(" ", strip=True)
        h1["data-running"] = title
        return art.decode_contents(), title, heading_number(title)

    def build(self) -> str:
        body: list[str] = []
        toc: list[str] = []
        for page in self.pages:
            inner, title, number = self.render_page(page)
            classes = ["page"]
            chapter_head = ""
            if page.front:
                classes.append("front")
                h1_class, toc_class = "chapter", "toc-chapter"
            elif page.first_in_group:
                classes.append("chapter-start")
                if strip_number(title) == page.group:
                    h1_class, toc_class = "chapter", "toc-chapter"
                else:
                    # e.g. "Preliminary": the nav group has no page of its own,
                    # so give it a chapter heading above its first page.
                    chap_no = number.rsplit(".", 1)[0] if number and "." in number else ""
                    chap_title = f"{chap_no} {page.group}".strip()
                    chapter_head = (
                        f'<h1 class="chapter group" id="{page.key}-group" '
                        f'data-running="{chap_title}">{chap_title}</h1>'
                    )
                    toc.append(f'<li class="toc-chapter"><a href="#{page.key}-group">{chap_title}</a></li>')
                    h1_class, toc_class = "section", "toc-section"
            else:
                h1_class = "section"
                toc_class = "toc-section" if page.depth <= 1 else "toc-subsection"

            inner = re.sub(r"<h1\b", f'<h1 class="{h1_class}"', inner, count=1)
            toc.append(f'<li class="{toc_class}"><a href="#{page.key}">{title}</a></li>')
            body.append(
                f'<section class="{" ".join(classes)}" id="{page.key}">{chapter_head}{inner}</section>'
            )
        return self.document("".join(toc), "".join(body))

    def document(self, toc: str, body: str) -> str:
        version = build_version()
        year = datetime.date.today().year
        return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{TITLE}</title>
<meta name="author" content="{COMMISSION}">
<meta name="description" content="{EDITION}. {version}">
</head><body>
<section class="cover">
  <p class="cover-org">Fédération internationale des archives du film<br>
  International Federation of Film Archives<br>
  Federación Internacional de Archivos Fílmicos</p>
  <h1 class="book-title">{TITLE}</h1>
  <p class="cover-edition">{EDITION}</p>
</section>
<section class="title-page">
  <p class="tp-title">{TITLE}</p>
  <p class="tp-edition">{EDITION}</p>
  <p class="tp-by">{COMMISSION}</p>
</section>
<section class="colophon">
  <p>{TITLE}, {EDITION.lower()}.</p>
  <p>Published by the {PUBLISHER}, {year}.</p>
  <p>Licensed under {LICENSE}.</p>
  <p>The online edition is available at <span class="url-inline">https://fiaf.github.io/fiaf-cataloguing-manual/</span>.
  This PDF is generated from the same source.</p>
  <p class="build">{version}</p>
</section>
<nav class="toc"><h1 class="toc-title">Contents</h1><ol>{toc}</ol></nav>
{body}
</body></html>"""


def build_version() -> str:
    date = datetime.date.today().isoformat()
    try:
        rev = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        return f"Generated {date} from revision {rev}."
    except (OSError, subprocess.CalledProcessError):
        return f"Generated {date}."


# --------------------------------------------------------------------------
# Main


def mkdocs_build(dest: Path) -> None:
    log("Building site with mkdocs ...")
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--quiet", "--site-dir", str(dest)],
        cwd=ROOT, check=True,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("-o", "--output", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--paper", choices=sorted(PAPER), default="book")
    ap.add_argument("--site-dir", type=Path, help="reuse an existing `mkdocs build` output")
    ap.add_argument("--html", type=Path, help="also write the joined print HTML here")
    ap.add_argument("--chromium", help="path to Chromium/Chrome for diagram rendering")
    ap.add_argument(
        "--allow-svg-fallback", action="store_true",
        help="build without Chromium; diagram labels will be missing",
    )
    ap.add_argument("--strict", action="store_true", help="fail on unresolved internal links")
    args = ap.parse_args(argv)

    # imported late: slow, and needs Pango
    from weasyprint import CSS, HTML
    from weasyprint.text.fonts import FontConfiguration

    pages = load_nav()
    svgs = sorted((ROOT / "markdown" / "diagrams").glob("*.svg"))
    chromium = find_chromium(args.chromium)
    diagrams: dict[str, Path] = {}
    if chromium:
        log(f"Rendering {len(svgs)} diagrams with {chromium} (cached in {CACHE_DIR.relative_to(ROOT)}) ...")
        diagrams = rasterise_all(svgs, chromium)
    elif args.allow_svg_fallback:
        log("WARNING: Chromium not found; diagrams will render without labels.")
    else:
        log("ERROR: Chromium/Chrome is needed to render diagram labels. "
            "Install it, pass --chromium PATH, or use --allow-svg-fallback.")
        return 2

    with tempfile.TemporaryDirectory() as td:
        site = args.site_dir.resolve() if args.site_dir else Path(td) / "site"
        if not args.site_dir:
            mkdocs_build(site)
        assembler = Assembler(pages, site, diagrams)
        html = assembler.build()

    for md, href in assembler.report.unresolved_links:
        log(f"WARNING: {md}: link to a page outside the print edition: {href}")
    if args.strict and assembler.report.unresolved_links:
        return 1

    if args.html:
        args.html.parent.mkdir(parents=True, exist_ok=True)
        args.html.write_text(html, encoding="utf-8")

    log(f"Laying out PDF ({args.paper}) ...")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # @font-face rules only load when the same FontConfiguration is passed to
    # the stylesheet and to write_pdf.
    fonts = FontConfiguration()
    HTML(string=html, base_url=str(ROOT)).write_pdf(
        args.output,
        stylesheets=[
            CSS(filename=str(PDF_DIR / "print.css"), font_config=fonts),
            CSS(string=PAPER[args.paper], font_config=fonts),
        ],
        font_config=fonts,
    )
    log(f"Wrote {args.output.relative_to(ROOT) if args.output.is_relative_to(ROOT) else args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
