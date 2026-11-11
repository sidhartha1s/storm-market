"""Pre-render checks on a 1080x1920 composition: python3 scripts/test_portrait_gates.py

The frame is the root's data-width / data-height (media_budget.comp_size, stage_comp.mjs compSize). Each
browser gate gets one case a 1920x1080 assumption gets wrong on the portrait fixture scripts/fixtures/portrait_ep:
its text sits below y 1080 (in frame on a short) and the defect variants sit inside 1920 px but past 1080 px.
Runs headless Chromium (render_busy.py refuses it beside a render).
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
FIXTURE = S / "fixtures" / "portrait_ep"
GSAP = S.parent / "library" / "gallery" / "gsap.min.js"
FAILS = []


def check(label, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + label + ("" if cond else f"\n{detail}"))
    if not cond:
        FAILS.append(label)


def node(script, *args, cwd=None):
    r = subprocess.run(["node", str(S / script), *map(str, args)], capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout + r.stderr


def make_ep(root, comps=None, index=None):
    """Copy of the fixture; comps = {name: html} replaces or adds compositions, index replaces index.html."""
    ep = Path(root) / "ep-portrait"
    shutil.copytree(FIXTURE, ep)
    shutil.copy(GSAP, ep / "gsap.min.js")
    for name, html in (comps or {}).items():
        (ep / "compositions" / f"{name}.html").write_text(html, encoding="utf-8")
    if index:
        (ep / "index.html").write_text(index, encoding="utf-8")
    return ep


def comp(body, tween="tl.to('#a', { duration: 8, x: 40 }, 0);"):
    return ("<!doctype html><html><head><meta charset='utf-8'></head><body><template>" + body +
            "<script>window.__timelines = window.__timelines || {}; const tl = gsap.timeline({ paused: true }); " + tween +
            " window.__timelines['" + "NAME" + "'] = tl;</script></template></body></html>")


def named(name, body, tween="tl.to('#a', { duration: 8, x: 40 }, 0);"):
    return comp(body, tween).replace("NAME", name)


TXT = "position:absolute;font:700 60px sans-serif;color:#fff;"
HOST = ('<div id="host-{n}" data-composition-id="{n}" data-composition-src="compositions/{n}.html" data-start="0" '
        'data-duration="8" data-track-index="{t}" data-width="1080" data-height="1920"></div>')


def index_with(*hosts):
    base = (FIXTURE / "index.html").read_text(encoding="utf-8")
    return re.sub(r'<div id="host-g1".*?</div>', "\n".join(hosts), base, flags=re.S)


# ---- shared readers: stage_comp.mjs compSize and media_budget.comp_size give the same answer
PORTRAIT_ROOT = '<div id="root" data-width="1080" data-height="1920" data-duration="8"></div><div id="host-x" data-width="1920" data-height="1080">'
r = subprocess.run(["node", "--input-type=module", "-e",
                    f"import {{ compSize }} from '{(S / 'stage_comp.mjs').as_uri()}';"
                    f"console.log(JSON.stringify([compSize({json.dumps(PORTRAIT_ROOT)}), compSize('<div id=\"root\"></div>')]))"],
                   capture_output=True, text=True)
check("stage_comp.compSize reads the root's data-width/height (not a host mount's) and defaults to 1920x1080",
      r.stdout.strip() == '[{"w":1080,"h":1920},{"w":1920,"h":1080}]', r.stdout + r.stderr)

sys.path.insert(0, str(S))
try:
    from media_budget import comp_size
except ImportError as e:
    comp_size = None
    check("media_budget.comp_size exists", False, str(e))
if comp_size:
    check("media_budget.comp_size: portrait root, then the 1920x1080 default",
          comp_size(PORTRAIT_ROOT) == (1080, 1920) and comp_size("<div id='root'></div>") == (1920, 1080))
check("optimize_clips.py calls comp_size instead of keeping its own data-width regex",
      'id="root"' not in (S / "optimize_clips.py").read_text(encoding="utf-8"))

# ---- blank_scan: text at y 1500 is ink on a 1080x1920 frame
with tempfile.TemporaryDirectory() as d:
    code, out = node("blank_scan.mjs", make_ep(d))
    check("blank_scan: text below y 1080 counts as ink on a 1080x1920 frame", code == 0 and "BLANK SCAN PASS" in out, f"(exit {code})\n{out[-500:]}")

# ---- overlap_check: an overlay line running past x 1080, and two comp texts colliding below y 1080
with tempfile.TemporaryDirectory() as d:
    wide = ('<div id="ov-wide" data-start="0" data-duration="8" data-track-index="5" style="position:absolute;left:700px;top:300px;'
            'white-space:nowrap;font-size:60px"><span>WIDE OVERLAY LINE TEXT</span></div>')
    ep = make_ep(d, index=(FIXTURE / "index.html").read_text(encoding="utf-8").replace("</body>", wide + "</body>"))
    code, out = node("overlap_check.mjs", ep)
    check("overlap_check: an overlay line past x 1080 is off-frame on a 1080x1920 frame", "off-frame: #ov-wide" in out, f"(exit {code})\n{out[-500:]}")
with tempfile.TemporaryDirectory() as d:
    stack = (f'<div id="a" style="{TXT}left:100px;top:1500px">FIRST LOWER LINE</div>'
             f'<div id="b" style="{TXT}left:100px;top:1520px">SECOND LOWER LINE</div>')
    code, out = node("overlap_check.mjs", make_ep(d, {"g1": named("g1", stack)}))
    check("overlap_check: two comp texts colliding below y 1080 are seen on a 1080x1920 frame", "comp-internal: g1" in out, f"(exit {code})\n{out[-500:]}")
with tempfile.TemporaryDirectory() as d:
    code, out = node("overlap_check.mjs", make_ep(d))
    check("overlap_check: the clean portrait fixture passes", code == 0, f"(exit {code})\n{out[-500:]}")

# ---- occlusion_check: a bottom-anchored line (y ~1600 on a short, ~700 on a 1080-high page) under an opaque card at y 1500
with tempfile.TemporaryDirectory() as d:
    lo = named("g-lo", f'<div id="a" style="{TXT}left:100px;bottom:300px">LOWER LINE TEXT</div>')
    up = named("g-up", '<div id="a" style="position:absolute;left:0;top:1500px;width:1080px;height:300px;background:#000"></div>')
    ep = make_ep(d, {"g-lo": lo, "g-up": up}, index_with(HOST.format(n="g-lo", t=2), HOST.format(n="g-up", t=4)))
    code, out = node("occlusion_check.mjs", ep)
    check("occlusion_check: a card covering text low in a 1080x1920 frame is found", code == 1 and "g-up covers g-lo" in out, f"(exit {code})\n{out[-500:]}")

# ---- graphics_qc: out-of-frame is measured against 1080x1920
with tempfile.TemporaryDirectory() as d:
    code, out = node("graphics_qc.mjs", make_ep(d))
    check("graphics_qc: text at y 1500 is in frame on a 1080x1920 frame (no out-of-frame)", "out-of-frame" not in out, f"(exit {code})\n{out[-700:]}")
with tempfile.TemporaryDirectory() as d:
    right = named("g1", f'<div id="a" style="{TXT}left:1200px;top:100px">RIGHT OF THE FRAME</div>')
    code, out = node("graphics_qc.mjs", make_ep(d, {"g1": right}))
    check("graphics_qc: text starting at x 1200 is out-of-frame on a 1080x1920 frame", "out-of-frame" in out, f"(exit {code})\n{out[-700:]}")

# ---- beat_probe: motion of an element low in the frame is motion
with tempfile.TemporaryDirectory() as d:
    code, out = node("beat_probe.mjs", make_ep(d), "g1=8")
    spans = json.loads(out.strip().splitlines()[-1]).get("g1", {}).get("spans") if code == 0 else None
    check("beat_probe: a tween on text at y 1500 is motion on a 1080x1920 frame", bool(spans), f"(exit {code})\n{out[-500:]}")

# ---- freeze_scan: a static comp low in the frame is a hold with something on screen, not "NOTHING on screen"
with tempfile.TemporaryDirectory() as d:
    still = named("g1", f'<div id="a" style="{TXT}left:100px;top:1500px">STILL LOWER TEXT</div>', "tl.to('#a', { duration: 0.1, opacity: 1 }, 0);")
    code, out = node("freeze_scan.mjs", make_ep(d, {"g1": still}), "--hold", "6")
    check("freeze_scan: a hold of text low in a 1080x1920 frame is reported with content on screen",
          code == 1 and "static" in out and "NOTHING on screen" not in out, f"(exit {code})\n{out[-600:]}")

print()
if FAILS:
    print(f"test_portrait_gates: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_portrait_gates: all PASS")
