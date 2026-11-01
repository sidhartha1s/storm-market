# BRIEF · g-a4-walmart · "the wall came to rest on a set of cabinets" · plan + section · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A4, segments A4-S3 and A4-S4. Full-frame MG, own ground (tokens.md radial gradient).
One cutaway sits over it: the NIST Walmart wall photo (sourcing pick c2, `a4-s3_c2_nist-walmart-fig3-40-wall.jpg`,
599 x 399, so an inset or slow push, never full-frame sharp) from a4-s3 "area." 15.00 to a4-s4 "Look" 0.00, mounted
by the orchestrator on a higher track. The comp keeps drifting under it.
Exemplar: `references/editing-patterns/ep2-met-explainer.html` (labelled diagram that builds on the voice); official
`svg-stroke-trace` for the outline draw. `g-a4-homedepot` is built on this file after its full-size read.
Open numbers: the three Walmart victims' location (`_list.md` Open 1): not drawn. Store dimensions (Open 4): SCHEMATIC.

## 0. What this graphic claims
About 200 people were inside; staff sent 50 to 60 of them to the layaway area at the back, the store's refuge area. The
tornado collapsed the perimeter wall next to that area inward onto it, and the wall came to rest on a set of cabinets,
leaving a D-shaped pocket of safety. Three people were lost at the Walmart, and where in the store is uncertain.

## 1. SOURCE
- B9 "the approximately 200 occupants located inside the building during the storm" (NIST Sec. 4.6.2.1).
- B5 "congregate at the back of the building in the 'Site-to-Store' or layaway area, which served as the main refuge area" (Sec. 1.2).
- B6 "some protection for the 50 to 60 occupants located there ... the tornado collapsed the adjacent perimeter wall inward and onto this refuge area" (Sec. 1.2).
- B10 "the collapsed wall closest to the refuge area rested on a set of cabinets nearby, creating a D-shaped pocket of safety" (Sec. 4.6.2.1).
- B7 "Three people lost their lives at Walmart. It is uncertain exactly where inside the store these victims were located." (Sec. 1.2).
- B8 "The store did not have an underground location (or basement) or an indoor storm shelter" (Sec. 4.6.2.1).
- No published floor plan is used: NIST's Fig. 4-12 is a GeoEye aerial "Used with permission". The plan is a schematic
  rectangle; front at the bottom, back at the top; no compass is claimed.

## 2. DATUM, SCALE, ORIENTATION
- SCHEMATIC · NOT TO SCALE (printed, small tier, whenever the plan or the section is on).
- PLAN (A4-S3, full size): store rectangle x 260 to 1260, y 200 to 800. Back wall = top edge y 200, label "BACK" centred
  above it at y 170; front wall = bottom edge, label "FRONT" below it at y 850. Rail for text: x 1320 to 1824, y 150 to 640.
- PLAN (A4-S4, reduced): the same plan scaled 0.55 about (260, 200), then moved so it sits at x 96 to 646, y 300 to 630.
  The rescale happens while the photo covers the comp, so A4-S4 opens two-pane.
- SECTION A-A (A4-S4): floor line y 600 from x 760 to 1560. Store interior is LEFT ("STORE INTERIOR" at (780, 640)),
  outside is RIGHT ("OUTSIDE" at (1530, 640)). The section line A-A is drawn across the reduced plan through the refuge band.

## 3. GEOMETRY
PLAN
- Outline: 4 px stroke `#dfe7ee`, drawn on (dash length `ceil(len)+1`).
- Refuge band: x 700 to 1060, y 200 to 300, touching the back wall; fill amber `#d8a13a` at 0.35 once lit; label
  "SITE-TO-STORE · LAYAWAY" (diagram-label tier) inside the plan just below the band at y 330, never on a dot.
- Dots: exactly 200, 8 px, `#dfe7ee` at 0.85, positions from a seeded PRNG inside the plan, 20 px clear of the walls
  and of the band. On the cue, 55 of them (the midpoint of 50 to 60, B6) move into the band on per-dot `x`/`y` tweens
  with a stagger; the other 145 keep a ±3 px seeded float the whole time.
- Wall falling in (plan): the top-edge segment x 700 to 1060 becomes a slab rectangle 360 x 100 anchored at y 200,
  `scaleY 0 → 1`, `transformOrigin: "top"`, crimson `#8e2020` at 0.7, so the 55 band dots stay visible beneath it.
SECTION (A4-S4)
- Cabinets: a box x 1100 to 1200, y 490 to 600, stroke `#93a3b2`, label "CABINETS" left of it at (960, 470).
- Wall slab: a 360 x 14 px bar, crimson `#8e2020`, pivot at its base (1500, 600) (`svgOrigin: "1500 600"`). Start
  vertical (top at (1500, 240)); at rest it lies 17.8° above the floor, so its free end sits on the cabinet top at
  x 1156.4, y 490 (contact point computed by script: 1500 − √(360² − 110²)). Fall ease power3.in, then a 3 px settle.
