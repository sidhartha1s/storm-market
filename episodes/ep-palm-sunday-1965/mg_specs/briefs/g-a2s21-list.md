Host: id=g-a2s21-list file=compositions/g-a2s21-list.html start=(timeline-map.md) duration=9.00 s plus gaps from timeline-map.md track=2

# g-a2s21-list · A2-S21 · the blank row, then 6:50 PM and a blank sheet (wave 2, list family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 3, 4, 5, 8, 9 and 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3e row PT-07.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the photograph shows (rule 5). This is the second of the three uses of the teletype room photograph in A1 to Z1 (rule 9). Typed sheets use two type sizes by design (rule 10).
**Spoken (A2-S21):** "Whose job it was to tell a family is still open. And at six fifty, the South Bend desk typed a message no warning office wants to send."
**One look:** the list with its empty last row and a blinking cursor; then the clock at 6:50 and a blank sheet where the message will come.

## 0. What this graphic claims
The list still has no row for whoever tells a family: the question of the hook is open. At 6:50 PM the South Bend office typed a message; what it said is held for the next segment, so the paper is blank.

## 1. Source
- `edit_script.md` A2-S21, Rows (the question of T1-S5, restated) and [A10; survey printed p. 40], with the note that loop L7 (what the 6:50 message said) is paid in A3-S1.
- The list: the study's sentence on printed p. 14, set as design sheet section 5. The blank ninth row is ours: it marks that the sentence names no one whose job was to tell a family. It is never a claim that the row is missing from the page.
- The 6:50 PM entry is on survey printed p. 40 (`media/docs/survey-p40-650pm-crop.png`, 1460 x 240). **It is not mounted here**: no word of it may show before A3-S1.
- Ground: `media/stills/a3-teletype-operators.jpg` (1370 x 1080, inventory row A3): the Weather Bureau Communications Center about 1955. Not South Bend, not 1965.

