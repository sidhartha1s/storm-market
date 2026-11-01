# g-a6-6-surge · A6-S4 7.06 to end · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Base: `g-a6-3-wall` (plate, datum y 900, 36 px/ft both ways, wall path, colours): copy it after it passed its full-size frame read. Exemplar for rising water: `episodes/ep6-katrina-2005/compositions/g-surge-ms.html`.

## 0. Claim
In 1915 the surge reached 16.2 ft and waves crested at 21 ft against the wall; a four-masted schooner was thrown over it and broke up on top; the wall itself came out with two small chips.

## 1. Source
- NWS Houston/Galveston 1910s page (sources-a6.md §4): "storm surge reached 16.2' with wave crests of 21'"; "The seawall's only damage was two small chips near 39th street where the four-masted schooner 'Crockett' was blown over the wall"; "the schooner was pounded to pieces on top of the wall"; "first real test of the Galveston seawall".
- Wall numbers: g-a6-3 §1.
- The NWS page gives no datum for 16.2 and 21 ft: they are drawn on the same mean-low-tide axis as the wall (the closest reading). Receipt says so; no on-screen caveat beyond the source line's "heights as reported".

## 2. Datum, scale, orientation
Exactly g-a6-3: Gulf left, city right, datum (mean low tide) y 900, 36 px per ft. Heights: 16.2 ft y 316.8 · 17 ft (wall top) y 288 · 21 ft y 144.

## 3. Geometry (px)
- Plate, beach, wall, land behind: g-a6-3 §3 unchanged. The 1900 island line, brackets and dimension labels of g-a6-3 are NOT on (frame 0 = the bare wall).
- Surge body: the sea fill left of the wall rises from its calm surface (y 900) to y 316.8, its right edge clipped by the curved face (the water meets the face, never crosses the wall). Surface line `#5a768f` 3 px with a sine wave (amplitude 10 px once risen).
- Wave crests: three crest shapes `#c8d3e0` at opacity 0.85 that travel right on the surge surface and break on the face; at the top of each break a spray arc reaches y 144 (21 ft) and falls over the wall top onto the land side (spray particles, 6 to 10 px dots, fall 300 px and fade).
- Surge level line: dashed `#7fb2e5` 2 px at y 316.8 from x 96 to 1156, with chip "SURGE 16.2 FT" (glass) left edge x 120, top 180.
- Wave-crest line: dashed `#f2f5f8` 2 px at y 144 from x 600 to 1156, with chip "WAVES 21 FT" (glass) left edge x 1420, top 110 (right of the wall top, above the spray, which falls x 1340 to 1600 below y 288). No chip sits on the crest line or the spray path; the builder checks frames at every break.
- Schooner: no photo on disk. A small schematic four-masted silhouette (`#4a5560`, 200 x 120 px, NOT to scale, the only out-of-scale element) rides a crest, is thrown onto the wall top at (1246, 288), tilts and breaks into 4 pieces that slide off the land side. No name label (the narration never says "Crockett"). Beside it, the note "not to scale" Arial 700 19 px `#93a3b2` near the silhouette while it is on screen.
- Chips on the wall: two 14 x 10 px notches cut into the wall's top edge at x 1190 and x 1300 (dark `#04070c`), each ringed by a 30 px `#d8a13a` circle 2 px at the cue. Chip "2 SMALL CHIPS" (glass) left edge x 1420, top 380.
- Source line top-left: "National Weather Service Houston/Galveston · Rosenberg Library", second line "Heights as reported, above mean low tide".

## 4. Must be true in the picture
1. Surge surface at y 316.8 ±3: 29 px (0.8 ft) BELOW the wall top at y 288. The calm surge never tops the wall; only waves and spray go over.
2. Wave/spray peak at y 144 ±5: 144 px (4 ft) above the wall top. Ratio (21 − 17) / 17 shown true at 36 px/ft.
3. The wall shape is pixel-identical to g-a6-3 (same path), and stays intact except two tiny notches; nothing else on the wall breaks.
4. The schooner silhouette is the only element not to scale and carries "not to scale" while visible.
5. No city flooding drawn here (the flood belongs to S5, g-a6-7).
6. Corner x >= 1600, y >= 680: land fill only; circle may stay if spray never enters the corner (spray x max 1600).

## 5. Text and cues (a6-s4.words.json, 19.403 s; host starts at "The" 7.06)
Comp-local = word time − 7.06. Frame 0: bare wall, calm sea, waves small.
- 7.06: source line in.
- 7.20 ("surge") /* SURGE @7.20 */: sea rises 7.20 to 8.90 (power2.inOut) to y 316.8; surge line draws as it lands; chip "SURGE 16.2 FT" in at 7.76 ("16").
- 9.84 ("waves") /* WAVES 21 @10.74 */: first crest travels and breaks on the face 9.84 to 10.74; spray peaks at y 144 exactly at 10.74 ("21"); crest line draws; chip "WAVES 21 FT" in at 10.74. Further breaks every 2.4 s to the host end (finite repeats).
- 12.08 ("A") /* SCHOONER @12.66 */: schooner rides in on a crest 12.08 to 13.28; thrown onto the wall top 13.28 to 13.90 ("thrown over" 13.28/13.52); "not to scale" note with it; SURGE chip out at 12.08, WAVES chip out at 13.20.
- 14.58 ("pounded") to 15.96 ("it."): schooner tilts and breaks, pieces slide off the land side by 16.30; note out with it.
- 16.64 ("wall") : wall edge brightens (stroke `#f2f5f8`, 0.4 s).
- 18.10 ("two") /* 2 CHIPS @18.10 */: the two notches ring in turn (18.10, 18.44); chip "2 SMALL CHIPS" in at 18.44 ("small").
- Host end: 19.403 + land time.

## Motion for the whole window
Surge surface sine phase and wave breaks run the whole host; the plate pushes 1.00 to 1.03 linear.

## Exit
Cut to g-a6-7 at A6-S5: root fades to 0 over the last 0.4 s.

## Footage under it
None: full-frame diagram. If the Crockett-on-the-wall photograph is found and cleared (Rosenberg Library), the orchestrator cuts to it 12.08 to 16.40 and this comp holds the waves under the cut; the silhouette is then dropped.
