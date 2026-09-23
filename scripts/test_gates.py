"""Self-check for the c1-gates fixes: python3 scripts/test_gates.py

Builds throwaway episodes carrying each bug class and a clean twin (style of
test_comp_gates.py). Every assertion here is about NEW behavior; the old-vs-old
comparison quoted in the fixer report was done separately with `git show HEAD:<path>`
before these edits were committed.
"""
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

S = Path(__file__).resolve().parent
FAILS = []


def check(label, cond, detail=""):
    if cond:
        print(f"PASS {label}")
    else:
        FAILS.append(label)
        print(f"FAIL {label} {detail}")


def run(script, *args, cwd=None):
    r = subprocess.run([sys.executable, str(S / script), *[str(a) for a in args]],
                       capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout + r.stderr


def run_node(script, *args, cwd=None):
    r = subprocess.run(["node", str(S / script), *[str(a) for a in args]],
                       capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout + r.stderr


def write_wav(path, seconds, rate=8000):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(b"\x00\x00" * int(seconds * rate))


# ===================================================================================
# 1. comp_consts.fold — identifier-digit-eating + operator precedence (qc-gates-10 RCA)
# ===================================================================================
from comp_consts import fold  # noqa: E402

check("fold: leaves an unresolvable identifier position alone (t0 + 0.25)",
      fold('tl.to(a,{}, t0 + 0.25);') == 'tl.to(a,{}, t0 + 0.25);')
check("fold: leaves an unresolvable identifier position alone (x1 + 4)",
      fold('tl.to(a,{}, x1 + 4);') == 'tl.to(a,{}, x1 + 4);')
check("fold: multiplies before it subtracts (DUR - 2 * 0.5 -> 9.0, not 4.0)",
      "9.0" in fold('const DUR = 10; tl.to(a,{}, DUR - 2 * 0.5);'))
check("fold: still folds a known const's arithmetic (CUES.six + 1.5 -> 8.34)",
      "8.34" in fold('const CUES = { six: 6.84 }; tl.to(a,{}, CUES.six + 1.5);'))

# ===================================================================================
# 2 + 5. sweep_episode.py — exit code, freshness gate, check-7 coverage
# ===================================================================================
GSAP = (Path(__file__).resolve().parent.parent / "library/gallery/gsap.min.js").read_text(encoding="utf-8")


def make_ep(d, comp_html=None, nx_dur=1.0, nx_wav_secs=1.0, words_last_end=None,
            words_mtime_before_wav=False, unparsed_tween=False, comp_window=2.0):
    # Track 1 carries a plain background video spanning the WHOLE episode (picture coverage);
    # the composition mounts on track 3, same as real episodes ("overlay comps ride tracks
    # 3-4") — mounting a graphic directly on track 1 makes an unrelated check (5, "media files
    # exist") look for a file literally named after the composition id and fail on it.
    ep = Path(d)
    ep.mkdir(parents=True, exist_ok=True)
    (ep / "compositions").mkdir()
    (ep / "audio").mkdir()
    (ep / "media").mkdir()
    (ep / "gsap.min.js").write_text(GSAP, encoding="utf-8")
    write_wav(ep / "audio" / "a1-s1.wav", nx_wav_secs)
    words = [{"text": "hi", "start": 0.0, "end": nx_wav_secs if words_last_end is None else words_last_end}]
    (ep / "audio" / "a1-s1.words.json").write_text(json.dumps(words), encoding="utf-8")
    if words_mtime_before_wav:
        import os
        wj = ep / "audio" / "a1-s1.words.json"
        st = (ep / "audio" / "a1-s1.wav").stat()
        os.utime(wj, (st.st_atime - 10, st.st_mtime - 10))
    tween_extra = 'tl.to("#x", {duration: 0.2}, i * 0.2);' if unparsed_tween else ''
    comp = comp_html or (
        f'<template><div id="g"><span id="t">hi</span></div>'
        f'<script>const DUR={comp_window}; tl.to("#t", {{duration:1}}, 0.1); {tween_extra}</script></template>'
    )
    (ep / "compositions" / "g1.html").write_text(comp, encoding="utf-8")
    total = max(comp_window, nx_dur) + 0.5
    html = f'''<section data-duration="{total}">
<div id="root" data-width="1920" data-height="1080"></div>
<video data-start="0" data-duration="{total}" data-track-index="1" src="media/bg.mp4" muted></video>
<div data-composition-id="g1" data-start="0" data-duration="{comp_window}" data-track-index="3"></div>
<audio id="nx-a1s1" src="audio/a1-s1.wav" data-start="0" data-duration="{nx_dur}"></audio>
</section>'''
    (ep / "index.html").write_text(html, encoding="utf-8")
    (ep / "media" / "bg.mp4").write_bytes(b"0")
    return ep


with tempfile.TemporaryDirectory() as d:
    ep_clean = make_ep(Path(d) / "clean")
    code, out = run("sweep_episode.py", ep_clean)
    check("sweep_episode: exits 0 on a clean episode", code == 0, f"(exit {code})\n{out[-400:]}")

with tempfile.TemporaryDirectory() as d:
    # data-duration (1.0) doesn't match the real wav (2.0s) -> freshness gate must FAIL, and the
    # whole process must exit non-zero (docs-drift-sweep-exit-zero)
    ep_stale = make_ep(Path(d) / "stale", nx_dur=1.0, nx_wav_secs=2.0)
    code, out = run("sweep_episode.py", ep_stale)
    check("sweep_episode: exits 1 when a FAIL is printed (was exit 0 unconditionally)", code == 1, f"(exit {code})")
    check("sweep_episode: freshness gate catches a stale data-duration vs the real wav",
          "narration freshness" in out and "FAIL" in out, out[-600:])

with tempfile.TemporaryDirectory() as d:
    # words.json last word ends past the wav -> stale words.json, same class as ep3-tristate a3-s7
    ep_stale2 = make_ep(Path(d) / "stalewords", nx_dur=2.0, nx_wav_secs=2.0, words_last_end=5.0)
    code, out = run("sweep_episode.py", ep_stale2)
    check("sweep_episode: freshness gate catches a words.json whose last word outruns the wav",
          code == 1 and "last word ends" in out, out[-600:])

with tempfile.TemporaryDirectory() as d:
    ep_unparsed = make_ep(Path(d) / "unparsed", unparsed_tween=True)
    code, out = run("sweep_episode.py", ep_unparsed)
    check("sweep_episode: check 7 reports unparsed tween coverage instead of a silent pass",
          "parsed" in out and "tweens" in out, out[-600:])

# ===================================================================================
# 3. beat_density.py — exit code on a DEAD (>=4s motionless) composition
# ===================================================================================
with tempfile.TemporaryDirectory() as d:
    dead_comp = ('<template><div id="g"></div>'
                '<script>tl.to("#g", {duration: 0.1}, 0.1);</script></template>')
    ep_dead = make_ep(Path(d) / "dead", comp_html=dead_comp)
    code, out = run("beat_density.py", ep_dead)
    check("beat_density: exits 1 on a composition with a >=4s motionless stretch (was always 0)",
          code == 1, f"(exit {code})\n{out[-400:]}")

with tempfile.TemporaryDirectory() as d:
    live_comp = ('<template><div id="g"></div>'
                '<script>tl.to("#g", {duration: 2, ease: "none"}, 0);</script></template>')
    ep_live = make_ep(Path(d) / "live", comp_html=live_comp)
    code, out = run("beat_density.py", ep_live)
    check("beat_density: exits 0 on a composition with no dead stretch", code == 0, f"(exit {code})")

# ===================================================================================
# 4. audio_levels.py — data-hf-id id-collision bug, data-bed classification, 6dB FAIL,
#    unclassified-audio FAIL
# ===================================================================================
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    (ep / "media").mkdir()
    write_wav(ep / "media" / "nx.wav", 1.0)
    write_wav(ep / "media" / "bed.wav", 1.0)
    write_wav(ep / "media" / "unknown.wav", 1.0)
    html = '''<section>
<audio data-hf-id="hf-onw2" id="nx-a1s1" src="media/nx.wav" data-start="0" data-duration="1" data-volume="1"></audio>
<audio data-hf-id="hf-bed1" id="sfx-bed" src="media/bed.wav" data-bed data-start="0" data-duration="1" data-volume="1"></audio>
<audio id="mystery-1" src="media/unknown.wav" data-start="0" data-duration="1" data-volume="1"></audio>
</section>'''
    (ep / "index.html").write_text(html, encoding="utf-8")
    code, out = run("audio_levels.py", ep)
    check("audio_levels: reads the real id past a data-hf-id attribute (no more hf- misread)",
          "nx-a1s1" in out and "hf-onw2" not in out, out)
    check("audio_levels: a data-bed element at narration level FAILs (was warn-only)",
          "sfx-bed" in out and code == 1, out)
    check("audio_levels: an audio id that is neither nx-/ins- nor data-bed FAILs as unclassified",
          "mystery-1" in out and "unclassified" in out, out)

# ===================================================================================
# 6. lint_timeline.py — unmuted b-roll gate, narration-vs-wav gate, bounded CTA gap
# ===================================================================================
BANNED = (Path(__file__).resolve().parent.parent / "assets/sfx/BANNED.md5")


def make_lint_ep(d, extra_video="", nx2_dur=None, nx2_start=None, cta=False):
    ep = Path(d)
    (ep / "media").mkdir()
    (ep / "compositions").mkdir()
    write_wav(ep / "media" / "a1.wav", 2.0)
    if nx2_dur is not None:
        write_wav(ep / "media" / "a2.wav", 2.0)
    body = f'''<section data-duration="30">
<audio id="nx-a1" src="media/a1.wav" data-start="0" data-duration="2"></audio>
{extra_video}'''
    if nx2_dur is not None:
        body += f'<audio id="nx-a2" src="media/a2.wav" data-start="{nx2_start}" data-duration="{nx2_dur}"></audio>'
    if cta:
        body += '<video src="media/cta/paul.mp4" data-start="4.0" data-duration="2.0"></video>'
        (ep / "media" / "cta").mkdir()
        (ep / "media" / "cta" / "paul.mp4").write_bytes(b"0")
    body += "</section>"
    (ep / "index.html").write_text(body, encoding="utf-8")
    return ep


with tempfile.TemporaryDirectory() as d:
    v = '<video src="media/broll.mp4" data-start="0" data-duration="2" data-track-index="1"></video>'
    ep = make_lint_ep(Path(d), extra_video=v)
    (ep / "media" / "broll.mp4").write_bytes(b"0")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: FAILs unmuted track-1 video with no data-has-audio (FORMAT.md:57)",
          code == 1 and "unmuted b-roll" in out, out)

with tempfile.TemporaryDirectory() as d:
    v = '<video src="media/broll.mp4" data-start="0" data-duration="2" data-track-index="1" muted></video>'
    ep = make_lint_ep(Path(d), extra_video=v)
    (ep / "media" / "broll.mp4").write_bytes(b"0")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: a muted track-1 video passes clean", "unmuted b-roll" not in out, out)

with tempfile.TemporaryDirectory() as d:
    # narration window (1.0s) shorter than its real wav (2.0s) -> truncation gate (FORMAT.md:59)
    ep = Path(d)
    (ep / "media").mkdir(); (ep / "compositions").mkdir()
    write_wav(ep / "media" / "a1.wav", 2.0)
    (ep / "index.html").write_text(
        '<section data-duration="30">'
        '<audio id="nx-a1" src="media/a1.wav" data-start="0" data-duration="1.0"></audio>'
        '</section>', encoding="utf-8")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: FAILs a narration window shorter than its wav", code == 1 and "shorter than its wav" in out, out)

with tempfile.TemporaryDirectory() as d:
    # gap of 5s with no CTA and no structure -> already failed before; confirms baseline still works
    ep = make_lint_ep(Path(d), nx2_dur=2.0, nx2_start=7.0)
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: an unexplained 5s narration gap still FAILs", code == 1 and "narration gap" in out, out)

with tempfile.TemporaryDirectory() as d:
    # CTA sits in the gap but the dip either side is way past config dip_in/dip_out (1.0s) -> must now FAIL
    ep = make_lint_ep(Path(d), nx2_dur=2.0, nx2_start=11.0, cta=True)
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: an oversized CTA dip (config dip_in/dip_out) now FAILs (was unbounded)",
          code == 1 and ("dip-in" in out or "dip-out" in out), out)

