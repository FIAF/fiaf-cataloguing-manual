#!/bin/bash
set -e
pip install mkdocs-material
cd /app/mkdocs
mkdocs serve --dev-addr 0.0.0.0:8000
