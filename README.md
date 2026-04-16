# FIAF Moving Image Cataloguing Manual

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

A static site build of the [FIAF Moving Image Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html), published at:
https://fiaf-cataloguing-manual.s3-website.fr-par.scw.cloud/

---

## Site setup

The site is built with [MkDocs](https://www.mkdocs.org/) using the [Material theme](https://squidfunk.github.io/mkdocs-material/).

### Directory structure

```
fiaf-cataloguing-manual/
├── markdown/              ← master content — one index.md per section/subsection
│   ├── preliminary/
│   ├── works/
│   ├── variants/
│   ├── manifestations/
│   ├── items/
│   ├── boundaries/
│   ├── agents/
│   ├── events/
│   ├── other-relationships/
│   ├── appendices/
│   │   ├── titles/
│   │   ├── cataloguers-notes/
│   │   ├── aggregates/
│   │   ├── element-comparison/
│   │   ├── rights/
│   │   ├── record-examples/
│   │   ├── bibliography/
│   │   └── element-list/
│   ├── assets/            ← CSS, logo, favicon, PDF scripts
│   └── diagrams/          ← diagram images
├── hooks/
│   ├── heading_numbers.py ← MkDocs hook for auto-numbering headings
│   └── pdf_images.py      ← MkDocs hook for PDF image path handling
├── overrides/
│   └── partials/          ← MkDocs Material theme overrides
├── mkdocs.yml             ← site configuration and navigation
├── compose.yml            ← Docker Compose setup for local preview
└── SYNTAX.md              ← Markdown syntax guide for contributors
```

Each chapter index is `{chapter}/index.md`; subsections are `{chapter}/{slug}/index.md`.

### Local preview

With Docker:

```sh
docker compose up
```

Without Docker:

```sh
pip install mkdocs-material
mkdocs serve
```

The site is served at `http://localhost:8000`.

### Deployment

On every push to the `develop` branch, GitHub Actions builds the site and syncs it to a [Scaleway Object Storage](https://www.scaleway.com/en/object-storage/) bucket in the Paris region using the AWS CLI.

The workflow requires two repository secrets:

| Secret | Description |
| --- | --- |
| `SCW_ACCESS_KEY_ID` | Scaleway API access key ID |
| `SCW_SECRET_ACCESS_KEY` | Scaleway API secret key |

### PDF generation

The site can export an aggregated PDF of the full manual. PDF generation is handled by [mkdocs-exporter](https://adrienbrignon.github.io/mkdocs-exporter/), which renders each page in a headless Chromium browser (via Playwright) and then concatenates them.

#### Running a local PDF build

PDF generation is disabled by default (it adds ~40 s to every build). Enable it by setting the `CI_PDF` environment variable:

```sh
CI_PDF=true mkdocs build
```

The output is written to `site/assets/fiaf-cataloguing-manual.pdf`.

#### How it works

**Renderer**: Playwright/Chromium renders each MkDocs page to PDF. CSS Paged Media properties (page margins, `@page`, `counter(page)`) are not natively supported by Chromium, so mkdocs-exporter bundles **Paged.js** (v0.4.3), a JavaScript polyfill that handles them before the browser takes a screenshot.

**Stylesheets**: `markdown/assets/print.css` is injected as a print stylesheet. It sets page margins, a page-number footer, and all footnote-related rules.

**Scripts**: `markdown/assets/footnotes-preprocess.js` runs before Paged.js processes the document (see below).

**Aggregation**: After all pages are rendered individually, mkdocs-exporter concatenates them into a single PDF at `assets/fiaf-cataloguing-manual.pdf`.

**Table of contents**: `hooks/pdf_toc.py` runs after mkdocs-exporter completes. It counts the pages in each individual section PDF, computes cumulative page numbers, generates a TOC page as a standalone HTML document, renders it to PDF with Playwright, and prepends it to the aggregated PDF. The TOC shows two levels of navigation (chapters and immediate subsections).

#### Footnotes

The Python `footnotes` Markdown extension collects all footnotes into a `<div class="footnote">` block at the end of each page's HTML. Left alone, these would all appear at the end of each section in the PDF rather than at the bottom of the page where each reference appears.

To produce conventional academic footnote layout, two files work together:

**`markdown/assets/footnotes-preprocess.js`** — runs before Paged.js. For each `<sup id="fnref:N">` reference in the body text, it finds the matching `<li id="fn:N">` in the end-of-document footnote block, copies its content into an inline `<span class="pdf-footnote">` placed immediately after the `<sup>`, then removes the original footnote block. Inline `<span>` is used rather than `<li>` to avoid Chrome's block-in-inline splitting, which would create ghost blank lines.

**`markdown/assets/print.css`** — declares `float: footnote` on `.pdf-footnote`, which Paged.js uses to lift each span to the bottom of whichever page it appears on. `span.pdf-footnote` is given `position: absolute; width: 0; height: 0` so its text content does not inflate the paragraph height before Paged.js moves it. `[data-footnote-call]` (a call-marker element inserted by Paged.js) is hidden with `display: none !important` because the original Python-generated `<sup>` already serves as the visible inline reference number.

#### CI

PDF generation runs in CI on pushes to the `288-generate-pdf` branch (and is intended to run on `develop` after the feature is merged). The workflow sets `CI_PDF=true` and uploads the resulting PDF as a build artifact. See `.github/workflows/main.yml`.

---

### Editorial workflow

- Work on feature branches, PR to `develop`
- Edit Markdown files directly in `markdown/`
- Navigation changes require updating `mkdocs.yml`
- Issues are tracked at https://github.com/FIAF/fiaf-cataloguing-manual/issues
