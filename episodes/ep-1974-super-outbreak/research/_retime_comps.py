"""One-shot mechanical retime of hand-decided comp windows (orchestrator's per-comp decisions, applied by regex).
Person cards: DUR = the host window chosen in index.html (the card exits at DUR-0.6).
g-person-gilbert: mounted at "helicopter" (513.4 abs) so CUES.commendation moves to 26.8.
g-radar-a3: fivehooks/dark re-cued to the final words.json (a3-s2), DUR = 44.03 (host runs to the map handover).
g-f6: mounted 2.44 s into A3-S1 (real footage carries the CTA payoff cut first), cues shift by -2.44.
Deleted after use; diff reviewed before commit.
"""
import re, pathlib
C = pathlib.Path(__file__).resolve().parent.parent / "compositions"
dur = {"g-person-pearson": 10.5, "g-person-haley": 14.0, "g-person-allen": 12.0, "g-person-heath": 12.0,
       "g-person-gilligan": 12.0, "g-person-poole": 12.0, "g-person-pennington": 14.0, "g-person-mcguire": 12.0,
       "g-person-gilbert": 28.3}
for name, d in dur.items():
    p = C / f"{name}.html"; s = p.read_text(encoding="utf8")
    s2, n = re.subn(r"const DUR = [\d.]+;[^\n]*", f"const DUR = {d}; // host window set by the orchestrator (index.html)", s)
    assert n == 1, name
    if name == "g-person-gilbert":
        s2, n = re.subn(r"commendation: [\d.]+", "commendation: 26.8", s2); assert n == 1
    p.write_text(s2, encoding="utf8"); print("retimed", name, d)
p = C / "g-radar-a3.html"; s = p.read_text(encoding="utf8")
for a, b in [(r"fivehooks: [\d.]+", "fivehooks: 38.44"), (r"dark: [\d.]+", "dark: 42.94"),
             (r"const DUR = [\d.]+;[^\n]*", "const DUR = 44.03; // dark. at 42.94 + eyebrow-only hold to the map handover")]:
    s, n = re.subn(a, b, s); assert n == 1, a
p.write_text(s, encoding="utf8"); print("retimed g-radar-a3")
p = C / "g-f6.html"; s = p.read_text(encoding="utf8")
for a, b in [(r"six: [\d.]+", "six: 4.40"), (r"tookback: [\d.]+", "tookback: 9.04"),
             (r"const DUR = [\d.]+;[^\n]*", "const DUR = 12.56; // mounted 2.44 s into A3-S1 after the real-footage payoff cut")]:
    s, n = re.subn(a, b, s); assert n == 1, a
p.write_text(s, encoding="utf8"); print("retimed g-f6")
