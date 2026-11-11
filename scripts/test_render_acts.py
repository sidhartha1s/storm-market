"""Self-check for render_acts.py: python3 scripts/test_render_acts.py

The seam proof itself (per-act concat vs one render of a 2-act Moore slice) is in the PR body; this pins the logic
that proof depends on: where the seams fall, what each act's staged composition keeps, and that the root timeline
of an act plays from the act's start (run on the repo's own gsap.min.js under node).
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import render_acts as ra  # noqa: E402

FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


COMP = """<html><body>
<div id="root" data-composition-id="ep-x" data-start="0" data-width="1920" data-height="1080" data-duration="20" data-fps="30">
  <audio id="nx-1" src="audio/a.wav" data-start="1" data-duration="5"></audio>
  <video id="v-a1" src="media/a.mp4" data-start="0" data-duration="9.8" muted></video>
  <section class="clip blackout" id="bo-1" data-start="9.8" data-duration="0.4"></section>
  <video id="v-a2" src="media/b.mp4" data-start="10.2" data-duration="9.8" data-media-start="3" muted></video>
  <div id="host-g" data-composition-id="g" data-composition-src="compositions/g.html" data-start="12" data-duration="4"></div>
  <section class="clip still-wrap" id="kb-1" data-start="2" data-duration="3"><img src="media/s.jpg"></section>
