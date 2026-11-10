"""Emit the full clip-length ledger for an episode index.html.

Authoritative window list = every element on a picture track carrying
data-start + data-duration: <section> stills, <video> clips, and
sub-composition hosts. Audio elements live on their own tracks and are excluded.

Coverage is computed over timeline.PICTURE_TRACKS only (timeline.picture_holes). Tracks above those carry
overlays (date cards, source chips, quote cards, lower-thirds) that sit ON TOP
of picture; counting them as coverage hides real black gaps underneath.
"""
import re
import sys
from pathlib import Path

import timeline


ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

wins = timeline.windows(h)   # the one window reader: a src-less element names the file in its own body, never the next one
rows = []
for w in wins:
    cid = w["attrs"].get("data-composition-id")
    if cid:
        kind, name = "graphic", cid
    else:
        name = Path(w["src"]).name if w["src"] else "?"
        kind = "clip" if w["kind"] == "video" else "still"
    rows.append((w["at"], w["dur"], w["tr"], kind, name))

rows.sort()


def ts(s):
    return f"{int(s)//60}:{s%60:05.2f}"


print("| # | start | len | track | kind | source |")
print("|---|-------|-----|-------|------|--------|")
for n, (at, dur, tr, kind, s) in enumerate(rows, 1):
    print(f"| {n} | {ts(at)} | {dur:.2f}s | {tr} | {kind} | {s} |")

lens = sorted(r[1] for r in rows)
print()
print(f"windows: {len(rows)}  median: {lens[len(lens)//2]:.2f}s  "
      f"mean: {sum(lens)/len(lens):.2f}s  min: {lens[0]:.2f}s  max: {lens[-1]:.2f}s")

# coverage: any moment with no picture-track window is black
total = float(re.search(r'data-duration="([\d.]+)"', h).group(1))
holes = timeline.picture_holes(wins, total)
print(f"uncovered picture gaps (tracks {list(timeline.PICTURE_TRACKS)}): {len(holes)}")
for a, b in holes:
    print(f"  {ts(a)} -> {ts(b)}  ({b-a:.2f}s BLACK)")

print()
print("windows >= 15s:")
for at, dur, tr, kind, s in rows:
    if dur >= 15:
        print(f"  {ts(at)}  {dur:6.2f}s  {kind}  {s}")
