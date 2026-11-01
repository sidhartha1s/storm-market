# g-a2-14-bothsides: both sides on one map, nothing joining them (A2-S14)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a2/_list.md`, and `briefs/intro/g-intro-2-hookmap.md` (the hook map this returns to: pin styles, credit spot, frame D) first.
Start from: `library/inhouse/master-map-us-canada.html` and the built `compositions/g-intro-2-hookmap.html` (copy its basemap, pin and label styles under the `x14-` prefix; never edit the intro file). `logZoom` from `library/inhouse/snippets/helpers.js`.
Sits over: nothing. Full-frame designed map on track 2, ground on from frame 0 (fade-through from g-a2-13). Ends on a hard cut to Paul's clip `ins-paul-4` (A2-S15).

## 0. Claim
On the same Saturday (25 Nov 1950) there were five feet of snow in West Virginia and hurricane-force wind on the Jersey coast, with Buffalo in the 40s and no snow between them; this map shows no reason why they hit together (cta-hinge open, L1 open).

## 1. Source
`research/nws-facts.md` §2 Coburn Creek 62 in (snow side), NCEI 18 in+ footprint (the NCEI PNG `media/a2/A2-S9_c2_ncei-snowfall-index-nov22-30-1950.png`), §1/§4 Newark 108 mph gust 25 Nov, FFC "hurricane-force winds and wind damage to the Northeast" (P), NCEI "onshore winds along the coast caused extreme high tides and flooding in New Jersey and Connecticut" (P), §3 JKL Buffalo "temps in the 40s and recorded no snow at all" (P). `factcheck/a2-r1.md` rows 44 to 47 (row 47: tie only the Saturday). `grades/a2-r2.md` item 4: Buffalo is picture only, not voice.

## 2. Datum, scale, orientation
Projection from `briefs/a2/_list.md`. North up.
- Frame 0 = intro frame D: s 0.04024, top-left (59078.1, 18954.6): Newark (1240, 560), Pittsburgh (340, 626), Buffalo (513, 77).
- Target frame A2-X: s 0.03, top-left (42191.8, 15852.5): Newark (1431, 511), Pittsburgh (760, 560), Buffalo (889, 150), Elkins (777, 814), Columbus (414, 640), Erie (750, 277). Move D to A2-X: ratio 1.34 with a pan, `logZoom` for consistency, 1.6 s, expo.inOut.
- Snow footprint: lon/lat polygon of the NCEI 18 in+ area (red + dark red on the PNG) in OH, PA, WV, read against the PNG's state lines (16 to 30 vertices), converted with the formula; list vertices in the receipt. It may be the same outline g-a2-10 traced, re-read as lon/lat. Expected span: Lake Erie shore near Erie south through western PA and eastern/central Ohio into West Virginia and the Kentucky/WV border.
- Wind coast band: a 26 px-wide stroke-style band hugging the shoreline from Cape May NJ (38.9351, -74.9060; A2-X px (1346, 813)) north along the NJ shore, past Newark/NY harbour, along the Connecticut and Rhode Island shore to Boston (42.3601, -71.0589; A2-X px (1790, 238)). Coastline vertices from the basemap's own coastline, offset 8 px seaward.
- Gap: the nearest points of snow footprint and coast band are at least 300 px apart at A2-X (snow east edge expected near x 930, coast band west edge near x 1330); Buffalo's pin at least 40 px outside the footprint.

