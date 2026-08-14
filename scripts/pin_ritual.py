#!/usr/bin/env python3
"""The hyperframes pin upgrade ritual, as code (owner order 2026-08-14).

The pin policy is deliberate: renders must run the version that was reviewed, and
upstream ships ~1.6 releases/day with behavior changes in minor bumps (0.7.81 cut
the ffprobe deadline 4x; 0.7.107 changed the hidden-audio mix). The WEAK part was
the refresh: bumps happened manually and the pin sat 2 weeks / 26 versions stale
while a non-blocking warning fired unheard. This script is the ritual made
mechanical, so the pin never rots more than one production run:

  1. `npm view hyperframes version` — pin current? done.
  2. Newer upstream: render the demo episode at the CANDIDATE version and diff it
     against the recorded BASELINE (committed metrics in scripts/pin_baseline.json,
     plus the cached baseline mp4 on disk for SSIM when present; if the record is
     missing or belongs to an older pin, the baseline render runs too).
  3. Metrics identical (duration, blackdetect map, RMS, SSIM) -> bump the pin in
     config.yaml + every live scripts/*.cmd, refresh the baseline record, exit 0.
     The caller (a session, in a worktree) commits and PRs the bump.
  4. Any metric drifts -> NO bump, print the drift table, exit 3. A human decides.

render_preflight.py enforces the other half: a FULL render refuses to start while
upstream is newer than the pin, and the fix it names is running this script.

Runtime: one 90s demo render ~10-13 min on this box; two when the baseline record
is stale. Launch detached (schtasks one-shot / Start-Process) when driving it from
a harness that reaps foreground calls — same rule as render.cmd.

Usage: python3 scripts/pin_ritual.py [--check-only]
Exit codes: 0 pin current or bumped clean; 2 setup error; 3 metric drift (no bump);
            4 npm unreachable (currency unknowable — this tool exists to answer it).
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from render_preflight import npm_latest, parse_pin, semver

REPO = Path(__file__).resolve().parent.parent
DEMO = REPO / "episodes" / "demo-joplin-90"
BASELINE_JSON = Path(__file__).resolve().parent / "pin_baseline.json"
RENDER_CMD = Path(__file__).resolve().parent / "render.cmd"

# Mirrors render.cmd full-quality flags — the ritual must exercise the production
# recipe, not a lighter one. Bump both together.
RENDER_FLAGS = ["--gpu", "--browser-gpu", "--experimental-fast-capture=true",
                "--quality", "standard", "--crf", "16", "--fps", "30", "--workers", "3"]


def ff_paths():
    """ffmpeg/ffprobe from render.cmd's `set HYPERFRAMES_FF*_PATH=` lines — the render
    recipe is the single source of truth for which build measures (a wrong/stale build
    silently disagrees on blackdetect/astats, see LEARNINGS on the shared-build spawn cost)."""
    txt = RENDER_CMD.read_text(encoding="utf-8", errors="replace")
    paths = dict(re.findall(r"^set (HYPERFRAMES_FF(?:MPEG|PROBE)_PATH)=(.+)$", txt,
                            re.MULTILINE))
    probe, mpeg = paths.get("HYPERFRAMES_FFPROBE_PATH"), paths.get("HYPERFRAMES_FFMPEG_PATH")
    if not (probe and mpeg and Path(probe.strip()).exists() and Path(mpeg.strip()).exists()):
        sys.exit("[ritual] could not resolve ffprobe/ffmpeg from render.cmd's set lines")
    return Path(probe.strip()), Path(mpeg.strip())


FFPROBE, FFMPEG = ff_paths()

# Identity thresholds: the demo comp is deterministic, so a version that changes
# nothing lands well inside these (measured 0.7.81 vs 0.7.107: duration exact,
# blackdetect exact, RMS delta 0.006 dB, SSIM 0.997).
DUR_TOL = 0.05          # seconds
BLACK_TOL = 0.10        # seconds, per boundary
RMS_TOL = 0.20          # dB
SSIM_MIN = 0.99


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def render(version, out_mp4):
    """Render the demo comp at a specific hyperframes version, synchronously."""
    npx = shutil.which("npx")
    if not npx:
        sys.exit("[ritual] npx not on PATH")
    log = DEMO / f"pin-ritual-{version}.log"
    print(f"[ritual] rendering demo at {version} -> {out_mp4.name} (log {log.name})")
    env = dict(**os.environ,
               HYPERFRAMES_FFPROBE_PATH=str(FFPROBE),
               HYPERFRAMES_FFMPEG_PATH=str(FFMPEG),
               PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS="120000",
               PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS="900000")
    with open(log, "w", encoding="utf-8") as lf:
        # -y: an uncached version makes npx prompt "Ok to proceed?" and a detached run
        # hangs on it until the timeout (measured: 40 min lost on 0.7.109's first run).
        r = subprocess.run([npx, "-y", f"hyperframes@{version}", "render", str(DEMO),
                            *RENDER_FLAGS, "-o", str(out_mp4)],
                           stdout=lf, stderr=subprocess.STDOUT, env=env,
                           stdin=subprocess.DEVNULL, timeout=2400, cwd=DEMO)
    if r.returncode != 0 or not out_mp4.exists():
        sys.exit(f"[ritual] render at {version} FAILED (exit {r.returncode}) — see {log}")


def measure(mp4):
    dur = float(run([str(FFPROBE), "-v", "error", "-show_entries",
                     "format=duration", "-of", "csv=p=0", str(mp4)]).stdout.strip())
    r = run([str(FFMPEG), "-hide_banner", "-i", str(mp4),
             "-vf", "blackdetect=d=0.5", "-af", "astats=metadata=1",
             "-f", "null", "-"], timeout=600)
    txt = r.stdout + r.stderr
    black = [(float(a), float(b)) for a, b in
             re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", txt)]
    # last Peak/RMS pair in astats output is the Overall section
    peaks = re.findall(r"Peak level dB: (-?[\d.]+)", txt)
    rmss = re.findall(r"RMS level dB: (-?[\d.]+)", txt)
    if not peaks or not rmss:
        sys.exit(f"[ritual] astats gave no levels for {mp4.name}")
    return {"duration": dur, "blackdetect": black,
            "rms_db": float(rmss[-1]), "peak_db": float(peaks[-1])}


def ssim(a, b):
    r = run([str(FFMPEG), "-hide_banner", "-i", str(a), "-i", str(b),
             "-lavfi", "ssim", "-f", "null", "-"], timeout=600)
    m = re.search(r"All:([\d.]+)", r.stdout + r.stderr)
    return float(m.group(1)) if m else None


def compare(base, cand, ssim_all):
    drifts = []
    if abs(base["duration"] - cand["duration"]) > DUR_TOL:
        drifts.append(f"duration {base['duration']:.3f}s -> {cand['duration']:.3f}s")
    if len(base["blackdetect"]) != len(cand["blackdetect"]):
        drifts.append(f"blackdetect segments {len(base['blackdetect'])} -> "
                      f"{len(cand['blackdetect'])}")
    else:
        for (bs, be), (cs, ce) in zip(base["blackdetect"], cand["blackdetect"]):
            if abs(bs - cs) > BLACK_TOL or abs(be - ce) > BLACK_TOL:
                drifts.append(f"black segment moved ({bs:.2f}-{be:.2f}) -> "
                              f"({cs:.2f}-{ce:.2f})")
    if abs(base["rms_db"] - cand["rms_db"]) > RMS_TOL:
        drifts.append(f"RMS {base['rms_db']:.3f} -> {cand['rms_db']:.3f} dB")
    if ssim_all is not None and ssim_all < SSIM_MIN:
        drifts.append(f"SSIM {ssim_all:.4f} < {SSIM_MIN}")
    return drifts


def bump_pins(new):
    cfg = REPO / "config.yaml"
    cfg.write_text(re.sub(r'(hyperframes_version:\s*")[\d.]+(")',
                          rf"\g<1>{new}\g<2>", cfg.read_text(encoding="utf-8")),
                   encoding="utf-8")
    for script in sorted((REPO / "scripts").glob("*.cmd")):
        txt = script.read_text(encoding="utf-8")
        if "npx hyperframes@" in txt:
            script.write_text(re.sub(r"(hyperframes@)[\d.]+", rf"\g<1>{new}", txt),
                              encoding="utf-8")
            print(f"[ritual] pinned {script.name} -> {new}")
    print(f"[ritual] pinned config.yaml -> {new}")


def main():
    check_only = "--check-only" in sys.argv
    pin = parse_pin(REPO)
    if pin is None:
        sys.exit("[ritual] no hyperframes_version in config.yaml")
    latest = npm_latest(timeout=60)
    if latest is None:
        # preflight tolerates an unreachable npm; this tool's entire job is the answer
        print("[ritual] npm unreachable — currency unknowable", file=sys.stderr)
        return 4
    if semver(latest) <= semver(pin):
        print(f"[ritual] pin {pin} is current (npm latest {latest})")
        return 0
    print(f"[ritual] pin {pin} is STALE — npm latest is {latest}")
    if check_only:
        return 3

    if not (DEMO / "index.html").exists():
        sys.exit(f"[ritual] demo episode missing: {DEMO}")
    html = (DEMO / "index.html").read_text(encoding="utf-8", errors="replace")
    missing = [s for s in re.findall(r'src="(media/[^"]+)"', html)
               if not (DEMO / s).exists()]
    if missing:
        sys.exit(f"[ritual] demo media incomplete ({len(missing)} missing, e.g. "
                 f"{missing[0]}) — copy media/ from the main checkout first")

    renders = DEMO / "renders"
    renders.mkdir(exist_ok=True)

    # Baseline: reuse the committed record when it belongs to the current pin.
    base_mp4 = renders / f"pin-baseline-{pin}.mp4"
    record = None
    if BASELINE_JSON.exists():
        record = json.loads(BASELINE_JSON.read_text(encoding="utf-8"))
        if record.get("version") != pin:
            record = None
    if record is None:
        render(pin, base_mp4)
        record = {"version": pin, **measure(base_mp4)}
    base_has_mp4 = base_mp4.exists()

    cand_mp4 = renders / f"pin-baseline-{latest}.mp4"
    render(latest, cand_mp4)
    cand = measure(cand_mp4)
    ssim_all = ssim(base_mp4, cand_mp4) if base_has_mp4 else None
    if not base_has_mp4:
        print("[ritual] no baseline mp4 on disk — SSIM skipped (metrics-only compare)")

    drifts = compare(record, cand, ssim_all)
    print(f"[ritual] {pin} vs {latest}: duration {record['duration']:.3f}/"
          f"{cand['duration']:.3f}s, black {len(record['blackdetect'])}/"
          f"{len(cand['blackdetect'])} segs, RMS {record['rms_db']:.3f}/"
          f"{cand['rms_db']:.3f} dB, SSIM "
          f"{'n/a' if ssim_all is None else f'{ssim_all:.4f}'}")
    if drifts:
        print(f"[ritual] METRIC DRIFT — NOT bumping {pin} -> {latest}:", file=sys.stderr)
        for d in drifts:
            print(f"    {d}", file=sys.stderr)
        print("[ritual] read the changelog, eyeball both renders, decide by hand.",
              file=sys.stderr)
        return 3

    bump_pins(latest)
    BASELINE_JSON.write_text(json.dumps({"version": latest, **cand}, indent=2),
                             encoding="utf-8")
    if base_has_mp4:
        base_mp4.unlink()
    print(f"[ritual] PASS — pin bumped {pin} -> {latest}; baseline refreshed. "
          f"Commit + PR the bump (config.yaml, scripts/*.cmd, pin_baseline.json).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
