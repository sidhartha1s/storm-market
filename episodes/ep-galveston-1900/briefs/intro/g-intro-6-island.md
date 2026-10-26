# g-intro-6-island · T1-S1 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `episodes/ep6-katrina-2005/compositions/g-surge-ms.html` (cross-section on a datum line with a measured height) and `library/inhouse/then-now-scale.html` (one measured axis). Reference worked brief: `references/mg-brief-example-g-slope.md`.

## 0. Claim
Galveston was an island city of about 38,000 people whose highest ground was 8.7 ft above the sea; it had been warned, and still few people left.

## 1. Source
- Population: TSHA "the city of 38,000 inhabitants" (sources-cline.md §5; factcheck-A/C/D T1-S1). Nearly 38,000 (OSU, Wikipedia). The 37,789 census figure is UNSOURCED: never on screen.
- Highest point: NPS "the highest elevation on Galveston Island was 8.7 feet" (sources-cline.md §5). Average elevation "barely four feet" (OSU Origins, sources-cline.md §5 conflict 4).
- Warned: TSHA "placed Galveston under a 'storm warning' on September 7" (sources-cline.md §6).
- Few left: NPS "comparatively few people had evacuated the city" (factcheck-C/D H1-S5, chip FEW HAD LEFT CONFIRMED). No number for how many left exists in the research: nothing on screen may quantify it.

## 2. Datum, scale, orientation
- North-south cross-section of the island, looking west: Gulf of Mexico on the LEFT (south), Galveston Bay and the mainland on the RIGHT (north).
- Datum: mean sea level = the line y 780, x 96 to 1824.
- Vertical scale: 40 px per ft. 8.7 ft = 348 px, so the crest is at y 432. 4 ft = 160 px (y 620).
- Horizontal: SCHEMATIC, NOT TO SCALE (no island width is in the research). Vertical is exaggerated against the horizontal; the diagram says so on screen.

## 3. Geometry (px)
- Water: two bodies below y 780 filled `#0b1016` to `#04070c`, with a surface line `#5a768f` 3 px. Gulf x 96 to 360; bay x 1560 to 1824 (bay narrower, calmer: smaller wave amplitude).
- Island profile (one closed path, fill `#15202b`, top stroke `#93a3b2` 3 px): Gulf beach (360, 780) up to (520, 640), shoulder to (720, 620) [4 ft], up to the crest plateau (900, 432) to (1020, 432) [8.7 ft], down to (1200, 620) [4 ft], to (1400, 640), to the bay shore (1560, 780). Below 780 the island fill continues to y 900 and fades out.
- Houses: 22 small house glyphs (28 x 24 px, `#4a5560`, roof `#93a3b2`) sitting on the profile between x 560 and 1380, spaced evenly by a script from the profile path (their bottoms on the line within 2 px).
- Measure bracket: a vertical dashed line `#d8a13a` 3 px at x 960 from y 780 (sea level) up to y 432 (crest), drawn upward; end ticks 30 px wide; at y 780 the tick label "Sea level" Arial 700 22 px `#93a3b2` left of the bracket base.
- Labels (Arial 700 22 px `#93a3b2` tracking 3, diagram-label tier): "Gulf of Mexico" centred over the Gulf water at (228, 840); "Galveston Bay" at (1692, 840); "Galveston Island" above the crest is NOT used (the chip names the city).
- Note: "Vertical scale exaggerated" Arial 700 19 px `#93a3b2` at left 96, top 1000.
- Chips (glass, `_list.md` "Shared rules" chip spec):
  - C1 "ABOUT 38,000 PEOPLE", centred on x 960, top 150.
  - C2 "HIGHEST POINT ABOUT 8.7 FT", left edge at x 1000, top 290 (card bottom about y 400: above the crest line at y 432 and the descending profile, right of the bracket top; not over either).
  - C3 "WARNED", centred x 960, top 150 (C1's spot, after C1 leaves).
  - C4 "FEW HAD LEFT", centred x 960, top 260, under C3.
- Leaving dots: 3 of the 22 houses' small person dots (8 px `#f2f5f8`) travel right along a dashed arrow from (1380, 600) over the bay to the mainland edge at (1800, 700); only these 3 move. No count is printed.
- Source line top-left: "Texas State Historical Association · National Park Service".

## 4. Must be true in the picture
1. Crest top at y 432 ±4 and sea level at y 780 ±2: the bracket measures exactly 348 px (8.7 × 40). The 4 ft shoulders sit at y 620 ±4 (160 px). Ratio crest/shoulder height = 2.18 within 3 %.
2. Gulf on the left, bay on the right, and the labels say so.
3. Nothing shows water rising over the island. The bracket rises; the sea does not (the 15 ft surge belongs to a later act; a rising sea here would claim the surge was 8.7 ft).
4. The narration says "less than nine feet" and the chip says 8.7: both true; the chip keeps "ABOUT".
5. The leaving dots are clearly a small minority (3 of the 22 houses' dots) and no number or fraction appears.
6. Nothing in x >= 1600, y >= 680 except the bay water and the leaving-dots arrow head, which is an unlabelled shape; the circle stays off for this comp's window (a highlighted path is under it). Report this to the orchestrator.

## 5. Text and cues (t1-s1.words.json, segment 11.717 s; host starts at "island" 0.88)
Comp-local = word time − 0.88.
- 0.88 ("island") /* ISLAND @0.88 */: frame 0 shows sea, datum and the profile already drawn (the cut lands on a finished cross-section); waves moving. Source line in at 0.88.
- 2.14 ("coast"): "Gulf of Mexico" and "Galveston Bay" labels in, 0.4 s stagger 0.3.
- 2.90 ("home"): houses pop in left to right, 0.03 s apart, `scale 0 -> 1` from their base, back.out.
- 3.48 ("38" 3.48) /* 38,000 @3.48 */: C1 in; its figure counts 10,000 to 38,000 on a leaf, 3.48 to 4.38, power3.out, landing with "people" 4.50.
- 5.28 ("Its"): C1 out (slide right). 
- 5.42 ("highest" 5.42) /* HIGHEST @5.42 */: bracket draws up from sea level to the crest, 5.42 to 6.70, power2.out; crest plateau stroke brightens `#d8a13a` as it arrives.
- 6.74 ("nine" 6.74): C2 in. "Vertical scale exaggerated" note fades in at 6.74 too.
- 8.40: C2 out (before "The" 8.46).
- 9.22 ("warned" 9.22) /* WARNED @9.22 */: C3 in.
- 10.86 ("few" 10.86) /* FEW @10.86 */: C4 in under C3; C3 dims to opacity 0.6; the 3 dots leave along the arrow 10.86 to 11.70.
- Host: T1-S1 0.88 to 11.717 plus 1.0 s land time if the edit leaves a pause (default end 11.717 + the gap to I1-S1, capped at 12.70).

## Motion for the whole window
Waves: the two water surfaces are sine paths whose phase tweens continuously (Gulf amplitude 6 px, bay 3 px, `ease:none`, one long tween over the whole host). A slow camera push on the whole diagram, scale 1.00 to 1.04, `ease:none`, over the host (linear is fine at this size). Chips drift.

## Exit
I1-S1 opens on the MWR page (a cut): fade-through, the root to 0 over the last 0.4 s.

## Footage under it
None: full-frame designed diagram (root background tokens.md radial gradient).
