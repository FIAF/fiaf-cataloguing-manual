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
│   │   ├── value-lists/
│   │   ├── aggregates/
│   │   ├── element-comparison/
│   │   ├── rights/
│   │   ├── record-examples/
│   │   ├── bibliography/
│   │   └── element-list/
│   ├── assets/            ← CSS, logo, favicon
│   └── diagrams/          ← diagram images
├── scripts/
│   └── diagrams/          ← Python scripts that generate diagram images
├── hooks/
│   └── heading_numbers.py ← MkDocs hook for auto-numbering headings
├── overrides/
│   └── partials/          ← MkDocs Material theme overrides (logo.html)
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

### Editorial workflow

- Work on feature branches, PR to `develop`
- Edit Markdown files directly in `markdown/`
- Navigation changes require updating `mkdocs.yml`
- Issues are tracked at https://github.com/FIAF/fiaf-cataloguing-manual/issues
