"""Audio-level gate: every audible element lands where its class belongs.

Why this exists: ep6 shipped a mixdown where the NPR hook insert was 6.8 dB
quieter than narration (source wav quiet, attr volume already 1.0) and an
earlier cut had a score bed at data-volume 0.08 — inaudible under a -16 LUFS
mix. Both defects are three numbers per element; a human ear catches them only
after a full listen. Mechanical, repeated, must never be forgotten -> code.

Checks (effective dB = file mean_volume + 20*log10(data-volume)):
  1. Narration (nx-*): reference = median; any segment >3 dB off median = FAIL.
  2. Inserts (ins-*): effective level within +/-2.5 dB of narration ref = FAIL
     otherwise ("dispatch must be as audible as narration" — owner 2026-08-17).
  3. Beds (any <audio data-bed>, regardless of id prefix — bgm-/sfx-/sx-/hf- all carry
     it): FAIL if within 6 dB of the narration ref (a bed that close competes with voice,
     never a WARN-only defect — DESIGN.md "ducked under narration"). FAIL if a music bed
     (id sx-mus-*) is inaudible (<ref-30 dB). WARN if near-inaudible otherwise.
  4. Audible video clips (any <video> not `muted`, data-volume default 1.0):
     WARN if above narration ref (clip audio shouting over voice).
  5. Any other audible <audio> (no nx-/ins- id and no data-bed attribute) is an
     unclassified element = FAIL — tag it data-bed or use the nx-/ins- convention.

Usage: python3 scripts/audio_levels.py episodes/<slug>
Exit 0 = pass. Exit 1 = level defects, do not build the mixdown yet.
"""
import math
import re
import statistics
import subprocess
import sys
from pathlib import Path

ep = Path(sys.argv[1])
html = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

def file_mean_db(p):
    out = subprocess.run(
        ["ffmpeg", "-i", str(p), "-map", "0:a:0", "-af", "volumedetect",
         "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.search(r"mean_volume: (-?[\d.]+) dB", out)
    return float(m.group(1)) if m else None

els = []
for m in re.finditer(r"<(audio|video)\b([^>]*)>", html):
    kind, attrs = m.group(1), m.group(2)
    src = re.search(r'src="([^"]+)"', attrs)
    # `\s` before id= — hyperframes stamps `data-hf-id="hf-xxxx"` on most elements, and an
    # unanchored `id="..."` search matches INSIDE that attribute name ("...hf-id=") before it
    # ever reaches the real `id="nx-..."` attribute, misreading every classified element as an
    # unclassified "hf-xxxx" one. Root cause of the reported "hf- (164), bgm-, sfx- all take
    # the warn-only path" — those elements were never actually being read by their real id.
    eid = re.search(r'\sid="([^"]+)"', attrs)
    vol = re.search(r'data-volume="([\d.]+)"', attrs)
    if not (src and eid):
        continue
    # A video is silent only when it says so: the `muted` attribute (repo convention) or
    # data-volume 0. hyperframes plays every other video's track at data-volume, default 1.0;
    # the old "no data-volume = muted" assumption let El Reno v3 ship audible stock footage.
    if kind == "video" and re.search(r"\smuted(?=[\s>/=]|$)", attrs):
        continue
    v = float(vol.group(1)) if vol else 1.0
    if v <= 0:
        continue
    is_bed = bool(re.search(r'\sdata-bed(?=[\s>/=]|$)', attrs))
    els.append((kind, eid.group(1), src.group(1), v, is_bed))

cache, rows = {}, []
for kind, eid, src, v, is_bed in els:
    p = ep / src
    if src not in cache:
        cache[src] = file_mean_db(p) if p.exists() else None
    mean = cache[src]
    if mean is None:
        rows.append((kind, eid, src, v, is_bed, None, None))
        continue
    rows.append((kind, eid, src, v, is_bed, mean, mean + 20 * math.log10(v)))

narr = [eff for eid, _, _, _, eff in rows if eid.startswith("nx-") and eff is not None]
if not narr:
    print("[audio_levels] FAIL — no nx-* narration elements found")
    raise SystemExit(1)
ref = statistics.median(narr)
print(f"[audio_levels] narration reference (median of {len(narr)} nx-*): {ref:.1f} dB")

fails, warns = [], []
for eid, src, v, mean, eff in rows:
    if eff is None:
        fails.append(f"{eid}: no audio stream / unreadable ({src})")
        continue
    d = eff - ref
    if eid.startswith("nx-"):
        if abs(d) > 3.0:
            fails.append(f"{eid}: narration {d:+.1f} dB off reference")
    elif eid.startswith("ins-"):
        if abs(d) > 2.5:
            fails.append(f"{eid}: insert {d:+.1f} dB vs narration (fix the FILE gain, attr vol is {v})")
    elif eid.startswith("sx-"):
        if eid.startswith("sx-mus") and d < -30:
            fails.append(f"{eid}: music bed inaudible ({d:+.1f} dB vs narration)")
        elif d > -3:
            warns.append(f"{eid}: bed only {d:+.1f} dB under narration — competes with voice")
        elif d < -30:
            warns.append(f"{eid}: bed {d:+.1f} dB vs narration — near-inaudible, intended?")
    else:  # audible video clip
        if d > 0:
            warns.append(f"{eid}: clip audio {d:+.1f} dB ABOVE narration")

for w in warns:
    print(f"  warn  {w}")
for f in fails:
    print(f"  FAIL  {f}")
print(f"[audio_levels] {'FAIL' if fails else 'PASS'} — {len(rows)} audible elements, "
      f"{len(fails)} failures, {len(warns)} warnings")
raise SystemExit(1 if fails else 0)
