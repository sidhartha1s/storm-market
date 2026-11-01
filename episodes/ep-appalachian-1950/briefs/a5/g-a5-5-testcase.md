# g-a5-5-testcase: the two-level test that fell short (A5-S5, A5-S6)
Builder: Opus 5.5, high effort. Depth: deep (multi-layer explainer that runs across two segments). Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: `library/inhouse/split-shared-scale.html` (layered build and camera), catalog `mk-progress-stat` (track fill pattern), popfig from `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`. Eastern-US outline: export the coastline/state paths from `library/inhouse/master-map-us-canada.html` through the projection below; never redraw by hand. Prefix every id/class `a55-`.
Sits over: nothing. Full-frame designed scene on track 2, background radial gradient `#0b1016` to `#030507`, ground on from frame 0.

## 0. Claim
The storm was chosen as the first test case for Charney's two-level model, a computer picture of the atmosphere in two layers instead of one. The test fell short ("not as successful as hoped"), but it set off the meetings that led to the Joint Numerical Weather Prediction Unit in 1954.

## 1. Source (quoted, with rows)
- AMS abstract (Kistler et al. 2004), https://ams.confex.com/ams/84Annual/techprogram/paper_73168.htm: "the 1950 storm was chosen the first test case for Charney's 2 Level model"; results "not as successful as hoped"; "set in motion the meetings and plans that would ultimately evolve into the formation of the ... JNWPU in 1954". `factcheck/a5-r2.md` rows 23, 24, 28, 29, 30, 32, 35.
- Two layers instead of one: row 25 (vs the 1950 single-level barotropic model, EMC history, SECONDARY).
- JNWPU organised 1 July 1954; twice-daily output by mid-1955: NOAA https://vos.noaa.gov/MWL/dec_07/weatherprediction.shtml, rows 32-34.
- What the run got wrong is NOT sourced (maps-forecast.md §2; edit_script A5-S5 "Grade fix 1 declined"). The bar's stall point is a picture of "fell short", never a measured fraction.

## 2. Datum, scale, orientation
- Slab outline: eastern US (lon -92 to -66, lat 29 to 48) projected with map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213), scaled s 0.0055 so it fits a 1100 x 560 box, then laid flat in fake isometric: CSS-free SVG matrix `matrix(1, 0, -0.55, 0.42, 0, 0)` (skew + squash) applied once to a static inner group (static transform on a non-mover only; the movers are the slab groups around it). Slab box centre on screen (920, 640). North points up-and-right on the tilted plane; no compass text.
- SCHEMATIC, NOT TO SCALE: layer heights and the lift distance are illustration, no altitude numbers.

