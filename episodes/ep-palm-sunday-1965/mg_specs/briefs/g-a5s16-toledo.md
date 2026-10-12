Host: id=g-a5s16-toledo file=compositions/g-a5s16-toledo.html start=955.97 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=19.27 s track=2

# g-a5s16-toledo · A5-S16, A5-S17 · Toledo at 9:30 PM: its own Weather Bureau office, never warned, 18 lives lost; one mention from Columbus (wave 4, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a row DR-11, section 6 item 7. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). A flash is a stroke or fill change (rule 12). Beat counts are checked against the window (rule 13). Map geometry comes from the file (rule 14). No map shows Alto; inlined ids take this comp's prefix (rule 20). No county chip appears in this comp. A zone is never written beside a time.
**Spoken (A5-S16):** "At nine thirty that night, a tornado started in northern Toledo, Ohio, a city with its own Weather Bureau office. The Weather Service says it was never warned for, and eighteen people there lost their lives."
**Spoken (A5-S17):** "It got one mention, not a warning, from the Weather Bureau in Columbus, ten minutes before it struck."
**One look:** our own map of Ohio with one dot, Toledo, at 9:30 PM; the toll, 18; then a second dot, Columbus, joined to Toledo by a dotted line, and the words "a mention".

## 0. What this graphic claims
A tornado started in northern Toledo, Ohio, at 9:30 PM. Toledo had its own Weather Bureau office. By the National Weather Service's account the tornado was never warned for and 18 people there lost their lives. The only mention it got came from the Columbus weather office ten minutes before it struck.

## 1. Source
- `edit_script.md` A5-S16, Rows [B table: 18; start 0230 UTC, nine thirty is that time converted] · [survey table of contents: a Toledo log] · [C18; the National Weather Service narrative]. Ohio's source is the National Weather Service, not the study, and no cause is claimed. A5-S17, Rows [C18: "The only mention the storm got was from the Columbus weather office ten minutes before the twister struck"]. No source says how the message travelled.
- Plan section 6 item 7: our own Ohio map with a dot for Toledo; the track map is not shown.
- Positions, map units of `media/maps/midwest-states.svg` (`media/data/points.csv`): `pt-toledo` (803.5, 190.8), `pt-columbus` (879.4, 501.2). Ohio's shape `st-oh`: box x 646.2 to 1192.7, y 133.0 to 793.3.
- The dot marks the city. "Northern Toledo" is not resolved at this scale and is said in words only.

