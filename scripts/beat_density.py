"""Report animation beat density per composition.

A "beat" is any GSAP call scheduled at an explicit timeline position. The
metric that matters is the largest interval between consecutive beats: that is
how long the frame can sit visually unchanged. Continuous tweens (a spine that
grows for 20s, a marker that crawls a map) are counted as covering their whole
span, not just their start, so a graphic with one long moving element does not
read as dead.
"""
import re
import sys
from pathlib import Path
from comp_consts import fold

ep = Path(sys.argv[1])
idx = (ep / "index.html").read_text(encoding="utf-8", errors="replace")
# Parse attributes per tag so attribute order doesn't matter.
hosts = {}
for m in re.finditer(r'<[^>]*\bdata-composition-id="([^"]+)"[^>]*>', idx):
    gid = m.group(1)
    dur = re.search(r'\bdata-duration="([\d.]+)"', m.group(0))
    if dur:
        hosts[gid] = float(dur.group(1))
    else:
        print(f"[WARN] beat_density: host '{gid}' has no numeric data-duration, not checked")

CALL = re.compile(r'tl\.(to|from|fromTo|set|add)\s*\(', re.S)

rows = []
for f in sorted((ep / "compositions").glob("*.html")):
    gid = f.stem
    if gid not in hosts:
        print(f"[WARN] beat_density: compositions/{f.name} is not mounted in index.html, not checked")
        continue
    src = fold(f.read_text(encoding="utf-8", errors="replace"))
    spans = []
    for m in CALL.finditer(src):
        # walk to the matching close paren, then read the trailing position arg
        depth, i = 0, m.end() - 1
        while i < len(src):
            if src[i] == "(":
                depth += 1
            elif src[i] == ")":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        body = src[m.end():i]
        tail = body.rsplit(",", 1)[-1].strip()
        pos = re.fullmatch(r'([\d.]+)', tail)
        if not pos:
            continue
        at = float(pos.group(1))
        # duration may be a numeric literal or a const defined in the comp (duration: HOST_WINDOW);
        # an unknown identifier is a hard error, never a silent 0 (alert-levels 17 Sep 26: 8/9 comps
        # read DEAD because every long tween used a variable).
        consts = {k: float(v) for k, v in re.findall(r'const\s+([A-Z_][A-Z0-9_]*)\s*=\s*([\d.]+)', src)}
        dur = []
        for tok in re.findall(r'duration:\s*([A-Za-z_][\w]*|[\d.]+)', body):
            if re.fullmatch(r'[\d.]+', tok): dur.append(float(tok))
            elif tok in consts: dur.append(consts[tok])
            else: sys.exit(f"[beat_density] FAIL {gid}: duration '{tok}' is not a literal or a numeric const in the comp")
        d = max(dur) if dur else 0.0
        # a repeating tween keeps moving for repeat+1 cycles (yoyo reverses but does not
        # change the total). Counting only the first cycle reported blinking markers and
        # pulsing dots as dead frames.
        rep = re.search(r'repeat:\s*(-?\d+)', body)
        if rep:
            n = int(rep.group(1))
            rd = re.search(r'repeatDelay:\s*([\d.]+)', body)
            cycle = d + (float(rd.group(1)) if rd else 0.0)
            d = hosts[gid] if n < 0 else d + n * cycle
        spans.append((at, at + d))

    win = hosts[gid]
    if not spans:
        rows.append((gid, win, 0, win, "NO BEATS"))
        continue
    spans.sort()
    cur, gap, when = 0.0, 0.0, 0.0
    for a, b in spans:
        if a - cur > gap:
            gap, when = a - cur, cur
        cur = max(cur, b)
    if win - cur > gap:
        gap, when = win - cur, cur
    rows.append((gid, win, len(spans), round(gap, 2), f"at {when:.1f}s"))

rows.sort(key=lambda r: -r[3])
print(f"{'composition':22} {'window':>7} {'beats':>6} {'max still':>10}  where")
for gid, win, n, gap, when in rows:
    flag = "  <-- DEAD" if gap >= 4.0 else ""
    print(f"{gid:22} {win:6.1f}s {n:6} {gap:9.2f}s  {when}{flag}")
worst = [r for r in rows if r[3] >= 4.0]
print(f"\ncompositions with a >=4s motionless stretch: {len(worst)}/{len(rows)}")
sys.exit(1 if worst else 0)