## 3. Geometry (px)
- Lower layer: tilted plane about 1100 x 240 px on screen, fill `#15202b` at 0.85, edge `#4a5560` 1.6 px, eastern-US coastline/state lines `#2a3644` 1.2 px on it; a 14 px dark side face below its front edge for depth.
- Upper layer: identical plane, fill `#5a768f` at 0.35, edge `#7fb2e5` 1.6 px, starts coincident with the lower layer, lifts y -190 px on its cue. Faint vertical guide lines (4, `#4a5560` 1 px dashed) join the layer corners while lifted.
- Starting conditions (undated): 36 small station dots (5 px `#dfe7ee`) and 12 short wind ticks (`#93a3b2`, 18 px) on a jittered grid inside the lower plane; they drop from y -260 onto the plane, staggered 0.04 s. They do NOT include a Minnesota swirl or any feature from g-a5-3 (a5-r2 row 28: the test's start is not sourced).
- Chip "TWO-LEVEL MODEL": glass surface, radius 14, padding 10 x 18, Arial Black 900 52 px `#f2f5f8`, top-left zone: left 110, top 90.
- Progress bar: label "TEST CASE #1" Arial Black 900 40 px `#f2f5f8` at left 460, top 840; track x 460 to 1460, y 902, 16 px tall, `rgba(255,255,255,.12)`, radius 8; fill `#d8a13a` (scaleX from 0, transformOrigin left center). Stall point: scaleX 0.68. On the stall the fill turns `#c0392b` (0.3 s) and blinks twice (opacity 1 to 0.5, 0.2 s yoyo).
- Quoted chip: “NOT AS SUCCESSFUL AS HOPED” Arial Black 900 40 px `#f2f5f8` on glass, centred x 960, top 720 (above the bar, below the slab); attribution under it Arial 700 20 px `#c8d3e0`: "Kistler et al., AMS 2004" (this IS the picture line's source line; do not print it twice).
- Popfig (after the scene clears): big "1954" AbrilFig 150 px `#d0121f`, `.pf-big` shadow, centred, block top 360; sub "JOINT NUMERICAL WEATHER PREDICTION UNIT" Arial 700 32 px `#e8e3d8`, `.pf-sub` shadow, 12 px under (about 760 px wide).
- Scan line 2 px, opacity 0.25, sweeping top to bottom at 60 px/s for the whole comp.
- Tiers: 150/52 (big), 40/32 (mid), 20 (small).

## 4. Must be true in the picture
1. Two layers, visibly separate after the lift; the lower one carries the eastern-US outline (recognisable Atlantic coast, Florida tip at the south-west of the plane, New England at the north-east).
2. No date, no "NOV", no Minnesota ripple, no storm swirl in the input. No number on or beside the bar (no %, no ticks).
3. The bar never reaches the end; it stops at 0.68 and stays stopped (it may blink, never creep).
4. "1954" appears only after the slab, bar and chips are gone: the popfig never sits over the diagram.
5. One reading target at a time: "TWO-LEVEL MODEL" is dimmed to 0.35 when the quote chip lands; all are out before the popfig.
6. Corner x >= 1600, y >= 680 empty: the plane's right corner and the bar end left of x 1600 below y 680.

## 5. Panel text (exact) and cues
Text: `TWO-LEVEL MODEL` · `TEST CASE #1` · `“NOT AS SUCCESSFUL AS HOPED”` · `Kistler et al., AMS 2004` · `1954` · `JOINT NUMERICAL WEATHER PREDICTION UNIT`
Segment offsets (comp-local seconds; assumes a 0.40 s gap, replace with the real `data-start` difference):
`SEG = { a5s5: 0.000, a5s6: 14.580 }` ; segment lengths 14.18, 18.04 s.
Cues (segment word time from `audio/<seg>.words.json`, comp time = SEG + t):
- A5-S5 0.00 "Then": lower layer on at frame 0 (ground), slow orbit drift: whole slab group rotation -1° to +1° and y 0 to -8 over the comp (ease none, finite).
- A5-S5 2.04 "picked": starting-condition dots drop onto the lower plane (stagger 0.04 s, 0.4 s each, power2.in then a 4 px settle). `/* PICKED @2.04 */`
- A5-S5 3.94 "first": bar label and empty track in (`fromTo` autoAlpha 0, y 24 to 0, 0.4 s, power3.out). `/* FIRST TEST @3.94 */`
- A5-S5 5.42 "two": upper layer lifts (y 0 to -190, 1.0 s, power3.inOut), guide lines draw; chip "TWO-LEVEL MODEL" in (`fromTo` autoAlpha 0, x -20 to 0, 0.4 s, back.out(1.4)). `/* TWO-LEVEL @5.42 */`
- A5-S5 8.32 "two layers": both layers one brightness pulse (edge opacity 1 to 0.5 to 1, 0.6 s), lower then upper 0.3 s apart. `/* TWO LAYERS @8.32 */`
- A5-S5 10.18 "pass,": bar fill starts, scaleX 0 to 0.55 by A5-S5 14.18 (power1.inOut). `/* PASS @10.18 */`
- A5-S5 13.52 "lot": upper layer a small wobble (y ±6, 0.4 s, 2 finite repeats). `/* LOT @13.52 */`
- A5-S6 0.12 "fell": fill 0.55 to 0.68 (0.25 s, power4.out) and stops; fill turns red and blinks twice. `/* FELL SHORT @0.12 */`
- A5-S6 3.44 "not": "TWO-LEVEL MODEL" dims to 0.35; quote chip in (`fromTo` autoAlpha 0, scale 0.9 to 1, 0.4 s, back.out(1.4)), attribution 0.3 s after. `/* NOT AS SUCCESSFUL @3.44 */`
- A5-S6 5.32 "storm won": upper layer drops back onto the lower one (y -190 to 0, 0.8 s, power2.in), guide lines retract. `/* STORM WON @5.32 */`
- A5-S6 8.82 "The meetings": everything exits: chips and bar slide out (`to` x 980, autoAlpha 0, 0.6 s, power3.in), slab group scale 1 to 0.85 and autoAlpha 0 (0.8 s). Ground and scan line stay. `/* MEETINGS @8.82 */`
- A5-S6 11.26 "1954": big "1954" in (`fromTo` autoAlpha 0, scale 1.4 to 1, y -30 to 0, 0.35 s, back.out(2.0): the "stamp down"). `/* 1954 @11.26 */`
- A5-S6 12.16 "built": sub in (`fromTo` autoAlpha 0, y 18 to 0, 0.4 s, power3.out). `/* BUILT @12.16 */`
- A5-S6 12.60 to 17.30: popfig float y 0 to -10, sine.inOut, finite yoyo.
- A5-S6 17.40 to 18.00: popfig exits (`to` autoAlpha 0, y -40, scale 0.96, 0.6 s, power3.in), then 0.4 s land on ground. `/* DAY @17.88 */`
Host: data-start = A5-S5 audio start, duration = SEG.a5s6 + 18.40 (32.98 s with the assumed gap). Root `id="g-a5-5-testcase-root"`.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 6: compute the outline path from the projection by script and print the box it lands in. Report any §4 vs §3 conflict instead of choosing.
Must not: CSS @keyframes, `id="root"`, CSS transform initial states on movers, a percentage on the bar, a date card colour block.
