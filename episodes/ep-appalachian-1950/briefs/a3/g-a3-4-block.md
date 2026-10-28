# g-a3-4-block: the blocking high (A3-S4)
Builder: Opus 5.5, high effort. Depth: deep (zoom-out, new basemap, multi-layer explainer). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (frame E), then this brief.
Start from: `library/inhouse/master-map-us-canada.html` (basemap paths, projection, camera rig, `logZoom` from `library/inhouse/snippets/helpers.js`). Delete its Enderlin layers and labels. Prefix every id and class `a3b-`.
Sits over: nothing. Full-frame designed scene. Frame 0 shows the 25 Nov chart (camera C1, dimmed, with g-a3-1's red track and grey ghost only, no arrows, no pins), which crossfades into the basemap.

## 0. Claim
A big, slow, stationary high over eastern Canada and the North Atlantic blocked the ocean route (an omega block), so the low curled back inland to the northwest.

## 1. Source
- `research/nws-facts.md` §4 RLX "Upper low over central Appalachians, omega block forming", 25 Nov; RLX 12Z 25 Nov "the development of an omega-blocking pattern with strong downstream ridging" (factcheck a3-r1 row 26).
- `research/maps-forecast.md` §3 M6, Ocean Weather (SECONDARY, oceanweatherservices.com/blog/?p=154): "a strong High-pressure area was nearly stationary over Eastern Canada", "an Omega Block was developing over the North Atlantic Ocean" (factcheck a3-r1 row 25).
- Causal link, Wikipedia (SECONDARY) "retrograded, or moved northwestward, into Ohio due to a blocking ridge up across eastern Canada", citing Smith 1950 (factcheck a3-r1 row 27).
- The dome's extent and the track are SCHEMATIC (no source gives the high's outline).

## 2. Datum, scale, orientation
Frame E (`_list.md`): s 0.0078, top-left (-19654.3, -50096.2) map units; north up. Places (px): Carolinas (722, 875), Pittsburgh (680, 660), Ohio 40.2N 82.8W (596, 670), Newark (854, 647), open Atlantic 41N 66W (1099, 636), H eastern Canada 50N 68W (1039, 244), H east of Labrador 53.5N 57W (1369, 91). The crossfade from the chart is a cut-through, not a geometric match: the chart is not on this projection.

