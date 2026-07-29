#!/usr/bin/env python3
"""The ep3 graphics not covered by the build fan-out: sources, wires, relief, family,
fujita, the word-ban bookend and the close card.

Same contract as everything else (DESIGN.md GRAPHICS CONTRACT): textured background,
three type tiers, kinetic entrances, and one continuous element that runs the whole window
so the frame is never frozen.
"""
from pathlib import Path

EP = Path(__file__).resolve().parent.parent / "episodes" / "ep3-tristate"
OUT = EP / "compositions"
OUT.mkdir(exist_ok=True)

BASE = """
  #root { position:absolute; inset:0; font-family:Arial, sans-serif;
    background:radial-gradient(ellipse at 46% 52%, #0d141c 0%, #04070a 76%); overflow:hidden; }
  .eyebrow { position:absolute; left:96px; top:76px; font-size:22px; letter-spacing:6px; color:#93a3b2; font-weight:700; }
  .hl { position:absolute; left:96px; top:112px; font-family:'Arial Black',Arial,sans-serif; font-size:52px; color:#f2f5f8; }
  .sub { position:absolute; left:96px; top:196px; font-family:Georgia,serif; font-style:italic; font-size:26px; color:#d8a13a; }
  .drift { position:absolute; inset:-40% 0; opacity:0.30; pointer-events:none;
    background:repeating-linear-gradient(0deg, rgba(120,150,180,0.16) 0 1px, transparent 1px 46px); }
  .lab { font-size:19px; letter-spacing:4px; color:#93a3b2; font-weight:700; }
  .val { font-size:30px; color:#dfe7ee; font-weight:700; letter-spacing:1px; }
  .num { font-family:'Courier New',monospace; font-size:84px; color:#e74c3c; font-weight:700; line-height:1; }
  .maplab { font-family:Arial,sans-serif; font-weight:700; font-size:25px; fill:#e8eef4; }
  .foot { position:absolute; left:96px; bottom:74px; font-family:Georgia,serif; font-style:italic;
    font-size:26px; color:#d8a13a; }
"""

def wrap(cid, style, body, js, dur):
    html = f"""<!doctype html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>{BASE}{style}</style>
<div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080">
<div class="drift" id="{cid}-drift"></div>
{body}
</div>
<script>
window.__timelines = window.__timelines || {{}};
(function() {{
  const tl = gsap.timeline({{ paused: true }});
  const P = "#{cid}-";
  tl.fromTo(P+"drift", {{y:-120}}, {{y:120, duration:DURV, ease:"none"}}, 0);
{js}
  window.__timelines["{cid}"] = tl;
}})();
</script>
</template>
</body>
</html>
"""
    (OUT / f"{cid}.html").write_text(html.replace("DURV", str(dur)), encoding="utf-8")


def head(cid, eyebrow, hl, sub=None, at=0.15):
    b = f'<div class="eyebrow" id="{cid}-eb">{eyebrow}</div><div class="hl" id="{cid}-hl">{hl}</div>'
    if sub:
        b += f'<div class="sub" id="{cid}-sb">{sub}</div>'
    j = (f'  tl.fromTo(P+"eb", {{autoAlpha:0, x:-30}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, {at});\n'
         f'  tl.fromTo(P+"hl", {{autoAlpha:0, x:-30}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, {at+0.2});\n')
    if sub:
        j += f'  tl.fromTo(P+"sb", {{autoAlpha:0, x:-24}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, {at+0.4});\n'
    return b, j


