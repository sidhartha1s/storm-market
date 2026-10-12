Host: id=g-a5s10-alert file=compositions/g-a5s10-alert.html start=906.75 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=17.99 s track=2

# g-a5s10-alert · A5-S10, A5-S11 · Four counties put on alert after the tornado had left; the 9:07 phone call (wave 4, map family with a film window)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a row DR-11, section 6 item 13. Times: `mg_specs/timeline-map.md` tables 1, 3 and 5. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). While film shows, the film label is the only chip on screen (rule 4). A flash is a stroke or fill change (rule 12). Beat counts are checked against the window (rule 13). Map geometry comes from the file (rule 14). The film is mounted under this comp by the orchestrator in `index.html`, never by the builder; it is never frozen, slowed or looped (rule 15). No map shows Alto; inlined ids take this comp's prefix; county names that crowd are placed by hand (rule 20). The four counties are named by the Weather Bureau's own message, so `County A` and `County B` never appear. A zone is never written beside a time.
**Spoken (A5-S10):** "With that message Fort Wayne put four counties on alert for a storm moving east. The tornado had already crossed three of them and left Indiana."
**Spoken (A5-S11):** "The reason was a phone call. Word from Marion reached Fort Wayne's signal department at nine oh seven, about an hour after the tornadoes hit."
**One look:** four counties light at 9:20 PM; the storm's path already runs through three of them and the tornado mark stands in Ohio at 8:52 PM; a few seconds of a telephone on film; then 9:07 PM on the map, word from Marion reaching Fort Wayne.

## 0. What this graphic claims
At 9:20 PM Fort Wayne's office put Wells, Adams, Blackford and Jay counties on alert for eastward movement. By the Bureau's survey the tornado had already crossed Blackford, Wells and Adams and entered Ohio near 8:52 PM. The office learned of Marion by a report through Fort Wayne's signal department at 9:07 PM, about an hour after Marion was hit.

## 1. Source
- `edit_script.md` A5-S10, Rows [A22; survey printed p. 43: "under alert for eastward movement"] · [survey printed p. 45: across Blackford, Wells and Adams, into Ohio near 8:52]. A5-S11, Rows [A22; survey printed p. 43: "reported through the Fort Wayne signal department at 9.07 PM EST"] · [C16, Curran: "a tornado that had passed through an hour earlier"].
- The message's order of the counties (survey printed p. 43): Wells, Adams, Blackford, Jay.
- Positions, map units (`media/data/points.csv`): `pt-fort-wayne` (605.1, 297.0), `pt-marion` (539.5, 396.7), `pt-linn-grove` (619.0, 379.1). County shapes: paths `co-in-wells`, `co-in-adams`, `co-in-blackford`, `co-in-jay` in `media/maps/indiana-counties.svg` (ids read from the file on 12 Oct 26). Indiana's east line: x 648.4.
- The path is SCHEMATIC, the same construction as `g-a5s07-marion`: a point 8 map units south of Marion's dot (539.5, 404.7), Linn Grove, the state line at (648.4, 369.6). Checked by script against the county boxes: it runs 8.4 map units (23.6 px) inside Blackford's north-west corner, then Wells, then Adams (Linn Grove is in Adams). It never enters Jay.
- Film: `media/films/cuts/a14-08-telephone-call.mp4`, a cut of the 1967 civil defense training film. It stands for a telephone call. It is not Fort Wayne's office and the label says only what the film is.

