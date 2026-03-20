"""
MkDocs hook: inject hierarchical section numbers into all headings.

Manual chapters are numbered 0–8 (Preliminary = 0).
Appendix groups are lettered A, B, C, ...

On each page:
  h1  → chapter number (with trailing period for top-level pages)
                                 e.g.  "1."  or  "A."
                                 but   "1.1" on a sub-section index page
  h2  → chapter.section         e.g.  "1.1"
  h3  → chapter.section.sub     e.g.  "1.1.1"
  h4  → chapter.section.sub.sub e.g.  "1.1.1.1"

Numbers are prepended inside the heading tag as a <span class="section-number">.
Source markdown is never modified.
"""

import re

# Populated in on_config; maps src_path → chapter string e.g. "0", "1", "A"
_page_numbers: dict[str, str] = {}

# Populated in on_config; maps nav section title → chapter string e.g. "0", "1", "A"
_nav_labels: dict[str, str] = {}


def _assign(pages: list, chapter: str) -> None:
    """Walk a section's page list and assign chapter numbers, skipping duplicates."""
    sub = 0
    for item in pages:
        if isinstance(item, str):
            # Unlabeled entry — section index page
            if item not in _page_numbers:
                _page_numbers[item] = chapter
        elif isinstance(item, dict):
            _, value = next(iter(item.items()))
            if isinstance(value, str) and value not in _page_numbers:
                sub += 1
                _page_numbers[value] = f"{chapter}.{sub}"
            elif isinstance(value, list):
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
            chapter_num = 0
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
                else:
                    _assign(section_pages, str(chapter_num))
                    _nav_labels[section_label] = str(chapter_num)
                    chapter_num += 1

    return config


def on_nav(nav, config, files):
    from mkdocs.structure.nav import Section

    def _prefix(items):
        for item in items:
            if isinstance(item, Section) and item.title in _nav_labels:
                num = _nav_labels[item.title]
                item.title = f"{num}. {item.title}"
            if hasattr(item, "children") and item.children:
                _prefix(item.children)

    _prefix(nav.items)
    return nav


def on_post_page(output: str, page, config, **kwargs) -> str:
    chapter = _page_numbers.get(page.file.src_path.replace("\\", "/"))
    if not chapter:
        return output

    h2 = h3 = h4 = 0

    def replace_heading(m):
        nonlocal h2, h3, h4
        tag, attrs, content = m.group(1), m.group(2), m.group(3)

        if tag == "h1":
            number = chapter + "." if "." not in chapter else chapter
        elif tag == "h2":
            h2 += 1; h3 = 0; h4 = 0
            number = f"{chapter}.{h2}"
        elif tag == "h3":
            h3 += 1; h4 = 0
            number = f"{chapter}.{h2}.{h3}"
        elif tag == "h4":
            h4 += 1
            number = f"{chapter}.{h2}.{h3}.{h4}"
        else:
            return m.group(0)

        span = f'<span class="section-number">{number}</span> '
        return f"<{tag}{attrs}>{span}{content}</{tag}>"

    return re.sub(r"<(h[1-4])([^>]*)>(.*?)</\1>", replace_heading, output, flags=re.DOTALL)