# ---------------------------------------------------------------- g-sources
def sources():
    cid, D = "g-sources", 30.0
    items = [("01", "THE NEWSREEL", "Fox Movietone, 1925 — Univ. of South Carolina", 2.2),
             ("02", "WEATHER BUREAU RECORDS", "the original forecast documents", 8.0),
             ("03", "THE FRONT PAGES", "that week's newspapers, six states", 13.5),
             ("04", "MODERN REANALYSIS", "Johns, Burgess et al. · 2013", 19.0)]
    b, j = head(cid, "HOW THIS STORY IS BUILT", "FOUR SOURCES", "everything you will see comes from one of them")
    for i, (n, t, s, at) in enumerate(items):
        y = 300 + i * 150
        b += (f'<div id="{cid}-c{i}" style="position:absolute;left:96px;top:{y}px;width:1360px;'
              f'border-left:6px solid #8e2020;background:linear-gradient(90deg,rgba(9,14,20,0.92),rgba(9,14,20,0.25));'
              f'padding:18px 28px;box-sizing:border-box;">'
              f'<span class="lab">SOURCE {n}</span>'
              f'<div style="font-family:\'Arial Black\',Arial,sans-serif;font-size:38px;color:#f2f5f8;margin-top:6px">{t}</div>'
              f'<div style="font-family:Georgia,serif;font-style:italic;font-size:24px;color:#b8c6d4;margin-top:6px">{s}</div></div>')
        j += (f'  tl.fromTo(P+"c{i}", {{autoAlpha:0, x:-70}}, {{autoAlpha:1, x:0, duration:0.55, ease:"power3.out"}}, {at});\n'
              f'  tl.fromTo(P+"c{i}", {{scaleX:0.985}}, {{scaleX:1, duration:0.5, ease:"power2.out", transformOrigin:"left center"}}, {at});\n')
    b += f'<div class="foot" id="{cid}-ft">No source, no scene. Everything else stays out.</div>'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 25.0);\n'
    wrap(cid, "", b, j, D)
    return cid


# ---------------------------------------------------------------- g-wires
def wires():
    cid, D = "g-wires", 36.0
    b, j = head(cid, "WHY NO ONE COULD BE TOLD", "IT CUT ITS OWN WIRES",
                "the telegraph line ran along the railroad — straight down the path")
    poles = [(240 + i * 128, 600) for i in range(12)]
    svg = ['<svg viewBox="0 0 1920 1080" style="position:absolute;inset:0">']
    svg.append('<line id="%s-wire" x1="240" y1="560" x2="1650" y2="560" stroke="#7fb2e5" stroke-width="5"/>' % cid)
    for i, (x, y) in enumerate(poles):
        svg.append(f'<rect id="{cid}-p{i}" x="{x}" y="530" width="7" height="120" fill="#5a768f"/>')
    svg.append(f'<circle id="{cid}-storm" cx="200" cy="560" r="0" fill="#c0392b" opacity="0.9"/>')
    svg.append(f'<text id="{cid}-t1" x="240" y="500" class="maplab" fill="#93a3b2">TELEGRAPH &amp; TELEPHONE LINE</text>')
    svg.append('</svg>')
    b += "".join(svg)
    b += (f'<div id="{cid}-count" style="position:absolute;right:120px;top:300px;text-align:right">'
          f'<div class="num"><span id="{cid}-cv">0</span></div>'
          f'<div class="lab" style="margin-top:8px">POLES DOWN BEHIND IT</div></div>')
    b += f'<div class="foot" id="{cid}-ft">Every town it hit lost the only way to warn the next one.</div>'
    j += f'  tl.fromTo(P+"storm", {{attr:{{r:0}}}}, {{attr:{{r:26}}, duration:0.5, ease:"power4.in"}}, 3.0);\n'
    j += f'  tl.to(P+"storm", {{attr:{{cx:1680}}, duration:24.0, ease:"none"}}, 3.4);\n'
    j += f'  tl.to(P+"wire", {{attr:{{x1:1680}}, duration:24.0, ease:"none"}}, 3.4);\n'
    j += f'  tl.set([{", ".join(chr(34) + "#" + cid + "-p" + str(i) + chr(34) for i in range(len(poles)))}], {{transformOrigin:"bottom center"}}, 0);\n'
    j += f'  tl.fromTo(P+"count", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.5}}, 4.0);\n'
    for i, (x, y) in enumerate(poles):
        at = 3.4 + 24.0 * (x - 200) / 1480.0
        j += f'  tl.to(P+"p{i}", {{rotation:{-62 if i % 2 else 58}, y:14, duration:0.55, ease:"power4.in"}}, {at:.2f});\n'
        j += f'  tl.to(CNT, {{v:{i+1}, duration:0.3, onUpdate:cu}}, {at:.2f});\n'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 29.5);\n'
    js = ("  const CNT={v:0};\n  function cu(){const e=document.getElementById('%s-cv'); if(e) e.textContent=Math.round(CNT.v);}\n" % cid) + j
    wrap(cid, "", b, js, D)
    return cid


