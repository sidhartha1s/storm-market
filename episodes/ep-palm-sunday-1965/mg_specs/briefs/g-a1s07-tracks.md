Host: id=g-a1s07-tracks file=compositions/g-a1s07-tracks.html start=170.07 (timeline-map.md table 1; the mount in index.html wins) duration=26.08 s (wavs 25.74 s plus their gaps) track=2

# g-a1s07-tracks · A1-S7, A1-S8 · the day's tracks, then county after county (wave 2, photograph family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 4 and 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 6 items 4 and 5 are the buildable versions of these two Picture notes; section 3e row PT-04.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the photograph shows (rule 5). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window (rule 13). Nothing on a map is placed by eye from a picture (rule 14).
**Spoken (A1-S7):** "The storms it set off were supercells, thunderstorms that rotate, and single storms lasted up to four and a half hours. South Bend's own messages had them moving east northeast at about forty five miles an hour."
**Spoken (A1-S8):** "A storm that lasts that long crosses county after county, so its warning has to be handed on each time. That day, passing word ahead of a tornado from county to county was neither planned ahead nor systematic."
**One look:** the real track map comes up out of the dark from west to east; then it dims and one storm steps along a row of plain county tiles, the hand-off marks between them going grey and dropping out.

## 0. What this graphic claims
The day's storms were supercells; single storms lasted up to 4.5 hours and moved east northeast at about 45 mph. A storm that long crosses many counties, so its warning must be handed from county to county, and that day the handing on was neither planned ahead nor systematic.

