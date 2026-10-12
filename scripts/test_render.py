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


def run_verify(ep_dir, base, mode=None):
    return subprocess.run(["bash", str(S / "verify_render.sh"), str(ep_dir), base, *([mode] if mode else [])],
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

        # Review finding (23 Sep 26): silencedetect must exempt a declared hold/blackout/CTA
        # window (DESIGN.md "hold 2-4s in silence or low ambience"), not fail every real
        # episode's intentional emotional holds and chapter blackouts.
        mp4d = ep / "renders" / "held-final.mp4"
        # testsrc, not a static color: a still frame for the full 8s trips freezedetect on its
        # own (unrelated to the silence gate under test here) since nothing in the picture moves.
        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", "testsrc=size=320x240:rate=25:duration=8",
                        "-f", "lavfi", "-i", "sine=frequency=440:duration=8",
                        "-filter_complex", "[1:a]volume=enable='between(t,2,5)':volume=0[aout]",
                        "-map", "0:v", "-map", "[aout]",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(mp4d)],
                       capture_output=True)
        held_index = (
            '<div id="root" data-composition-id="x" data-start="0" data-width="320" '
            'data-height="240" data-duration="8.00" data-fps="25">'
            '<section class="clip hold" id="hold-1" data-start="2" data-duration="3" data-track-index="8"></section>'
            '</div>')
        (ep / "index.html").write_text(held_index, encoding="utf-8")
        r4 = run_verify(ep, "held-final")
        check("render-07 NEW: a 3s silent span INSIDE a declared hold passes",
              r4.returncode == 0, f"rc={r4.returncode}\n{r4.stdout[-800:]}")

        # Drop the <section> entirely (not just rename its class) — "hold-DISABLED" still
        # word-boundary-matches "hold" inside \b(?:blackout|hold)\b, so renaming alone would
        # not actually remove the sanctioned window.
        unheld_index = re.sub(r'<section class="clip hold".*?</section>', "", held_index)
        (ep / "index.html").write_text(unheld_index, encoding="utf-8")
        r5 = run_verify(ep, "held-final")
        check("render-07 NEW: the SAME 3s silent span with no declared hold fails",
              r5.returncode != 0 and "FAIL:" in r5.stdout and "silence span" in r5.stdout,
              f"rc={r5.returncode}\n{r5.stdout[-800:]}")

        # Black and freeze follow the same declared windows as silence: a designed blackout
        # (bo-close, bo-void) passes, the same span with nothing declared fails.
        def span_case(name, video_graph, dur, section, kind):
            mp4x = ep / "renders" / f"{name}-final.mp4"
            subprocess.run(["ffmpeg", "-y", "-v", "error", *video_graph,
                            "-f", "lavfi", "-i", f"sine=frequency=440:duration={dur}",
                            "-map", "[v]", "-map", f"{video_graph.count('-i')}:a",
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(mp4x)],
                           capture_output=True)
            root = (f'<div id="root" data-composition-id="x" data-start="0" data-width="320" '
                    f'data-height="240" data-duration="{dur}.00" data-fps="25">')
            (ep / "index.html").write_text(root + section + '</div>', encoding="utf-8")
            ok = run_verify(ep, f"{name}-final")
            (ep / "index.html").write_text(root + '</div>', encoding="utf-8")
            bad = run_verify(ep, f"{name}-final")
            check(f"render-07 NEW: a {kind} span inside a declared window passes",
                  ok.returncode == 0, f"rc={ok.returncode}\n{ok.stdout[-800:]}")
            check(f"render-07 NEW: the same {kind} span with nothing declared fails",
                  bad.returncode != 0 and f"FAIL: 1 {kind} span" in bad.stdout, f"rc={bad.returncode}\n{bad.stdout[-800:]}")

        span_case("black", ["-f", "lavfi", "-i", "testsrc=size=320x240:rate=25:duration=8",
                            "-filter_complex", "[0:v]drawbox=c=black:t=fill:enable='between(t,2,5)'[v]"], 8,
                  '<section class="clip blackout" id="bo-1" data-start="2" data-duration="3"></section>', "black")
        frozen = ["-f", "lavfi", "-i", "testsrc=size=320x240:rate=25:duration=2",
                  "-f", "lavfi", "-i", "color=c=gray:s=320x240:r=25:d=7",
                  "-f", "lavfi", "-i", "testsrc=size=320x240:rate=25:duration=2",
                  "-filter_complex", "[0:v][1:v][2:v]concat=n=3:v=1:a=0[v]"]
        span_case("frozen", frozen, 11,
                  '<section class="clip blackout" id="bo-2" data-start="2" data-duration="7"></section>', "freeze")

        # A hold may be quiet but must keep a live picture, and the CTA body must never be black
        # or frozen (a CTA that fails to decode renders black for 15 s): both still FAIL.
        root11 = ('<div id="root" data-composition-id="x" data-start="0" data-width="320" '
                  'data-height="240" data-duration="11.00" data-fps="25">')
        (ep / "index.html").write_text(root11 + '<section class="clip hold" id="hold-3" data-start="2" '
                                       'data-duration="7"></section></div>', encoding="utf-8")
        r6 = run_verify(ep, "frozen-final")
        check("render-07 NEW: a 7s freeze inside a declared hold still fails",
              r6.returncode != 0 and "FAIL: 1 freeze span" in r6.stdout, f"rc={r6.returncode}\n{r6.stdout[-800:]}")
        (ep / "index.html").write_text(root11.replace('11.00', '8.00') + '<video id="ins-cta-paul" '
                                       'src="media/cta/x.mp4" data-start="2" data-duration="3"></video></div>',
                                       encoding="utf-8")
        r7 = run_verify(ep, "black-final")
        check("render-07 NEW: a black span over the CTA body still fails",
              r7.returncode != 0 and "FAIL: 1 black span" in r7.stdout, f"rc={r7.returncode}\n{r7.stdout[-800:]}")

    # render-11 (12 Oct 26): a draft is rendered at render.cmd's 15 fps, so judging it against the
    # composition's data-fps failed every draft, and the log came from the basename ("draft" in it),
    # so a draft named ...-preview-v1 was checked against render_full.log. The mode is now an
    # argument; the final-render checks must keep failing.
    def mk_clip(path, fps):
        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", f"testsrc=size=320x240:rate={fps}:duration=2",
                        "-f", "lavfi", "-i", "sine=frequency=440:duration=2",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(path)],
                       capture_output=True)

    with tempfile.TemporaryDirectory() as d:
        ep = Path(d)
        (ep / "renders").mkdir()
        (ep / "index.html").write_text(
            '<div id="root" data-composition-id="x" data-start="0" data-width="320" '
            'data-height="240" data-duration="2.00" data-fps="25"></div>', encoding="utf-8")
        (ep / "render_draft.log").write_text("browserGpuMode probe worker0 NVIDIA GeForce GTX 1650\n", encoding="utf-8")
        (ep / "render_full.log").write_text("browserGpuMode probe worker0 Intel(R) UHD Graphics\n", encoding="utf-8")
        mk_clip(ep / "renders" / "pal-preview-v1.mp4", 15)
        mk_clip(ep / "renders" / "pal-24.mp4", 24)

        r = run_verify(ep, "pal-preview-v1", "draft")
        check("render-10 NEW: a 15 fps draft with no 'draft' in its name passes, reading render_draft.log",
              r.returncode == 0 and "OK: 320x240 @ 15/1" in r.stdout, f"rc={r.returncode}\n{r.stdout[-800:]}")
        r = run_verify(ep, "pal-preview-v1", "full")
        check("render-10 NEW: the same 15 fps file checked as a final still fails the fps check",
              r.returncode != 0 and "FAIL: fps 15 != full 25fps" in r.stdout, f"rc={r.returncode}\n{r.stdout[-800:]}")
        r = run_verify(ep, "pal-24", "draft")
        check("render-10 NEW: a draft at another rate than render.cmd's draft rate fails",
              r.returncode != 0 and "FAIL: fps 24 != draft 15fps" in r.stdout, f"rc={r.returncode}\n{r.stdout[-800:]}")
        r = run_verify(ep, "pal-preview-v1", "mastered")
        check("render-10 NEW: an unknown mode is a usage error, not a guess",
              r.returncode == 1 and "usage:" in r.stdout, f"rc={r.returncode}\n{r.stdout[-800:]}")
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
# The real HyperFrames log line is JSON (`streaming-encode gate {"renderJobId":"...",
# "enabled":true,...}`), copied verbatim from a real render_full.log
# (.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak/render_full.log:156) —
# the old regex `streaming-encode gate.*enabled:true` never matches this JSON form, so the
# ritual could never pass. Exercise all three cases through the same harness.
def _run_render_against_log(log_body):
    # render() opens its log path with "w" (truncating it) as part of the real subprocess
    # call, so a log pre-written before calling render() would be wiped before the ritual
    # ever reads it back. The fake subprocess.run must write log_body into the same
    # stdout=lf file handle render() passes it, the way the real npx child would.
    with tempfile.TemporaryDirectory() as d:
        fake_demo = Path(d)
        (fake_demo / "index.html").write_text("<div></div>", encoding="utf-8")
        pin_ritual.DEMO = fake_demo
        out_mp4 = fake_demo / "out.mp4"
        out_mp4.write_bytes(b"not a real mp4, existence is all render() checks post-subprocess")

        class FakeCompleted:
            returncode = 0

        def fake_run(*a, **k):
            k["stdout"].write(log_body)
            return FakeCompleted()

        orig_run = pin_ritual.subprocess.run
        orig_which = pin_ritual.shutil.which
        pin_ritual.shutil.which = lambda name: "npx" if name == "npx" else orig_which(name)
        pin_ritual.subprocess.run = fake_run
        pin_ritual.FFPROBE = pin_ritual.FFMPEG = Path("ffmpeg")
        try:
            pin_ritual.render("9.9.9", out_mp4)
            return False, None
        except SystemExit as e:
            return True, str(e)
        finally:
            pin_ritual.subprocess.run = orig_run
            pin_ritual.shutil.which = orig_which


