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
from mkdocs.structure.nav import Section

# Populated in on_config; maps src_path → chapter string e.g. "0", "1", "A"
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
                # Duplicates (already assigned paths) are silently skipped without
                # incrementing sub, so numbering stays contiguous.
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

        # The entire manual lives under the "Home" nav entry in mkdocs.yml.
        # All chapter and appendix sections are direct children of it.
        if label == "Home" and isinstance(value, list):
            chapter_num = 1
            appendix_idx = 0
            for section_item in value:
                if not isinstance(section_item, dict):
                    continue
                section_label, section_pages = next(iter(section_item.items()))
                if not isinstance(section_pages, list):
                    continue
                # "Appendices" is a special grouping section in mkdocs.yml whose
                # children are the individual appendix groups (A, B, C, ...).
                if section_label == "Appendices":
                    for appendix_item in section_pages:
                        if not isinstance(appendix_item, dict):
                            continue
                        appendix_label, appendix_pages = next(iter(appendix_item.items()))
                        if isinstance(appendix_pages, list):
                            letter = chr(ord("A") + appendix_idx)
                            _assign(appendix_pages, letter)
                            # Record the label so on_nav can prefix it in the sidebar.
                            _nav_labels[appendix_label] = letter
                            appendix_idx += 1
                elif section_label in ['Dedication', 'Acknowledgements', 'Introduction']:
                    pass
                else:
                    # Regular chapter — numbered from 0 (Preliminary) upwards.
                    _assign(section_pages, str(chapter_num))
                    # Record the label so on_nav can prefix it in the sidebar.
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
            # Recurse into sub-sections regardless, so nested groups are also visited.
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
            # Top-level chapter pages get a trailing period ("1.", "A.").
            # Sub-section index pages already have a dot in their chapter string
            # (e.g. "1.1") so no period is added.
            is_top_level = "." not in chapter
            number = chapter + "." if is_top_level else chapter
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
