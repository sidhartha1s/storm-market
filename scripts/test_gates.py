"""Self-check for the c1-gates fixes: python3 scripts/test_gates.py

Builds throwaway episodes carrying each bug class and a clean twin (style of
test_comp_gates.py). Every assertion here is about NEW behavior; the old-vs-old
comparison quoted in the fixer report was done separately with `git show HEAD:<path>`
before these edits were committed.
"""
import json
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path
import yaml

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
            words_mtime_before_wav=False, unparsed_tween=False, comp_window=2.0, extra=""):
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
{extra}
</section>'''
    (ep / "index.html").write_text(html, encoding="utf-8")
    (ep / "media" / "bg.mp4").write_bytes(BG_MP4_BYTES)
    return ep


with tempfile.TemporaryDirectory() as d:
    ep_clean = make_ep(Path(d) / "clean")
    code, out = run("sweep_episode.py", ep_clean)
    check("sweep_episode: exits 0 on a clean episode", code == 0, f"(exit {code})\n{out[-400:]}")

def ask_check(out):
    return next((l for l in out.splitlines() if "End ask present" in l), "")


_ASK = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text(encoding="utf-8"))["channel"]["end_ask"]


def ask_ep(d, start_back=20.0, gap=0.0, vol="1", dur_off=0.0, flip=False, mount=True):
    """A 60.5 s ep- episode with the config end-ask clips staged and mounted from total - start_back."""
    ep = make_ep(Path(d) / "ep-ask-test", nx_dur=60.0, nx_wav_secs=60.0)
    if not mount:
        return ep
    (ep / "media" / "end-ask").mkdir()
    t, vids = 60.5 - start_back, ""
    for i, f in enumerate(_ASK["files"]):
        src = Path(__file__).resolve().parent.parent / f["file"]
        data = bytearray(src.read_bytes())
        if flip and i == 1:
            data[-1] ^= 1
        (ep / "media" / "end-ask" / src.name).write_bytes(bytes(data))
        vids += (f'<video id="ins-ask-{i}" src="media/end-ask/{src.name}" data-start="{t:.3f}" data-duration="{f["duration"] + dur_off}" '
                 f'data-track-index="2" data-volume="{vol}" data-srt-label="ask"></video>\n')
        t += f["duration"] + gap
    html = (ep / "index.html").read_text(encoding="utf-8")
    (ep / "index.html").write_text(html.replace("</section>", vids + "</section>"), encoding="utf-8")
    return ep


for label, kw, want in [
    ("an ep- episode without the end ask FAILs it", dict(mount=False), "FAIL"),
    ("the end ask staged from config, back to back in the last 30 s, PASSes", {}, "PASS"),
    ("an end ask starting 40 s before the end FAILs (last_s)", dict(start_back=40.0), "FAIL"),
    ("a 1 s gap between the two clips FAILs (back to back)", dict(gap=1.0), "FAIL"),
    ("a staged clip one byte off the asset FAILs (md5)", dict(flip=True), "FAIL"),
    ('data-volume="0.5" on the clips FAILs', dict(vol="0.5"), "FAIL"),
    ("a data-duration 0.2 s off config FAILs", dict(dur_off=0.2), "FAIL"),
    ("an end ask that runs past the episode end FAILs", dict(start_back=10.0), "FAIL"),
]:
    with tempfile.TemporaryDirectory() as d:
        code, out = run("sweep_episode.py", ask_ep(d, **kw))
        check(f"sweep_episode: {label}", ask_check(out).startswith(want), ask_check(out) or out[-400:])

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

# audio_levels.py — a narration wav that ends in a burst after silence FAILs; a clean ending passes
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    (ep / "audio").mkdir()
    lav = {"clean": "sine=f=220:r=24000:d=2.0,afade=t=out:st=1.6:d=0.3,apad=pad_dur=0.4",
           "burst": "sine=f=220:r=24000:d=2.0[s];anullsrc=r=24000:cl=mono:d=0.3[q];"
                    "anoisesrc=r=24000:a=0.6:d=0.08[n];[s][q][n]concat=n=3:v=0:a=1"}
    for name, graph in lav.items():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-filter_complex", graph, "-ac", "1",
                        str(ep / "audio" / f"{name}.wav")], check=True)
    (ep / "index.html").write_text(
        '<audio id="nx-a1-s1" src="audio/clean.wav" data-start="0" data-duration="2.4" data-volume="1"></audio>\n'
        '<audio id="nx-a1-s2" src="audio/burst.wav" data-start="3" data-duration="2.38" data-volume="1"></audio>\n',
        encoding="utf-8")
    code, out = run("audio_levels.py", ep)
    check("audio_levels: a narration wav ending in a burst after silence FAILs",
          code == 1 and "nx-a1-s2: ends in a" in out, out)
    check("audio_levels: a narration wav that fades to silence is not flagged as a burst",
          "nx-a1-s1: ends in a" not in out, out)

# G7: an audible <audio> with no id FAILs as unclassified (it was skipped). G9: an nx-ins element is an insert
# (2.5 dB rule), not narration (3 dB rule, joins the median).
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    (ep / "audio").mkdir()
    for name, vol in (("nx", 0.1), ("ins", 0.138), ("loud", 1.0)):  # 0.138 = 0.1 + 2.8 dB
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"sine=f=220:r=24000:d=2.0,volume={vol}",
                        "-ac", "1", str(ep / "audio" / f"{name}.wav")], check=True)
    nx = "".join(f'<audio id="nx-a1-s{i}" src="audio/nx.wav" data-start="{3 * i}" data-duration="2"></audio>\n' for i in range(3))
    (ep / "index.html").write_text(nx + '<audio src="audio/loud.wav" data-start="10" data-duration="2" data-volume="1"></audio>\n',
                                   encoding="utf-8")
    code, out = run("audio_levels.py", ep)
    check("G7 audio_levels: an audible <audio> with no id FAILs as unclassified", code == 1 and "unclassified" in out, out)
    (ep / "index.html").write_text(nx + '<audio id="nx-ins-911" src="audio/ins.wav" data-start="10" data-duration="2"></audio>\n',
                                   encoding="utf-8")
    code, out = run("audio_levels.py", ep)
    check("G9 audio_levels: an nx-ins element 2.8 dB off narration FAILs as an insert", code == 1 and "nx-ins-911: insert" in out, out)

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

# narration a1 covers 0-2 s. Every passing case would FAIL if the voice were ignored (Joplin pip-w16: 12.8 s of still face)
for label, pip_start, pip_dur, nx2_start, want in (
    ("a circle 3.5s past the last line passes", 0, 5.5, None, False),
    ("a circle 6.0s past the last line FAILs", 0, 8.0, None, True),
    ("a circle starting mid-line, 3.5s past it, passes", 1.0, 4.5, None, False),
    ("a 5.0s silence between two lines under one circle FAILs", 0, 9.0, 7.0, True),
):
    with tempfile.TemporaryDirectory() as d:
        v = f'<video class="pip" id="pip-w01" src="media/pip.mp4" data-start="{pip_start}" data-duration="{pip_dur}" data-track-index="7" muted></video>'
        ep = make_lint_ep(Path(d), extra_video=v, nx2_dur=None if nx2_start is None else 2.0, nx2_start=nx2_start)
        (ep / "media" / "pip.mp4").write_bytes(b"0")
        code, out = run("lint_timeline.py", ep)
        check(f"lint_timeline: {label}", ("presenter circle on with no voice" in out) == want, out)

# outside voices (owner 20 Oct 26, Joplin radio): a radio insert at 3-5 s needs a caption host over its whole window
RADIO = '<audio id="{}" src="media/r.wav" data-start="3" data-duration="2" data-volume="1"{}></audio>'
CAP = '<div id="host-cap" data-composition-id="g-cap" data-start="{}" data-duration="{}" data-caption-for="ins-radio"></div>'
for slug, label, extra, want in (
    ("ep-cap", "an uncaptioned radio insert FAILs", RADIO.format("ins-radio", ""), True),
    ("ep-cap", "an uncaptioned nx-ins insert FAILs (only nx- without ins is narration)", RADIO.format("nx-ins1", ""), True),
    ("ep-cap", "a caption host over the whole radio window passes", RADIO.format("ins-radio", "") + CAP.format(3, 2), False),
    ("ep-cap", "a caption that ends 1 s before the radio does FAILs (sound outlasting its picture)",
     RADIO.format("ins-radio", "") + CAP.format(3, 1), True),
    ("ep-cap", "a commented-out caption host does not count",
     RADIO.format("ins-radio", "") + "<!--" + CAP.format(3, 2) + "-->", True),
    ("ep-cap", 'data-caption-ok="reason" on a wordless sound passes',
     RADIO.format("ins-radio", ' data-caption-ok="siren, no words"'), False),
    ("ms-cap", "the caption rule stays off for an ms- mini", RADIO.format("ins-radio", ""), False),
    ("ep1-joplin", "the caption rule stays off for a shipped episode (config exempt list)", RADIO.format("ins-radio", ""), False),
    ("ep-cap", "an uncaptioned radio with no data-volume FAILs (hyperframes plays it at 1.0)",
     '<audio id="ins-radio" src="media/r.wav" data-start="3" data-duration="2"></audio>', True),
    ("ep-cap", "a studio-saved tag (data-hf-id before id) still matches its caption",
     RADIO.format("ins-radio", "").replace("<audio ", '<audio data-hf-id="hf-a1" ') + CAP.format(3, 2), False),
    ("ep-cap", "studio-saved narration (data-hf-id before id) is not an outside voice",
     RADIO.format("nx-a9", "").replace("<audio ", '<audio data-hf-id="hf-a2" '), False),
    ("ep-cap", "an uncaptioned unmuted video FAILs",
     '<video id="v-news" src="media/r.wav" data-start="3" data-duration="2" data-track-index="2"></video>', True),
    ("ep-cap", "a muted video is not a voice",
     '<video id="v-news" src="media/r.wav" data-start="3" data-duration="2" data-track-index="2" muted></video>', False),
    ("ep-cap", "Paul's own clip is not an outside voice", RADIO.format("ins-paul-1", ""), False),
):
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / slug).mkdir()
        ep = make_lint_ep(Path(d) / slug, extra_video=extra)
        write_wav(ep / "media" / "r.wav", 2.0)
        code, out = run("lint_timeline.py", ep)
        check(f"lint_timeline: {label}", ("outside voice without a caption" in out) == want, out)

# dead air (owner 21 Oct 26, Joplin): a declared hold sanctions a pause of at most 4 s with nothing but a bed playing.
# The radio carries data-caption-ok: a wordless outside sound still carries a hold (the same outside_voice test as captions)
HOLD = '<section class="clip hold" id="hold-1" data-start="2" data-duration="{}" data-track-index="8"></section>'
RAD = '<audio id="ins-radio" src="media/r.wav" data-start="{}" data-duration="2" data-volume="1" data-caption-ok="test"></audio>'
for slug, label, nx2, extra, want in (
    ("ep-air", "a 3 s hold passes", 5.0, HOLD.format(3), False),
    ("ep-air", "a 7 s hold with nothing in it FAILs", 9.0, HOLD.format(7), True),
    ("ep-air", "a 7 s hold carried by a radio in its middle passes (2.5 s quiet either side)", 9.0, HOLD.format(7) + RAD.format(4.5), False),
    ("ep-air", "a radio at the start of a 9 s hold leaves 5 s of dead air after it and FAILs", 11.0, HOLD.format(9) + RAD.format(2), True),
    ("ep-air", "a muted clip does not carry a hold", 9.0, HOLD.format(7) + RAD.format(4.5).replace("<audio", "<video").replace("></audio>", " muted></video>"), True),
    ("ep-air", "a bed does not carry a hold", 9.0, HOLD.format(7) + RAD.format(4.5).replace("<audio", "<audio data-bed"), True),
    ("ep-air", "a commented-out radio does not carry a hold", 9.0, HOLD.format(7) + "<!--" + RAD.format(4.5) + "-->", True),
    ("ep1-joplin", "a shipped episode is exempt", 9.0, HOLD.format(7), False),
):
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / slug).mkdir()
        ep = make_lint_ep(Path(d) / slug, extra_video=extra, nx2_dur=2.0, nx2_start=nx2)
        write_wav(ep / "media" / "r.wav", 2.0)
        code, out = run("lint_timeline.py", ep)
        check(f"lint_timeline: {label}", ("dead air" in out) == want and "narration gap" not in out, out)

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
    names = ["render_preflight.py", "paul_start_frame.py", "sweep_episode.py", "lint_timeline.py", "narration_picture_check.py",
             "flag_words.py", "hook_shape.py", "homograph_scan.py", "beat_density.py", "media_budget.py", "audio_levels.py"]
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
          ran == ["render_preflight.py", "paul_start_frame.py", "sweep_episode.py", "lint_timeline.py"], f"ran={ran}\n{r.stdout}{r.stderr}")
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

# sweep_episode.py — a CTA made from another voice reference than the narrator's FAILs.
# sweep reads config.yaml next to its scripts/ dir, so run a copy beside a config with a wrong CTA md5.
with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    (root / "scripts").mkdir()
    for f in S.glob("*.py"):
        (root / "scripts" / f.name).write_bytes(f.read_bytes())
    cfg = (S.parent / "config.yaml").read_text(encoding="utf-8")
    real = _re.search(r"voice_ref_md5: ([0-9a-f]{32})", cfg).group(1)
    cta_line = _re.search(r"\n    voice_ref_md5: [0-9a-f]{32}", cfg)
    check("config: channel.cta carries voice_ref_md5", cta_line is not None, "no CTA voice_ref_md5 line")
    if cta_line:
        bad = cfg[:cta_line.start()] + "\n    voice_ref_md5: " + "0" * 32 + cfg[cta_line.end():]
        (root / "config.yaml").write_text(bad, encoding="utf-8")
        ep = S.parent / "episodes" / "ep-nepal-floods-2026"   # a tracked episode, so sweep reaches its CTA block
        r = subprocess.run([sys.executable, str(root / "scripts" / "sweep_episode.py"), str(ep)],
                           capture_output=True, text=True)
        check("sweep_episode: a CTA voiced from another reference FAILs (voice_ref_md5 mismatch)",
              f"!= external.voice_ref_md5 {real}" in r.stdout + r.stderr, (r.stdout + r.stderr)[-600:])

# ===================================================================================
# 9b. sweep_episode.py — the last-act close carries the library brand lockup (outro-brand.html).
# Owner order 29 Oct 26: batch A hand-built three different closes. Shipped closes PASS; a title
# without the amber WARNING lockup FAILs; an episode with no comp ending at the end FAILs;
# non-`ep-` episodes are not checked.
# ===================================================================================
CLOSE_LABEL = "close card carries the brand lockup"
FX = S / "fixtures" / "close_standard"


def close_line(out):
    return next((l for l in out.splitlines() if CLOSE_LABEL in l), "")


def close_ep(root, slug, comp_html, start=0.5, dur=2.0, track=2):
    # make_ep's episode is 2.5 s long; the default host (0.5 + 2.0) ends exactly at that end
    host = (f'<div id="host-close" data-composition-id="g-close" data-composition-src="compositions/g-close.html" '
            f'data-start="{start}" data-duration="{dur}" data-track-index="{track}"></div>')
    ep = make_ep(Path(root) / slug, extra=host)
    (ep / "compositions" / "g-close.html").write_text(comp_html, encoding="utf-8")
    return ep


# every shipped ep- episode: the exempt two SKIP, every other close PASSes (review 3 Nov 26: E02 and E05 failed unseen)
for slug, want in (("ep-palm-sunday-1965", "SKIP"), ("ep-camille-1969", "SKIP"), ("ep-joplin-2011", "PASS"),
                   ("ep-moore-1999", "PASS"), ("ep-mayfield-2021", "PASS"), ("ep-buffalo-2022", "PASS"),
                   ("ep-appalachian-1950", "PASS"), ("ep-galveston-1900", "PASS")):
    code, out = run("sweep_episode.py", S.parent / "episodes" / slug)
    check(f"sweep_episode close card: shipped {slug} {want}s", close_line(out).startswith(want), close_line(out) or out[-400:])

for slug in ("ep-1974-super-outbreak", "ep-enderlin-2025", "ep-nepal-floods-2026"):
    with tempfile.TemporaryDirectory() as d:
        comp = (S.parent / "episodes" / slug / "compositions" / "g-outro.html").read_text(encoding="utf-8")
        code, out = run("sweep_episode.py", close_ep(d, "ep-close-shipped", comp))
        check(f"sweep_episode close card: shipped {slug} g-outro PASSes", close_line(out).startswith("PASS"), close_line(out) or out[-400:])

for fx, want in (("galveston-g-a6-12-close.html", "FAIL"), ("appalachian-g-a5-9-title.html", "FAIL"),
                 # Buffalo's as-built close (548ae1db) is the Enderlin lockup adapted (cl- classes), so it PASSes
                 ("buffalo-g-a5-10-close.html", "PASS")):
    with tempfile.TemporaryDirectory() as d:
        code, out = run("sweep_episode.py", close_ep(d, "ep-close-fx", (FX / fx).read_text(encoding="utf-8")))
        check(f"sweep_episode close card: batch-A {fx} {want}", close_line(out).startswith(want) and (want == "PASS" or "lacks the lockup" in out), close_line(out) or out[-400:])

with tempfile.TemporaryDirectory() as d:
    comp = (S.parent / "episodes" / "ep-enderlin-2025" / "compositions" / "g-outro.html").read_text(encoding="utf-8")
    # track filter pinned both ways: Appalachian's real close sits on track 3; track 4 is no close
    code, out = run("sweep_episode.py", close_ep(d, "ep-close-t3", comp, track=3))
    check("sweep_episode close card: a lockup close on track 3 PASSes", close_line(out).startswith("PASS"), close_line(out) or out[-400:])
    code, out = run("sweep_episode.py", close_ep(Path(d) / "t4", "ep-close-t4", comp, track=4))
    check("sweep_episode close card: a close on track 4 is no close, FAILs",
          close_line(out).startswith("FAIL") and "ends at the episode end" in out, close_line(out) or out[-400:])

with tempfile.TemporaryDirectory() as d:
    code, out = run("sweep_episode.py", close_ep(d, "ep-close-early", "<template><div>THE WARNING HOUR</div></template>", start=0.2, dur=1.0))
    check("sweep_episode close card: an ep- episode with no comp ending at its end FAILs",
          close_line(out).startswith("FAIL") and "ends at the episode end" in out, close_line(out) or out[-400:])

with tempfile.TemporaryDirectory() as d:
    code, out = run("sweep_episode.py", close_ep(d, "close-not-ep", "<template><div>THE WARNING HOUR</div></template>"))
    check("sweep_episode close card: a non-`ep-` slug is skipped", "SKIP " + CLOSE_LABEL in out, out[-400:])

# ===================================================================================
# 10. verify_render.sh silence classifier: the closing end card (last 4 s) may be silent
# (owner 21 Oct 26: Joplin's final failed on silence 1194.33-1196.54 under its 4 s end card).
# Runs the real heredoc out of verify_render.sh so the test cannot drift from what ships.
# ===================================================================================
def spans_check(sh_src, ep, vid_dur, silence_raw, black_raw="", freeze_raw=""):
    block = next(b.split("\nPYEOF", 1)[0] for b in sh_src.replace("\r\n", "\n").split("<<'PYEOF'\n")[1:]
                 if "silence" in b.split("\nPYEOF", 1)[0])
    r = subprocess.run([sys.executable, "-", str(ep), str(vid_dur), black_raw, silence_raw, freeze_raw],
                       input=block, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


_vr = (S / "verify_render.sh").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory() as d:
    (Path(d) / "index.html").write_text(
        '<div id="root" data-duration="1196.522"><div id="host-z1-close" data-start="1192.522" '
        'data-duration="4"></div></div>', encoding="utf-8")
    code, out = spans_check(_vr, d, 1196.522, "silence_start: 1194.33\nsilence_end: 1196.54")
    check("verify_render: silence under the closing end card is OK (Joplin 1194.33-1196.54)", code == 0, out)
    code, out = spans_check(_vr, d, 1196.522, "silence_start: 1184.0\nsilence_end: 1186.5")
    check("verify_render: a 2.5 s silence ending 10 s before the end still FAILs", code == 1 and "1184.00s" in out, out)
    code, out = spans_check(_vr, d, 1196.522, "", black_raw="black_start: 1194.0\nblack_end: 1196.5")
    check("verify_render: black over the end card still FAILs (silence-only allowance)", code == 1, out)

# ===================================================================================
# 11. build_srt.py --check: same input validation as a build, writes nothing, names every gap;
# run_gates.py runs it right after lint_timeline.py so a gap fails before render, not at master.
# ===================================================================================
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    (ep / "audio").mkdir()
    (ep / "index.html").write_text(
        '<audio id="nx-a1" src="audio/a1-v2.wav" data-start="0.0"></audio>\n'
        '<audio id="nx-ins1" src="audio/radio.wav" data-start="5" data-duration="3" data-srt-label="[radio]"></audio>\n',
        encoding="utf-8")
    (ep / "audio" / "a1-v2.words.json").write_text('[{"word": "Hello", "start": 0.1, "end": 0.5}]', encoding="utf-8")
    (ep / "audio" / "a1-v2.txt").write_text("Hello", encoding="utf-8")
    code, out = run("build_srt.py", ep, "--check")
    check("build_srt --check: complete inputs pass and write no SRT", code == 0 and not (ep / "renders").exists(), out)
    (ep / "audio" / "a1-v2.txt").rename(ep / "audio" / "a1-v2.txt.off")
    html = (ep / "index.html").read_text(encoding="utf-8")
    (ep / "index.html").write_text(html.replace(' data-srt-label="[radio]"', ""), encoding="utf-8")
    code, out = run("build_srt.py", ep, "--check")
    check("build_srt --check: names both the missing -v2.txt and the unlabeled insert",
          code == 1 and "a1-v2.txt" in out and "no data-srt-label" in out, out)

# G1: narration tags in any attribute order, data-media-start honoured, words past a cut-by window dropped,
# and --check FAILs a narration tag that yields no cue (it used to pass on any cue at all).
def srt_ep(d, tags, words):
    ep = Path(d)
    (ep / "audio").mkdir()
    (ep / "renders").mkdir()
    (ep / "index.html").write_text("\n".join(tags), encoding="utf-8")
    for stem, ws in words.items():
        (ep / "audio" / f"{stem}.words.json").write_text(json.dumps([{"word": w, "start": s, "end": s + 0.3} for w, s in ws]), encoding="utf-8")
        (ep / "audio" / f"{stem}.txt").write_text(" ".join(w for w, _ in ws), encoding="utf-8")
    return ep


_srt_tags = ['<audio id="nx-a1" src="audio/a1.wav" data-start="0" data-duration="1"></audio>',
             '<audio id="nx-a2" data-cut-by="ins-paul-1" src="audio/a2.wav" data-start="10" data-duration="1"></audio>',
             '<audio data-start="20" data-duration="2" data-media-start="2" src="audio/a3.wav" id="nx-a3"></audio>']
_srt_words = {"a1": [("First", 0.1)], "a2": [("Second", 0.1), ("Paulsays", 1.5)], "a3": [("Unplayed", 0.5), ("Third", 2.3)]}
with tempfile.TemporaryDirectory() as d:
    ep = srt_ep(d, _srt_tags, _srt_words)
    code, out = run("build_srt.py", ep, "t")
    srt = (ep / "renders" / "t.srt").read_text(encoding="utf-8") if (ep / "renders" / "t.srt").exists() else out
    check("G1 build_srt: a data-cut-by mount (cut-by before src) is captioned", "00:00:10,100 --> " in srt and "Second" in srt, srt)
    check("G1 build_srt: words after a cut-by window are left to Paul's clip", "Paulsays" not in srt, srt)
    check("G1 build_srt: data-media-start offsets the words and drops the unplayed head",
          "00:00:20,300 --> " in srt and "Third" in srt and "Unplayed" not in srt, srt)
with tempfile.TemporaryDirectory() as d:
    ep = srt_ep(d, _srt_tags + ['<audio id="nx-a4" src="audio/a4.wav" data-start="30" data-duration="1"></audio>'],
                dict(_srt_words, a4=[("Late", 4.0)]))
    code, out = run("build_srt.py", ep, "--check")
    check("G1 build_srt --check: a narration tag that yields no cue FAILs", code == 1 and "nx-a4" in out, out)

_rg = (S / "run_gates.py").read_text(encoding="utf-8")
check("run_gates: build_srt.py --check runs right after lint_timeline.py",
      _rg.index('"lint_timeline.py",') < _rg.index('"build_srt.py --check"') < _rg.index('"narration_picture_check.py"'))

# ===================================================================================
# 12. sweep_episode.py — cut-by mounts, designed src-less sections, .webm cuts (30 Oct 26 finals)
# ===================================================================================
def cutby_ep(d, cut_by=True, paul_at=1.0):
    # narration wav is 2.0 s, mounted for 1.0 s and cut where Paul's clip (ins-paul-1) takes the line over
    ep = make_ep(Path(d), nx_dur=1.0, nx_wav_secs=2.0)
    h = (ep / "index.html").read_text(encoding="utf-8")
    cb = ' data-cut-by="ins-paul-1"' if cut_by else ""
    h = h.replace('data-start="0" data-duration="1.0"></audio>', f'data-start="0" data-duration="1.0"{cb}></audio>')
    h = h.replace("</section>", f'<video id="ins-paul-1" src="media/bg.mp4" data-start="{paul_at}" data-duration="1" '
                                'data-track-index="2" data-volume="1"></video>\n</section>')
    (ep / "index.html").write_text(h, encoding="utf-8")
    return ep

with tempfile.TemporaryDirectory() as d:
    code, out = run("sweep_episode.py", cutby_ep(d))
    check("sweep_episode: a data-cut-by narration mount ending where Paul's clip starts is fresh",
          "FAIL narration freshness" not in out, out[-600:])
with tempfile.TemporaryDirectory() as d:
    code, out = run("sweep_episode.py", cutby_ep(d, cut_by=False))
    check("sweep_episode: the same short mount without data-cut-by is stale", "FAIL narration freshness" in out, out[-600:])
with tempfile.TemporaryDirectory() as d:
    code, out = run("sweep_episode.py", cutby_ep(d, paul_at=1.5))
    check("sweep_episode: a data-cut-by whose clip starts 0.5 s after the mount ends is stale",
          "FAIL narration freshness" in out, out[-600:])

with tempfile.TemporaryDirectory() as d:
    # a designed <section class="clip ground"> with no src of its own, 8 s long, followed by a .webm film cut of 8 s:
    # neither is a still, the section is not a missing file, and the section is not a duplicate of the film after it
    ep = make_ep(Path(d), nx_dur=1.0, nx_wav_secs=1.0, comp_window=17.0)
    h = (ep / "index.html").read_text(encoding="utf-8")
    h = h.replace("</section>", '<section id="c-a5-ground" class="clip ground" data-start="0" data-duration="8" '
                                'data-track-index="2"><div class="sky"></div></section>\n'
                                '<video src="media/film.webm" data-start="8" data-duration="8" data-track-index="2" muted></video>\n'
                                '<video src="media/film.webm" data-start="16" data-duration="1" data-track-index="2" muted></video>\n</section>')
    (ep / "index.html").write_text(h, encoding="utf-8")
    (ep / "media" / "film.webm").write_bytes(BG_MP4_BYTES)
    code, out = run("sweep_episode.py", ep)
    check("sweep_episode: a src-less designed section is not a still, a missing file or a duplicate of the next cut",
          "[c-a5-ground]" not in out.split("FAIL media files exist")[-1][:200] and "FAIL no still over 6s" not in out
          and "FAIL adjacent duplicate cuts" not in out, out[-800:])

# lint_timeline.py — the same cut-by and media-start rules as sweep (scripts/cut_by.py is the one owner)
def lint_nx_ep(d, dur, extra_attrs="", paul_at=None):
    ep = make_lint_ep(Path(d), nx2_dur=2.0, nx2_start=7.0)
    # the fixture's first narration is nx-a1 on media/a1.wav, 2.0 s; its mount becomes `dur` (+ extra attrs)
    h = (ep / "index.html").read_text(encoding="utf-8")
    old_tag = '<audio id="nx-a1" src="media/a1.wav" data-start="0" data-duration="2"></audio>'
    assert old_tag in h
    h = h.replace(old_tag, '<audio id="nx-a1" src="media/a1.wav" data-start="0" data-duration="%s"%s></audio>' % (dur, extra_attrs))
    if paul_at is not None:
        h = h.replace("</section>", f'<video id="ins-paul-9" src="media/paul.mp4" data-start="{paul_at}" data-duration="1" '
                                    'data-track-index="2" data-volume="1" data-has-audio="true" data-srt-label="x"></video>\n</section>')
        (ep / "media" / "paul.mp4").write_bytes(b"0")
    (ep / "index.html").write_text(h, encoding="utf-8")
    return ep

with tempfile.TemporaryDirectory() as d:
    code, out = run("lint_timeline.py", lint_nx_ep(d, 1.0))
    check("lint_timeline: a narration window shorter than its wav FAILs", "narration window shorter" in out, out[-500:])
with tempfile.TemporaryDirectory() as d:
    code, out = run("lint_timeline.py", lint_nx_ep(d, 1.0, ' data-media-start="1.0"'))
    check("lint_timeline: media-start + duration reaching the wav end is not a short window", "narration window shorter" not in out, out[-500:])
with tempfile.TemporaryDirectory() as d:
    code, out = run("lint_timeline.py", lint_nx_ep(d, 1.0, ' data-cut-by="ins-paul-9"', paul_at=1.0))
    check("lint_timeline: a data-cut-by mount ending where Paul's clip starts is not a short window", "narration window shorter" not in out, out[-500:])
with tempfile.TemporaryDirectory() as d:
    code, out = run("lint_timeline.py", lint_nx_ep(d, 1.0, ' data-cut-by="ins-paul-9"', paul_at=1.5))
    check("lint_timeline: a data-cut-by whose clip starts 0.5 s late still FAILs", "narration window shorter" in out, out[-500:])

# G5: a voiced Paul clip or a hold written with data-duration before data-start still counts (attribute order is free)
def lint_order_ep(d, middle):
    ep = Path(d)
    (ep / "audio").mkdir(parents=True)
    for n in ("a1-s1", "a1-s2"):
        write_wav(ep / "audio" / f"{n}.wav", 4.0)
    (ep / "p.mp4").write_bytes(b"0")
    (ep / "index.html").write_text(
        '<div data-composition-id="root" data-duration="12">\n'
        '<section class="clip" id="bg" data-start="0" data-duration="12" data-track-index="1"></section>\n'
        '<audio id="nx-a1-s1" src="audio/a1-s1.wav" data-start="0" data-duration="4"></audio>\n'
        f'{middle}\n'
        '<audio id="nx-a1-s2" src="audio/a1-s2.wav" data-start="8" data-duration="4"></audio>\n</div>', encoding="utf-8")
    return ep


for label, middle in (
        ("a voiced Paul clip", '<video id="ins-paul-1" src="p.mp4" data-duration="4" data-start="4" data-track-index="5" '
                               'data-volume="1" data-has-audio="true"></video>'),
        ("a declared hold", '<section class="clip hold" id="h1" data-duration="4" data-start="4" data-track-index="2"></section>')):
    with tempfile.TemporaryDirectory() as d:
        code, out = run("lint_timeline.py", lint_order_ep(d, middle))
        check(f"G5 lint_timeline: {label} with data-duration before data-start fills the pause", "narration gap" not in out, out[-400:])

# G9: one narration/insert classification (scripts/timeline.py), used by sweep, build_srt, lint, npc, audio_levels
import timeline  # noqa: E402
check("G9 timeline: nx-a1-s1 is narration, nx-ins-911 / ins-paul-1 are inserts, sx-bed is neither",
      [(timeline.is_narration(i), timeline.is_insert(i)) for i in ("nx-a1-s1", "nx-ins-911", "ins-paul-1", "sx-bed")]
      == [(True, False), (False, True), (False, True), (False, False)])

# G13: a class or attribute that merely contains "muted" does not mute a b-roll clip
with tempfile.TemporaryDirectory() as d:
    v = '<video class="not-muted-really" data-muted-ok="x" src="media/broll.mp4" data-start="0" data-duration="2" data-track-index="1"></video>'
    ep = make_lint_ep(Path(d), extra_video=v)
    (ep / "media" / "broll.mp4").write_bytes(b"0")
    code, out = run("lint_timeline.py", ep)
    check("G13 lint_timeline: 'muted' inside a class name is not the muted attribute", "unmuted b-roll" in out, out[-400:])

# G10: one coverage rule (timeline.picture_holes): a 0.04 s hole between two picture windows gets one verdict from
# every gate that reports coverage (sweep used 0.05 s and passed it while lint failed it)
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    (ep / "index.html").write_text(
        '<div data-composition-id="root" data-duration="10">\n'
        '<section class="clip" id="a" data-start="0" data-duration="5" data-track-index="1"></section>\n'
        '<section class="clip" id="b" data-start="5.04" data-duration="4.96" data-track-index="1"></section>\n</div>', encoding="utf-8")
    verdicts = {"sweep_episode.py": "FAIL picture coverage" in run("sweep_episode.py", ep)[1],
                "lint_timeline.py": "picture gap" in run("lint_timeline.py", ep)[1],
                "clip_report.py": "uncovered picture gaps (tracks [1, 2]): 1" in run("clip_report.py", ep)[1]}
    check("G10: sweep, lint and clip_report all report a 0.04 s picture hole", all(verdicts.values()), str(verdicts))

# ===================================================================================
# R2: a documentary named e10-<topic> (CLAUDE.md step 7) is checked exactly like an ep- one (scripts/episode.py)
# ===================================================================================
def _verdicts(out, slug):
    """Each sweep check's verdict word and name, slug and counts stripped."""
    return [re.sub(r":\s*\d+$", "", l.replace(slug, "<slug>")) for l in out.splitlines()
            if l.startswith(("PASS ", "FAIL ", "SKIP "))]


_radio = '<audio id="ins-radio" src="audio/a1-s1.wav" data-start="0.2" data-duration="0.5"></audio>'
with tempfile.TemporaryDirectory() as d:
    res = {}
    for slug in ("ep-foo", "e10-foo", "ep4-foo"):
        ep = make_ep(Path(d) / slug, extra=_radio)
        res[slug] = (_verdicts(run("sweep_episode.py", ep)[1], slug), run("lint_timeline.py", ep)[1])
    check("R2 sweep: an e10- episode gets every check an ep- episode gets (CTA, end ask, close card)",
          res["e10-foo"][0] == res["ep-foo"][0] and not any(l.startswith("SKIP") for l in res["e10-foo"][0]),
          f"\n ep-:  {res['ep-foo'][0]}\n e10-: {res['e10-foo'][0]}")
    check("R2 sweep: a legacy ep4- episode still skips only the close card",
          [l for l in res["ep4-foo"][0] if l.startswith("SKIP")] == ["SKIP close card carries the brand lockup — <slug> is not a current documentary"],
          str(res["ep4-foo"][0]))
    check("R2 lint: an e10- episode gets the outside-voice caption check like an ep- one",
          all("outside voice without a caption" in res[s][1] for s in ("ep-foo", "e10-foo", "ep4-foo")),
          res["e10-foo"][1][-400:])

import render_preflight  # noqa: E402
_bare = '<section data-duration="10"><audio id="nx-a1" src="a.wav" data-start="0" data-duration="5"></audio></section>'
check("R2 layers: an e10- documentary must carry the layers an ep- one must",
      render_preflight.missing_layers("e10-foo", _bare) == render_preflight.missing_layers("ep-foo", _bare) != [])
check("R2 layers: legacy ep4- and ms- slugs keep skipping the layer gate",
      render_preflight.missing_layers("ep4-foo", _bare) == render_preflight.missing_layers("ms-foo", _bare) == [])

print()
if FAILS:
    print(f"test_gates: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_gates: all PASS")