## 2. Datum, scale, orientation
The list sheet keeps the world coordinates of design sheet section 5 and one camera transform (origin top left; screen = s x world + t), in the Beside state of `mg_specs/briefs/g-a1s18-list.md`:
| State | s | tx | ty | Sheet on screen | Row text | Eyebrow |
|---|---|---|---|---|---|---|
| Beside | 1.1 | 669.6 | 44 | x 740 to 1576, y 110 to 759 | 28.6 px | 20.9 px |
Row centres on screen, slots 1 to 9: 279.4, 332.2, 385.0, 437.8, 490.6, 543.4, 596.2, 649.0, 701.8. The cursor (world x 150, 14 x 28 px on the ninth row's centre line) is on screen at left 834.6, top 686.4, 15.4 x 30.8 px.
Clock angles, clockwise from 12: 6:50 is hour 205 degrees, minute 300 degrees.
The blank sheet takes the box the next comp's document card will take (`g-a3s01-message`, wave 3): left 96, top 320, 1480 x 260, which is the 1460 x 240 crop of the 6:50 entry plus the 10 px border, under the clock stamp as in `compositions/g-t1s2-warning.html`. This box is a shared number with that comp.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | `<img src="media/stills/a3-teletype-operators.jpg">` at cover (1.4015 times), `object-position:50% 40%`, scale 1.00 to 1.04 over the whole comp, `ease:"none"`. On from frame 0 |
| Scrim | full frame, `rgba(2,4,6,0.68)` from frame 0 (paper is on screen from the first frame) |
| List sheet | design sheet section 5 in the Beside state: sheet x 740 to 1576, y 110 to 759, on from frame 0. Eyebrow, title `Organizations notified included:`, telephone glyph, rule, eight rows **Plain** (Caption dark). The ninth slot: its row rule and the cursor block (Caption dark), nothing typed |
| List source | credit corner, left 96, bottom 60, source-line type: `Disaster Research Center, 1966, p. 14`, on from frame 0 while the list is on |
| Clock stamp | design sheet section 8, as built in `compositions/g-t1s2-warning.html`: glass card left 96, top 96, 590 x 200; eyebrow `WEATHER BUREAU`, time `6:50 PM`, place `South Bend, Indiana`; hour hand 205, minute hand 300 |
| Blank sheet | Beige polaroid, left 96, top 320, 1480 x 260 (right 1576, bottom 580), the shadow of design sheet section 9, no border line, nothing on it: no rule, no heading, no cursor, no type |
| Photo caption | same corner and type as the list source: `Weather Bureau Communications Center, about 1955 · NOAA`. It replaces the list source when the list leaves |
Rows, exact, top to bottom: `State Police` · `Sheriffs' Departments` · `City Police Departments` · `Indiana and Michigan Electric Company` · `Red Cross` · `Specified radio and TV stations` · `Flying services` · `Airlines`.

## 4. Must be true in the picture
1. The ninth row is empty: a rule and a cursor, no word, no dash, no question mark. The cursor never types.
2. The eight rows are in one ink, in the study's order, with no number, tick, tick box, band or red line. The title is `Organizations notified included:`; no row count.
3. The clock reads 6:50 PM when the time is said: hour hand just short of 7, minute hand on 10.
4. **The sheet that slides in is blank.** No word of the 6:50 message, no time, no heading and no page number is on it. The stamp's `6:50 PM` is the only time on screen.
5. The list is gone before the blank sheet arrives: the two papers never overlap and never share a settled frame.
6. "South Bend, Indiana" is on the glass stamp, never bare on the photograph; the photograph's own caption shows once the list source has left.
7. The blank sheet's box is left 96, top 320, 1480 x 260, within 2 px (the next comp's page lands on it).
8. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `SOUTH BEND WEATHER BUREAU · BY TELEPHONE` · `Organizations notified included:` · the eight rows of section 3 · `Disaster Research Center, 1966, p. 14` · `WEATHER BUREAU` · `6:50 PM` · `South Bend, Indiana` · `Weather Bureau Communications Center, about 1955 · NOAA`.
Cue words and times are from `audio/a2-s21.words.json` as it stood on 12 Oct 26 at 18:00, after the voice conversion's re-transcription (wav 8.998 s). The comp holds one segment, so the two time columns are equal; if `mg_specs/timeline-map.md` (not on disk yet) puts a gap before the segment, add it to every row. The transcriber writes "six fifty" as `6` and `.50,`. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S21 | 0 | Whose | 0.00 | 0.00 | first frame: photograph, scrim, the list sheet with eight plain rows, list source on. The ninth slot shows nothing yet. The push starts (9.00 s) |
| 1 | A2-S21 | 5 | tell | 1.50 | 1.50 | the ninth row's rule draws (`scaleX` 0 to 1 from the left, 0.3 s); the cursor comes on at 1.80 and blinks, on 0.5 s, off 0.5 s, four times (finite) |
| 2 | A2-S21 | 13 | 6 | 3.82 | 3.82 | the stamp slides in (`x:-660` to 0 with the fade, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees, 270 to 300 (0.5 s, from 4.02), landing inside word 14 `.50,` (4.04) |
| 3 | A2-S21 | 16 | South | 4.98 | 4.98 | the place line `South Bend, Indiana` rises inside the stamp (`y:16` to 0, 0.3 s) |
| 4 | A2-S21 | 19 | typed | 5.90 | 5.90 | the list sheet leaves: it drops 40 px and fades (0.4 s, power2.in; gone at 6.30); the list source gives way to the photo caption (0.3 s cross fade) |
| 5 | A2-S21 | 21 | message | 6.46 | 6.46 | the blank sheet slides in from the right (`x:660` to 0 with the fade, 0.7 s, power3.out; it lands at 7.16). Hold to the cut at 9.00 |
The hold from 7.16 to 9.00 is carried by the photograph's drift under the paper edge. After this comp the orchestrator places a 0.7 s blackout; the comp does not fade itself out.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a2s21-list.html` is the only file the builder writes; `data-composition-id="g-a2s21-list"`; id prefix `l50-`; root `<div id="l50-root" ...>` styled through `#l50-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the built `compositions/g-t1s3-list.html` (the sheet, its world, the ninth row's rule and cursor, the photograph ground and scrim) and `compositions/g-t1s2-warning.html` (the clock stamp, its hands, the card's entrance from the right). It shares the Beside state with `g-a1s18-list` (same wave; numbers in section 2). `g-a3s01-message` (wave 3) opens on this comp's blank sheet box.
**Assets mounted (paths from the episode folder):**
- `media/stills/a3-teletype-operators.jpg` (1370 x 1080 px).
- `media/drawings/telephone.svg` (viewBox -6 -58 102 106), the list header glyph at 60 px wide as in `g-t1s3-list`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s21-list`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type flags typed sheets by design (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the Beside state (s 1.1, tx 669.6, ty 44), the cursor's screen box and the hand angles (205, 300) are computed by a script and stated in the receipt. Line 4: capture 1.80, 2.30 and 5.80 twice (forward, and after a seek back) so the cursor's finite blink shows the same state both ways.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): photograph, scrim, list with eight plain rows, list source; no cursor, no stamp. Then one settled frame per cue: 2.00 (ninth row rule and cursor on, nothing typed), 4.60 (stamp in, hands at 6:50), 5.40 (place line), 6.35 (list gone, photo caption in the corner, no paper on screen), 7.30 (blank sheet landed at left 96, top 320, nothing on it), 8.90 (last look).
