"""One-shot patch of three gates (reviewed as a diff, then deleted):
- sweep_episode.py: fold comp consts before reading tween positions (check 7); count hosts on ANY track as
  mounted (overlay comps sit on tracks 3-4); accept `ep-<year>` slugs in the CTA gate.
- beat_density.py: fold comp consts before parsing tweens.
- lint_timeline.py: a narration gap is sanctioned when a blackout or a declared hold spans it.
"""
import pathlib, re
S = pathlib.Path(__file__).resolve().parent


def patch(name, pairs):
    p = S / name; s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert s.count(a) == 1, (name, a[:60], s.count(a))
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8"); print("patched", name)


patch("sweep_episode.py", [
    ("from pathlib import Path\n", "from pathlib import Path\nfrom comp_consts import fold\n"),
    ('_cta_applies = bool(re.match(r"(ep\\d+|ms-)", _slug))', '_cta_applies = bool(re.match(r"(ep\\d*-|ms-)", _slug))'),
    ('mounted = {w["name"] for w in pic if w["tr"] == 2}', 'mounted = {w["name"] for w in wins if w["name"] in authored}   # overlay comps ride tracks 3-4'),
    ('    src = (ep / "compositions" / f"{gid}.html").read_text(encoding="utf-8", errors="replace")\n    ends = ',
     '    src = fold((ep / "compositions" / f"{gid}.html").read_text(encoding="utf-8", errors="replace"))\n    ends = '),
    ('    for w in pic:\n        if w["name"] != gid:', '    for w in wins:\n        if w["name"] != gid:'),
])
patch("beat_density.py", [
    ("from pathlib import Path\n", "from pathlib import Path\nfrom comp_consts import fold\n"),
    ('    src = f.read_text(encoding="utf-8", errors="replace")\n', '    src = fold(f.read_text(encoding="utf-8", errors="replace"))\n'),
])
patch("lint_timeline.py", [
    ("    # segments may be apart by at most the blackout length; the only sanctioned hole is the CTA.\n",
     "    # segments may be apart by at most the blackout length; the sanctioned holes are the CTA, a chapter\n"
     "    # blackout, and a declared hold (<section class=\"clip hold\" data-start data-duration>, DESIGN.md).\n"),
    ("    for (s1, e1), (s2, e2) in zip(voice, voice[1:]):\n        gap = s2 - e1\n        if gap > 0.8 and not any(e1 - 0.5 <= c <= s2 for c in cta_starts):",
     "    structure = [(float(a), float(a) + float(b)) for a, b in re.findall(\n"
     "        r'<section\\b[^>]*class=\"[^\"]*\\b(?:blackout|hold)\\b[^\"]*\"[^>]*data-start=\"([\\d.]+)\"[^>]*data-duration=\"([\\d.]+)\"', html)]\n"
     "    for (s1, e1), (s2, e2) in zip(voice, voice[1:]):\n        gap = s2 - e1\n"
     "        if gap > 0.8 and not any(e1 - 0.5 <= c <= s2 for c in cta_starts) \\\n"
     "                and not any(bs < s2 and be > e1 for bs, be in structure):"),
])
