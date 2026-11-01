# BRIEF g-a3-apartments · A3-S4 · DEEP (Opus 5.5, high effort) · on base `g-master-map`

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Base: `g-master-map` (copy its BASEMAP block verbatim, as in `g-a3-map-homes`). Drawing part: `episodes/ep8-krakatau-seabed/compositions/g-slope.html` for line weight and labelling.
Before this host: the NIST photograph of a demolished apartment complex (a3-s4 0.00 → 7.96, credit via the source-label snippet).

**Open (left out of the drawing):** how the 12 split across the three complexes; where the three complexes are; which outline is Somerset; how many storeys Somerset had. Dots go where the base's fatality layer puts them; if it has no sourced per-complex positions, the 12 dots sit in a tray of 12 beside the three outlines (2 rows of 6, 10 px apart) so no split is implied. The outlines are never labelled with a name. The staircase drawing is SCHEMATIC, NOT TO SCALE, and says so.

## 0. What this graphic claims
Twelve people were lost in three apartment complexes, all above ground, in buildings with no protected space (H19); at Somerset one woman got out of her apartment and rode it out under the building's staircase with her neighbors (H20).

## 1. SOURCE
- H19, Sec. 4.6.2.2: "All 12 fatalities occurred in apartment complexes that were rated as "demolished." These complexes were primarily wood-frame structures, and were not equipped with underground or aboveground protection areas. Consequently, all of those killed were located above ground when the storm hit".
- H20, Sec. 1.2: "In the Somerset complex, a survivor recalled evacuating her apartment and taking refuge underneath the building's staircase with her neighbors, rather than remaining inside her garden-style apartment."
- H26 / Table 4-3: apartments 12, base 154.

## 2. DATUM, SCALE, ORIENTATION
Part A: the base's projection, at the end framing of g-a3-map-homes (residential push-in). Positions computed by script from the base's data, stated in the receipt.
Part B (the drawing): full frame, schematic. **Grade line y = 760**, full width, stroke `#93a3b2` 2 px; earth below as in g-a3-house-section.

## 3. GEOMETRY
Part A:
- The 59 house dots from g-a3-map-homes stay at opacity .35.
- Three apartment outlines: rectangles ≈ 40 × 26 px, stroke `#dfe7ee` 2 px, at the base's positions.
- 12 dots: 7 px, `#c0392b`, inside the outlines (or in the tray, see Open).
- Chip (glass popup-chip, left 96, top 96): "12 IN APARTMENTS", Arial Black 900, 52 px.
Part B (fade-through 0.5 s from the map):
- Building: two-storey garden-style block, x 360–1560, floors y 610–760 and 460–610, roof line y 440. Wood-frame walls stroke `#dfe7ee` 3 px, fill rgba(223,231,238,.05). Ground-floor apartment doors at x 560 and 820.
- Stair bay x 1100–1300: two flights, lower flight from (1110, 760) up to (1290, 610), upper flight from (1290, 610) up to (1110, 460), treads every 18 px. The space under the lower flight is the triangle (1110,760) – (1290,760) – (1290,610).
- Figures (amber `#d8a13a`, 60 px tall crouched silhouettes): "her" starts at the door x 560, feet y 760; ends under the lower flight at (1250, 760). Two neighbours appear beside her at (1170, 760) and (1210, 760). All three inside the triangle.
- Labels (22 px diagram labels): "Somerset complex" centred at (960, 410), above the roof; "Staircase" at (1330, 560), right of the bay; "Schematic · not to scale" 19 px at left 96, y 990.
- Source line (glass source-label, left 96, baseline ≤ 1026, 20 px): "NIST Sec. 4.6.2.2 · Sec. 1.2" on for the whole host.

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 12 apartment dots and exactly 3 apartment outlines; no number shown other than 12.
2. No dot, figure or marker below ground anywhere. In Part B every figure's feet are on y 760 (grade), never below it.
3. The three figures end inside the triangle under the lower flight, not in an apartment and not on the stair treads.
4. Exactly one figure travels (door → under the stair); two appear there. No label counts the neighbours.
5. No outline carries a name; "Somerset complex" appears only on the drawing.

## 5. PANEL TEXT (exact) and CUES (a3-s4.words.json)
Text: "12 IN APARTMENTS" · "Somerset complex" · "Staircase" · "Schematic · not to scale" · "NIST Sec. 4.6.2.2 · Sec. 1.2".
Host: a3-s4 "every" @7.96 → "it?" @20.48 + 0.6.
- 7.96 "every": map on from frame 0 at the residential framing; the three outlines draw on (0.4 s).
- 8.70 "twelve": 12 dots light (stagger 0.05 s); chip in.
- 9.40 "above": the 12 dots pulse once (scale 1 → 1.4 → 1).
- 11.36 "At": chip out (0.6 s); fade-through to the drawing (0.5 s).
- 11.70 "Somerset": building draws on (strokes 0.8 s); "Somerset complex" label in at 12.4.
- 13.42 "out": "her" figure appears at the door x 560 and walks east along y 760 (x tween, 2.6 s, power1.inOut) to (1250, 760), arriving at 16.14.
- 16.14 "staircase": stair bay strokes brighten `#93a3b2` → `#f2f5f8`; "Staircase" label in.
- 16.98 "neighbors.": two neighbours in (autoAlpha + y 12 → 0, 0.4 s, 0.15 s apart).
- 17.0 → end: figures breathe (y ±2 px), slow push 1.00 → 1.04 on the drawing; text exits per quickref "Motion and exits" in the last 0.6 s.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-apartments`, root id `g-a3-apartments-root`.
