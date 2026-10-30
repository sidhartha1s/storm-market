# g-a5-16-island-return · A5-S10 9.94 to end · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Base: `compositions/g-intro-6-island.html` and its brief `briefs/intro/g-intro-6-island.md` (copy datum, scale, profile, water and bracket exactly; change only what §3 lists). Reference: `references/mg-brief-example-g-slope.md`.

## 0. Claim
After the storm the island had not changed: a sand island under nine feet at its highest point (8.7 ft), with a ruined city to rebuild on the same low ground. The chapter ends on the question of what to do with that ground.

## 1. Source
- Highest point 8.7 ft: NPS "the highest elevation on Galveston Island was 8.7 feet" (factcheck-A.md T1-S1; fact-check a5-r1 row 45).
- "A whole city to put back on it": writer's line, no number (row 46). No count of destroyed buildings appears on screen (none is in this act's rows).
- The A6 answers (seawall, grade raising) are NOT shown or hinted (Rows: "A6 answers it ... not narrated here").

## 2. Datum, scale, orientation
Identical to g-intro-6: north-south cross-section looking west, Gulf LEFT, bay RIGHT; sea level y 780; 40 px per ft; crest y 432 (8.7 ft); 4 ft shoulders y 620; horizontal SCHEMATIC, note "Vertical scale exaggerated" at left 96, top 1000.

## 3. Geometry (px), changes from g-intro-6 only
- Houses: the same 22 positions on the profile, now wreckage glyphs: each house glyph replaced by 3 to 4 broken planks (rects 22 to 30 x 4 px, `#4a5560`, rotated -35 to +35 deg, seeded so the pattern is fixed), sitting on the profile within 2 px. Grey only: no red, no bodies, nothing that reads as people.
- Water: sea back at datum, calm (Gulf amplitude 4 px, bay 2 px). A faint wet line: the island top stroke `#5a768f` instead of `#93a3b2` (the water has been over it); no water drawn on the island.
- Bracket: as g-intro-6 (x 960, y 780 -> 432, `#d8a13a` dashed).
- Chip C1 "HIGHEST POINT ABOUT 8.7 FT", same spot as intro C2 (left 1000, top 290).
- Chip C2 "A CITY TO PUT BACK", centred x 960, top 150 (glass). Text drawn from the narration ("a whole city to put back on it").
- No question text on screen: the spoken question carries itself.
- Source line top-left: "NOAA AOML, 2015 · National Park Service".

## 4. Must be true in the picture
1. Crest y 432 ±4, sea level y 780 ±2, bracket exactly 348 px (8.7 x 40); shoulders y 620 ±4: identical to g-intro-6, so the viewer recognises it.
2. The sea is at sea level and never above the island in any frame (the surge is over; a raised sea would claim a height).
3. Wreckage is grey, abstract and on the ground line; no human figures.
4. Nothing hints at a seawall or raised grade (A6's reveal).
5. Corner x >= 1600, y >= 680 holds only bay water: the circle may stay on; no label there.
6. C1 and C2 never overlap the bracket, the crest stroke or each other.

## 5. Text and cues (a5-s10.words.json; host starts at "And" 9.94)
Comp-local = word time − 9.94.
- 9.94 ("And" 9.94): frame 0 = sea, datum, profile, wreckage already on (the cut lands on a finished picture); calm waves moving; source line in at 10.10.
- 10.16 ("island" 10.16) /* ISLAND @10.16 */: slow pull-out begins, scale 1.06 -> 1.00 over 10.16 to 13.06 (`ease:none`).
- 12.84 ("sand" 12.84): profile fill brightens slightly toward sand `#c8b98a` at 0.25 (one tween, 0.6 s), back to base by 13.88.
- 13.88 ("under" 13.88) /* NINE FEET @14.08 */: bracket draws up 13.88 to 15.18 (power2.out); crest stroke turns `#d8a13a` on arrival.
- 15.00 ("highest" 15.00): C1 in.
- 16.02 ("with" 16.02): C1 dims to 0.6. 16.46 ("city" 16.46) /* CITY @16.46 */: wreckage pulses once (opacity 0.7 -> 1, stagger 0.02 left to right); C2 in at 16.88 ("put").
- 18.00 ("So" 18.00): C1 and C2 slide out right by 18.60; the picture holds on the island alone for the question; 19.14 ("Gulf" 19.14): the Gulf surface brightens `#7fb2e5` at 0.5 for 0.8 s (only the water at its own level).
- Host: 9.94 to 20.16 + 1.0 s land time, then the chapter blackout (DESIGN.md).

## Motion for the whole window
Waves continuous (`ease:none`, one tween over the host); the pull-out 10.16 to 13.06, then a slow push 1.00 to 1.03 to the end so nothing idles.

## Exit
Fade to black over the last 0.6 s into the chapter blackout (A5 -> A6).

## Footage under it
None: full-frame diagram (root background tokens radial gradient).
