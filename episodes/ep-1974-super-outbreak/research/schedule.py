"""Timing table for hand-authoring index.html: places every narration segment on the master clock with the
script's voids, holds, chapter blackouts and the CTA (DESIGN.md blackout table + CTA contract). Prints the table
and writes research/schedule.json. Pure arithmetic over audio/manifest.json; authors nothing.
"""
import json, pathlib

ep = pathlib.Path(__file__).resolve().parent.parent
man = json.loads((ep / "audio/manifest.json").read_text(encoding="utf8"))
GAP = 0.45          # breath between segments inside an act
PAD = 0.30          # picture pad either side of a chapter blackout
CTA_DUR, DIP = 15.139, 1.0
order = ["h", "i-1", "i-2", "a1-s1", "a1-s1b", "a1-s2", "a1-s3a", "a1-s3b", "a2-s1", "a2-s2a", "a2-s2b", "a2-s3", "a2-s4", "a2-s5",
         "a3-s1", "a3-s2", "a3-s2b", "a3-s3", "a3-s4", "a3-s5", "a4-s1a", "a4-s1b", "a4-s2", "a4-s3",
         "a5-s1", "a5-s2", "a5-s3", "a5-s4", "a6-s1", "a6-s1b", "a6-s2", "a6-s3", "z-1"]
# what happens AFTER a segment ends (before the next starts)
after = {"h": ("void", 1.5), "i-2": ("blackout", 0.7), "a1-s3a": ("hold", 3.0), "a1-s3b": ("blackout", 0.8),
         "a2-s2a": ("hold", 4.0), "a2-s5": ("blackout", 0.8), "a3-s5": ("blackout", 0.8), "a4-s1a": ("hold", 3.5),
         "a4-s3": ("blackout", 0.9), "a5-s4": ("blackout", 0.8),
         "a6-s1b": ("cta", None)}   # owner 21 Sep 26 after the draft: CTA at ~88 %, hinge = the 16-vs-4 payoff, then "here is what changed"
t = 5.2             # hook narration enters after the WHAS anchor line (0-4.9 s: "we have a hook echo on the radar")
rows, markers = [], []
for sid in order:
    d = man[sid]["duration"]
    rows.append({"id": sid, "start": round(t, 3), "dur": d, "end": round(t + d, 3), "wpm": man[sid]["wpm"]})
    t += d
    kind, val = after.get(sid, ("gap", GAP))
    if kind == "gap":
        t += val
    elif kind == "void":
        markers.append({"kind": "void", "start": round(t, 3), "dur": val}); t += val
    elif kind == "hold":
        markers.append({"kind": "hold", "start": round(t, 3), "dur": val}); t += val + 0.2
    elif kind == "blackout":
        markers.append({"kind": "blackout", "start": round(t + PAD, 3), "dur": val}); t += PAD + val + PAD
    elif kind == "cta":
        markers.append({"kind": "dip", "start": round(t + PAD, 3), "dur": DIP})
        cta_start = t + PAD + DIP
        markers.append({"kind": "cta", "start": round(cta_start, 3), "dur": CTA_DUR})
        markers.append({"kind": "dip", "start": round(cta_start + CTA_DUR, 3), "dur": DIP})
        t = cta_start + CTA_DUR + DIP + 0.1
TAIL = 4.0          # outro card after the last line
total = round(t + TAIL, 2)
cta = next(m for m in markers if m["kind"] == "cta")
out = {"total": total, "segments": rows, "markers": markers, "cta_fraction": round(cta["start"] / total, 3)}
(ep / "research/schedule.json").write_text(json.dumps(out, indent=1), encoding="utf8")
for r in rows:
    print(f"{r['id']:8s} {r['start']:8.2f} -> {r['end']:8.2f}  ({r['dur']:5.1f}s, {r['wpm']} wpm)")
for m in markers:
    print(f"   {m['kind']:9s} {m['start']:8.2f} +{m['dur']}")
print(f"TOTAL {total}s = {total/60:.2f} min | CTA at {cta['start']:.2f}s = {out['cta_fraction']:.0%} (owner window for this episode 85-92 %)")
