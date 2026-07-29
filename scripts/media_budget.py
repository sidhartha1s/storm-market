"""Refuse to render when the media is too expensive to extract. HARD GATE.

Twelve ep3 v3 renders died at `video_extract` with `[FFmpeg] ffprobe deadline with
code 0`. Eleven of them were "fixed" by guessing and re-rendering. The defect was
visible in the asset table the whole time and nothing looked at it:

  - seven clips were 1920x1440 feeding a 1920x1080 composition, which CLAUDE.md
    already forbade ("cap every source asset at the composition's resolution before
    wiring it") with no gate to enforce it;
  - stock clips ran 4-6x longer than the window that used them (46.5s of 7.2 Mbps
    source for a window under 9s);
  - 240 MB of source had to be decoded to fill about 90s of screen time.

The probe that dies is not slow on its own — 3.18s serial, 8.18s at six-way
concurrency, against a deadline hardcoded at 120s in hyperframes 0.7.64. It dies
queued behind that decode.

So this checks the cost BEFORE a render, and `render_preflight.py` calls it, which
means the render script itself refuses to start. Every check below is a number that
could have been read at any point in the last twelve attempts.

Usage: python3 scripts/media_budget.py episodes/<slug>
Exit 0 = safe to render. Exit 1 = do not render, with the offending files named.
"""
import re
import subprocess
import sys
from pathlib import Path

ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

root = re.search(r'id="root"[^>]*data-width="(\d+)"[^>]*data-height="(\d+)"', h)
COMP_W, COMP_H = (int(root.group(1)), int(root.group(2))) if root else (1920, 1080)

# Measured on this box: 67 MB of trimmed source extracts inside the deadline; 240 MB
# did not. Half way between, rounded down, is the line we refuse to cross.
BUDGET_MB = 150
SLACK = 4.0          # a clip may exceed its longest window by this much and no more


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=width,height:format=duration",
                          "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout
    nums = [x for x in re.split(r'[,\n]', out) if x.strip()]
    if len(nums) < 3:
        return None
    return int(nums[0]), int(nums[1]), float(nums[2])


windows = {}
for m in re.finditer(r'<video\b([^>]*)>', h):
    src = re.search(r'src="([^"]+)"', m.group(1))
    dur = re.search(r'data-duration="([\d.]+)"', m.group(1))
    if src and dur:
        windows[src.group(1)] = max(windows.get(src.group(1), 0.0), float(dur.group(1)))

oversize, overlong, missing = [], [], []
total_mb = 0.0
for src, want in sorted(windows.items()):
    p = ep / src
    if not p.exists():
        missing.append(src)
        continue
    info = probe(p)
    if not info:
        missing.append(src)
        continue
    w, hgt, dur = info
    mb = p.stat().st_size / 1e6
    total_mb += mb
    if w > COMP_W or hgt > COMP_H:
        oversize.append((src, f"{w}x{hgt}", mb))
    if dur > want + SLACK:
        overlong.append((src, dur, want, mb))

fails = []
def installed_probe_deadline():
    """Read the ffprobe deadline out of the installed hyperframes bundle.

    It is a hardcoded literal with no env override, and it CHANGES between releases:
    0.7.64 allowed 120s, 0.7.81 allows 30s. Twelve renders died against that number
    while nobody could see it, so the gate prints it every run.
    """
    npx = Path.home() / "AppData" / "Local" / "npm-cache" / "_npx"
    best = None
    for cli in npx.glob("*/node_modules/hyperframes/dist/cli.js"):
        pkg = cli.parent.parent / "package.json"
        ver = re.search(r'"version":\s*"([\d.]+)"', pkg.read_text(encoding="utf-8", errors="replace"))
        hits = re.findall(r'deadlineAtMs:\s*Date\.now\(\)\s*\+\s*(\d+)e(\d+)',
                          cli.read_text(encoding="utf-8", errors="replace"))
        secs = {int(a) * 10 ** int(b) / 1000 for a, b in hits}
        if ver and secs:
            cand = (ver.group(1), min(secs))
            if best is None or cand[0] > best[0]:
                best = cand
    return best


print(f"composition {COMP_W}x{COMP_H} | {len(windows)} distinct clips | {total_mb:.0f} MB to decode")
dl = installed_probe_deadline()
if dl:
    print(f"installed hyperframes {dl[0]} allows {dl[1]:.0f}s per ffprobe "
          f"(0.7.64 allowed 120s — a newer pin can be STRICTER)")

if missing:
    fails.append(f"{len(missing)} clip(s) missing or unreadable")
    for s in missing:
        print(f"  MISSING  {s}")

if oversize:
    fails.append(f"{len(oversize)} clip(s) larger than the composition")
    print(f"\nover composition resolution ({COMP_W}x{COMP_H}):")
    for s, dim, mb in oversize:
        print(f"  {Path(s).name:44} {dim:>11} {mb:7.1f} MB")

if overlong:
    fails.append(f"{len(overlong)} clip(s) longer than the window that uses them")
    print(f"\nlonger than their window by more than {SLACK:.0f}s:")
    for s, dur, want, mb in overlong:
        print(f"  {Path(s).name:44} {dur:6.1f}s source for a {want:.1f}s window  {mb:7.1f} MB")

if total_mb > BUDGET_MB:
    fails.append(f"{total_mb:.0f} MB of source exceeds the {BUDGET_MB} MB decode budget")

if fails:
    print(f"\nMEDIA BUDGET FAIL — do not render:")
    for f in fails:
        print(f"  - {f}")
    print("\nFix: python3 scripts/optimize_clips.py <episode> --apply, then rebuild index.html.")
    print("A render started here dies at video_extract with 'ffprobe deadline with code 0',")
    print("which reads like a corrupt asset and is not one.")
    sys.exit(1)

print(f"MEDIA BUDGET PASS — every clip within {COMP_W}x{COMP_H}, "
      f"within {SLACK:.0f}s of its window, {total_mb:.0f}/{BUDGET_MB} MB budget")
