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
check("fold: left-to-right, not additions-before-subtractions (10 - 2 + 3 -> 11.0, not 5.0)",
      "11.0" in fold('tl.to(a,{}, 10 - 2 + 3);'))
check("fold: chained sub/add on a const (DUR - 1.2 + 0.3 -> 13.55, not 12.95)",
      "13.55" in fold('const DUR = 14.45; tl.to(a,{}, DUR - 1.2 + 0.3);'))
check("fold: no spaces (5-3+1 -> 3.0)",
      "3.0" in fold('tl.to(a,{}, 5-3+1);'))
check("fold: parens group before the outer multiply ((2 + 3) * 2 -> 10.0)",
      "10.0" in fold('tl.to(a,{}, (2 + 3) * 2);'))
check("fold: division then subtraction (8 / 2 - 1 -> 3.0)",
      "3.0" in fold('tl.to(a,{}, 8 / 2 - 1);'))
check("fold: a bare date-like sequence stays text (2026-09-21)",
      fold('// updated 2026-09-21 owner note') == '// updated 2026-09-21 owner note')

# fix-fold-ast (24 Sep 26): call parens were folded before the identifier guard ran, and a span
# bordering an unresolved identifier through an operator got evaluated alone, eating the operator
# that tied it to the identifier. All six fail on PR head 3e99a621 (confirmed via git show).
check("fold: nested paren arg to a call stays a call, inner math still folds (Math.floor((30.25) / 1) - 1)",
      fold('Math.floor((30.25) / 1) - 1') == 'Math.floor(30.25) - 1')
check("fold: call parens are not treated as grouping parens (Math.round(10.4) - 1)",
      fold('Math.round(10.4) - 1') == 'Math.round(10.4) - 1')
check("fold: single-arg call left untouched (f(2) + 1)",
      fold('f(2) + 1') == 'f(2) + 1')
check("fold: span bordering an identifier via '-' stays whole, not folded piecemeal (t0 - 0.5 - 0.2)",
      fold('t0 - 0.5 - 0.2') == 't0 - 0.5 - 0.2')
check("fold: operator tying a span to an identifier is not eaten (t0 - 2 + 3)",
      fold('t0 - 2 + 3') == 't0 - 2 + 3')
check("fold: span bordering an identifier via '*' stays whole (x * 2 + 3)",
      fold('x * 2 + 3') == 'x * 2 + 3')
check("fold: '%' borders a span like '*' ('i % 2 * 0.5' and '7 % 3 + 1' stay whole)",
      fold('delay: i % 2 * 0.5') == 'delay: i % 2 * 0.5' and fold('7 % 3 + 1') == '7 % 3 + 1')

# ===================================================================================
# 2 + 5. sweep_episode.py — exit code, freshness gate, check-7 coverage
# ===================================================================================
GSAP = (Path(__file__).resolve().parent.parent / "library/gallery/gsap.min.js").read_text(encoding="utf-8")

# a real tiny clip (moving test pattern, not a 1-byte stub) — the luma/motion probes in
# sweep_episode.py's "media probes succeeded" check correctly FAIL an undecodable file, and a
# fake fixture file was tripping that gate for reasons unrelated to what these tests check.
_BG_MP4 = Path(tempfile.gettempdir()) / "_test_gates_bg.mp4"
if not _BG_MP4.exists():
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc=size=64x64:duration=12:rate=10",
                    "-pix_fmt", "yuv420p", str(_BG_MP4)], check=True)
BG_MP4_BYTES = _BG_MP4.read_bytes()


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
    (ep / "media" / "bg.mp4").write_bytes(BG_MP4_BYTES)
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
    # a loop-driven position (i * 0.2) can never fold to a literal — unparseable is not the
    # same claim as defective (review 24 Sep 26: this hit 3/3 real episodes as a false FAIL,
    # g-scale-hook.html:69,82-83). Coverage must be visible but must NOT fail the sweep alone.
    ep_unparsed = make_ep(Path(d) / "unparsed", unparsed_tween=True)
    code, out = run("sweep_episode.py", ep_unparsed)
    check("sweep_episode: check 7 reports tween coverage honestly, unparsed alone does not FAIL",
          code == 0 and "resolved" in out and "not checked" in out, f"(exit {code})\n{out[-600:]}")

with tempfile.TemporaryDirectory() as d:
    # a loop-driven position PLUS a genuine window overrun among the tweens it could resolve
    # (comp_window=6 vs a 1.1s resolvable timeline -> "holds") must still FAIL, on the real
    # defect, not on the unparsed position.
    ep_real = make_ep(Path(d) / "realoverrun", unparsed_tween=True, comp_window=6.0)
    code, out = run("sweep_episode.py", ep_real)
    check("sweep_episode: a genuine overrun among resolved tweens still FAILs (unparsed doesn't mask it)",
          code == 1 and "holds" in out and "resolved" in out, f"(exit {code})\n{out[-600:]}")

