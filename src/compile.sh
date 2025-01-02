#!/bin/bash

# collect markdown files.
MARKDOWN=$(find markdown -type f -name 'en.md' | sort)

# render pdf.
pandoc $MARKDOWN --pdf-engine=xelatex -o /render/manual_en.pdf
