# BRIEF · g-a4-homedepot · "It depended on where you were standing." · plan · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A4, segment A4-S5. Full-frame MG, own ground.
Base: `g-a4-walmart` (same schematic-plan family). Copy it after its full-size read; keep its plan rectangle, rail,
labels, colours and SCHEMATIC line, and replace the store content below. Rail rows: `library/inhouse/stat-panel.html`.
Open numbers: store dimensions and the lumber entrance's position (`_list.md` Open 4): SCHEMATIC. No marker for the
eight lost (see §4.5).

## 0. What this graphic claims
Where you stood decided it. About 35 people sheltered in the training room at the back, and the concrete wall panels
next to that room fell outward, away from them. Eight people were lost at the Home Depot; store management said they
had just come in through the lumber entrance and were walking parallel to the front wall when it collapsed on them.

## 1. SOURCE
- B11 "approximately 35 of the building's occupants took refuge in the training room located at the back of the store ... the concrete wall panels adjacent to this refuge area collapsed outward, away from these occupants." NIST Sec. 1.2.
- B12 "A total of eight people lost their lives at the Home Depot. Store management reported that these individuals had entered the store through the lumber entrance just before the storm hit and were walking parallel to the store's front wall, which collapsed on them." Sec. 1.2.
- B14 "Death certificates ... a total of eight fatalities ... interviews with Home Depot survivors reflected that seven deaths occurred inside the structure." Sec. 4.6.2.1. Per the facts.md CONFLICT note: 8 on screen, with its base on the source line.
- No published plan is traced (NIST's aerials are "Used with permission"). Schematic: back at the top, front at the bottom, no compass.

## 2. DATUM, SCALE, ORIENTATION
- As `g-a4-walmart` §2 PLAN (A4-S3, full size): rectangle x 260 to 1260, y 200 to 800; "BACK" above at y 170, "FRONT"
  below at y 850; rail x 1320 to 1824, y 150 to 640; "SCHEMATIC · NOT TO SCALE" on whenever the plan is on.
- Outside the store: above y 200 (back) and below y 800 (front).

## 3. GEOMETRY
- Training room: box x 300 to 540, y 200 to 330, against the back wall; label "TRAINING ROOM" (diagram-label tier)
  inside the plan just below it at y 360. Fill amber `#d8a13a` at 0.35 once lit.
- 35 dots (8 px `#dfe7ee`, seeded positions) inside the training room, 12 px clear of its walls, with a ±3 px float.
- Panels in plan, same device as `g-a4-walmart`'s slab: a standing panel is its wall line; a fallen panel is a crimson
  `#8e2020` rectangle (0.7) the panel's schematic height (80 px) long, lying on the side it fell to, grown by
  `scaleY 0 → 1` from the wall line.
- Back panels by the training room: 4 panels, each 60 px wide, x 300 to 540. They fall OUTWARD: each rectangle spans
  y 120 to 200 (`transformOrigin: "bottom"`), outside the store, never over the room.
- Front wall: 13 panels, 60 px wide with 4 px gaps, from x 300 (13 × 64 − 4 = 828 px, so x 300 to 1128, computed by
  script). On the cue they fall INWARD: each rectangle spans y 720 to 800 (`transformOrigin: "bottom"`), over the path.
- Lumber entrance: a 60 px gap marker at the front wall's right end, x 1160 to 1220, label "LUMBER ENTRANCE" below the
  front wall at y 880 (schematic place: no row puts the entrance on a side, §4.4).
- Walking path: an amber dashed arrow from the entrance gap running left, parallel to the front wall and 40 px inside
  it, y 760, from x 1160 to x 420; it draws by `strokeDashoffset`.
- Rail: eyebrow "HOME DEPOT" (22 px) at y 170; rows (36 px Arial Black 900 `#f2f5f8`, max width 504, two lines allowed):
  "ABOUT 35 IN THE TRAINING ROOM" at y 250; "8 LOST" (big tier, 72 px, `#e74c3c`) at y 420.
- Source line bottom-left (x 96, baseline 1026; two lines allowed, x 96 to 1500): "8 per death certificates · 7 inside
  per survivors · lumber entrance and front wall per store management · NIST Sec. 4.6.2.1 · Sec. 1.2".

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 35 dots, all inside the training room, and the room touches the BACK wall.
2. The training-room panels end OUTSIDE the store (above y 200), away from the 35 dots; none lands on the room.
3. The front-wall panels end INSIDE the store, over the walking path.
4. The lumber entrance and the path are drawn as schematic; the path runs parallel to the front wall, inside it.
5. No markers or figures for the eight lost: "8 LOST" lives on the rail only (B14's 8 against 7 is not drawn as people).
6. No basement or below-ground element.
7. Nothing in the presenter corner (x ≥ 1600, y ≥ 680).

## 5. PANEL TEXT (exact) and CUES
Text: "HOME DEPOT" · "TRAINING ROOM" · "BACK" · "FRONT" · "SCHEMATIC · NOT TO SCALE" · "LUMBER ENTRANCE" ·
"ABOUT 35 IN THE TRAINING ROOM" · "8 LOST" · the source line above.
Cues (`_list.md` "Cue notation"):
- frame 0: ground on, plan outline drawing a4-s5 "About" 4.56 → 5.30 (the cut from the photo lands on an opening state).
- 35 dots in a4-s5 "35" 4.72; eyebrow + BACK / FRONT / SCHEMATIC 5.06.
- training room lights + label a4-s5 "training" 6.08; row "ABOUT 35 IN THE TRAINING ROOM" a4-s5 "room" 6.32.
- back panels fall outward a4-s5 "fell" 9.62 → "outward," 9.92 + 0.6 s; room glow pulses on "away" 10.58.
- training room dims to 0.5, rest of the floor brightens a4-s5 "Out" 12.06; "8 LOST" a4-s5 "eight" 13.44.
- source line a4-s5 "The" 15.04.
- LUMBER ENTRANCE marker a4-s5 "lumber" 17.30; path arrow draws a4-s5 "walking" 18.54 → "wall" 19.62.
- front-wall panels fall inward a4-s5 "came" 20.28 → 20.90.
- hold with the floats; fade-through over the last 0.6 s; host ends a4-s5 "The" 21.80 (the site clip takes over).

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-homedepot`. Comp-specific: copy `g-a4-walmart`'s
file only after the orchestrator's full-size read of it; re-prefix every id `hd-`.