# ===================================================================================
# 3. beat_density.py — exit code on a DEAD (>=4s motionless) composition
# ===================================================================================
def bd_comp(js, dom='<div id="g" style="position:absolute;left:100px;top:100px;width:200px;height:80px;background:#c33"></div>'):
    """A real composition: beat_density reads the built timeline, so the fixture must register one."""
    return ('<template><div id="root" style="position:absolute;inset:0">' + dom + '</div><script>'
            'window.__timelines = window.__timelines || {}; const tl = gsap.timeline({ paused: true });'
            + js + ' window.__timelines["g1"] = tl;</script></template>')


with tempfile.TemporaryDirectory() as d:
    dead_comp = bd_comp('tl.to("#g", {x: 10, duration: 0.1}, 0.1);')
    ep_dead = make_ep(Path(d) / "dead", comp_html=dead_comp, comp_window=6.0)
    code, out = run("beat_density.py", ep_dead)
    check("beat_density: exits 1 on a composition with a >=4s motionless stretch (was always 0)",
          code == 1, f"(exit {code})\n{out[-400:]}")
    idx = ep_dead / "index.html"
    idx.write_text(idx.read_text(encoding="utf-8").replace(
        'data-composition-id="g1" data-start="0" data-duration="6.0"',
        'data-duration="6.0" data-composition-id="g1" data-track-index="3" data-start="0"'), encoding="utf-8")
    code, out = run("beat_density.py", ep_dead)
    check("beat_density: host attribute order does not matter (was a silent skip)",
          code == 1 and "1/1" in out, f"(exit {code})\n{out[-400:]}")
    idx.write_text(idx.read_text(encoding="utf-8").replace('data-duration="6.0" ', ''), encoding="utf-8")
    (ep_dead / "compositions" / "orphan.html").write_text(dead_comp, encoding="utf-8")
    code, out = run("beat_density.py", ep_dead)
    check("beat_density: WARNs on a host without data-duration and on an unmounted comp",
          "host 'g1' has no numeric data-duration" in out and "orphan.html is not mounted" in out,
          f"(exit {code})\n{out[-400:]}")

with tempfile.TemporaryDirectory() as d:
    live_comp = bd_comp('tl.to("#g", {x: 300, duration: 2, ease: "none"}, 0);')
    ep_live = make_ep(Path(d) / "live", comp_html=live_comp)
    code, out = run("beat_density.py", ep_live)
    check("beat_density: exits 0 on a composition with no dead stretch", code == 0, f"(exit {code})\n{out[-400:]}")

# Runtime beats (fix/beat-density-runtime): the regex path could not see an aliased duration, a tween
# made inside a helper, or an onUpdate canvas renderer, and it counted a `tl.to({}, ...)` clock as
# motion. Each fixture runs on the new gate and on the pre-fix gate, pinned to 11ba4c09 (never
# origin/main: after the merge origin/main holds the fix and the old-code half would go red).
OLD_BD = S / "_old_beat_density_tmp.py"   # beside comp_consts.py, which the old gate imports
OLD_BD.write_text(subprocess.run(["git", "show", "11ba4c09:scripts/beat_density.py"], cwd=S.parent,
                                 capture_output=True, text=True, check=True).stdout, encoding="utf-8")
CANVAS = '<canvas id="cv" width="1920" height="1080" style="position:absolute;left:0;top:0"></canvas>'
DRAW = ('const cx = document.getElementById("cv").getContext("2d");'
        'tl.eventCallback("onUpdate", () => { cx.clearRect(0, 0, 1920, 1080); cx.fillRect(200 + tl.time() * 100, 400, 80, 80); });')
try:
    for label, js, dom, want_new, want_old in (
        ("an aliased duration (C.duration, const C = CONFIG) resolves",
         'const CONFIG = { duration: 10 }; const C = CONFIG; tl.to("#g", {x: 300, duration: C.duration, ease: "none"}, 0);',
         None, 0, 1),
        ("tweens made inside a helper function count",
         'function slide(at) { tl.to("#g", {x: "+=60", duration: 3, ease: "none"}, at); }'
         ' for (let i = 0; i < 4; i++) slide(i * 2.5);', None, 0, 1),
        ("an onUpdate + full-frame canvas renderer counts as continuous",
         DRAW + ' const LEN = { s: 10 }; const L = LEN; tl.to({}, {duration: L.s}, 0);', CANVAS, 0, 1),
        ("a literal tl.to({}, {duration: N}, 0) clock alone is not motion (old code passed it)",
         'tl.to({}, {duration: 10}, 0);', None, 1, 0),
    ):
        with tempfile.TemporaryDirectory() as d:
            ep = make_ep(Path(d) / "bd", comp_html=bd_comp(js, dom) if dom else bd_comp(js), comp_window=10.0)
            code, out = run("beat_density.py", ep)
            old, old_out = run(OLD_BD.name, ep)
            check(f"beat_density: {label}", code == want_new and old == want_old,
                  f"(new exit {code}, want {want_new}; old exit {old}, want {want_old})\n{out[-500:]}\n{old_out[-300:]}")
