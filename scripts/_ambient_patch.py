#!/usr/bin/env python3
import re, math, sys

E = "episodes/ep-1974-super-outbreak/compositions"

FILES = {
    "g-map-i": 83.492,
    "g-map-a1": 137.273,
    "g-map-a2": 29.946,
    "g-map-a3": 126.290,
    "g-map-a4": 78.5,
    "g-map-a6": 49.072,
    "g-plane": 28.163,
}

# safe zone: x < 1160 (clear of rail x>=1270 and presenter x>=1600), y scattered 150-950
BD_POS = [
    (120, 200), (900, 160), (200, 900), (1050, 850), (500, 950), (760, 480),
]

def html_block(p):
    divs = []
    for i, (x, y) in enumerate(BD_POS):
        divs.append(
            f'<div id="{p}bd{i}" style="position:absolute; left:{x}px; top:{y}px; width:6px; height:6px; '
            f'border-radius:50%; background:#93a3b2; opacity:0.25; pointer-events:none;"></div>'
        )
    scan = (
        f'<div id="{p}scan" style="position:absolute; left:60px; top:40px; width:1100px; height:2px; '
        f'background:linear-gradient(90deg, transparent, rgba(147,163,178,0.4), transparent); opacity:0.5; '
        f'pointer-events:none;"></div>'
    )
    lines = [
        '<!-- QC fix (2026-09-21, owner draft review): ambient motion so the graphic never goes fully static -->',
    ] + divs + [scan]
    return "\n".join(lines)


def js_block(p, dur):
    interval = 1.2
    ticks = math.ceil(dur / interval)
    pass_dur = 25
    scan_repeat = max(0, math.ceil(dur / pass_dur) - 1)
    n_bd = len(BD_POS)
    lines = []
    lines.append('')
    lines.append('  // QC fix (2026-09-21, owner draft review): "motion graphics need some motion, after some')
    lines.append('  // time it is static" -- add a staggered dot blip (a new blip starts at least every 1.2s,')
    lines.append('  // well inside the 1.5s bar) plus a slow scanline sweep (well over the 6px/s floor), both')
    lines.append('  // for the FULL comp window, independent of any cue. Finite counts sized to DUR (never repeat:-1).')
    lines.append(f'  const AMBIENT_BD_INTERVAL = {interval};')
    lines.append(f'  const AMBIENT_BD_TICKS = {ticks}; // Math.ceil(DUR / {interval})')
    lines.append('  for (let i = 0; i < AMBIENT_BD_TICKS; i++) {')
    lines.append(f'    const id = "bd" + (i % {n_bd});')
    lines.append('    const at = i * AMBIENT_BD_INTERVAL;')
    lines.append('    tl.to(P+id, { opacity: 0.85, scale: 1.8, duration: 0.4, ease: "sine.inOut" }, at);')
    lines.append('    tl.to(P+id, { opacity: 0.25, scale: 1, duration: 0.4, ease: "sine.inOut" }, at + 0.4);')
    lines.append('  }')
    lines.append(f'  const AMBIENT_SCAN_PASS = {pass_dur}; // {pass_dur}s to cross 1000px = 40px/s, well over the 6px/s floor')
    lines.append(f'  const AMBIENT_SCAN_REPEAT = {scan_repeat}; // Math.max(0, Math.ceil(DUR / {pass_dur}) - 1), sized to DUR')
    lines.append('  tl.fromTo(P+"scan", { y: 0 }, { y: 1000, duration: AMBIENT_SCAN_PASS, ease: "none", repeat: AMBIENT_SCAN_REPEAT, yoyo: true }, 0);')
    return "\n".join(lines)


for name, dur in FILES.items():
    path = f"{E}/{name}.html"
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()

    p_match = re.search(r'const P = "(#[a-zA-Z0-9-]+-)";', src)
    if not p_match:
        print(f"SKIP {name}: no P prefix found")
        continue
    p = p_match.group(1).lstrip("#")

    anchor_html = '<div class="railfade"></div>'
    if anchor_html not in src:
        print(f"SKIP {name}: no railfade anchor")
        continue
    block = html_block(p)
    src = src.replace(anchor_html, anchor_html + "\n" + block, 1)

    dur_match = re.search(r'const DUR = [0-9.]+;', src)
    if not dur_match:
        print(f"SKIP {name}: no DUR const found for JS insert")
        continue
    jsblock = js_block(p, dur)
    src = src[:dur_match.end()] + jsblock + src[dur_match.end():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    print(f"OK {name}: prefix={p} dur={dur}")
