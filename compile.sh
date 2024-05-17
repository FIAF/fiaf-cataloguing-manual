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


# npm install jsdom
# npm install d3@6
# node diagrams/E.5.1.1/en.js

node render.js
# gm convert ./diagrams/1.1/en.svg -resize 500x ./diagrams/1.1/en.png


# render pdf.

echo "building pdf..."
MARKDOWN=$(find markdown -type f -name '*.md' | sort)
pandoc $MARKDOWN --pdf-engine=xelatex -o manual.pdf --template=config.tex
echo "finished."