import contextlib, io
_orig_workers = pin_ritual.WORKERS
for _w, _want in ((1, True), (2, False)):
    pin_ritual.WORKERS = _w
    _buf = io.StringIO()
    with contextlib.redirect_stdout(_buf):
        _run_render_against_log("streaming-encode gate {\"enabled\":true}\n")
    check(f"pin-review NEW: [FALLBACK] single-worker line printed iff workers < 2 (workers={_w})",
          (pin_ritual.FALLBACK_1W in _buf.getvalue()) == _want, _buf.getvalue())
pin_ritual.WORKERS = _orig_workers

raised, _ = _run_render_against_log("some other log output, no streaming gate line\n")
check("render-09 NEW: render() exits when the log has no 'streaming-encode gate ... enabled:true'", raised)

REAL_GATE_LINE_TRUE = (
    '[INFO] streaming-encode gate {"renderJobId":"21a9bb7d-eeaf-4f12-976e-37c2a565e237",'
    '"enabled":true,"configFlag":true,"outputFormat":"mp4","workerCount":2,'
    '"durationSeconds":1050.9,"maxDurationSeconds":7200}\n'
)
raised, _ = _run_render_against_log(REAL_GATE_LINE_TRUE)
check("render-10 NEW: render() PASSES on the real JSON gate line (enabled:true) from "
      "render_full.log — proves the fixed regex matches HyperFrames' actual log format",
      not raised)

