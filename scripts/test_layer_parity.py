"""Self-check for render_preflight's layer-parity gate: python3 scripts/test_layer_parity.py

Owner 18 Oct 26: "I need gates for the stuff which I have already asked". Each fixture is staged as an episode folder
and run through layer_refusal(), the call render.cmd's preflight makes.
- ep-joplin-2011-540857c1.html: the Joplin timeline at commit 540857c1 (beds mounted, 0 corner-circle mounts) must refuse
  naming only the circle.
- ep-palm-sunday-1965.html: the shipped Palm Sunday timeline (origin/ep-palm-sunday-1965 6fec3f20) must pass.
- The same Palm Sunday timeline with its bed mounts removed must refuse naming only the bed.
"""
import re
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import render_preflight  # noqa: E402

FIX = S / "fixtures" / "layer_parity"
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def run(slug, html):
    with tempfile.TemporaryDirectory() as tmp:
        ep = Path(tmp) / slug
        ep.mkdir()
        (ep / "index.html").write_text(html, encoding="utf-8")
        rc = render_preflight.layer_refusal(ep)
    return rc, [name for name, _, _ in render_preflight.missing_layers(slug, html)]


palm = (FIX / "ep-palm-sunday-1965.html").read_text(encoding="utf-8")
joplin = (FIX / "ep-joplin-2011-540857c1.html").read_text(encoding="utf-8")
no_bed = re.sub(r'\s*<audio id="sx-bed[^>]*></audio>', "", palm)

check("Joplin 540857c1 refuses naming the circle",
      run("ep-joplin-2011", joplin) == (6, ["presenter corner circle"]))
check("Palm Sunday passes", run("ep-palm-sunday-1965", palm) == (None, []))
check("Palm Sunday stripped of its 8 bed mounts",
      palm.count('id="sx-bed') == 8 and no_bed.count('id="sx-bed') == 0)
check("Palm Sunday without its bed refuses naming the bed",
      run("ep-palm-sunday-1965", no_bed) == (6, ["music bed"]))
hook_bed_only = re.sub(r'\s*<audio id="sx-bed-[az]\d[^>]*></audio>', "", palm)
check("Palm Sunday with only its 111 s hook bed refuses on coverage",
      hook_bed_only.count('id="sx-bed') == 1
      and render_preflight.missing_layers("ep-palm-sunday-1965", hook_bed_only)[0][:2]
      == ("music bed", "beds cover 9% of the narration span 9.9-1176.8 s, need 80%"))
check("a mini (ms-) is out of scope", run("ms-palm-sunday", no_bed) == (None, []))

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all layer-parity checks passed")
