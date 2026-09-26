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
  3. Metrics identical (duration, blackdetect map, RMS, video-region luma, workers, SSIM
     full-frame and video-region) -> bump the pin in
     config.yaml + every live scripts/*.cmd, refresh the baseline record, exit 0.
     The caller (a session, in a worktree) commits and PRs the bump.
  4. Any metric drifts -> NO bump, print the drift table, exit 3. A human decides.

When it runs (owner 26 Sep 26): at episode kickoff, before the episode's first render
(`--check-only`, then the full ritual if stale), so an episode never switches version
mid-way. render_preflight.py only checks pin drift, never currency.

The demo is episodes/demo-pin: 24 s, fully committed (MG showcase + WebGL probe + an
ffmpeg-made video and tone), no gitignored media, so it runs from any fresh worktree.
  - Mixer: sfx/tone.ogg (440 Hz) at 3-7 s, gain 0.5. Both renders must carry audio and
    their overall RMS must agree within RMS_TOL; a silent render is drift, never a pass.
  - Video capture: clips/probe.webm mounted at 16 s with data-media-start 1, so capture
    must seek into it (0.8.72/0.8.77/0.8.78 changed "capture waits for seeking video").
    The clip burns its own timecode; measure() records the per-frame luma of VIDEO_BOX over
    VIDEO_WIN and compare() diffs it, and SSIM is also taken on that region alone.
  - The WebGL probe's frame barcode is checked by the full-frame SSIM.

Workers: RENDER_FLAGS use --workers 2, the production full-render path, which routes
capture through the parallel-stream router (HF_CAPTURE_PARALLEL_STREAM). RENDER_WORKERS
(the render.cmd knob) still overrides it on a RAM-tight box, but below 2 the ritual takes
the single-worker capture path and prints `[FALLBACK] single-worker capture path,
parallel-stream router unverified` on every render. The worker count is stored in
pin_baseline.json and a baseline/candidate mismatch is drift.

Runtime: one 24 s demo render ~2-4 min on this box; two when the baseline record
is stale. Launch detached (schtasks one-shot via run_hidden.vbs) when driving it from
a harness that reaps foreground calls — same rule as render.cmd.

--baseline re-records the baseline at the CURRENT pin (render, measure, write
pin_baseline.json + the BASELINE_DIR mp4) without consulting npm. Run it whenever
demo-pin changes: the old record measures a different comp.

Usage: python3 scripts/pin_ritual.py [--check-only | --baseline]
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

from render_preflight import parse_pin

REPO = Path(__file__).resolve().parent.parent
DEMO = REPO / "episodes" / "demo-pin"
BASELINE_JSON = Path(__file__).resolve().parent / "pin_baseline.json"
RENDER_CMD = Path(__file__).resolve().parent / "render.cmd"
# The baseline mp4 lives OUTSIDE any worktree (assets-comps-02): episodes/*/renders/ is
# gitignored and every ritual run happens in a fresh worktree per CLAUDE.md worktree
# isolation, so a path under DEMO never survives to the next run and SSIM silently never ran.
BASELINE_DIR = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData" / "Local"))) / "storm-market" / "pin-baseline"

# Mirrors render.cmd full-quality flags — the ritual must exercise the production
# recipe, not a lighter one. Bump both together. --workers 2 matches every production
# full-render wrapper (scripts/*_full_task.cmd all set RENDER_WORKERS=2); render.cmd's own
# bare default of 3 is the draft-tuned value, not what full renders actually use.
WORKERS = int(os.environ.get("RENDER_WORKERS", "2"))
RENDER_FLAGS = ["--gpu", "--browser-gpu", "--experimental-fast-capture=true",
                "--quality", "standard", "--crf", "16", "--fps", "30",
                "--workers", str(WORKERS)]
FALLBACK_1W = "[FALLBACK] single-worker capture path, parallel-stream router unverified"

# The demo's video probe (episodes/demo-pin/index.html #probe-video): box x, y, w, h and
# the window measured inside its 16-18 s mount, 0.1 s clear of each edge.
VIDEO_BOX = (96, 300, 854, 480)
VIDEO_WIN = (16.1, 17.9)


def npm_latest(timeout=30):
    """Latest hyperframes on npm, or None (npm missing/unreachable/garbage output)."""
    npm = shutil.which("npm")
    if not npm:
        return None
    try:
        out = subprocess.run([npm, "view", "hyperframes", "version"],
                             capture_output=True, text=True, timeout=timeout).stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return None
    return out if re.fullmatch(r"[\d.]+", out) else None


def semver(v):
    return tuple(int(x) for x in v.split("."))


