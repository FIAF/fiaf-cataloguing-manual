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

Internal links reference the site path and anchor:

```md
[Extent of a Manifestation](/manifestations/elements_of_a_manifestation/#sec-extent_of_a_manifestation)
```

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

Diagram images are stored in `markdown/diagrams/` and inserted with standard Markdown image syntax:

```md
![Figure 1](/diagrams/figure_01.png)
```

Source files for regenerating diagrams are in `scripts/diagrams/`. Contact the manual administrator for the creation of new diagrams.
