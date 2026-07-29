"""Emit the full clip-length ledger for an episode index.html.

Authoritative window list = every element on a picture track carrying
data-start + data-duration: <section> stills, <video> clips, and
sub-composition hosts. Audio elements live on their own tracks and are excluded.
"""
import re
import sys
from pathlib import Path

ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

rows = []
for m in re.finditer(r'<(section|video|img|div)\b([^>]*)>', h):
    tag, attrs = m.group(1), m.group(2)
    st = re.search(r'data-start="([\d.]+)"', attrs)
    du = re.search(r'data-duration="([\d.]+)"', attrs)
    tr = re.search(r'data-track-index="(\d+)"', attrs)
    if not (st and du and tr):
        continue
    at, dur = float(st.group(1)), float(du.group(1))
    cid = re.search(r'data-composition-id="([^"]+)"', attrs)
    if cid:
        kind, name = "graphic", cid.group(1)
    else:
        src = re.search(r'src="([^"]+)"', attrs)
        if src:
            name = Path(src.group(1)).name
        else:
            inner = h[m.end():m.end() + 900]
            s2 = re.search(r'src="([^"]+)"', inner)
            name = Path(s2.group(1)).name if s2 else "?"
        kind = "clip" if tag == "video" else "still"
    rows.append((at, dur, tr.group(1), kind, name))

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
spans = sorted((at, at + dur) for at, dur, *_ in rows)
cur, holes = 0.0, []
for a, b in spans:
    if a > cur + 0.05:
        holes.append((cur, a))
    cur = max(cur, b)
if cur < total - 0.05:
    holes.append((cur, total))
print(f"uncovered picture gaps: {len(holes)}")
for a, b in holes:
    print(f"  {ts(a)} -> {ts(b)}  ({b-a:.2f}s BLACK)")

print()
print("windows >= 15s:")
for at, dur, tr, kind, s in rows:
    if dur >= 15:
        print(f"  {ts(at)}  {dur:6.2f}s  {kind}  {s}")
