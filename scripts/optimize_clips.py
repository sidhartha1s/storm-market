"""Trim and cap every mounted clip to what the timeline actually uses.

Why this exists: ep3 v3 failed eleven renders at `video_extract` with
`[FFmpeg] ffprobe deadline with code 0`. The probe itself is not slow — measured with
hyperframes' own arguments, the worst clip is 3.18s serial and 8.18s at six-way
concurrency, against a 120s deadline. What blows the deadline is the extract stage
running underneath it: 549 MB of 1080p24-30 source is decoded to frames by three
workers while a probe waits behind that I/O, and the stage had already run 204s when
it died.

The clips are far larger than the cut needs. `stock-cloudsomen-01.mp4` is 46.5s at
7.2 Mbps feeding a window under 9s; `mvtn-centerpiece-aerial-30s.mp4` is 1920x1440,
which the repo's own rule already forbids ("cap every source asset at the
composition's resolution before wiring it").

So: trim each clip to its longest window plus a safety margin, cap height at 1080,
and re-encode with a short GOP so seeking is cheap. Originals are moved to
media/_orig/ — nothing is destroyed.

Usage: python3 scripts/optimize_clips.py episodes/<slug> [--apply]
Without --apply it prints the plan and changes nothing.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ep = Path(sys.argv[1])
apply = "--apply" in sys.argv
if apply and subprocess.run([sys.executable, str(Path(__file__).with_name('render_busy.py'))]).returncode:
    sys.exit(3)      # one heavy job at a time: no ffmpeg batch under a live render (owner 2026-09-11)
MARGIN = 1.5          # headroom over the longest window, so vdur() never clips a window
GOP = 15              # draft renders at 15fps; a keyframe per second keeps seeks cheap
BUDGET_MB = 150       # must match media_budget.py; crf escalates until under this
CRF_LADDER = [23, 27, 31]  # ep6 measured: 51 clips at crf23 = 194 MB, crf27 = 143 MB

h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

root = re.search(r'id="root"[^>]*data-width="(\d+)"[^>]*data-height="(\d+)"', h)
COMP_W, COMP_H = (int(root.group(1)), int(root.group(2))) if root else (1920, 1080)

used = {}
for m in re.finditer(r'<video\b([^>]*)>', h):
    attrs = m.group(1)
    src = re.search(r'src="([^"]+)"', attrs)
    dur = re.search(r'data-duration="([\d.]+)"', attrs)
    if not (src and dur):
        continue
    # data-media-start is the clip's in-point: the source must supply media_start + duration
    # seconds, or the trim below cuts off before the in-point plays (render-05: ep1/ep6
    # vx-warmend needs 8s + 13.1s = 21.1s, not 13.1s — --apply then wrote a 14.6s file).
    start = re.search(r'data-media-start="([\d.]+)"', attrs)
    need = (float(start.group(1)) if start else 0.0) + float(dur.group(1))
    used[src.group(1)] = max(used.get(src.group(1), 0.0), need)

# The CTA insert is a provenance contract (config.yaml channel.cta, md5-checked by sweep_episode):
# re-encoding it broke the md5 silently (jma-vs-nhc, 17 Sep 26). Never touch it.
import yaml
_cta = ((yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text(encoding="utf-8"))
         .get("channel") or {}).get("cta") or {}).get("file", "")
for _k in [k for k in used if _cta and Path(k).name == Path(_cta).name]:
    print(f"skip {_k}: CTA insert, md5 contract (config channel.cta.file)")
    del used[_k]

orig_dir = ep / "media" / "_orig"
plan, total_before = [], 0
for src, want in sorted(used.items()):
    p = ep / src
    if not p.exists():
        print(f"MISSING {src}")
        continue
    info = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                           "-show_entries", "stream=width,height:format=duration",
                           "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
    nums = [x for x in re.split(r'[,\n]', info) if x.strip()]
    w, hgt, dur = int(nums[0]), int(nums[1]), float(nums[2])
    mb = p.stat().st_size / 1e6
    total_before += mb
    keep = min(dur, want + MARGIN)
    plan.append((src, mb, w, hgt, dur, keep))

print(f"composition {COMP_W}x{COMP_H}")
print(f"{'clip':44} {'MB':>7} {'source':>12} {'len':>7} {'keep':>7}")
for src, mb, w, hgt, dur, keep in plan:
    flag = "  <- over comp" if (w > COMP_W or hgt > COMP_H) else ""
    print(f"{Path(src).name:44} {mb:7.1f} {w:5}x{hgt:<6} {dur:6.1f}s {keep:6.1f}s{flag}")
print(f"\n{len(plan)} clips, {total_before:.0f} MB before")
if not apply:
    print("dry run — pass --apply to rewrite (originals move to media/_orig/)")
    raise SystemExit(0)

orig_dir.mkdir(parents=True, exist_ok=True)

def has_audio(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a",
                          "-show_entries", "stream=codec_type", "-of", "csv=p=0",
                          str(p)], capture_output=True, text=True).stdout
    return bool(out.strip())

def encode(src_file, out_file, keep, crf, audio):
    # Audio is PRESERVED (ep6 lesson: -an forced a re-mux ritual on every audible
    # clip and a silent-track patch on every muted one — hyperframes >=0.7.109
    # requires an audio stream on every mounted video). Clips with no audio get
    # a silent track muxed in the same pass.
    base = ["ffmpeg", "-y", "-v", "error", "-i", str(src_file)]
    if audio:
        maps = ["-map", "0:v", "-map", "0:a:0", "-c:a", "aac", "-b:a", "96k"]
    else:
        base += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        maps = ["-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "32k", "-shortest"]
    # Fit inside the REAL composition box, not a hardcoded 1080-tall cap (render-06: that cap
    # halved every clip in a 1080x1920 short — media_budget.py already reads data-width/height
    # off the root and passed those same clips at full resolution). min(iw,W)/min(ih,H) never
    # upscales a source smaller than the box; force_original_aspect_ratio=decrease then picks
    # whichever axis is tighter so the aspect ratio holds; force_divisible_by=2 keeps yuv420p happy.
    scale = (f"scale=w='min(iw,{COMP_W})':h='min(ih,{COMP_H})':"
             "force_original_aspect_ratio=decrease:force_divisible_by=2")
    cmd = base + ["-t", f"{keep:.2f}", *maps,
                  "-vf", scale, "-c:v", "libx264",
                  "-preset", "veryfast", "-crf", str(crf), "-g", str(GOP),
                  "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out_file)]
    return subprocess.run(cmd, capture_output=True, text=True)

for crf in CRF_LADDER:
    total_after = 0
    for src, mb, w, hgt, dur, keep in plan:
        p = ep / src
        backup = orig_dir / Path(src).name
        if not backup.exists():
            shutil.copy2(p, backup)
        tmp = p.with_suffix(".opt.mp4")
        r = encode(backup, tmp, keep, crf, has_audio(backup))
        if r.returncode != 0 or not tmp.exists():
            print(f"FAILED {Path(src).name}: {r.stderr.strip()[:120]}")
            tmp.unlink(missing_ok=True)
            total_after += p.stat().st_size / 1e6
            continue
        tmp.replace(p)
        after = p.stat().st_size / 1e6
        total_after += after
        print(f"crf{crf} {Path(src).name:42} {mb:7.1f} -> {after:6.1f} MB")
    print(f"\ncrf {crf}: {total_before:.0f} MB -> {total_after:.0f} MB "
          f"({100 * (1 - total_after / total_before):.0f}% less to decode)")
    if total_after <= BUDGET_MB:
        break
    if crf != CRF_LADDER[-1]:
        print(f"still over the {BUDGET_MB} MB budget — escalating crf")
print("originals in media/_orig/ — rebuild index.html, the window caps come from vdur()")
if total_after > BUDGET_MB:
    print(f"FAIL: {total_after:.0f} MB still over {BUDGET_MB} MB at crf "
          f"{CRF_LADDER[-1]} — reduce clip count/length, don't render")
    raise SystemExit(1)
