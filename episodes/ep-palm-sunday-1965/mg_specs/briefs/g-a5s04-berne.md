Host: id=g-a5s04-berne file=compositions/g-a5s04-berne.html start=846.18 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=18.70 s track=2

# g-a5s04-berne · A5-S4, A5-S5 · The tornado reaches the Ohio line in 12 minutes; the warning ran 30 to 60 (wave 4, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a row DR-11. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves, so every town label fades before the push and returns after it (rule 2). The root is styled through its id, never `id="root"` (rule 3). A flash is a stroke or fill change, never a scale pop (rule 12). Beat counts are checked against the window (rule 13). Map geometry comes from the file (rule 14). No map shows Alto; inlined ids take this comp's prefix; line weight is read after the push (rule 20). Real places are named here, so `County A` and `County B` never appear. A zone is never written beside a time.
**Spoken (A5-S4):** "Curran later wrote that the man in charge, Clyde Downes, issued it straight off the radar. The Bureau's own survey has that tornado over Linn Grove at eight forty, and across the Ohio line near eight fifty two."
**Spoken (A5-S5):** "A warning for the next hour was covering a tornado with about twelve minutes left in Indiana."
**One look:** the tornado mark stands on Linn Grove at 8:40 PM and reaches the state line near 8:52 PM; under the map a long amber bar for the warning runs far past the line and a short red bar of 12 minutes stops at it, both on one scale.

## 0. What this graphic claims
By John Curran's recollection the 8:40 warning was issued straight off Fort Wayne's radar. By the Weather Bureau's survey the tornado was over Linn Grove at 8:40 PM and crossed into Ohio near 8:52 PM. The warning named "the next 30 to 60 minutes"; the tornado had about 12 minutes left in Indiana.

## 1. Source
- `edit_script.md` A5-S4, Rows [E, Downes; Curran's recollection; survey printed p. 45 for the name] · [A20; survey printed p. 45]. A5-S5, Rows [A20] (8:40 to near 8:52: twelve minutes; the warning's own words, survey printed p. 43: "for the next 30 to 60 minutes").
- Positions, map units (`media/data/points.csv`): `pt-fort-wayne` (605.1, 297.0), `pt-berne` (629.0, 376.8), `pt-linn-grove` (619.0, 379.1). Indiana's east line read off `st-in` in `media/maps/indiana-counties.svg`: x 648.4 between y 280 and 450.
- The leg from Linn Grove to the state line is SCHEMATIC: the survey gives two places and two times, not a surveyed track. It is the straight leg the family uses in `g-a5s07-marion` and `g-a5s10-alert`, meeting the line at map (648.4, 369.6).