## 1. Source
- `edit_script.md` A1-S7, Rows [IWX: "individual storms persisted for up to 4.5 hours"; NWS glossary "supercell"] and [survey printed pp. 38 and 39: "moving east northeast about 45 mph"]. A1-S8, Rows [the writer's reading] and [study printed p. 21: "neither pre-planned nor systematic"].
- Photograph: `media/stills/b7-tornado-track-map.jpg` (1396 x 1046, inventory row B7; credit "Courtesy: Dr. Russell Schneider, SPC"). White ground, grey county lines, red tracks. It prints no state name, no time and no track name, so no track can be told from another on it.
- Red ink measured on the file: image x 67 to 1066, y 53 to 575. Nothing red lies below image y 575.

## 2. Datum, scale, orientation
North is up. The map sits exactly as in the built `compositions/g-i1s4-states.html` part A: shown whole at 0.9293, screen x = 251.4 + 0.9293 x image x, screen y = 54 + 0.9293 x image y, so the image covers x 251 to 1549, y 54 to 1026, inside a Beige polaroid border 10 px (card left 241, top 44, 1297 x 972 inside the border). On that scale the red ink ends at screen y 588: **the band y 640 to 1026 of the map holds no track** and takes every element of ours.
East northeast is 22.5 degrees north of east: on screen, a line rising 22.5 degrees from the horizontal toward the right.
The tile row is schematic: six equal squares, not real counties, not to scale, not registered to the map.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map card | as `.st6-card` in `compositions/g-i1s4-states.html`: left 241, top 44, 1297 x 972, border 10 px Beige polaroid, white fill, the shadow of design sheet section 9; `<img>` 1297 x 972 inside. The card pushes scale 1.00 to 1.03 over the whole comp, `ease:"none"`, `transformOrigin:"900px 540px"` (at 1.03 its right edge is x 1577.7: left of the corner) |
| Veil | inside the card, over the image only: a `<div>` 1297 x 972, `rgba(3,5,8,0.45)`, on at frame 0. A1-S7: it shrinks to nothing toward the east (`scaleX` 1 to 0, `transformOrigin:"right center"`), so the map brightens from west to east. A1-S8: it returns over the whole image at `rgba(3,5,8,0.62)` (a second `<div>`, opacity 0 to 1) |
| Amber edge | inside the card (the card clips it): a band 90 px wide, 972 tall, `linear-gradient(to right, transparent, Amber 2 at 35 %, transparent)`, riding the veil's west edge from image x 0 to 1297. It is one soft line across the whole height of the map |
| Credit | as `.st6-mapcr`: Beige polaroid plate, left 271, bottom 64, padding 6 x 12, Arial 700 22 px, Caption dark: `Courtesy: Dr. Russell Schneider, SPC`. On from frame 0, fixed (it does not ride the push) |
| Label 1 | glass card (the stamp's glass, fill raised to `rgba(10,16,24,0.82)` because the ground under it is white paper), left 291, top 690, height 78, padding 0 x 28, Arial 700 34 px, Headline white, one line: `supercell: a thunderstorm that rotates` |
| Label 2 | same glass, left 291, top 784, height 78: `single storms lasted up to 4.5 hours`. Both labels are fixed HUD and stay until A1-S8 starts |
| Arrow | full-frame overlay SVG: a straight line from (1080, 900) to (1412.6, 762.2), 360 px long at 22.5 degrees, 8 px, Panel dark, round cap, with a closed head 34 px long at the far end. Drawn from the tail with `strokeDashoffset`; the head fades in when the line arrives |
| Chip | glass chip (design sheet section 9 "County label" metrics: height 46, padding 0 x 22, Arial 700 26 px, Body light; fill as label 1), left 1080, top 926: `about 45 mph` |
| Tiles (A1-S8) | six squares 150 x 150 in one row, top 640, left edges 275, 495, 715, 935, 1155, 1375 (gap 70; the row runs x 275 to 1525, centred on x 900). Fill Panel dark, stroke Body light 4 px, square corners. No name, number or letter on any tile |
| Hand-off marks | five dotted links in the gaps on the row's centre line y 715, each from 10 px right of a tile to 10 px left of the next (50 px): 6 px round dots, `stroke-dasharray:"0 12.5"`, `stroke-linecap:round`. Amber 2 when drawn (the travelling word), Label grey later |
| Tornado mark | `media/drawings/tornado-mark.svg` inline at scale 1.0 (object box 60 x 80, line 6), group stroke Body light, never red. Its point rides y 628, from x 350 (over tile 1) to x 1450 (over tile 6) |
| Row caption | Arial 700 22 px, Label grey, centred on x 900, top 812: `schematic: not a real track` |

## 4. Must be true in the picture
1. **No track is singled out.** The veil and its amber edge cross the whole height of the map in one move. Nothing of ours touches, circles, traces or brightens one red line more than another.
2. No timer, clock or duration sits on or beside a track. `4.5 hours` is a label in the lower band, about storms in general.
3. Every element of ours sits at screen y 640 or lower, clear of all red ink (which ends at y 588), except the veil and its edge.
4. The arrow rises 22.5 degrees from the horizontal, to the right. It starts and ends on no track, and its chip reads `about 45 mph`.
5. The tiles are plain and unnamed: six equal squares, with the caption `schematic: not a real track`. They are not aligned to any county line of the map, and the map under them is dimmed so that no real county reads as one of them.
6. Six tiles blink, one at a time, in order from the west. A blink is a fill change (Panel dark to Amber 2 at 45 % and back).
7. Five hand-off marks are drawn; at the end two remain. The marks that drop are numbers 2, 3 and 5 from the west, so what is left is uneven, not a pattern.
8. No state, county or town is named. The credit is the photograph's own.
9. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680 (tile 6 ends at x 1525; the card at 1.03 ends at x 1577.7).

## 5. Text (exact) and cues
Text: `Courtesy: Dr. Russell Schneider, SPC` · `supercell: a thunderstorm that rotates` · `single storms lasted up to 4.5 hours` · `about 45 mph` · `schematic: not a real track`.
Cue words and times are from `audio/a1-s7.words.json` and `audio/a1-s8.words.json` as they stood on 12 Oct 26 at 18:00, after the voice conversion's re-transcription. Wavs: A1-S7 12.232 s, A1-S8 13.509 s; the comp is their sum, 25.74 s. "t from comp start" for A1-S8 is 12.232 plus the time in the segment; gaps from `mg_specs/timeline-map.md` (not on disk yet) are added to every A1-S8 row. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S7 | 0 | The | 0.00 | 0.00 | first frame: the map card under its veil, the credit plate on. The push starts (25.74 s) |
| 1 | A1-S7 | 1 | storms | 0.50 | 0.08 | the veil shrinks west to east with the amber edge on its lip (2.2 s, ease none; the map is fully bright at 2.70) |
| 2 | A1-S7 | 6 | supercells, | 1.52 | 1.10 | label 1 slides in from the left (0.4 s, power3.out) |
| 3 | A1-S7 | 11 | single | 4.26 | 3.84 | label 2 slides in under it (0.4 s) |
| 4 | A1-S7 | 28 | east | 9.36 | 8.94 | the arrow draws from its tail (0.6 s, power2.out); its head fades in at 9.96 |
| 5 | A1-S7 | 31 | about | 10.38 | 9.96 | chip `about 45 mph` fades in (0.3 s, `y:12` to 0) |
| 6 | A1-S8 | 0 | A | 0.00 | 12.32 | labels, arrow and chip fade out (0.3 s); the heavy veil fades in over the whole map (0.5 s) |
| 7 | A1-S8 | 6 | crosses | 1.92 | 13.78 | the six tiles draw on from the west (stagger 0.05 s, 0.3 s each); the tornado mark and the row caption fade in, the mark over tile 1 |
| 8 | A1-S8 | 7 | county | 2.30 | 14.16 | the mark steps along the row (x 350 to 1450, ease none) and each tile blinks as the mark is over it: six blinks of 0.45 s, 2.70 s in all, ending at 17.232 |
| 9 | A1-S8 | 16 | handed | 5.04 | 16.90 | the five hand-off marks draw in Amber 2, west to east (stagger 0.12 s, 0.25 s each; the last is complete at 18.002) |
| 10 | A1-S8 | 20 | That | 7.12 | 18.98 | the mark returns to tile 1 (fade out, fade in, 0.3 s) |
| 11 | A1-S8 | 22 | passing | 8.08 | 19.94 | the mark steps along the row again (2.6 s, ease none) and the tiles blink again; the five hand-off marks stay as they are |
| 12 | A1-S8 | 33 | neither | 11.02 | 22.88 | all five hand-off marks turn Label grey (0.3 s) |
| 13 | A1-S8 | 36 | nor | 12.14 | 24.00 | marks 2, 3 and 5 fade out (stagger 0.15 s, 0.25 s each; done at 24.922). Hold to the cut at 25.74 |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.
Beat count (rule 13), computed: six blinks x 0.45 s = 2.70 s, inside the window from "county" (2.30) to "handed" (5.04), 2.74 s. If the final voice shortens that window, shorten each blink; never drop a tile.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a1s07-tracks.html` is the only file the builder writes; `data-composition-id="g-a1s07-tracks"`; id prefix `trk-`; root `<div id="trk-root" ...>` styled through `#trk-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the built `compositions/g-i1s4-states.html` part A for the map card, its fit and its credit plate (copy the numbers, not the state chips). The photograph family bases `compositions/g-a2s17-funnels.html` and `compositions/g-a1s01-kc.html` (wave 1) set the family's caption and push habits. The tile row is new here; `g-a4s14-eight` (wave 3) uses the same plain square.
This is the track map's second use in the episode (the first is `g-i1s4-states`): the orchestrator declares the callback in `index.html`; the builder does not touch that file.
**Assets mounted (paths from the episode folder):**
- `media/stills/b7-tornado-track-map.jpg` (1396 x 1046 px).
- `media/drawings/tornado-mark.svg` (object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s07-tracks`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the tile left edges (275, 495, 715, 935, 1155, 1375), the arrow's end (1412.6, 762.2) and the blink total (2.70 s) are computed by a script from this brief's numbers and stated in the receipt. Line 5: both glass labels are read on a frame over the white map; if the type does not hold, darken the glass, never move a label up into the tracks.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the map under its veil, credit on, nothing else. Then one settled frame per cue: 1.60 (wipe half way, the edge one soft line top to bottom), 3.00 (map bright, label 1 on), 5.00 (both labels), 10.00 (arrow whole), 11.00 (chip), 13.00 (map dimmed, lower band clear), 14.50 (tiles, mark, caption), 15.90 (a blink in the middle of the row), 18.20 (five amber marks), 21.60 (second pass, the five marks unchanged), 23.80 (marks grey), 25.40 (two marks left, last look).
