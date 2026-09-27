"""Report animation beat density per composition, read from the built timeline.

The metric that matters is the largest interval with nothing moving: how long the frame can sit
visually unchanged. scripts/beat_probe.mjs loads each mounted composition in headless Chromium and
returns its motion spans (what counts as motion, and why a `tl.to({}, {duration: N}, 0)` clock does
not, is in its header). Continuous motion covers its whole span, not just its start, so a graphic
with one long moving element does not read as dead. FAIL at a gap of 4.0 s or more, including
before the first span and after the last one up to the host window.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

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

comps = []
for f in sorted((ep / "compositions").glob("*.html")):
    if f.stem in hosts:
        comps.append(f.stem)
    else:
        print(f"[WARN] beat_density: compositions/{f.name} is not mounted in index.html, not checked")

probe = {}
if comps:
    # stderr passes through, so a crashed probe shows its Node trace to run_gates and e2e
    r = subprocess.run(["node", str(Path(__file__).with_name("beat_probe.mjs")), str(ep.resolve()),
                        *[f"{g}={hosts[g]}" for g in comps]], stdout=subprocess.PIPE, text=True, encoding="utf-8")
    lines = r.stdout.strip().splitlines()
    if r.returncode != 0 or not lines:
        sys.exit(f"[beat_density] FAIL: beat_probe.mjs exited {r.returncode}\n{r.stdout[-800:]}")
    probe = json.loads(lines[-1])  # earlier lines are render_busy's preflight print

rows, errors = [], []
for gid in comps:
    win, res = hosts[gid], probe[gid]
    if "error" in res:  # unmeasured is a FAIL at any window: as a gap-equals-window row a <4 s comp passed
        errors.append((gid, win, res["error"]))
        continue
    spans = sorted(res["spans"])
    if not spans:
        rows.append((gid, win, 0, win, "NO BEATS"))
        continue
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
for gid, win, err in errors:
    print(f"{gid:22} {win:6.1f}s {'-':>6} {'-':>10}  <-- ERROR {err}")
worst = [r for r in rows if r[3] >= 4.0]
print(f"\ncompositions with a >=4s motionless stretch: {len(worst)}/{len(comps)}")
if errors:
    print(f"compositions the probe could not measure (ERROR): {len(errors)}/{len(comps)}")
sys.exit(1 if worst or errors else 0)
