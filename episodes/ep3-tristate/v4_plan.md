# ep3-tristate v4 — single-pass fix plan (owner QC of v3 draft, 2026-07-29)

Executor: Opus (same session, main thread — NOT a subagent). Planner: Fable.
Goal: ship `ep3-tristate-v3-draft` → **v4 draft** in ONE pass. Owner spent 40 min QC-ing v3; do not waste it.

## Hard constraints (owner, this round)
- **Single pass.** Fix everything below, run static gates, ONE render at the end. Never render to check.
- **No frame QC for deterministic items** — read the code. Render a SINGLE frame only where judgment
  genuinely needs eyes (spacing/layout: items 3, 9, 13). Snapshot method per CLAUDE.md 6d.
- **Text volume is AI reasoning, NOT code.** Do not write any script that counts words or gates text.
  (Owner, re 18:24: "It shouldn't be code. It should be AI's reasoning. Do not put code headache.")
- **Minimal new code.** Only additions to main beyond owner's list: owed items A/B below + this plan
  + LEARNINGS append. Anything else = stop and ask.
- Source of truth: `compositions/*.html` + `scripts/build_ep3.py` → rebuild `index.html` → gates.
  Never hand-edit index.html only.
- v3 render verdicts: the 3 long blackdetect spans = FALSE POSITIVES (graphics in motion) — ignore.
  freezedetect 6:17 / 6:32 = real but owner says don't flag/fix this round.

## The global text law (applies to EVERY graphic — owner's core feedback)
1. **Remove ALL "eyebrow" texts** (small kicker/label lines above headings) across the video.
2. **Exception — "subheaders" that carry real data stay.** Reference: 7:37 (time-in-town,
   buildings-destroyed) and 28:12 (subheader-year-text-below format) are CORRECT — keep those.
   Also 18:24-class story/timeline graphics keep city names, count-ups, times, data.
3. Fluff sentences that don't add context to THIS beat: delete. Repeated dates/places/facts within
   one frame: delete duplicates. Recaps of previous segments ("the word tornado was banned…" shown
   again later): delete.
4. Text must be match-cut to the TTS or it goes. "No one's gonna read if it is not matchcut and
   TTS friendly." When motion already conveys the story, keep graphics, strip text to minimum.
5. Big numbers as NUMERALS not words ("$16.5 million", not "sixteen point five million" spelled out).
   (Narration TTS text stays spelled out — this rule is on-screen text only.)

Sweep method: walk all 38 comps + build_ep3.py generated cards; for each text node ask
"does the TTS say this right now / is it data or fluff?" — delete fluff. This is a reasoning
sweep over the HTML, not a regex.

## Timestamp map — how to locate each item
mm:ss → seconds → find window in index.html (`data-start`/`data-duration` on tracks 1/2) →
composition id → `compositions/<id>.html`. Use `renders/ep3-tristate-v3-draft.srt` to confirm which
narration line plays there. v3 timeline == current tree (no edits since render).

## Work items (todo — check off each)

### Act 1 area
- [ ] **0:30** — TTS sentence ends, then 4s awkward slow-zoom before next scene. Kill the dead
      zoom: fade to black / cut when the sentence ends. "I would hit esc."
- [ ] **0:41** — cluttered graphic, text all over, not paced per story. Motion good — keep motion,
      strip text per global law. Pace what remains to the narration beats.
- [ ] **Opening Washington/ban graphics segment (through ~0:50+)** — restructure:
      show Washington a few seconds → year count-up animation → at "forecasters were forbidden to
      use…" show the word "TORNADO" and bar/strike it off → hold till beat ends. REMOVE all other
      text (the 200-word typing paragraphs die).
- [ ] **Forecast graphic (owner screenshot, ~2min area)** — currently ~35-40 words: full Chicago
      district forecast quote, date shown twice, "Illinois" repeated, banned-word recap, eyebrows
      everywhere. Reduce to essentials: **"rains and strong shifting winds"** + what did NOT exist:
      **"no watches · no sirens · no radar"** (the five-words idea). Nothing else.
- [ ] **Finley segment** — image order now: finley-1, building, finley-2.
      New order: finley-1, finley-2, tornado image, one more Finley. REMOVE the building image.
      (Flag F1: if only two Finley portraits exist in media/, close on a reuse of finley-1 —
      no-repeat rule needs `data-callback` — or end on the tornado image; pick and note.)
- [ ] **2:41** — too much empty space + eyebrows. Put b-roll behind; card becomes right-side panel
      on blackish translucent bg, ~30% width — the ep2 7:37 pattern. (Single-frame check OK.)
