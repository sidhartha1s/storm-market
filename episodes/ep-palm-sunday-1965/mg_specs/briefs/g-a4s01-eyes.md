Host: id=g-a4s01-eyes file=compositions/g-a4s01-eyes.html start=661.85 (timeline-map.md table 1; the mount in index.html wins) duration=6.71 s track=2
RULED by the lead 12 Oct 26: film. Build the 'If the lead rules film' variant. File media/films/cuts/a14-05-operations-room.mp4 from 20.0 s into the file, window 0.00 to 3.15 s, mounted by the composer on track 1 at 661.85.

# g-a4s01-eyes · A4-S1 · he waited fifteen minutes, until he saw it "with his own eyes" (wave 3, page family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3c row PC-09. Times: `mg_specs/timeline-map.md` tables 1, 5 and 6.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). While a training film shot is on screen its own label is the only chip in the frame (rule 4; it decides the film question in section 2). No page crop holds past about 8 seconds without a visible change (rule 7). The study's hidden county is labelled `County B` only, and `County A` never appears in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A4-S1):** "He waited fifteen minutes, until he saw the tornado, in the study's words, "with his own eyes.""
**One look:** the study's typed page with four words underlined, and a clock beside it whose minute hand runs a quarter turn.

## 0. What this graphic claims
County B's civil defense director did not pass the report on to other organizations in his county at once. He waited fifteen minutes, to about 7:30 PM, until he saw the tornado, in the study's words, "with his own eyes". The page gives "about 7:30 p. m." and "fifteen minutes"; about 7:15 PM is those two put together and is shown as "about".

## 1. Source
- `edit_script.md` A4-S1, Rows [A13; study printed p. 21] (County B).
- Crop: `media/docs/study-p21-eyes-crop.png` (1460 x 299, cut from `media/docs/study-pdf-23-orig.png`, study printed p. 21; row in `provenance.csv`). Read by eye 12 Oct 26, line by line:
  1. `ganization, but did not notify any other organizations in County B. Rather, he`
  2. `waited fifteen minutes(to about 7:30 p. m. ), until he saw the tornado "with his`
  3. `own eyes". He then radioed the City Police telling them of the tornado's lo-`
  4. `cation, the direction in which it was moving and also asked them to notify the`
- The crop prints the study's code `County B` once (line 1). It matches the chip. `County A` is not in the crop.
- Lines 3 and 4 after `own eyes".` are the next beat's subject (the radio call) and stay dim here.

## 2. Datum, scale, orientation
The crop is mounted at its own size, 1460 x 299, at screen (106, 126) inside the card: screen x = crop x + 106, screen y = crop y + 126. The page is double spaced (line pitch 76 px), so the underline is the design sheet's 6 px at 4 px under the line box. Boxes measured on the file by a row and column projection (12 Oct 26):
| Item | Crop px (x0 to x1, y0 to y1) | Screen px |
|---|---|---|
| Line 1, whole | 81 to 1420, 23 to 53 | x 187 to 1526, y 149 to 179 |
| Line 1, `County B.` | 1045 to 1204, 23 to 53 | x 1151 to 1310, y 149 to 179 |
| Line 2, whole | 79 to 1399, 97 to 128 | x 185 to 1505, y 223 to 254 |
| Line 2, `waited fifteen minutes(to about 7:30 p. m. ),` | 79 to 808, 97 to 128 | x 185 to 914, y 223 to 254 |
| Line 2, `"with his` | 1255 to 1399, 97 to 128 | x 1361 to 1505, y 223 to 254 |
| Line 3, `own eyes".` | 81 to 261, 173 to 205 | x 187 to 367, y 299 to 331 |
| Line 4, whole | 81 to 1401, 249 to 283 | x 187 to 1507, y 375 to 409 |
Clock hands, clockwise degrees from 12: 7:15 is hour 217.5, minute 90; 7:30 is hour 225, minute 180. The sweep is a quarter turn of the minute hand.

