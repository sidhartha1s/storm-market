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
  6. Narration (nx-*) ending in a burst: a loud run (> -40 dB) in the file's last
     0.6 s that follows 0.1 s or more of silence (< -55 dB) = FAIL. TTS sometimes
     appends a full-band click after the last word; it plays as a split second of
     static at the line's end. Fix: a -v2 copy with the burst silenced, same length.

Usage: python3 scripts/audio_levels.py episodes/<slug>
Exit 0 = pass. Exit 1 = level defects, do not build the mixdown yet.
"""
import array
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

def tail_burst(p, tail_s=0.6, win_s=0.01):
    """(peak dB, silence gap s) when the file ends in a loud run after silence, else None."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-sseof", f"-{tail_s}", "-i", str(p), "-map", "0:a:0",
                          "-ac", "1", "-ar", "24000", "-f", "s16le", "-"], capture_output=True).stdout
    s = array.array("h", raw[: len(raw) // 2 * 2])
    w = int(24000 * win_s)
    db = []
    for i in range(0, len(s) - w + 1, w):
        ms = sum(v * v for v in s[i:i + w]) / w
        db.append(10 * math.log10(ms / 32768 ** 2) if ms else -180.0)
    k = len(db)
    while k and db[k - 1] > -40:
        k -= 1
    if k == len(db):
        return None  # last window is quiet: a normal ending
    gap = 0
    while k - gap - 1 >= 0 and db[k - gap - 1] < -55:
        gap += 1
    return (max(db[k:]), gap * win_s) if gap * win_s >= 0.1 else None


els = []
# Attributes as a dict (timeline.mounts): `id` is the real id, never the tail of hyperframes' `data-hf-id`.
for kind, a in timeline.mounts(html):
    if "src" not in a:
        continue
    # A video is silent only when it says so: the `muted` attribute (repo convention) or
    # data-volume 0. hyperframes plays every other video's track at data-volume, default 1.0;
    # the old "no data-volume = muted" assumption let El Reno v3 ship audible stock footage.
    if kind == "video" and "muted" in a:
        continue
    v = float(a.get("data-volume") or 1.0)
    if v <= 0:
        continue
    # an element with no id is still audible: it reaches check 5 (unclassified), it is never skipped
    els.append((kind, a.get("id") or f"<no id: {a['src']}>", a["src"], v, "data-bed" in a))

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

narr = [eff for kind, eid, _, _, _, _, eff in rows if timeline.is_narration(eid) and eff is not None]
if not narr:
    print("[audio_levels] FAIL — no nx-* narration elements found")
    raise SystemExit(1)
ref = statistics.median(narr)
print(f"[audio_levels] narration reference (median of {len(narr)} nx-*): {ref:.1f} dB")

fails, warns = [], []
for kind, eid, src, v, is_bed, mean, eff in rows:
    if eff is None:
        fails.append(f"{eid}: no audio stream / unreadable ({src})")
        continue
    d = eff - ref
    if eid.startswith("nx-"):
        if abs(d) > 3.0:
            fails.append(f"{eid}: narration {d:+.1f} dB off reference")
        burst = tail_burst(ep / src)
        if burst:
            fails.append(f"{eid}: ends in a {burst[0]:.0f} dB burst after {burst[1]:.2f} s of silence ({src}); "
                         f"write a -v2 copy with the burst silenced, same length")
    elif eid.startswith("ins-"):
        if abs(d) > 2.5:
            fails.append(f"{eid}: insert {d:+.1f} dB vs narration (fix the FILE gain, attr vol is {v})")
    elif is_bed:
        if d > -6.0:
            fails.append(f"{eid}: bed {d:+.1f} dB vs narration — within 6 dB, competes with voice (DESIGN.md ducking)")
        elif eid.startswith("sx-mus") and d < -30:
            fails.append(f"{eid}: music bed inaudible ({d:+.1f} dB vs narration)")
        elif d < -30:
            warns.append(f"{eid}: bed {d:+.1f} dB vs narration — near-inaudible, intended?")
    elif kind == "video":  # audible video clip
        if d > 0:
            warns.append(f"{eid}: clip audio {d:+.1f} dB ABOVE narration")
    else:
        fails.append(f"{eid}: unclassified audio ({src}) — not nx-/ins- and no data-bed attribute")

for w in warns:
    print(f"  warn  {w}")
for f in fails:
    print(f"  FAIL  {f}")
print(f"[audio_levels] {'FAIL' if fails else 'PASS'} — {len(rows)} audible elements, "
      f"{len(fails)} failures, {len(warns)} warnings")
raise SystemExit(1 if fails else 0)
