# g-a5-greenbriar · A5-S6 · DEEP (Opus 5.5, high or above)

Open numbers: none. Open drawing fact: the building's wall material (facts.md CONFLICT line 278: Sec. 1.2 says wood-framed, Sec. 4.4.4 and Table 4-7 say unreinforced masonry). The drawing shows no wall material.
Two states in one comp. **Host start = a5-s6 10.20**, duration 17.88 s (wav 27.48 + 0.60 tail).
- 10.20 to 13.94: overlay, root transparent, over `media/candidates/a5/a5-s6_c3_nist-greenbriar-north-fig3-106.jpg` (NIST Fig 3-106, rubble and the surviving north-wing wall), mounted on a lower track for that span.
- 13.94 to the end: full-frame drawing, its ground (tokens.md canvas radial gradient) fades in over 0.5 s from "The"@13.94.

## 0. Claim
Ninety-five people were inside the Greenbriar and nineteen were lost. The plan was to move residents into the inner hallway and close the room doors; people in that hallway were buried in rubble; where in the building the nineteen were is not known.

## 1. Source
- C17: "The center of the tornado passed directly over the Greenbriar Nursing Home, and the one-story ... structure was completely demolished, causing 19 fatalities out of a total of 95 occupants" (Sec. 1.2).
- C19: "move residents to inner hallways and close all doors to residents' rooms (to avoid flying window glass)" (Sec. 1.2).
- C20: "According to media reports and CDC interviews, people located in this hallway became buried in rubble" (Sec. 4.4.4).
- C21: "It is unclear where the 19 fatalities were located within the Greenbriar" (Sec. 4.6.2.2).
- Footprint traced: NIST Fig 3-102, "Overview of the Greenbriar Nursing Home, shown in relation to the estimated center line of the tornado damage path" (printed p. 188). Trace the wing outline only; the aerial under it is not ours to show. If the figure is not extracted, use §3 and treat it as SCHEMATIC, NOT TO SCALE.

## 2. Datum, scale, orientation
Plan view, one storey, no compass on screen. Drawing area x 180 to 1440, y 220 to 860. No px-per-metre (schematic unless Fig 3-102 is traced, then state its scale in the receipt).

## 3. Geometry (schematic fallback)
- One long wing: outer wall rect x 180 to 1440, y 300 to 780, stroke 3 px `#93a3b2`, plain line, no brick or timber texture.
- Rooms: 7 along each long side, 180 px wide, 170 px deep (y 300 to 470 and y 610 to 780), walls 2 px `#4a5560`, each with a 40 px door on the hallway side drawn as a hinged leaf (line) standing open at 70 degrees.
- Inner hallway: band y 470 to 610, `#2a3644` at rest, lit `#d8a13a` at 0.55 on cue.
- Windows: short 4 px `#7fb2e5` marks on the outer walls, 2 per room.
- Rubble: a field of 60 to 80 small irregular polygons (`#4a5560`, `#2a3644`), seeded, filling the hallway band only.
- Chip `19 OF 95 LOST`: in the overlay state centred x 960, top 140; at 13.94 it slides to the top-left zone (left 96, top 96) and stays.
- Source chip under the chip in its fine line when it appears.
- Source line bottom-left. Nothing at x >= 1600, y >= 680.

## 4. Must be true in the picture
1. One storey: plan view only, no second floor, no stair, no basement.
2. No dot, figure or mark for the 19 anywhere in the building, at any time (C21: location unknown).
3. The hallway is the inner one: rooms on both sides of it, outer walls on the far side of every room.
4. Rubble lands only in the hallway band and only from "buried"@23.06; before it the hallway is clear.
5. "19 OF 95" never reads as a share of residents only (95 = all occupants, C17); no "residents" or "staff" split on screen (the 85 + 10 split is media accounts, C18).
6. Walls drawn as plain lines, no material (CONFLICT line 278).

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| chip `19 OF 95 LOST` (whole chip; the number lands on the spoken 19) | a5-s6 "nineteen"@12.38 |
| source line `NIST Sec. 1.2 · Sec. 4.4.4 · Sec. 4.6.2.2` | a5-s6 "Ninety"@10.38 |
| drawing ground in, walls draw on (strokeDashoffset 1.0 s) | a5-s6 "The"@13.94 |
| hallway lit | a5-s6 "inner"@15.42 |
| room doors swing closed (rotation on svgOrigin at each hinge, stagger 0.06 s) | a5-s6 "close"@16.24 |
| window marks flicker once (the glass the doors are closed against) | a5-s6 "class."@17.76 (spoken "glass") |
| rubble falls into the hallway (y from -40, stagger, 0.8 s) | a5-s6 "buried"@23.06 |
| source chip `media reports · CDC interviews · where the 19 were: not known (NIST)` | a5-s6 "buried"@23.06 |
| slow pull-out 1.06 -> 1.00 on the drawing (labels on the HUD layer, not riding it) | a5-s6 "Nobody"@24.60 to 27.48 |
| exit: fade-through to the next shot | 27.48 to 28.08 |
Motion between 17.8 and 23.0: rubble-free hallway glow breathes plus a slow push 1.00 -> 1.06 from 18.0 to 23.0, so no 4 s still.
Note: the chip shows "19" and the source chip "19" at once; neither is a 3-character digit string, so overlap_check dup-fact does not fire; the frame read decides whether it reads as one fact.

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