# ---------------------------------------------------------------- g-relief
def relief():
    cid, D = "g-relief", 42.0
    b, j = head(cid, "THAT NIGHT", "THE TRAINS CAME", "into a landscape with no lights and no telephones")
    b += ('<svg viewBox="0 0 1920 1080" style="position:absolute;inset:0">'
          f'<path id="{cid}-rt1" d="M 360 380 Q 620 470 880 570" stroke="#7fb2e5" stroke-width="6" fill="none" '
          f'stroke-dasharray="14 12" stroke-dashoffset="0"/>'
          f'<path id="{cid}-rt2" d="M 1520 320 Q 1200 440 940 570" stroke="#7fb2e5" stroke-width="6" fill="none" '
          f'stroke-dasharray="14 12" stroke-dashoffset="0"/>'
          f'<circle cx="905" cy="585" r="15" fill="#c0392b"/>'
          f'<text x="820" y="650" class="maplab" fill="#93a3b2">THE PATH</text>'
          f'<text x="300" y="350" class="maplab">ST. LOUIS</text>'
          f'<text x="1470" y="290" class="maplab">CHICAGO</text>'
          f'<circle id="{cid}-t1" cx="360" cy="380" r="0" fill="#e8c56a"/>'
          f'<circle id="{cid}-t2" cx="1520" cy="320" r="0" fill="#e8c56a"/>'
          '</svg>')
    rows = [("FIRST RELIEF TRAIN", "LEFT WITHIN THE HOUR", 9.0),
            ("CARRIED", "DOCTORS · NURSES · LANTERNS · COFFINS", 14.0),
            ("FOUND", "TOWNS THAT COULD NOT CALL FOR HELP", 19.5)]
    for i, (l, v, at) in enumerate(rows):
        b += (f'<div id="{cid}-r{i}" style="position:absolute;right:110px;top:{300 + i*140}px;text-align:right">'
              f'<div class="lab">{l}</div><div class="val" style="margin-top:6px">{v}</div></div>')
        j += f'  tl.fromTo(P+"r{i}", {{autoAlpha:0, x:40}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, {at});\n'
    j += f'  tl.fromTo(P+"t1", {{attr:{{r:0}}}}, {{attr:{{r:13}}, duration:0.4, ease:"power4.in"}}, 5.0);\n'
    j += f'  tl.fromTo(P+"t2", {{attr:{{r:0}}}}, {{attr:{{r:13}}, duration:0.4, ease:"power4.in"}}, 6.2);\n'
    j += f'  tl.to(P+"t1", {{attr:{{cx:880, cy:570}}, duration:26.0, ease:"none"}}, 5.4);\n'
    j += f'  tl.to(P+"t2", {{attr:{{cx:940, cy:570}}, duration:26.0, ease:"none"}}, 6.6);\n'
    j += f'  tl.to(P+"rt1", {{attr:{{"stroke-dashoffset":-520}}, duration:30.0, ease:"none"}}, 5.4);\n'
    j += f'  tl.to(P+"rt2", {{attr:{{"stroke-dashoffset":-520}}, duration:30.0, ease:"none"}}, 6.6);\n'
    b += f'<div class="foot" id="{cid}-ft">Rescue arrived by rail, in the dark, hours after the last house fell.</div>'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 33.0);\n'
    wrap(cid, "", b, j, D)
    return cid


