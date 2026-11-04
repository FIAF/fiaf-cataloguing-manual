### Syntax Guide

Content is written in [Markdown](https://www.markdownguide.org/) and rendered by [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Each section lives in its own `index.md` file under `markdown/`.

**Headings**

Use standard Markdown headings. Top-level section pages start at `##`; subsections nest from there.

Do not use `#` (h1) in markdown files. MkDocs uses the page title from `nav:` in `mkdocs.yml` as the h1 heading — adding one in the file would create a duplicate.

```md
## Section Title

### Subsection Title

#### Subsubsection Title
```

To create an anchor that can be linked to from other pages, place an HTML `id` attribute immediately before the heading:

```md
<a id="sec-my-section"></a>
## My Section
```

**Footnotes**

Footnotes use standard Markdown footnote syntax:

```md
Some text with a footnote.[^1]

[^1]: The footnote text goes here.
```

**Links**

External links use standard Markdown syntax:

```md
[FIAF Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html)
```

Internal links use a path relative to the current page, optionally followed by an anchor. For example, from `markdown/restorations/index.md`:

```md
[Extent of a Manifestation](../manifestations/elements_of_a_manifestation/index.md#sec-extent_of_a_manifestation)
```

Do not start internal page links with `/`. MkDocs leaves absolute `.md` links unprocessed, and a leading slash points to the domain root, which breaks on GitHub Pages, where the site is served from `/fiaf-cataloguing-manual/`.

**Examples**

Examples are rendered as MkDocs Material admonitions:

```md
!!! example "Example"
    Lola rennt (Germany, 1998, Tom Tykwer)
    
    Work identifier: ISAN 0000-0000-606A-0000-0-0000-0000-3
```

**Tables**

Tables use standard Markdown syntax:

```md
| **Column A** | **Column B** | **Column C** |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
```

**Diagrams**

Diagram images are stored in `markdown/diagrams/` (and images in `markdown/images/`). Reference them from the site root:

```html
<center><object data="/diagrams/figure_01.drawio.svg" type="image/svg+xml" width="100%"></object></center>
```

A build hook (`hooks/content_paths.py`) rewrites these root-absolute paths to page-relative paths during the build, so they work on GitHub Pages and do not need to be changed when a page moves.

Standard Markdown images work too: `![Figure 1](/diagrams/figure_01.drawio.svg)`.

Source files for regenerating diagrams are in `scripts/diagrams/`. Contact the manual administrator for the creation of new diagrams.
