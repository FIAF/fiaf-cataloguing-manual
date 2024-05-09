

# curl -O https://font.download/dl/font/brownstd.zip
# unzip -n brownstd.zip -d brownstd
# mkdir -p ~/.fonts/brownstd
# cp -r brownstd ~/.fonts/brownstd


MARKDOWN=$(find markdown -type f -name '*.md' | sort)
pandoc $MARKDOWN --pdf-engine=xelatex -o manual.pdf --template=config.tex

# pandoc $MARKDOWN --pdf-engine=xelatex -o manual.pdf
