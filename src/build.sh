#!/bin/bash

DEBIAN_FRONTEND=noninteractive

apt update

apt install -y pandoc texlive-xetex fonts-firacode

cp -r /app/src/font/ /usr/share/fonts/BrownStd

cp -r /app/markdown /app/src/markdown

MARKDOWN_EN=$(find /app/src/markdown -type f -name 'en.md' | sort)

pandoc --number-sections --pdf-engine=xelatex $MARKDOWN_EN -o /app/src/manual.pdf --include-in-header=/app/src/config.tex

rm -r /app/src/markdown
