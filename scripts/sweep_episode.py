"""Every static check I can make against the episode, in one pass.

Each check prints PASS/FAIL and the offending items. No check depends on a render.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")
fails = []


def report(name, bad, detail=lambda x: str(x)):
    if bad:
        fails.append(name)
        print(f"FAIL {name}: {len(bad)}")
        for b in bad[:8]:
            print("      ", detail(b))
    else:
        print(f"PASS {name}")


# ---- windows -------------------------------------------------------------
wins = []
for m in re.finditer(r'<(section|video|div)\b([^>]*)>', h):
    a = m.group(2)
    st, du, tr = (re.search(r'data-start="([\d.]+)"', a),
                  re.search(r'data-duration="([\d.]+)"', a),
                  re.search(r'data-track-index="(\d+)"', a))
    if not (st and du and tr):
        continue
    cid = re.search(r'data-composition-id="([^"]+)"', a)
    src = re.search(r'src="([^"]+)"', a)
    if not src and not cid and 'blackout' in a:
        # deliberate black dip: a valid window with no asset of its own —
        # never scan forward or it inherits the NEXT clip's src
        wins.append(dict(at=float(st.group(1)), dur=float(du.group(1)),
                         tr=int(tr.group(1)), name="[blackout]"))
        continue
    if not src and not cid:
        inner = h[m.end():m.end() + 900]
        s2 = re.search(r'src="([^"]+)"', inner)
        src = s2
    wins.append(dict(at=float(st.group(1)), dur=float(du.group(1)), tr=int(tr.group(1)),
                     name=cid.group(1) if cid else (src.group(1) if src else "?")))

pic = sorted([w for w in wins if w["tr"] in (1, 2)], key=lambda w: w["at"])

# 1. picture coverage
total = round(float(re.search(r'data-duration="([\d.]+)"', h).group(1)))
cur, holes = 0.0, []
for w in sorted(pic, key=lambda w: w["at"]):
    if w["at"] > cur + 0.05:
        holes.append((round(cur, 2), round(w["at"], 2)))
    cur = max(cur, w["at"] + w["dur"])
if cur < total - 0.05:
    holes.append((round(cur, 2), total))
report("picture coverage (no black)", holes, lambda x: f"{x[0]}s -> {x[1]}s")

# 2. same-track overlap
ov = []
for tr in {w["tr"] for w in wins}:
    t = sorted([w for w in wins if w["tr"] == tr], key=lambda w: w["at"])
    for a, b in zip(t, t[1:]):
        if a["at"] + a["dur"] - b["at"] > 0.005:
            ov.append((tr, a["name"], b["name"], round(a["at"] + a["dur"] - b["at"], 3)))
report("same-track overlap", ov, lambda x: f"track {x[0]} {x[1]} over {x[2]} by {x[3]}s")

# 3. adjacent duplicate cuts on track 1
t1 = [w for w in pic if w["tr"] == 1]
dup = [(a["at"], a["name"]) for a, b in zip(t1, t1[1:]) if a["name"] == b["name"]]
report("adjacent duplicate cuts", dup, lambda x: f"{x[0]}s {Path(x[1]).name}")

# 4. reuse ceiling (3 uses)
uses = Counter(w["name"] for w in t1)
report("asset reuse <= 3", [(n, c) for n, c in uses.items() if c > 3],
       lambda x: f"{Path(x[0]).name} x{x[1]}")

# 5. missing media
miss = [w["name"] for w in pic if w["tr"] == 1 and not (ep / w["name"]).exists()]
report("media files exist", sorted(set(miss)))

# 6. authored but unmounted compositions
authored = {p.stem for p in (ep / "compositions").glob("*.html")}
mounted = {w["name"] for w in pic if w["tr"] == 2}
report("no unmounted compositions", sorted(authored - mounted))
report("no missing compositions", sorted(mounted - authored))

# 7. graphic window vs its own timeline length
overrun = []
for gid in sorted(mounted):
    src = (ep / "compositions" / f"{gid}.html").read_text(encoding="utf-8", errors="replace")
    ends = [float(m.group(1)) + max([float(d) for d in re.findall(
        r'duration:\s*([\d.]+)', m.group(0))] or [0])
        for m in re.finditer(r'tl\.\w+\([^;]*?,\s*([\d.]+)\s*\);', src)]
    if not ends:
        continue
    tl_end = max(ends)
    # The last DISCRETE beat, not the end of the timeline. Clipping the tail of a
    # continuous element loses nothing a viewer can name; cutting a reveal does. The two
    # are told apart by HOW they are eased, not by how long they run: a continuous element
    # is a long linear drift (ease "none" — the grain drift, the map push, g-metmap's 14s
    # zone rotation), while a beat lands with an entrance ease. A duration-fraction rule
    # got this wrong, which is how this check first cried wolf on g-metmap.
    beats = []
    for m in re.finditer(r'tl\.\w+\([^;]*?,\s*([\d.]+)\s*\);', src):
        body = m.group(0)
        d = max([float(x) for x in re.findall(r'duration:\s*([\d.]+)', body)] or [0])
        if d > 4.0 and re.search(r'ease:\s*"none"', body):
            continue                      # continuous, not a beat
        beats.append(float(m.group(1)) + d)
    last_beat = max(beats) if beats else 0.0
    for w in pic:
        if w["name"] != gid:
            continue
        if w["dur"] - tl_end > 4.0:
            overrun.append(("holds", gid, round(w["dur"], 1), round(tl_end, 1)))
        # the direction this check used to ignore entirely: a mount SHORTER than the
        # composition cuts off its own authored reveals
        elif last_beat - w["dur"] > 0.30:
            overrun.append(("cuts a beat", gid, round(w["dur"], 1), round(last_beat, 1)))
report("graphic window fits its timeline", overrun,
       lambda x: f"{x[0]:9} {x[1]} window {x[2]}s vs timeline {x[3]}s")

# NOTE: there is deliberately no "cue alignment" check here. One used to sit at this
# spot; it initialised an empty findings list, never appended to it, and printed PASS on
# every input. A gate that cannot fail is worse than no gate, because it is counted as
# coverage. Reveal-vs-spoken-word alignment is still verified by reading words.json when
# a composition is authored — it is not, and must not pretend to be, automated here.

# 9. long stills
long_still = [(w["at"], w["name"], w["dur"]) for w in t1
              if w["dur"] > 12.0 and not w["name"].endswith(".mp4")]
report("no still over 12s", long_still, lambda x: f"{x[0]}s {Path(x[1]).name} {x[2]}s")

print()
print("SWEEP", "FAIL" if fails else "PASS", "-", len(fails), "failing checks")
