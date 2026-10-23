# g-a5-condition-gray · A5-S2 · DEEP (Opus 5.5, high or above)

Open numbers: none. Full-frame drawn diagram, ground on from frame 0 (tokens.md canvas radial gradient). **Host start = a5-s2 0.00**, duration 23.36 s (wav 22.76 + 0.60 tail into A5-S3).

## 0. Claim
The hospital's plan moved patients out of their rooms into the hallways, and the head nurse's one siren was most likely the 5:38 round, which by her own count left five to seven minutes before the tornado hit.

## 1. Source
- C10: "under a procedure known as Condition Gray, when the head nurse verified that sirens were sounding in Joplin" (NIST Sec. 1.2).
- C11: "What she heard was likely the second round of sirens, activated at 5:38 p.m., since she only remembered hearing sirens one time" (NIST Sec. 4.4.2); 5 to 7 minutes before the tornado hit the hospital, her recollection (C11 fact line).
- Floor plan traced: NIST NCSTAR 3 Fig 3-127, "Typical floor plan of SJRMC's East and West Towers (patient rooms along perimeter and hallway toward the center)" (printed p. 216). Extract the figure from the PDF before drawing. If it is not extracted, draw the plan below and treat it as SCHEMATIC, NOT TO SCALE (the caption's room-on-perimeter, hallway-in-centre layout is the only claim).

## 2. Datum, scale, orientation
Plan view, north unspecified (no compass on screen). Plan rectangle 1200 x 520 px, left 200, top 300. No px-per-metre: schematic.

## 3. Geometry
- Outer wall: rect x 200 to 1400, y 300 to 820, stroke 3 px `#93a3b2`.
- Rooms: 8 along the top (y 300 to 470) and 8 along the bottom (y 650 to 820), each 150 px wide, walls 2 px `#4a5560`; each room has a door gap 40 px on its hallway side.
- Central hallway: band y 470 to 650 (180 px), fill `#2a3644` at rest.
- Beds: 6 bed icons (rounded rect 90 x 44 px, `#dfe7ee` at 0.85) start inside rooms 2, 4, 6 (top) and 3, 5, 7 (bottom), centred in their rooms; end in the hallway in one row at y 560, x = 300, 470, 640, 810, 980, 1150 (+-10 px).
- Clock: top-left zone, left 96, top 96, the A2 countdown clock's look (Courier New 700, as the A2 clock brief sets it).
- Label "Condition Gray": diagram label 26 to 30 px `#d8a13a` right of the hallway's west end at x 220, y 448 (just above the hallway, not over a wall line).
- Chip + its source chip: centred on x 960, top 860, the pair ending above y 1026 and clear of the bottom-left source line.
- Nothing at x >= 1600, y >= 680.

## 4. Must be true in the picture
1. Every room touches the outer wall; the hallway is in the middle (Fig 3-127). No room sits in the centre.
2. At the end of the move every bed is inside the hallway band (y 470 to 650), none in a room, none on a wall line.
3. The clock reads `5:38 PM`, never 5:11 (the head nurse heard the second round).
4. "5 TO 7 MINUTES" is shown with its source chip at the same time: it is her recollection, never presented as a measured time.
5. No tornado, debris or damage in this comp (that is A5-S3).
6. No count of patients or beds is implied: no number on the beds.

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| plan draws on (strokeDashoffset, 1.2 s) | a5-s2 "hospital"@1.54 |
| label `Condition Gray` | a5-s2 "Condition"@2.60 |
| hallway band brightens `#2a3644` -> `#5a768f` at 0.6 | a5-s2 "sirens"@5.82 |
| beds roll from rooms through the door gaps into the hallway (per-leg x/y tweens, stagger 0.15 s) | start a5-s2 "moved"@7.50, all parked by "hallways."@8.62 + 0.6 |
| clock `5:38 PM` | a5-s2 "538."@13.48 |
| chip `5 TO 7 MINUTES` | a5-s2 "five"@16.72 |
| source chip (fine line under the chip) `the head nurse's own recollection · before the tornado hit the hospital · NIST Sec. 4.4.2` | a5-s2 "minutes"@17.70 |
| source line `NIST Sec. 1.2 · Sec. 4.4.2` | a5-s2 "Condition"@2.60, stays to the end |
| camera push into the hallway's centre, 1.0 -> 1.25 (linear is fine under 1.5x); labels and chip fade to 0 before the push starts (HUD never rides a move) | a5-s2 "What"@20.20 to 22.76 |
Motion between 8.62 and 13.48: a continuous slow push 1.00 -> 1.04 over 0 to 20.2 plus a bed float y +-3 px, so no 4 s still.

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
