#!/bin/bash

# pull font if required.

if [ ! -d "brownstd" ]; then
    echo "pulling font..."
    curl -O https://font.download/dl/font/brownstd.zip
    unzip -n brownstd.zip -d brownstd
    mkdir -p ~/.fonts/brownstd
    cp -r brownstd ~/.fonts/brownstd
fi

# render mermaid.

# mmdc -i mermaid/e.5.1.1/en.mmd -o mermaid/e.5.1.1/en.svg  --width 800 -c ~/.config/mermaid/config.json


# pandoc -i mermaid/e.5.1.1/test.html --pdf-engine=xelatex -o manual.pdf --template=config.tex
npm install jsdom
npm install d3@6
npm install puppeteer
npm install fontfaceobserver

node diagrams/E.5.1.1/en.js


# maybe do a svg conversion here?

# render pdf.

echo "building pdf..."
MARKDOWN=$(find markdown -type f -name '*.md' | sort)
pandoc $MARKDOWN --pdf-engine=xelatex -o manual.pdf --template=config.tex
# pandoc $MARKDOWN --pdf-engine=wkhtmltopdf -o manual.pdf --pdf-engine-opt=--enable-local-file-access

# echo "finished."


# {
#   "flowchart": {
#     "useMaxWidth": false,
#     "htmlLabels": false
#   }
# }

# mmdc -i mermaid/e.5.1.1/en.mmd -o mermaid/e.5.1.1/en.svg -c ~/.config/mermaid/config.json

# mmdc -c ~/.config/mermaid/config.json
