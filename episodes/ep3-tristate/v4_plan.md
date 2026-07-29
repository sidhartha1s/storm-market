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

## Timestamp → composition map (pre-computed, v3 timeline == current tree)
```
 0:30 (  30s): asset window [26-35s]        <- the 4s dead slow-zoom
 0:41 (  41s): g-wordban   [35-61s]         <- clutter + Washington/ban rebuild (also 0:50)
 2:00 ( 120s): g-forecast  [115-137s]       <- the 35-40-word forecast card (owner screenshot)
 2:41 ( 161s): g-sources   [139-170s]       <- empty space, right-panel ep2 style
 4:01 ( 241s): g-metmap    [211-247s]       <- slow the line-wave; end freeze low-prio
 4:28 ( 268s): g-scale     [247-275s]       <- keep, strip texts
 5:30 ( 330s): g-lone      [316-343s]       <- good, no change
 7:37 ( 457s): g-panel-annapolis [437-460s] <- REFERENCE pattern (subheaders stay)
 8:53 ( 533s): g-wires     [498-535s]       <- layout scatter + "12 poles" verify
17:55 (1075s): g-baro      [1062-1088s]     <- declutter final frame
18:24 (1104s): g-track-5   [1095-1106s]     <- REFERENCE exception class, no change
19:37 (1177s): g-panel-griffin [1154-1179s] <- too much text
23:19 (1399s): img [1397-1405s] over g-panel-nonet [1397-1421s] <- remove the man, both uses
25:50 (1550s): g-panel-cost [1537-1563s]    <- money card rebuild
27:40 (1660s): g-wordban2  [1640-1663s]     <- decent, remove h1/h2 eyebrows
28:12 (1692s): g-timeline  [1663-1697s]     <- keep subheader-year format; fix label overlap
28:42 (1722s): g-family    [1705-1745s]     <- remove clutter
29:20+29:30 (1760/1770s): g-remeasure [1745-1774s] <- declutter + match-cut
30:10 (1810s): g-compare   [1791-1817s]     <- match-cut
30:53 (1853s): g-fujita    [1829-1874s]     <- remove "1972 PD", declutter
31:28 (1888s): g-modern    [1874-1903s]     <- declutter
32:03 (1923s): g-prep      [1909-1931s]     <- declutter
32:38 (1958s): g-centennial [1945-1973s]    <- good, no change
Timeline label-overlap fix: g-timeline + g-track-1/2/3/5/7 (the track family).
```

## Eyebrow sweep handle (deterministic worklist)
`grep -l eyebrow compositions/*.html` → 36 of 38 comps, ~2 hits each (CSS rule + usage).
That is the sweep list. Judgment per hit stays AI (subheader-with-data stays, fluff dies) — but
nothing gets missed. After the sweep, the same grep returning only intentional survivors is the check.

## Executor traps (this session's scars — read before touching anything)
1. `build_ep3.py` REGENERATES index.html. Generated cards' text lives in build_ep3.py, comp text
   in compositions/*.html. Find which owns a string before editing (`grep` both). Never edit
   index.html by hand and call it fixed.
2. JS/WAAPI + GSAP only — CSS @keyframes silently disables fast-capture.
3. Comp `duration` attr must equal the GSAP timeline end (g-close drift lesson) — check after
   trimming any animation.
4. Auto-commit hook fires per Edit; Bash heredoc writes DON'T auto-commit — `git status` before push.
5. `python3` never `python`; PYTHONUTF8=1 on anything that prints unicode.
6. node/Playwright gates: `run_in_background: true` always — foreground timeout kills them.
7. NEVER poll the render with interruptible background shells — ^C propagates into the detached
   render and kills it (killed 2 launches today). Progress = /loop cron only, direct Bash reads.
8. Render launch: owner `!` method proven, or WMI Win32_Process.Create. Empty/absent log =
   script never started ([start] stamp is first write). Verify liveness by COMMAND LINE match
   on 'hyperframes render', never process counts.
9. media_budget spawn check is load-sensitive: refusal at ~0.4-0.6s means the BOX is busy
   (other Claude sessions/browsers), not a code bug. Quiet the box, don't touch the threshold.
10. Word-level match-cut timings: audio/<seg>.words.json (nx id = filename minus dashes).
11. Don't touch ep2. Don't delete render artifacts (v3 mp4 stays until owner says).
12. Do NOT relaunch a failed render without owner permission — standing gate.

## Flags for owner (decisions/notes, not blockers)
- **F1**: "one more finley" at segment end — if no third Finley portrait exists, choose reuse
  (needs data-callback) vs ending on tornado image. Executor picks, reports which.
- **F2**: 8:53 "12 poles" — will verify; if unverifiable, stat deleted (not softened).
- **F3**: 23:19 man — RESOLVED by owner + SRT check: not in narration, remove both uses entirely;
  executor names him from provenance and reports the replacement fill.
- **F4**: freeze at 6:17/6:32 real but explicitly not fixed this round (owner's call) — logged, not touched.
- **F5**: nothing new lands on main beyond: this plan file, the QC edits above, owed A + B,
  LEARNINGS append. If execution reveals a needed extra (e.g. a missing asset), STOP and ask.