- Pocket: the space between the cabinet's right side (x 1200), the floor (y 600) and the underside of the slab; fill amber
  `#d8a13a` at 0.45, a soft glow pulsing (finite repeats) through the end of the host.
- Rail below the section (x 760 to 1560): chip "A D-SHAPED POCKET" (mid tier, 40 px Arial Black 900) at y 720;
  "3 LOST" (big tier, 72 px Arial Black 900, `#e74c3c`) at y 800 with three 16 px red dots inside the chip, right of the
  text; source chip (small tier) "location uncertain · NIST Sec. 1.2" at y 880.
RAIL (A4-S3)
- Eyebrow "WALMART · RANGE LINE ROAD" (22 px, tokens.md eyebrow) at y 170; chip rows (40 px Arial Black 900 `#f2f5f8`):
  "ABOUT 200 INSIDE" at y 260, "50 TO 60 AT THE BACK" at y 340. Rows enter `fromTo(autoAlpha 0, y 24 → 0, 0.4)`.
- Source line bottom-left (x 96, baseline 1026): "NIST Sec. 1.2 · Sec. 4.6.2.1" for both segments.

## 4. MUST BE TRUE IN THE PICTURE
1. The plan shows exactly 200 dots before the move and 55 inside the band after it (count them by script on the built DOM).
2. The refuge band touches the BACK wall, and the BACK label is on that side.
3. The fallen slab (plan) covers the band and lies inside the store, inward of the back wall line.
4. Section: the slab pivots on the floor at the wall base, ends resting on the cabinet top (x 1156 ± 10, y 490 ± 10), and
   the lit pocket lies on the STORE INTERIOR side of the wall, between cabinets, floor and slab.
5. No marker for the three lost on the plan or in the section; the three red dots exist only inside the "3 LOST" chip.
6. No basement, stair or below-ground line anywhere (B8).
7. "SCHEMATIC · NOT TO SCALE" is visible whenever the plan or the section is on.
8. Nothing in the presenter corner (x ≥ 1600, y ≥ 680).

## 5. PANEL TEXT (exact) and CUES
Text: "WALMART · RANGE LINE ROAD" · "ABOUT 200 INSIDE" · "50 TO 60 AT THE BACK" · "SITE-TO-STORE · LAYAWAY" · "BACK" ·
"FRONT" · "SCHEMATIC · NOT TO SCALE" · "SECTION A–A" · "STORE INTERIOR" · "OUTSIDE" · "CABINETS" · "A D-SHAPED POCKET" ·
"3 LOST" · "location uncertain · NIST Sec. 1.2" · "NIST Sec. 1.2 · Sec. 4.6.2.1".
Cues (`_list.md` "Cue notation"):
- frame 0: ground on, plan outline starting to draw. Outline draw a4-s3 "I" 0.00 → "stores," 1.96.
- eyebrow a4-s3 "Walmart" 3.12; BACK and FRONT labels + SCHEMATIC line 3.42.
- 200 dots in (stagger over 0.8 s) + row "ABOUT 200 INSIDE" a4-s3 "200" 5.74.
- 55 dots move into the band a4-s3 "sent" 7.66 → 9.40; row "50 TO 60 AT THE BACK" a4-s3 "50" 7.94.
- band lights + "SITE-TO-STORE · LAYAWAY" a4-s3 "layway" 9.82.
- slab falls in a4-s3 "pushed" 12.62 → "in," 13.80; it settles a4-s3 "onto" 14.58.
- photo cutaway covers a4-s3 "area." 15.00 → a4-s4 "Look" 0.00 (orchestrator's mount). Under it: rail rows out, plan
  rescales to the two-pane layout, dots keep floating.
- section line A-A draws on the reduced plan a4-s4 "Look" 0.00; section floor + wall (vertical) + cabinets build a4-s4 "where" 0.86.
- slab falls a4-s4 "came" 2.60 → lands a4-s4 "rest" 2.90; "CABINETS" label a4-s4 "cabinets," 3.80.
- pocket lights a4-s4 "pocket" 5.12; chip "A D-SHAPED POCKET" a4-s4 "D." 6.74.
- chip "3 LOST" a4-s4 "Three" 7.88; source chip a4-s4 "Exactly" 10.04.
- hold to the end with the pocket glow and a slow camera drift (scale 1.00 → 1.02 over the hold); nothing still for 4 s.
- exit: fade-through to black over the last 0.6 s of the host, which ends at a4-s4 "Depot?" 16.68 + 1.0 s.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-walmart`. Comp-specific: the cutaway window is a
higher-track photo, so the frame read at a4-s4 0.00 + 0.1 s (first uncovered frame) must show the two-pane layout settled.