# ---------------------------------------------------------------- g-family
def family():
    cid, D = "g-family", 38.0
    b, j = head(cid, "A CENTURY-OLD ARGUMENT", "ONE TORNADO — OR MANY?",
                "the question that has never fully closed")
    b += ('<svg viewBox="0 0 1920 1080" style="position:absolute;inset:0">'
          f'<path id="{cid}-one" d="M 200 470 L 1720 420" stroke="#c0392b" stroke-width="9" fill="none" '
          f'stroke-dasharray="1530" stroke-dashoffset="1530"/>'
          f'<g id="{cid}-fam" opacity="0">'
          f'<path d="M 200 720 L 660 700" stroke="#e8c56a" stroke-width="8" fill="none"/>'
          f'<path d="M 720 697 L 1180 678" stroke="#e8c56a" stroke-width="8" fill="none"/>'
          f'<path d="M 1240 675 L 1720 655" stroke="#e8c56a" stroke-width="8" fill="none"/>'
          f'<circle id="{cid}-g1" cx="690" cy="699" r="9" fill="#7fb2e5"/>'
          f'<circle id="{cid}-g2" cx="1210" cy="677" r="9" fill="#7fb2e5"/>'
          f'</g></svg>')
    b += (f'<div id="{cid}-l1" style="position:absolute;left:200px;top:380px"><span class="lab">THE OFFICIAL VIEW</span>'
          f'<div class="val" style="color:#c0392b;font-size:34px;margin-top:6px">ONE CONTINUOUS TRACK — 219 MILES</div></div>')
    b += (f'<div id="{cid}-l2" style="position:absolute;left:200px;top:790px"><span class="lab">THE CHALLENGE</span>'
          f'<div class="val" style="color:#e8c56a;font-size:34px;margin-top:6px">A FAMILY OF TORNADOES — GAPS HIDDEN IN THE RAIN</div></div>')
    b += f'<div class="foot" id="{cid}-ft">Modern reanalysis: the continuous track holds across most of the path.</div>'
    j += f'  tl.to(P+"one", {{strokeDashoffset:0, duration:5.0, ease:"none"}}, 3.0);\n'
    j += f'  tl.fromTo(P+"l1", {{autoAlpha:0, x:-40}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, 4.0);\n'
    j += f'  tl.fromTo(P+"fam", {{autoAlpha:0}}, {{autoAlpha:1, duration:0.8}}, 12.0);\n'
    j += f'  tl.fromTo(P+"l2", {{autoAlpha:0, x:-40}}, {{autoAlpha:1, x:0, duration:0.5, ease:"power3.out"}}, 12.6);\n'
    j += f'  tl.fromTo(P+"g1", {{attr:{{r:9}}}}, {{attr:{{r:26}}, duration:1.2, yoyo:true, repeat:11, ease:"sine.inOut"}}, 14.0);\n'
    j += f'  tl.fromTo(P+"g2", {{attr:{{r:9}}}}, {{attr:{{r:26}}, duration:1.2, yoyo:true, repeat:11, ease:"sine.inOut"}}, 14.6);\n'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 30.0);\n'
    wrap(cid, "", b, j, D)
    return cid


# ---------------------------------------------------------------- g-fujita
def fujita():
    cid, D = "g-fujita", 44.0
    style = """
  .fportrait { position:absolute; left:110px; top:290px; width:520px; height:600px; overflow:hidden;
    border:3px solid #22303d; background:#080d13; }
  .fportrait img { width:100%; height:100%; object-fit:contain; filter:sepia(0.2) contrast(1.06); }
"""
    b, j = head(cid, "THE MAN WHO LEARNED TO READ RUINS", "TETSUYA THEODORE FUJITA",
                "he first studied destruction in Hiroshima")
    b += (f'<div class="fportrait" id="{cid}-ph"><img src="media/portraits/fujita-portrait-01.jpg" alt=""></div>'
          f'<div style="position:absolute;left:110px;top:912px" class="lab">1972 PRESS PHOTOGRAPH · PUBLIC DOMAIN</div>')
    rows = [("HIS METHOD", "READ THE DAMAGE, INFER THE WIND", 6.0),
            ("HIS SCALE", "F0 TO F5 — STILL IN USE TODAY", 11.0),
            ("APPLIED BACKWARD", "IT LET 1925 BE MEASURED AT LAST", 16.0)]
    for i, (l, v, at) in enumerate(rows):
        b += (f'<div id="{cid}-r{i}" style="position:absolute;left:700px;top:{320 + i*130}px;width:1100px">'
              f'<div class="lab">{l}</div><div class="val" style="margin-top:6px">{v}</div></div>')
        j += f'  tl.fromTo(P+"r{i}", {{autoAlpha:0, y:26}}, {{autoAlpha:1, y:0, duration:0.45, ease:"power3.out"}}, {at});\n'
    # F-scale ladder that fills continuously
    for i in range(6):
        b += (f'<div id="{cid}-f{i}" style="position:absolute;left:{700 + i*170}px;top:730px;width:150px;height:76px;'
              f'background:#12202c;border:2px solid #2a3644;color:#f2f5f8;font-family:\'Arial Black\',Arial,sans-serif;'
              f'font-size:36px;text-align:center;line-height:76px;">F{i}</div>')
        j += f'  tl.fromTo(P+"f{i}", {{autoAlpha:0, scale:0.7}}, {{autoAlpha:1, scale:1, duration:0.3, ease:"power4.in"}}, {21.0 + i*0.5});\n'
    j += f'  tl.to(P+"f5", {{backgroundColor:"#8e2020", duration:0.5, ease:"power2.out"}}, 24.4);\n'
    j += f'  tl.to(P+"ph", {{scale:1.05, duration:{D-2:.1f}, ease:"none"}}, 1.0);\n'
    b += (f'<div id="{cid}-verdict" style="position:absolute;left:700px;top:850px"><span class="lab">TRI-STATE, RE-RATED</span>'
          f'<div style="font-family:\'Arial Black\',Arial,sans-serif;font-size:56px;color:#e74c3c;margin-top:6px">F5</div></div>')
    j += f'  tl.fromTo(P+"verdict", {{autoAlpha:0, y:26}}, {{autoAlpha:1, y:0, duration:0.5, ease:"power3.out"}}, 26.5);\n'
    b += f'<div class="foot" id="{cid}-ft">A scale built in the 1970s finally gave 1925 its number.</div>'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 33.0);\n'
    wrap(cid, style, b, j, D)
    return cid


