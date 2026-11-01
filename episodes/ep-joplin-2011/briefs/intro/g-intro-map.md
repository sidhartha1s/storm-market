# BRIEF · g-intro-map · "the sirens went off twice; nobody was below ground" · DEEP (Opus 5.5, high) · MASTER MAP BASE

Episode ep-joplin-2011, segments T1-S2 and T1-S3. Full-frame MG on the channel ground. One host from t1-s2 0.00 to the t1-s3 wav end 5.24
(comp-local t1-s3 times = `nx-t1-s3` data-start − host data-start + word time). It comes in on a cut from `g-intro-161`'s photo and
cuts to CLIP 1 (i1-s1).
**This comp holds the episode's MASTER MAP base**: everything geographic sits inside `<!--BASEMAP:g-master-map--> … <!--/BASEMAP-->`
with ids `g-master-map-*`, the way `episodes/ep-enderlin-2025/compositions/g-master-map.html` does. Every later map comp (intro, a1 to a6)
copies that block verbatim and toggles its layers. Build the full base (every layer, most hidden in this comp), then send one
still with ALL layers on for a full-size read before any copy is made (template 7a "A family built on one base"; delete the still page before the gates).
Exemplars: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (block, layers, draw-in), `references/editing-patterns/ep3-map-route-fit.html` (fitting a route to real landmarks).
Open: `_list.md` Open 2 (siren positions, NIST Fig. 4-2) and Open 4 (location positions). Build every other layer; leave a blocked layer empty with its id and report it.

## 0. What this graphic claims
The sirens did not fail: they sounded twice that evening, at 5:11 and 5:38 p.m., three minutes each (E6, E14, S27). Then the
question: nobody the investigators placed was below ground (the empty line; paid in I1). The map is the case board for the whole episode.

## 1. SOURCE
- E6 "511 pm CDT - Initial 3 minute siren alert sounded for Jasper County and Joplin". NWS Assessment Table 1.
- E14 "538 pm CDT - Second 3 minute siren alert sounded for Jasper County and Joplin." NWS Assessment Table 1.
- S27 "the rare occurrence of two siren activations (at 5:11 p.m. and 5:38 p.m.) during the same evening." NIST Sec. 4.7.3.
- Base geometry (no facts.md numbers; traced sources, credited in the description):
  - City outline and streets: US Census TIGER/Line 2010, place "Joplin city, Missouri" and its roads (public domain, 2011-era).
  - Damage path: NWS Assessment Figure 1 "Storm Track and Intensities", `media/candidates/intro/i1-s9_c1_nws-assessment-p7-60-survivors.png`,
    georeferenced on its printed roads (I-44, US-71, MO-43, MO-66, MO-249). Checked against W3/W4 (6 miles in the city), W5/W6/W7 (up to 1 mile wide), W6 (west to east).
  - 25 siren positions: NIST NCSTAR 3 Fig. 4-2 (Open 2); count S2 "the 25-siren outdoor warning system". NIST Finding 31.
  - Table 4-3 location markers: `research/map-positions.md` (Open 4).

## 2. DATUM, SCALE, ORIENTATION
- North up. Equirectangular, x scaled by cos(37.08°). One px-per-mile `s` for the whole base, chosen so the city outline's bounding
  box fits inside x 200 to 1500, y 200 to 770, centred in that box. Compute `s`, the centroid and the ring radius by script from
  the TIGER outline and state all three in the receipt; every later map brief uses them.
- The box keeps the chip zone (y 96 to 166) and the presenter corner (x ≥ 1600, y ≥ 680) clear, and leaves y 800 to 1000 for the below-ground line.
- Layer ids inside the block (later comps toggle these, never redraw them): `g-master-map-l-grid`, `-l-city`, `-l-streets`, `-l-path`
  (polygon + centre line), `-l-sirens` (25 `<use>` of `#g-master-map-siren`), `-l-places` (Table 4-3 markers), `-l-ring`, `-l-below`.

## 3. GEOMETRY
- Ground: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`, on from frame 0.
- Grid: 1 px `#5a768f` at 13 %, a line every 1 mile (s px).
- City outline: 2 px `#f2f5f8` at 70 %, fill `rgba(242,245,248,.03)`.
- Streets: TIGER primary and secondary roads in the frame, 1.5 px `#4a5560`; I-44 3 px. Each named street the acts use is its own
  path id (`g-master-map-st-<name>`): Range Line Rd, Main St, Schifferdecker Ave, 7th St, 20th St, 26th St, 32nd St, Connecticut Ave, I-44.
  No street labels in the base (acts add them).
- Damage path (hidden here, opacity 0): polygon fill `rgba(192,57,43,.22)`, 1 px edge `#c0392b` at 60 %; centre line 2 px `#f2f5f8`,
  `stroke-dasharray` = ceil(length)+1 (computed), dashoffset full, so a copy draws it west to east.
