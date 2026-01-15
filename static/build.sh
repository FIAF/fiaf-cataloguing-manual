#!/bin/bash

DEBIAN_FRONTEND=noninteractive

apt update

apt install -y wget

wget -O hugo.deb https://github.com/gohugoio/hugo/releases/download/v0.152.2/hugo_extended_0.152.2_linux-amd64.deb

dpkg -i hugo.deb

hugo version

hugo new site /manual --format=yaml

cd /manual

apt install -y git

git init

git submodule add https://github.com/imfing/hextra.git themes/hextra

cp /app/static/hugo.yml /manual/hugo.yaml

cp /app/static/custom.css /manual/public/css/custom.css

cp -r /app/static/content/ /manual/

hugo server --buildDrafts --disableFastRender --bind 0.0.0.0
