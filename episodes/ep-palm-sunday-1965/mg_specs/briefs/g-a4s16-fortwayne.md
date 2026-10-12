Host: id=g-a4s16-fortwayne file=compositions/g-a4s16-fortwayne.html start=803.50 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=10.31 s (last sound at 9.31) track=2

# g-a4s16-fortwayne · A4-S16 · one office to the east, still typing warnings for storms already gone (wave 3, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3a rows DR-01 and DR-03. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`. Base: `mg_specs/briefs/g-a2s14-six.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2): the message card carries no words. The root is styled through its id, never `id="root"` (rule 3). A flash is a stroke or fill change (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids take this comp's prefix (rule 20). This comp names two real Weather Bureau offices, so `County A` and `County B` never appear in it (rule 8).
**Spoken (A4-S16):** "And one office to the east, the Fort Wayne Weather Bureau was still typing warnings for storms that had already gone by. Later that night, some came after."
**One look:** the map's South Bend dot goes dim and a dot to the east lights with a teletype under it, paper coming out; then, off the map, a tornado mark runs past a town with no name and a paper card from that teletype lands behind it.

## 0. What this graphic claims
The Fort Wayne Weather Bureau, east of South Bend, was typing warnings for storms that had already passed, and later that night some of its warnings arrived after the storm. The picture names the office and nothing else: no town, no time and no storm is identified. Act 5 does that.

## 1. Source
- `edit_script.md` A4-S16, Rows [A20, A22, C16; survey printed pp. 43, 45]. Its Picture note is the only source of what is drawn. The note gives no source line and none is shown.
- Positions: `media/data/points.csv` (US Census gazetteer), map units: `pt-south-bend` (462.2, 188.5), `pt-fort-wayne` (605.1, 297.0). Map: `media/maps/indiana-counties.svg` (BM-1). Allen County (`co-in-allen`) is x 580.4 to 648.4, y 263.5 to 328.9 in map units.
- The town the mark passes is not named by the script, so it is not on the map: it is a plain circle on a line under the map, with the label `a town`.

## 2. Datum, scale, orientation
North is up on the map; the map stays in the family's NORTH state for the whole comp (no zoom): box left 716, top 62, 1080 x 450, viewBox `296 166 360 150`, 3.0 px per map unit (screen x = 3u - 172, y = 3u - 436). By script: South Bend (1214.6, 129.5); Fort Wayne (1643.3, 455.0); Allen County on screen x 1569.2 to 1773.2, y 354.5 to 550.7 (cut by the box's bottom edge, y 512).
The lower band (y 620 to 912) is SCHEMATIC, NOT TO SCALE and is not part of the map: a line, a circle and a mark that moves left to right, the direction the day's storms moved. Nothing in it has a real position.
Fort Wayne's dot is at x 1643, right of x 1600, but at y 455: the presenter corner (x >= 1600 and y >= 680) stays empty. Everything below y 680 ends at x 1565 or less.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `ftw-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px. Every `pt-` group hidden except `ftw-pt-south-bend` and `ftw-pt-fort-wayne`. No county is lit |
| South Bend | dot (1214.6, 129.5), `r` 2 map units (6 px); label `South Bend`, Arial 700 22 px, left 1232, top 118. Frame 0: dot and label Body light. Dim: both `#55606b` |
| Fort Wayne | dot (1643.3, 455.0), `r` 2 map units, fill Amber 2 when lit; one ring, centre on the dot, radius 8 to 26, 3 px Amber 2, fading as it grows (once). Label `Fort Wayne`, Arial 700 22 px, Headline white with the credit shadow, centred on x 1671, top 392 (inside Allen County, on no county line) |
| Link to the teletype | one path `M1643.3 465 V670 H1540`, 4 px Body light, round caps and joins, no fill |
| Teletype | `media/drawings/teletype.svg` inline, `translate(1400 600)`, scale 1 (box x 1400 to 1540, y 600 to 740; its paper is x 1434 to 1506, y 600 to 650). Lines Headline white; body Panel dark; paper (`dw-lamp`) Beige polaroid `#f4f0e6`; bars (`dw-type`) Caption dark sub |
| Teletype label | Arial 700 22 px, line-height 28, Label grey, left 1375, width 190, centred, top 752, two lines: `Weather Bureau ·` / `Fort Wayne` (right edge x 1565) |
| Paper strip | one group clipped to the slot window x 1434 to 1506, y 520 to 600: a Beige polaroid rect 72 x 80 and three typed bars on it (6 px tall, Caption dark sub, left x 1444, widths 44, 52, 36). The group moves up from `y:80` to `y:0` (ease none, 31.87 px per second), so the paper comes out of the teletype's top and its bars come out with it; no bar has a tween of its own. Rest place (5.90 on): paper y 520 to 600 (8 px under the map box), bar tops at y 524.2, 544.0, 578.4, by script, so each bar clears the slot on its cue word |
| Schematic line | one line, y 860, x 96 to 1300, 2 px Label grey |
| Town | circle, centre (700, 860), radius 12, 4 px Body light, fill Panel dark; label `a town`, Arial 700 22 px, Label grey, centred on x 700, top 884 |
| Tornado mark | `media/drawings/tornado-mark.svg` inline, scale 1 (60 x 80, line 6), stroke Body light, never red; its lowest point rides the line (y 860): box y 780 to 860. Its point moves from x 200 to x 1150 (ease none), then drifts on to x 1210 |
| Message card | Beige polaroid rect 200 x 120, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, with four Caption dark sub bars (left 24 inside the card, 12 px tall, widths 150, 128, 142, 96 at y 24, 46, 68, 90 inside the card). No words. Rest place: left 600, top 640 (x 600 to 800, y 640 to 760). It starts over the paper strip at left 1370, top 500 and scale 0.36, and flies to its rest place and scale 1 |
| Card leader and label | 2 px Label grey line from (700, 760) to (700, 846); label `the warning`, Arial 700 22 px, Body light, left 816, top 688 |

