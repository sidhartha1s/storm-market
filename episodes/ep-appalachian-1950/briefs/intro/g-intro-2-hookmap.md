# g-intro-2-hookmap: two hazards, three pins, no link (H1-S2 to H1-S5)
Builder: Opus 5.5, high effort. Depth: deep (the hook's main graphic). Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: `library/inhouse/master-map-us-canada.html`. Copy it to `compositions/g-intro-2-hookmap.html`; keep the basemap paths, the projection and the camera rig (`#...-cam`, a single camera group, svgOrigin based). Delete the Enderlin swath/track, survey points, the RHS rail cards and every Enderlin label. Rename every id/class prefix to `ih2-`.
Sits over: nothing. Full-frame designed scene on track 2, ground on from frame 0 (hard cut from Paul on "That's"). Presenter circle is hidden in the hook. PROVISIONAL hook: a different hook shape redoes this graphic.

## 0. Claim
On one Saturday the same storm put a hurricane-force gust on Newark and more than two feet of snow on Pittsburgh, while Buffalo, north of Pittsburgh, sat in the 40s with no snow. The picture shows the places as separate points and refuses to show what joins them (loop L1 stays closed until Act 3).

## 1. Source (quoted, with rows)
- Newark 108 mph, 25 Nov: `research/nws-facts.md` §1 (JKL "Newark, NJ recorded a 108 mph wind gust"; PHI Nov 25 entry). Fact-check intro-r2 rows 1, 4.
- Hurricane force: §4 FFC "hurricane-force winds and wind damage to the Northeast"; fact-check row 5, 6 (108 > 74 mph threshold).
- Pittsburgh more than two feet: §2 PBZ "27.4" November 24-26, 1950" (rank 1); fact-check rows 7, 8 (27.4 in = 2.3 ft).
- Toll: §5 JKL "160 people were dead", NCEI "contributed to at least 160 deaths"; fact-check rows 9, 10.
- Buffalo: §3 JKL "only 200 miles to the north, Buffalo, NY enjoyed temps in the 40s"; §2 "recorded no snow at all"; Pittsburgh "temperatures in the single digits". Fact-check rows 11 to 15 (chip becomes "ABOUT 200 MI NORTH"; straight-line distance is about 179 mi, so no scale bar or ruler with numbers).
- Basemap: Natural Earth 50m admin-1 (public domain) inside the exemplar.

## 2. Datum, scale, orientation
- North up, no rotation in any frame. Projection: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213). Pins in map units: Newark (89893.2, 32871.1), Pittsburgh (67525.2, 34519.2), Buffalo (71817.5, 20859.4).
- Camera frames (screen = (map - top-left) × s):
  - A: s 0.12, top-left (80726.5, 28204.4): Newark at (1100, 560).
  - B: s 0.04024, top-left (54602.7, 19608.7): Pittsburgh (520, 600), Newark (1420, 534), Buffalo (693, 50).
  - C: s 0.04024, top-left (48638.5, 14141.5): Pittsburgh (760, 820), Buffalo (933, 270), Newark (1660, 754).
  - D: s 0.04024, top-left (59078.1, 18954.6): Newark (1240, 560), Pittsburgh (340, 626); Buffalo would be (513, 77) and must be gone by then.
- A to B is a 3x pull-out: use `logZoom` from `library/inhouse/snippets/helpers.js`, not linear scale. B to C and C to D are pans at the same scale (linear translate, power2.inOut).

## 3. Geometry (px)
- Basemap: state fills `#0b1016` to `#15202b`, state lines `#2a3644` 1.2 px (non-scaling stroke), coastline `#4a5560` 1.6 px, ocean = background radial gradient. Lakes as cut out in the exemplar.
- Pins (screen size constant at every scale: draw them on a HUD layer positioned from the camera maths, or counter-scale them): core dot 18 px, ring 34 px, 3 px stroke.
  - Newark: wind blue `#7fb2e5` fill. Pulse ring 34 to 70 px, opacity 0.8 to 0, 1.2 s, every 1.4 s (finite repeats sized to the window).
  - Pittsburgh: starts as an empty ring `#93a3b2`, fills snow white `#f2f5f8` on its cue (a fill sweep, top to bottom, 0.6 s, via a clip rect, not a fade only). Small snow dots (2 to 3 px, `#dfe7ee` at 0.7) fall inside a 90 px radius around it from the fill cue to the end of H1-S4 (drift 30 to 50 px/s).
  - Buffalo: ring `#93a3b2` at first; on its cue turns warm orange `#d8a13a` fill (amber 1 is the warm-air colour in tokens.md).
