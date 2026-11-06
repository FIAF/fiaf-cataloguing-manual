"""Keep table cells as separate blocks in the search index.

Material's search plugin flattens tables: its HTML parser only records
``p``, ``li``, ``code`` and similar tags as block boundaries, so an entire
table ends up as one block of text in ``search_index.json``. The client-side
search then renders that whole block as the result teaser, which means any hit
inside a table shows the full table, not just the matching row or cell.

Keeping ``td`` and ``th`` makes each cell its own block, so search results
show only the matching cell(s). After indexing, non-empty cells are wrapped in
``div`` tags: unlike bare table-cell tags, these are valid in search previews
and keep adjacent snippets separate. Empty cells are removed.

This hook relies on internals of the pinned Material for MkDocs version.
If the expected parser attribute changes, it leaves the parser untouched
instead of breaking the build.
"""

import json
import os
import re
from html import unescape

from material.plugins.search import plugin as search_plugin

_TABLE_CELL_TAGS = {"td", "th"}
_CELL_RE = re.compile(r"<(?P<tag>td|th)>(?P<content>.*?)</(?P=tag)>", re.DOTALL)
_TAG_RE = re.compile(r"<[^>]*>")


class _TableCellParser(search_plugin.Parser):
    """Search parser that keeps table cell boundaries in the indexed text."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        keep = getattr(self, "keep", None)
        if isinstance(keep, set):
            keep.update(_TABLE_CELL_TAGS)

    def handle_endtag(self, tag):
        # Pages can contain unclosed inline tags, e.g. the colour <span>s in
        # example_two. Material's parser leaves those on its context stack, so
        # a later </p> is ignored and everything after it becomes one giant
        # search block. Drop unclosed non-block tags before closing a block.
        context = getattr(self, "context", None)
        keep = getattr(self, "keep", ())
        skip = getattr(self, "skip", ())
        if context is not None and tag in keep:
            # Find the matching opener before changing anything. A stray
            # closing tag must not discard unrelated enclosing elements.
            for index in range(len(context) - 1, -1, -1):
                element = context[index]
                if element in skip:
                    break
                if element == tag:
                    del context[index + 1:]
                    break
                if getattr(element, "tag", None) in keep:
                    break
        super().handle_endtag(tag)


if getattr(search_plugin.Parser, "__name__", "") != _TableCellParser.__name__:
    search_plugin.Parser = _TableCellParser


def on_post_build(config):
    """Use valid preview blocks for non-empty cells; discard empty ones."""
    path = os.path.join(config.site_dir, "search", "search_index.json")
    if not os.path.isfile(path):
        return

    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)

    changed = False
    for document in data.get("docs", []):
        text = document.get("text", "")
        if _CELL_RE.search(text):
            def replace_cell(match):
                content = match.group("content")
                if not unescape(_TAG_RE.sub("", content)).strip():
                    return ""
                return f"<div>{content}</div>"

            document["text"] = _CELL_RE.sub(replace_cell, text)
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, separators=(",", ":"), default=str)
