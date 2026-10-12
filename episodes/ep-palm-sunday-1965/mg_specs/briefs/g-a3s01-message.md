Host: id=g-a3s01-message file=compositions/g-a3s01-message.html start=480.67 (timeline-map.md table 1; the mount in index.html wins) duration=18.73 s track=2

# g-a3s01-message · A3-S1, A3-S2, A3-S3 · the 6:50 message: telephones out, the words a child remembered, the warning widened (wave 3, page family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3b row BM-1, section 3c row PC-08, section 6 item 11. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No page crop holds past about 8 seconds without a visible change (rule 7). The teletype room photograph is not used here: its three uses are spent elsewhere (rule 9). The page and the lifted strip use two type sizes by design (rule 10). A flash is a stroke or fill change, never a scale pop (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids take this comp's prefix; the first frame read of the map checks its line weight (rule 20).
**Spoken (A3-S1):** "The six fifty message said telephones were out in many areas, and that it was impossible to notify many people."
**Spoken (A3-S2):** "It opened with almost the words an eleven year old remembered on television, tornado reports so numerous it was impossible to keep track."
**Spoken (A3-S3):** "And it widened the warning to the whole north central part of Indiana."
**One look:** the typed 6:50 entry under its clock, two phrases underlined; then the television from the opening with the remembered words, beside the message's own; then Indiana with its north central part lit.

## 0. What this graphic claims
The South Bend Weather Bureau's 6:50 PM message said telephones were out in many areas and that it was impossible to notify many people. It opened with words close to the ones a viewer recalled seeing on television in 2014 ("impossible to keep track" on the page, "hard to keep track" in the recollection). It said warnings should exist throughout the northern central portion of Indiana. The amber area on the map is a schematic of that phrase: the message gives no boundary and names no town in it.

## 1. Source
- `edit_script.md` A3-S1, Rows [A10; survey printed p. 40]; A3-S2, Rows [E, Przybylinski, 2014: "hard to keep track"; A10: "impossible to keep track"]; A3-S3, Rows [A10; survey printed p. 40: "Warnings should therefore exist throughout the northern central portion of Indiana"].
- Crop: `media/docs/survey-p40-650pm-crop.png` (1460 x 240, cut from `media/docs/survey-pdf-68-orig.png`, survey printed p. 40; row in `provenance.csv`). Read by eye 12 Oct 26, line by line:
  1. `Issued at 6:50 PM EST.`
  2. `Reports of tornadoes and funnel clouds have become so numerous that it is`
  3. `impossible to keep track of them. Warnings should therefore exist throughout`
  4. `the northern central portion of Indiana. The problems have been intensified`
  5. `by telephones being out in many areas and it is impossible to notify many`
  6. `people.`
- The page is single spaced and skewed about half a degree (each line rises to the right), so line boxes overlap by a pixel or two and each underline has its own y.
- Television and station card: the built `compositions/g-i1s2-station.html` (`stn-screen`) and `media/drawings/README.md` "Television screen".
- Map: `media/maps/indiana-counties.svg` (BM-1), its `st-in` outline and `map-neighbours` only.

