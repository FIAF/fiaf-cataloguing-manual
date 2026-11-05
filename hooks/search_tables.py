"""Keep table cells as separate blocks in the search index.

Material's search plugin flattens tables: its HTML parser only records
``p``, ``li``, ``code`` and similar tags as block boundaries, so an entire
table ends up as one block of text in ``search_index.json``. The client-side
search then renders that whole block as the result teaser, which means any hit
inside a table shows the full table, not just the matching row or cell.

Keeping ``td`` and ``th`` makes each cell its own block, so search results
show only the matching cell(s). The tags are stripped again by the search
tokenizer, so matching itself is unchanged.

The search result can contain up to two matched blocks, which the client joins
without a separator. A ``&#x20;`` entity is appended to every cell in the
index so that adjacent cell snippets are separated by a space when rendered.

This hook relies on internals of the pinned Material for MkDocs version.
If the expected parser attribute changes, it leaves the parser untouched
instead of breaking the build.
"""

import json
import os
import re

from material.plugins.search import plugin as search_plugin

_TABLE_CELL_TAGS = {"td", "th"}
_CELL_END_RE = re.compile(r"(?<!&#x20;)</(?:td|th)>")


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
            while (
                context
                and context[-1] != tag
                and getattr(context[-1], "tag", None) not in keep
                and context[-1] not in skip
            ):
                context.pop()
        super().handle_endtag(tag)


if getattr(search_plugin.Parser, "__name__", "") != _TableCellParser.__name__:
    search_plugin.Parser = _TableCellParser


def on_post_build(config):
    """Separate adjacent table-cell snippets with a rendered space."""
    path = os.path.join(config.site_dir, "search", "search_index.json")
    if not os.path.isfile(path):
        return

    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)

    changed = False
    for document in data.get("docs", []):
        text = document.get("text", "")
        if _CELL_END_RE.search(text):
            document["text"] = _CELL_END_RE.sub(
                lambda match: f" &#x20;{match.group(0)}", text
            )
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, separators=(",", ":"), default=str)
