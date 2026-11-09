<div align="center">

<img src="assets/mark-light.svg" alt="Zyvor Pharma QMS" width="64" height="64">

# Zyvor Pharma QMS

**Batch to release for manufacturers.**

[![Status: pilot-ready](https://img.shields.io/badge/status-pilot--ready-0071e3?style=flat-square)](#)
[![Not validated](https://img.shields.io/badge/validation-not%20validated-ff453a?style=flat-square)](#)
[![Not Part 11](https://img.shields.io/badge/Part%2011-not%20claimed-ff9f0a?style=flat-square)](#)
[![Website](https://img.shields.io/badge/Website-0071e3?style=for-the-badge)](https://zyvorai.github.io/zyvor-pharma-qms-site/)

</div>

> [!IMPORTANT]
> **Zyvor Pharma QMS is pilot-ready software, not a validated / Part 11 system.** Use synthetic or non-regulated demonstration data only. Do not use for regulated release decisions without your own validation. Distinct from retail [Zyvora Pharmacy](https://zyvorai.github.io/zyvor-pharma-site/).

This repository is the **public product website**. There is **no application source code** here. The product repository is private.

## What it is

Manufacturing quality management: **batch → laboratory → QA → release / recall**, plus plant ops and **India / US / EU / abroad** market modules (APQR, PV, FAR, QP, serialization, GDP, licences, and more).

- [Website](https://zyvorai.github.io/zyvor-pharma-qms-site/)
- [Try it](https://zyvorai.github.io/zyvor-pharma-qms-site/try/) — native Mac/Windows apps + one-line install
- [Modules](https://zyvorai.github.io/zyvor-pharma-qms-site/modules/)
- [Markets](https://zyvorai.github.io/zyvor-pharma-qms-site/markets/)
- [Pilot](https://zyvorai.github.io/zyvor-pharma-qms-site/pilot/)
- [Intended use](docs/INTENDED-USE.md)

### Try / install (no source)

When a release is published on this repo:

```bash
# Mac / Linux
curl -fsSL https://github.com/zyvorai/zyvor-pharma-qms-site/releases/latest/download/get.sh | sh -s -- up
```

```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm https://github.com/zyvorai/zyvor-pharma-qms-site/releases/latest/download/get.ps1))) up
```

Release assets: `get.sh`, `get.ps1`, `pharma-qms-install.tar.gz`, `SHA256SUMS` (built from the private product tree via `make package-install`). Native apps: `PharmaQMS.app` / `PharmaQMS.exe` from `make desktop-macos` / `make desktop-windows`.

## Contact

sales@zyvor.dev · security@zyvor.dev

## License

Copyright © 2026 ZyvorAI Labs Private Limited. See [LICENSE](LICENSE). Website content only; no application source is published here.
