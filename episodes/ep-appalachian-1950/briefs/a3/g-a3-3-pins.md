# g-a3-3-pins: Newark, Pittsburgh, Buffalo on the swirl (A3-S3)
Builder: Sonnet 5.5, high effort. Depth: standard (pins and chips on an existing scene). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md`, then this brief.
Start from: g-a3-2's finished file (chart, dim, scan line, track, ghost, arrows, ring; copy them, prefix every id and class `a3p-`). Pin and chip style: `briefs/intro/g-intro-2-hookmap.md` §3 (the hook's pins, so the callback reads as the same pins).
Sits over: nothing underneath; chart still `media/a3/A3-S1_c1_nws-jkl-surface-1950-11-25.jpg` inside the comp, camera C1. Frame 0 = g-a3-2's last frame.

## 0. Claim
The same storm put Newark under ocean wind, Pittsburgh on the cold side in snow at single-digit temperatures, and Buffalo, about 200 miles north of Pittsburgh, in the 40s with no snow; one track joins the three. Then the question: why did it turn inland?

## 1. Source
- Pittsburgh single digits vs Buffalo 40s "only 200 miles to the north": `research/nws-facts.md` §3 JKL (spoken "about"; great circle about 179 mi, factcheck intro-r2 row 11, so no ruler or mileage on screen).
- Buffalo "recorded no snow at all": §2 JKL (factcheck a3-r1 row 9).
- Newark wind: §1 PHI Newark 108 mph (not shown here; g-a3-6 owns the number).
- Buffalo inside the warm arrows is inference, on screen only (factcheck a3-r1 row 9 note): no line or chip says why.

## 2. Datum, scale, orientation
Camera C1, static. Stations at the corrected chart points from g-a3-1's receipt; starting values: Newark (1380, 296), Pittsburgh (1078, 364), Buffalo (1132, 224). Buffalo is north and slightly east of Pittsburgh (dy about -140 px on this chart), as on the real map.

## 3. Geometry (px)
- Pins (constant size): core 18 px, ring 34 px, 3 px stroke.
  - Newark: wind blue `#7fb2e5` fill; pulse ring 34 to 70 px, opacity .8 to 0, 1.2 s, every 1.4 s (finite repeats) from its cue to the end.
  - Pittsburgh: snow white `#f2f5f8` fill (fill sweep top to bottom 0.5 s through a clip rect); snow dots (2 to 3 px `#dfe7ee` at .7) fall in a 70 px radius round it from its cue (30 to 50 px/s drift), seeded positions.
  - Buffalo: warm orange `#d8a13a` fill (sweep 0.4 s).
- Labels: Arial 700 26 px `#dfe7ee`, paint-order stroke `#04070c` 5 px. "NEWARK" right of its pin (left edge 24 px right of the dot; right edge <= 1600 since y < 680 is fine but keep <= 1824). "PITTSBURGH" left of its pin (right edge 24 px left of the dot). "BUFFALO" left of its pin.
- Chips (glass chip, radius 14, padding 10 x 18), each anchored 30 px from its label on the side away from the arrows' heads:
  - Pittsburgh chip below-left of its label: "SINGLE DIGITS" Arial Black 900 40 px `#7fb2e5` with "· SNOW" Arial Black 900 40 px `#f2f5f8` beside it (two halves, two cues).
  - Buffalo chip above-left of its label (box top >= 54): "40s" Arial Black 900 40 px `#d8a13a` with "· NO SNOW" beside it.
- Join: at the end, the red track gets one bright pass (as g-a3-2 at "line") and a 4 px `#d0121f` at .6 thin connector draws from the track's nearest point to each pin that the track does not already pass (Newark, Buffalo) so "the three pins are finally joined by the red track". Connectors are part of the track family (same red), dashed 8 6, not arrows.
- Question line (lower-third, the act's open loop A3b): glass card left 110, bottom 140, padding 18 x 28: "WHY DID IT TURN INLAND?" Arial Black 900 52 px `#f2f5f8`. Before it lands, both chips dim to .35.
- Source line "Source: NWS Jackson, KY" left 110, bottom 60.
- Tiers: 52 / 40 / 26 / 19.

## 4. Must be true in the picture
1. Buffalo's pin is inside the orange arrows; Pittsburgh's is among the blue arrows; Newark's is at the coast where the orange arrow W3 comes ashore.
2. One reading target at a time: at most one chip at full opacity; the earlier dims to .35 when the next lands.
3. "40s" appears only after "40s" is spoken (16.74); "SINGLE DIGITS" only after "single" (12.06). No mileage number on screen.
4. No chip, label or pin overlaps an arrowhead or another label in any frame, entrances included.
5. Nothing of this comp in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a3-s3.words.json`, seconds from A3-S3 start)
Text: `NEWARK` · `PITTSBURGH` · `BUFFALO` · `SINGLE DIGITS` · `· SNOW` · `40s` · `· NO SNOW` · `WHY DID IT TURN INLAND?` · `Source: NWS Jackson, KY`
- 0.00 frame 0 = g-a3-2 last frame (arrows flowing, ring turning). `/* NOW @0.00 */`
- 2.24 "Newark,": Newark pin + label in (scale .4 to 1, back.out(1.6), 0.4 s). `/* NEWARK @2.24 */`
- 2.82 "Pittsburgh,": Pittsburgh pin + label in. `/* PITTSBURGH @2.82 */`
- 3.58 "Buffalo.": Buffalo pin + label in (ring only, grey `#93a3b2`, no fill yet). `/* BUFFALO @3.58 */`
- 5.80 "Newark": Newark pulse starts; W3 arrowhead flashes once. `/* NEWARK2 @5.80 */`
- 8.28 "Pittsburgh": Pittsburgh fill sweep white, snowfall starts. `/* PITTSBURGH2 @8.28 */`
- 12.06 "single": chip "SINGLE DIGITS" in (scale .9 to 1, back.out(1.4), 0.4 s). `/* SINGLE @12.06 */`
- 10.40 "snow,": (before the chip) the snowfall thickens (second set fades in .5 s). `/* SNOW @10.40 */`
- 12.34 "digits.": "· SNOW" half in (x -12 to 0, 0.3 s). `/* DIGITS @12.34 */`
- 13.42 "Buffalo,": Pittsburgh chip dims .35; Buffalo pin fill sweeps orange. `/* BUFFALO2 @13.42 */`
- 16.74 "40s": chip "40s" in. `/* 40S @16.74 */`
- 17.26 "no": "· NO SNOW" in. `/* NO SNOW @17.26 */`
- 18.58 "So": both chips to .35; red track bright pass and connectors draw to Newark and Buffalo (0.8 s). `/* SO @18.58 */`
- 19.80 "usually": the dim ghost path brightens to .6 for 0.6 s and back to .3 (the usual path callback). `/* USUALLY @19.80 */`
- 21.08 "turn": question card in (y 30 to 0, autoAlpha, 0.5 s, power3.out). `/* TURN @21.08 */`
- Exit: last 0.6 s of the host: question card `to` y 30, autoAlpha 0 (0.6 s, power3.in); pins, labels and chips fade to 0 with it; the chart crossfade into g-a3-4 is g-a3-4's job.
Host: data-start = A3-S3 start, duration = 21.74 + 0.40 = 22.14 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