# ===================================================================================
# 7. blank_scan.mjs — exit code + ancestor-opacity ink measurement
# ===================================================================================
with tempfile.TemporaryDirectory() as d:
    # a real blank: the whole composition is empty ink the entire 1s window
    ep = make_ep(Path(d) / "blank", comp_html='<template><div id="g"></div><script>tl.to("#g", {duration: 1}, 0);</script></template>')
    code, out = run_node("blank_scan.mjs", str(ep.resolve()))
    check("blank_scan: exits non-zero on a blank composition (was always 0)", code == 1, f"(exit {code})\n{out[-500:]}")

with tempfile.TemporaryDirectory() as d:
    # text is inside a parent tweened to opacity:0 the whole time -> must still read as blank
    comp = ('<template><div id="wrap" style="opacity:0"><span id="t">HELLO WORLD TEXT HERE</span></div>'
           '<script>tl.set("#wrap", {}, 0);</script></template>')
    ep = make_ep(Path(d) / "ghost", comp_html=comp)
    code, out = run_node("blank_scan.mjs", str(ep.resolve()))
    check("blank_scan: a parent at opacity:0 hides its text child from the ink count (qc-gates-09)",
          code == 1, f"(exit {code})\n{out[-500:]}")

# ===================================================================================
# 8. run_gates.py — stops at the first failing gate, in CLAUDE.md order, non-zero exit
# ===================================================================================
with tempfile.TemporaryDirectory() as d:
    stub_dir = Path(d) / "scripts"
    stub_dir.mkdir()
    order_log = Path(d) / "order.log"
    names = ["sweep_episode.py", "lint_timeline.py", "beat_density.py", "media_budget.py",
             "audio_levels.py"]
    for i, name in enumerate(names):
        fail_here = (name == "lint_timeline.py")
        (stub_dir / name).write_text(
            f'import sys\nopen(r"{order_log}", "a").write("{name}\\n")\n'
            f'sys.exit({1 if fail_here else 0})\n', encoding="utf-8")
    for name in ["blank_scan.mjs", "overlap_check.mjs", "occlusion_check.mjs", "graphics_qc.mjs"]:
        (stub_dir / name).write_text(
            f'const fs=require("fs"); fs.appendFileSync(String.raw`{order_log}`, "{name}\\n"); process.exit(0);',
            encoding="utf-8")
    real_run_gates = (S / "run_gates.py").read_text(encoding="utf-8")
    (stub_dir / "run_gates.py").write_text(real_run_gates, encoding="utf-8")
    ep = Path(d) / "ep"
    ep.mkdir()
    code, out = run(str(Path(d) / "scripts" / "run_gates.py"), ep) if False else (None, None)
    r = subprocess.run([sys.executable, str(stub_dir / "run_gates.py"), str(ep)],
                       capture_output=True, text=True)
    ran = order_log.read_text(encoding="utf-8").splitlines() if order_log.exists() else []
    check("run_gates: stops at the first failing gate (lint_timeline.py), never reaches later gates",
          ran == ["sweep_episode.py", "lint_timeline.py"], f"ran={ran}\n{r.stdout}{r.stderr}")
    check("run_gates: exits non-zero when a gate fails", r.returncode == 1, f"(exit {r.returncode})")
    check("run_gates: names the failing gate", "lint_timeline.py" in r.stdout, r.stdout[-300:])

print()
if FAILS:
    print(f"test_gates: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_gates: all PASS")