REAL_GATE_LINE_FALSE = REAL_GATE_LINE_TRUE.replace('"enabled":true', '"enabled":false')
assert '"enabled":false' in REAL_GATE_LINE_FALSE
raised, msg = _run_render_against_log(REAL_GATE_LINE_FALSE)
check("render-10 NEW: render() still FAILS on a JSON gate line with enabled:false",
      raised and "streaming-encode gate" in (msg or ""))

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

# ---------------------------------------------------------------------------
# pin policy 26 Sep 26: preflight keeps the drift LOCK but never checks npm currency (a
# newer release must not stop a render mid-episode); the ritual demo is the committed
# episodes/demo-pin with its video and tone probes (demo-joplin-90's gitignored media no
# longer exists anywhere).
# ---------------------------------------------------------------------------
with tempfile.TemporaryDirectory() as d:
    repo = Path(d)
    (repo / "scripts").mkdir()
    (repo / "config.yaml").write_text('render:\n  hyperframes_version: "0.8.78"\n', encoding="utf-8")
    (repo / "scripts" / "render.cmd").write_text("call npx hyperframes@0.8.78 render .\n", encoding="utf-8")
    orig_pf_run = render_preflight.subprocess.run

    def _no_network(*a, **k):
        raise AssertionError(f"version_check spawned {a[0] if a else k}")
    render_preflight.subprocess.run = _no_network
    try:
        check("pin-policy NEW: agreeing pins pass with no npm lookup (currency is kickoff's job)",
              render_preflight.version_check(repo) == 0)
        (repo / "scripts" / "draft.cmd").write_text("npx hyperframes@0.8.41 render .\n", encoding="utf-8")
        check("pin-policy NEW: a .cmd pinned to another version is still PIN DRIFT (exit 5)",
              render_preflight.version_check(repo) == 5)
    finally:
        render_preflight.subprocess.run = orig_pf_run
