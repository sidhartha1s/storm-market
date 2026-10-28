# g-a1-8-cline-picture · A1-S4 4.62 to end · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (incl. "The elevation plate"). Base: `compositions/g-a1-11-elevation.html` if built first, else `compositions/g-intro-6-island.html` (copy the plate, renamed ids; edit neither). Exemplars: `episodes/ep6-katrina-2005/compositions/g-surge-ms.html` (a water body that rises and moves), `library/inhouse/snippets/helpers.js` `logZoom` (the 2x pull-out).

## 0. Claim
Cline's picture in 1891, as he described it: a large territory north of the island lay lower than the island, so a storm wave from the Gulf would spread out over it and thin out, and no cyclone could build a wave that would badly hurt the city. This is HIS model, labelled as his; it is not what happened (A4 pays that).

## 1. Source
- Scan / Commons: "as there is too large a territory to the north which is lower than the island, over which the water may spread, it would be impossible for any cyclone to create a storm wave which could [Commons: would] materially injure the city" (factcheck/a1-r1.md rows 17 to 20; sources-cline.md §1 "large, lower-lying territory to the north"). "Run off ... and thin out" is the writer's gloss of "spread" (row 20).
- "Cyclone" as Cline's word: factcheck/a1-r2.md row 13.
- No research row gives the mainland's elevation, the wave's height or the distance north: all are SCHEMATIC, no number on screen.