# ---------------------------------------------------------------- g-wordban2
def wordban2():
    cid, D = "g-wordban2", 24.0
    style = """
  .big { position:absolute; left:0; right:0; top:300px; text-align:center; font-family:'Courier New',monospace;
    font-weight:700; font-size:150px; letter-spacing:16px; color:#f2f5f8; }
  .strike { position:absolute; left:50%; top:392px; height:12px; background:#c0392b; transform:translateX(-50%); width:0; }
  .step { position:absolute; top:640px; width:420px; text-align:center; }
  .step .yr { font-family:'Arial Black',Arial,sans-serif; font-size:56px; color:#e8c56a; }
  .step .tx { font-size:22px; letter-spacing:3px; color:#b8c6d4; font-weight:700; margin-top:10px; line-height:1.35; }
  .axis { position:absolute; left:220px; top:600px; height:5px; background:#2a3644; width:1480px; }
  .late { position:absolute; left:0; right:0; top:790px; text-align:center; }
  .late .n { font-family:'Courier New',monospace; font-size:84px; color:#e74c3c; font-weight:700; line-height:1; }
  .late .l { font-size:20px; letter-spacing:6px; color:#c8d3e0; font-weight:700; margin-top:8px; }
"""
    b, j = head(cid, "THE BOOKEND", "THE WORD COMES BACK", "but not in time for anyone in this story")
    b += (f'<div class="big" id="{cid}-w">TORNADO</div><div class="strike" id="{cid}-s"></div>'
          f'<div class="axis" id="{cid}-ax"></div>')
    steps = [("1938", "THE BAN BEGINS TO EASE", 250, 8.0),
             ("1948", "FIRST TORNADO FORECAST<br>TINKER AIR FORCE BASE", 750, 11.5),
             ("1952", "PUBLIC TORNADO WATCHES", 1250, 15.0)]
    for i, (yr, tx, x, at) in enumerate(steps):
        b += (f'<div class="step" id="{cid}-st{i}" style="left:{x}px"><div class="yr">{yr}</div>'
              f'<div class="tx">{tx}</div></div>')
        b += f'<div id="{cid}-dot{i}" style="position:absolute;left:{x + 205}px;top:592px;width:21px;height:21px;background:#e8c56a;border-radius:50%"></div>'
        j += f'  tl.fromTo(P+"st{i}", {{autoAlpha:0, y:30}}, {{autoAlpha:1, y:0, duration:0.45, ease:"power3.out"}}, {at});\n'
        j += f'  tl.fromTo(P+"dot{i}", {{scale:0}}, {{scale:1, duration:0.35, ease:"power4.in", transformOrigin:"50% 50%"}}, {at - 0.2});\n'
    b += (f'<div class="late" id="{cid}-late"><div class="n"><span id="{cid}-lv">0</span></div>'
          f'<div class="l">YEARS AFTER THE TRI-STATE</div></div>')
    b += f'<div class="foot" id="{cid}-ft" style="left:0;right:0;text-align:center">Every fix on this line arrived after the funerals.</div>'
    j += f'  tl.set(P+"s", {{width:760, scaleX:0, transformOrigin:"50% 50%"}}, 0);\n'
    j += f'  tl.to(P+"s", {{scaleX:1, duration:0.6, ease:"power3.out"}}, 1.4);\n'
    j += f'  tl.fromTo(P+"w", {{autoAlpha:0, scale:1.3}}, {{autoAlpha:1, scale:1, duration:0.5, ease:"power4.in"}}, 1.0);\n'
    j += f'  tl.to(P+"s", {{scaleX:0, duration:0.9, ease:"power3.inOut"}}, 5.2);\n'
    j += f'  tl.set(P+"ax", {{scaleX:0, transformOrigin:"left center"}}, 0);\n'
    j += f'  tl.to(P+"ax", {{scaleX:1, duration:{D - 6:.1f}, ease:"none"}}, 5.6);\n'
    j += f'  tl.to(P+"w", {{scaleX:1.16, duration:{D - 3:.1f}, ease:"none"}}, 1.5);\n'
    j += f'  tl.fromTo(P+"late", {{autoAlpha:0, y:24}}, {{autoAlpha:1, y:0, duration:0.5}}, 18.0);\n'
    j += f'  tl.to(LATE, {{v:23, duration:1.1, ease:"power4.out", onUpdate:lu}}, 18.2);\n'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 20.5);\n'
    js = ("  const LATE={v:0};\n  function lu(){const e=document.getElementById('%s-lv'); if(e) e.textContent=Math.round(LATE.v);}\n" % cid) + j
    wrap(cid, style, b, js, D)
    return cid


