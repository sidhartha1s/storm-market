Host: id=g-a1s18-list file=compositions/g-a1s18-list.html start=277.48 (timeline-map.md table 1; the mount in index.html wins) duration=11.68 s (wavs 11.49 s plus their gaps) track=2

# g-a1s18-list · A1-S18, A1-S19 · 5:43 PM, one message, one telephone list (wave 2, list family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 3, 4, 5, 8 and 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3e row PT-07.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the photograph shows, never the town the voice is talking about (rule 5). This is the first of the three uses of the teletype room photograph in A1 to Z1 (rule 9). Typed sheets use two type sizes by design (rule 10).
**Spoken (A1-S18):** "At five forty three, South Bend issued a warning of its own. Now there was one message, with one telephone list to cross."
**Spoken (A1-S19):** "How long does a warning take to cross that list?"
**One look:** the clock at 5:43, the typed list beside it, and the minute hand beginning to move.

## 0. What this graphic claims
At 5:43 PM the South Bend Weather Bureau issued its own warning. That one message now had a telephone list to cross, and the open question is how long that takes. The picture does not say how long: nothing on the list is ticked, lit or timed.

## 1. Source
- `edit_script.md` A1-S18, Rows [A6; survey printed p. 39; study printed p. 13: "The first actual tornado warning for parts of northern Indiana was issued by the South Bend Weather Bureau at 5:43 p.m."]. A1-S19: the act's exit question, no row.
- The list: the study's sentence on printed p. 14, set as design sheet section 5 ("Those organizations notified included ..."). It is not the whole warning system and not a call order.
- Ground: `media/stills/a3-teletype-operators.jpg` (1370 x 1080, inventory row A3): the Weather Bureau Communications Center about 1955, two operators from behind. Not South Bend, not 1965.

## 2. Datum, scale, orientation
The list sheet keeps the world coordinates of design sheet section 5 and one camera transform on its world container (origin top left; screen = s x world + t). This comp adds one camera state, used by both list comps of wave 2:
| State | s | tx | ty | Sheet on screen | Row text | Eyebrow | Title |
|---|---|---|---|---|---|---|---|
| Beside | 1.1 | 669.6 | 44 | x 740 to 1576, y 110 to 759 | 28.6 px | 20.9 px | 33 px |
Row centres on screen in this state, slots 1 to 9: 279.4, 332.2, 385.0, 437.8, 490.6, 543.4, 596.2, 649.0, 701.8. Row text left edge 834.6. The sheet's right edge is x 1576 and its bottom y 759: it passes left of the presenter corner (x >= 1600, y >= 680).
Clock angles, clockwise from 12: 5:43 is hour 171.5 degrees, minute 258 degrees (design sheet section 8). One minute is 6 degrees of the minute hand and 0.5 degrees of the hour hand.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | `<img src="media/stills/a3-teletype-operators.jpg">` at cover (1.4015 times), `object-position:50% 40%`, scale 1.00 to 1.05 over the whole comp, `ease:"none"`. On from frame 0 |
| Scrim | full frame, `rgba(3,5,8,0.45)`; it deepens to `rgba(2,4,6,0.68)` as the paper arrives (the two values of `compositions/g-t1s3-list.html`) |
| Clock stamp | design sheet section 8, as built in `compositions/g-t1s2-warning.html` (`.warn-stamp`): glass card left 96, top 96, 590 x 200; eyebrow `WEATHER BUREAU`, time `5:43 PM`, place `South Bend, Indiana`; hour hand 171.5, minute hand 258 |
| List sheet | design sheet section 5, all nine slots, in the Beside state: sheet x 740 to 1576, y 110 to 759. Eyebrow `SOUTH BEND WEATHER BUREAU · BY TELEPHONE`, title `Organizations notified included:`, the telephone glyph, the rule, eight rows in the **Plain** state (all eight in Caption dark), the ninth slot with its row rule and nothing on it. No tick, no band, no red line, no cursor in this comp |
| Photo caption | credit corner, left 96, bottom 60, source-line type: `Weather Bureau Communications Center, about 1955 · NOAA`. On from frame 0 until the list arrives |
| List source | same place and type: `Disaster Research Center, 1966, p. 14`. It replaces the caption when the list lands (one line in the corner at a time) |
Rows, exact, top to bottom: `State Police` · `Sheriffs' Departments` · `City Police Departments` · `Indiana and Michigan Electric Company` · `Red Cross` · `Specified radio and TV stations` · `Flying services` · `Airlines`.

