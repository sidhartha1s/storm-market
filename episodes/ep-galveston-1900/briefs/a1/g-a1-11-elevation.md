# g-a1-11-elevation · A1-S6 2.84 to A1-S7 end · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (incl. "The elevation plate"). Base: `compositions/g-intro-6-island.html` (copy the plate, renamed ids; do not edit it). Exemplar: `library/inhouse/then-now-scale.html` (one measured axis with comparison figures). This plate is also the base for g-a1-8 and g-a1-4: build it first and send it for a full-size read.

## 0. Claim
Set against Cline's reasoning, the island itself was low: highest point about 8.7 ft, average about 4 ft (well under a 10 ft basketball hoop), and the ground under Cline's house in 1900 at 5.2 ft (less than a tall man's height). By 1899 the world's foremost cotton port stood on that ground.

## 1. Source
- Highest point 8.7 ft: NPS "the highest elevation on Galveston Island was 8.7 feet" (sources-cline.md §5; factcheck-A.md T1-S1; factcheck/a1-r1.md row 27).
- Average about 4 ft: OSU Origins "barely four feet" (sources-cline.md §5; factcheck/a1-r1.md row 28, chip CORRECTED to "AVERAGE ABOUT 4 FT").
- Cline's house 5.2 ft in 1900: Cline, Monthly Weather Review, Sept 1900, "The ground was 5.2 feet elevation" (sources-cline.md §3; factcheck/a1-r1.md row 29, chip CORRECTED to "CLINE'S HOUSE, 1900: 5.2 FT"). No datum is claimed; the plate's datum is mean sea level, and the chip says only "5.2 FT". Where the house stood along the island: not in the research, so its x is schematic.
- Hoop 10 ft and "tall man" above 5.2 ft: factcheck/a1-r2.md rows 17, 19 (arithmetic comparisons).
- World's foremost cotton port by 1899: TSHA Galveston Wharves, Port of Galveston (factcheck/a1-r1.md row 31).

## 2. Datum, scale, orientation
The plate exactly (`_list.md`): datum y 780, 40 px/ft, Gulf LEFT, bay RIGHT, profile and 22 houses as g-intro-6. Computed: 4 ft y 620, 5.2 ft y 572, 6 ft y 540, 8.7 ft y 432, 10 ft y 380; ground at 5.2 ft on the Gulf-side slope x 766.0. Horizontal schematic; note "Vertical scale exaggerated" (19 px, left 96, top 1000) from frame 0. Camera: whole-plate push 1.00 → 1.03, `ease:none`, over the host (centre 960, 540); chips, labels on a fixed HUD layer.

## 3. Geometry (px)
- Crest bracket (as g-intro-6): dashed `#d8a13a` 3 px at x 960 from y 780 to 432, end ticks 30 px; "Sea level" label (22 px) left of its base.
- Average line: dashed `#d8a13a` 2 px at y 620 from x 360 to 1560, drawn BEHIND the house glyphs.
- Cline's house: one house glyph recoloured `#d8a13a` (the glyph nearest x 766; if none sits within 20 px, add one at x 766, bottom on y 572 ±2), plus a dashed `#d8a13a` 2 px bracket at x 766 from y 780 to 572 with end ticks 24 px.
- Ghost hoop (comparison, standing on the datum over the Gulf): pole x 150 from y 780 to 380, backboard 6 x 70 px at x 150 (y 330 to 400), rim 36 px wide at y 380 to x 186; all dashed outline `#93a3b2` 2 px, no fill. Label "Basketball hoop" 22 px `#93a3b2` left edge 96, baseline 318.
- Ghost man: outline silhouette 240 px tall (6 ft at 40 px/ft), feet on y 780, centred x 300 (head top y 540), dashed `#93a3b2` 2 px, no fill, no height number. Label "Tall man" 22 px `#93a3b2` centred x 300, baseline 526.
- Chips stack top-right, right-aligned at x 1824 (glass, Arial Black 900 40 px `#f2f5f8`, padding 18px 28px, about 88 px tall, left edge ≥ 1064 so they clear the crest houses):
  - C1 "HIGHEST POINT ABOUT 8.7 FT", top 130.
  - C2 "AVERAGE ABOUT 4 FT", top 236.
  - C3 "CLINE'S HOUSE, 1900: 5.2 FT", top 342 (bottom ≈ 430; the right slope's house tops at x 1064 are at ≈ 454).
- S7 buildings: 14 more glyphs (warehouse 40 x 30, `#4a5560`, roof `#93a3b2`) between x 560 and 1380, bottoms on the profile (±2, computed by script from the path), interleaved with the houses, never overlapping one.
- Chip C4 "WORLD'S FOREMOST COTTON PORT · 1899": glass, Arial Black 900 52 px, centred x 960, top 140 (about 1,200 x 100; bottom 240).
- Source line top-left, swaps: S6 "National Park Service · Ohio State University, Origins · Isaac Cline, Monthly Weather Review, Sept. 1900"; S7 "Texas State Historical Association · Port of Galveston".
- Tiers: 52 / 40, 26 / 22, 19.

## 4. Must be true in the picture
1. Bracket 8.7 ft = 348 px (y 780 to 432 ±2); average line at y 620 ±2 (160 px); Cline's bracket 208 px (y 780 to 572 ±2). Ratios 8.7 : 5.2 : 4 hold within 2 %.
2. Hoop rim at y 380 ±2: clearly above the average line and the crest; the man's head at y 540 ±2: above the 5.2 ft line (y 572) by 32 px, and he carries no number.
3. The comparisons stand on the sea-level datum, not on the island, so they compare heights above the sea as the narration does.
4. No chip overlaps a house, the crest bracket or the profile; C1 to C3 all show together once C3 lands (they stack, per the Picture line), and all three leave before C4 enters.
5. Nothing moves the sea level; no water rises (the surge belongs to A4).
6. Nothing labelled in x >= 1600, y >= 680 (bay water only).

## 5. Text and cues (a1-s6 then a1-s7 words.json; comp-local = S6 time − 2.84 inside S6)
- S6 2.84 ("Its"): plate on, finished; crest bracket draws up 2.84 to 3.60; C1 in at 3.00 ("average", the first word after the cut; 8.7 is not spoken here, the chip carries it). /* PLATE @2.84 */
- S6 4.62 ("4"): average line draws left to right 0.6 s; C2 in. /* FOUR @4.62 */
- S6 6.44 ("basketball"): ghost hoop draws (strokes from the datum up, 0.6 s), label in at 6.78 ("hoop."). /* HOOP @6.44 */
- S6 9.52 ("Klein's" = Cline's): Cline's house glyph turns amber (0.3 s, scale pulse 1 → 1.15 → 1).
- S6 11.52 ("5"): Cline's bracket draws up 11.52 to 12.32 ("feet."); C3 in at 11.82. /* 5.2 @11.52 */
- S6 13.02 ("That"): ghost man draws (0.6 s); label at 14.60 ("tall"). /* TALL MAN @14.60 */
- S6 15.00 to 15.40: C1 to C3, hoop, man and their labels out (chips `y:-24`, figures fade 0.4 s).
- S7 0.14 ("1899,"): source line swaps. 1.96 ("Galveston"): 14 buildings rise left to right, 0.04 s apart, scaleY 0 → 1 from their base, back.out. /* BUILD @1.96 */
- S7 2.60 ("world's"): C4 in. /* COTTON PORT @2.60 */
- S7 5.34 ("a few feet"): average line pulses (opacity 0.6 → 1 → 0.6, 0.8 s). /* FEW FEET @5.52 */
- Host: A1-S6 2.84 to A1-S7 6.673 (plus the S6/S7 gap from the mounts).

## Motion for the whole window
Plate waves (phase, whole host), camera push, HUD drift ±4 px; draws land every 1 to 3 s.

## Exit
A1-S8 opens on the timeline: C4 slides out `x:980` over the last 0.6 s and the root fades over the last 0.4 s.

## Footage under it
None: full-frame designed diagram. (No usable 1890s Strand or wharf photo, `_list.md` change 8.)
