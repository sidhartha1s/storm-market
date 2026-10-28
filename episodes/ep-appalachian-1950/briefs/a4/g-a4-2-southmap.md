# g-a4-2-southmap: over the mountains to the Gulf (A4-S4, A4-S5)
Builder: Opus 5.5, high effort. Depth: deep (two camera moves, fill to the Gulf, crop-row layer). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a4/_list.md`, `briefs/a4/g-a4-1-kymap.md` (its last frame is this comp's frame 0), then this brief.
Start from: a copy of the built `compositions/g-a4-1-kymap.html` if it exists (same basemap, camera, fill, pin layer), else `library/inhouse/master-map-us-canada.html` cleaned as g-a4-1 §"Start from". File `compositions/g-a4-2-southmap.html`, prefix `a42-`.
Sits over: nothing. Full-frame designed scene on track 2. Corner circle on: nothing but basemap and fill at x ≥ 1600, y ≥ 680.

## 0. Claim
The same cold crossed the Appalachians and reached the Gulf: Asheville 1°F, Atlanta 3°F, Birmingham 5°F, Pensacola 22°F, with widespread crop damage in Georgia and South Carolina, while Buffalo, up near Canada, sat in the 40s that same weekend.

## 1. Source (quoted, with rows)
- §3 NCEI "Temperatures fell to 22°F in Pensacola, Florida, 5°F in Birmingham, Alabama, 3°F in Atlanta, Georgia, and 1°F in Asheville, North Carolina." (`factcheck/a4-r1.md` row 11; Pensacola also NWS Mobile "Low 22° occurred on the 25th/1950", row 15). Atlanta conflict: NCEI 3°F used, NBC CT -3°F rejected (act notes, conflict 5).
- Buffalo: §3 JKL "only 200 miles to the north, Buffalo, NY enjoyed temps in the 40s" (a4-r1 rows 12 to 14). NCEI gives no dates for the Southeast lows, so nothing on screen pairs a Buffalo hour with a Southeast hour (no clock, no date on these chips).
- Crops: NCEI "this record cold led to widespread crop damage, particularly in Georgia and South Carolina" (a4-r1 row 17).

## 2. Datum, scale, orientation
North up. Projection and pins: `_list.md`.
- Frame 0 = P2s: s 0.075, top-left (35150.0, 43938.6) (g-a4-1's last frame, pins only).
- P4: s 0.015, top-left (-5316.0, 12192.7): Buffalo (1157,130), Asheville (945,741), Atlanta (840,895), Birmingham (700,915); Kentucky pins as small dots at (719..889, 518..656); Chicago (653,214).
- P0: s 0.012, top-left (-15129.9, 11692.7): Pensacola (659,945), Birmingham (678,738), Atlanta (789,722), Asheville (874,599), Buffalo (1043,110), Chicago (640,178); state centres GA (835,793), SC (950,712).
- P2s to P4 is a 5x pull-out: `logZoom`. P4 to P0 is 1.25x plus a pan: linear, power2.inOut.

## 3. Geometry (px)
- Basemap, fill, pin style, source line spot, basemap credit, scan line: as g-a4-1 (`_list.md`).
- Cold fill edge per cue in §5 (lat 36.4 at frame 0, to 30.2 at the Gulf). The Gulf coast clips it (land-clipped), so the fill visibly stops at the water.
- Kentucky and Chicago pins: dots only, 12 px core, at 0.6 opacity in P4 and P0; Farmers stays grey.
- Buffalo pin: orange, glow breathing (0.5 to 0.7, 2 s period, finite repeats) whenever on screen; it enters the frame during the pull-out.
- Labels and values (HUD layer):
  - Asheville (P4): label "ASHEVILLE" right of the pin (left edge 969, centred y 741), value "1°F" Arial Black 900 52 px `#7fb2e5` right of the label, 14 px gap.
  - Atlanta (P4): label "ATLANTA" right of the pin (left edge 864, centred y 895), value "3°F" right of it.
  - Birmingham (P4): label "BIRMINGHAM" left of the pin (right edge 676, centred y 915), value "5°F" left of the label (right edge 14 px before it). Keep x ≥ 96.
  - Buffalo (P4): label "BUFFALO" right of the pin (left edge 1181, centred y 130), value "40s" Arial Black 900 52 px `#d8a13a` right of the label. Top of the value box ≥ 54.
  - Pensacola (P0): label "PENSACOLA" right of the pin (left edge 683, centred y 945), value "22°F" right of it, 52 px `#7fb2e5`. Box bottom ≤ 1026.
  - Crop chip (P0): glass, left 1060, top 600, right edge ≤ 1584: line 1 "WIDESPREAD CROP DAMAGE" Arial Black 900 34 px `#f2f5f8`; line 2 "GEORGIA · SOUTH CAROLINA" Arial 700 22 px `#93a3b2` tracking 3. It sits over the Atlantic east of South Carolina; a 2 px `#93a3b2` leader line from its left edge to the SC coast near (1000, 700) is optional, and if drawn it must not cross any label.
- Crop rows (SCHEMATIC, NOT TO SCALE): a pattern of straight furrow lines clipped to the Georgia and South Carolina state paths: 2 px lines, 9 px apart at P0 scale, angle -18°, colour `#d8a13a` at 0.35 (warm, living rows). Frost: a second copy of the same pattern in `#f2f5f8` at 0.85, revealed by a clip rect sweeping north to south over each state, then small frost glints (3 px `#f2f5f8` dots, 20 of them, scattered inside the two states, each a 0.4 s blink, at most 1.2 s apart) for the rest of the comp.
- Source line text changes per segment (crossfade 0.3 s, at the segment start): S4 "Source: NOAA NCEI · NWS Jackson, KY"; S5 "Source: NOAA NCEI".
- Type tiers: 52 big, 34/26 mid, 22/20/19 small.