## 4. Must be true in the picture
1. The clock reads 5:43 PM when the time is said: hour hand between 5 and 6, minute hand between 8 and 9.
2. "South Bend, Indiana" is on the glass stamp, never bare on the photograph. The photograph carries its own caption before the list arrives.
3. The list has eight typed rows in the study's order and a ninth slot with only its rule. No number, letter, arrow, tick or tick box on or beside any row; no row count; the title is `Organizations notified included:`.
4. All eight rows are in the same ink. No row is lit, marked or dimmed: the picture does not say who was called or when.
5. In A1-S19 the minute hand moves forward by no more than one minute (258 to 264 degrees) and is still moving on the last frame. The printed time stays `5:43 PM`; no second time, no arc and no duration is shown (the count belongs to A2-S5).
6. The stamp and the sheet do not overlap (stamp ends x 686, sheet starts x 740).
7. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680, including while the sheet slides in.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `5:43 PM` · `South Bend, Indiana` · `SOUTH BEND WEATHER BUREAU · BY TELEPHONE` · `Organizations notified included:` · the eight rows of section 3 · `Weather Bureau Communications Center, about 1955 · NOAA` · `Disaster Research Center, 1966, p. 14`.
Cue words and times are from `audio/a1-s18.words.json` and `audio/a1-s19.words.json` as they stood on 12 Oct 26 at 18:00, after the voice conversion's re-transcription. Wavs: A1-S18 8.402 s, A1-S19 3.083 s; the comp is their sum, 11.49 s. "t from comp start" for A1-S19 is 8.402 plus the time in the segment; gaps from `mg_specs/timeline-map.md` (not on disk yet) are added to every A1-S19 row. The transcriber writes "five forty three" as one word, `543`. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S18 | 0 | At | 0.00 | 0.00 | first frame: the photograph under its scrim, the photo caption on. The push starts (11.49 s) |
| 1 | A1-S18 | 1 | 543 | 0.52 | 0.11 | the stamp slides in (`x:-660` to 0 with the fade, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees, 228 to 258 (0.5 s, from 0.72) |
| 2 | A1-S18 | 2 | South | 1.40 | 0.99 | the place line `South Bend, Indiana` rises inside the stamp (`y:16` to 0, 0.3 s) |
| 3 | A1-S18 | 10 | Now | 4.68 | 4.27 | the scrim deepens (0.7 s) |
| 4 | A1-S18 | 17 | telephone | 6.68 | 6.27 | the list sheet slides in from the right in the Beside state (world `x` from tx + 900 to tx, 0.7 s, power3.out; it lands at 7.38), rows already typed; the photo caption gives way to the list source (0.3 s cross fade) |
| 5 | A1-S19 | 0 | How | 0.00 | 8.48 | hold on the clock and the list |
| 6 | A1-S19 | 1 | long | 0.58 | 8.62 | the minute hand starts to move: 258 to 264 degrees over 2.50 s, `power1.in`, ending on the comp's last frame (11.485); the hour hand moves 171.5 to 172 with it |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.
Entrance check for step 4: at its start the sheet's left edge is at x 1640 and its bottom at y 759, inside the corner zone for the first frames of the slide. Give the slide a lead on y as `g-t1s3-list` does: start the sheet 120 px high (world `y` from ty - 120 to ty, `power3.out`) so its bottom edge is above y 680 until its right edge is left of x 1600, and read the first three frames of the slide.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a1s18-list.html` is the only file the builder writes; `data-composition-id="g-a1s18-list"`; id prefix `l43-`; root `<div id="l43-root" ...>` styled through `#l43-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the built `compositions/g-t1s3-list.html` (the sheet, its world, its camera transform, the photograph ground and scrim) and `compositions/g-t1s2-warning.html` (the clock stamp and its hands). No wave 1 base is needed. `g-a2s21-list` (same wave) copies the Beside state from this brief; the two builders agree the state's numbers from section 2, not from each other's file.
**Assets mounted (paths from the episode folder):**
- `media/stills/a3-teletype-operators.jpg` (1370 x 1080 px).
- `media/drawings/telephone.svg` (viewBox -6 -58 102 106), the list header glyph at 60 px wide as in `g-t1s3-list`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s18-list`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type flags typed sheets by design (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the Beside state (s 1.1, tx 669.6, ty 44) and the nine row centres are computed by a script from design sheet section 5 and stated in the receipt. Line 7: the place and time are on the glass stamp; the photograph's caption names the photograph.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): photograph, scrim, caption; no stamp, no paper. Then one settled frame per cue: 1.30 (stamp in, hands at 5:43), 2.00 (place line), 5.60 (deeper scrim, still no paper), 6.80 and 6.90 (the slide's first frames: nothing in the corner), 7.60 (sheet landed, eight plain rows, list source in the corner), 8.60 (hold), 11.40 (minute hand past 258, time still `5:43 PM`).
