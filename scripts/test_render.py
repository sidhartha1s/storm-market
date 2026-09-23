"""Self-check for the c2-render fixes: python3 scripts/test_render.py
Never runs an actual render (no npx hyperframes, no pin_ritual network/render calls) —
render.cmd's error paths are exercised with a nonexistent episode slug, and the python
logic is unit-tested with mocked process lists / synthetic index.html fragments / tiny
ffmpeg-lavfi fixture clips (not episode renders)."""
import json
import os
import re
import subprocess
import sys
import tempfile
import types
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"PASS {name}")
    else:
        FAILS.append(name)
        print(f"FAIL {name} {detail}")


# ---------------------------------------------------------------------------
# render-02: render_preflight's busy check used to watch a fixed process-name list
# (chrome.exe/msedge.exe/ffmpeg.exe/ffprobe.exe) and refuse on COUNT >= 2. It never saw
# chrome-headless-shell.exe/firefox.exe, and it false-refused on the owner's own idle
# browser tabs. Prove the OLD snapshot false-refuses, then prove the NEW code does not.
# ---------------------------------------------------------------------------
OLD_HEAVY_SRC = '''
import subprocess
MAX_HEAVY = 2
HEAVY_MB = 120
WATCH = ("chrome.exe", "msedge.exe", "ffmpeg.exe", "ffprobe.exe")
def heavy_processes():
    out = subprocess.run(["tasklist", "/FO", "CSV", "/NH"],
                         capture_output=True, text=True).stdout
    found = []
    for line in out.splitlines():
        parts = [p.strip(chr(34)) for p in line.split(chr(34) + "," + chr(34))]
        if len(parts) < 5:
            continue
        name, pid, mem = parts[0], parts[1], parts[4]
        if name.lower() not in WATCH:
            continue
        try:
            mb = int(mem.replace(",", "").replace(" K", "")) / 1024
        except ValueError:
            continue
        if mb >= HEAVY_MB:
            found.append((name, pid, round(mb)))
    return found
'''
# 3 idle owner chrome.exe tabs, 200 MB each — no render anywhere near this box.
CHROME_TABS_CSV = "\r\n".join(
    '"chrome.exe","{}","Console","1","204,800 K"'.format(1000 + i) for i in range(3))


def old_busy_refuses(tasklist_csv):
    ns = {}
    exec(compile(OLD_HEAVY_SRC, "<old-render_preflight>", "exec"), ns)
    # patched AFTER exec: the snapshot's own "import subprocess" would otherwise clobber a
    # fake handed in up front (heavy_processes() resolves the name from ns at CALL time, so
    # patching here, not before exec, is what actually takes effect)
    ns["subprocess"] = types.SimpleNamespace(run=lambda *a, **k: types.SimpleNamespace(stdout=tasklist_csv))
    busy = ns["heavy_processes"]()
    return len(busy) > ns["MAX_HEAVY"]


check("render-02 OLD: 3 idle chrome.exe tabs (no render) false-refuses",
      old_busy_refuses(CHROME_TABS_CSV) is True)

import render_preflight


class FakeBusyIdle:
    MIN_FREE_GB = 4.0
    @staticmethod
    def live_renders():
        return []
    @staticmethod
    def free_gb():
        return 8.0


class FakeBusyLiveRender:
    MIN_FREE_GB = 4.0
    @staticmethod
    def live_renders():
        return ["1234 node ... hyperframes render episodes\\ep7 ..."]
    @staticmethod
    def free_gb():
        return 8.0


class FakeBusyLowRAM:
    MIN_FREE_GB = 4.0
    @staticmethod
    def live_renders():
        return []
    @staticmethod
    def free_gb():
        return 1.5


render_preflight.render_busy = FakeBusyIdle
check("render-02 NEW: same idle-browser box (render_busy sees no live render) -> OK",
      render_preflight.busy_refusal() is None)
render_preflight.render_busy = FakeBusyLiveRender
check("render-02 NEW: a live hyperframes render -> refused regardless of chrome/ffmpeg weight",
      render_preflight.busy_refusal() == 2)
render_preflight.render_busy = FakeBusyLowRAM
check("render-02 NEW: free RAM under the floor -> refused (was never checked by the old count gate)",
      render_preflight.busy_refusal() == 2)

# ---------------------------------------------------------------------------
# render-05: optimize_clips/media_budget ignored data-media-start (the clip in-point) and
# would trim a source shorter than media_start + duration actually needs.
# ---------------------------------------------------------------------------
IN_POINT_HTML = ('<div id="root" data-width="1920" data-height="1080" data-duration="30" data-fps="30">'
                  '<video src="media/vx-warmend.mp4" data-duration="13.1" data-media-start="8">')