## 2. Datum, scale, orientation
North is up. No camera move.
| State | Box | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| OHIO (this comp only) | left 700, top 62, 811.3 x 900 (right 1511.3, bottom 962) | `616 110 640 710` on BM-2 | 1.2676 (screen x = 1.2676u - 80.8, y = 1.2676u - 77.4) | whole comp |
On screen: Ohio's shape spans (738.3, 91.2) to (1431.0, 928.2); its west line (Indiana) is at x 741.1; Toledo (937.7, 164.4); Columbus (1033.9, 557.9); the two are 405.1 px apart. Fort Wayne would fall at (686.2, 299.0), outside the box: it is not drawn.
Clock hands at 9:30, degrees clockwise from 12: hour 285, minute 180.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-2 group `map-states` inlined with ids prefixed `tol-`, in one SVG in the OHIO box, `preserveAspectRatio="xMidYMid meet"`. `st-oh`: fill Panel dark, outline Body light 3 px. Every other state: no fill, outline Label grey 2 px. All strokes non-scaling. Group `map-points`: every `pt-` hidden except `pt-toledo` and, from its cue, `pt-columbus`; their `r` set to 4.73 map units (6 px on screen; the file's own `r` is 15.8), fill Body light |
| `OHIO` | Arial 700 22 px, Label grey, tracking 6, centred on x 1085, top 700 (inside the state, south of Columbus) |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `A TORNADO STARTS` / `9:30 PM` / `Toledo, Ohio`; hands 285 and 180 |
| Toledo | dot (937.7, 164.4); label `Toledo`, Arial 700 22 px, Body light, left 972, top 153 |
| Tornado mark | `media/drawings/tornado-mark.svg` inline in an overlay SVG at 0.75 scale (45 x 60 px), group stroke Body light, never red; its lowest point 12 px above Toledo's dot: box x 915.2 to 960.2, y 92.4 to 152.4 |
| Office chip | glass chip, left 96, top 320, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Toledo had its own Weather Bureau office` (about 616 px wide: it ends near x 712, over Indiana's unlit edge and clear of Ohio's west line at x 741.1) |
| Map dim | scrim `rgba(3,5,8,0.45)` over the map box only (700, 62, 811.3 x 900) |
| Toll plate | glass plate as `compositions/g-i1s2-station.html` `.stn-card`: left 96, top 384, 590 x 270 (bottom 654) |
| Toll figure | `18` in the popfig type of `compositions/g-t1s1-toll.html` (`.toll-num`, AbrilFig 150 px, Popfig red), left 138, top 392 |
| Toll label | two lines, Arial Black 900 38 px, Headline white, tracking 0.2em, no `text-transform`, left 138: `lives lost` top 554, `northern Toledo` top 604 |
| Source line | left 96, top 690, Arial 700 20 px, Body light with the credit shadow: `National Weather Service` |
| Columbus | dot (1033.9, 557.9); label `Columbus`, Arial 700 22 px, Body light, left 1046, top 547 |
| Dotted line | Toledo's dot to Columbus's dot, (937.7, 164.4) to (1033.9, 557.9), Body light 3 px, dash 2 10, round caps, no arrowhead at either end |
| Columbus chip | glass chip of two lines, left 96, top 320, height 92, padding 0 x 22, each line Arial 700 26 px, Body light: `Columbus weather office` / `a mention, ten minutes before` |
The map box ends at x 1511.3 and everything on the left ends at x 712 or less: the presenter corner (x >= 1600, y >= 680) stays empty.

## 4. Must be true in the picture
1. The map is ours (BM-2), Ohio the one filled state. The track map is not shown, and no storm path is drawn anywhere.
2. Toledo is the only dot until "Columbus". Fort Wayne is not drawn and no line joins Toledo to Fort Wayne or to anything in Indiana.
3. The stamp reads `9:30 PM` and `Toledo, Ohio`: hour hand halfway from 9 to 10, minute hand on the 6. No zone beside the time.
4. The toll reads `18`, `lives lost`, `northern Toledo`, on glass, and appears on "eighteen", not before. The figure is Popfig red; the tornado mark is not.
5. `National Weather Service` is on screen from "never" to the last frame: both the "never warned for" and the Columbus mention are its account.
6. The dotted line between Toledo and Columbus fades in whole. It does not grow from either end and has no arrowhead: no source says how the message travelled.
7. The Columbus chip says `a mention`, never "warning". The word "warning" appears nowhere in this comp.
8. Beat check: the Columbus chip lands at 16.43 and holds 2.84 s; the toll is on screen 3.14 s (9.58 to 12.72).
9. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom.

## 5. Text (exact) and cues
Text: `OHIO` · `A TORNADO STARTS` · `9:30 PM` · `Toledo, Ohio` · `Toledo` · `Toledo had its own Weather Bureau office` · `18` · `lives lost` · `northern Toledo` · `National Weather Service` · `Columbus` · `Columbus weather office` / `a mention, ten minutes before`.
Cue words and times are from `audio/a5-s16.words.json` and `audio/a5-s17.words.json` as they stood on 12 Oct 26. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A5-S16 -0.44, A5-S17 12.29) plus the word's time; a segment's first word uses table 5's first sound (0.00, 12.72). Retime from the word, never from the seconds. The transcriber writes "nine thirty" as "9" and "30", "eighteen" as "18" and "ten" as "10".
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S16 | 0 | At | first sound 0.44 | 0.00 | first frame: ground, the map in OHIO (Ohio filled, neighbours in outline), `OHIO`, no dot |
| 1 | A5-S16 | 1 | 9 | 0.56 | 0.12 | clock stamp slides in from the left (`x: -660` to 0, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees onto the 6 |
| 2 | A5-S16 | 10 | Toledo, | 3.38 | 2.94 | Toledo's dot and label (0.3 s); the tornado mark fades in over it (0.3 s) |
| 3 | A5-S16 | 14 | with | 4.94 | 4.50 | chip `Toledo had its own Weather Bureau office` fades in (0.3 s, `y: 12` to 0) |
| 4 | A5-S16 | 26 | never | 8.64 | 8.20 | the scrim dims the map (0.4 s); the source line fades in |
| 5 | A5-S16 | 30 | 18 | 10.02 | 9.58 | toll plate fades in (0.25 s) with `18`; the two label lines 0.15 s apart |
| 6 | A5-S17 | 0 | It | first sound 0.43 | 12.72 | the toll plate and its text, the scrim and the office chip fade out (0.3 s) |
| 7 | A5-S17 | 12 | Columbus | 3.68 | 15.97 | Columbus's dot and label (0.3 s); the dotted line fades in whole (0.4 s) |
| 8 | A5-S17 | 13 | 10 | 4.14 | 16.43 | the Columbus chip fades in (0.3 s, `y: 12` to 0). Hold to the last frame (19.27) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s16-toledo.html` is the only file the builder writes; `data-composition-id="g-a5s16-toledo"`; id prefix `tol-`; root `<div id="tol-root" ...>` styled through `#tol-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (brief `mg_specs/briefs/g-a2s14-six.md`) for the one-SVG mount, the inlining and prefixing, the dot radius and the stamp; the whole-state view on BM-2 from `compositions/g-a1s09-forecasts.html` where it mounts `midwest-states.svg`, else from `media/maps/README.md`; the toll figure, its label and the map scrim from `compositions/g-a2s08-first.html`; the glass plate from `compositions/g-i1s2-station.html`.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/midwest-states.svg` (BM-2, viewBox -980 -1280 2220 2560, 148,112 bytes; groups `map-states` and `map-points`), inlined.
- `media/drawings/tornado-mark.svg` (DR-11, object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined once.
- The stamp's clock face: `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124) inline, or the face of `compositions/g-t1s2-warning.html`.
- `media/data/points.csv` is the source of the two positions; it is read, not mounted.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s16-toledo`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 9.70 (toll arriving) and 12.90 (toll leaving) forward and backward and match the frames. Line 6: both dots and Ohio's box are computed from `media/data/points.csv`, the `st-oh` path and the section 2 numbers by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus: the measured width of `northern Toledo` (it must end inside the plate, x 686) and of the office chip, and a statement that no `pt-` other than Toledo and Columbus is visible in any frame.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): Ohio filled, neighbours in outline, no dot, line weights. Then one settled frame per cue: 0.90 (stamp at 9:30), 3.50 (Toledo, its label and the mark), 5.00 (office chip), 8.80 (map dim, source line), 10.20 (toll complete), 13.20 (toll and chip gone), 16.40 (Columbus and the dotted line), 17.00 (Columbus chip), 19.20 (last frame).