## 2. Datum, scale, orientation
Three views, hard cuts between them.
**View PAGE.** The crop is mounted at its own size at screen (106, 330) inside the card: screen x = crop x + 106, screen y = crop y + 330. The card's box is the blank sheet's box of `mg_specs/briefs/g-a2s21-list.md` (left 96, top 320, 1480 x 260): the sheet that was blank at the end of act 2 is now typed. Boxes measured on the file by a row and column projection (12 Oct 26):
| Item | Crop px (x0 to x1, y0 to y1) | Screen px |
|---|---|---|
| Line 1 `Issued at 6:50 PM EST.` | 43 to 422, 18 to 41 | x 149 to 528, y 348 to 371 |
| Line 2, whole | 42 to 1335, 45 to 79 | x 148 to 1441, y 375 to 409 |
| Line 3, `impossible to keep track of them.` | 43 to 617, 80 to 115 | x 149 to 723, y 410 to 445 |
| Line 3, `Warnings should therefore exist throughout` | 660 to 1409, 80 to 114 | x 766 to 1515, y 410 to 444 |
| Line 4, whole | 44 to 1391, 116 to 153 | x 150 to 1497, y 446 to 483 |
| Line 5, `telephones being out in many areas` | 98 to 691, 165 to 193 | x 204 to 797, y 495 to 523 |
| Line 5, `it is impossible to notify many` | 790 to 1338, 155 to 185 | x 896 to 1444, y 485 to 515 |
| Line 6, `people.` | 43 to 159, 203 to 231 | x 149 to 265, y 533 to 561 |
Underlines here are 4 px thick and sit 2 px under their own words' lowest ink, not the 6 px at 4 px of design sheet section 9 (the page is single spaced).
**View SET.** The television of the opening at 2.8 times (0.875 of the big television's 3.2), so the small line `as recalled in 2014` stays at 19.25 px, above the 19 px floor. Object box x 96 to 936, y 150 to 822 (cabinet bottom y 710). Screen area x 152 to 689.6, y 206 to 654 (537.6 x 448), corner radius 67.2, centre x 420.8. Every number of the built station card is its big-television value times 0.875, measured from the screen's top left.
**View MAP.** North is up. One inline SVG in the box left 672, top 60, 576 x 960 with viewBox `206 153 468 780` (1.2308 px per map unit; screen x = 672 + 1.2308 x (u - 206), y = 60 + 1.2308 x (u - 153)). Indiana's outline lands on x 701 to 1219, y 85 to 992. Its northern third ends at map y 418.6, screen y 387.

## 3. Geometry (screen px)
View PAGE (0.00 to 8.01):
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0, under all three views |
| Clock stamp | design sheet section 8, as the built `compositions/g-t1s2-warning.html`: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `6:50 PM` / `South Bend, Indiana`; hour hand 205, minute hand 300. On from frame 0 |
| Document card | left 96, top 320, 1480 x 260 (right 1576, bottom 580), Beige polaroid border 10 px, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`; the crop 1460 x 240 at (106, 330). On from frame 0, all of it bright |
| Unlit page 1 | Panel dark at 45 %: D1 screen x 106 to 1566, y 373 to 483 (lines 2, 3 and 4); D2 screen x 281 to 1566, y 530 to 570 (line 6 to the right of `people.`). Line 1, line 5 and `people.` stay bright |
| Underline A | Popfig red, 4 px, screen x 204 to 797, y 526 to 530, under `telephones being out in many areas`; `scaleX` 0 to 1 from the left |
| Underline B1 | Popfig red, 4 px, screen x 896 to 1444, y 518 to 522, under `it is impossible to notify many` |
| Underline B2 | Popfig red, 4 px, screen x 149 to 265, y 563 to 567, under `people.` |
| Strip S | quote strip (design sheet section 9): Beige polaroid, left 96, top 610, 1480 x 170 (right 1576, bottom 780), the card's shadow. Quote in Georgia 40 px, Caption dark, line height 52 px, left 136: line 1 `“telephones being out in many areas ...` top 628, line 2 `it is impossible to notify many people”` top 680. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 740: `Weather Bureau, South Bend · 6:50 PM` |
| Unlit page 2 | Panel dark at 45 %: D3 screen x 106 to 1566, y 484 to 570 (lines 5 and 6); D4 screen x 746 to 1566, y 412 to 446 (line 3 from `Warnings`); D5 screen x 106 to 1566, y 446 to 484 (line 4). Line 1, line 2 and `impossible to keep track of them.` stay bright. D1 and D2 are off; underlines A, B1, B2 are off |
View SET (8.01 to 14.44):
| Element | Px |
|---|---|
| Television | `media/drawings/television.svg` inline, ids prefixed `msg-`, at 2.8 times: `<g transform="translate(96 150) scale(2.8)">`; the file's 2-unit line is 5.6 px. On the dark ground set every stroke to Body light, legs and cabinet edge included (in the file they are Panel dark and do not show on a dark ground); body fill Panel dark. Screen Idle |
| Station card | the `stn-screen` block of `compositions/g-i1s2-station.html` at 0.875: a `<div>` at left 152, top 206, 537.6 x 448, radius 67.2, fill Panel dark; frame line 2 px Headline white, 8.75 px inside the screen edge, radius 58.4; four lines Arial 700 35 px, Headline white, centred on x 420.8, tops 281.2, 326.8, 372.2, 417.8, line height 38.5 px; small line Arial 700 19.25 px, Label grey, centred on x 420.8, top 508.7. The screen's outline is drawn again above the card: 5.6 px Body light on x 152 to 689.6, y 206 to 654, radius 67.2 |
| Strip G | Beige polaroid, left 980, top 300, 596 x 290 (right 1576, bottom 590), the card's shadow. Quote in Georgia 40 px, Caption dark, line height 52 px, left 1012: `“so numerous that it is` top 330, `impossible to keep track` top 382, `of them”` top 434. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 1012, top 510: `Weather Bureau, South Bend · 6:50 PM` |
View MAP (14.44 to 18.73):
| Element | Px |
|---|---|
| Map | BM-1's `map-neighbours` group and the `st-in` path only, ids prefixed `msg-`; no county path and no `pt-` group is inlined. Indiana's outline 3 px Body light, neighbour outlines 2 px Label grey at 0.4, as the map family |
| Band | one `<rect>` in map units, x 206 to 674, y 153 to 478.6, fill Amber 2, clipped to the `st-in` path with a `<clipPath>`, under the outline. Its opacity is a vertical `linearGradient` mask: 0.45 from map y 153 to 398.6 (screen y 60 to 362), falling to 0 at map y 478.6 (screen y 461). The fade is the soft edge: its mid point is the end of the northern third (screen y 387). No county line is inside it |
| Area label | glass chip, left 1250, top 210, height 46, padding 0 x 22, Arial 700 26 px, Body light: `north central Indiana` |
| Source line | design sheet section 10, left 96, bottom 60: `Weather Bureau survey, 1965, p. 40 · area drawn is schematic` |

## 4. Must be true in the picture
1. Every word on the card is the page's own. Only the two strips are retyped, each with quotation marks and its attribution.
2. In view PAGE the underlined words are `telephones being out in many areas`, then `it is impossible to notify many` with `people.` and nothing else. Strip S does not rise before underline B2 is complete.
3. The stamp reads 6:50 PM (hour hand between 6 and 7, minute hand on the 10) and the page's first line reads `Issued at 6:50 PM EST.`; both are bright in view PAGE.
4. The station card on the television carries exactly the built card's words, `“so many tornado` / `reports that it was` / `hard to keep track` / `of them”` and `as recalled in 2014`. It never carries "WEATHER BUREAU", a time, a map or a county. Strip G carries the message's words. The two wordings differ ("hard" and "impossible") and are never merged into one quote.
5. No child, no person and no named viewer is drawn or named.
6. On the map the amber area covers the north of the state across its whole width and fades out; it has no hard lower edge and no county line inside it. No town dot, no town name and no county name is on the map. The source line says the area is schematic.
7. The card is never still for 8 seconds: a visible change lands at 1.31, 3.87, 5.35, 5.60 and 6.79, and the card leaves at 8.01.
8. The ground is the canvas gradient in all three views; the teletype room photograph does not appear.
9. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `6:50 PM` · `South Bend, Indiana` · `“telephones being out in many areas ...` / `it is impossible to notify many people”` · `Weather Bureau, South Bend · 6:50 PM` (on both strips) · `“so many tornado` / `reports that it was` / `hard to keep track` / `of them”` · `as recalled in 2014` · `“so numerous that it is` / `impossible to keep track` / `of them”` · `north central Indiana` · `Weather Bureau survey, 1965, p. 40 · area drawn is schematic`. Page words are the image.
Cue words and times are from `audio/a3-s1.words.json`, `audio/a3-s2.words.json` and `audio/a3-s3.words.json` as they stood on 12 Oct 26 at 19:30. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A3-S1 -0.55, A3-S2 6.45, A3-S3 14.07) plus the word's time; a segment's first word uses table 5's first sound. The transcriber writes A3-S1 word 1 as "650" and A3-S2 word 7 as "11"; the voice says "six fifty" and "eleven". Retime from the word index and the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S1 | 0 | The | 0.00 | 0.00 | first frame: ground, the stamp at 6:50 PM, the document card whole and bright |
| 1 | A3-S1 | 4 | telephones | 1.86 | 1.31 | unlit page 1 fades in (0.4 s); underline A draws (0.6 s, power2.out) |
| 2 | A3-S1 | 14 | impossible | 4.42 | 3.87 | underline B1 draws (0.6 s) |
| 3 | A3-S1 | 18 | people. | 5.90 | 5.35 | underline B2 draws (0.2 s); at 5.60, when it is complete, strip S rises (`y:60` set at 0, to 0 with the fade; 0.4 s, power3.out) |
| 4 | A3-S2 | 1 | opened | 0.34 | 6.79 | underlines A, B1, B2 fade out (0.2 s); unlit page 1 gives way to unlit page 2 (0.4 s cross fade): the message's opening sentence is the bright part |
| 5 | A3-S2 | 6 | an | 1.56 | 8.01 | hard cut inside the comp: stamp, card, unlit page and strip S off; the television on, drawn, screen Idle |
| 6 | A3-S2 | 12 | television. | 3.08 | 9.53 | the screen cuts from Idle to the station card (hard cut, one 0.1 s flash of Headline white at 30 % over the screen area) |
| 7 | A3-S2 | 15 | so | 4.78 | 11.23 | strip G rises (`y:60` to 0 with the fade, 0.4 s, power3.out) showing its first line only |
| 8 | A3-S2 | 19 | impossible | 5.90 | 12.35 | strip G's second and third lines and its attribution fade in (0.3 s) |
| 9 | A3-S3 | 0 | and | 0.00 | 14.44 | hard cut inside the comp: television and strip G off; the map on (Indiana's outline and the faint neighbours), nothing lit |
| 10 | A3-S3 | 4 | warning | 1.14 | 15.21 | the source line fades in (0.3 s, `y:12` to 0) |
| 11 | A3-S3 | 7 | whole | 1.82 | 15.89 | the band comes on at once (opacity 0 to 1 in 0.4 s; a fill change, no scale) |
| 12 | A3-S3 | 8 | north | 2.06 | 16.13 | the area label lands (0.3 s, `y:16` to 0 with the fade). Hold to the cut at 18.73 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s01-message.html` is the only file the builder writes; `data-composition-id="g-a3s01-message"`; id prefix `msg-`; root `<div id="msg-root" ...>` styled through `#msg-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** page crop, unlit page, underline and strip from the built `compositions/g-i1s3-cloud.html` and `compositions/g-i1s7-sheriff.html` (two underlines in turn); stamp over a card at top 320 from the built `compositions/g-t1s2-warning.html`; the card's box from `mg_specs/briefs/g-a2s21-list.md` (the blank sheet); television and station card from the built `compositions/g-i1s2-station.html`; map line weights and the lit value 0.45 from the map base `compositions/g-a2s14-six.html` (brief `mg_specs/briefs/g-a2s14-six.md`). No later composition copies this one.
**Assets mounted (paths from the episode folder):**
- `media/docs/survey-p40-650pm-crop.png` (1460 x 240 px).
- `media/drawings/television.svg` (object box 300 x 240, viewBox -3 -3 306 246, line 2), inlined.
- `media/drawings/wall-clock.svg` (object box 124 x 124, viewBox -6 -6 136 136), inlined for the stamp's face if the builder does not copy the built stamp's own face.
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880): the `st-in` path and the `map-neighbours` group, inlined.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s01-message`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type flags this comp by design (page and strip, plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 8.01, 9.53 and 14.44 forward and backward and match the frames. Line 5: read underlines A and B1 on one frame at full size; neither may touch `people.` on line 6, and B2 must sit inside the crop (its lower edge is crop y 237 of 240). Line 6: the screen boxes of section 2 are the crop boxes plus (106, 330), the station card numbers are the built ones times 0.875, and the map box and band are the section 2 formula; all computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): stamp at 6:50, card bright, no underline. Then one settled frame per cue: 2.10 (unlit page 1, underline A complete), 4.60 (underline B1), 5.58 (underline B2, strip not yet on), 6.20 (strip S whole), 7.30 (unlit page 2: line 1, line 2 and `impossible to keep track of them.` bright, no underline), 8.05 (television, screen Idle, all lines visible on the dark ground), 9.70 (station card, small line readable), 11.80 (strip G first line only), 12.90 (strip G whole), 14.48 (map: outline only, line weight 3 px), 15.60 (source line), 16.40 (band on, soft lower edge, no county line), 17.00 (area label), 18.60 (last look).