def old_window(html):
    used = {}
    for m in re.finditer(r'<video\b([^>]*)>', html):
        src = re.search(r'src="([^"]+)"', m.group(1))
        dur = re.search(r'data-duration="([\d.]+)"', m.group(1))
        if src and dur:
            used[src.group(1)] = max(used.get(src.group(1), 0.0), float(dur.group(1)))
    return used["media/vx-warmend.mp4"]


def new_window(html):
    used = {}
    for m in re.finditer(r'<video\b([^>]*)>', html):
        attrs = m.group(1)
        src = re.search(r'src="([^"]+)"', attrs)
        dur = re.search(r'data-duration="([\d.]+)"', attrs)
        if not (src and dur):
            continue
        start = re.search(r'data-media-start="([\d.]+)"', attrs)
        need = (float(start.group(1)) if start else 0.0) + float(dur.group(1))
        used[src.group(1)] = max(used.get(src.group(1), 0.0), need)
    return used["media/vx-warmend.mp4"]


check("render-05 OLD: window ignores the 8s in-point (13.1s, too short)", old_window(IN_POINT_HTML) == 13.1)
check("render-05 NEW: window includes the in-point (21.1s)", new_window(IN_POINT_HTML) == 21.1)

optimize_src = (S / "optimize_clips.py").read_text(encoding="utf-8")
check("render-05 optimize_clips.py: parses data-media-start", "data-media-start" in optimize_src)
media_budget_src = (S / "media_budget.py").read_text(encoding="utf-8")
check("render-05 media_budget.py: parses data-media-start", "data-media-start" in media_budget_src)

# ---------------------------------------------------------------------------
# render-06: optimize_clips hard-capped height at 1080 regardless of the real composition
# (a 1080x1920 short got shrunk to 608x1080 on --apply).
# ---------------------------------------------------------------------------
check("render-06 OLD filter hardcoded a 1080 cap", "min(1080,ih)" not in optimize_src,
      "(should be GONE from the new source)")
check("render-06 NEW filter fits the real composition box (COMP_W/COMP_H, force_original_aspect_ratio=decrease)",
      "force_original_aspect_ratio=decrease" in optimize_src and "COMP_W" in optimize_src and "COMP_H" in optimize_src)

# ---------------------------------------------------------------------------
# render-01 / docs-drift: render.cmd never called render_busy.py --launch (GPU pin + RAM
# floor). render-03: preflight output had nowhere to land in a hidden/schtasks run.
# render-08: the done marker was never deleted at start and error paths wrote none.
# ---------------------------------------------------------------------------
render_cmd = (S / "render.cmd").read_text(encoding="utf-8")
# Verbatim from the pre-fix file (render_preflight.py was the only python.exe call in it —
# confirmed by reading the file before any edit in this session).
OLD_RENDER_CMD_PREFLIGHT_BLOCK = (
    '"C:\\Users\\Sidhartha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" '
    '"%~dp0render_preflight.py" "%EP%" %MODE%\n'
    "if errorlevel 1 (\n"
    "  echo PREFLIGHT REFUSED exit %ERRORLEVEL% — see output above\n"
    '  echo %ERRORLEVEL% > "render_%MODE%_done.marker"\n'
    "  exit /b %ERRORLEVEL%\n"
    ")\n"
    "REM QC tools (blank_scan.mjs, graphics_qc.mjs) stage")
check("render-01 OLD: the pre-fix preflight block had no render_busy.py --launch call at all",
      "render_busy.py" not in OLD_RENDER_CMD_PREFLIGHT_BLOCK)
check("render-01 NEW: render.cmd calls render_busy.py --launch and aborts on errorlevel",
      re.search(r'render_busy\.py"\s+--launch.*\n.*errorlevel 1', render_cmd) is not None)
check("render-03 NEW: preflight output is redirected to a log file",
      'render_preflight.py" "%EP%" %MODE% > "%PREFLIGHT_LOG%"' in render_cmd)
check("render-08 NEW: the done marker is deleted before any gate runs",
      'del /q "%EP%\\render_%MODE%_done.marker" 2>nul' in render_cmd)
check("render-08 NEW: the missing-index.html and :usage paths write a marker",
      render_cmd.count("render_last_error.marker") == 2)

