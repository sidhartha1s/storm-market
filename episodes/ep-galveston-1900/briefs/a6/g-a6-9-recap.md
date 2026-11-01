# g-a6-9-recap · A6-S6 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/stat-timeline.html` (tile row), wire layer of `g-intro-4-wire-map`, chip "MODERATE STORM" from `g-intro-9-warnings`; the 1875 and sky chips belong to A3 (comps not built yet: use the strings below; the A3 lane matches them).

## 0. Claim
In 1900 Galveston had a warning too, but it called the storm moderate; many houses stood above the 1875 high water; and the brick-dust sky Cline watched for never showed. Three reasons to stay, side by side.

## 1. Source
- Warning existed: TSHA storm warning Friday 7 Sept (edit_script.md I1-S4 rows).
- "Moderate": OSU Origins Friday midday warning, SECONDARY (I1-S4 rows; g-intro-9 §1): no quote marks.
- 1875: MWR p. 376, Evening Sun, "having built their houses after that event so that the first floor was above the level of danger then" (A3-S9 rows).
- Sky: MWR p. 372, "The brick-dust sky was not in evidence" (A3-S7 rows).
- Havana kept off the wire: sources-cuba.md §2, AOML "decreed that only its forecasts would be carried over the telegraph" (as g-intro-4).

## 2. Datum, scale, orientation
No measured axis. Starts on the g-intro-4 wire view (V-WIRE), which then shrinks into tile 1. Tiles: three, 520 x 420 px, top 300, left edges x 120, 700, 1280 (gaps 60 px); right edge 1800, bottom 720 (> 680: circle OFF all window).

## 3. Geometry (px)
- Ground: tokens.md radial gradient (designed full-frame card; each tile is a glass panel with a drawing, so no dark text-only card).
- Tile 1 (wire): the V-WIRE view scaled to fit the tile: Washington line lit `#7fb2e5`, Havana line dark (dashed `#5a768f` opacity 0.35, the base's "×"). Label under the drawing inside the tile: "MODERATE STORM" Arial Black 900 44 px `#f2f5f8`, sub "Washington, Friday midday" Arial 700 22 px `#93a3b2`.
- Tile 2 (1875): a house on piers (g-intro-6 glyph, 160 px) with its first floor above a painted tide line `#d8a13a` 3 px across the tile; label "1875 HIGH WATER" Arial Black 900 44 px.
- Tile 3 (sky): a sky swatch 440 x 220 px in plain grey-blue layers `#5a768f` to `#93a3b2` drifting; a dashed outline 120 x 60 px marked where a brick-red patch `#b5532f` would be, which never fills (stays outline only); label "NO BRICK-DUST SKY" Arial Black 900 44 px.
- Source line top-left, two lines: "Isaac Cline, Monthly Weather Review, September 1900 · Ohio State University, Origins".

## 4. Must be true in the picture
1. No quote marks on MODERATE STORM (only OSU's summary is sourced).
2. Tile 1 shows the Havana line dark the whole window; Washington's lit.
3. Tile 3's brick-red patch is never filled: the sky "never showed".
4. Tile 2's tide line sits BELOW the house's first floor.
5. Labels exactly as A3 and I1 used them (1875 HIGH WATER, NO BRICK-DUST SKY, MODERATE STORM); if A3 ships different strings, A3's win and this brief is updated.
6. Two type tiers by design (44 px labels, 22 px subs and source line): "NO BRICK-DUST SKY" at 52 px would overrun a 520 px tile. Declare `data-type-ok="three labelled drawings, one label size"` on the root (mg-quickref "Declared exemptions"); add no decorative text to reach a third tier.

## 5. Text and cues (a6-s6.words.json, 12.390 s; host 0.00 to 12.390)
Note: the words file reads "1902" at 1.30 where the locked text says "nineteen hundred" (ear check open, `_list.md`); cue on the word's time either way.
- 0.00: frame 0 = V-WIRE full frame (as g-a6-8's end, but with the Havana pin and its dark line on). Source line in at 0.20.
- 0.80 ("warning") /* WARNING @0.80 */: pulse on the Washington line; Havana "×" pulses red once at 1.30.
- 2.90 ("It called") : the wire view shrinks into tile 1 (2.90 to 3.50, power3.inOut); tile 1's glass frame lands.
- 3.68 ("moderate.") /* MODERATE @3.68 */: tile 1 label in; sub at 3.98.
- 4.68 ("Many") : tile 2 slides in (fromTo y 40, autoAlpha); house drawn.
- 6.52 ("high water") : tide line draws across 6.52 to 7.20.
- 7.26 ("1875,") /* 1875 @7.26 */: tile 2 label in.
- 8.90 ("and") : tile 3 slides in; grey layers drift.
- 9.24 ("brick") /* SKY @9.24 */: tile 3 label in; the dashed patch outline draws 9.64 ("sky") to 10.20.
- 11.62 ("never") : the dashed outline blinks off once and back (0.3 s), stays empty.
- Host end 12.390; A6-S7 (Paul full frame) follows on a cut.

## Motion for the whole window
Wire pulse repeats every 1.6 s in tile 1; sky layers drift 8 px/s in tile 3; tiles float ±4 px.

## Exit
Cut to Paul (P6): the root fades to 0 over the last 0.3 s.

## Footage under it
None: full-frame designed card.
