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
check("act 2: narration audio dropped (sound comes from the one full pass)", "<audio" not in a2)
check("act 2: act 1's video dropped, its own video kept", 'id="v-a1"' not in a2 and 'id="v-a2"' in a2)
check("act 2: times shifted by the act start", 'id="v-a2" src="media/b.mp4" data-start="0.1999999999999993"' in a2
      and re.search(r'id="host-g"[^>]*data-start="2.0"', a2))
check("act 2: media offset untouched for a clip inside the act", 'data-media-start="3"' in a2)
check("act 2: authored scripts can read the original times", 'data-act-src-start="10.2"' in a2)
check("act 2: a plain element over before the act stays (scripts may count it), parked past the act's end",
      re.search(r'id="kb-1" data-start="11.0"', a2))
check("act 2: the blackout running through the seam starts at 0 with its remaining length",
      re.search(r'id="bo-1" data-start="0.0" data-act-start="0.0" data-act-src-start="9.8" data-duration="0.2000', a2))
check("act 2: root length is the act's frames", re.search(r'id="root"[^>]*data-duration="10.0"', a2))
check("act 1 drops act 2's media and host", 'id="v-a2"' not in ra.slice_html(COMP, 0, 300, 30)
      and "host-g" not in ra.slice_html(COMP, 0, 300, 30))
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

# Audio in the staged act (defects 1 and 2 of PR 223: a JS clock read 6:26 instead of 7:41, a county fill showed).
SWEEP = COMP.replace('<audio id="nx-1" src="audio/a.wav" data-start="1" data-duration="5"></audio>',
                     '<audio id="nx-1" src="audio/a.wav" data-start="1" data-duration="5"></audio>\n'
                     '  <audio id="nx-2" src="audio/b.wav" data-start="11" data-duration="6"></audio>\n'
                     '  <audio id="bed" src="audio/c.wav" data-start="8" data-duration="10" data-media-start="2"></audio>')
a1, a2s = ra.slice_html(SWEEP, 0, 300, 30), ra.slice_html(SWEEP, 300, 600, 30)
check("act 1: its audio stays at its time, audio after the act parks on the act's last frame",
      re.search(r'id="nx-1"[^>]*data-start="1.0"', a1) and re.search(r'id="nx-2"[^>]*data-start="9.96666', a1))
check("act 2: audio over before the act goes, audio through the seam starts at 0 with its media advanced",
      'id="nx-1"' not in a2s and re.search(r'id="bed"[^>]*data-start="0.0"[^>]*data-duration="8.0"[^>]*data-media-start="4.0"', a2s))


def sweep_frames(comp, fa, fb, fps=30):
    """What a graphic's JS clock reads on each frame [fa, fb) of a render of comp: hyperframes' pre-capture audio
    sweep (root totalTime over every audio window at 1/fps, suppressed, then 0), then one seek per frame."""
    p = ra._Timed(comp)
    dur = float(p.root["attrs"]["data-duration"])
    wins = [(float(e["attrs"]["data-start"]), float(e["attrs"]["data-start"]) + float(e["attrs"]["data-duration"]))
            for e in p.els if e["tag"] == "audio"]
    host = next(e for e in p.els if e["attrs"].get("id") == "host-g")
    post = comp.find("<script>/* render_acts: back")
    js = re.sub(r"</?script>(/\*.*?\*/)?", "", comp[post:comp.rfind("</script>") + 9]) if post >= 0 else ""
    node = f"""
const {{gsap}} = require({json.dumps(str(gsap))});
global.gsap = gsap; global.window = {{ __timelines: {{}} }}; global.document = {{ querySelectorAll: () => [] }};
const root = gsap.timeline({{ paused: true }}); root.set({{}}, {{}}, 20); window.__timelines["ep-x"] = root;
{js}
const clk = {{ m: 0 }}; let text = "start"; const g = gsap.timeline({{ paused: true }});
[[1, 0, 10], [2, 10, 20], [3, 20, 30]].forEach(([t, a, b]) => g.fromTo(clk, {{ m: a }}, {{ m: b, duration: 1, ease: "none",
  immediateRender: false, onUpdate: () => {{ text = String(Math.floor(clk.m)); }} }}, t));
root.add(g, {float(host["attrs"]["data-start"])});
for (const [s, e] of {json.dumps(wins)}) {{
  for (let t = Math.max(0, s); t <= Math.min({dur}, e) + 1e-6; t = Math.min({dur}, e, t + 1 / {fps})) {{
    root.totalTime(t, true); if (t === Math.min({dur}, e)) break; }}
}}
root.totalTime(0, true);
const out = [];
for (let f = 0; f < {fb - fa}; f++) {{ root.totalTime(f / {fps}); out.push(text); }}
console.log(out.join(","));
"""
    r = subprocess.run(["node", "-e", node], capture_output=True, text=True)
    return r.stdout.strip().split(",") if r.returncode == 0 else [r.stderr]


single = sweep_frames(SWEEP, 0, 600)
staged = sweep_frames(a2s, 300, 600)
check("act 2: a graphic's JS state on every frame matches the single render's (audio sweep kept)",
      len(single) == 600 and staged == single[300:] and single[300] != "start")
old = re.sub(r'\s*<audio[^>]*></audio>', "", a2s)  # the old staging: no audio, so no sweep
check("act 2 without its audio diverges from the single render (the defect this guards)",
      sweep_frames(old, 300, 600) != single[300:])

# Defect 3 of PR 223: an element over before the act painted on act 2's first frames of one run.
styled = COMP.replace('id="kb-1"', 'id="kb-1" style="opacity: 0.9;"')
check("act 2: an element over before the act can never paint (display none, its own style kept)",
      re.search(r'id="kb-1"[^>]*style="display: none !important"', a2)
      and re.search(r'style="opacity: 0.9; display: none !important"', ra.slice_html(styled, 300, 600, 30))
      and "display: none" not in ra.slice_html(COMP, 0, 300, 30))

print(f"\n{'ALL PASS' if not FAILS else str(len(FAILS)) + ' FAILED'}")
sys.exit(1 if FAILS else 0)