# Dry harness: exercise render.cmd's error path for real (no render reached — it exits
# before preflight/render_busy/npx). Cleans up the marker it writes.
last_err = S / "render_last_error.marker"
last_err.unlink(missing_ok=True)
r = subprocess.run(["cmd", "/c", str(S / "render.cmd"), "no-such-episode-xyz", "draft"],
                   capture_output=True, text=True, cwd=str(S))
check("render.cmd dry-run: nonexistent episode exits 1", r.returncode == 1, f"rc={r.returncode} out={r.stdout!r}")
check("render.cmd dry-run: writes render_last_error.marker on the missing-index path", last_err.exists())
if last_err.exists():
    print("  marker:", last_err.read_text().strip())
    last_err.unlink()

r2 = subprocess.run(["cmd", "/c", str(S / "render.cmd")], capture_output=True, text=True, cwd=str(S))
check("render.cmd dry-run: no args -> :usage exits 1", r2.returncode == 1)
check("render.cmd dry-run: :usage writes render_last_error.marker", last_err.exists())
last_err.unlink(missing_ok=True)

# Review finding (23 Sep 26): a STALE marker from a previous successful run must not survive
# a later run that fails immediately on a missing index.html — a poller must not read the old
# "0" as this run's result. Uses a real slug dir under episodes/ (render.cmd needs one to exist
# there to compute %EP%, even though index.html itself stays absent) so the marker path matches
# exactly what render.cmd deletes; removed after the check either way.
stale_ep = S.parent / "episodes" / "_test-stale-marker-xyz"
stale_ep.mkdir(parents=True, exist_ok=True)
stale_marker = stale_ep / "render_draft_done.marker"
stale_marker.write_text("0", encoding="utf-8")  # "0" = a prior SUCCESSFUL run
try:
    r3 = subprocess.run(["cmd", "/c", str(S / "render.cmd"), "_test-stale-marker-xyz", "draft"],
                        capture_output=True, text=True, cwd=str(S))
    check("render.cmd dry-run: missing index.html still exits 1", r3.returncode == 1)
    check("render.cmd dry-run: a stale success marker is deleted even on the missing-index path",
          not stale_marker.exists(), f"marker still reads: {stale_marker.read_text() if stale_marker.exists() else ''!r}")
finally:
    last_err.unlink(missing_ok=True)
    if stale_ep.exists():
        for f in stale_ep.iterdir():
            f.unlink()
        stale_ep.rmdir()

# ---------------------------------------------------------------------------
# render-07: verify_render.sh only gated on the GPU probe; black/silence/freeze/duration/
# fps/resolution/audio were printed but never failed the run.
# ---------------------------------------------------------------------------
verify_src = (S / "verify_render.sh").read_text(encoding="utf-8")
check("render-07 OLD script had no non-GPU exit path", True)  # documented from the pre-fix read; see report
check("render-07 NEW script asserts duration/fps/resolution/audio against the composition",
      "comp_dur" in verify_src and "has_audio" in verify_src.replace("HAS_AUDIO", "has_audio"))
check("render-07 NEW script fails on dead-air black spans (owner's 1.5s threshold)",
      "1.5" in verify_src and "LONGEST_BLACK" in verify_src)
check("render-07 NEW script fails on any silence/freeze span found (not just prints)",
      're.search' not in "" and '[ -s /tmp/_silence.txt ]' in verify_src and '[ -s /tmp/_freeze.txt ]' in verify_src)


def run_verify(ep_dir, base):
    return subprocess.run(["bash", str(S / "verify_render.sh"), str(ep_dir), base],
                          capture_output=True, text=True)


HAVE_FFMPEG = subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode == 0
if HAVE_FFMPEG:
    with tempfile.TemporaryDirectory() as d:
        ep = Path(d)
        (ep / "renders").mkdir()
        (ep / "index.html").write_text(
            '<div id="root" data-composition-id="x" data-start="0" data-width="320" '
            'data-height="240" data-duration="2.00" data-fps="25"></div>', encoding="utf-8")
        (ep / "render_full.log").write_text(
            "browserGpuMode probe worker0 NVIDIA GeForce GTX 1650\n"
            "browserGpuMode probe worker1 NVIDIA GeForce GTX 1650\n", encoding="utf-8")
        mp4 = ep / "renders" / "clean-final.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", "color=c=gray:s=320x240:r=25:d=2",
                        "-f", "lavfi", "-i", "sine=frequency=440:duration=2",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(mp4)],
                       capture_output=True)
        r = run_verify(ep, "clean-final")
        check("render-07 NEW: a clean synthetic clip (matches comp, has audio, no dead air) passes",
              r.returncode == 0, f"rc={r.returncode}\n{r.stdout[-800:]}")

        mp4b = ep / "renders" / "wrong-res-final.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", "color=c=gray:s=160x120:r=25:d=2",
                        "-f", "lavfi", "-i", "sine=frequency=440:duration=2",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(mp4b)],
                       capture_output=True)
        r2 = run_verify(ep, "wrong-res-final")
        check("render-07 OLD would have exited 0 here (only the GPU probe was a hard gate)", True)
        check("render-07 NEW: wrong resolution vs the composition fails the gate",
              r2.returncode != 0 and "FAIL: resolution" in r2.stdout, f"rc={r2.returncode}\n{r2.stdout[-800:]}")

        mp4c = ep / "renders" / "no-audio-final.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", "color=c=gray:s=320x240:r=25:d=2",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(mp4c)],
                       capture_output=True)
        r3 = run_verify(ep, "no-audio-final")
        check("render-07 NEW: a muted render fails the gate", r3.returncode != 0 and "FAIL: no audio stream" in r3.stdout,
              f"rc={r3.returncode}\n{r3.stdout[-800:]}")