**The lead's question: can a film cut open this picture, since it is the first one after the book ad and DESIGN.md asks for real footage on that cut?**
- Mechanically yes, for 3.15 s at most. The page must be up by word 9 "in" ("in the study's words", 3.15 s from the comp's start) and its underline lands on word 13 "with" (4.73 s). A film window could run from 0.00 to 3.15 s under "He waited fifteen minutes, until he saw the tornado,". `media/films/cuts/a14-08-telephone-call.mp4` (4.17 s) covers that; so does `media/films/cuts/a14-10-desk-telephone.mp4` (15.72 s), whose seconds 11.41 to 15.72 are not shown anywhere (the A3-S7 mount ends at 11.41).
- I advise against both, and this brief is written without film. Reasons: (1) both shots show a man on a telephone, and the line under them is "He waited": the study says he did not notify any other organization in those fifteen minutes, so a man telephoning is the opposite of the claim; (2) each shot is already used once (14-10 in A3-S7, 14-08 in A5-S11) and the script's note gives each shot one use, so the second use needs `data-callback` and the lead's ruling; (3) rule 4 keeps the `County B` chip and the clock off the frame while film shows, so the fifteen minute sweep would lose its spoken words (0.11 to 2.03 s) and County B would not be named until 3.15 s; (4) the page would have 1.58 s on screen before its underline instead of 4.73 s.
- What this picture already is: a scan of the real 1966 page, not a drawn graphic. If the lead still wants moving footage on the cut, the smallest change is in section 5 under "If the lead rules film".

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| County chip | design sheet section 9 "County label": glass chip, left 96, top 54, height 46, padding 0 x 22, Arial 700 26 px, Body light: `County B`. On from frame 0 |
| Document card | design sheet section 9: left 96, top 116, 1480 x 319 (right 1576, bottom 435), Beige polaroid border 10 px, its shadow; the crop at (106, 126). On from frame 0, all of it bright |
| Unlit page | Panel dark at 45 %: R1 screen x 106 to 1566, y 126 to 201 (line 1); R2 screen x 386 to 1566, y 277 to 353 (line 3 after `own eyes".`); R3 screen x 106 to 1566, y 353 to 425 (line 4). Line 2 whole and `own eyes".` stay bright |
| Underline 1 | Popfig red, 6 px, screen x 1361 to 1505, y 258 to 264, under `"with his`; `scaleX` 0 to 1 from the left |
| Underline 2 | Popfig red, 6 px, screen x 187 to 367, y 335 to 341, under `own eyes".` |
| Clock stamp | design sheet section 8 moved down by 374 px: glass card left 96, top 470, 590 x 200 (bottom 670). Clock face centre (191, 570), radius 62. Eyebrow at x 284, y 490, Arial 700 20 px, Label grey, tracking 6: `ABOUT`. Time at x 284, y 516, Courier New 700 84 px, Amber 2: `7:15 PM`, then `7:30 PM` (two spans in one place, toggled). Place line at x 286, y 618, Arial 700 26 px, Body light: `by the study's account`. "about 7:15 PM" does not fit on the time line at 84 px, so `ABOUT` is the eyebrow |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 21` |

## 4. Must be true in the picture
1. Every word on the card is the page's own; nothing on the card is retyped. The underlined words are `"with his` and `own eyes".` and nothing else.
2. The clock starts at 7:15 (hour hand between 7 and 8, minute hand on the 3) and ends at 7:30 (minute hand on the 6, hour hand half way between 7 and 8). The minute hand moves a quarter turn, clockwise, once. The word `ABOUT` is on the stamp the whole time.
3. The time text changes from `7:15 PM` to `7:30 PM` when the sweep ends, not before; the page's own `7:30 p. m.` is bright while it does.
4. The chip reads `County B` and no other county, town or person is named. No person is drawn.
5. No telephone, radio or police desk is drawn here: in these fifteen minutes he told no other office. The radio call belongs to the next composition.
6. Line 1 with the page's own `County B.` is dimmed, not hidden; it stays readable under the dim.
7. The card is never still for 8 seconds: a visible change lands at 0.11, 0.83, 1.25, 2.03, 3.15, 4.73 and 5.07.
8. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `County B` · `ABOUT` · `7:15 PM` · `7:30 PM` · `by the study's account` · `Disaster Research Center, 1966, p. 21`. Page words are the image.
Cue words and times are from `audio/a4-s1.words.json` as it stood on 12 Oct 26 at 19:30. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: -0.31) plus the word's time; the first word uses table 5's first sound. The transcriber writes word 2 as "15"; the voice says "fifteen". Retime from the word index and the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S1 | 0 | He | 0.00 | 0.00 | first frame (the cut out of the book ad): ground, chip `County B`, the document card whole and bright |
| 1 | A4-S1 | 1 | waited | 0.42 | 0.11 | the clock stamp slides in from the left (`x:-660` set at 0, to 0 with the fade; 0.6 s, power3.out) reading `7:15 PM`, hands 217.5 and 90 |
| 2 | A4-S1 | 3 | minutes | 1.14 | 0.83 | the minute hand sweeps 90 to 180 and the hour hand 217.5 to 225 (1.2 s, power2.inOut); at 2.03, when the sweep ends, the time text cuts to `7:30 PM` |
| 3 | A4-S1 | 4 | until | 1.56 | 1.25 | the unlit page fades in over R1, R2, R3 (0.4 s) |
| 4 | A4-S1 | 9 | in | 3.46 | 3.15 | the source line fades in (0.3 s, `y:12` to 0) |
| 5 | A4-S1 | 13 | with | 5.04 | 4.73 | underline 1 draws under `"with his` (0.3 s, power2.out) |
| 6 | A4-S1 | 15 | own | 5.38 | 5.07 | underline 2 draws under `own eyes".` (0.3 s). Hold to the cut at 6.71 |
**If the lead rules film** (not built unless the orchestrator says so and mounts the cut on track 1 at left 480, top 150, 960 x 720): the comp opens as the film view of `compositions/g-a1s15-offices.html` (ground with hole, frame, the one chip `Civil defense training film, 1967`), window open 0.00 to 3.15; at step 4 (word 9 "in", 3.15) a hard cut covers the hole and brings on the chip `County B`, the card with the unlit page already on, the source line and the stamp already reading `7:30 PM` (no sweep); steps 5 and 6 as above. Steps 1 to 3 are dropped.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s01-eyes.html` is the only file the builder writes; `data-composition-id="g-a4s01-eyes"`; id prefix `eyes-`; root `<div id="eyes-root" ...>` styled through `#eyes-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the built `compositions/g-i1s6-page.html` (page crop, unlit page, underline, county chip above the card) and `compositions/g-t1s2-warning.html` (the clock stamp and its hands); layout habits of the acts' page briefs from `mg_specs/briefs/g-a2s15-old.md`. `g-a4s08-chief` (same wave) uses the same chip and card position. No later composition copies this one.
**Assets mounted (paths from the episode folder):**
- `media/docs/study-p21-eyes-crop.png` (1460 x 299 px).
- `media/drawings/wall-clock.svg` (object box 124 x 124, viewBox -6 -6 136 136), inlined for the stamp's face if the builder does not copy the built stamp's own face.
Not mounted: `media/films/cuts/a14-10-desk-telephone.mp4` (15.72 s) and `media/films/cuts/a14-08-telephone-call.mp4` (4.17 s), named only for the lead's question in section 2.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s01-eyes`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type flags this comp by design (the page).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 1.40 (mid sweep) and 2.03 forward and backward and match the frames; the hands' `svgOrigin` is set once at build, before any tween. Line 6: the screen boxes of section 2 are the crop boxes plus (106, 126) and the hand angles are (217.5, 90) and (225, 180), computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): chip, card bright, no stamp, no underline. Then one settled frame per cue: 0.75 (stamp in at `7:15 PM`, hands right), 1.40 (mid sweep, still `7:15 PM`), 2.10 (`7:30 PM`, minute hand on the 6), 1.70 and 2.60 (unlit page: line 2 and `own eyes".` bright, `County B.` readable under the dim), 3.50 (source line), 5.05 (underline 1 complete, underline 2 not yet), 5.40 (both underlines), 6.60 (last look).
