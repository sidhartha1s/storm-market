# g-a1-4-overflow · A1-S3 0.00 to 5.46 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (incl. "The elevation plate"). Exemplar: `compositions/g-intro-6-island.html`: copy its plate (water, profile, houses, wave motion, note) into this file with renamed ids; do not edit g-intro-6.

## 0. Claim
Galveston was a sand island in the Gulf, and every so often high water swept over the beachfront (the "overflows" people were used to), not over the town.

## 1. Source
- TSHA Galveston Hurricane of 1900: Galvestonians "had become used to occasional 'overflows,' when high water swept beachfronts" (factcheck/a1-r1.md row 12, CORRECTED from "streets" to "beachfronts"; factcheck-A.md H1-S5). https://www.tshaonline.org/handbook/entries/galveston-hurricane-of-1900
- No overflow height exists in the research: the tide line's rise is SCHEMATIC and carries no number.

## 2. Datum, scale, orientation
The plate exactly as g-intro-6 (`_list.md` "The elevation plate"): datum y 780, 40 px/ft, Gulf LEFT (south), bay RIGHT (north). Horizontal schematic; note "Vertical scale exaggerated" (19 px, left 96, top 1000) on from frame 0.

## 3. Geometry (px)
- Plate as g-intro-6 (profile, 22 houses, water bodies, waves). No measure bracket, no chips from g-intro-6.
- Overflow sheet: a thin water shape `#7fb2e5` at opacity 0.55 with a 2 px `#7fb2e5` top edge, riding up the Gulf beach slope (360,780) to (520,640). Its leading edge runs up the slope to x 451, y 700 (the slope point 80 px above the datum, 2 ft at the plate's scale, schematic) and back down to the datum. Thickness 6 to 10 px, following the slope.
- Labels (diagram tier): "Gulf of Mexico" at (228, 840); "Galveston Bay" at (1692, 840) is NOT shown (keep the corner clear); "Sand island" centred over the crest at (960, 360), set as the beat's headline: Arial Black 900 52 px `#f2f5f8`, paint-order stroke `#04070c` 6 px (bottom ≈ 390, clear of the crest at 432 and the crest houses at ≥ 408).
- Tag on the overflow: "'Overflows'" Arial 700 26 px `#7fb2e5` at (330, 600), left-aligned, with a 1 px `#7fb2e5` leader to the sheet's leading edge at (451, 700); the leader ends 6 px short of the sheet.
- Source line top-left: "Texas State Historical Association".
- Tiers: 52 / 26 / 22, 19.

## 4. Must be true in the picture
1. The water's leading edge never passes x 520 (the top of the beach slope) and never touches a house glyph (first house at x ≥ 560): the overflows swept the beachfront, not the streets.
2. No number, height or date on screen.
3. Gulf on the left, labelled; sea level stays at y 780 except the overflow sheet on the slope.
4. Nothing in x >= 1600, y >= 680 except unlabelled bay water.
5. Frame 0 is the finished cross-section (the cut from the page lands on a drawn plate).

## 5. Text and cues (a1-s3.words.json, segment 21.589 s; host 0.00 to 5.46)
- 0.00: plate on, waves moving; source line in (0.4 s). /* ISLAND @0.00 */
- 0.64 ("sand"): "Sand island" label in (autoAlpha, y 10 → 0, 0.35 s).
- 1.60 ("Gulf,"): "Gulf of Mexico" label in.
- 3.12 ("high"): overflow sheet runs up the slope 3.12 to 4.14 ("over"), power2.out, reaching x 451 on "beachfront." 4.52. /* OVERFLOW @3.86 */
- 3.86 ("swept"): tag "'Overflows'" and leader in.
- 4.60 to 5.30: sheet runs back down to the datum (power2.in); tag stays.
- Host: A1-S3 0.00 to 5.46 ("Down" is the cut to g-a1-5).

## Motion for the whole window
Wave phase tween over the host (as g-intro-6); slow push scale 1.00 to 1.03, `ease:none`; labels drift ±4 px.

## Exit
Cut to the coast map at 5.46: the root fades to 0 over 5.16 to 5.46 (fade-through).

## Footage under it
None: full-frame designed diagram (tokens.md radial ground).