- [ ] **4:01** — line-wave animation: SLOW DOWN the wave speed (users will skip). Remove eyebrows.
      Low-prio: kill the end freeze-frame where the yellow semicircle line rotates alone.
- [ ] **4:28** — keep (good taste); strip stray texts only.
- [ ] 5:30 — good. No change.

### Mid
- [ ] **8:53** — layout scatter: elements at 1 o'clock, 7 o'clock, middle simultaneously; eye can't
      scan. Restructure to one reading flow. (Single-frame check OK.)
      AND: verify the "12 poles destroyed" stat against sources/provenance. Unverifiable → delete
      the stat. (Flag F2.)
- [ ] 9:15, 10:12 quote, 13:57 — good. No change.
- [ ] **17:55** — final graphics frame: declutter text.
- [ ] 18:24 — GOOD, exception class (story/timeline). Keep city names/count-ups/times. No change.
- [ ] **19:37** — too much text. Strip per law.

### Timeline graphics (all instances)
- [ ] **City/town labels overlap the white dot and red lines — fix offset on ALL timeline segments.**

### Act 5-6 area
- [ ] **23:19** — a man's photo appears TWICE around here. SRT verified (cues 471-478): narration
      is Red Cross relief, tent cities, 7000 homeless families — NO named man anywhere. Owner call:
      he shouldn't appear at all. REMOVE both instances (the img window [1397-1405s] over
      g-panel-nonet, + find the second occurrence nearby); fill with relief/tent-city-aligned
      material. Name him from provenance.csv in the report for the record.
- [ ] **25:50** — money graphic rebuild: eyebrow ("the bill, March 1925") delete. Show
      **$16.5 million** (numerals) + small "in 1925 money" → then **$3 billion in today's money**.
      Delete the duplicated "in 1925 money" text-line and the two irrelevant sentences that vanish
      before readable. One idea, once.
- [ ] **27:40 + next** — decent. Keep 28:12's subheader-year-text format. Remove h1/h2 eyebrows.
- [ ] **28:42, 29:20** — remove clutter text.
- [ ] **29:30, 30:10** — good; match-cut these segments to the TTS beats.
- [ ] **30:53** — remove the "1972 PD" text; declutter.
- [ ] **31:28** — declutter (segment itself nice).
- [ ] **32:03** — declutter.
- [ ] 32:38 — good. No change.

### Owed items → land on main (owner: "do 2 and 3 to main")
- [ ] **A. Assembled-timeline black check, pre-render** (was owed-2). blank_scan checks comps in
      isolation; the seams are unchecked. Extend `blank_scan.mjs` (or minimal sibling) to load the
      ASSEMBLED index.html and sample ±1s around every picture-track window boundary. IMPORTANT:
      v3 proved luma-only blackdetect false-positives on dark graphics in motion — sample 2-3
      frames per seam and fail only if ALL are black (motion = not blank). Keep it small.
- [ ] **B. npm version check out of render gate → production start** (was owed-3). Strip the
      `npm view` block from `render_preflight.py` (pin-drift check STAYS — offline, render-time
      invariant). Enforce at production start: check runs when episode work begins (first
      production script — TTS/build — refuses stale-pin-vs-published with override flag  `--pin-ok`
      only after a human decision; plus docs line in CLAUDE.md pointing at the gate). No prose-only rule.

### After all edits
- [ ] `python3 scripts/build_ep3.py` → regenerate index.html.
- [ ] Full static suite green: sweep_episode, blank_scan (+new seam check), beat_density,
      graphics_qc, lint_timeline, narration_picture_check, media_budget (via render_preflight).
- [ ] Single-frame snapshots ONLY for: 0:41 rebuild, 2:41 panel, 8:53 layout, forecast card,
      25:50 money card (subagent reads frames, text verdict back).
- [ ] Commit per logical fix; push; LEARNINGS.md append (text law + this round's misses).
- [ ] ONE render: v4 draft. Launch = owner's `!` method (proven alive) or WMI-detached; marker +
      3-min /loop cron progress; verify_render.sh + SRT; deliver path.

## Flags for owner (decisions/notes, not blockers)
- **F1**: "one more finley" at segment end — if no third Finley portrait exists, choose reuse
  (needs data-callback) vs ending on tornado image. Executor picks, reports which.
- **F2**: 8:53 "12 poles" — will verify; if unverifiable, stat deleted (not softened).
- **F3**: 23:19 duplicate man — will name him from provenance and report what replaced him.
- **F4**: freeze at 6:17/6:32 real but explicitly not fixed this round (owner's call) — logged, not touched.
- **F5**: nothing new lands on main beyond: this plan file, the QC edits above, owed A + B,
  LEARNINGS append. If execution reveals a needed extra (e.g. a missing asset), STOP and ask.