- Place labels (Arial 700, 26 px, `#dfe7ee`, paint-order stroke `#04070c` 5 px, as `.mm4-lab`): "NEWARK" to the left of its pin (right edge 24 px left of the dot), "PITTSBURGH" to the right of its pin (left edge 24 px right of the dot), "BUFFALO" to the right of its pin. No state names, no other city names.
- Chips (map-native, inside this comp; the glass surface from tokens.md: `rgba(10,16,24,.55)`, blur 18, 1 px `rgba(255,255,255,.14)` border, radius 14, padding 10 x 18):
  - Newark chip, stacked, anchored 30 px below-left of the Newark pin: line 1 "108 MPH" Arial Black 900 58 px `#f2f5f8`; line 2 "HURRICANE FORCE" Arial 700 22 px `#7fb2e5` tracking 3. In frame A the chip box is about x 820 to 1120, y 600 to 720.
  - Pittsburgh chip, 30 px right of the label: "2+ FEET OF SNOW" Arial Black 900 40 px `#f2f5f8`. In frame C it flips (text-state swap: old line y 0 to -20 autoAlpha 0, new line y 20 to 0, 0.35 s each) to "SINGLE DIGITS" in `#7fb2e5`.
  - Buffalo chip, 30 px right of the label: "ABOUT 200 MI NORTH" Arial 700 30 px `#dfe7ee`; swaps to "40s · NO SNOW" Arial Black 900 40 px `#d8a13a` (two halves: "40s" on its word, "· NO SNOW" on "no").
  - Toll line (H1-S3 only), centred on x 960, block top y 880: "AT LEAST 160 LIVES LOST" Arial Black 900 52 px `#f2f5f8`; under it "Source: NCEI · NWS Jackson, KY" Arial 700 20 px `#c8d3e0` tracking 1. Glass card behind both, centred, about 900 x 130 px; bottom edge at or above y 1026.
- Three type tiers: 58/52 (big), 40/30/26 (mid), 22/20 (small).
- Scan line: the exemplar's `.mm4-scan` (2 px, 1180 px wide) sweeping top to bottom at about 60 px/s for the whole comp, opacity 0.30.

## 4. Must be true in the picture
1. L1: no line, arc, arrow, band, gradient, "L" symbol, front, isobar or shading touches or joins any two pins in any frame. Pins are isolated dots on plain ground.
2. Geography is real: Buffalo sits north and slightly east of Pittsburgh (dx +173 px, dy -550 px at s 0.04024); Newark is about 900 px east of Pittsburgh at s 0.04024. Every pin is placed from the formula; a ±10 px check against the frame table above.
3. One reading target at a time: at most one chip at full opacity per moment; the previous chip dims to 0.35 or exits when the next lands. The toll line is alone on screen at full opacity (all chips at 0.35 or less during H1-S3).
4. "160" appears once on screen; "108 MPH" once; no number appears before its spoken word.
5. In H1-S5 only the Newark and Pittsburgh pins and their two place labels are visible: no chips, no Buffalo, no toll line. Pittsburgh reads small at the west side (frame D, x 340), Newark wind blue on the coast.
6. The last frame equals camera frame D exactly (g-intro-3-coast opens on it): Newark pin blue with "NEWARK" label, Pittsburgh pin white with "PITTSBURGH" label, nothing else on the map layer.
7. No scale bar, no mileage ruler, no compass rose with text.

## 5. Panel text (exact) and cues
Text strings: `NEWARK` · `108 MPH` · `HURRICANE FORCE` · `PITTSBURGH` · `2+ FEET OF SNOW` · `AT LEAST 160 LIVES LOST` · `Source: NCEI · NWS Jackson, KY` · `BUFFALO` · `ABOUT 200 MI NORTH` · `40s` · `· NO SNOW` · `SINGLE DIGITS`

