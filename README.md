# FIAF Moving Image Cataloguing Manual

A work-in-progress static site build of the [FIAF Moving Image Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html).

The current branch is building and publishing a live preview at:
**https://fiaf-cataloguing-manual-mkdocs.s3-website.fr-par.scw.cloud/**

---

## Site setup

The site is built with [MkDocs](https://www.mkdocs.org/) using the [Material theme](https://squidfunk.github.io/mkdocs-material/).

### Directory structure

| Path | Purpose |
| --- | --- |
| `markdown/` | Master content — one `index.md` per section/subsection |
| `mkdocs.yml` | Site configuration and navigation |
| `markdown/assets/` | CSS, logo, and favicon |
| `markdown/diagrams/` | Diagram images |
| `source_pdf_markdown/` | Original LaTeX/Markdown hybrid source (migration input only) |
| `scripts/` | Migration and diagram generation tools |

Content is organised into chapter directories under `markdown/`:

```
preliminary/   works/       variants/      manifestations/   items/
boundaries/    agents/      events/        other-relationships/
appendices/titles/          appendices/cataloguers-notes/
appendices/value-lists/     appendices/aggregates/
appendices/element-comparison/  appendices/rights/
appendices/record-examples/ appendices/bibliography/
appendices/element-list/
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

### Content migration

The `markdown/` directory was generated from `source_pdf_markdown/` using the conversion script. To regenerate:

```sh
python3 scripts/convert_mkdocs_content.py
```

This overwrites all files in `markdown/`. Edit the source files in `markdown/` directly for ongoing content work — the conversion script is only needed if re-migrating from the LaTeX source.

### Deployment

On every push to the `181-static-site` branch, GitHub Actions builds the site and syncs it to a [Scaleway Object Storage](https://www.scaleway.com/en/object-storage/) bucket in the Paris region using the AWS CLI.

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