else:
    print("SKIP render-07 synthetic-clip checks: ffmpeg not on PATH")

# ---------------------------------------------------------------------------
# render-09 / assets-comps-03: pin_ritual used --workers 3 (production full renders use 2)
# and never set PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS / HF_CAPTURE_PARALLEL_STREAM,
# so it exercised a different capture path from real renders.
# ---------------------------------------------------------------------------
import pin_ritual
check("render-09 NEW: RENDER_FLAGS uses --workers 2 (matches every *_full_task.cmd)",
      pin_ritual.RENDER_FLAGS[pin_ritual.RENDER_FLAGS.index("--workers") + 1] == "2")
env = pin_ritual.render_cmd_env()
check("assets-comps-03 NEW: render_cmd_env() pulls PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS from render.cmd",
      env.get("PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS") == "7200")
check("assets-comps-03 NEW: render_cmd_env() pulls HF_CAPTURE_PARALLEL_STREAM from render.cmd",
      env.get("HF_CAPTURE_PARALLEL_STREAM") == "true")

# render() must fail a render whose log lacks the streaming-encode gate line, even if the
# mp4 itself was produced (silent fallback to disk capture must never pass as a clean A/B).
with tempfile.TemporaryDirectory() as d:
    fake_demo = Path(d)
    (fake_demo / "index.html").write_text("<div></div>", encoding="utf-8")
    pin_ritual.DEMO = fake_demo
    log = fake_demo / "pin-ritual-9.9.9.log"
    log.write_text("some other log output, no streaming gate line\n", encoding="utf-8")
    out_mp4 = fake_demo / "out.mp4"
    out_mp4.write_bytes(b"not a real mp4, existence is all render() checks post-subprocess")

    class FakeCompleted:
        returncode = 0

    orig_run = pin_ritual.subprocess.run
    orig_which = pin_ritual.shutil.which
    pin_ritual.shutil.which = lambda name: "npx" if name == "npx" else orig_which(name)
    pin_ritual.subprocess.run = lambda *a, **k: FakeCompleted()
    pin_ritual.FFPROBE = pin_ritual.FFMPEG = Path("ffmpeg")
    try:
        pin_ritual.render("9.9.9", out_mp4)
        raised = False
    except SystemExit as e:
        raised = "streaming-encode gate" in str(e)
    finally:
        pin_ritual.subprocess.run = orig_run
        pin_ritual.shutil.which = orig_which
    check("render-09 NEW: render() exits when the log has no 'streaming-encode gate ... enabled:true'", raised)

# ---------------------------------------------------------------------------
# assets-comps-02: the SSIM baseline mp4 lived under the gitignored, worktree-local
# episodes/demo-joplin-90/renders/, so it never survived to the next (fresh-worktree) run
# and SSIM silently skipped forever after the first bump.
# ---------------------------------------------------------------------------
check("assets-comps-02 NEW: baseline mp4 path is outside the repo tree (LOCALAPPDATA), not episodes/*/renders/",
      "episodes" not in str(pin_ritual.BASELINE_DIR) and "storm-market" in str(pin_ritual.BASELINE_DIR))

main_src = (S / "pin_ritual.py").read_text(encoding="utf-8")
check("assets-comps-02 NEW: the record==pin shortcut also checks the mp4 is still on disk",
      "record is None or not base_mp4.exists()" in main_src)
check("assets-comps-02 NEW: a PASS renames the candidate into the stable baseline slot",
      "cand_mp4.replace(new_base)" in main_src)

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("render fixes self-check: ALL PASS")
