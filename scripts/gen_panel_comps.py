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


import json as _json, re as _re

_UNITS = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,
 "nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,
 "seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,
 "sixty":60,"seventy":70,"eighty":80,"ninety":90}


def _to_digits(tokens):
    """Whisper writes numbers as digits ("234"); scripts spell them out
    ("two hundred thirty-four"). Collapse spelled runs so cues still match."""
    out, i = [], 0
    while i < len(tokens):
        if tokens[i] in _UNITS or tokens[i] == "hundred":
            total, cur, j = 0, 0, i
            while j < len(tokens) and (tokens[j] in _UNITS or tokens[j] in ("hundred", "thousand")):
                t = tokens[j]
                if t == "hundred":
                    cur = (cur or 1) * 100
                elif t == "thousand":
                    total += (cur or 1) * 1000
                    cur = 0
                else:
                    cur += _UNITS[t]
                j += 1
            val = total + cur
            if j > i and val:
                out.append(str(val))
                i = j
                continue
        out.append(tokens[i])
        i += 1
    return out


def cue(seg, phrase, fallback):
    """Reveal times come from the narration, not a metronome (DESIGN.md §6, ep2 g-met).
    Returns the spoken start of `phrase` in audio/<seg>.words.json minus a 0.2s pre-roll."""
    wp = EP / "audio" / f"{seg}.words.json"
    if not wp.exists():
        return fallback
    words = _json.loads(wp.read_text(encoding="utf-8"))
    norm = lambda t: _re.sub(r"[^a-z0-9]", "", t.lower())
    toks = [norm(w["text"]) for w in words]
    want = [t for t in (norm(x) for x in phrase.replace("-", " ").split()) if t]
    if not want:
        return fallback
    for cand in (want, _to_digits(want)):
        for i in range(len(toks) - len(cand) + 1):
            if toks[i:i + len(cand)] == cand:
                return max(0.4, round(words[i]["start"] - 0.2, 2))
    dig = _to_digits(want)
    for i, t in enumerate(toks):            # last resort: first distinctive token
        if t and (t == dig[0] or t == want[0]) and len(t) > 3:
            return max(0.4, round(words[i]["start"] - 0.2, 2))
    print(f"  [cue] no match in {seg}: \"{phrase}\" -> fallback {fallback}s")
    return fallback


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
  .tick { position:absolute; left:110px; top:96px; width:4px; height:0;
    background:linear-gradient(180deg, #8e2020 0%, #d8a13a 100%); }
"""

# id, eyebrow, name, sub, stamp, rows[(label,value,at)], counter(value,label,at) | None, dur
PANELS = [
    ("g-panel-finley", "1880s · THE SCIENCE THAT WAS STOPPED", "JOHN PARK FINLEY", "US Army Signal Corps · experimental tornado alerts",
     None, [("HE FOUND", "REAL PATTERNS BEFORE TORNADOES", 3.0),
            ("HIS PROGRAMME", "SHUT DOWN — FEAR OF PANIC", 6.0),
            ("", "American forecasting looked away for two generations", 9.5)], None, 15.0,
     "a1-s1b", {"r0": "finding real patterns", "r1": "His work was shut down", "r2": "for two generations"}),
    ("g-panel-lone", "MODERN REANALYSIS · JOHNS ET AL. 2013", "ONE LONE SUPERCELL", "not a squall line — a single storm",
     None, [("DISTANCE", "MORE THAN 400 MILES", 2.6), ("TIME ALOFT", "ABOUT SEVEN HOURS", 5.2),
            ("", "Among the longest-lived storms ever documented", 8.4)], None, 14.0,
     "a1-s4d", {"r0": "crossing more than four hundred miles", "r1": "in about seven hours", "r2": "ranks among the longest lived"}),
    ("g-panel-annapolis", "1:14 PM · MISSOURI", "ANNAPOLIS", "a lead-mining town of a few hundred",
     None, [("TIME IN TOWN", "UNDER ONE MINUTE", 2.2),
            ("BUILDINGS DESTROYED", "NINE OF EVERY TEN", 5.0),
            ("", "The storm's first town. Not the worst.", 8.0)], None, 12.0,
     "a2-s2", {"r0": "It crossed the town in under a minute", "r1": "nine of every ten buildings", "r2": "It would not be the worst"}),
    ("g-panel-gorham", "DAMAGE SURVEY · GORHAM, ILLINOIS", "RATED F5", "the highest rating wind can earn",
     "F5", [("THE EVIDENCE", "PLANKS DRIVEN THROUGH LIVING TREES", 3.0),
            ("STILL EXISTS", "A PIERCED TRUNK IN A JACKSON COUNTY MUSEUM", 6.5),
            ("WHY", "SOFT PINE CANNOT PIERCE HARDWOOD BELOW F5 WINDS", 10.0)], None, 16.0,
     "a3-s1b", {"r0": "driven through the trunks", "r1": "still sits in a museum", "r2": "Physics has a blunt explanation"}),
    ("g-panel-murphysboro", "2:34 PM · ILLINOIS", "MURPHYSBORO", "Jackson County · population 12,000",
     None, [("INJURED", "623", 8.0), ("TIME IN TOWN", "ABOUT THREE MINUTES", 11.0),
            ("", "More than one person killed or wounded EVERY SECOND", 14.0),
            ("", "No American town, before or since, has lost so many", 18.5)],
     (234, "DEAD", 4.0), 25.0,
     "a3-s4c", {"cnt": "Two hundred thirty-four dead", "r0": "Six hundred twenty-three injured",
                "r1": "in about three minutes", "r2": "every single second", "r3": "No American town"}),
    ("g-panel-desoto", "2:45 PM · ILLINOIS", "THE SCHOOL DAY", "it struck mid-afternoon, on a school day",
     None, [("LONGFELLOW · LOGAN · DE SOTO", "THE BIGGEST BUILDING ON THE STREET", 5.0),
            ("", "Again and again, the deadliest address in town", 9.0)],
     (33, "CHILDREN KILLED AT DE SOTO", 2.4), 13.0,
     "a3-s6b", {"r0": "the school was often the biggest building", "r1": "the deadliest address in town"}),
    ("g-panel-schools", "MAPPED DAMAGE POINTS", "48 SCHOOLS", "one-room schoolhouses, two miles apart",
     None, [("WHY TWO MILES", "WALKING DISTANCE FOR A CHILD IN 1925", 5.0),
            ("", "The geography that made school reachable put one in the path", 9.0)],
     (48, "SCHOOLS IN THE PATH", 2.0), 13.0,
     "a3-s6c", {"cnt": "Forty-eight of those damage points", "r0": "walking distance for a child", "r1": "The geography that made school"}),
    ("g-panel-wf", "3:00 PM · ILLINOIS", "WEST FRANKFORT", "a coal city of eighteen thousand",
     None, [("THE MEN", "FIVE HUNDRED FEET UNDERGROUND", 2.8),
            ("THE POWER DIED", "THEY CLIMBED OUT BY LADDER", 6.0),
            ("THE DEAD", "OVERWHELMINGLY WOMEN AND CHILDREN", 9.5)], None, 14.0,
     "a3-s7", {"r0": "five hundred feet underground", "r1": "climbed out by ladder", "r2": "because the men were underground"}),
    ("g-panel-parrish", "3:07 PM · ILLINOIS", "PARRISH", "Williamson County — the town that never came back",
     None, [("BUILDINGS DESTROYED", "NINE OF EVERY TEN", 2.4),
            ("REBUILT", "NEVER", 5.2),
            ("", "The storm could erase the place itself", 8.0)], (22, "DEAD", 1.6), 11.0,
     "a3-s8", {"cnt": "Twenty-two dead", "r0": "nine of every ten buildings", "r1": "Parrish never came back", "r2": "erase the place itself"}),
    ("g-panel-griffin", "~4:00 PM · INDIANA", "THREE HOURS ON THE GROUND", "a typical tornado lives for minutes",
     None, [("CROSSED", "TWO ENTIRE STATES, STARTING A THIRD", 3.0),
            ("WITHOUT", "WEAKENING · LIFTING · LETTING GO", 6.0),
            ("", "Meteorologists have argued for a century about how", 9.0)], None, 13.0,
     "a4-s1b", {"r0": "crossed two entire states", "r1": "without weakening", "r2": "argued for a century"}),
    ("g-panel-princeton", "4:18 PM · INDIANA", "THE NEAR MISS", "a field away, and untouched",
     None, [("THE MARGIN", "A FEW HUNDRED FEET · A FEW SECONDS", 4.0),
            ("SOMETIMES", "WHICH ROOM OF THE HOUSE YOU STOOD IN", 8.0)], None, 12.0,
     "a4-s2b", {"r0": "a few hundred feet or a few seconds", "r1": "which room of the house"}),
    ("g-panel-redcross", "THE RESPONSE · 1925", "AMERICAN RED CROSS", "built on volunteers and donations",
     None, [("SPENT", "OVER $3,000,000 IN 1920s DOLLARS", 2.6),
            ("DURATION", "A FULL YEAR OF RELIEF WORK", 5.4),
            ("FAMILIES", "MORE THAN 7,000 HOMELESS OR BROKEN", 8.0)], None, 13.0,
     "a5-s1c", {"r0": "over three million", "r1": "ran for a full year", "r2": "More than seven thousand families"}),
    ("g-panel-nonet", "1925 · WHAT DID NOT EXIST", "NOBODY ELSE WAS COMING", "disasters were local problems",
     None, [("NO", "FEDERAL DISASTER AGENCY", 2.4),
            ("NO", "EMERGENCY MANAGEMENT OF ANY KIND", 5.0),
            ("WHO REBUILT IT", "CHURCHES · NEIGHBOURS · RAILROADS · ONE CHARITY", 8.5)], None, 13.0,
     "a5-s1d", {"r0": "no federal disaster agency", "r1": "no emergency management", "r2": "rebuilt by churches"}),
    ("g-panel-cost", "THE BILL · MARCH 1925", "$16.5 MILLION", "in nineteen twenty-five money",
     None, [("IN TODAY'S MONEY", "ON THE ORDER OF $3 BILLION", 3.6),
            ("", "Not one city absorbing a disaster", 7.0),
            ("", "A chain of small towns, each losing everything at once", 10.0)], None, 14.0,
     "a5-s3b", {"r0": "on the order of three billion", "r1": "not one city absorbing", "r2": "a chain of small towns"}),
    ("g-panel-song", "MURPHYSBORO · SPRING 1925", "“AFTER THE TORNADO IS OVER”", "written in the ruins, sold for the survivors",
     None, [("THE TOWN", "HAD JUST BURIED 234 OF ITS OWN", 3.8),
            ("", "There was before the storm, and there was after", 7.5)], None, 11.0,
     "a5-s4", {"r0": "sold to raise money for the survivors", "r1": "There was before the storm"}),
]


def build(cid, eyebrow, name, sub, stamp, rows, counter, dur, seg=None, cues=None):
    cues = cues or {}
    if seg:
        rows = [(l, v, cue(seg, cues.get(f"r{i}", ""), at)) for i, (l, v, at) in enumerate(rows)]
        if counter:
            counter = (counter[0], counter[1], cue(seg, cues.get("cnt", ""), counter[2]))
        rows = sorted(rows, key=lambda r: r[2])
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
    <div class="tick" id="{P}tick"></div>
    <div class="eyebrow" id="{P}eb">{eyebrow}</div>
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
        # two elements run the whole window so the card is never a frozen still (§5)
        f'  tl.fromTo(P+"tick", {{height:0}}, {{height:900, duration:{dur - 1.4:.2f}, ease:"none"}}, 0.7);',
        f'  tl.fromTo(P+"eb", {{letterSpacing:"6px"}}, {{letterSpacing:"11px", duration:{dur - 1.4:.2f}, ease:"none"}}, 0.7);',
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
