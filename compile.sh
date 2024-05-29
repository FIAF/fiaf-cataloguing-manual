#!/bin/bash

# pull font if required.

if [ ! -d "brownstd" ]; then
    echo "pulling font..."
    curl -O https://font.download/dl/font/brownstd.zip
    unzip -n brownstd.zip -d brownstd
    mkdir -p ~/.fonts/brownstd
    cp -r brownstd ~/.fonts/brownstd
fi

# render diagrams.

npm install puppeteer
npm install d3@6
node render.js


# render pdf.

echo "building pdf..."
MARKDOWN=$(find markdown -type f -name '*.md' | sort)
pandoc $MARKDOWN --pdf-engine=xelatex -o manual.pdf --template=config.tex
echo "finished."
