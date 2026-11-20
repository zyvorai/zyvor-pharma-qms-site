#!/usr/bin/env python3
"""Generate Pharma QMS social / README / page SVGs (light + dark).

  python3 scripts/gen-graphics.py
  ./scripts/render-social.sh   # PNG OG + social-preview via rsvg-convert

Colours match site.css. Every graphic has title + desc for a11y.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DOCS_ASSETS = ROOT / "docs" / "assets"

FONT = "-apple-system,BlinkMacSystemFont,'SF Pro Display','SF Pro Text','Segoe UI',Roboto,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"
PAL = {
    "light": dict(
        bg="#ffffff", card="#f5f5f7", line="#d2d2d7", text="#1d1d1f", dim="#6e6e73",
        mute="#86868b", green="#34c759", accent="#0071e3", warn="#ff9f0a",
        warnbg="#fff4e0", soft="#d6ebff", okbg="#e8f8ec", ink="#1d1d1f",
    ),
    "dark": dict(
        bg="#000000", card="#1d1d1f", line="#3a3a3c", text="#f5f5f7", dim="#a1a1a6",
        mute="#86868b", green="#30d158", accent="#2997ff", warn="#ffd60a",
        warnbg="#2b2300", soft="#0a2744", okbg="#0f2a18", ink="#f5f5f7",
    ),
}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, size=16, weight=400, fill="text", anchor="start", mono=False, p=None, ls=0.0):
    p = p or PAL["light"]
    fam = MONO if mono else FONT
    return (
        f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
        f'fill="{p[fill]}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(s)}</text>'
    )


def rect(x, y, w, h, r, fill, p, stroke=None, sw=1.0):
    st = f' stroke="{p[stroke]}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{p[fill]}"{st}/>'


def svg(w, h, title, desc, body, p):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-labelledby="t d">'
        f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>'
        f'<rect width="{w}" height="{h}" fill="{p["bg"]}"/>{body}</svg>\n'
    )


def mark(x, y, scale, p):
    # Flask / assay mark matching assets/mark-*.svg
    return (
        f'<g transform="translate({x} {y}) scale({scale})">'
        f'<rect x="2" y="2" width="60" height="60" rx="17" fill="{p["accent"]}"/>'
        f'<path d="M24 16v18c0 6 4 10 8 10s8-4 8-10V16" fill="none" stroke="#fff" stroke-width="4.2" stroke-linecap="round"/>'
        f'<path d="M22 16h20" fill="none" stroke="#fff" stroke-width="4.2" stroke-linecap="round"/>'
        f'<circle cx="32" cy="44" r="3.2" fill="#b5f5c8"/>'
        f'<path d="M18 50h28" fill="none" stroke="#b5f5c8" stroke-width="3.4" stroke-linecap="round"/>'
        f"</g>"
    )


def gradients(p, ga="ga", gb="gb", tx="tx"):
    a, g = p["accent"], p["green"]
    return (
        f'<defs>'
        f'<radialGradient id="{ga}" cx=".12" cy=".18" r=".55">'
        f'<stop offset="0" stop-color="{a}" stop-opacity=".12"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{gb}" cx=".92" cy=".8" r=".55">'
        f'<stop offset="0" stop-color="{g}" stop-opacity=".12"/><stop offset="1" stop-color="{g}" stop-opacity="0"/></radialGradient>'
        f'<linearGradient id="{tx}" x1="0" x2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="#32ade6"/></linearGradient>'
        f"</defs>"
        f'<rect width="100%" height="100%" fill="url(#{ga})"/><rect width="100%" height="100%" fill="url(#{gb})"/>'
    )


def banner(p):
    b = [gradients(p), mark(80, 56, 0.88, p)]
    b += [
        t(150, 103, "PHARMA QMS", 22, 600, p=p, ls=2.4),
        t(80, 200, "Batch to release for", 64, 700, p=p, ls=-2.2),
        t(80, 276, "manufacturers.", 64, 700, fill="accent", p=p, ls=-2.2),
        t(82, 330, "One spine for manufacturing, laboratory and QA — India, US and EU.", 20, 400, "dim", p=p),
        t(82, 360, "Pilot electronic records. Not validated. Not Part 11.", 20, 400, "dim", p=p),
    ]
    # Mini console card
    b += [
        rect(760, 52, 440, 336, 28, "card", p, "line"),
        t(788, 96, "RELEASE SPINE", 13, 600, "dim", p=p, ls=1.2),
        t(1172, 96, "● pilot", 13, 600, "green", "end", p=p),
        rect(784, 116, 190, 100, 18, "bg", p, "line"),
        t(800, 144, "Active batches", 13, 400, "dim", p=p),
        t(800, 190, "12", 40, 700, "accent", p=p, ls=-1.2),
        rect(986, 116, 190, 100, 18, "bg", p, "line"),
        t(1002, 144, "Open OOS", 13, 400, "dim", p=p),
        t(1002, 190, "2", 40, 700, "warn", p=p, ls=-1.2),
        rect(784, 232, 392, 120, 18, "bg", p, "line"),
        t(800, 262, "Path", 13, 400, "dim", p=p),
    ]
    steps = [("Draft", "okbg", "green"), ("Lab", "soft", "accent"), ("QA", "warnbg", "warn"), ("Release", "okbg", "green")]
    x0 = 800
    for i, (lab, bgk, fg) in enumerate(steps):
        x = x0 + i * 90
        b += [
            f'<rect x="{x}" y="280" width="78" height="36" rx="18" fill="{p[bgk]}"/>',
            t(x + 39, 304, lab, 12, 600, fg, "middle", p=p),
        ]
    b.append(t(1176, 370, "synthetic data · illustration", 11, 400, "mute", "end", p=p))
    return svg(
        1280, 440,
        "Zyvor Pharma QMS: batch to release for manufacturers",
        "Pharma QMS logo, headline, and a synthetic release-spine dashboard card.",
        "".join(b), p,
    )


def og(p):
    """1200×630 Open Graph / Twitter card."""
    b = [gradients(p, "oga", "ogb", "ogtx"), mark(72, 72, 1.0, p)]
    b += [
        t(152, 118, "ZYVOR PHARMA QMS", 20, 600, p=p, ls=2.0),
        t(72, 250, "Batch to release", 58, 700, p=p, ls=-1.8),
        t(72, 318, "for manufacturers.", 58, 700, fill="accent", p=p, ls=-1.8),
        t(72, 380, "Manufacturing · Laboratory · QA · India / US / EU markets", 22, 400, "dim", p=p),
        t(72, 420, "Pilot electronic records · not validated · not Part 11", 20, 500, "mute", p=p),
        rect(72, 470, 160, 44, 22, "accent", p),
        t(152, 499, "Pilot-ready", 16, 600, "bg", "middle", p=p),
        rect(248, 470, 200, 44, 22, "card", p, "line"),
        t(348, 499, "59 modules", 16, 600, p=p, anchor="middle"),
        rect(464, 470, 220, 44, 22, "card", p, "line"),
        t(574, 499, "Self-hosted", 16, 600, p=p, anchor="middle"),
        t(1128, 560, "zyvor.dev", 16, 500, "mute", "end", p=p),
    ]
    return svg(
        1200, 630,
        "Zyvor Pharma QMS social card",
        "Open Graph image: Pharma QMS headline, pilot badges, zyvor.dev.",
        "".join(b), p,
    )


def architecture(p):
    boxes = [
        (80, 140, 240, 120, "Console", "React SPA · same-origin"),
        (400, 140, 280, 120, "API", "Go · chi · append-only audit"),
        (760, 140, 280, 120, "Postgres", "Migrations · plant data"),
        (200, 340, 280, 110, "Desktop apps", "macOS · Windows · CLI"),
        (560, 340, 320, 110, "Deploy", "Compose · FluxVM · k3s · WSL"),
    ]
    b = [
        t(560, 56, "How it fits together", 28, 700, p=p, anchor="middle", ls=-0.6),
        t(560, 90, "One API, one database, console or native launcher. You host it.", 16, 400, "dim", p=p, anchor="middle"),
    ]
    for x, y, w, h, title, sub in boxes:
        b += [rect(x, y, w, h, 20, "card", p, "line"), t(x + 24, y + 48, title, 22, 700, p=p), t(x + 24, y + 80, sub, 15, 400, "dim", p=p)]
    # arrows
    b.append(f'<path d="M320 200 H400" stroke="{p["accent"]}" stroke-width="3" fill="none" marker-end="url(#arr)"/>')
    b.append(f'<path d="M680 200 H760" stroke="{p["accent"]}" stroke-width="3" fill="none"/>')
    b.append(f'<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="{p["accent"]}"/></marker></defs>')
    return svg(1120, 500, "Pharma QMS architecture", "Console to API to Postgres, plus desktop apps and deploy paths.", "".join(b), p)


def security(p):
    cards = [
        ("Self-hosted", "Your Postgres. Your network. Nothing leaves the plant by default."),
        ("Role actors", "mfg / lab / qa / viewer / admin for pilot walkthroughs."),
        ("Append-only audit", "Application audit log on every write path — not a tamper-proof claim."),
        ("Honest limits", "Not Part 11. No live CDSCO / FDA / EMVS gateways. No pen-test yet."),
    ]
    b = [
        t(560, 52, "Security posture, plainly", 28, 700, p=p, anchor="middle", ls=-0.6),
        t(560, 86, "What we built — and what we have not claimed.", 16, 400, "dim", p=p, anchor="middle"),
    ]
    for i, (title, body) in enumerate(cards):
        x, y = 60 + (i % 2) * 500, 130 + (i // 2) * 160
        # wrap body ~42 chars
        words, lines, cur = body.split(), [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if len(trial) > 42 and cur:
                lines.append(cur)
                cur = w
            else:
                cur = trial
        if cur:
            lines.append(cur)
        b += [
            rect(x, y, 460, 130, 20, "card", p, "line"),
            t(x + 28, y + 42, title, 22, 700, p=p),
        ]
        for j, line in enumerate(lines[:3]):
            b.append(t(x + 28, y + 78 + j * 22, line, 15, 400, "dim", p=p))
    return svg(1120, 460, "Pharma QMS security posture", "Four cards: self-hosted, roles, audit, honest limits.", "".join(b), p)


def capabilities(p):
    groups = [
        ("Manufacturing", "Batches · eBMR · IPC · line clearance · packaging"),
        ("Laboratory", "Samples · specs · OOS · second-person verify"),
        ("Quality", "Deviations · CAPA · complaints · release checklist"),
        ("Markets", "India Schedule M · US FDA · EU GMP / QP"),
        ("Plant ops", "Stability · env · warehouse · training · change"),
        ("Traceability", "Genealogy · CoA · quarantine · recalls"),
    ]
    b = [
        t(640, 48, "What the system covers", 28, 700, p=p, anchor="middle", ls=-0.6),
        t(640, 80, "59 modules in the feature catalogue — pilot electronic records only.", 16, 400, "dim", p=p, anchor="middle"),
    ]
    for i, (title, body) in enumerate(groups):
        x, y = 40 + (i % 3) * 400, 120 + (i // 3) * 160
        b += [
            rect(x, y, 370, 130, 20, "card", p, "line"),
            f'<circle cx="{x + 36}" cy="{y + 40}" r="10" fill="{p["accent"]}"/>',
            t(x + 60, y + 46, title, 20, 700, p=p),
            t(x + 28, y + 90, body, 14, 400, "dim", p=p),
        ]
    return svg(1280, 440, "Pharma QMS capabilities", "Six groups: manufacturing, lab, quality, markets, plant ops, traceability.", "".join(b), p)


def write_pair(name, fn):
    for mode in ("light", "dark"):
        out = ASSETS / f"{name}-{mode}.svg"
        out.write_text(fn(PAL[mode]), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    DOCS_ASSETS.mkdir(parents=True, exist_ok=True)
    write_pair("banner", banner)
    write_pair("architecture", architecture)
    write_pair("security", security)
    write_pair("capabilities", capabilities)
    # OG uses light palette (social networks prefer light cards)
    og_path = ASSETS / "og.svg"
    og_path.write_text(og(PAL["light"]), encoding="utf-8")
    print("wrote", og_path.relative_to(ROOT))
    # GitHub / docs social preview (1280×640)
    social_svg = og(PAL["light"]).replace('viewBox="0 0 1200 630" width="1200" height="630"',
                                          'viewBox="0 0 1200 630" width="1280" height="640"', 1)
    (DOCS_ASSETS / "social-preview.svg").write_text(social_svg, encoding="utf-8")
    print("wrote docs/assets/social-preview.svg")


if __name__ == "__main__":
    main()
