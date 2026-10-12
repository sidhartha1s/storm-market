Host: id=g-a1s06-low file=compositions/g-a1s06-low.html start=(timeline-map.md) duration=7.25 s plus gaps from timeline-map.md track=2

# g-a1s06-low · A1-S6 · the low on the morning map (wave 2, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md`. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3e row PT-03 and section 6 item 12 (the buildable version of this Picture note). Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `id="root"` (rule 3). A photograph's label names what the photograph shows (rule 5). A flash is a stroke or fill change (rule 12). Map geometry comes from the file (rule 14). Inlined map ids take this comp's prefix; the first frame read checks line weight (rule 20).
**Spoken (A1-S6):** "What the forecasters had on the map that morning was one powerful storm system, a low, turning over the northern plains."
**One look:** the Weather Bureau's real map on paper at the left; beside it our plain map, where one L lands over the Dakotas and wind arrows turn around it.

## 0. What this graphic claims
The Weather Bureau's surface map for 1:00 AM EST on Sunday, April 11, 1965 showed a low over the Dakotas and Minnesota. A low turns counter-clockwise.

## 1. Source
- `edit_script.md` A1-S6, Rows [H; IWX: "A powerful mid-latitude cyclone"; NWS Louisville; inventory B5 opened by the fact check: "SURFACE WEATHER MAP AND STATION WEATHER AT 1:00 A.M., E.S.T.", an "L" over the Dakotas and Minnesota].
- Real map: `media/stills/b5-surface-map-1965-04-11.png` (1503 x 1200; `provenance.csv`: U.S. Weather Bureau Daily Weather Map; the sheet prints `SUNDAY, APRIL 11, 1965` on its right edge and the legend above at lower left).
- No source gives the positions of the fronts. Plan section 6 item 12 allows leaving them to the real map: this comp draws no front of its own. The fronts the viewer sees are the Weather Bureau's, on the card.
- State outlines: `media/maps/us-states.svg` (BM-3).

## 2. Datum, scale, orientation
North is up. Our map is BM-3 inlined in an SVG mounted at left 1100, top 151, width 724, height 509 with `viewBox="-2300 -1300 3000 2109.1"` (state PLAINS: 0.2413 px per map unit; screen x = 1100 + 0.2413 x (u + 2300), screen y = 151 + 0.2413 x (u + 1300)). The window runs from Montana to Ohio and from the Canadian border to Missouri. Its bottom edge is y 660, above the presenter corner.
The L's centre is the centre of the joint box of `st-nd`, `st-sd` and `st-mn`: map units (-873, -598), screen (1444.4, 320.4). That point is where the two Dakotas meet Minnesota. The low's exact centre is not claimed: our map is labelled a sketch.
The real map is shown at 950 x 758 (0.632 of its file size), never enlarged.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Our map | BM-3 group `map-states` inlined, ids prefixed `low-`; outlines Body light 2 px non-scaling, fill Panel dark. On from frame 0 |
| Sketch label | Arial 700 22 px, Label grey, left 1100, top 672: `our sketch · not to scale`. On from frame 0 |
| Real map card | Beige polaroid border 10 px with the page shadow of design sheet section 9: left 96, top 151, 970 x 778 (right 1066, bottom 929). The `<img>` 950 x 758 inside at (106, 161) |
| Card label | glass chip above the card: left 96, top 93, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Surface weather map · 1:00 AM EST` (437 px of text) |
| Source line | design sheet section 10, left 96, bottom 60: `Weather Bureau Daily Weather Map · Sunday, April 11, 1965` |
| System disc | circle radius 110 centred (1444.4, 320.4), fill Body light at 12 %, no stroke |
| L | the letter `L`, Arial Black 900 120 px, Headline white, centred on (1444.4, 320.4) |
| Wind arrows | overlay SVG: four arcs on a circle of radius 96 about (1444.4, 320.4), each 50 degrees long, starting at 0, 90, 180 and 270 degrees, Body light 4 px, round caps, each with a two-stroke head 16 px at its counter-clockwise end. One group; it turns -40 degrees (counter-clockwise) about the centre, `svgOrigin` set once at build |
| Plains label | Arial 700 22 px, Body light, centred on x 1444, top 444: `the northern plains` |

## 4. Must be true in the picture
1. The L sits on our map where North Dakota, South Dakota and Minnesota meet, inside the outlines of those three states' joint box. It is not over Indiana, the Great Lakes or the Rockies.
2. The arrows point and turn counter-clockwise.
3. Our map carries no front, no isobar with a number, no pressure figure and no time. The only time on screen is `1:00 AM EST`, on the real map's label, and it is the legend printed on that sheet.
4. The real map is whole (not cropped), at 950 x 758, and is never enlarged or covered: the L, the disc and the arrows stay on our map, right of x 1100.
5. Our map is labelled `our sketch · not to scale` from the first frame.
6. The card label names what the sheet is. It does not say "forecast" and does not name Indiana.
7. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `our sketch · not to scale` · `Surface weather map · 1:00 AM EST` · `Weather Bureau Daily Weather Map · Sunday, April 11, 1965` · `L` · `the northern plains`.
Cue words and times are from `audio/a1-s6.words.json` as it stood on 12 Oct 26 (wav 7.25 s). One segment, so the two time columns are equal; a lead-in gap from `mg_specs/timeline-map.md` (not on disk yet), if any, is added to every row. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S6 | 0 | What | 0.00 | 0.00 | first frame: ground, our map's state outlines and the sketch label, nothing else |
| 1 | A1-S6 | 6 | map | 1.80 | 1.80 | the real map card slides in from the left (`x:-1080` set at 0, to 0; 0.6 s, power3.out); its label chip and the source line fade in 0.2 s after it lands |
| 2 | A1-S6 | 12 | storm | 3.52 | 3.52 | the system disc fades in on our map (0.4 s) |
| 3 | A1-S6 | 15 | low, | 4.78 | 4.78 | the `L` lands (fade and `y:20` to 0, 0.3 s) |
| 4 | A1-S6 | 16 | turning | 5.46 | 5.46 | the four arrows draw on (0.4 s, `strokeDashoffset`), then the group turns -40 degrees to the end of the comp (ease none) |
| 5 | A1-S6 | 19 | northern | 6.08 | 6.08 | `the northern plains` fades in (0.3 s). Hold to the end |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a1s06-low.html` is the only file the builder writes; `data-composition-id="g-a1s06-low"`; id prefix `low-`; root `<div id="low-root" ...>` styled through `#low-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family bases `compositions/g-a2s14-six.html` and `compositions/g-a1s02-strip.html` (wave 1; briefs in `mg_specs/briefs/`) for the way a base map is inlined and prefixed. No built graphic uses BM-3; the state PLAINS is this comp's own. The page card's border and shadow are those of the built `compositions/g-i1s6-page.html`.
**Assets mounted (paths from the episode folder):**
- `media/maps/us-states.svg` (BM-3, viewBox -4490 -1300 7470 4720, 102,775 bytes), inlined.
- `media/stills/b5-surface-map-1965-04-11.png` (1503 x 1200), shown at 950 x 758.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s06-low`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: the arrow group's `svgOrigin` is set at build, never inside a deferred tween; seek to 6.5 forward and backward and match. Line 6: the L's centre is computed from the three state paths' boxes by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): our map and the sketch label only, state lines 2 px. Then one settled frame per cue: 2.80 (real map card, chip, source line; the sheet's own legend readable), 4.20 (disc), 5.20 (the L over the Dakotas and Minnesota), 6.00 (arrows drawn), 6.90 (arrows turned counter-clockwise, plains label clear of the arrows).
