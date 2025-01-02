#!/bin/bash

# render de pdf.
MARKDOWN_DE=$(find markdown -type f -name 'de.md' | sort)
pandoc $MARKDOWN_DE --pdf-engine=xelatex -o /render/manual_de.pdf

# render en pdf.
MARKDOWN_EN=$(find markdown -type f -name 'en.md' | sort)
pandoc $MARKDOWN_EN --pdf-engine=xelatex -o /render/manual_en.pdf

# render es pdf.
MARKDOWN_ES=$(find markdown -type f -name 'es.md' | sort)
pandoc $MARKDOWN_ES --pdf-engine=xelatex -o /render/manual_es.pdf

# render en pdf.
MARKDOWN_FR=$(find markdown -type f -name 'fr.md' | sort)
pandoc $MARKDOWN_FR --pdf-engine=xelatex -o /render/manual_fr.pdf

# render en pdf.
MARKDOWN_HR=$(find markdown -type f -name 'hr.md' | sort)
pandoc $MARKDOWN_HR --pdf-engine=xelatex -o /render/manual_hr.pdf
