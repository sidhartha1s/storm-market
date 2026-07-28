#!/usr/bin/env python3
"""Generate ep3 stat-panel sub-compositions in the ep2 anatomy (DESIGN.md §2).

A panel is an OVERLAY: 820px full-height gradient card on the right, archival photo still
running underneath with its Ken Burns move. v2's version was a 560px box parked in the top
right corner — the owner's "you're making me look at stuff instead of showing it" note.

Row schema: (label, value, offset_seconds). Offsets are spoken-word times inside the window.
"""
from pathlib import Path

EP = Path(__file__).resolve().parent.parent / "episodes" / "ep3-tristate"
OUT = EP / "compositions"
OUT.mkdir(exist_ok=True)

STYLE = """
  #root { position:absolute; inset:0; font-family:Arial, sans-serif; }
  .panel { position:absolute; right:0; top:0; bottom:0; width:820px; box-sizing:border-box;
    background:linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0)); padding:90px 70px 0 170px; }
  .eyebrow { font-size:22px; letter-spacing:6px; color:#93a3b2; font-weight:700; }
  .tname { font-family:'Arial Black',Arial,sans-serif; font-size:52px; color:#f2f5f8; line-height:1.05; margin-top:14px; }
  .tsub { font-family:Georgia,serif; font-style:italic; font-size:26px; color:#d8a13a; margin-top:10px; }
  .stamp { display:inline-block; margin-top:34px; font-family:'Arial Black',Arial,sans-serif; font-size:96px;
    color:#fff; background:#8e2020; padding:2px 30px; letter-spacing:2px; }
  .row { font-size:30px; color:#dfe7ee; font-weight:700; letter-spacing:1px; margin-top:22px; }
  .row .lab { display:block; font-size:19px; color:#93a3b2; letter-spacing:4px; font-weight:700; }
  .cnt { font-family:'Courier New',monospace; font-size:84px; color:#e74c3c; font-weight:700; margin-top:26px; line-height:1; }
  .cntlab { font-size:20px; color:#c8d3e0; letter-spacing:6px; font-weight:700; margin-top:6px; }
  .tick { position:absolute; left:110px; width:4px; background:#8e2020; }
"""

# id, eyebrow, name, sub, stamp, rows[(label,value,at)], counter(value,label,at) | None, dur
PANELS = [
    ("g-panel-lone", "THE PARENT STORM · MODERN REANALYSIS", "ONE SUPERCELL", "Johns, Burgess et al. · 2013",
     None, [("TIME ALOFT", "SEVEN HOURS", 2.6), ("DISTANCE", "~413 MILES", 5.2),
            ("", "Among the longest-lived storms ever documented", 8.4)], None, 13.5),
    ("g-panel-annapolis", "1:14 PM · MISSOURI", "ANNAPOLIS", "Iron County · a mining town of a few hundred",
     None, [("BUILDINGS DESTROYED", "NINE OF EVERY TEN", 2.2),
            ("WARNING GIVEN", "NONE", 5.0)], None, 9.0),
    ("g-panel-gorham", "2:26 PM · ILLINOIS", "GORHAM", "Jackson County · population 500",
     None, [("KILLED", "ONE IN FIFTEEN RESIDENTS", 3.0)], (34, "DEAD", 5.4), 9.5),
    ("g-panel-f5", "MODERN DAMAGE SURVEY", "RATED F5", "the highest rating wind can earn",
     "F5", [("EVIDENCE", "PLANKS DRIVEN THROUGH LIVING TREES", 4.2),
            ("HOMES", "SWEPT FROM THEIR FOUNDATIONS", 7.0)], None, 12.0),
    ("g-panel-murphysboro", "2:34 PM · ILLINOIS", "MURPHYSBORO", "Jackson County · population 12,000",
     None, [("TIME IN TOWN", "THREE MINUTES", 4.0), ("INJURED", "623", 8.0),
            ("", "More than one person hurt or killed EVERY SECOND", 12.0),
            ("", "No American town has ever lost more to a tornado", 17.5)],
     (234, "DEAD", 2.2), 24.0),
    ("g-panel-desoto", "2:45 PM · ILLINOIS", "DE SOTO SCHOOL", "the deadliest school tornado in US history",
     None, [("KILLED WHERE THEY SAT", "THE NORTH WALL FELL FIRST", 4.6)], (33, "CHILDREN", 2.4), 10.0),
    ("g-panel-wf", "3:00 PM · ILLINOIS", "WEST FRANKFORT", "a coal town of 18,000",
     None, [("THE MEN", "500 FEET UNDERGROUND", 2.8),
            ("THE DEAD", "MOSTLY WOMEN AND CHILDREN", 6.0)], None, 10.0),
    ("g-panel-parrish", "3:07 PM · ILLINOIS", "PARRISH", "Williamson County",
     None, [("BUILDINGS GONE", "NINE OF TEN", 2.4), ("REBUILT", "NEVER", 5.2)], (22, "DEAD", 3.6), 9.0),
    ("g-panel-griffin", "~4:00 PM · INDIANA", "GRIFFIN", "Posey County · the town the storm erased",
     None, [("INJURED", "OVER 200", 3.0), ("STRUCK", "SIX OF EVERY TEN PEOPLE IN TOWN", 5.6)],
     (25, "DEAD", 2.0), 10.0),
    ("g-panel-princeton", "4:18 PM · INDIANA", "PRINCETON", "Gibson County · the storm's last town",
     None, [("HOMES DESTROYED", "OVER 400", 3.4)], (45, "DEAD", 2.0), 9.0),
    ("g-panel-redcross", "THE RESPONSE · 1925", "AMERICAN RED CROSS", "there was no federal disaster agency to call",
     None, [("RAISED AND SPENT", "OVER $3,000,000", 2.6), ("FAMILIES SERVED", "MORE THAN 7,000", 5.4),
            ("DURATION", "A FULL YEAR OF RELIEF WORK", 8.0)], None, 11.5),
    ("g-panel-schools", "THE HOUR IT CHOSE", "48 SCHOOLS", "in the path, mid-afternoon",
     None, [("DISMISSAL", "THREE THIRTY", 4.4), ("THE TORNADO", "CAME FIRST", 7.0)],
     (48, "SCHOOLS IN THE PATH", 2.0), 12.0),
    ("g-panel-cost", "THE BILL · MARCH 1925", "$16.5 MILLION", "in 1925 dollars",
     None, [("IN TODAY'S MONEY", "ABOUT $3 BILLION", 3.6),
            ("HOMES DESTROYED", "15,000", 6.4)], None, 10.0),
    ("g-panel-nonet", "1925 · WHAT DID NOT EXIST", "NO SAFETY NET", "no FEMA, no federal disaster declaration",
     None, [("WHO CAME", "CHURCHES · NEIGHBOURS · RAILROADS", 3.2),
            ("WHO PAID", "THE SURVIVORS, MOSTLY", 6.6)], None, 11.0),
    ("g-panel-song", "MURPHYSBORO · SPRING 1925", "“AFTER THE TORNADO IS OVER”", "sheet music sold for survivor relief",
     None, [("WRITTEN BY", "A TOWN THAT HAD JUST BURIED 234", 3.8)], None, 9.5),
]