## 2. Datum, scale, orientation
- Plate px. Columns 0 to 1920 are the elevation plate exactly (datum y 780, 40 px/ft, Gulf left, island 360 to 1560). Extended north (right): bay water 1560 to 2400 (surface y 780, as the plate's bay), mainland 2400 to 3600, ground top at y 720 from 2400 to 3200 rising to y 700 at 3600 (SCHEMATIC: drawn lower than every point of the island above its shoreline, per Cline). Gulf extended left to x −200.
- Camera `screen = (960 + (X − cx)·s, 540 + (Y − cy)·s)`, pure function of comp time:
  - V0 (frame 0 to 1.52): s 1.0, c (960, 540): identical framing to g-intro-6 / g-a1-11.
  - V1 (S4 6.14 "north" to 7.54): pan to c (2500, 540), s 1.0, power2.inOut: bay and mainland fill the frame.
  - V2 (S4 10.30 "In" to 11.30): pull-out to c (1700, 600), s 0.5, `logZoom` (2x): whole plate x −200 to 3600 on screen (x 10 to 1910). Datum then at screen y 630, island crest y 456, mainland top y 600.
  - V2 holds with drift s 0.50 → 0.52 (`ease:none`) to the end.
- Labels and chips sit on a fixed HUD layer (they never ride the camera; they enter after a move settles and leave before the next starts).

## 3. Geometry (plate px unless marked screen)
- Mainland: one closed path, fill `#15202b`, top stroke `#93a3b2` 3 px; label "Mainland" (diagram tier) on the HUD, centred at screen (1300, 640) at V1 (on the ground fill, left of x 1500).
- Level line (S4 7.20 "lower"): dashed `#d8a13a` 2 px from the island crest plate (1020, 432) right to (3600, 432), drawn left to right 0.8 s; with it a short down-tick from the line to the mainland top at plate x 3000 (y 432 to 716), label "Lower than the island" Arial 700 26 px `#d8a13a` at screen (1200, 300) at V1 (Cline's words, no number).
- Spread arrow (S4 9.00 "spread"): dashed `#7fb2e5` 3 px arrow along the mainland top from plate (2450, 700) to (3450, 690), drawn left to right 0.7 s.
- Storm glyph: a spiral (the channel's hurricane symbol, 160 plate px, stroke `#93a3b2`) over the Gulf at plate (−60, 560), rotating slowly from V2; three wind arrows `#c8d3e0` pointing right (plate x 0 to 300, y 640 to 700).
- Storm wave: a mound on the Gulf surface, plate x −100 to 140 at start, peak 100 plate px above the datum (y 680), fill `#7fb2e5` opacity 0.75, 2 px `#7fb2e5` top edge. Moves right to the beach (front at x 360) 11.48 to 12.96, power1.inOut.
- Spill (13.50 to 15.16): the mound collapses at the beach (peak 680 → 772) while a thin sheet (4 plate px, same fill, drawn UNDER the house glyphs) runs over the island's top surface left to right (13.50 to 14.22), the bay surface rises 4 px (14.22), and the sheet spreads over the mainland (14.22 to 15.16), tapering 4 → 1 px toward x 3500.
- Thin out (15.40 "thin"): the whole sheet's opacity 0.75 → 0.25 over 1.0 s.
- Chip "TOO LARGE A TERRITORY TO THE NORTH" (glass, Shared rules, Arial Black 900 52 px, tag line "Isaac Cline, 1891" Arial 700 22 px `#93a3b2` tracking 4), screen `left:50%` with `xPercent:-50` set in `tl.set` at 0, top 130; about 1,280 x 130.
- Eyebrow "CLINE'S PICTURE, 1891" Arial 700 22 px `#93a3b2` tracking 6, screen centred x 960, top 120 (shows only after the chip has left).
- Label "Cyclone" Arial 700 30 px `#f2f5f8` next to the storm glyph at V2, screen (150, 360) left edge 96.
- Note "Schematic · vertical scale exaggerated" Arial 700 19 px `#93a3b2`, screen left 96, top 1000, from frame 0.
- Source line top-left: "Isaac Cline, Galveston Daily News, July 16, 1891".
- Tiers: 52 / 30, 26 / 22, 19.

## 4. Must be true in the picture
1. The mainland top is below the island everywhere the island is above its shoreline (mainland y ≥ 700 vs island crest 432 and shoulders 620): Cline's "lower than the island" holds by eye and by the level line.
2. The wave's peak never reaches the crest (peak y ≥ 680 plate, 252 px under the crest at 432) and no house glyph moves, tilts or disappears: this is Cline's picture, in which the city is not hurt.
3. The water sheet over the island is ≤ 4 plate px and drawn under the houses; it ends thinner over the mainland than where it started.
4. Every frame from 10.30 on carries "CLINE'S PICTURE, 1891" or the chip (Cline, 1891): the picture is never presented as what happened.
5. No number, height or distance on screen.
6. Labels never ride a camera move; nothing labelled in x >= 1600, y >= 680 (only unlabelled ground or water fill there).
7. Frame 0 equals the plate's g-intro-6 framing (the cut from the column lands on the known island).

## 5. Text and cues (a1-s4.words.json; comp-local = S4 time − 4.62)
- 4.62 ("He"): plate on at V0, note and source line in. /* HE SAID @4.62 */
- 6.14 ("north"): chip in; V1 pan starts (chip is on the HUD, it does not move). /* NORTH @6.14 */
- 7.20 ("lower"): level line draws, down-tick, "Lower than the island" label in at 7.54 (pan settled); "Mainland" label in with it. /* LOWER @7.20 */
- 9.00 ("spread"): spread arrow draws. /* SPREAD @9.00 */
- 9.70 to 10.10: chip out (`y:-24`), labels "Lower than the island" and "Mainland" out (0.3 s) before the pull-out.
- 10.30 ("In"): V2 pull-out; storm glyph and wind arrows fade in as it settles (11.30); eyebrow "CLINE'S PICTURE, 1891" in at 10.58 ("picture,"). /* HIS PICTURE @10.58 */
- 11.48 ("storm"): wave mound rises (scaleY 0 → 1 from the datum, 0.4 s) and travels right to 12.96 ("Gulf"). /* WAVE @11.48 */
- 13.50 ("run"): spill starts (collapse, island sheet, bay, mainland to 15.16). /* SPILL @13.50 */
- 15.40 ("thin"): sheet thins. /* THIN @15.40 */
- 20.28 ("city."): the 22 houses pulse once (scale 1 → 1.06 → 1, 0.5 s): the city stands, in his picture. /* CITY @20.28 */
- 20.54 ("Cyclone"): label "Cyclone" in beside the storm glyph. /* CYCLONE @20.54 */
- Host: A1-S4 4.62 to 23.639 plus the gap to A1-S5 (read the mounts).

## Motion for the whole window
Plate waves (phase tween, whole host), storm glyph rotation from V2 (finite), camera drift, HUD drift ±4 px. 16.74 to 20.28 has only these: they keep the frame alive (no 4 s gap).

## Exit
A1-S5 opens on a different cross-section: fade-through, root to 0 over the last 0.4 s.

## Footage under it
None: full-frame designed diagram.
