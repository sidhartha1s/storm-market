"""Self-check for render_preflight's moving-face layer: python3 scripts/test_frozen_circle.py

Camille and Mayfield rough cuts (23 Oct 26) mounted pip-w*.mp4 stand-ins: a still of assets/paul/circle-portrait-560.jpg
(episodes/ep-camille-1969/media/pip/STAND-INS-README.txt; Camille commit 0ab221e4 swapped them for FlashHead face cuts).
The stand-in is rebuilt here the same way and mounted as every circle window of the shipped Palm Sunday timeline: it
must refuse naming only the moving face. A clip that moves (ffmpeg testsrc2, no face in git) must pass.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import render_preflight  # noqa: E402

palm = (S / "fixtures" / "layer_parity" / "ep-palm-sunday-1965.html").read_text(encoding="utf-8")
portrait = S.parent / "assets" / "paul" / "circle-portrait-560.jpg"
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def run(make_clip):
    with tempfile.TemporaryDirectory() as tmp:
        ep = Path(tmp) / "ep-palm-sunday-1965"
        (ep / "media" / "pip").mkdir(parents=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", *make_clip, "-t", "6", "-r", "25", "-pix_fmt", "yuv420p",
                        str(ep / "media" / "pip" / "clip.mp4")], check=True)
        html = re.sub(r'(<video class="pip"[^>]*src=")[^"]*', r"\1media/pip/clip.mp4", palm)
        (ep / "index.html").write_text(html, encoding="utf-8")
        rc = render_preflight.layer_refusal(ep)
        return rc, [name for name, _, _ in render_preflight.missing_layers(ep.name, html, ep)]


check("Camille 23 Oct stand-in (still portrait) refuses naming the moving face",
      run(["-loop", "1", "-i", str(portrait)]) == (6, ["moving presenter face"]))
check("a moving clip passes", run(["-f", "lavfi", "-i", "testsrc2=size=560x560"]) == (None, []))

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all frozen-circle checks passed")
