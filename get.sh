#!/bin/sh
# Bootstrap: download the Pharma QMS install bundle and run install.sh.
#   curl -fsSL https://github.com/zyvorai/zyvor-pharma-qms-site/releases/latest/download/get.sh | sh -s -- up
set -eu
BASE="${PHARMA_QMS_RELEASE_BASE:-https://github.com/zyvorai/zyvor-pharma-qms-site/releases/latest/download}"
APP="${PHARMA_QMS_APP_DIR:-$HOME/.zyvor-pharma-qms/app}"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
command -v curl >/dev/null 2>&1 || { echo "curl is required" >&2; exit 1; }
echo "Downloading Zyvor Pharma QMS install bundle (pilot / not Part 11)…"
curl -fsSL "$BASE/pharma-qms-install.tar.gz" -o "$tmp/pharma-qms-install.tar.gz"
curl -fsSL "$BASE/SHA256SUMS" -o "$tmp/SHA256SUMS"
want="$(grep ' pharma-qms-install.tar.gz$' "$tmp/SHA256SUMS" | cut -d' ' -f1)"
if command -v sha256sum >/dev/null 2>&1; then got="$(sha256sum "$tmp/pharma-qms-install.tar.gz" | cut -d' ' -f1)"; else got="$(shasum -a 256 "$tmp/pharma-qms-install.tar.gz" | cut -d' ' -f1)"; fi
[ -n "$want" ] && [ "$want" = "$got" ] || { echo "checksum mismatch: refusing to run" >&2; exit 1; }
rm -rf "$APP"; mkdir -p "$APP"; tar -xzf "$tmp/pharma-qms-install.tar.gz" -C "$APP"
exec "$APP/deploy/install/install.sh" "$@"
