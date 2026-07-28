#!/usr/bin/env python3
"""Generate the ep3 path-map sub-compositions (compositions/g-track-N.html).

One designed component, seven instances — every instance shows ALL twelve towns with
collision-free label anchors (v2 showed 5 of 12 and garbled Murphysboro/De Soto), a storm
marker that keeps moving for the whole window (the continuous element DESIGN.md §5 requires),
and the cumulative death toll ticking town by town.
"""
import json
from pathlib import Path

EP = Path(__file__).resolve().parent.parent / "episodes" / "ep3-tristate"
OUT = EP / "compositions"
OUT.mkdir(exist_ok=True)

# name, x, y, clock, miles, cumulative dead on leaving, label anchor: (dx, dy, align)
TOWNS = [
    ("Ellington",      300, 792, "1:01 PM",   0,   1, (0, -34, "start")),
    ("Annapolis",      404, 745, "1:14 PM",  13,   5, (0,  46, "start")),
    ("Biehle",         556, 690, "~1:30 PM", 55,  13, (0, -34, "start")),
    ("Gorham",         690, 636, "2:26 PM",  88,  39, (0,  46, "start")),
    ("Murphysboro",    780, 600, "2:34 PM",  97, 273, (-14, -36, "end")),
    ("De Soto",        858, 566, "2:45 PM", 106, 342, (18, -34, "start")),
    ("West Frankfort", 962, 528, "3:00 PM", 122, 490, (-14,  50, "end")),
    ("Parrish",       1046, 496, "3:07 PM", 131, 512, (18, -32, "start")),
    ("Crossville",    1168, 456, "~3:23 PM",152, 516, (0,  48, "start")),
    ("Griffin",       1332, 412, "~4:00 PM",183, 541, (0, -34, "start")),
    ("Princeton",     1452, 372, "4:18 PM", 203, 586, (0,  46, "start")),
    ("Petersburg",    1596, 330, "4:30 PM", 219, 695, (-10, -34, "end")),
]

# instance: id, upTo index, window duration, toll shown at start, headline
INSTANCES = [
    ("g-track-1",  0, 24.0, 0,   "THE STORM IS BORN"),
    ("g-track-2",  3, 22.0, 5,   "INTO ILLINOIS"),
    ("g-track-3",  5, 12.0, 39,  "ELEVEN MINUTES, TWO TOWNS"),
    ("g-track-5",  9, 10.0, 490, "ACROSS THE WABASH"),
    ("g-track-7", 11, 30.0, 537, "THE COMPLETE TRACK"),
]

STYLE = """
  #root { position:absolute; inset:0; font-family:Arial, sans-serif;
    background:radial-gradient(ellipse at 46% 52%, #0d141c 0%, #04070a 76%); }
  .eyebrow { position:absolute; left:88px; top:74px; font-size:22px; letter-spacing:6px; color:#93a3b2; font-weight:700; }
  .hl { position:absolute; left:88px; top:104px; font-family:'Arial Black',Arial,sans-serif; font-size:52px; color:#f2f5f8; }
  .tollwrap { position:absolute; left:88px; top:196px; }
  .toll { font-family:'Courier New',monospace; font-size:84px; color:#e74c3c; font-weight:700; line-height:1; }
  .tolllab { font-size:20px; letter-spacing:6px; color:#c8d3e0; font-weight:700; margin-top:8px; }
  .clockwrap { position:absolute; right:96px; top:78px; text-align:right; }
  .clock { font-family:'Courier New',monospace; font-size:64px; color:#e8c56a; font-weight:700; line-height:1; }
  .clocklab { font-size:19px; letter-spacing:4px; color:#93a3b2; font-weight:700; margin-top:8px; }
  .miles { font-family:'Arial Black',Arial,sans-serif; font-size:44px; color:#f2f5f8; margin-top:26px; }
  .mileslab { font-size:19px; letter-spacing:4px; color:#93a3b2; font-weight:700; margin-top:4px; }
  .statelab { font-family:Georgia,serif; font-style:italic; font-size:27px; fill:#40607d; }
  .town { font-family:Arial,sans-serif; font-weight:700; font-size:26px; fill:#e8eef4; }
  .town.past { fill:#7d8c9a; }
  .foot { position:absolute; left:88px; bottom:70px; font-family:Georgia,serif; font-style:italic;
    font-size:26px; color:#d8a13a; }
"""


