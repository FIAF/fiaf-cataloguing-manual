"""
MkDocs hook: inject hierarchical section numbers into all headings.

Manual chapters are numbered 1–9 (Preliminary = 1, Other Relationships = 9).
Appendix groups are lettered A, B, C, ...

On each page:
  h1  → chapter number (with trailing period for top-level pages)
                                 e.g.  "1."  or  "A."
                                 but   "1.1" on a sub-section index page
  h2  → chapter.section         e.g.  "1.1"
  h3  → chapter.section.sub     e.g.  "1.1.1"
  h4  → chapter.section.sub.sub e.g.  "1.1.1.1"

Special case — top-level chapter index pages (h1 = "2.", "A.", …):
  These pages have nav sub-pages numbered 2.1, 2.2, … which would collide
  with h2 headings numbered from the same base.  To avoid the collision,
  h2–h4 on top-level index pages use ".0" as an inserted level:
    h2  → chapter.0.section      e.g.  "2.0.1"
    h3  → chapter.0.section.sub  e.g.  "2.0.1.3"
  Sub-pages (chapter = "2.1") are unaffected and use the normal scheme.

For the website, numbers are prepended inside the heading tag as a
<span class="section-number">.

For the PDF, on_page_content injects numbers into the Markdown-rendered HTML
fragment (h2–h4) before the template wraps it and before mkdocs-exporter
captures page.html.  on_page_context prepends the chapter number to page.title
so the Material theme renders the h1 with the number included.

Source markdown is never modified.
"""

import re
from mkdocs.structure.nav import Section

# Populated in on_config; maps src_path → chapter string e.g. "1", "2.3", "A"
_page_numbers: dict[str, str] = {}

# Populated in on_config; maps nav section title → chapter string e.g. "0", "1", "A"
_nav_labels: dict[str, str] = {}


def _assign(pages: list, chapter: str) -> None:
    """Walk a section's page list and assign chapter numbers, skipping duplicates."""
    sub = 0
    for item in pages:
        if isinstance(item, str):
            # Unlabeled entry — this is the section index page (e.g. "works/index.md").
            # Assign the bare chapter number without incrementing sub, so it doesn't
            # consume a sub-section slot.
            if item not in _page_numbers:
                _page_numbers[item] = chapter
        elif isinstance(item, dict):
            _, value = next(iter(item.items()))
            if isinstance(value, str) and value not in _page_numbers:
                # Leaf page with a nav label — assign the next sub-section number.
                sub += 1
                _page_numbers[value] = f"{chapter}.{sub}"
            elif isinstance(value, list):
                # Nested section — recurse with the next sub-section number.
                sub += 1
                _assign(value, f"{chapter}.{sub}")


def on_config(config):
    global _page_numbers, _nav_labels
    _page_numbers = {}
    _nav_labels = {}

    for top_item in config.get("nav", []):
        if not isinstance(top_item, dict):
            continue
        label, value = next(iter(top_item.items()))

        if label == "Home" and isinstance(value, list):
            chapter_num = 1
            appendix_idx = 0
            for section_item in value:
                if not isinstance(section_item, dict):
                    continue
                section_label, section_pages = next(iter(section_item.items()))
                if not isinstance(section_pages, list):
                    continue
                if section_label == "Appendices":
                    for appendix_item in section_pages:
                        if not isinstance(appendix_item, dict):
                            continue
                        appendix_label, appendix_pages = next(iter(appendix_item.items()))
                        if isinstance(appendix_pages, list):
                            letter = chr(ord("A") + appendix_idx)
                            _assign(appendix_pages, letter)
                            _nav_labels[appendix_label] = letter
                            appendix_idx += 1
                elif section_label in ['Dedication', 'Acknowledgements', 'Introduction']:
                    # Front-matter sections — not part of the numbered chapter sequence.
                    pass
                else:
                    _assign(section_pages, str(chapter_num))
                    _nav_labels[section_label] = str(chapter_num)
                    chapter_num += 1

    return config


def on_nav(nav, **kwargs):
    """Prefix sidebar section titles with their chapter/appendix number."""

    def _prefix(items):
        for item in items:
            if isinstance(item, Section) and item.title in _nav_labels:
                num = _nav_labels[item.title]
                item.title = f"{num}. {item.title}"
            if hasattr(item, "children") and item.children:
                _prefix(item.children)

    _prefix(nav.items)
    return nav


def on_page_context(context, page, config, nav, **kwargs):
    """Prepend chapter number to page.title so the Material h1 renders with the number.

    This fires before the template is rendered and before page.html is set,
    so both the website h1 and the PDF h1 (captured by mkdocs-exporter from
    page.html) will include the section number.
    """
    chapter = _page_numbers.get(page.file.src_path.replace("\\", "/"))
    if not chapter:
        return context

    is_top_level = "." not in chapter
    number = chapter + "." if is_top_level else chapter

    # Avoid double-prepending on hot-reload rebuilds.
    if not page.title.startswith(number):
        page.title = f"{number} {page.title}"

    return context


def on_page_content(html: str, page, config, **kwargs) -> str:
    """Inject section numbers into h2–h4 in the Markdown-rendered HTML fragment.

    This fires before the page template is applied and before page.html is set,
    so mkdocs-exporter (which captures page.html in on_post_page at priority 100)
    will always see the numbered headings in the PDF.

    Top-level chapter index pages (those assigned a bare chapter number with no
    dot, e.g. "2" or "A") use a ".0" infix so their h2–h4 numbers ("2.0.1",
    "2.0.2") do not collide with the nav-assigned sub-page numbers ("2.1", "2.2").
    """
    chapter = _page_numbers.get(page.file.src_path.replace("\\", "/"))
    if not chapter:
        return html

    # Top-level chapter index pages (chapter = "2", "9", "A", etc.) use "chapter.0"
    # as the effective prefix for h2–h4 headings (e.g. "9.0.1", "9.0.2") so they
    # don't collide with the nav-assigned sub-page numbers ("9.1", "9.2", …).
    if "." not in chapter:
        chapter = chapter + ".0"

    h2 = h3 = h4 = 0

    def replace_heading(m):
        nonlocal h2, h3, h4
        tag, attrs, content = m.group(1), m.group(2), m.group(3)

        if tag == "h2":
            h2 += 1
            h3 = 0
            h4 = 0
            number = f"{chapter}.{h2}"
        elif tag == "h3":
            h3 += 1
            h4 = 0
            number = f"{chapter}.{h2}.{h3}"
        elif tag == "h4":
            h4 += 1
            number = f"{chapter}.{h2}.{h3}.{h4}"
        else:
            return m.group(0)

        span = f'<span class="section-number">{number}</span> '
        return f"<{tag}{attrs}>{span}{content}</{tag}>"

    return re.sub(r"<(h[2-4])([^>]*)>(.*?)</\1>", replace_heading, html, flags=re.DOTALL)