finally:
    OLD_BD.unlink()

# New-only: a plain-object proxy counts where an onUpdate hub turns it into page change (library/
# inhouse/moves), and not at all without one. A 100 px canvas does not earn the renderer span.
PROXY = 'const cam = { x: 0 }; tl.to(cam, {x: 300, duration: 10, ease: "none"}, 0);'
HUB = ' const g = document.getElementById("g"); tl.eventCallback("onUpdate", () => { g.style.transform = "translateX(" + cam.x + "px)"; });'
# The schedule fixtures tween backgroundColor on purpose: the picture diff (rule 3) reads box,
# transform, opacity and text, not colour, so only the tween schedule (rule 1) can pass them. Drop
# the parent offset or use duration() for totalDuration() and the 7 s tail goes DEAD.
SUB = ('const sub = gsap.timeline(); sub.to("#g", {backgroundColor: "#33c", duration: 3, ease: "none"}, 0);'
       ' tl.add(sub, 3.5);')
REPEAT = 'tl.to("#g", {backgroundColor: "#33c", duration: 2, repeat: 3, yoyo: true, ease: "none"}, 1);'
HIDDEN = '<div id="g" style="display:none;position:absolute;left:100px;top:100px;width:200px;height:80px"></div>'
DATASET = ('const root = document.getElementById("root");'
           ' tl.eventCallback("onUpdate", () => { root.dataset.t = tl.time().toFixed(2); }); tl.to({}, {duration: 10}, 0);')
for label, js, dom, want in (
    ("a proxy driven through an onUpdate hub counts", PROXY + HUB, None, 0),
    ("a proxy nothing reads is not motion", PROXY, None, 1),
    ("a 100 px canvas renderer is not continuous motion",
     DRAW + ' tl.to({}, {duration: 10}, 0);', CANVAS.replace('width="1920" height="1080"', 'width="100" height="100"'), 1),
    ("a nested timeline's tl.add offset shifts its tweens' spans", SUB, None, 0),
    ("repeat:3 spans the tween's totalDuration, not one cycle", REPEAT, None, 0),
    ("a long tween on a display:none element is not motion", 'tl.to("#g", {x: 300, duration: 10, ease: "none"}, 0);',
     HIDDEN, 1),
    ("an onUpdate writing root.dataset.t (nothing visible) is not motion", DATASET, None, 1),
):
    with tempfile.TemporaryDirectory() as d:
        ep = make_ep(Path(d) / "bd", comp_html=bd_comp(js, dom) if dom else bd_comp(js), comp_window=10.0)
        code, out = run("beat_density.py", ep)
        check(f"beat_density: {label}", code == want, f"(exit {code}, want {want})\n{out[-500:]}")

# A probe ERROR fails at any window: it used to print as a gap equal to the window, so a 3 s comp
# the probe could not measure passed.
with tempfile.TemporaryDirectory() as d:
    ep = make_ep(Path(d) / "bd", comp_html='<template><div id="root"></div><script>/* registers no timeline */</script></template>',
                 comp_window=3.0)
    code, out = run("beat_density.py", ep)
    check("beat_density: a probe ERROR on a <4 s window fails, labelled ERROR",
          code == 1 and "ERROR no timeline registered" in out and "DEAD" not in out, f"(exit {code})\n{out[-500:]}")

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
    # a still-buggy id read would find "hf-onw2" as the narration's id (doesn't start with
    # nx-), so narr would be empty and the script would exit early with "no nx-* narration
    # elements found" instead of computing a reference from the one real nx- element.
    check("audio_levels: reads the real id past a data-hf-id attribute (no more hf- misread)",
          "median of 1 nx-*" in out and "hf-onw2" not in out, out)
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
    # a 40 s b-roll hold is reported for the editor; the presenter circle held just as long is not a cut and is not
    ep = Path(d)
    (ep / "media").mkdir(); (ep / "compositions").mkdir()
    write_wav(ep / "media" / "a1.wav", 2.0)
    for name in ("broll.mp4", "paul-w01.mp4"):
        (ep / "media" / name).write_bytes(b"0")
    (ep / "index.html").write_text(
        '<section data-duration="300">'
        '<audio id="nx-a1" src="media/a1.wav" data-start="0" data-duration="2"></audio>'
        '<video src="media/broll.mp4" data-start="0" data-duration="40" data-track-index="1" muted></video>'
        '<video id="pip-w01" class="pip" src="media/paul-w01.mp4" data-start="0" data-duration="40" data-track-index="7" muted></video>'
        '</section>', encoding="utf-8")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: the pacing report names a long b-roll hold but never the presenter circle",
          "[pacing report] video media/broll.mp4" in out and "paul-w01.mp4" not in out, out)

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