def render_cmd_env():
    """The extra env vars render.cmd sets that gate the production capture path.

    With --workers > 1, streaming capture also needs HF_CAPTURE_PARALLEL_STREAM (render.cmd's
    own comment: without it 'the gate logs enabled:false and the render dies at Disk capture
    may need ~131 GB'). Pulled from render.cmd's `set` lines, not hand-copied, so a future edit
    to render.cmd can't silently re-diverge the ritual from the recipe it is meant to verify.
    Only these two names are pulled — render.cmd's batch-local vars (SLUG, EP, QUAL, _CRF...)
    are not real env vars and would corrupt the child env if copied blindly."""
    txt = RENDER_CMD.read_text(encoding="utf-8", errors="replace")
    names = ("PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS", "HF_CAPTURE_PARALLEL_STREAM")
    found = dict(re.findall(r"^set (" + "|".join(names) + r")=(.+)$", txt, re.MULTILINE))
    missing = [n for n in names if n not in found]
    if missing:
        sys.exit(f"[ritual] render.cmd no longer sets {missing} — update render_cmd_env(), "
                  "the ritual's production-recipe env is now stale")
    return found


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


# resolved in main() AFTER the check-only/currency early exits — a box without the
# render toolchain can still answer "is the pin current"
FFPROBE = FFMPEG = None

# Identity thresholds: the demo comp is deterministic, so a version that changes
# nothing lands well inside these (measured 0.7.81 vs 0.7.107: duration exact,
# blackdetect exact, RMS delta 0.006 dB, SSIM 0.997).
DUR_TOL = 0.05          # seconds
BLACK_TOL = 0.10        # seconds, per boundary
RMS_TOL = 0.20          # dB
SSIM_MIN = 0.99
# per-frame mean luma (0-255) of the video box; an unseeked, stale or missing frame moves it
# by tens (burned timecode + sliding white box on testsrc2). Not yet measured across versions:
# the first re-baseline pair sets the evidence for this number.
VIDEO_LUMA_TOL = 2.0


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def render(version, out_mp4):
    """Render the demo comp at a specific hyperframes version, synchronously."""
    npx = shutil.which("npx")
    if not npx:
        sys.exit("[ritual] npx not on PATH")
    log = DEMO / f"pin-ritual-{version}.log"
    if WORKERS < 2:
        print(FALLBACK_1W)
    print(f"[ritual] rendering demo at {version} -> {out_mp4.name} (log {log.name}, "
          f"{WORKERS} workers)")
    # hyperframes >=0.8 flushes PostHog telemetry via a DETACHED `node -e fetch(...)` child
    # without windowsHide -> one visible console window per flush on Windows (owner saw
    # "lots of CMDs, 4 at a time", 2026-08-23). Opt out; never a visible window.
    env = dict(**os.environ,
               HYPERFRAMES_NO_TELEMETRY="1", DO_NOT_TRACK="1",
               HYPERFRAMES_FFPROBE_PATH=str(FFPROBE),
               HYPERFRAMES_FFMPEG_PATH=str(FFMPEG),
               PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS="120000",
               PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS="900000",
               **render_cmd_env())
    with open(log, "w", encoding="utf-8") as lf:
        # -y: an uncached version makes npx prompt "Ok to proceed?" and a detached run
        # hangs on it until the timeout (measured: 40 min lost on 0.7.109's first run).
        r = subprocess.run([npx, "-y", f"hyperframes@{version}", "render", str(DEMO),
                            *RENDER_FLAGS, "-o", str(out_mp4)],
                           stdout=lf, stderr=subprocess.STDOUT, env=env,
                           stdin=subprocess.DEVNULL, timeout=2400, cwd=DEMO)
    if r.returncode != 0 or not out_mp4.exists():
        sys.exit(f"[ritual] render at {version} FAILED (exit {r.returncode}) — see {log}")
    # --workers 2 (>1) only streams if the parallel-capture router picked it up (render.cmd's
    # own comment: otherwise "the gate logs enabled:false"). A silent fallback to disk capture
    # here means the ritual verified the WRONG capture path (assets-comps-03) — never a pass.
    # HyperFrames writes this as a JSON blob, e.g. `streaming-encode gate
    # {"renderJobId":"...","enabled":true,...}` — no literal "enabled:true" substring.
    # Match the JSON form ("enabled":true) and tolerate an unquoted enabled:true too.
    log_txt = log.read_text(encoding="utf-8", errors="replace")
    if not re.search(r'streaming-encode gate.*\benabled"?\s*:\s*true', log_txt):
        sys.exit(f"[ritual] {version}: no 'streaming-encode gate ... enabled:true' in {log.name} "
                  "— this render did not exercise the production streaming-capture path")


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
    has_audio = bool(run([str(FFPROBE), "-v", "error", "-select_streams", "a",
                          "-show_entries", "stream=index", "-of", "csv=p=0",
                          str(mp4)]).stdout.strip())
    if has_audio and (not peaks or not rmss):
        sys.exit(f"[ritual] astats gave no levels for {mp4.name}")
    # a render with no audio stream measures None; compare() fails it (demo-pin has a tone)
    return {"workers": WORKERS, "duration": dur, "blackdetect": black,
            "rms_db": float(rmss[-1]) if has_audio else None,
            "peak_db": float(peaks[-1]) if has_audio else None,
            "video_luma": video_luma(mp4)}