## 4. Must be true in the picture
1. Geography is real: Asheville north-east of Atlanta, Birmingham west of Atlanta, Pensacola on the Gulf coast south of Birmingham, Buffalo far north; every pin within ±10 px of the `_list.md` frame table.
2. The cold fill never covers Buffalo, New York or the New Jersey coast; Buffalo stays orange and is the only warm pin.
3. The fill edge has passed a pin's latitude before that pin turns blue: Asheville 35.60 by S4 2.64, Atlanta 33.75 by 5.88, Birmingham 33.52 by 8.42, Pensacola 30.42 by S5 2.98.
4. No value before its word: "1°F" not before "one" (S4 4.54), "3°F" not before "three" (6.62), "5°F" not before "five" (10.40), "40s" not before "40s" (15.58), "22°F" not before "22" (S5 6.80).
5. One reading target: the previous value dims to 0.6 when the next lands; the Buffalo "40s" lands alone (Southeast values at 0.6).
6. The crop layer sits only inside Georgia and South Carolina (no rows in Florida, Alabama or North Carolina) and frosts only after "record cold" (S5 15.58).
7. The last frame is P0 with all cold pins blue (Farmers grey), Buffalo orange, the Pensacola label and value at 0.6, the crop chip on, the fill reaching the Gulf. This is the "drained map" the act names before Paul's clip.
8. Corner x ≥ 1600, y ≥ 680 holds only basemap and fill.

## 5. Panel text (exact) and cues
Text strings: `ASHEVILLE` · `1°F` · `ATLANTA` · `3°F` · `BIRMINGHAM` · `5°F` · `BUFFALO` · `40s` · `PENSACOLA` · `22°F` · `WIDESPREAD CROP DAMAGE` · `GEORGIA · SOUTH CAROLINA` · `Source: NOAA NCEI · NWS Jackson, KY` · `Source: NOAA NCEI` · `Basemap: Natural Earth`

Segment offsets (0.40 s gaps assumed): `SEG = { a4s4: 0.000, a4s5: 16.505 }` ; lengths 16.105, 18.273 s.

Cues (segment-relative, from `audio/a4-s4.words.json`, `a4-s5.words.json`; comp time = SEG + t):
- S4 0.00 "Then": pull-out P2s to P4 (logZoom, 1.9 s, expo.inOut), arrives 1.90; fill edge 36.4 to 35.4 by 2.40 (power2.inOut) as the frame passes the mountains. `/* CROSSED THE MOUNTAINS @0.00 */`
- S4 2.64 "Asheville,": Asheville pin turns blue (fill sweep 0.5 s), label in. `/* ASHEVILLE @2.64 */`
- S4 4.54 "one": "1°F" in (`fromTo` autoAlpha 0, scale 0.9 to 1, 0.4 s, back.out(1.4)). `/* ONE ABOVE @4.54 */`
- S4 4.60 to 5.80: fill edge 35.4 to 33.3 (power1.inOut).
- S4 5.88 "Atlanta": pin + label. `/* ATLANTA @5.88 */`
- S4 6.62 "three": "3°F" in. `/* THREE ABOVE @6.62 */`
- S4 8.42 "Birmingham,": pin + label. `/* BIRMINGHAM @8.42 */`
- S4 10.40 "five": "5°F" in. `/* FIVE ABOVE @10.40 */`
- S4 11.46 "That same weekend": Southeast labels and values to 0.6; slow drift up 20 px (ease none, 11.46 to 16.1) toward Buffalo. `/* SAME WEEKEND @11.46 */`
- S4 12.72 "Buffalo,": Buffalo glow one strong pulse (ring 30 to 70 px), label in. `/* BUFFALO @12.72 */`
- S4 15.58 "40s.": "40s" in (`fromTo` autoAlpha 0, y 14 to 0, 0.35 s, power3.out). `/* 40S @15.58 */`
- S5 0.00 "It": every label and value out (0.4 s, power3.in); move P4 to P0 (1.8 s, power2.inOut); fill edge 33.3 to 30.2 from 0.30 to 1.82, front line bright. `/* DIDNT STOP @0.00 */`
- S5 1.82 "Mexico.": fill meets the coast; front line flashes once and fades to 0 (the front has nowhere left to go). `/* GULF @1.82 */`
- S5 2.98 "Pensacola,": Pensacola pin turns pale blue, label in. `/* PENSACOLA @2.98 */`
- S5 6.80 "22": "22°F" in. `/* 22 DEGREES @6.80 */`
- S5 8.30 to 13.4: hold; Pensacola ring pulse every 1.4 s (finite repeats) and a 2 % slow push centred on (760, 820), ease none.
- S5 13.50 "In Georgia": Pensacola label and value to 0.6; crop rows fade in over GA then SC (0.4 s each, 0.25 s apart). `/* GEORGIA @13.50 */`
- S5 15.58 "record cold": frost sweep north to south over both states (1.2 s, power1.in); glints start. `/* RECORD COLD @15.58 */`
- S5 16.74 "widespread": crop chip in (`fromTo` x 40 to 0, autoAlpha, 0.5 s, power3.out), line 2 at 17.16 "crop". `/* WIDESPREAD @16.74 */`
- To end: glints and scan line keep moving; no exit (the edit cuts to Paul's clip 5 on frame P0).
Host: data-start = A4-S4 audio start, duration = SEG.a4s5 + 18.273 + 0.40 = 35.178 s (assumed gaps).

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 6: pin and label anchors computed by script from the formula, printed in the receipt. Item 3: frame 0 must match g-a4-1's last frame pixel for pixel on the map layer (read both frames side by side).
