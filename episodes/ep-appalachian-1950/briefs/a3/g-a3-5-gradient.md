# g-a3-5-gradient: squeezed between two highs (A3-S5)
Builder: Opus 5.5, high effort. Depth: deep (isobar explainer). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (frame E), then this brief.
Start from: g-a3-4's finished file (basemap, frame E, dome, "H", track, ghost; prefix every id and class `a3g-`) plus `references/editing-patterns/ep2-met-explainer.html` for line style.
Sits over: nothing. Full-frame designed map, frame E. Frame 0 = g-a3-4's last frame.

## 0. Claim
Air flows from high pressure toward low, and the closer they sit the harder it blows. NWS Albany: the storm sat between two very strong highs, one east of Labrador and one over the Mississippi Valley, giving a very tight pressure gradient over New Jersey, New York and New England.

## 1. Source
- `research/nws-facts.md` §4 ALY "situated between two very strong high pressure centers ... producing a very tight pressure gradient", highs east of Labrador and over the Mississippi Valley (factcheck a3-r1 row 29).
- High-to-low flow and gradient wind: standard meteorology (row 28).
- "That same high" as the coast's wind source: NBC Connecticut (SECONDARY) "what made the winds vicious was the 1050ish mb high near Maine" (row 30). No number shown here.
- Isobar spacing is SCHEMATIC (no isobar was traced from a chart); only the ordering (tightest over NJ/NY/New England) is a claim.

## 2. Datum, scale, orientation
Frame E: s 0.0078, top-left (-19654.3, -50096.2). Places (px): L Appalachians 40N 80.5W (665, 679), H east of Labrador 53.5N 57W (1369, 91), H Mississippi Valley 36N 90W (380, 853), Newark (854, 647), New England coast about (930, 560). Keep one eastern high on screen: g-a3-4's dome is "that same high". The brief writer's call: shift the dome's "H" from (1150, 230) to (1290, 150) over 1.0 s at "That same high" (still over eastern Canada / off Labrador, top margin kept: "H" box top >= 54). Report if the dome then breaks a §4 truth.

## 3. Geometry (px)
- "L" Arial Black 900 84 px `#d0121f` centred at (665, 679) (on the red track's Ohio-ward end; the track stays). Note y 679 is outside the corner because x 665 < 1600.
- Second "H" Arial Black 900 84 px `#f2f5f8` at (380, 853) with a small soft blue disc (radius 90, `#5a768f` .35) behind it.
- Isobars: 7 closed-ish curves round the L, drawn as SVG paths, 2.5 px `#dfe7ee` at .55, numbered nothing. Spacing: between L and the western H the lines are 60 to 70 px apart; between L and the eastern H, over NJ/NY/New England (the band x 760 to 1000, y 420 to 640), they bunch to 14 to 18 px apart. Lay them as offset curves of one seed curve that runs from (560, 300) round the L's north and east side to (980, 760); compute the offsets by script and state them in the receipt (done line 6).
- Bunching motion: lines start evenly spaced (40 px) and slide into their final spacing on "closer together" (1.6 s, power2.inOut), so the squeeze is seen happening. After that a slow shimmer: each line's opacity cycles .45 to .7 (2 s, staggered, finite repeats).
- Flow arrows (3) `#dfe7ee` 6 px with heads, from the eastern H side down toward the L across the bunched band (e.g. (1180, 300) → (880, 560)), conveyor dashes running; plus 1 short arrow from the western H toward the L. They draw on at "flows".
- Highlight: the tight band gets a soft glow `#7fb2e5` .25 (a blurred path along it) from "highs".
- Chip (glass chip, radius 14, padding 10 x 18): "VERY TIGHT PRESSURE GRADIENT" Arial Black 900 40 px `#f2f5f8`, box left x 1060, top y 470 (right edge <= 1824, bottom <= 540); a 2 px `#dfe7ee` leader from the chip's left edge to the band centre (about (930, 520)).
- Headline (title zone, glass card left 110, top 90): "AIR FLOWS HIGH TO LOW" Arial Black 900 52 px `#f2f5f8`; exits when the chip lands.
- Source: "Source: NWS Albany · isobars schematic" left 110, bottom 90; basemap credit bottom 60.
- Ambient: scan line continues (60 px/s).
- Tiers: 84 / 52 / 40 / 19.

## 4. Must be true in the picture
1. The isobars are tightest between the L and the eastern H, over NJ, NY and New England (east of the L), and visibly wider on the west side toward the Mississippi Valley H. Ratio: tight spacing <= 1/3 of the wide spacing.
2. Flow arrows point from an H toward the L, never the reverse.
3. Exactly two "H" and one "L" on screen from "highs" (12.94) on; the L sits on the track's inland side.
4. No pressure number on screen (g-a3-6 owns 980 / 1050).
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a3-s5.words.json`, seconds from A3-S5 start)
Text: `L` · `H` (twice) · `AIR FLOWS HIGH TO LOW` · `VERY TIGHT PRESSURE GRADIENT` · `Source: NWS Albany · isobars schematic` · `Basemap: Natural Earth`
- 0.00 "That": frame 0 = g-a3-4 last frame. `/* THAT @0.00 */`
- 0.54 "high": eastern dome pulses (scale 1.06, .4 s) and its "H" shifts to (1290, 150) over 1.0 s. `/* HIGH @0.54 */`
- 2.06 "wind": 3 flow arrows draw from the dome toward the coast (0.8 s), conveyors start. `/* WIND @2.06 */`
- 3.36 "Air": headline in (y 24 to 0, 0.45 s). `/* AIR @3.36 */`
- 4.84 "low,": "L" in at (665, 679) (scale .6 to 1, back.out(1.6), 0.4 s); isobars draw on evenly spaced (1.0 s, stagger .08). `/* LOW @4.84 */`
- 5.96 "closer": isobars slide into the bunched spacing (1.6 s, power2.inOut). `/* CLOSER @5.96 */`
- 8.34 "blows.": flow arrows speed up (conveyor 2x) and one gust flash runs along the tight band (0.6 s). `/* BLOWS @8.34 */`
- 10.12 "Albany": source line pulses brighter once (`#c8d3e0` to `#f2f5f8` and back, 0.6 s). `/* ALBANY @10.12 */`
- 12.94 "highs": western "H" + disc in (scale .6 to 1, 0.4 s); one short flow arrow from it toward the L; band glow fades in. `/* HIGHS @12.94 */`
- 14.30 "pack" (Whisper for "packed"): headline exits (x -60, autoAlpha 0, 0.5 s, power3.in); chip "VERY TIGHT PRESSURE GRADIENT" in with its leader (x 30 to 0, 0.45 s). `/* PACKED @14.30 */`
- Exit: last 0.6 s: chip `to` x 980, autoAlpha 0 (0.6 s, power3.in); the whole map fades to `#04070c` with it (g-a3-6 opens on a designed card).
Host: data-start = A3-S5 start, duration = 15.48 + 0.40 = 15.88 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
