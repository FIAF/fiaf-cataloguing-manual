"""Map legacy example color categories to accessible, theme-aware styles.

The worked examples share a color legend across many tables. Normalize their
old inline named colors at render time without changing the source data or the
association between each legend entry and its matching cells.
"""

import re

_COLOR_SPAN = re.compile(r'<span\s+style="color:\s*([a-zA-Z]+)\s*;?\s*">')
_COLORS = {"blue", "brown", "turquoise", "purple", "orange", "grey", "magenta", "green", "pink"}


def on_page_content(html, page, config, files):
    if not page.file.src_uri.startswith("appendices/record-examples/"):
        return html

    def replace(match):
        color = match[1].lower()
        if color not in _COLORS:
            return match[0]
        return f'<span class="example-color--{color}">'

    return _COLOR_SPAN.sub(replace, html)
