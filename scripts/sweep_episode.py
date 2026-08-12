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
        for b in bad[:40]:  # a truncated report hid 16 of 24 family findings once — print them all
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
    cls = re.search(r'class="([^"]*)"', a)
    is_black = bool(cls and "blackout" in cls.group(1))
    if not src and not cid and not is_black:
        inner = h[m.end():m.end() + 900]
        s2 = re.search(r'src="([^"]+)"', inner)
        src = s2
    wins.append(dict(at=float(st.group(1)), dur=float(du.group(1)), tr=int(tr.group(1)),
                     name="[blackout]" if is_black else
                          (cid.group(1) if cid else (src.group(1) if src else "?"))))

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

# 3. adjacent duplicate cuts on track 1 (blackouts are structure, not footage)
t1 = [w for w in pic if w["tr"] == 1 and w["name"] != "[blackout]"]
dup = [(a["at"], a["name"]) for a, b in zip(t1, t1[1:]) if a["name"] == b["name"]]
report("adjacent duplicate cuts", dup, lambda x: f"{x[0]}s {Path(x[1]).name}")

# 4. reuse ceiling (3 uses)
uses = Counter(w["name"] for w in t1)
report("asset reuse <= 3", [(n, c) for n, c in uses.items() if c > 3],
       lambda x: f"{Path(x[0]).name} x{x[1]}")

# 5. missing media
miss = [w["name"] for w in t1 if not (ep / w["name"]).exists()]
report("media files exist", sorted(set(miss)))

# 5b. duplicate element ids — hyperframes keys frame placement by id; a duplicate
# renders one window BLACK while every attribute-level check passes (ep5 v1, 8s hole)
ids = Counter(re.findall(r' id="([^"]+)"', h))
report("element ids unique", sorted(n for n, c in ids.items() if c > 1))

# 5c. visual-identity repeats — the viewer sees SOURCES, not filenames. Cuts a/b/c of one
# homogeneous source read as the same clip (ep5 v1: burnaer02 family 16x, fire02 4x in
# the first five minutes). Flag any source family appearing twice within 60s, or >6/episode.
fam_uses = {}
for w in t1:
    fam = re.sub(r'-[a-f]\.mp4$', '', Path(w["name"]).name).replace(".mp4", "")
    # victim portraits deliberately RETURN within their own vignette (namecard -> face ->
    # quote); that is narrative continuation, not a b-roll repeat — the owner's complaint
    if fam.startswith("portrait-"):
        continue
    fam_uses.setdefault(fam, []).append((w["at"], w["at"] + w["dur"]))
fam_bad = []
for fam, fwins in fam_uses.items():
    fwins.sort()
    # a cut that CONTINUES the same source (next window starts as the last ends) is one
    # sequence, not a repeat — the sin is interruption-and-return, not a split shot
    tight = [(a[0], b[0]) for a, b in zip(fwins, fwins[1:])
             if b[0] - a[0] < 60 and b[0] - a[1] > 0.5
             # the hook montage's cold-open -> payoff return (owner-approved v4 shape:
             # the signature shot opens at 0s and lands again on the thesis line before
             # the title) is structure, not a footage-shortage repeat
             and not (a[0] < 35 and b[0] < 35)]
    ats = [w[0] for w in fwins]
    if tight:
        fam_bad.append((fam, f"{len(ats)}x, {len(tight)} pair(s) <60s apart at {int(tight[0][0])}s"))
    elif len(ats) > 6:
        fam_bad.append((fam, f"{len(ats)}x across the episode"))
report("source-family repeats (viewer identity)", fam_bad, lambda x: f"{x[0]}: {x[1]}")

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

# 9. long stills — owner 2026-08-12: stills are 3-6s with motion, "not a PowerPoint"
long_still = [(w["at"], w["name"], w["dur"]) for w in t1
              if w["dur"] > 6.0 and not w["name"].endswith(".mp4")]
report("no still over 6s", long_still, lambda x: f"{x[0]}s {Path(x[1]).name} {x[2]}s")

print()
print("SWEEP", "FAIL" if fails else "PASS", "-", len(fails), "failing checks")