def _region(label):
    """Filter chain cutting VIDEO_WIN x VIDEO_BOX out of input `label`."""
    x, y, w, h = VIDEO_BOX
    s, e = VIDEO_WIN
    return f"[{label}:v]trim=start={s}:end={e},setpts=PTS-STARTPTS,crop={w}:{h}:{x}:{y}"


def video_luma(mp4):
    """Per-frame mean luma of the video probe's box over VIDEO_WIN, 2 dp."""
    r = run([str(FFMPEG), "-hide_banner", "-i", str(mp4), "-filter_complex",
             _region(0) + ",signalstats,metadata=print:key=lavfi.signalstats.YAVG",
             "-an", "-f", "null", "-"], timeout=600)
    return [round(float(v), 2) for v in
            re.findall(r"lavfi\.signalstats\.YAVG=([\d.]+)", r.stdout + r.stderr)]


def ssim(a, b, region=False):
    """SSIM All of a vs b: full frame, or the video probe's box/window when region=True."""
    lavfi = (f"{_region(0)}[a];{_region(1)}[b];[a][b]ssim" if region else "ssim")
    r = run([str(FFMPEG), "-hide_banner", "-i", str(a), "-i", str(b),
             "-lavfi", lavfi, "-f", "null", "-"], timeout=600)
    m = re.search(r"All:([\d.]+)", r.stdout + r.stderr)
    return float(m.group(1)) if m else None


def compare(base, cand, ssim_all, ssim_video=None):
    drifts = []
    if base.get("workers") != cand.get("workers"):
        drifts.append(f"workers {base.get('workers')} -> {cand.get('workers')} "
                      "(different capture path; re-run both at the same count)")
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
    # demo-pin mounts a tone, so both sides must carry audio: silent == mixer unverified
    if base["rms_db"] is None or cand["rms_db"] is None:
        drifts.append(f"audio RMS {base['rms_db']} -> {cand['rms_db']} dB "
                      "(a silent render: the mixer probe was not measured)")
    elif abs(base["rms_db"] - cand["rms_db"]) > RMS_TOL:
        drifts.append(f"RMS {base['rms_db']:.3f} -> {cand['rms_db']:.3f} dB")
    bl, cl = base.get("video_luma") or [], cand.get("video_luma") or []
    if not bl or len(bl) != len(cl):
        drifts.append(f"video-probe frames {len(bl)} -> {len(cl)} (region unmeasured or "
                      "frame count moved)")
    else:
        worst = max(abs(b - c) for b, c in zip(bl, cl))
        if worst > VIDEO_LUMA_TOL:
            drifts.append(f"video-probe luma moved {worst:.2f} > {VIDEO_LUMA_TOL} "
                          "(seek/capture of the <video> changed)")
    if ssim_all is not None and ssim_all < SSIM_MIN:
        drifts.append(f"SSIM {ssim_all:.4f} < {SSIM_MIN}")
    if ssim_video is not None and ssim_video < SSIM_MIN:
        drifts.append(f"video-region SSIM {ssim_video:.4f} < {SSIM_MIN}")
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


def record_baseline(pin, base_mp4):
    """Render the demo at `pin` into base_mp4, measure it, persist pin_baseline.json."""
    render(pin, base_mp4)
    record = {"version": pin, "demo": DEMO.name, **measure(base_mp4)}
    BASELINE_JSON.write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


def setup():
    global FFPROBE, FFMPEG
    FFPROBE, FFMPEG = ff_paths()
    if not (DEMO / "index.html").exists():
        sys.exit(f"[ritual] demo episode missing: {DEMO}")
    (DEMO / "renders").mkdir(exist_ok=True)
    BASELINE_DIR.mkdir(parents=True, exist_ok=True)