def build(cid, eyebrow, name, sub, stamp, rows, counter, dur):
    P = f"{cid}-"
    html_rows = []
    for i, (lab, val, at) in enumerate(rows):
        lab_html = f'<span class="lab">{lab}</span>' if lab else ''
        html_rows.append(f'<div class="row" id="{P}r{i}">{lab_html}{val}</div>')
    stamp_html = f'<div><span class="stamp" id="{P}stamp">{stamp}</span></div>' if stamp else ''
    cnt_html = ''
    if counter:
        cnt_html = f'<div class="cnt" id="{P}cnt">0</div><div class="cntlab" id="{P}cntlab">{counter[1]}</div>'

    body = f"""<div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080">
  <div class="panel" id="{P}panel">
    <div class="eyebrow">{eyebrow}</div>
    <div class="tname">{name}</div>
    <div class="tsub">{sub}</div>
    {stamp_html}
    {cnt_html}
    {''.join(html_rows)}
  </div>
</div>"""

    hide = [f"#{P}r{i}" for i in range(len(rows))]
    if stamp:
        hide.append(f"#{P}stamp")
    if counter:
        hide += [f"#{P}cnt", f"#{P}cntlab"]
    hide_js = ", ".join(f'"{h}"' for h in hide)
    j = [
        "window.__timelines = window.__timelines || {};",
        "(function() {",
        "  const tl = gsap.timeline({ paused: true });",
        f'  const P = "#{cid}-";',
        f'  tl.set([{hide_js}], {{autoAlpha:0}}, 0);' if hide else "",
        f'  tl.fromTo(P+"panel", {{x:660}}, {{x:0, duration:0.7, ease:"power3.out"}}, 0.0);',
    ]
    if stamp:
        j.append(f'  tl.fromTo(P+"stamp", {{scale:2.6, autoAlpha:0}}, {{scale:1, autoAlpha:1, duration:0.35, ease:"power4.in"}}, 1.0);')
    if counter:
        val, lab, at = counter
        j.append(f'  tl.set([P+"cnt", P+"cntlab"], {{autoAlpha:1}}, {at});')
        j.append(f'  tl.to(CNT, {{v:{val}, duration:0.9, ease:"power4.out", onUpdate:cntUpd}}, {at});')
    for i, (lab, val, at) in enumerate(rows):
        j.append(f'  tl.fromTo(P+"r{i}", {{autoAlpha:0, y:24}}, {{autoAlpha:1, y:0, duration:0.4, ease:"power3.out"}}, {at});')
    j.append(f'  tl.to(P+"panel", {{x:980, autoAlpha:0, duration:0.6, ease:"power3.in"}}, {dur - 0.7:.2f});')
    j.append(f'  window.__timelines["{cid}"] = tl;')
    j.append("})();")
    js = "\n".join(x for x in j if x)
    if counter:
        js = js.replace("(function() {",
                        "(function() {\n  const CNT = {v:0};\n"
                        f'  function cntUpd(){{const e=document.getElementById("{cid}-cnt"); if(e) e.textContent=Math.round(CNT.v);}}')

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
    made = [build(*p) for p in PANELS]
    print(f"[gen_panels] wrote {len(made)} panel compositions")
    for cid, dur in made:
        print(f"  {cid}  {dur}s")