def build(cid, up_to, dur, toll_start, headline):
    shown = TOWNS[: up_to + 1]
    pts = " ".join(f"{t[1]},{t[2]}" for t in shown)
    path_len = 0.0
    for a, b in zip(shown, shown[1:]):
        path_len += ((b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2) ** 0.5
    path_len = max(path_len, 1)

    svg = [
        '<svg viewBox="0 0 1920 1080" style="position:absolute;inset:0">',
        '<defs><filter id="glow"><feGaussianBlur stdDeviation="9" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>',
        '<line x1="664" y1="150" x2="664" y2="1010" stroke="#16212c" stroke-width="3"/>',
        '<line x1="1272" y1="150" x2="1272" y2="1010" stroke="#16212c" stroke-width="3"/>',
        '<text x="470" y="994" class="statelab">MISSOURI</text>',
        '<text x="930" y="994" class="statelab">ILLINOIS</text>',
        '<text x="1450" y="994" class="statelab">INDIANA</text>',
    ]
    # full route ghosted so the viewer always sees where it is going
    ghost = " ".join(f"{t[1]},{t[2]}" for t in TOWNS)
    svg.append(f'<polyline points="{ghost}" fill="none" stroke="#22303d" stroke-width="4" stroke-dasharray="9 12"/>')
    svg.append(
        f'<polyline id="{cid}-line" points="{pts}" fill="none" stroke="#c0392b" stroke-width="8" '
        f'stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{path_len:.0f}" '
        f'stroke-dashoffset="{path_len:.0f}"/>'
    )
    # every town, always: dot + label. Anchors are hand-placed to keep ink boxes apart.
    for i, (nm, x, y, clock, mi, dead, (dx, dy, anchor)) in enumerate(TOWNS):
        active = i <= up_to
        svg.append(
            f'<circle id="{cid}-d{i}" cx="{x}" cy="{y}" r="{0 if active else 5}" '
            f'fill="{"#f2f5f8" if active else "#3d5063"}"/>'
        )
        cls = "town" if active else "town past"
        op = 0 if active else 0.55
        svg.append(
            f'<text id="{cid}-t{i}" x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" '
            f'class="{cls}" opacity="{op}">{nm}</text>'
        )
    svg.append(f'<circle id="{cid}-storm" cx="{TOWNS[0][1]}" cy="{TOWNS[0][2]}" r="0" fill="#c0392b" filter="url(#glow)" opacity="0.92"/>')
    svg.append(f'<circle id="{cid}-ring" cx="{TOWNS[0][1]}" cy="{TOWNS[0][2]}" r="14" fill="none" stroke="#e8c56a" stroke-width="3" opacity="0"/>')
    svg.append("</svg>")

    body = f"""<div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080">
  {''.join(svg)}
  <div class="eyebrow" id="{cid}-eb">THE TRACK · MARCH 18, 1925</div>
  <div class="hl" id="{cid}-hl">{headline}</div>
  <div class="tollwrap" id="{cid}-tollwrap">
    <div class="toll" id="{cid}-toll">{TOWNS[0][5]}</div>
    <div class="tolllab">CONFIRMED DEAD SO FAR</div>
  </div>
  <div class="clockwrap" id="{cid}-clockwrap">
    <div class="clock" id="{cid}-clock">{TOWNS[0][3]}</div>
    <div class="clocklab">LOCAL TIME</div>
    <div class="miles"><span id="{cid}-mi">0</span> MI</div>
    <div class="mileslab">ON THE GROUND</div>
  </div>
</div>"""

    # ---- timeline: draw, walk the storm marker the whole window, tick the toll per town
    walk_start, walk_end = 0.9, dur - 1.6
    walk = max(walk_end - walk_start, 2.0)
    j = [
        "window.__timelines = window.__timelines || {};",
        "(function() {",
        "  const tl = gsap.timeline({ paused: true });",
        f'  const P = "#{cid}-";',
        f'  tl.fromTo(P+"eb", {{autoAlpha:0, x:-30}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, 0.15);',
        f'  tl.fromTo(P+"hl", {{autoAlpha:0, x:-30}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, 0.35);',
        f'  tl.fromTo(P+"clockwrap", {{autoAlpha:0, x:34}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, 0.55);',
        f'  tl.fromTo(P+"tollwrap", {{autoAlpha:0, y:26}}, {{autoAlpha:1, y:0, duration:0.5, ease:"power3.out"}}, 0.75);',
        f'  tl.to(P+"line", {{strokeDashoffset:0, duration:{walk:.2f}, ease:"none"}}, {walk_start});',
        f'  tl.fromTo(P+"storm", {{attr:{{r:0}}}}, {{attr:{{r:19}}, duration:0.45, ease:"power4.in"}}, {walk_start});',
    ]
    # storm marker + ring pulse walk town to town (continuous motion across the window)
    seg_t = walk_start
    per = walk / max(up_to, 1) if up_to else walk
    toll_prev = TOWNS[0][5]
    for i in range(1, up_to + 1):
        nm, x, y, clock, mi, dead, _ = TOWNS[i]
        t0 = seg_t
        seg_t += per
        j.append(f'  tl.to(P+"storm", {{attr:{{cx:{x}, cy:{y}}}, duration:{per:.2f}, ease:"none"}}, {t0:.2f});')
        j.append(f'  tl.to(P+"ring", {{attr:{{cx:{x}, cy:{y}}}, duration:{per:.2f}, ease:"none"}}, {t0:.2f});')
        j.append(f'  tl.fromTo(P+"ring", {{attr:{{r:14}}, autoAlpha:0.95}}, {{attr:{{r:52}}, autoAlpha:0, duration:0.9, ease:"power2.out"}}, {seg_t - 0.1:.2f});')
        j.append(f'  tl.to(P+"d{i}", {{attr:{{r:9}}, duration:0.3, ease:"power4.in"}}, {seg_t - 0.15:.2f});')
        j.append(f'  tl.to(P+"t{i}", {{opacity:1, duration:0.35}}, {seg_t - 0.05:.2f});')
        j.append(f'  tl.to(P+"clock", {{duration:0.01, onComplete:function(){{const e=document.getElementById("{cid}-clock"); if(e) e.textContent="{clock}";}}}}, {seg_t:.2f});')
        if dead != toll_prev:
            j.append(f'  tl.to(TOLL, {{v:{dead}, duration:0.85, ease:"power3.out", onUpdate:tollUpd}}, {seg_t:.2f});')
            toll_prev = dead
    # first town dot + label pop even when it is the only one
    j.insert(9, f'  tl.to(P+"d0", {{attr:{{r:9}}, duration:0.3, ease:"power4.in"}}, {walk_start + 0.1:.2f});')
    j.insert(10, f'  tl.to(P+"t0", {{opacity:1, duration:0.35}}, {walk_start + 0.25:.2f});')
    j.append(f'  tl.to(MI, {{v:{TOWNS[up_to][4]}, duration:{walk:.2f}, ease:"none", onUpdate:miUpd}}, {walk_start});')
    j.append(f'  tl.to(P+"storm", {{attr:{{r:26}}, duration:0.6, yoyo:true, repeat:3, ease:"sine.inOut"}}, {walk_end:.2f});')
    j.append(f'  window.__timelines["{cid}"] = tl;')
    j.append("})();")

    js = "\n".join(j)
    js = js.replace(
        "(function() {",
        "(function() {\n  const TOLL = {v:%d}, MI = {v:0};\n"
        '  function tollUpd(){const e=document.getElementById("%s-toll"); if(e) e.textContent=Math.round(TOLL.v);}\n'
        '  function miUpd(){const e=document.getElementById("%s-mi"); if(e) e.textContent=Math.round(MI.v);}'
        % (TOWNS[0][5], cid, cid),
    )

    html = f"""<!doctype html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>{STYLE}</style>
{body}
<script>
{js}
</script>
</template>
</body>
</html>
"""
    (OUT / f"{cid}.html").write_text(html, encoding="utf-8")
    return cid, dur


if __name__ == "__main__":
    made = [build(*inst) for inst in INSTANCES]
    print(f"[gen_track] wrote {len(made)} track compositions -> {OUT}")
    for cid, dur in made:
        print(f"  {cid}  {dur}s")
