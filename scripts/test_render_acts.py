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
      re.search(r'id="bo-1" data-start="0.0" data-act-start="0.0" data-act-src-start="9.8" data-duration="0.1999', a2))
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

print(f"\n{'ALL PASS' if not FAILS else str(len(FAILS)) + ' FAILED'}")
sys.exit(1 if FAILS else 0)
