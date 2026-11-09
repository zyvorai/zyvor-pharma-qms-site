#!/usr/bin/env bash
# Static sanity checks for the Pharma QMS marketing site.
set -euo pipefail
cd "$(dirname "$0")/.."
need=(index.html site.css site.js theme.js robots.txt sitemap.xml LICENSE README.md
  modules/index.html markets/index.html pilot/index.html deploy/index.html security/index.html contact/index.html
  assets/mark-light.svg assets/mark-dark.svg assets/og.png docs/INTENDED-USE.md)
for f in "${need[@]}"; do
  test -f "$f" || { echo "missing $f" >&2; exit 1; }
done
# Must state honest limits on the home page
grep -q 'Not Part 11' index.html
grep -q 'not a validated' index.html || grep -qi 'Not validated' index.html
grep -q 'Zyvora Pharmacy' index.html
# Must not ship application source
! find . -name 'go.mod' -o -name 'Dockerfile' -o -path './backend/*' | grep -q .
echo "site-check ok"