def main():
    check_only = "--check-only" in sys.argv
    pin = parse_pin(REPO)
    if pin is None:
        sys.exit("[ritual] no hyperframes_version in config.yaml")
    if "--baseline" in sys.argv:
        setup()
        base_mp4 = BASELINE_DIR / f"pin-baseline-{pin}.mp4"
        rec = record_baseline(pin, base_mp4)
        print(f"[ritual] baseline re-recorded at {pin} ({rec['workers']} workers): RMS "
              f"{rec['rms_db']} dB, {len(rec['video_luma'])} video-probe frames, "
              f"mp4 {base_mp4}. Commit scripts/pin_baseline.json.")
        # a baseline that could never pass compare() is a setup error, not a record
        bad = compare(rec, dict(rec), None)
        if bad:
            print("[ritual] baseline is unusable: " + "; ".join(bad), file=sys.stderr)
            return 2
        return 0
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

    global FFPROBE, FFMPEG
    FFPROBE, FFMPEG = ff_paths()

    if not (DEMO / "index.html").exists():
        sys.exit(f"[ritual] demo episode missing: {DEMO}")

    renders = DEMO / "renders"
    renders.mkdir(exist_ok=True)
    BASELINE_DIR.mkdir(parents=True, exist_ok=True)

    # Baseline mp4 lives at the stable BASELINE_DIR (outside any worktree) so it survives
    # worktree teardown between runs. Reuse the committed metrics record only when it BOTH
    # belongs to the current pin AND the mp4 is actually still on disk (assets-comps-02: the
    # record==pin shortcut used to skip re-rendering even when the mp4 was long gone, which
    # skipped SSIM silently forever after the first bump).
    base_mp4 = BASELINE_DIR / f"pin-baseline-{pin}.mp4"
    record = None
    if BASELINE_JSON.exists():
        record = json.loads(BASELINE_JSON.read_text(encoding="utf-8"))
        # a record measured on another demo (demo-joplin-90 before 26 Sep 26) is not a baseline
        if record.get("version") != pin or record.get("demo") != DEMO.name:
            record = None
    if record is None or not base_mp4.exists():
        render(pin, base_mp4)
        record = {"version": pin, "demo": DEMO.name, **measure(base_mp4)}
        # persist NOW — a crash in the candidate render must not cost this ~13 min again
        BASELINE_JSON.write_text(json.dumps(record, indent=2), encoding="utf-8")
    base_has_mp4 = base_mp4.exists()

    cand_mp4 = renders / f"pin-baseline-{latest}.mp4"
    render(latest, cand_mp4)
    cand = measure(cand_mp4)
    ssim_all = ssim(base_mp4, cand_mp4) if base_has_mp4 else None
    if not base_has_mp4:
        print("[ritual] no baseline mp4 on disk — SSIM skipped (metrics-only compare)")

    drifts = compare(record, cand, ssim_all)
    if base_has_mp4 and ssim_all is None:
        # an un-computable SSIM (e.g. resolution change broke the filter) is a failed
        # visual gate, never a silent pass
        drifts.append("SSIM could not be computed from ffmpeg output — visual identity "
                      "UNVERIFIED")
    print(f"[ritual] {pin} vs {latest}: duration {record['duration']:.3f}/"
          f"{cand['duration']:.3f}s, black {len(record['blackdetect'])}/"
          f"{len(cand['blackdetect'])} segs, RMS {record['rms_db']}/{cand['rms_db']} dB, SSIM "
          f"{'n/a' if ssim_all is None else f'{ssim_all:.4f}'}")
    if drifts:
        print(f"[ritual] METRIC DRIFT — NOT bumping {pin} -> {latest}:", file=sys.stderr)
        for d in drifts:
            print(f"    {d}", file=sys.stderr)
        print("[ritual] read the changelog, eyeball both renders, decide by hand.",
              file=sys.stderr)
        return 3

    bump_pins(latest)
    BASELINE_JSON.write_text(json.dumps({"version": latest, "demo": DEMO.name, **cand}, indent=2),
                             encoding="utf-8")
    if base_has_mp4:
        base_mp4.unlink()
    # Rename the candidate INTO the stable baseline slot for the new pin — it is already the
    # verified-current render, so the next stale-pin run finds it on disk and actually runs
    # SSIM instead of printing "no baseline mp4 on disk" forever (assets-comps-02).
    new_base = BASELINE_DIR / f"pin-baseline-{latest}.mp4"
    cand_mp4.replace(new_base)
    print(f"[ritual] PASS — pin bumped {pin} -> {latest}; baseline refreshed at {new_base}. "
          f"Commit + PR the bump (config.yaml, scripts/*.cmd, pin_baseline.json).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
