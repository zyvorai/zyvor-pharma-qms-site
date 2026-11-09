#!/usr/bin/env bash
# Rasterise OG + social-preview + apple-touch from SVGs.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/gen-graphics.py
command -v rsvg-convert >/dev/null || { echo "rsvg-convert required (brew install librsvg)" >&2; exit 1; }
rsvg-convert -w 1200 -h 630 assets/og.svg -o assets/og.png
rsvg-convert -w 1280 -h 640 docs/assets/social-preview.svg -o docs/assets/social-preview.png
# Apple touch from mark
rsvg-convert -w 180 -h 180 assets/mark-light.svg -o assets/apple-touch-icon.png
echo "rasterised assets/og.png docs/assets/social-preview.png assets/apple-touch-icon.png"
file assets/og.png docs/assets/social-preview.png