</div>
<script>
const tl = gsap.timeline({ paused: true }); window.__timelines["ep-x"] = tl;
</script>
</body></html>
"""

acts, skipped = ra.plan_acts(COMP, 30)
check("the seam is the blackout's middle frame (10.0 s = frame 300)", acts == [(0, 300), (300, 600)] and not skipped)
spanned = COMP.replace('data-start="10.2" data-duration="9.8" data-media-start="3"',
                       'data-start="9.9" data-duration="10.1" data-media-start="3"')
acts2, skipped2 = ra.plan_acts(spanned, 30)
check("a video running through the blackout skips that seam", acts2 == [(0, 600)] and skipped2[0][2] == ["v-a2"])

a2 = ra.slice_html(COMP, 300, 600, 30)
check("act 2: narration over before the act parks, hidden, on the act's first frame",
      re.search(r'id="nx-1"[^>]*data-start="0.0"[^>]*data-duration="0.0333[^>]*style="display: none !important"', a2))
check("act 2: act 1's silent video parks past the act's end, hidden; its own video plays",
      re.search(r'id="v-a1"[^>]*data-start="11.0"[^>]*style="display: none !important" data-act-parked', a2)
      and "display" not in re.search(r'<video id="v-a2"[^>]*>', a2).group(0))
check("act 2: times shifted by the act start", 'id="v-a2" src="media/b.mp4" data-start="0.1999999999999993"' in a2
      and re.search(r'id="host-g"[^>]*data-start="2.0"', a2))
check("act 2: media offset untouched for a clip inside the act", 'data-media-start="3"' in a2)
check("act 2: authored scripts can read the original times", 'data-act-src-start="10.2"' in a2)
check("act 2: a plain element over before the act stays (scripts may count it), parked past the act's end",
      re.search(r'id="kb-1" data-start="11.0"', a2))
check("act 2: the blackout running through the seam starts at 0 with its remaining length",
      re.search(r'id="bo-1" data-start="0.0" data-act-start="0.0" data-act-src-start="9.8" data-duration="0.2000', a2))
check("act 2: root length is the act's frames", re.search(r'id="root"[^>]*data-duration="10.0"', a2))
# PR 223 defects 1 and 2: dropping act 2's sub-composition removed what made hyperframes run its pre-capture sweep
check("act 1 keeps act 2's media and sub-composition on the page, parked and hidden",
      re.search(r'id="host-g"[^>]*data-composition-src="compositions/g.html"[^>]*data-start="12.0"[^>]*'
                r'display: none !important" data-act-parked', a1 := ra.slice_html(COMP, 0, 300, 30))
      and re.search(r'id="v-a2"[^>]*data-act-parked', a1))
try:
    ra.slice_html(spanned, 300, 600, 30)
    check("a slice that would start mid-video refuses", False)
except SystemExit as e:
    check("a slice that would start mid-video refuses", "v-a2" in str(e))

check("frame count follows hyperframes (1117.329 s at 30 fps = 33520)", ra.frame_count(1117.329, 30) == 33520)
check("frame count: a whole-frame duration within 1e-3 rounds", ra.frame_count(32.6, 30) == 978)

render_cmd = (S / "render.cmd").read_text(encoding="utf-8")
fps_defaults = dict(re.findall(r'"%MODE%"=="(draft|full)" \(\s*set QUAL=\w+\s*set _CRF=\d+\s*set _FPS=(\d+)', render_cmd))
check("mode fps agrees with render.cmd", {m: int(f) for m, f in fps_defaults.items()}
      == {"draft": ra.mode_fps("draft"), "full": ra.mode_fps("full")})
check("render.cmd renders RENDER_COMPOSITION, default index.html",
      "render . -c %RENDER_COMPOSITION% " in render_cmd and "set RENDER_COMPOSITION=index.html" in render_cmd)
check("render.cmd keeps the staged act file during an act render",
      '"%RENDER_COMPOSITION%"=="index.html" del /q _*_tmp.html' in render_cmd)

with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    (ep / "compositions").mkdir()
    (ep / "compositions" / "g.html").write_text("v1")
    f1 = ra.fingerprint(a2, ep, "full", 30)
    f1b = ra.fingerprint(a2, ep, "full", 30)
    (ep / "compositions" / "g.html").write_text("v2")
    check("fingerprint is stable, and changes when a mounted graphic changes",
          f1 == f1b and f1 != ra.fingerprint(a2, ep, "full", 30))
    check("fingerprint changes with mode", ra.fingerprint(a2, ep, "draft", 15) != ra.fingerprint(a2, ep, "full", 30))
    act1 = ra.slice_html(COMP, 0, 300, 30)  # host-g is parked here
    f0 = ra.fingerprint(act1, ep, "full", 30)
    (ep / "compositions" / "g.html").write_text("v3")
    f1 = ra.fingerprint(act1, ep, "full", 30)
    (ep / "compositions" / "g.html").write_text('v3 <video src="m.mp4" muted></video>')
    check("a parked graphic's edit keeps the act reusable, unless it changes hyperframes' probe (media without data-start)",
          f0 == f1 and f1 != ra.fingerprint(act1, ep, "full", 30))

# The act's root timeline (act starts at 10): a tween authored at 12-14 runs at act 2-4, one at 8-12 is half done at
# act 0, and one over at 4 has left its end state.
post = ra.POST % {"id": json.dumps("ep-x"), "a": 10.0}
js = re.sub(r"</?script>(/\*.*?\*/)?", "", post)
gsap = S.parent / "episodes" / "ep-1974-super-outbreak" / "gsap.min.js"
node = f"""
const {{gsap}} = require({json.dumps(str(gsap))});
global.gsap = gsap; global.window = {{ __timelines: {{}} }}; global.document = {{ querySelectorAll: () => [] }};
const o = {{ x: 0, y: 0, z: 0 }}; const tl = gsap.timeline({{ paused: true }});
tl.fromTo(o, {{ x: 0 }}, {{ x: 100, duration: 2, ease: "none" }}, 12);
tl.fromTo(o, {{ y: 0 }}, {{ y: 100, duration: 4, ease: "none" }}, 8);
tl.fromTo(o, {{ z: 0 }}, {{ z: 100, duration: 2, ease: "none" }}, 2);
tl.set({{}}, {{}}, 30); window.__timelines["ep-x"] = tl;
{js}
const r = [];
for (const t of [0, 2, 3, 4]) {{ tl.totalTime(t, true); r.push([o.x, o.y, o.z].join("/")); }}
console.log(r.join(" "));
"""
out = subprocess.run(["node", "-e", node], capture_output=True, text=True)
check("act root timeline: tweens land at act time (x/y/z at act 0,2,3,4 s)",
      out.stdout.strip() == "0/50/100 0/100/100 50/100/100 100/100/100")

# Audible media in the staged act (PR 223 defects 1 and 2: a JS clock read 6:26 where the single render read 7:41,
# a county fill showed): hyperframes' pre-capture sweep must visit this act's graphics as in the single render.
SWEEP = COMP.replace('<audio id="nx-1" src="audio/a.wav" data-start="1" data-duration="5"></audio>',
                     '<audio id="nx-1" src="audio/a.wav" data-start="1" data-duration="5"></audio>\n'
                     '  <audio id="nx-2" src="audio/b.wav" data-start="11" data-duration="6"></audio>\n'
                     '  <audio id="bed" src="audio/c.wav" data-start="7.99" data-duration="10" data-media-start="2"></audio>')
a1, a2s = ra.slice_html(SWEEP, 0, 300, 30), ra.slice_html(SWEEP, 300, 600, 30)
check("act 1: its audio stays at its time, audio after the act parks on the act's last frame",
      re.search(r'id="nx-1"[^>]*data-start="1.0"', a1) and re.search(r'id="nx-2"[^>]*data-start="9.96666', a1))
check("act 2: audio through the seam starts on its first sweep sample in the act, its media advanced with it",
      re.search(r'id="bed"[^>]*data-start="0.02333[^>]*data-duration="7.96666[^>]*data-media-start="4.03333', a2s))


def sweep(comp, fps=30):
    """Where hyperframes' pre-capture audio sweep (discoverAudioVolumeAutomationFromTimeline: every audible clip's
    window in document order at 1/fps, clamped to the composition, then 0) puts host-g's timeline: its local times,
    with before and after its span folded and repeats collapsed. Equal sequences leave equal GSAP state."""
    p = ra._Timed(comp)
    dur = float(p.root["attrs"]["data-duration"])
    host = next(e for e in p.els if e["attrs"].get("id") == "host-g")
    h0, h1 = ra._span(host)
    seq = []
    for el in p.els:
        if el["tag"] != "audio" and not (el["tag"] == "video" and "muted" not in el["attrs"]):
            continue
        s, e = ra._span(el)
        t, end = max(0.0, s), min(dur, e)
        while t <= end + 1e-6:
            loc = round(t - h0, 6)
            seq.append("before" if loc <= 0 else "after" if t >= h1 - 1e-6 else loc)
            if t == end:
                break
            t = min(end, t + 1 / fps)
    seq.append("before")
    return [x for i, x in enumerate(seq) if i == 0 or x != seq[i - 1]]


single = sweep(SWEEP)
check("act 2: the sweep visits its graphic at the same local times, in the same order, as in the single render",
      sweep(a2s) == single and "after" in single)
old = re.sub(r'\s*<audio[^>]*></audio>', "", a2s)  # the old staging dropped all audio: no sweep at all
check("act 2 without its audio is swept differently (the defect this guards)", sweep(old) != single)

# Defect 3 of PR 223: an element over before the act painted on act 2's first frames of one run.
styled = COMP.replace('id="kb-1"', 'id="kb-1" style="opacity: 0.9;"')
check("act 2: an element over before the act can never paint (display none, its own style kept)",
      re.search(r'id="kb-1"[^>]*style="display: none !important"', a2)
      and re.search(r'style="opacity: 0.9; display: none !important"', ra.slice_html(styled, 300, 600, 30))
      and re.search(r'style="font-family: &quot;Inter&quot;; display: none !important"',
                    ra.slice_html(COMP.replace('id="kb-1"', 'id="kb-1" style="font-family: &quot;Inter&quot;"'), 300, 600, 30))
      and re.search(r'id="kb-1" style="opacity:.5; display: none !important"',
                    ra.slice_html(COMP.replace('id="kb-1"', 'id="kb-1" style=opacity:.5'), 300, 600, 30))
      and "display: none" not in re.search(r'<section[^>]*id="kb-1"[^>]*>', ra.slice_html(COMP, 0, 300, 30)).group(0))

# main() with render.cmd, ffmpeg and ffprobe stubbed (no render): audit R5 (the run held no heavy lock, so TTS, e2e or
# another render took the machine between acts), R6 (a second run restaged _act_tmp.html while the first waited) and
# R12 (a poller read render.cmd's per-act "done 0" after act 1). Temp heavy lock; e2e's token is dropped.
import os  # noqa: E402
import types  # noqa: E402
import render_busy  # noqa: E402

with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    ep = root / "episodes" / "ep-t"
    (ep / "renders").mkdir(parents=True)
    (ep / "index.html").write_text(COMP, encoding="utf-8")
    import timeline  # noqa: E402
    lock = root / "heavy.lock"
    saved = (ra.SCRIPTS, ra.run_render, ra.video_frames, ra.subprocess, dict(os.environ))
    os.environ["HEAVY_LOCK_FILE"] = str(lock)
    os.environ.pop("HEAVY_LOCK_TOKEN", None)
    ra.SCRIPTS = root / "scripts"
    acts15 = ra.plan_acts(COMP, 15)[0]
    frames = {f"act{i:02d}.mp4": fb - fa for i, (fa, fb) in enumerate(acts15, 1)} | {"v1.mp4": acts15[-1][1]}
    seen, fail_on = [], None

    def fake_render(slug, mode, base, composition, extra_env=None):
        rec = {"base": base, "lock": render_busy.read_lock(lock), "staged": None, "hold": None,
               "marker": (ep / f"render_acts_{Path(base).parts[1]}_done.marker").exists()}
        if composition != "index.html":
            rec["staged"] = (ep / composition).read_text(encoding="utf-8")
        if not seen:  # render.cmd's own lock lines, from a cmd.exe: --hold must pass through, --release must not free it
            busy = f'"{sys.executable}" "{S / "render_busy.py"}"'
            bat = root / "hold.cmd"
            bat.write_text(f'@echo off\n{busy} --hold "render {slug} {mode}"\necho HOLD %ERRORLEVEL%\n{busy} --release\n',
                           encoding="utf-8")
            h = subprocess.run(["cmd", "/c", str(bat)], capture_output=True, text=True, timeout=30)
            rec["hold"] = (h.stdout, render_busy.read_lock(lock) == rec["lock"])
        seen.append(rec)
        if fail_on and base.endswith(fail_on):
            raise SystemExit("render.cmd failed (stub)")
        (ep / "renders" / f"{base}.mp4").write_bytes(b"")
        for log in (ep / f"render_{mode}.log", ep / "renders" / f"{base}.log"):  # render.cmd keeps a copy beside the mp4
            log.write_text(f"browserGpuMode probe worker0 NVIDIA {base}\n", encoding="utf-8")
        (ep / f"render_{mode}_done.marker").write_text("0\n")  # render.cmd writes this after every act

    def fake_subprocess_run(cmd, **k):
        if cmd[0] == "ffmpeg":
            Path(cmd[-1]).write_bytes(b"")
        return types.SimpleNamespace(returncode=0, stdout="20.0\n")

    ra.run_render, ra.subprocess = fake_render, types.SimpleNamespace(run=fake_subprocess_run)
    ra.video_frames = lambda path: frames[Path(path).name]
    try:
        ra.main(["ep-t", "draft", "v1"])
        acts_seen = [r for r in seen if "/act" in r["base"]]
        check("R5: every act and the audio pass render while this run holds the heavy lock",
              len(seen) == len(acts15) + 1 and all(r["lock"] and r["lock"]["pid"] == os.getpid()
                                                   and r["lock"]["job"] == "render_acts ep-t draft v1" for r in seen))
        check("R5: the lock is free once the run ends", not lock.exists())
        h = seen[0]["hold"]
        check("R5: render.cmd's --hold passes through on the run's token and its --release leaves the run's lock",
              h[0].strip() == "HOLD 0" and h[1])
        check("R6: each act renders its own slice, staged while the run holds the lock",
              [r["staged"] for r in acts_seen] == [ra.slice_html(COMP, fa, fb, 15) for fa, fb in acts15]
              and all(r["lock"] and r["lock"]["pid"] == os.getpid() for r in acts_seen))
        done = ep / "render_acts_v1_done.marker"
        check("R12: no render_acts done marker while acts render; 0 once the concat is checked",
              not any(r["marker"] for r in seen) and done.exists() and done.read_text() == "0\n")
        check("R11: the output's own fps (the act rate) and log sit beside it for verify_render.sh",
              (ep / "renders" / "v1.fps").read_text() == "15\n"
              and "acts/v1/audio" in (ep / "renders" / "v1.log").read_text(encoding="utf-8"))
        seen.clear()
        fail_on = "act02"
        try:
            ra.main(["ep-t", "draft", "v2"])
        except SystemExit:
            pass
        check("R12: a run that fails on act 2 leaves 1 in its marker (render.cmd's per-act marker said 0 after act 1)",
              (ep / "render_acts_v2_done.marker").exists() and (ep / "render_acts_v2_done.marker").read_text() == "1\n"
              and (ep / "render_draft_done.marker").read_text() == "0\n")
        check("R5: the lock is free after a failed run", not lock.exists())
    finally:
        ra.SCRIPTS, ra.run_render, ra.video_frames, ra.subprocess, env = saved
        os.environ.clear()
        os.environ.update(env)

print(f"\n{'ALL PASS' if not FAILS else str(len(FAILS)) + ' FAILED'}")
sys.exit(1 if FAILS else 0)