## 3. Geometry (px, 1920 x 1080)
- Frame 0 = g-intro-2 frame D state (its §4.6): Newark pin blue with "NEWARK" label, Pittsburgh pin white with "PITTSBURGH" label, nothing else. Basemap credit "Basemap: Natural Earth" Arial 700 19 px `#93a3b2`, left 110, bottom 60 (same spot as the intro maps).
- Snow footprint: fill `rgba(242,245,248,.80)`, edge 2 px `#f2f5f8`, a soft inner glow; revealed by a north-to-south mask sweep (Erie first).
- Coast band: fill `#7fb2e5` at 85 %, revealed south to north from Cape May to Boston (`stroke-dashoffset` on a centreline path, length `ceil(len)+1`), with short wind streaks (8 to 12 dashes, 2 px `#7fb2e5`, moving north-east along the band at 120 px/s, finite repeats) ON the band only, never across the land.
- Pins at A2-X: Newark (1431, 511) blue; Pittsburgh (760, 560) white; Buffalo (889, 150) orange `#d8a13a` 16 px with a 2 px `#e8c56a` ring.
- Labels (fixed HUD, appear after the camera settles, glass pills where they sit over a fill):
  - "SNOW" Arial Black 900 52 px `#f2f5f8` on a glass pill at left 470, top 700 (west of the footprint's south part; check it sits off the fill or on a pill).
  - "WIND" Arial Black 900 52 px `#7fb2e5`, single line, at left 1180, top 600 (about x 1180 to 1340, y 600 to 660): inland, west of the NJ shore band (shore near x 1445 at lat 40, y 634) and far east of the snow footprint.
  - Buffalo label right of the pin: "BUFFALO" Arial 700 22 px `#93a3b2` tracking 3 over "40s · NO SNOW" Arial Black 900 40 px `#e8c56a` (edit_script "40s · NO SNOW"), pill left edge x 914, centre y 150.
  - "NEWARK" and "PITTSBURGH" labels stay as at frame D, re-placed beside their A2-X pins (Newark label left of its pin so it does not sit on the coast band).
- Source line "Source: NOAA NCEI; NWS" Arial 700 19 px `#c8d3e0`, left 110, bottom 90.
- Tiers: 52 / 40 / 26 / 22 / 19.

## 4. Must be true in the picture
1. L1 and cta-hinge open: no line, arc, arrow, gradient, "L" symbol, front, isobar or shading touches or joins the snow footprint, the coast band and Buffalo. Three separate things on plain ground, with the §2 gaps.
2. Pins at A2-X px ±10 (formula). Buffalo sits north of Pittsburgh and outside the snow.
3. The snow footprint follows the published NCEI 18 in+ area (side-by-side check with the PNG); the coast band runs NJ to Massachusetts and nowhere inland.
4. No figure from Act 1's coast beat or A2 respent as a number (no "108 MPH", no "62 IN"): the voice carries "five feet" and "hurricane-force".
5. Nothing in x >= 1600, y >= 680 (Boston end of the band is at y 238; Cape May at x 1346).
6. "WIND" label: placed inland of the band, between Newark and the band's NJ stretch, not over Newark's pin or label.

## 5. Panel text (exact) and cues (`audio/a2-s14.words.json`, seconds from A2-S14 start)
Text: `NEWARK` · `PITTSBURGH` · `SNOW` · `WIND` · `BUFFALO` · `40s · NO SNOW` · `Source: NOAA NCEI; NWS` · `Basemap: Natural Earth`
- 0.00 "That": frame D, Newark and Pittsburgh labels on; at 0.10 labels fade (0.3 s) and the move D to A2-X starts (1.6 s, arrives 1.70; no text rides the move). `/* THAT @0.00 */`
- 1.38 "map.": camera settling; labels NEWARK/PITTSBURGH return at 1.70 beside the A2-X pins. `/* MAP @1.38 */`
- 2.40 "five": snow footprint sweeps in north to south (1.2 s, power2.inOut), "SNOW" label in at 3.58 "Virginia". `/* FIVE @2.40 */ /* VIRGINIA @3.58 */`
- 4.54 "hurricane": coast band draws Cape May to Boston (1.4 s, power2.inOut), wind streaks start; "WIND" label in at 5.28 "wind". `/* HURRICANE @4.54 */ /* WIND @5.28 */`
- 6.86 "both": both fills pulse once together (brightness 1 to 1.25, 0.4 s yoyo), with no shape between them. `/* BOTH @6.86 */`
- 7.64 "Saturday.": Buffalo pin pops (scale 0 to 1, back.out) and its pill in. `/* SATURDAY @7.64 */`
- 8.80 "nothing": a slow push in 4 % toward the empty land between the fills (centre about (1100, 450)), ease none, to the end. `/* NOTHING @8.80 */`
- 10.10 "why" to 10.70 "together.": wind streaks and snow glow keep moving; nothing else is added.
- Exit: hard cut to Paul (`ins-paul-4`) at the host end; the push and streaks are still moving (full-frame MG scene may end on a cut).
Host: data-start = A2-S14 start, duration = 11.06 + 0.40 = 11.46 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Receipt lists the snow footprint and coastline vertices, the measured minimum gap (px) between the two fills, and Buffalo's distance to the footprint.