## 2. Datum, scale, orientation
North is up. One map box for both states: left 716, top 62, 1080 x 450.
| State | Box | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| EAST (new in wave 4, shared with `g-a5s07-marion` and `g-a5s10-alert`) | 716, 62, 1080 x 450 | `330 284 384 160` | 2.8125 (screen x = 2.8125u - 212.125, y = 2.8125u - 736.75) | frame 0 to A5-S4 word 16 |
| LINE (this comp only) | same box | `550 328 270 112.5` | 4.0 (screen x = 4u - 1484, y = 4u - 1250) | after the push, to the end |
The push EAST to LINE is 1.422 times: a plain tween of the viewBox proxy with `onUpdate`, 0.8 s, power2.inOut, end values set exactly. Dot `r` is tweened with it: 2.133 map units in EAST, 1.5 in LINE (6 px on screen in both).
Time scale for the bars: 9.8 px per minute. It is the map's own: Linn Grove's dot and the state line are 117.6 px apart in LINE, and the survey gives 12 minutes between them. Bars start at x 992 (Linn Grove's x): 12 minutes ends at x 1109.6 (the state line), 30 minutes at x 1286, 60 minutes at x 1580.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `brn-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px, non-scaling. Every `pt-` group hidden except Fort Wayne, Berne and Linn Grove. No county is lit and no county is named in this comp |
| EAST, frame 0 | Fort Wayne dot (1489.7, 98.6); label `Fort Wayne` right aligned to x 1441, top 88. Berne dot (1556.9, 323.0); label `Berne` right aligned to x 1544, top 312. Town labels Arial 700 22 px, Body light |
| Radar ring | overlay SVG centred on Fort Wayne's dot, as `g-a2s01-radar` but radius 36 and 20 (so the ring stays inside the box top at y 62: it spans y 62.6 to 134.6), Body light 3 px, one sweep line from the centre to the outer circle, at rest pointing up |
| Recollection chip | glass chip, left 96, top 96, height 46, padding 0 x 22, Arial 700 26 px, Body light: `John Curran's recollection` |
| Source line | left 716, top 524, Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey, 1965, pp. 43 and 45` |
| LINE, after the push | Linn Grove dot (992.0, 266.4); label `Linn Grove` right aligned to x 974, top 272 (below and west of the dot, by hand: the two dots are 41 px apart). Berne dot (1032.0, 257.2); label `Berne` left 1042, top 268 (below and east). State line x 1109.6, top to bottom of the box. Fort Wayne is above the box in LINE and is not shown |
| Tornado mark | `media/drawings/tornado-mark.svg` inline in an overlay SVG at 0.75 scale (45 x 60 px), group stroke Body light, never red. Its lowest point sits 12 px above the point it marks. At Linn Grove: box x 969.5 to 1014.5, y 194.4 to 254.4. At the line, marking (1109.6, 228.5): box x 1087.1 to 1132.1, y 156.5 to 216.5 |
| Trail | one straight line from (992.0, 266.4) to (1109.6, 228.5), Body light at 60 %, 3 px, drawn behind the mark as it moves. It passes 3.7 px north of Berne's dot |
| `8:40 PM` chip | glass chip, height 46, centred on x 992, top 136 (12 px above the mark) |
| `near 8:52 PM` chip | glass chip, height 46, left 1150, top 164 (east of the line, beside the mark) |
| State names | Arial 700 22 px, Label grey, tracking 6: `INDIANA` right aligned to x 1089, top 80; `OHIO` left 1130, top 80 |
| Line highlight | the part of `st-in` on x 1109.6 goes from Body light 3 px to Headline white 5 px (a stroke change), drawn as one vertical overlay line x 1109.6, y 62 to 512 |
| Guides | two dashed verticals, Label grey 2 px, dash 6 6: x 992 and x 1109.6, from y 512 to y 742 |
| Amber bar (the warning) | top 620, height 40, Amber 2. Solid from x 992 to x 1286 (30 minutes); Amber 2 at 45 % from x 1286 to x 1580 (60 minutes). Tick labels under it, Arial 700 20 px, Label grey, top 668: `30 min` centred on x 1286, `60 min` right aligned to x 1580 |
| Red bar (the tornado) | top 702, height 40, Popfig red, x 992 to x 1109.6 (12 minutes) |
| Bar labels | Arial 700 26 px, right aligned to x 968: `warning: the next 30 to 60 minutes` Amber 2, top 625; `12 minutes` Headline white, top 707 |
The bars end at x 1580 and the lowest element is the red bar (bottom 742): the presenter corner (x >= 1600, y >= 680) stays empty.

## 4. Must be true in the picture
1. `John Curran's recollection` is on screen under the first sentence only: in at "later", out at "The" (5.94). It is never on screen with either time chip or the source line.
2. The ring is at Fort Wayne and turns once on "straight"; no ring anywhere else. Clyde Downes is not named or drawn.
3. The mark stands on Linn Grove, not on Berne, when `8:40 PM` appears. Linn Grove is west of Berne and both are west of the state line.
4. The mark moves east and a little north to the state line and stops with its marked point on the line. It never crosses deeper into Ohio in this comp.
5. `near 8:52 PM` keeps the word `near`. Neither chip carries a zone.
6. The red bar's right end is on the same x as the state line on the map above it (x 1109.6), and both bars start on Linn Grove's x (992): the guides show it.
7. The amber bar is 2.5 times the red bar's length at 30 minutes (294 px against 117.6 px) and 5 times at 60 (588 px). The 60 minute part is lighter than the 30 minute part.
8. Beat check: two times, two bars, each from its spoken word; the last change (the red bar) is at 16.03 and holds 2.67 s to the end.
9. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom; line weights after the push are still 1.5, 2 and 3 px.

## 5. Text (exact) and cues
Text: `Fort Wayne` · `Berne` · `Linn Grove` · `John Curran's recollection` · `Weather Bureau survey, 1965, pp. 43 and 45` · `8:40 PM` · `near 8:52 PM` · `INDIANA` · `OHIO` · `warning: the next 30 to 60 minutes` · `30 min` · `60 min` · `12 minutes`.
Cue words and times are from `audio/a5-s4.words.json` and `audio/a5-s5.words.json` as they stood on 12 Oct 26. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A5-S4 0.00, A5-S5 13.09) plus the word's time; a segment's first word uses table 5's first sound (0.00, 13.36). Retime from the word, never from the seconds. The transcriber writes "Curran" as "Cohen", and the two times as "840" and "852.".
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S4 | 0 | Cohen | first sound 0.00 | 0.00 | first frame: ground, the map in EAST, Fort Wayne's dot, label and resting ring, Berne's dot and label |
| 1 | A5-S4 | 1 | later | 0.24 | 0.24 | chip `John Curran's recollection` fades in (0.3 s, `y: 12` to 0) |
| 2 | A5-S4 | 12 | straight | 3.96 | 3.96 | the ring's sweep line turns one turn (1.8 s, ease none, to 5.76) |
| 3 | A5-S4 | 16 | The | 5.94 | 5.94 | the chip, the ring and both town labels fade (0.2 s); from 6.14 the push EAST to LINE (0.8 s, to 6.94); then `Berne` returns at its LINE place and the source line fades in (0.3 s) |
| 4 | A5-S4 | 24 | Linn | 8.34 | 8.34 | Linn Grove's dot and label (0.3 s), the tornado mark fades in over it (0.3 s) |
| 5 | A5-S4 | 27 | 840 | 9.08 | 9.08 | chip `8:40 PM` (0.3 s, `y: 12` to 0) |
| 6 | A5-S4 | 29 | across | 10.14 | 10.14 | the mark moves to the state line (1.1 s, power1.inOut, to 11.24); the trail draws behind it |
| 7 | A5-S4 | 31 | Ohio | 10.60 | 10.60 | `INDIANA` and `OHIO` fade in (0.3 s); the line highlight comes on (stroke change, 0.3 s) |
| 8 | A5-S4 | 34 | 852. | 11.48 | 11.48 | chip `near 8:52 PM` (0.3 s) |
| 9 | A5-S5 | 0 | A | first sound 0.27 | 13.36 | the two guides draw down from the map (0.4 s) |
| 10 | A5-S5 | 1 | warning | 0.40 | 13.49 | the amber bar grows from x 992: to x 1286 in 0.6 s, then the lighter part to x 1580 in 0.6 s (`scaleX`, origin left); its label and the two tick labels fade in |
| 11 | A5-S5 | 12 | 12 | 2.94 | 16.03 | the red bar grows from x 992 to x 1109.6 (0.4 s, power2.out); `12 minutes` fades in. Hold to the last frame (18.70) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s04-berne.html` is the only file the builder writes; `data-composition-id="g-a5s04-berne"`; id prefix `brn-`; root `<div id="brn-root" ...>` styled through `#brn-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (brief `mg_specs/briefs/g-a2s14-six.md`) for the mount, the inlining and prefixing, the push maths and the dot radius; the ring from `compositions/g-a2s01-radar.html`; the bars on one stated scale from `compositions/g-a2s06-headstart.html`; the tornado mark's mount (0.75 scale, 12 px above its dot) from the family's track comps. The EAST state is defined once, in section 2 of this brief, and is the same in `g-a5s07-marion` and `g-a5s10-alert`.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/drawings/tornado-mark.svg` (DR-11, object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined once.
- `media/data/points.csv` is the source of the three positions; it is read, not mounted.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s04-berne`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 6.50 (mid push) and 10.70 (mark mid move) forward and backward and match the frames. Line 6: the three town positions in both states, the line's x and the bar ends are computed from `media/data/points.csv`, the `st-in` path and the section 2 numbers by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus: the measured x of the red bar's right end and of the state line in one frame (both 1109.6 asked), and the measured width of `warning: the next 30 to 60 minutes` (it must start at or right of x 96).

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): EAST, Fort Wayne with its ring, Berne, line weights. Then one settled frame per cue: 0.70 (recollection chip), 4.80 (sweep turning), 7.40 (LINE state, chip gone, source line), 8.80 (Linn Grove and the mark), 9.50 (`8:40 PM`), 10.70 (mark mid move), 11.30 (mark on the line, state names), 12.00 (`near 8:52 PM`), 13.45 (guides), 15.00 (amber bar complete), 16.60 (red bar and `12 minutes`), 18.60 (last frame).
