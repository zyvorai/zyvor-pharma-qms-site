#!/usr/bin/env bash
# Static sanity checks for the Pharma QMS marketing site.
set -euo pipefail
cd "$(dirname "$0")/.."
need=(index.html site.css site.js theme.js robots.txt sitemap.xml LICENSE README.md
  modules/index.html markets/index.html pilot/index.html deploy/index.html security/index.html contact/index.html
  try/index.html get.sh get.ps1
  assets/mark-light.svg assets/mark-dark.svg assets/og.png assets/og.svg
  assets/banner-light.svg assets/banner-dark.svg
  assets/architecture-light.svg assets/architecture-dark.svg
  assets/security-light.svg assets/security-dark.svg
  assets/capabilities-light.svg assets/capabilities-dark.svg
  docs/INTENDED-USE.md docs/README.md docs/assets/social-preview.png
  resources/PharmaQMS-Executive-overview.pdf
  resources/PharmaQMS-Pilot-guide.pdf
  resources/PharmaQMS-Module-guide.pdf
  resources/PharmaQMS-Markets-India-US-EU.pdf
  resources/PharmaQMS-Security-and-honest-limits.pdf
  resources/PharmaQMS-Architecture-and-deployment.pdf
  resources/PharmaQMS-IT-and-security-questions.pdf)
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
