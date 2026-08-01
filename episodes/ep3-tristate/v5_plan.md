# ep3-tristate v5 — final-render pass (owner QC of v4 draft, 2026-07-30)

Executor: Opus, SAME session main thread (no subagent). Planner: Fable.
Owner verdict on v4: clutter removal landed ("clean and minimalistic, won't say AI created
this"), graphics mostly nice and match-cut. Remaining items below, then — if ALL gates and
preflight pass — **ship the FINAL full-quality render** (owner authorized 2026-07-30).

## Work items

### 1. 5:48 — kill the wind SFX, permanently
`02_wind_ominous_steady.mp3` (sfx-wind1, window 346–370s) reads as grey noise under the TTS.
- Remove the `sfx-wind1` audio element + its two volume tweens from `build_ep3.py` (the `sfx`
  list and `sfxjs`). Keep sfx-rumble (0–36s) — not flagged.
- LEARNINGS.md: owner order — this file is never used again in any episode. (File stays in
  assets/sfx; the ban is on wiring it.)

### 2. 6:33 — frozen frame on g-track-1 tail
Window 374–398s; the draw finishes ~22s in and the frame sits. Owner suggestion: blip the
red dot. Add a gentle repeating pulse on `g-track-1-storm` (and the Ellington dot `d0`)
covering the tail — e.g. `repeat:-1, yoyo:true` scale/opacity breath from ~20s to end of
timeline. beat_density counts repeats now, so this clears the gate too.

### 3. 10:05 — Gorham quote lands too early
`q-83` fires at 603.6s (qs = seg_start + 8.0 because a lower third is present; seg a3-s1
starts 595.4s). Narration: check `audio/a3-s1.words.json` — the quote should appear when the
survivor line is actually reached, not 8s in. Fix in build_ep3.py `quote` block: delay the
gorham quote start (likely `seg_start + 11–13s` — read the words.json and pick the moment the
quoted description begins, "the air was full of everything"). Verify no collision with the
lower third (it runs 7s from seg_start+0.4).

### 4. RHS panel cards exit early — ALL panels
Every g-panel-*.html flies out (`x:980, autoAlpha:0`) ~1.5s before its own timeline end, and
`close_picture_gaps` often extends the host window past the comp duration — so the panel is
gone while its beat is still talking. Fix once, mechanically:
- In each `compositions/g-panel-*.html`: DELETE the exit tween (the `x:980, autoAlpha:0`
  line). The panel holds until the hard cut, like ep2. That also removes the early-exit
  freeze the extension was showing.
- Panels: finley, annapolis, gorham, murphysboro, desoto, schools, wf, parrish, griffin,
  princeton, redcross, nonet, cost, song. (g-sources has no exit tween — check.)
- graphics_qc measures a comp never outliving its timeline — deleting exits doesn't affect it.

### 5. 28:00 — g-timeline pacing: slow the middle, match-cut to TTS
Comp 1660–1695s, narration a6-s2 runs to 1702s. Owner: beginning close, MIDDLE too fast,
ending close. Read `audio/a6-s2.words.json`; re-time the six milestone reveals so each lands
on its spoken date (1938/1948/1952/1970s/1990s/today are named in narration). Stretch the
middle reveals; comp timeline may grow toward ~1702−1660 = 42s — bump `_durations.json` via
graphics_qc re-measure (it regenerates) and rebuild.

### 6. 30:02 — g-compare too fast + exits 9s early
Comp 1788–1814s, narration a6-s2d runs to 1823s. Slow the three bar reveals to land on their
spoken names (Carolinas / Woodward / Tri-State in `audio/a6-s2d.words.json`), and extend the
comp timeline to cover the narration (~35s) so the window stops cutting away early.

### 7. 32:00 / 32:06 — g-prep exits early + "MINUTES ARE ENOUGH" block
Comp 1906–1928s, narration a6-s3d runs to 1941s (13s uncovered tail goes to TAIL stills now).
- Owner: the closing "THE THREE RULES / MINUTES ARE ENOUGH — IF YOU USE THEM" section does
  not align with the TTS. Read `audio/a6-s3d.words.json`: if the narration never says
  anything like it, DELETE that section (elements + tweens) — it is exactly the fluff class.
- Re-time the three rule reveals to the spoken rules; extend the comp to cover the narration
  window so it doesn't exit under a talking voice.

### 8. Screenshot (g-track-7 "THE COMPLETE TRACK") — label spacing
Halo landed but spacing is still wrong: labels sit ON dots and on each other
(Murphysboro⨯West Frankfort, Ellington⨯Annapolis, De Soto near its dot, Parrish⨯Crossville).
Fix on ALL g-track-* comps: move each town label ≥18px clear of its dot and stagger the
alternation (above-line vs below-line) so neighbouring labels never share a side when closer
than ~150px horizontally. This is per-label x/y attribute surgery in the SVG — verify with
graphics_qc (text-collision detector) after; if the detector doesn't cover SVG <text>,
eyeball ONE staged frame per track comp (subagent), not a sweep.

## After all edits
1. `python3 scripts/build_ep3.py` (regenerates index.html; version check prints at compose).
2. Re-measure comp durations if any timeline grew (graphics_qc writes `_durations.json`),
   then REBUILD index.html again so windows pick up new durations.
3. Full static suite green: sweep, blank_scan, beat_density, graphics_qc, lint_timeline
   (+coverage), narration_picture_check.
4. Commit per logical fix; push.
5. **FINAL RENDER** — full quality this time (owner authorized if gates pass):
   `scripts\render.cmd ep3-tristate full ep3-tristate-v5-final` — launch in a detached
   console (`cmd /c start` via WMI Create, the proven pattern), NOT via harness-tracked
   foreground, NEVER poll with interruptible wait-loops. ~75 min on this box at 2 workers.
   Progress via 5-min /loop cron, single `cat` reads only.
6. On completion: verify_render.sh + build_srt.py + `master_deliverables.py` (−14 LUFS
   master + SRT, per repo CLAUDE.md step 7) and report paths.

## Traps (inherited — still binding)
- build_ep3.py owns generated text/quotes/sfx; compositions own graphic internals.
- Foreground Playwright/node dies — run_in_background always. Don't pipe background output
  through grep (buffers, showed empty).
- ^C propagates into same-console children — detached console launch only.
- media_budget refusal at launch = busy box (kill leaked ms-playwright chromium, check CPU),
  not a code bug. Don't touch thresholds.
- Blackdetect on dark motion graphics = false positive; the coverage gate in lint_timeline
  is the truth for real holes.
- Marker file may come back empty from the start-detached console — mp4 + log success line
  is the real completion signal.
