#!/bin/bash

# copy markdown files locally for inclusion in docker container.
cp -r ../markdown ./

# create render dir.
mkdir -p ./render

# # render de pdf.
# MARKDOWN_DE=$(find markdown -type f -name 'de.md' | sort)
# pandoc $MARKDOWN_DE --pdf-engine=xelatex -o ./render/manual_de.pdf --template=config.tex

# render en pdf.
MARKDOWN_EN=$(find markdown -type f -name 'en.md' | sort)
# pandoc $MARKDOWN_EN --pdf-engine=xelatex -o ./render/manual_en.pdf --template=config.tex

pandoc --self-contained --lua-filter ./pikchr.lua --pdf-engine=xelatex $MARKDOWN_EN -o ./render/manual_en.pdf --include-in-header=config.tex


# # render es pdf.
# MARKDOWN_ES=$(find markdown -type f -name 'es.md' | sort)
# pandoc $MARKDOWN_ES --pdf-engine=xelatex -o ./render/manual_es.pdf --template=config.tex

# # render en pdf.
# MARKDOWN_FR=$(find markdown -type f -name 'fr.md' | sort)
# pandoc $MARKDOWN_FR --pdf-engine=xelatex -o ./render/manual_fr.pdf --template=config.tex

# # render en pdf.
# MARKDOWN_HR=$(find markdown -type f -name 'hr.md' | sort)
# pandoc $MARKDOWN_HR --pdf-engine=xelatex -o ./render/manual_hr.pdf --template=config.tex
