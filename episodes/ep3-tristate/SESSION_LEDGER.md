# ep3 v3 — every mistake I made this session, and its fix

Ordered worst first. "Fix" means a durable change in code or process, not a one-run patch.

---

## A. Process failures

### A1. I used renders as a diagnostic tool
**Nine render attempts.** Four completed, one crashed, four I killed. Runs 7, 8 and 9 each died
to a defect I could have found from the code before starting them — I rendered, thought of a
new check, killed it, rendered again.

**Fix:** every check I invented reactively is now a script that runs in seconds. Static gates
are exhausted first; the render is the last step.

| script | catches |
|---|---|
| `scripts/sweep_episode.py` | picture coverage (black), track overlap, adjacent duplicate cuts, reuse ceiling, missing media, unmounted/missing compositions, graphic window vs its own timeline, over-long stills |
| `scripts/blank_scan.mjs` | seeks every composition at 0.25s and measures on-screen ink — a pre-render blackdetect |
| `scripts/beat_density.py` | largest motionless interval per composition |
| `scripts/clip_report.py` | the full window ledger |

### A2. I asked you to re-point your own timestamps
You gave notes against the v2 draft. I said the v3 timeline had moved and asked you to
re-point 5:48 and 28:04. That was my job. The v2 draft was built from a commit still in the
tree; `git show <sha>:episodes/<slug>/index.html` into a temp dir plus the window ledger
answers it in one command.

Doing it showed **5:16 and 5:48 were the same defect** (one 33.4s stock cloud clip covering a
whole passage) and that **28:04 was a 0.904-aspect portrait stretched full-frame for 163
seconds**.

**Fix:** rule recorded — owner timestamps against an old cut get mapped by me, from git.

### A3. No task list until you demanded one
I carried the work in prose and rediscovered items after each compaction.
**Fix:** task list is live; every open item is a tracked task, not a paragraph.

### A4. I answered the wrong question, twice
You asked for the image-gen prompt for **the map**. I produced three person-portrait prompts
for a different open item. **Fix:** re-read the numbered item before answering a numbered ask.

### A5. I claimed things from my own change log instead of the artifact
Several "fixed" claims early in the round traced to my shot map, not to the built file.
**Fix:** every claim in `v3_review_response.md` cites the code or a measurement.

---

## B. Defects I shipped into the draft you reviewed

### B1. 63 cuts to pure black
The scheduler advanced by `seg_dur + GAP` but only covered `seg_dur` with picture windows, so
the 0.75s breath between narration segments had nothing on the picture tracks. Measured:
**81 black spans, 63 at segment boundaries.** ep2 has 2, ep1 has 6.
**Fix:** `close_picture_gaps()` holds the outgoing frame through the breath. Now 0.

### B2. 15.9 seconds of black at the end
A redundant `+14s` credits tail after `g-close` had already faded out.
**My first attempt made it worse** — I extended `g-close` to cover the gap, which just *held*
the black. That is a mask, not a fix. **Fix:** tail cut to 1.0s.

### B3. A whole segment carried by one 33.4s stock cloud clip
`a1-s4d` — "not a squall line / one lone supercell / 400 miles / seven hours" — the episode's
most spatial passage, played over generic rolling clouds. **Fix:** `g-lone`, a map.

### B4. Narration said 2025, picture said 1925
`a6-s3b` narrates the March 2025 centennial over 1925 wreckage photographs.
**Fix:** `g-centennial`, a designed card on the map plate. No fabricated footage.

### B5. A 0.904-aspect portrait stretched full-frame for 163 seconds
**Fix:** contained in a bordered frame inside `g-fujita`.

### B6. Four stills pillarboxed for no reason
A blanket `fit="contain"` put photos at 1.58–1.75 aspect inside blurred bars.
**Fix:** letterbox on the image's own aspect; papers exempt (cropping a front page cuts text).

---

## C. Bugs I introduced while fixing things

### C1. SVG dasharray shorter than its line — three times
A dash pattern shorter than the path paints the overhang as a second dash, **visible from
frame one**. Route: 1360 vs a true 1377.6 → a red mark sat in Indiana for eleven seconds.
Strike line: 1040 vs 1041.4. Then `"{rlen:.0f}"` rounded *down*.
**Fix:** `_ceil()` — compute the length, `ceil() + 1`. Never type a dash length.

### C2. A label outside the group it described
`sqlab` sat outside `<g id="squall">`, so "A SQUALL LINE · MANY STORMS" outlived the cells it
named — visible to the end of the graphic. **Fix:** moved inside the group.

### C3. `motionPath` is not in the bundled GSAP
**Fix:** per-leg `attr:{cx,cy}` tweens timed to each leg's length.

### C4. Chromium will not parse a page saved as `.html.tmp`
Every composition reported "no timeline". **Fix:** `.html` + `.gitignore`.

### C5. My first coverage report invented gaps and missed 32 windows
It parsed the ken-burns array and comp hosts, but `<video>` clips carry timing on the element.
**Fix:** enumerate by attribute, never by animation bookkeeping.

### C6. Temp pages committed to the repo
The QC helpers staged files next to the compositions. **Fix:** `.gitignore` + write at the
episode root.

### C7. Retired a graphic without retiring its generator entry
`g-panel-lone` became authored-but-unmounted. **Fix:** generator entry, `_durations.json` key
and file all go together — the sweep now catches it.

### C8. Bash ate backslashes in a quoted heredoc — again
`\n` became a real newline inside f-strings; the module stopped parsing.
**Fix:** patch scripts go through the Write tool, never a heredoc.

---

## D. The render crash (run 6)

`ffprobe deadline with code 0` at 10% of `video_extract`. All 18 video assets probed clean.
Cause: one **365 MB, 3840×2160** stock clip feeding 12.9s of a 1080p composition — 10× every
other asset. **Fix:** transcoded to 1080p, 365 → 54 MB. Retrying would have hit it again.
Rule: cap source assets at the composition's own resolution before wiring them.

---

## E. Your rules, recorded

**Renders**
- Never burn repeated renders to find defects a script can find. Exhaust static gates, render once.
- A render is the last step, not a diagnostic tool.

**QC**
- QC the **code**, not a frame sweep. "How can I have garbled text? in HTML."
- A 105-image frame sweep is not a QC method for graphics.
- Look at the actual artifact before any quality verdict.

**Graphics**
- Motion graphics must have motion. No frozen full-frame holds for 30s.
- Match ep2's anatomy — check it, don't assume it.
- **Do not touch ep2. It is shipped.**
- Show, don't make the viewer "look at stuff". Put it in the middle or across the RHS.
- A map beats b-roll for any spatial claim.
- Ambiguous labels are defects ("what they knew", an unexplained cone).

**Pacing**
- Segments and clips do not deserve the lengths they were getting. Cut for retention.

**Working method**
- Triage my own issues. Keep a task list.
- Do not ask you to re-derive things I can derive.
- The defects you name are a sample, not the set. Dig for the rest.