# ---------------------------------------------------------------- g-close
def close():
    cid, D = "g-close", 26.5
    style = """
  .ttl { position:absolute; left:0; right:0; top:400px; text-align:center; font-family:Georgia,serif;
    font-size:92px; color:#f2f5f8; letter-spacing:3px; }
  .epi { position:absolute; left:0; right:0; top:540px; text-align:center; font-family:Arial,sans-serif;
    font-weight:700; font-size:28px; color:#d8a13a; letter-spacing:6px; }
  .cred { position:absolute; left:0; right:0; top:700px; text-align:center; font-family:Arial,sans-serif;
    font-size:23px; line-height:2.0; color:#93a3b2; }
  .closing { position:absolute; left:0; right:0; text-align:center; font-family:Georgia,serif;
    font-style:italic; font-size:46px; color:#dfe7ee; }
  #g-close-l1 { top:420px; }
  #g-close-l2 { top:500px; }
  #g-close-l3 { top:580px; color:#d8a13a; }
"""
    b = (f'<div class="ttl" id="{cid}-t">The Warning Hour</div>'
         f'<div class="epi" id="{cid}-e">EPISODE THREE — THE TORNADO WITH NO PHOTOGRAPH</div>'
         f'<div class="cred" id="{cid}-c">Film courtesy Moving Image Research Collections, University of South Carolina<br>'
         f'Photographs: NWS Paducah · National Archives · Library of Congress · Jackson County Historical Society · The Indiana Album<br>'
         f'Reanalysis: Johns et al. 2013 · Maddox et al. 2013<br>'
         f'Some connecting scenes are modern recreations</div>')
    b += (f'<div class="closing" id="{cid}-l1">Disasters do not ask permission.</div>'
            f'<div class="closing" id="{cid}-l2">But they do send warnings.</div>'
            f'<div class="closing" id="{cid}-l3">Learn what yours sounds like.</div>')
    # cued to a6-s5 words.json: "Disasters" 0.0, "send warnings" 3.9, "Learn" 5.5
    j = (f'  tl.fromTo(P+"l1", {{autoAlpha:0, y:22}}, {{autoAlpha:1, y:0, duration:0.7, ease:"power3.out"}}, 0.30);\n'
         f'  tl.fromTo(P+"l2", {{autoAlpha:0, y:22}}, {{autoAlpha:1, y:0, duration:0.7, ease:"power3.out"}}, 3.70);\n'
         f'  tl.fromTo(P+"l3", {{autoAlpha:0, y:22}}, {{autoAlpha:1, y:0, duration:0.7, ease:"power3.out"}}, 5.30);\n'
         f'  tl.to([P+"l1", P+"l2", P+"l3"], {{autoAlpha:0, duration:0.8}}, 10.10);\n'
         f'  tl.fromTo(P+"t", {{autoAlpha:0, y:30}}, {{autoAlpha:1, y:0, duration:0.9, ease:"power3.out"}}, 11.28);\n'
         f'  tl.fromTo(P+"e", {{autoAlpha:0, y:24}}, {{autoAlpha:1, y:0, duration:0.7, ease:"power3.out"}}, 12.58);\n'
         f'  tl.fromTo(P+"c", {{autoAlpha:0}}, {{autoAlpha:1, duration:1.0}}, 16.60);\n'
         # scaleX, not letterSpacing: text-reflow properties snap per frame under capture
         f'  tl.to(P+"t", {{scaleX:1.05, duration:{D-13:.1f}, ease:"none"}}, 11.9);\n'
         f'  tl.to([P+"t", P+"e", P+"c"], {{autoAlpha:0, duration:1.6}}, {D-2.2:.1f});\n')
    wrap(cid, style, b, j, D)
    return cid