## 2. Datum, scale, orientation
North is up. No camera move.
| State | Box | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| EAST (shared with `g-a5s04-berne` and `g-a5s07-marion`) | left 716, top 62, 1080 x 450 | `330 284 384 160` | 2.8125 (screen x = 2.8125u - 212.125, y = 2.8125u - 736.75) | 0.00 to 8.83 and 11.03 to the end |
| FILM | hole x 480 to 1440, y 150 to 870 | none | none | 8.83 to 11.03 |
County boxes in EAST, screen px (top-left, bottom-right, centre): Wells (1380.6, 187.7) (1516.7, 370.0) (1448.7, 278.8); Adams (1514.8, 185.2) (1611.8, 369.4) (1563.3, 277.3); Blackford (1381.4, 369.7) (1469.2, 468.1) (1425.3, 418.9); Jay (1462.4, 367.2) (1611.8, 505.3) (1537.1, 436.2).
Clock hands at 9:07, degrees clockwise from 12: hour 273.5, minute 42.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `alr-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px, non-scaling. Every `pt-` group hidden except Fort Wayne and Marion. Dot radius 6 px (`r` 2.133 map units), Body light |
| Fort Wayne | dot (1489.7, 98.6); label `Fort Wayne` left 1503, top 87. Town labels Arial 700 22 px, Body light |
| Lit counties | Wells, Adams, Blackford, Jay: fill Amber 2 at `fill-opacity` 0.45 (the family's lit county), a fill change on the county's own path |
| County names | Arial 700 22 px, Headline white with the credit shadow, tracking 2, centred on the box centre: `WELLS` (1448.7, 278.8), `ADAMS` (1563.3, 277.3), `JAY` (1537.1, 436.2). `BLACKFORD` is wider than its county (87.8 px), so by hand: right aligned to x 1456, top 474 (under the county's south line), with a 2 px Body light leader from (1425, 470) up to (1425, 444) |
| Alert chip | glass chip, left 96, top 96, height 46, padding 0 x 22, Arial 700 26 px, Body light: `9:20 PM · on alert` |
| Marion | dot (1305.2, 379.0); label `Marion` left 1317, top 350 in A5-S10 |
| Path | one polyline in the map SVG, Body light 4 px, non-scaling, round joins: screen (1305.2, 401.5), (1528.8, 329.5), (1611.5, 302.8). Never red, no arrowhead |
| Tornado mark | `media/drawings/tornado-mark.svg` inline in an overlay SVG at 0.75 scale (45 x 60 px), group stroke Body light. It marks the point (1640.0, 293.6), 28.5 px past the state line on the same leg: box x 1617.5 to 1662.5, y 221.6 to 281.6 |
| `OHIO` | Arial 700 22 px, Label grey, tracking 6, left 1626, top 180 |
| Ohio chip | glass chip, height 46, right aligned to x 1796, top 524 (under the map box, y 524 to 570): `8:52 PM · already in Ohio` |
| Film view ground | four opaque gradient panels round a transparent hole x 480 to 1440, y 150 to 870, exactly as `g-a1s15-offices` |
| Film frame | 4 px Body light, outer x 476 to 1444, y 146 to 874 |
| Film label | glass chip, left 480, top 886, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Civil defense training film, 1967` |
| Hole cover | a fifth opaque panel x 480 to 1440, y 150 to 870 in the ground's colours, put on in one frame |
| Link | one dotted line Marion's dot to Fort Wayne's dot, (1305.2, 379.0) to (1489.7, 98.6), 335.7 px, Body light 3 px, dash 2 10, round caps, no arrowhead |
| Marion ring | one circle radius 14 px round Marion's dot, Headline white 3 px, no fill |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `WORD FROM MARION` / `9:07 PM` / `Fort Wayne signal department`; hands 273.5 and 42 |
| Marion chip (A5-S11) | glass chip, height 46, right aligned to x 1285, top 356: `tornadoes hit near 8:00 PM`. Label `Marion` moves to left 1317, top 386 for this half (set, not tweened: it returns after the film) |
The Ohio chip and the mark are right of x 1600 but above y 680; the stamp, the chips and the film label are left of x 1600: the presenter corner (x >= 1600, y >= 680) stays empty.

## 4. Must be true in the picture
1. Exactly four counties light, in the message's order: Wells, Adams, Blackford, Jay. Grant, Allen and Howard never light.
2. The path crosses three of the four (Blackford at its north-west corner, Wells, Adams) and does not enter Jay. It reaches the state line and the mark stands east of it, in Ohio.
3. `9:20 PM · on alert` and `8:52 PM · already in Ohio` are on screen together from 7.13 to 8.83: the later time on the alert, the earlier on the tornado.
4. The film view is a hard cut in and a hard cut out. From 8.83 to 11.03 the only words on screen are `Civil defense training film, 1967`. No map, no chip, no stamp shows through or round the hole.
5. The film's first frame after the cut is the mount's first frame (the mount starts at 8.83, the cut is at 8.83). The comp holds no `<video>` and no `src` to the film.
6. After the film the map returns with Fort Wayne and Marion only: no lit county, no path, no mark, no chip from A5-S10.
7. The stamp reads `9:07 PM`: hour hand just past 9, minute hand between the 1 and the 2 (42 degrees). Its place line names the signal department, as the message does.
8. The link runs between Marion and Fort Wayne and nowhere else; it is dotted, never a solid track.
9. Beat check: the film window is open 2.20 s (8.83 to 11.03). That is long enough to read one picture (a telephone call) and at the floor for the label's five words. The narration's first sentence ends at 10.21, so the last 0.82 s of the window is film with no words spoken. If the lead wants it longer, the cut back can move to A5-S11 word 9 "reached" (11.59 from comp start, 2.76 s open) and stays inside the mount, which ends at 13.00; steps 6 and 7 below then both fire at 11.59.
10. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom.
11. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry. As built, pending its reader (lead, 13 Oct 26): the map box stays open to the last frame, tall as in the file saved at 00:11 (to y 660, and to y 984 left of x 1580, from x 620); this brief's last frame, with the 450 px box, leaves 52.6 % of the frame bare for 6.96 s.

