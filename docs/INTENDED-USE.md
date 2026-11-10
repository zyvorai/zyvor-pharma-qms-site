# Intended use — Zyvor Pharma QMS

**Pilot electronic records for pharmaceutical manufacturers.** Not a validated system. Not 21 CFR Part 11 / EU GMP Annex 11 / WHO computerized-systems certified.

## Intended

- Evaluate batch → laboratory → QA → release workflows with **synthetic or non-regulated demonstration data**
- Explore India / US / EU / abroad **market module stubs** (APQR, PV, FAR, QP, serialization, GDP, licences, …)
- Self-host on compose, FluxVM, k3s or Windows/WSL for an internal pilot
- Evaluate document control, training, workflow reminders, trends/SPC, equipment/PM and the supplier portal with demonstration data
- Run with **strict authentication** (password + optional TOTP) for an internal pilot; the default demo mode trusts client identity headers and is for synthetic data only
- Try **propose-only AI drafts** (deviation, CAPA, OOS, CoA, etc.) that a person must accept — never auto-release

## Not intended

- Regulated batch release decisions without the customer’s own validation programme
- Live regulatory gateway filing (CDSCO, FDA ESG, EMVS, E2B)
- Retail pharmacy operations (see [Zyvora Pharmacy](https://zyvorai.github.io/zyvor-pharma-site/))
- Any claim of GMP, Part 11, Annex 11 or Schedule M compliance by the software alone
- Treating the hash-chained audit trail or re-authenticated signatures as a Part 11 / Annex 11 compliance claim
- Any claim that AI drafts are validated, accurate, or may act without a named human review

## Evidence

Module counts and market coverage are taken from the product’s own feature catalogue APIs. This website publishes **no application source code**.