# ---------------------------------------------------------------- g-lone
def lone():
    """The 400-mile / seven-hour claim, shown on a map instead of asserted as text.

    Owner note on the v2 draft at 5:16: "wont a map show it better than the fucking
    mountain broll?" It would. The narration makes a spatial argument — NOT a squall
    line, ONE cell, 400 miles — so the graphic draws a squall line, kills it, and runs
    the survivor across the same tri-state geometry the track maps use.
    Cued to a1-s4d words.json: "squall" 8.66, "lone supercell" 10.22, "400 miles" 12.64,
    "seven hours" 14.78, "ground" 17.56, "longest lived" 25.76.
    """
    cid, D = "g-lone", 27.0
    style = """
  .cell { fill:#7a4a52; opacity:0.85; }
  .lonecell { fill:#c0392b; }
  .statelab2 { font-family:Georgia,serif; font-style:italic; font-size:27px; fill:#40607d; }
  /* bottom-right: the route climbs to (1596,330), so the UPPER right is where the map
     lives. A readout at top:250px put the cell marker on top of its own caption. */
  .rdg { position:absolute; right:96px; top:620px; text-align:right; }
  .rdgnum { font-family:'Courier New',monospace; font-size:76px; color:#e8c56a; font-weight:700; line-height:1; }
  .rdglab { font-size:19px; letter-spacing:4px; color:#93a3b2; font-weight:700; margin-top:6px; }
  .verdict { position:absolute; left:96px; top:262px; font-family:'Arial Black',Arial,sans-serif;
    font-size:40px; color:#f2f5f8; }
  .verdictsub { position:absolute; left:96px; top:318px; font-family:Georgia,serif;
    font-style:italic; font-size:25px; color:#b8c6d4; }
"""
    # the squall line the storm was NOT: a row of cells along a front, later struck out
    squall = "".join(
        f'<circle id="{cid}-sq{i}" class="cell" cx="{470 + i * 118}" cy="{836 - i * 44}" r="0"/>'
        for i in range(9))
    # same geometry as the track maps so the two read as one map
    route = "300,792 404,745 556,690 690,636 780,600 858,566 962,528 1046,496 1168,456 1332,412 1452,372 1596,330"
    b = (f'<svg viewBox="0 0 1920 1080" style="position:absolute;inset:0">'
         f'<defs><filter id="lglow"><feGaussianBlur stdDeviation="10" result="b"/>'
         f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
         f'<line x1="664" y1="150" x2="664" y2="1010" stroke="#16212c" stroke-width="3"/>'
         f'<line x1="1272" y1="150" x2="1272" y2="1010" stroke="#16212c" stroke-width="3"/>'
         f'<text x="470" y="994" class="statelab2">MISSOURI</text>'
         f'<text x="930" y="994" class="statelab2">ILLINOIS</text>'
         f'<text x="1450" y="994" class="statelab2">INDIANA</text>'
         f'<g id="{cid}-squall">{squall}'
         f'<line id="{cid}-sqx" x1="452" y1="854" x2="1420" y2="470" stroke="#8e2020" '
         f'stroke-width="5" stroke-dasharray="1040" stroke-dashoffset="1040"/></g>'
         f'<polyline id="{cid}-route" points="{route}" fill="none" stroke="#c0392b" stroke-width="8" '
         f'stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1360" stroke-dashoffset="1360"/>'
         f'<circle id="{cid}-cell" class="lonecell" cx="300" cy="792" r="0" filter="url(#lglow)"/>'
         f'<text id="{cid}-sqlab" x="452" y="906" class="maplab" opacity="0">A SQUALL LINE · MANY STORMS</text>'
         f'<text id="{cid}-onelab" x="252" y="742" class="maplab" opacity="0">ONE CELL</text>'
         f'</svg>')
    eb, j = head(cid, "MODERN REANALYSIS · JOHNS ET AL. 2013", "ONE LONE SUPERCELL",
                 "not a wall of storms — a single storm, all afternoon")
    b += eb
    b += (f'<div class="verdict" id="{cid}-vd">NOT A SQUALL LINE</div>'
          f'<div class="verdictsub" id="{cid}-vds">what crossed three states was one cell</div>'
          f'<div class="rdg" id="{cid}-rdg">'
          f'<div class="rdgnum"><span id="{cid}-mi">0</span> MI</div>'
          f'<div class="rdglab">GROUND COVERED BY THE PARENT STORM</div>'
          f'<div class="rdgnum" style="margin-top:34px"><span id="{cid}-hr">0.0</span> HR</div>'
          f'<div class="rdglab">CONTINUOUSLY ALOFT</div></div>'
          f'<div class="foot" id="{cid}-ft">Among the longest-lived supercells ever documented</div>')

    j += f'  const MI = {{v:0}}, HR = {{v:0}};\n'
    j += (f'  function miUpd(){{ const e=document.getElementById("{cid}-mi");'
          f' if(e) e.textContent = Math.round(MI.v); }}\n')
    j += (f'  function hrUpd(){{ const e=document.getElementById("{cid}-hr");'
          f' if(e) e.textContent = HR.v.toFixed(1); }}\n')
    # the squall line builds, gets struck out, and only one cell survives
    for i in range(9):
        j += (f'  tl.fromTo(P+"sq{i}", {{attr:{{r:0}}}}, {{attr:{{r:21}}, duration:0.34, '
              f'ease:"power3.out"}}, {5.90 + i * 0.14:.2f});\n')
    j += f'  tl.fromTo(P+"sqlab", {{opacity:0}}, {{opacity:0.85, duration:0.5}}, 6.40);\n'
    j += f'  tl.to(P+"sqx", {{strokeDashoffset:0, duration:0.85, ease:"power2.in"}}, 8.66);\n'
    j += f'  tl.to(P+"squall", {{autoAlpha:0, duration:0.9}}, 9.60);\n'
    j += (f'  tl.fromTo(P+"cell", {{attr:{{r:0}}}}, {{attr:{{r:19}}, duration:0.5, '
          f'ease:"back.out(2)"}}, 10.22);\n')
    j += f'  tl.fromTo(P+"onelab", {{opacity:0}}, {{opacity:0.9, duration:0.5}}, 10.60);\n'
    j += f'  tl.to(P+"onelab", {{autoAlpha:0, duration:0.6}}, 13.40);\n'
    # the continuous element: the cell crosses the route for the rest of the window
    # MotionPathPlugin is not in the bundled gsap.min.js — walk the waypoints with
    # cx/cy attr tweens, each leg timed to its own length so the speed stays constant.
    pts = [tuple(int(v) for v in p.split(",")) for p in route.split()]
    legs = [((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5 for a, b in zip(pts, pts[1:])]
    span, at = D - 12.0, 11.60
    j += f'  tl.to(P+"route", {{strokeDashoffset:0, duration:{span:.2f}, ease:"none"}}, {at:.2f});\n'
    for (x, y), leg in zip(pts[1:], legs):
        dt = span * leg / sum(legs)
        j += (f'  tl.to(P+"cell", {{attr:{{cx:{x}, cy:{y}}}, duration:{dt:.2f}, '
              f'ease:"none"}}, {at:.2f});\n')
        at += dt
    j += f'  tl.to(MI, {{v:412, duration:11.20, ease:"none", onUpdate:miUpd}}, 12.64);\n'
    j += f'  tl.to(HR, {{v:7.0, duration:10.60, ease:"none", onUpdate:hrUpd}}, 14.78);\n'
    j += f'  tl.fromTo(P+"vd", {{autoAlpha:0, x:-40}}, {{autoAlpha:1, x:0, duration:0.6, ease:"power3.out"}}, 8.90);\n'
    j += f'  tl.fromTo(P+"vds", {{autoAlpha:0, x:-30}}, {{autoAlpha:1, x:0, duration:0.6, ease:"power3.out"}}, 10.30);\n'
    j += f'  tl.fromTo(P+"rdg", {{autoAlpha:0, x:40}}, {{autoAlpha:1, x:0, duration:0.6, ease:"power3.out"}}, 12.20);\n'
    j += f'  tl.fromTo(P+"ft", {{autoAlpha:0, y:20}}, {{autoAlpha:1, y:0, duration:0.6}}, 25.76);\n'
    wrap(cid, style, b, j, D)
    return cid


if __name__ == "__main__":
    made = [sources(), wires(), relief(), family(), fujita(), wordban2(), close(), lone()]
    print("[gen_misc] wrote:", ", ".join(made))