## 5. Text (exact) and cues
Text: `Fort Wayne` · `WELLS` · `ADAMS` · `BLACKFORD` · `JAY` · `9:20 PM · on alert` · `Marion` · `OHIO` · `8:52 PM · already in Ohio` · `Civil defense training film, 1967` · `WORD FROM MARION` · `9:07 PM` · `Fort Wayne signal department` · `tornadoes hit near 8:00 PM`.
Cue words and times are from `audio/a5-s10.words.json` and `audio/a5-s11.words.json` as they stood on 12 Oct 26. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A5-S10 -0.27, A5-S11 8.35) plus the word's time; a segment's first word uses table 5's first sound (0.00, 8.83). Retime from the word, never from the seconds. The transcriber writes "nine oh seven" as "907,".
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S10 | 0 | With | first sound 0.27 | 0.00 | first frame: ground, the map in EAST (lines only), Fort Wayne's dot and label |
| 1 | A5-S10 | 6 | four | 1.78 | 1.51 | the four counties fill, 0.2 s apart in the message's order (each a 0.3 s fill change), each name with its county |
| 2 | A5-S10 | 9 | alert | 2.64 | 2.37 | chip `9:20 PM · on alert` fades in (0.3 s, `y: 12` to 0) |
| 3 | A5-S10 | 16 | tornado | 5.40 | 5.13 | Marion's dot and label (0.2 s); the path draws west to east (1.2 s, `strokeDashoffset`, to 6.33) |
| 4 | A5-S10 | 24 | left | 7.40 | 7.13 | the tornado mark and `OHIO` fade in east of the line (0.3 s); chip `8:52 PM · already in Ohio` (0.3 s) |
| 5 | A5-S11 | 0 | The | first sound 0.48 | 8.83 | hard cut to the film view in one frame: map, dots, names, path, mark and both chips off; ground with the hole, frame and film label on |
| 6 | A5-S11 | 6 | Word | 2.68 | 11.03 | hard cut back in one frame: hole cover on, frame and film label off; the map returns with Fort Wayne and Marion only (`Marion` at its second place) |
| 7 | A5-S11 | 8 | Marion | 2.92 | 11.27 | the ring comes on round Marion's dot (stroke change, 0.2 s); the link draws from Marion to Fort Wayne (0.8 s, to 12.07) |
| 8 | A5-S11 | 15 | 907, | 5.38 | 13.73 | clock stamp slides in from the left (`x: -660` to 0, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees to 42 |
| 9 | A5-S11 | 16 | about | 6.70 | 15.05 | chip `tornadoes hit near 8:00 PM` fades in beside Marion's dot (0.3 s). Hold to the last frame (17.99) |

Film mount (the orchestrator's, in `index.html`; `mg_specs/timeline-map.md` table 3, id `v-a5s11-call`):
| Film mount | File | Starts in comp | Mounted | Ends in comp | Window open | Used of the file |
|---|---|---|---|---|---|---|
| `v-a5s11-call` | `media/films/cuts/a14-08-telephone-call.mp4` (4.17 s) | 8.83 | left 480, top 150, 960 x 720, track 1, class `filmwin`, muted | 13.00 | 8.83 to 11.03 | its first 2.20 s; the rest plays under the hole cover |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s10-alert.html` is the only file the builder writes; `data-composition-id="g-a5s10-alert"`; id prefix `alr-`; root `<div id="alr-root" ...>` styled through `#alr-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. The builder does not edit `index.html` and does not mount the film.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (brief `mg_specs/briefs/g-a2s14-six.md`) for the mount, the inlining and prefixing, the lit county and the stamp; the film view (ground panels, hole, frame, label, hole cover, hard cuts) from `compositions/g-a1s15-offices.html`. The EAST state and the path are the same as in `g-a5s07-marion`.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/drawings/tornado-mark.svg` (DR-11, object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined once.
- The stamp's clock face: `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124) inline, or the face of `compositions/g-t1s2-warning.html`.
- Under the comp, not mounted by it: `media/films/cuts/a14-08-telephone-call.mp4` (4.17 s, 640 x 480).

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s10-alert`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. Viewed alone, the hole shows the checker or black: that is correct.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 8.80, 8.84, 11.00 and 11.04 forward and backward and match the frames (the two hard cuts land on the same frame both ways). Line 6: the county boxes, the path's three points and both dots are computed from the file and `media/data/points.csv` with the section 2 numbers by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus: the measured width of `BLACKFORD` and whether it clears Jay's lit fill, and the length of the path inside Blackford in a frame (23.6 px asked).

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): EAST lines, Fort Wayne, line weights. Then one settled frame per cue: 2.30 (four counties lit and named), 3.00 (alert chip), 6.50 (path complete, Marion), 7.80 (mark in Ohio, both chips), 8.84 (first film frame, label the only chip), 10.90 (film still moving), 11.04 (map back, counties unlit, no chips), 12.30 (ring and link), 14.60 (stamp at 9:07), 15.60 (Marion chip), 17.90 (last frame). The film frames are read in the full episode preview, over the mounted film.
