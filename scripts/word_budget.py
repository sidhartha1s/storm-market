#!/usr/bin/env python3
"""Word budget for a storm-market script, measured, never assumed.

ep-1974 shipped 17:30 against a 22:00 target because three guesses stacked: a 152 wpm constant (the voice ran 165
native on that script, 181 after atempo 1.10), a 2.2 min overhead constant (the real non-voice time was 0.8 min),
and a script locked 273 words under its own budget. This gate replaces all three with measurements:

  pace     = words / seconds of the probe wavs you pass (the SAME tempo the episode ships at)
  overhead = the non-voice markers you pass (CTA, dips, void, blackouts, holds, outro tail), in seconds
  budget   = (target_min * 60 - overhead) * pace / 60 words
  verdict  = FAIL unless the script's count lands inside target +/- tolerance

Usage:
  python3 scripts/word_budget.py episodes/<slug> --target 25 --probe audio/probe/h.wav audio/probe/a4.wav
        [--overhead-s 60] [--tolerance-min 1.0] [--script edit_script.md]
Probe wavs need a sibling .txt with the exact text that was synthesised (tts_prep writes it).
Exit 0 inside the band, 1 outside. Prints the numbers either way.
"""
import argparse, pathlib, re, sys, wave

ap = argparse.ArgumentParser()
ap.add_argument("episode"); ap.add_argument("--target", type=float, required=True, help="minutes")
ap.add_argument("--probe", nargs="+", required=True, help="wav files at the shipping tempo, each with a .txt beside it")
ap.add_argument("--overhead-s", type=float, default=None, help="non-voice seconds; default derived from research/schedule.json markers if present, else 60")
ap.add_argument("--tolerance-min", type=float, default=1.0); ap.add_argument("--script", default="edit_script.md")
a = ap.parse_args()
ep = pathlib.Path(a.episode)

# 1. pace from the probes
sec = words = 0
for p in a.probe:
    w = ep / p if not pathlib.Path(p).is_absolute() else pathlib.Path(p)
    with wave.open(str(w)) as f: sec += f.getnframes() / f.getframerate()
    words += len(re.findall(r"[A-Za-z0-9']+", w.with_suffix(".txt").read_text(encoding="utf-8")))
pace = words / sec * 60

# 2. overhead
if a.overhead_s is None:
    sj = ep / "research/schedule.json"
    if sj.exists():
        import json
        a.overhead_s = sum(m["dur"] for m in json.loads(sj.read_text(encoding="utf-8"))["markers"]) + 4.0   # + outro tail
    else:
        a.overhead_s = 60.0

# 3. script count (tag-stripped, same rules as research/wordcount.py)
s = (ep / a.script).read_text(encoding="utf-8")
body = s.split("## SCRIPT", 1)[1] if "## SCRIPT" in s else s
body = body.split("## Fact register", 1)[0]
body = re.sub(r"\*\*[A-Z]\d?-S\d[^*]*\*\*", "", body); body = re.sub(r"\*\([^)]*\)\*", "", body); body = re.sub(r"\[[^\]]*\]", "", body)
body = re.sub(r"^#+ .*$", "", body, flags=re.M)
count = len(re.findall(r"[A-Za-z0-9']+", body))

budget = (a.target * 60 - a.overhead_s) * pace / 60
runtime = count / pace + a.overhead_s / 60
lo, hi = a.target - a.tolerance_min, a.target + a.tolerance_min
print(f"pace     {pace:6.1f} wpm  (measured on {len(a.probe)} probe wav(s), {words} words / {sec:.1f} s)")
print(f"overhead {a.overhead_s:6.1f} s    (non-voice)")
print(f"budget   {budget:6.0f} words for {a.target:.0f}:00")
print(f"script   {count:6d} words -> predicted {int(runtime)}:{int(runtime % 1 * 60):02d}")
ok = lo <= runtime <= hi
print(f"[word_budget] {'PASS' if ok else 'FAIL'} — {'inside' if ok else 'outside'} {lo:.0f}:00 to {hi:.0f}:00; {'add' if runtime < lo else 'cut'} about {abs(budget - count):.0f} words" if not ok else f"[word_budget] PASS — inside {lo:.0f}:00 to {hi:.0f}:00")
sys.exit(0 if ok else 1)