Segment offsets (comp-local seconds; assumes 0.40 s gaps, replace with the real `data-start` differences from index.html):
`SEG = { h1s2: 0.000, h1s3: 7.065, h1s4: 11.230, h1s5: 21.580 }` ; segment lengths 6.665, 3.765, 9.950, 7.101 s.

Cues (segment-relative word time from `audio/<seg>.words.json`, comp time = SEG + t):
- H1-S2 0.00 "That's": frame A on, Newark pin pulsing, "NEWARK" label and the "108 MPH" chip line ALREADY ON at frame 0 (carries Paul's number across the cut). Camera drifts in 2 % over 0-3.4. `/* THATS @0.00 */`
- H1-S2 0.36 "hurricane": "HURRICANE FORCE" line in (`fromTo` autoAlpha 0, x -16 to 0, 0.35 s, power3.out). `/* HURRICANE @0.36 */`
- H1-S2 2.06 "Inland,": Newark chip dims to 0.35; camera pull-out A to B starts (logZoom, 1.9 s, expo.inOut), arrives 3.96. `/* INLAND @2.06 */`
- H1-S2 4.02 "Pittsburgh": Pittsburgh ring + label in, white fill sweep starts, snowfall starts. `/* PITTSBURGH @4.02 */`
- H1-S2 5.62 "two": chip "2+ FEET OF SNOW" in (`fromTo` autoAlpha 0, scale 0.9 to 1, 0.4 s, back.out(1.4)). `/* TWO FEET @5.62 */`
- H1-S3 1.18 "at least": all chips to 0.35 (0.3 s); toll card in (`fromTo` y 40 to 0, autoAlpha, 0.5 s, power3.out), line "AT LEAST 160 LIVES LOST" with the source line 0.3 s after. `/* AT LEAST @1.18 */`  (the number lands in the voice at "160" 1.42; the card is fully opaque by 1.68)
- H1-S3 3.48 end "lives." to H1-S4 0.20: toll card exits (`to` y 30, autoAlpha 0, 0.5 s, power3.in), finishing by H1-S4 0.20.
- H1-S4 0.00 "You'd": pan B to C (1.0 s, power2.inOut), arrives 1.00. Pittsburgh chip back to 1.0 opacity. `/* YOUD @0.00 */`
- H1-S4 0.44 "Buffalo,": Buffalo ring + label in (label after the pan settles, at 1.00 at the latest; no text rides the pan). `/* BUFFALO @0.44 */`
- H1-S4 1.32 "200": chip "ABOUT 200 MI NORTH" in. `/* 200 @1.32 */`
- H1-S4 5.24 "Buffalo": "ABOUT 200 MI NORTH" chip out (0.3 s). `/* BUFFALO2 @5.24 */`
- H1-S4 6.16 "40s": Buffalo pin fill turns `#d8a13a` (fill sweep 0.4 s), chip "40s" in. `/* 40S @6.16 */`
- H1-S4 6.64 "no": "· NO SNOW" in beside "40s". `/* NO SNOW @6.64 */`
- H1-S4 9.14 "single": Pittsburgh chip flips "2+ FEET OF SNOW" to "SINGLE DIGITS"; Buffalo chip dims to 0.35. `/* SINGLE @9.14 */`
- H1-S5 0.00 "It's": Buffalo pin, label and chip out; Pittsburgh chip out; snowfall stops; pan C to a 3 % wider version of D (1.4 s, power2.inOut). `/* ITS @0.00 */`
- H1-S5 1.00 "hurricane": Newark pin one strong pulse (ring to 90 px). `/* HURRICANE @1.00 */`
- H1-S5 2.38 "snow": Pittsburgh pin one pulse, white. `/* SNOW @2.38 */`
- H1-S5 1.40 to 7.10: slow push from 3 % wide to exactly frame D (ease none), so motion runs through the riser and ends on D. `/* SEE HOW ends @6.96 */`
Host: data-start = H1-S2 audio start, duration = SEG.h1s5 + 7.101 (28.681 s with the assumed gaps). The cut to g-intro-3-coast is a continuation on the same frame, not a hard vanish.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 6 applies: compute every pin's screen position from the formula and the frame table by script and print them in the receipt. Report any §4 vs §3 conflict instead of choosing.