## 4. Must be true in the picture
1. South Bend dims and Fort Wayne lights; Fort Wayne is east (right) of South Bend and lower on the map, at the file's own position. Only these two towns are marked on the map and no county is lit.
2. The teletype stands under Fort Wayne's dot and is joined to it. Paper comes out of its top and keeps coming while the first sentence runs.
3. The town in the lower band has no name and is not on the map: it sits under the map's box, on its own line, labelled `a town`.
4. Order in the lower band: the tornado mark passes the town (its point crosses x 700 at 7.88), and only then does the card leave the teletype (8.31, the mark's point at x 970) and land above the town (8.81). The card is never at the town before the mark has passed.
5. The mark is Body light, never red, and has no time, path name or toll. Nothing in this comp is red.
6. The card and the paper strip carry bars, not words: no retyped warning text, no time.
7. Nothing appears before its spoken word, except that South Bend's dot and label are on in the first frame (the place the acts have held). Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom. No label on a county line: read `Fort Wayne` against Allen County's lines at 2.60.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `South Bend` · `Fort Wayne` · `Weather Bureau ·` / `Fort Wayne` · `a town` · `the warning`.
Cue words and times are from `audio/a4-s16.words.json` (28 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S16 -0.21) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S16 | 0 | and | 0.21 | 0.00 | first frame: ground, the map in NORTH, South Bend's dot and label in Body light. Nothing else |
| 1 | A4-S16 | 1 | one | 0.34 | 0.13 | South Bend's dot and label dim to `#55606b` (0.4 s) |
| 2 | A4-S16 | 7 | Fort | 2.12 | 1.91 | Fort Wayne's dot turns on in Amber 2 with its one ring (0.45 s); the label `Fort Wayne` fades in |
| 3 | A4-S16 | 9 | Weather | 2.58 | 2.37 | the link draws from the dot down to the teletype (0.4 s); the teletype draws on (0.5 s) and its label fades in |
| 4 | A4-S16 | 13 | typing | 3.60 | 3.39 | the paper strip starts to come out of the teletype (group `y` 80 to 0, ease none, 3.39 to 5.90) |
| 5 | A4-S16 | 14 | warnings | 3.92 | 3.71 | the first bar has cleared the slot (it rides on the paper) |
| 6 | A4-S16 | 16 | storms | 4.54 | 4.33 | the second bar has cleared the slot |
| 7 | A4-S16 | 20 | gone | 5.62 | 5.41 | the third bar has cleared the slot; the paper stops at 5.90 |
| 8 | A4-S16 | 22 | Later | 7.28 | 7.07 | the schematic line draws from the left (0.3 s), the town and `a town` fade in, and the tornado mark fades in at point x 200 and runs to x 1150 (ease none, to 8.60), then drifts to x 1210 by 10.31 |
| 9 | A4-S16 | 25 | some | 8.52 | 8.31 | the message card leaves the paper strip and flies to its rest place (0.5 s, power2.inOut, lands 8.81) |
| 10 | A4-S16 | 27 | after. | 8.98 | 8.77 | 0.1 s later the leader and the label `the warning` fade in (0.25 s). Hold on the card to 10.31 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s16-fortwayne.html` is the only file the builder writes; `data-composition-id="g-a4s16-fortwayne"`, `data-duration="10.31"`; id prefix `ftw-`; root `<div id="ftw-root" ...>` styled through `#ftw-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Family base it copies:** `compositions/g-a2s14-six.html` (wave 1), after it has passed its read: the inlined and prefixed BM-1 block, the NORTH box and viewBox, the town dot and label type, the tornado mark. It adds no camera move. `compositions/g-a5s01-radar.html` (wave 4) opens on this comp's map state: Fort Wayne's dot and its teletype.
**Assets (paths from the episode folder, read on disk 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880), inlined.
- `media/drawings/teletype.svg` (DR-01, object 140 x 140, viewBox -6 -6 152 152, line 4).
- `media/drawings/tornado-mark.svg` (DR-03, object 60 x 80, viewBox -6 -6 72 92, line 6).
Mount rules: `media/drawings/README.md` and `media/maps/README.md`, which win over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s16-fortwayne`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: the card's `x`, `y` and `scale`, the strip group's `y` and the mark's `x` are set at timeline 0; capture 8.55 (card in flight, mark past the town) both ways. Line 5 here: read the card's flight path against the teletype label and the tornado mark at 8.45 and 8.65. Line 6 here: both dots, the Allen County box and the mark's position at 7.88 and 8.31 are computed by a script from `media/data/points.csv` and the cue table and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map lines, South Bend lit, nothing else. Then: 0.70 (South Bend dim), 2.50 (Fort Wayne amber, label on no line), 3.10 (link and teletype, label inside x 1565), 4.60 (paper 38.6 px out, two bars), 6.00 (paper at full height, three bars, 8 px under the map box), 7.50 (line, town, mark west of the town), 8.20 (mark east of the town, no card yet), 8.55 (card in flight), 9.20 (card at rest above the town, leader and `the warning`), 10.20 (last frame).