check("pin-policy NEW: RENDER_PIN_STALE_OK is gone from preflight",
      "RENDER_PIN_STALE_OK" not in (S / "render_preflight.py").read_text(encoding="utf-8"))

# pin_ritual.DEMO was repointed at a temp dir by the render() harness above; read the source
check("pin-policy NEW: the ritual demo is episodes/demo-pin",
      'DEMO = REPO / "episodes" / "demo-pin"' in main_src)
DEMO = S.parent / "episodes" / "demo-pin"
demo_refs = []
for f in [DEMO / "index.html", *(DEMO / "compositions").glob("*.html")]:
    demo_refs += re.findall(r'(?:src="|url\(\')([^"\'#:]+\.(?:js|ttf|html|woff2?|png|jpg|mp4|webm|wav|mp3|ogg))',
                            f.read_text(encoding="utf-8"))
missing = [r for r in demo_refs if not (DEMO / r).exists()]
check("pin-policy NEW: every file demo-pin references exists", demo_refs and not missing, missing)
check("pin-review NEW: demo-pin mounts the video and audio probes",
      {"clips/probe.webm", "sfx/tone.ogg"} <= set(demo_refs), demo_refs)
# tracked, not merely "not ignored": check-ignore passes vacuously on an untracked file
_tracked = subprocess.run(["git", "-C", str(DEMO), "ls-files", "-z", "."],
                          capture_output=True, text=True).stdout.split("\0")
untracked = [r for r in demo_refs if r not in _tracked]
check("pin-policy NEW: every file demo-pin references is tracked (a fresh worktree can render it)",
      not untracked, untracked)
_bytes = sum((DEMO / f).stat().st_size for f in _tracked if f)
check("pin-review NEW: tracked demo-pin stays under 2 MB", 0 < _bytes < 2 * 1024 * 1024, _bytes)

# measure()'s silent branch: no astats lines and no audio stream -> levels None, no SystemExit
_orig_prun = pin_ritual.run

class _Out:
    def __init__(self, out=""):
        self.stdout, self.stderr = out, ""

pin_ritual.run = lambda cmd, **k: _Out("24.0\n" if "format=duration" in cmd else "")
pin_ritual.FFPROBE = pin_ritual.FFMPEG = Path("ffmpeg")
_m = {}
try:
    _m = pin_ritual.measure(Path("silent.mp4"))
    check("pin-review NEW: measure() on a silent render returns rms_db None without exiting",
          _m["rms_db"] is None and _m["peak_db"] is None and _m["duration"] == 24.0, _m)
except SystemExit as e:
    check("pin-review NEW: measure() on a silent render returns rms_db None without exiting",
          False, f"SystemExit {e}")
finally:
    pin_ritual.run = _orig_prun
check("pin-review NEW: measure() stores the worker count", _m.get("workers") == pin_ritual.WORKERS)

good = {"workers": 2, "duration": 24.0, "blackdetect": [], "rms_db": -30.0,
        "video_luma": [159.3, 235.2, 159.3]}
check("pin-review NEW: identical records with audio + video compare clean",
      pin_ritual.compare(good, dict(good), 0.997, 0.997) == [])
check("pin-review NEW: a silent render is drift (mixer unverified), even on both sides",
      pin_ritual.compare({**good, "rms_db": None}, {**good, "rms_db": None}, 0.997) != [])
check("pin-review NEW: audio appearing on one side only is drift",
      pin_ritual.compare({**good, "rms_db": None}, good, 0.997) != [])
check("pin-review NEW: an RMS shift past RMS_TOL is drift",
      pin_ritual.compare(good, {**good, "rms_db": -30.0 - 2 * pin_ritual.RMS_TOL}, 0.997) != [])
check("pin-review NEW: a moved video-probe tracer (seek changed) is drift",
      pin_ritual.compare(good, {**good, "video_luma": [159.3, 159.3, 159.3]}, 0.997) != [])
check("pin-review NEW: an unmeasured video probe is drift",
      pin_ritual.compare({**good, "video_luma": []}, {**good, "video_luma": []}, 0.997) != [])
check("pin-review NEW: a worker-count mismatch is drift",
      pin_ritual.compare(good, {**good, "workers": 1}, 0.997) != [])
check("pin-review NEW: a video-region SSIM under SSIM_MIN is drift",
      pin_ritual.compare(good, dict(good), 0.997, 0.95) != [])
check("pin-review NEW: a baseline record without video_luma/workers, or silent/flat, is re-rendered",
      'or baseline_problems(record)):' in main_src
      and all(pin_ritual.baseline_problems({k: v for k, v in good.items() if k != drop})
              for drop in ("workers", "video_luma", "rms_db")))

