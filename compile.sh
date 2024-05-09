MARKDOWN=$(find markdown -type f -name '*.md' | sort)
pandoc $MARKDOWN --pdf-engine=wkhtmltopdf --css style.css -o manual.pdf 

