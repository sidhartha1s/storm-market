# g-a6-usmap · DEEP (Opus 5.5, high) · a6-s3 0.00 to 20.54

Open numbers: N4 ("RISK CATEGORY III, IV", dropped from the ASCE chip), N5 (the highest tornado zone outline and which 22 states: no published figure in facts.md, so the zone layer is an empty slot and nothing on the map is filled), N6 ("IBC Section 423", "FEMA Recovery Advisory 1, Feb 2023": that source line is held).
Exemplar: `library/inhouse/master-map-us-canada.html` (Natural Earth 50m admin-1 states, public domain, with its own lon/lat projection). Copy its basemap and projection; drop Canada fill to a dimmer grey or leave it out.
Inset: the drawing from g-a6-saferoom (`<g id="sr-draw">`), copied, never redrawn.
Full-frame graphic, no footage beneath.

## 0. Claim
The engineering standard behind US building codes now plans for tornado winds, and the model building code requires storm shelters in new schools and emergency buildings in the worst tornado zone, which covers parts of 22 states.

## 1. Source
- R12, NIST web Impacts page: "Tornado hazard maps and tornado load provisions have been developed and adopted into the American Society of Civil Engineers ASCE 7-22 standard, which forms the design load basis for building codes in the U.S."
- R13, NIST web Impacts page: "tornado shelters are now required per the International Building Code (IBC) in new schools and emergency response facilities across parts of 22 states covering the most tornado-prone regions".
- R16, NIST web Impacts page: "Both codes added provisions for minimum shelter capacity and maximum travel distance to the shelters".
- Zone outline: none in facts.md (N5). The orchestrator supplies a traced outline from the published figure once a row exists; until then no state is filled, outlined or named.

## 2. Datum, scale, orientation
North up. Lower 48 only (Alaska and Hawaii are not drawn; the picture makes no claim about them). Fit the lower-48 box (lon -125 to -66, lat 24 to 50) into x 120 to 1240, centred on y 540; with the exemplar's projection that is about x 120 to 1240, y 231 to 849 (computed for an equirectangular fit at cos 37°; if the exemplar projects differently, keep the width 1120 and centre on y 540). Right column x 1300 to 1824 is the inset.

## 3. Geometry
- Basemap: state outlines Diagram grey 2 `#2a3644` 1.5 px, land Panel dark 2 `#0b1016`, ground the canvas radial gradient (tokens.md "Canvas"). Draws on at 0.00 (outline strokeDashoffset, 1.2 s).
- Camera: slow linear push 1.00 to 1.12 around (680, 540) over 0.00 to 19.94 (under 1.5x, so linear; about 6.5 px/s at the map edge keeps it moving).
- Zone slot: `<g id="usm-zone">`, empty. Its tween (fill Crimson `#8e2020` at 0.6, scale-in per state, stagger 0.04) is written and cued but targets nothing until N5 is released.
- Chip 1 (glass chip, row-value tier): "ASCE 7-22 · TORNADO-PRONE REGION", top-left, left 96, top 80. Exits 0.4 s before chip 2 enters.
- Chip 2 (glass chip, row-value tier): "22 STATES · NEW SCHOOLS", same top-left slot.
- Inset card (glass card, radius 28): x 1300 to 1824, y 180 to 520. Inside it, `sr-draw` cropped to x 110 to 1110, y 470 to 830 of its own frame and scaled 0.484 (so the room is about 194 px wide, people about 26 px tall). The drawing's own labels are not copied (they would shrink below 19 px). Two new marks, Amber 1 `#d8a13a`: a bracket over the people group, and a bracket over the dashed path from house to door.
- Inset labels (diagram label tier 22 px, label grey, each beside its bracket, inside the card): "MINIMUM SIZE" over the people bracket; "MAX WALKING DISTANCE" over the path bracket. These are the Picture line's chip "MINIMUM SIZE · MAX WALKING DISTANCE", split so each phrase names its mark.
- Source line: "ASCE 7-22 · NIST Impacts page", bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- Presenter corner x >= 1600, y >= 680: empty (inset ends at y 520, map at x 1240).
- Exit: the whole comp fades through (0.6 s) from 19.94, gone at 20.54, onto the footage under g-a6-cmt-mandatory.

## 4. Must be true in the picture
1. North is up and the lower-48 outline is the Natural Earth geometry, not hand-drawn.
2. No state is filled, outlined, coloured or named as part of the zone while N5 is open.
3. The inset is the g-a6-saferoom drawing (same room, door, path, people), not a new drawing.
4. "MINIMUM SIZE" sits beside the people, "MAX WALKING DISTANCE" beside the path; neither under a bracket or line.
5. Chip 1 and chip 2 are never on screen together; no "RISK CATEGORY" text anywhere.
6. Nothing in x >= 1600, y >= 680.

## 5. Panel text and cues (a6-s3.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Basemap draws, push starts | none | "As" @ 0.00 |
| Chip 1 + source line | ASCE 7-22 · TORNADO-PRONE REGION / ASCE 7-22 · NIST Impacts page | "engineering" @ 4.02 |
| Chip 1 pulse (scale 1 to 1.05 to 1) | none | "tornado" @ 7.26 |
| Inset card slides in from x +600 (0.7 s, power3.out) | none | "requires" @ 12.92 (words.json writes "cupboard" @ 12.64 for "code") |
| Bracket + label | MINIMUM SIZE | "schools" @ 14.36 |
| Bracket + label | MAX WALKING DISTANCE | "emergency" @ 15.00 |
| Inset slides out (x +600, autoAlpha 0, 0.6 s, power3.in); chip 1 exits | none | "worst" @ 16.26 |
| (zone slot, held N5) | none | "zone," @ 17.04, only once released |
| Chip 2 | 22 STATES · NEW SCHOOLS | "22" @ 18.78 |
| Fade-through exit | none | 19.94 to 20.54 ("What" @ 20.54 starts g-a6-cmt-mandatory) |

## 6 to 8
Template §6 to §8, COMPID `g-a6-usmap`. Template 7a item 6: the fit box and the inset crop/scale are computed by a script and stated in the receipt.