# (c) the baseline self-check is absolute: a flat trace equals itself, so compare() alone passes it
check("pin-review2 NEW: a good baseline (trace spans >= VIDEO_LUMA_SPAN_MIN) has no problems",
      pin_ritual.baseline_problems(good) == [], pin_ritual.baseline_problems(good))
_flat = {**good, "video_luma": [159.3] * 54}
check("pin-review2 NEW: a flat video trace fails the baseline self-check",
      pin_ritual.compare(_flat, dict(_flat), None) == [] and pin_ritual.baseline_problems(_flat) != [])
check("pin-review2 NEW: a trace spanning just under VIDEO_LUMA_SPAN_MIN fails",
      pin_ritual.baseline_problems({**good, "video_luma": [100.0, 100.0 + pin_ritual.VIDEO_LUMA_SPAN_MIN - 0.1]}) != [])
check("pin-review2 NEW: a silent baseline fails the self-check",
      pin_ritual.baseline_problems({**good, "rms_db": None}) != [])
# (d) audio is read over the tone's mount window, not the whole file
check("pin-review2 NEW: astats reads only TONE_WIN (inside the 3-7 s tone mount)",
      pin_ritual.TONE_WIN == (3.1, 6.9) and "atrim=start={TONE_WIN[0]}:end={TONE_WIN[1]},astats" in main_src)

# (b) --baseline: measure, validate, THEN write; old vs new printed; no "Commit" before validation
def _baseline_run(rec):
    with tempfile.TemporaryDirectory() as d:
        bj = Path(d) / "pin_baseline.json"
        bj.write_text(json.dumps({"version": "0.8.41", "demo": "demo-joplin-90"}), encoding="utf-8")
        base = Path(d) / "pin-baseline-0.8.78.mp4"
        base.write_bytes(b"old")
        saved = (pin_ritual.BASELINE_JSON, pin_ritual.BASELINE_DIR, pin_ritual.render, pin_ritual.measure,
                 pin_ritual.setup, pin_ritual.parse_pin, sys.argv)
        pin_ritual.BASELINE_JSON, pin_ritual.BASELINE_DIR = bj, Path(d)
        pin_ritual.render = lambda v, mp4: mp4.write_bytes(b"new")
        pin_ritual.measure = lambda mp4: dict(rec)
        pin_ritual.setup = lambda: None
        pin_ritual.parse_pin = lambda repo: "0.8.78"
        sys.argv = ["pin_ritual.py", "--baseline"]
        out, err = io.StringIO(), io.StringIO()
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                try:
                    code = pin_ritual.main()
                except SystemExit as e:
                    code = e.code
        finally:
            (pin_ritual.BASELINE_JSON, pin_ritual.BASELINE_DIR, pin_ritual.render, pin_ritual.measure,
             pin_ritual.setup, pin_ritual.parse_pin, sys.argv) = saved
        return (code, json.loads(bj.read_text(encoding="utf-8")), out.getvalue(), err.getvalue(),
                base.read_bytes())

_code, _written, _out, _err, _mp4 = _baseline_run(_flat)
check("pin-review2 NEW: --baseline on a flat trace exits 2 and leaves pin_baseline.json untouched",
      _code == 2 and _written.get("version") == "0.8.41", (_code, _written))
check("pin-final NEW: --baseline on a flat trace leaves the baseline mp4 untouched",
      _mp4 == b"old", _mp4)
check("pin-review2 NEW: --baseline never prints Commit when validation fails",
      "Commit" not in _out + _err, _out + _err)
_code, _written, _out, _err, _mp4 = _baseline_run(good)
check("pin-review2 NEW: --baseline on a good record exits 0 and writes it",
      _code == 0 and _written.get("version") == "0.8.78" and _written.get("video_luma") == good["video_luma"],
      (_code, _written))
check("pin-final NEW: --baseline on a good record replaces the baseline mp4",
      _mp4 == b"new", _mp4)
check("pin-review2 NEW: --baseline prints old vs new version, demo and workers",
      all(t in _out for t in ("version 0.8.41 -> 0.8.78", f"demo demo-joplin-90 -> {pin_ritual.DEMO.name}",
                              "workers None -> 2")), _out)
check("pin-review2 NEW: --baseline prints Commit only after the summary line",
      "Commit" in _out and _out.index("Commit") > _out.index("re-recorded"), _out)

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("render fixes self-check: ALL PASS")
