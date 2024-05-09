MARKDOWN=$(find markdown -type f -name '*.md' | sort)
pandoc $MARKDOWN --pdf-engine=xelatex -o manual.pdf
