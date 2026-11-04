"""Rewrite root-absolute content URLs to document-relative URLs.

Content in this repository uses root-absolute paths such as
``/diagrams/figure_01.drawio.svg``. Those work when the site is served from a
domain root, but break when it is served from a subpath, such as a GitHub Pages
project site at ``/fiaf-cataloguing-manual/``.

This hook rewrites root-absolute ``href``, ``src`` and ``data`` attributes in
rendered page content to paths relative to the current page. The same build
then works at a domain root and under any subpath.
"""

import re

_ATTR_RE = re.compile(r'\b(href|src|data)=(["\'])/(?!/)')


def _relative_prefix(page):
    """Return the prefix that resolves from the page to the site root."""
    page_dir = page.url.rsplit("/", 1)[0]
    depth = len([part for part in page_dir.split("/") if part])
    return "../" * depth or "./"


def on_page_content(html, page, config, files):
    prefix = _relative_prefix(page)
    return _ATTR_RE.sub(lambda m: f"{m.group(1)}={m.group(2)}{prefix}", html)
