Host: id=g-z1s04-drill file=compositions/g-z1s04-drill.html start=1156.02 (timeline-map.md table 1 as retimed 12 Oct 26, 19:13; the mount in index.html wins) duration=7.10 s track=2

# g-z1s04-drill · Z1-S4 · Indiana still runs a statewide tornado drill each spring (wave 5, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3b. Map facts: `media/maps/README.md`. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `id="root"` (rule 3). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window (rule 13; done in section 4). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids get this comp's prefix; the first frame read checks line weight (rule 20). `County A` and `County B` have no place here (rule 8).
**Spoken (Z1-S4):** "And Indiana still runs a statewide tornado drill each spring, a test of the systems that carry a warning."
**One look:** the whole state, dark; light leaves one dot in the north and every county fills amber in one sweep; then the light runs the state once more, the test.

## 0. What this graphic claims
Indiana runs a statewide tornado drill each spring, and the drill is a test of the systems that carry a warning. Statewide means all 92 counties. The picture gives no date and no year.

## 1. Source
- `edit_script.md` Z1-S4, Rows [NWS Indianapolis, https://www.weather.gov/ind/severewxweek : "statewide test of communication systems"; the 2026 drill was in March; no later date is published]. The Picture note: "our Indiana map, every county lighting amber in one sweep from the Weather Bureau's dot. Label `statewide tornado drill · each spring`. No date."
- Geometry: `media/maps/indiana-counties.svg` (BM-1), 92 county paths `co-in-<name>`, Indiana's outline `st-in`, the town dot `pt-south-bend` at map (462.2, 188.5). Built from US Census files; today's county lines.

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-1 in a fixed CSS box; no camera move in this comp.
| State | Box (left, top, width, height) | viewBox | Px per map unit | Screen |
|---|---|---|---|---|
| WHOLE | 720, 62, 600, 955 | `200 160 480 764` | 1.25 (screen x = 720 + 1.25 x (u - 200), y = 62 + 1.25 x (u - 160)) | Indiana x 757 to 1283, y 78 to 999; the South Bend dot at (1047.8, 97.6) |
`preserveAspectRatio="xMidYMid meet"`. The map is not text, so it may pass the 54 px bottom margin; it stays left of x 1600.
**The sweep rule (computed, never by eye):** take each county's box centre (the middle of its path's min and max x and y) and its distance d from the South Bend dot in map units. The greatest is Posey, 709.7. A county's fill starts `1.6 x d / 709.7` seconds after the sweep's cue and takes 0.3 s. First is St. Joseph (0.03 s after the cue), then Elkhart, Marshall, Laporte, Starke, Kosciusko; the middle county starts at 0.82 s; the last five are Perry, Warrick, Spencer, Vanderburgh, Posey (1.60 s). The builder's script recomputes all 92 delays from the SVG and states the first, the middle and the last in the receipt.
Colours (the family's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; county lines `#93a3b2` 1.5 px; Indiana's outline `#dfe7ee` 3 px; neighbour outlines `#93a3b2` at 0.4, 2 px; unlit county fill Panel dark `#15202b`; lit fill Amber 2 `#e8c56a`; Body light `#dfe7ee`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `drl-` (`drl-co-in-adams` and so on), in the WHOLE box. The file's `vector-effect="non-scaling-stroke"` keeps the line weights. Every `pt-` group is removed except `pt-south-bend`. `st-in` has no fill, so the lit counties show through it |
| The dot | `drl-pt-south-bend`, its circle at radius 4.8 map units (6 px on screen), fill Body light at rest, Amber 2 from the sweep's cue. No label, no ring, no stamp beside it |
| Lit county | fill Amber 2 at `fill-opacity` 0.45, the map family's lit value (`mg_specs/briefs/g-a2s14-six.md`). No county is named |
| Second pass | each county's `fill-opacity` goes 0.45 to 0.75 and back to 0.45 (0.2 s up, 0.4 s down) in the same order, on the same rule with 1.2 s in place of 1.6 s |
| Label | glass chip, left 96, top 500, height 46, padding 0 x 22, Arial 700 26 px, Body light: `statewide tornado drill · each spring`. Measure its right edge in a frame and state it; it must end left of x 700 (20 px clear of the map box) |
| Source line | design sheet section 10: left 96, bottom 60, Arial 700 22 px, `rgba(244,240,232,0.88)`, `letter-spacing:0.04em`, the credit shadow: `National Weather Service, Indianapolis` |

## 4. Must be true in the picture
1. All 92 counties are lit by 3.42 s and stay lit to the last frame. None is skipped and none is lit twice as bright as the rest at rest.
2. The light leaves the northern dot and reaches the far south-west last: counties fill in order of distance, so the edge of the lit area reads as one front moving across the state, not a random scatter.
3. A lit county changes by fill only: no scale, no outline thickening, no glow (rule 12).
4. No date, no year, no month, no "2026" and no clock anywhere. The label is exactly `statewide tornado drill · each spring`.
5. No county, town or office is named on the map. The dot has no label (the drill is the state's and the Weather Service's, not one office's; see the note in section 6). No Alto.
6. County lines are 1.5 px and Indiana's outline 3 px on screen (read frame 0 and the last frame).
7. One source on screen, the source line. No stamp, no chip but the label, no `County A`, no `County B`.
8. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680; all text at least 96 px from the sides and 54 px from top and bottom.
Beat check (rule 13): the sweep is one move of 1.6 s plus a 0.3 s fill: it starts on "statewide" (1.52) and is settled at 3.42, inside the first clause (its last word "spring," starts at 3.06). The second pass starts on "test" (4.26) and is settled by 6.06, as "warning." is spoken (5.72). The last 1.04 s holds the lit state.

## 5. Text (exact) and cues
Text: `statewide tornado drill · each spring` · `National Weather Service, Indianapolis`.
Cue words and times are from `audio/z1-s4.words.json` as on disk 12 Oct 26, 19:27 (wav 6.74 s). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (Z1-S4 -0.32) plus the word's time; the first word uses the table's "first sound" (0.07). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | Z1-S4 | 0 | And | first sound 0.39 | 0.07 | first frame (0.00, the cut): ground, the whole map in lines, every county unlit, the dot in Body light. No label, no source line |
| 1 | Z1-S4 | 5 | statewide | 1.84 | 1.52 | the dot turns Amber 2 (0.15 s) and the sweep starts: 92 fills by the rule of section 2, over 1.6 s, each 0.3 s. Settled 3.42 |
| 2 | Z1-S4 | 7 | drill | 2.78 | 2.46 | the label chip and the source line fade in (0.3 s, `y: 12` to 0) |
| 3 | Z1-S4 | 11 | test | 4.58 | 4.26 | the second pass runs from the dot (1.2 s rule, 0.6 s per county). Settled by 6.06. Hold to the last frame (7.10) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-z1s04-drill.html` is the only file the builder writes; `data-composition-id="g-z1s04-drill"`, `data-duration="7.10"`; id prefix `drl-`; root `<div id="drl-root" ...>` styled through `#drl-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. The host is mounted in `index.html` as `host-z1s04-drill`; do not edit `index.html`.
**Family base it copies:** `compositions/g-a2s14-six.html` (wave 1, brief `mg_specs/briefs/g-a2s14-six.md`): the way BM-1 is inlined and prefixed, the line weights, the lit-county fill. The whole-state view follows `mg_specs/briefs/g-a1s09-forecasts.md` (its INDIANA state: one SVG, the viewBox is the camera); this comp uses its own larger WHOLE box because nothing shares the frame with the map but one label.
**Note on the dot (the director's reading, for the lead to accept or strike):** the Picture note says "the Weather Bureau's dot". The dot is South Bend's, the office the viewer has followed. It is left without a label because the source says the drill is statewide and run with the Weather Service in Indianapolis; a `South Bend` label on the sweep's origin would say the drill starts there.
**Assets (paths from the episode folder):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined. `media/data/points.csv` holds the dot's position. `media/maps/README.md` wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-z1s04-drill`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3 -I media/maps/check_ids.py` (run from the episode folder) lists the 92 county ids.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 2.30 (mid sweep) and 4.90 (mid second pass) forward and backward and match the frames; no fill's start value lives only in a deferred tween's from vars. Line 6: the 92 delays are computed by a script from the SVG and the dot's position; the receipt states the count (92), the first three counties, the middle delay and the last county with its delay.

## 8. Receipt
As template section 8, plus the label chip's measured right edge.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the whole map in lines, nothing lit, dot in Body light, line weights 1.5 and 3 px. Then: 1.60 (dot amber, St. Joseph filling), 2.30 (mid sweep: the north lit, the south dark, one front), 3.00 (label and source line on, sweep near the south-west), 3.50 (all 92 lit), 4.90 (mid second pass: a brighter band part way down the state), 6.20 (settled, even fill), 7.06 (last frame: lit state, label, source line, corner empty).
