# g-a3-6-squeeze: 980 vs 1050, wind ashore at Newark (A3-S6)
Builder: Sonnet 5.5, high effort. Depth: standard (two gauges, then pins on a coast map). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (frame N), then this brief.
Start from: `library/official` `mk-usage-arc` (thin circular gauge drawing on with a count) for the gauges; `library/inhouse/master-map-us-canada.html` for the coast basemap and pins. Prefix every id and class `a3s-`.
Sits over: nothing. Full-frame designed card (0.00 to 6.06), then full-frame designed map (6.06 to end), ground on from frame 0 (background `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`).

## 0. Claim
The low bottomed near 980 mb while pressure near 1050 mb sat to its northeast; that squeeze drove east and southeast wind ashore hard, the wind that hit Newark (108 mph), and along the coast it piled the tide up (record tide at Philadelphia).

## 1. Source
- NBC Connecticut (SECONDARY, nbcconnecticut.com/news/local/the-great-southeast-of-1950/26557/): "980ish mb" low, "1050ish mb high near Maine" (factcheck a3-r1 rows 31, 32; Wikipedia 978 hPa uncited; no primary, so both carry "≈").
- Same URL: "freakishly strong pressure gradient produced violent southeasterly and easterly winds across New England" (row 33).
- Newark 108 mph: `research/nws-facts.md` §1 PHI.
- Philadelphia record 10.8 ft tide: PHI (spent in A1-S9, so only "RECORD TIDE", no figure). NCEI "onshore winds along the coast caused extreme high tides".
- Newark's wind direction and a Delaware link are stated by no source (row 34): the arrows are generic onshore east/south-east flow, SCHEMATIC.

## 2. Datum, scale, orientation
Gauges: card layout, no map. Coast map: frame N, s 0.06, top-left (71559.9, 25871.1); Newark (1100, 420), Philadelphia (871, 682). North up. The Delaware River: trace it from the basemap's river path if the exemplar has one; else draw it from Delaware Bay mouth 38.8N 75.1W to Philadelphia (compute px from the formula, state in the receipt).

## 3. Geometry (px)
- Gauges (0.00 to 6.06): two 300 px circular dials, centres (620, 470) and (1180, 470). Arc 270° (from 135° to 405°), 14 px track `#2a3644`, value arc 14 px. Scale on both: 950 to 1060 mb (same scale, so the gap is honest). Left value arc `#d0121f` to 980; right `#7fb2e5` to 1050. Big numeral in each centre: Arial Black 900 64 px `#f2f5f8`: "≈ 980" and "≈ 1050"; under each, label Arial 700 22 px `#93a3b2` tracking 6: "LOW · MB" and "HIGH · MB". Counter count-up from 950 on its cue (power3.out, 1.0 s), leaf span only.
- Gap glow: a horizontal bar between the dials (x 800 to 1000, y 470, 10 px) `#d8a13a` glowing (blur 12) that pulses .4 to 1 (1.2 s, finite repeats) from "higher".
- Gloss under the dials, centred x 900, top y 700: "MB = millibars, a measure of air pressure" Georgia italic 26 px `#d8a13a`.
- Source line (whole comp): "Source: NBC Connecticut (secondary) · arrows schematic" left 110, bottom 90; basemap credit "Basemap: Natural Earth" bottom 60 from the map scene on.
- Transition 6.06: dials and gloss scale .9 and fade (0.5 s) while the coast map (frame N) fades in.
- Coast map: basemap as g-a3-4 styles. Pins: Newark wind blue `#7fb2e5` core 18 / ring 34, pulse 34 to 70 px every 1.4 s; Philadelphia white core. Labels Arial 700 26 px `#dfe7ee`, stroke `#04070c` 5 px: "NEWARK" left of its pin, "PHILADELPHIA" left of its pin.
- Wind arrows (5) `#7fb2e5` 8 px with heads, conveyor dashes: three from the open sea east/south-east of Newark (start x 1450 to 1560, y 360 to 600) to the coast at Newark; two from Delaware Bay up the river toward Philadelphia (stay x < 1600 for y >= 680: their starts sit at x <= 1100 once below y 680).
- Chips (glass chip, radius 14, padding 10 x 18): "108 MPH" Arial Black 900 58 px `#f2f5f8` right-below Newark's pin (box left 1140, top 450; right edge <= 1560); "RECORD TIDE" Arial Black 900 40 px `#f2f5f8` left of Philadelphia's label (box right edge 24 px left of the label, top about 650). A rising water band (a 20 px `#7fb2e5` .5 strip along the coast near Philadelphia that grows scaleY 0 to 1) under "RECORD TIDE".
- Tiers: 64/58 / 40/26 / 22/19.

## 4. Must be true in the picture
1. Both dials share one scale (950 to 1060); the 1050 arc is visibly longer than the 980 arc by the true ratio of (1050-950)/(980-950) = 3.33x.
2. "≈" is on both numbers; no other pressure value anywhere.
3. Wind arrows come from the sea (east and south-east) toward the land; none leaves the land.
4. "108 MPH" lands on "Newark," (12.06), never before; "RECORD TIDE" on "tide" (14.26); no tide figure on screen.
5. One reading target at a time; nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a3-s6.words.json`, seconds from A3-S6 start)
Text: `≈ 980` · `LOW · MB` · `≈ 1050` · `HIGH · MB` · `MB = millibars, a measure of air pressure` · `NEWARK` · `PHILADELPHIA` · `108 MPH` · `RECORD TIDE` · `Source: NBC Connecticut (secondary) · arrows schematic` · `Basemap: Natural Earth`
- 0.00 "The": both dial tracks on, empty; source line on. `/* THE @0.00 */`
- 0.14 "low": left label "LOW · MB" in. `/* LOW @0.14 */`
- 1.20 "980": left arc fills to 980 and counter runs 950 to 980 (1.0 s, power3.out). `/* 980 @1.20 */`
- 2.06 "millibars,": gloss line in (y 16 to 0, 0.4 s). `/* MILLIBARS @2.06 */`
- 3.74 "higher": right label in, right arc fills to 1050, counter 950 to 1050 (1.2 s, power3.out). `/* HIGHER @3.74 */`
- 5.02 "northeast.": gap bar glows and starts pulsing. `/* NORTHEAST @5.02 */`
- 6.28 "squeeze": dials squeeze toward each other (x ±60, 0.5 s, power2.in) then the card-to-map transition (0.5 s). `/* SQUEEZE @6.28 */`
- 8.22 "ocean": three sea arrows draw on toward Newark (0.8 s), conveyors start. `/* OCEAN @8.22 */`
- 9.38 "southeast,": the two Delaware arrows draw on. `/* SOUTHEAST @9.38 */`
- 10.24 "hard.": all arrows speed up 2x. `/* HARD @10.24 */`
- 12.06 "Newark,": Newark pin + label in; chip "108 MPH" in (scale .9 to 1, back.out(1.4), 0.4 s); sound gust lands here. `/* NEWARK @12.06 */`
- 13.38 "coast": Philadelphia pin + label in; "108 MPH" dims .35. `/* COAST @13.38 */`
- 14.26 "tide": water band rises; chip "RECORD TIDE" in. `/* TIDE @14.26 */`
- 15.42 "snow": no new text (the Picture line gives none): both chips dim to .35, arrows and Newark pulse keep moving to the end. `/* SNOW @15.42 */`
- Exit: last 0.6 s: chips `to` x 980, autoAlpha 0 (0.6 s, power3.in); map fades to `#04070c` (cut to g-a3-7's chart).
Host: data-start = A3-S6 start, duration = 17.58 + 0.40 = 17.98 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
