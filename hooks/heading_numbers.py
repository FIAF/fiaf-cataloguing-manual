"""Style generated heading numbers after Markdown has established IDs and TOC."""

import re

from mkdocs.plugins import event_priority

_HEADING_NUMBER = re.compile(r'(<h[1-6]\b[^>]*>)(\d+(?:\.\d+)*)(\s+)')


@event_priority(-50)
def on_page_content(html, page, config, files):
    plugin = config.plugins.get("nav-numbering")
    number = plugin.page_numbers.get(page.file.src_uri) if plugin else None
    if not number:
        return html

    def wrap(match):
        prefix = match[2]
        if prefix != number and not prefix.startswith(number + "."):
            return match[0]
        return f'{match[1]}<span class="section-number">{prefix}</span>{match[3]}'

    return _HEADING_NUMBER.sub(wrap, html)
