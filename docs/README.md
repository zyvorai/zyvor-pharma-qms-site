# Docs — Zyvor Pharma QMS (public site)

| Doc | What it is |
|---|---|
| [INTENDED-USE.md](INTENDED-USE.md) | Boundary statement: pilot only, not Part 11 / Annex 11, synthetic data only |
| [assets/social-preview.png](assets/social-preview.png) | Social preview image for docs / GitHub |

## On the website

- [Home](https://zyvorai.github.io/zyvor-pharma-qms-site/)
- [Try it](https://zyvorai.github.io/zyvor-pharma-qms-site/try/), including the [live demo](https://pharma.zyvor.dev) (shared, read-only, synthetic data)
- [Modules](https://zyvorai.github.io/zyvor-pharma-qms-site/modules/) (84 catalogue entries: 73 modules + 11 AI assistants, release v0.1.0)
- [Markets](https://zyvorai.github.io/zyvor-pharma-qms-site/markets/)
- [Pilot](https://zyvorai.github.io/zyvor-pharma-qms-site/pilot/)
- [Deploy](https://zyvorai.github.io/zyvor-pharma-qms-site/deploy/)
- [Security](https://zyvorai.github.io/zyvor-pharma-qms-site/security/)

## Printable PDFs

See [`../resources/`](../resources/) — executive, pilot, modules, markets, security, architecture, IT Q&A.

## Regenerating graphics

```bash
./scripts/render-social.sh          # SVGs + og.png + social-preview.png
node scripts/build-pdfs.mjs         # resources/*.pdf from resources/src
./scripts/site-check.sh
```
