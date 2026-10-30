# g-a3-7-stall: the low spins in place over Lake Erie (A3-S7, 0.00 to 9.60)
Builder: Opus 5.5, high effort. Depth: deep (chart crossfade + track loop). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (chart camera C1), then this brief.
Start from: g-a3-1's finished file (chart camera C1, dim, scan line, red track; prefix every id and class `a3k-`); `svg-stroke-trace` for the loop draw.
Sits over: nothing underneath; chart stills `media/a3/A3-S7_c1_nws-jkl-surface-1950-11-26.jpg` (1174 x 757) and `media/a3/A3-S7_c2_nws-jkl-surface-1950-11-27.jpg` (1168 x 758) mounted inside the comp, each at scale 2.0 with the same top-left offset as C1 (-392, -220); ground on from frame 0.

## 0. Claim
The low stopped moving and spun in place over Lake Erie for two days (27 and 28 Nov), stacked straight up from the ground to the upper air.

## 1. Source
- `research/nws-facts.md` §4 JKL "spun in place over Lake Erie on the 27th and 28th".
- `research/maps-forecast.md` §3 M7 RLX (fetch summary): upper low stalled over the central Appalachians, low "vertically stacked and near-stationary" (SECONDARY).
- Charts: NWS Jackson KY 26 and 27 Nov 1950 (`maps-forecast.md` §1 item 1; provenance rows: 26 Nov "low 981 over Lake Erie/Ohio", 27 Nov "weaker low about 999 over Lake Erie/Ontario"). Header dates are cropped from the files, so no date is read off the chart on screen; the chip carries the date.
- The loop is SCHEMATIC, placed on the 27 Nov chart's printed low.

## 2. Datum, scale, orientation
Camera C1 for both charts. The loop centre = the printed low centre on the 27 Nov chart: the builder finds the "L"/lowest closed isobar on `A3-S7_c2` and converts with screen = (chart px - (196, 110)) × 2.0; expected near Lake Erie, screen about (1000, 260) (`_list.md`: Lake Erie centre). Report the measured value. The red track enters from the south-east (from the 26 Nov low position, measured the same way on `A3-S7_c1`) and ends in the loop.

## 3. Geometry (px)
- 0.00: 26 Nov chart, dim .38, red track (same style as g-a3-1) drawn from the chart's lower right up to the 26 Nov low. 
- Crossfade 26 to 27 Nov chart: 1.2 s, power1.inOut, from "stopped".
- Loop: a tight closed spiral of 1.5 turns, radius 70 px, about the loop centre, 6 px `#d0121f` with glow, drawn on as a continuation of the track (draw 1.4 s), then a small red arrowhead keeps circling the loop (counterclockwise, one lap per 2.4 s, finite repeats to the host end; GSAP rotation about the centre via `svgOrigin`).
- Chip (glass chip, radius 14, padding 10 x 18): "STALLED · NOV 27–28" Arial Black 900 40 px `#f2f5f8`, box left 1120, top 180 (right of the loop; right edge <= 1824).
- Stacked cue: on "stacked", a vertical column above the loop: three short horizontal ellipses (rx 70, ry 16) stacked at y offsets -0, -70, -140 from the loop centre (clamp top >= 60), 3 px `#dfe7ee` .7, each with a small counterclockwise arrowhead, appearing bottom to top (stagger .25); label "GROUND TO UPPER AIR" Arial 700 22 px `#93a3b2` tracking 3, left of the column (right edge 24 px left of it). The column fades at "still" to .4 and stays.
- Source line "Source: NWS Jackson, KY; NWS Charleston, WV · loop schematic" left 110, bottom 60.
- Scan line 60 px/s whole window.
- Tiers: 40 / 22 / 19 (two text tiers plus the source; add the big tier only if the gate's flat-type rule counts >= 4 text nodes: it does (chip, label, source = 3), so no exemption needed; if it does flag, declare `data-type-ok="map labels"` on the root after a frame read).

## 4. Must be true in the picture
1. The loop sits over Lake Erie on the 27 Nov chart (on the printed low), not over Ohio land or the Atlantic.
2. The red track is one continuous line from the earlier position into the loop; the loop turns counterclockwise.
3. The date shows only in the chip and only from "two days" (3.50).
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a3-s7.words.json`, seconds from A3-S7 start = comp time)
Text: `STALLED · NOV 27–28` · `GROUND TO UPPER AIR` · `Source: NWS Jackson, KY; NWS Charleston, WV · loop schematic`
- 0.00 "then": 26 Nov chart, dim, track to the 26 Nov low, scan line. `/* THEN @0.00 */`
- 0.34 "stopped": crossfade to the 27 Nov chart (1.2 s). `/* STOPPED @0.34 */`
- 1.82 "spun": loop draws (1.4 s), then the circling arrowhead starts. `/* SPUN @1.82 */`
- 2.90 "Lake": loop centre glows once (radius 90, `#d0121f` .25, 0.6 s). `/* LAKE ERIE @2.90 */`
- 3.50 "two": chip "STALLED · NOV 27–28" in (x 30 to 0, autoAlpha, 0.45 s, power3.out). `/* TWO DAYS @3.50 */`
- 5.06 "stacked": chip dims .35; stacked ellipses appear bottom to top, label in. `/* STACKED @5.06 */`
- 8.80 "still.": column to .4. `/* STILL @8.80 */`
- Exit: 9.00 to 9.60: chart, track and labels fade to `#04070c` (0.6 s, power2.in) as g-a3-8's relief fades in on top (g-a3-8 owns the fade-in).
Host: data-start = A3-S7 start, duration = 9.60 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Receipt states the measured loop centre.
