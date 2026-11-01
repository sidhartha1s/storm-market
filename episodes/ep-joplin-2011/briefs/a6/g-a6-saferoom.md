# g-a6-saferoom · DEEP (Opus 5.5, high) · a6-s2 5.92 to a6-s3 0.00

Open numbers: N1 ("14"), N2 ("250 MPH"), N3 ("Jul 30, 2024"). Their two chips and the date are left out; the slots are fixed in §3 so a release is a text drop-in plus a frame read.
Base: new in a6. g-a6-usmap reuses this drawing as its inset, so build this one first and keep the drawing in one `<g id="sr-draw">` that can be copied whole.
Exemplar: `references/editing-patterns/ep2-met-explainer.html` (a diagram that builds while the voice explains).
Full-frame graphic, no footage beneath. Label on screen: SCHEMATIC, NOT TO SCALE.

## 0. Claim
Joplin's schools have built storm safe rooms, and people who live nearby with nowhere else to go may use them.

## 1. Source
No facts.md row covers the safe rooms: the script cites the FEMA case study "Schools in Joplin, Missouri stand up to tornadoes by building safe rooms" (edit_script A6-S2 Rows) and says no FEMA photograph or figure exists on that page. So there is no published figure to trace: the drawing is a generic schematic of a reinforced room inside a school, and it claims nothing about size, count or rating. Context rows: H3 (NIST Finding 20: "There were no community shelters or safe rooms in the City of Joplin or Jasper County at the time of the May 22, 2011, Joplin tornado") is why the room matters; it is not drawn here.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE. Datum: ground line y 820, x 160 to 1560. Side view (a section through the school), wind from the right. No px-per-metre: no dimension is shown or implied.

## 3. Geometry
- Ground: line y 820, x 160 to 1560, Diagram grey 1 `#4a5560`, 3 px.
- School shell (faint): outline x 260 to 1500, y 360 to 820, flat roof at y 360, Diagram grey 2 `#2a3644`, 3 px. Not shown failing (no claim about the school building).
- Safe room: outer box x 700 to 1100, y 540 to 820; walls 18 px, roof slab 24 px; stroke and slab Headline white `#f2f5f8`, interior Panel dark `#15202b`. Door: Amber 1 `#d8a13a` panel in the left wall, y 700 to 820.
- People: 6 simple figures (circle head + rounded body, Body light `#dfe7ee`), 54 px tall, baseline y 812, evenly spaced x 750 to 1050.
- Wind: 4 arrows, Cold blue 2 `#7fb2e5`, 5 px, from x 1560 to an arrowhead tip at x 1110 (10 px off the right wall), at y 580, 640, 700, 760. Motion: dashes travel right to left continuously for the whole window (this is the comp's continuous motion).
- Neighbour: house glyph (outline, Body light) x 110 to 220, y 730 to 820; dashed path (Body light, 4 px, dash 14/10) from (230, 800) to the door at (690, 800).
- Labels (diagram label tier, label grey `#93a3b2`, each next to its thing, none under a line or arrow): "SCHOOL" left-aligned at (290, 400) inside the shell; "SAFE ROOM" centred at (900, 516) above the roof slab; "SCHEMATIC, NOT TO SCALE" small tier, right edge x 1824, baseline y 80.
- Chip (glass chip, row-value tier, Body light): "NEIGHBORS WITH NOWHERE ELSE MAY USE THEM · FEMA", centred x 960, centre y 930 (clear of the ground line and of the source line).
- Source line: "FEMA case study", bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- Held slots (empty until N1/N2 are released): slot A top-left, left 96, top 80 (for "14 SAFE ROOMS"); slot B, left-aligned at (1150, 520), above the arrowheads (for "250 MPH").
- Presenter corner x >= 1600, y >= 680: nothing there (house is at left, arrows end at x 1560).
- Exit: the drawing holds to the cut; the comp ends on a fade-through (0.4 s) into g-a6-usmap at a6-s3 0.00. No single element vanishes mid-frame.

## 4. Must be true in the picture
1. The safe room sits inside the school shell, on the ground line, and its walls read clearly thicker than the shell (18 px vs 3 px).
2. Wind arrows stop at the safe room's wall; none enters the room.
3. The neighbour's path runs from outside the school to the safe-room door.
4. No size, count, rating or date appears anywhere (N1 to N3 held).
5. "SCHEMATIC, NOT TO SCALE" is on screen whenever the room is.
6. No label under an arrow, path or wall at any frame, including the first 0.5 s of each entrance.

## 5. Panel text and cues (a6-s2.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Ground and shell draw on (strokeDashoffset, 0.8 s); "SCHEMATIC, NOT TO SCALE" | SCHEMATIC, NOT TO SCALE | "Since" @ 5.92 |
| School label | SCHOOL | "School" @ 7.64 |
| Safe room rises (scaleY 0 to 1 from the ground, transformOrigin bottom, 0.5 s) | none | "built" @ 8.40 |
| Safe room label | SAFE ROOM | "safe" @ 9.16 |
| People fade up, stagger 0.08 | none | "rooms," @ 9.48 |
| Wind arrows start | none | "winds" @ 10.66 |
| (slot A, held N1) | 14 SAFE ROOMS | "14" @ 8.58, only once released |
| (slot B, held N2) | 250 MPH | "250" @ 11.28, only once released |
| House draws | none | "live" @ 14.68 |
| Path draws to the door | none | "nowhere" @ 15.50 |
| Chip | NEIGHBORS WITH NOWHERE ELSE MAY USE THEM · FEMA | "you" @ 16.62 |
| Source line | FEMA case study | "Since" @ 5.92 |
| Fade-through | none | ends a6-s3 "As" @ 0.00 |
Between 10.66 and 14.68 the arrows keep travelling (no idle).

## 6 to 8
Template §6 to §8, COMPID `g-a6-saferoom`. Send the drawing for a full-size read before g-a6-usmap copies it.