def paul_clip(start, dur, volume="1"):
    return (f'<video id="ins-paul-1" src="media/paul.mp4" data-start="{start}" data-duration="{dur}" '
            f'data-track-index="1" data-volume="{volume}" data-has-audio="true" data-srt-label="x"></video>')


# These timelines have no picture outside Paul's clip, so lint always ends on its FAIL verdict line:
# "[lint_timeline] FAIL" in out proves it ran to the end instead of crashing before the seam check.
with tempfile.TemporaryDirectory() as d:
    # the same 5s hole as above, filled by Paul speaking on camera (2.2-6.8): his line is voice, not a gap
    ep = make_lint_ep(Path(d), extra_video=paul_clip(2.2, 4.6), nx2_dur=2.0, nx2_start=7.0)
    (ep / "media" / "paul.mp4").write_bytes(b"0")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: Paul's on-camera line between two narration segments is not a narration gap",
          "[lint_timeline] FAIL" in out and "narration gap" not in out, out)

with tempfile.TemporaryDirectory() as d:
    # the same clip with its sound off is not voice: the hole is still a hole
    ep = make_lint_ep(Path(d), extra_video=paul_clip(2.2, 4.6, volume="0"), nx2_dur=2.0, nx2_start=7.0)
    (ep / "media" / "paul.mp4").write_bytes(b"0")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: a silent ins-paul- clip does not hide a narration gap", "narration gap" in out, out)

with tempfile.TemporaryDirectory() as d:
    # Paul's line (2.2-3.8) runs into the CTA at 4.0: the dip-in is measured from his last word, not the narrator's
    ep = make_lint_ep(Path(d), extra_video=paul_clip(2.2, 1.6), nx2_dur=2.0, nx2_start=6.5, cta=True)
    (ep / "media" / "paul.mp4").write_bytes(b"0")
    code, out = run("lint_timeline.py", ep)
    check("lint_timeline: Paul's on-camera line right before the CTA keeps the dip-in inside config",
          "[lint_timeline] FAIL" in out and "dip-in" not in out and "narration gap" not in out, out)

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

# ===================================================================================
# 9. sweep_episode.py's motion-gate _frame() helper: PID-scoped temp paths (no cross-process
# collision) + any raised exception (locked file, timeout) reports loudly via probe_failed
# instead of crashing the whole sweep silently mid-run. Isolated the same way
# test_comp_gates.py isolates _gate_lines: exec the function body out of the real source so
# the test can't drift from what actually ships.
# ===================================================================================
import re as _re
_src = (S / "sweep_episode.py").read_text(encoding="utf-8")
check("sweep_episode: _tmpa/_tmpb are PID-scoped (no shared filename across concurrent runs)",
      "os.getpid()" in _src and '_sweep_ma_{os.getpid()}' in _src, "grep for os.getpid() in _tmpa/_tmpb")

_frame_src = _re.search(r"def _frame\(p, t, out\):.*?\n\n", _src, flags=_re.S).group(0)
_ns = {"subprocess": subprocess, "Path": Path, "probe_failed": []}
exec(_frame_src, _ns)
# a directory where a file path is expected makes Path(out).unlink() raise deterministically
# (confirmed PermissionError on this box) -- simulates the locked-file-under-load scenario
# without needing a real second process racing the same temp path.
with tempfile.TemporaryDirectory() as d:
    bogus_out_dir = Path(d) / "not_a_file"
    bogus_out_dir.mkdir()
    result = _ns["_frame"](Path(d) / "nonexistent-source.mp4", 0.4, str(bogus_out_dir))
    check("sweep_episode: _frame() reports a raised exception via probe_failed instead of crashing",
          result is False and len(_ns["probe_failed"]) == 1 and "frame extract raised" in _ns["probe_failed"][0][1],
          f"result={result} probe_failed={_ns['probe_failed']}")

print()
if FAILS:
    print(f"test_gates: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_gates: all PASS")