## 3. Geometry (px)
- 0.00 to 1.20: chart (C1, dim .38) with red track and ghost; the chart scales down to 0.85 about (1100, 450) while fading to 0 (1.2 s, power2.inOut), basemap fades in under it from 0 (same 1.2 s). Track and ghost fade with the chart; they are redrawn on the basemap.
- Basemap (frame E, static after 1.20; no camera move, so the HUD text holds still): state/province fills `#0b1016` to `#15202b`, lines `#2a3644` 1.2 px non-scaling, coastline `#4a5560` 1.6 px. Credit "Basemap: Natural Earth" left 110, bottom 60.
- Blocking dome: an ellipse of soft fill `radial-gradient` look (SVG radialGradient) `#5a768f` at .45 centre to 0 at edge, centre (1150, 230), radii 330 x 190, with a 3 px `#7fb2e5` .7 outline; "H" Arial Black 900 84 px `#f2f5f8` at the centre. The dome "breathes" (scale 1 to 1.03 to 1, 3 s, finite repeats) so the hold is never still. Its left edge reaches about x 820 and its bottom about y 420 (over eastern Canada and the North Atlantic, north of the coast).
- Omega outline: after "omega", a 4 px `#dfe7ee` .8 line draws an Ω-shaped upper-air contour round the dome: from (760, 520) up and over the dome's top at y about 60 and back down to (1540, 520), pinched in at the bottom (the two feet bending outward). Duration 1.4 s. Label "Ω" is not drawn: the chip names it.
- Usual-path ghost (re-drawn on the basemap, same style as g-a3-1: `#93a3b2` .55, 5 px, dash 14 10): from Carolinas (722, 875) north-east up the coast (854, 700) toward the open Atlantic, aimed at the dome; on its cue it draws only as far as the dome's bottom edge (about (1000, 440)) and stops there, a 10 px flat "stop bar" `#93a3b2` across its head.
- Red track (same style as g-a3-1: `#d0121f` 6 px, glow): from Carolinas (722, 875) north to about (760, 690), then bending left (west) away from the dome to Ohio (596, 670), arrowhead at the end.
- Chips (glass chip, radius 14, padding 10 x 18):
  - "BLOCKING HIGH" Arial Black 900 40 px `#f2f5f8`, box left x 1240, top y 400 (right of the dome's lower edge; right edge <= 1824, bottom <= 470).
  - "OMEGA BLOCK" Arial 700 30 px `#dfe7ee` tracking 3, box left x 1240, top y 480 (under the first chip; the first dims to .35 when it lands).
- Source lines: "Source: NWS Charleston, WV (omega pattern); Ocean Weather Services (secondary) · schematic" left 110, bottom 90 (Arial 700 19 px `#c8d3e0` tracking 2); basemap credit at bottom 60.
- Ambient: scan line 2 px `rgba(127,178,229,.30)` sweeping at 60 px/s for the whole window.
- Tiers: 84 / 40 / 30 / 19.

## 4. Must be true in the picture
1. The dome sits over eastern Canada and the North Atlantic, north-east of Newark, not over the US coast; its bottom edge is north of Newark's latitude (y < 600).
2. The grey usual path runs into the dome and stops at its edge; it never continues past it.
3. The red track bends west (left), away from the dome, and ends over Ohio; it never touches the dome.
4. "H" shows only from "high" (4.22); the omega contour only from "omega" (14.76).
5. Nothing in x >= 1600, y >= 680 (the dome and chips sit above y 680 on the right).
6. No numbers on screen.

## 5. Panel text (exact) and cues (`audio/a3-s4.words.json`, seconds from A3-S4 start)
Text: `H` · `BLOCKING HIGH` · `OMEGA BLOCK` · `Source: NWS Charleston, WV (omega pattern); Ocean Weather Services (secondary) · schematic` · `Basemap: Natural Earth`
- 0.00 "something": chart crossfade to basemap starts (1.2 s). `/* SOMETHING @0.00 */`
- 1.20: basemap settled; red track and grey ghost redraw quickly to their g-a3-1 shapes up to the Carolinas-north stub (track first 30 %, ghost first 40 %, 0.6 s). `/* SETTLED @1.20 */`
- 2.18 "northeast.": the dome's outline draws on (0.8 s) and fill fades in, no "H" yet. `/* NORTHEAST @2.18 */`
- 4.22 "high": "H" in (scale .6 to 1, back.out(1.6), 0.45 s). `/* HIGH @4.22 */`
- 6.32 "Canada": dome pulses once (scale 1.06, 0.4 s). `/* CANADA @6.32 */`
- 9.08 "moving.": dome breathing starts (finite repeats). `/* MOVING @9.08 */`
- 11.16 "block,": chip "BLOCKING HIGH" in (x 30 to 0, autoAlpha, 0.45 s, power3.out). `/* BLOCK @11.16 */`
- 14.76 "omega.": omega contour draws (1.4 s); chip "OMEGA BLOCK" in; "BLOCKING HIGH" dims .35. `/* OMEGA @14.76 */`
- 15.90 "ocean": grey ghost draws on to the dome edge (0.6 s, power2.in), stop bar slams in (scale 0 to 1, 0.15 s); sound thud lands here. `/* OCEAN @15.90 */`
- 16.46 "blocked,": ghost flashes once and dims to .3. `/* BLOCKED @16.46 */`
- 17.62 "curled": red track draws the rest: north leg then the left bend to Ohio (1.3 s, power2.inOut), arrowhead arrives on "northwest." 18.92. `/* CURLED @17.62 */`
- Exit: none (g-a3-5 continues on frame E). In the last 0.5 s the two chips and the omega contour fade to 0; dome, "H", track, ghost and basemap stay.
Host: data-start = A3-S4 start, duration = 19.30 + 0.40 = 19.70 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