- Siren icon `#g-master-map-siren` (hidden here): 28 px tall, a 2 px pole (14 px) under a horn head (trapezoid 14 px wide at the mouth)
  and two 2 px sound arcs to its right; stroke `#f2f5f8`, no fill. `g-a6-siren` enlarges this glyph, so it must read at 360 px too.
- Location markers (hidden here): 14 × 14 px rounded squares, 1.5 px `#dfe7ee` at 60 %, no fill, one per location row.
- **SIREN RING** (the base style every act copies): centre = the area centroid of the city outline; ring radius r = the largest
  centroid-to-outline-vertex distance + 24 px (computed). Stroke 4 px Danger red 2 `#e74c3c`, solid. Pulse = three expanding copies,
  scale 1.00 → 1.18 and opacity 0.8 → 0 over 1.2 s, staggered 0.4 s, `svgOrigin` at the centre in from and to vars, finite `repeat`.
  Here two rings: ring A (5:11) radius r, ring B (5:38) radius r + 24 (24 px is visual separation only, as `g-a1-second-siren` §2).
- Ring stamps: "5:11 PM" left of ring A at 200°, "5:38 PM" right of ring B at 340°, Arial 700 30 `#f2f5f8`, 20 px clear of that ring's
  largest pulse radius. If a stamp would leave the text-safe frame (x 96 to 1824), cap the pulse scale at 1.10 and report it.
- **BELOW-GROUND LINE** (the base style a2, a3 and a4 copy): y 880, x 200 to 1500, 2 px `#93a3b2`, solid, nothing on it. Label
  "Below ground", Arial 700 22 `#93a3b2` tracking 3, left x 200, baseline 864.
- Chip zone: glass chip centred x 960, y 96 to 166. Source line: x 96, baseline 1010, Arial 700 20 `#c8d3e0`.
- Push (T1-S3): a uniform scale 1.00 → 1.3292 (= 1728 / 1300, computed) about the comp, translated so the line's centre (850, 880)
  lands at (960, 540); the line then spans x 96 to 1824. Linear is fine (under 1.5x). Ease power2.inOut.
- HUD label after the push: "Below ground", Arial 700 26 `#93a3b2` tracking 8, left x 110, baseline 512 (fixed layer, not scaled).
- Presenter circle: graphics-only scene. If ring B × 1.18 enters x ≥ 1600, y ≥ 680, the circle is off for this comp; say which.

## 4. MUST BE TRUE IN THE PICTURE
1. Ring A covers the whole city outline: every outline vertex lies at least 10 px inside ring A (E6 "for Jasper County and Joplin").
2. Rings A and B differ in radius by 24 px ±2; neither reads as a wider reach.
3. Only two times appear, "5:11 PM" and "5:38 PM"; no siren icons, path, markers or dots are visible in this comp.
4. Base read (the all-layers still): the path's centre line inside the city outline measures 6 mi × s ±10 % (W3, W4); the path is never
   wider than 1.0 mi × s (W3, W5, W7); it runs west to east (W6); there are exactly 25 siren icons (S2) once Open 2 is filled.
5. The below-ground line carries nothing but its label, and no text rides the push: the line label is gone before the push starts and the HUD label enters after it settles.
6. No label sits under a ring or a pulse copy at the pulse's maximum.

## 5. PANEL TEXT (exact) and CUES
| element | text | cue |
|---|---|---|
| ground, grid | | frame 0 |
| city outline draws (strokeDashoffset), streets fade in 0.40 to 1.20 | | t1-s2 "You" 0.00 to "Joplin's" 1.22 |
| ring A draws (0.4 s) + stamp; pulse starts | "5:11 PM" (E6) | t1-s2 "sirens" 2.02 |
| ring B draws + stamp; pulse starts | "5:38 PM" (E14) | t1-s2 "didn't." 4.00 |
| source line | "NWS timeline · 3 minutes each" (E6, E14) | t1-s2 "didn't." 4.00 + 0.2 |
| chip | "SOUNDED TWICE" (S27) | t1-s2 "They" 4.64 |
| both rings flash (stroke 4 → 8 → 4 px, 0.4 s) | | t1-s2 "twice." 5.02 |
| chip, stamps, source line out (0.4 s); rings fade out (0.6 s) | | t1-s3 "Then," 0.00 |
| below-ground line draws left to right (0.8 s), label rises | "Below ground" | t1-s3 "Then," 0.00 |
| line label out | | t1-s3 "why" 3.14 − 0.15 |
| push onto the line | | t1-s3 "why" 3.14 to 4.30 |
| HUD label in | "Below ground" | t1-s3 "basement?" 4.40 |
| hold | | to 5.24: the scale keeps creeping 1.3292 → 1.345 (ease none); cut to CLIP 1 on the host end |
Map drift in T1-S2: scale 1.00 → 1.02 over 0.00 to the t1-s2 end, ease none. Longest gap between moves: under 4 s (pulses run throughout T1-S2).

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (item 6: `s`, centroid, r, the push transform and the path length computed by script and stated), §8.
