# BRIEF g-a3-house-joints · A3-S6 · DEEP (Opus 5.5, high effort) · on base `g-a3-house-section`

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Base: `compositions/g-a3-house-section.html` (copy its ground, grade line, foundation, floor, walls and roof geometry verbatim; drop the partitions, tub, figure and basement ghost). Motion reference: `library/inhouse/moves/demo.html`.
Before this host: the NIST ground photograph of a wood-frame house with roof and walls separated (a3-s6 0.00 → 2.60). If a moving clip of the same is sourced, it replaces the photo; the 7.88 s segment has no room for both.

## 0. What this graphic claims
Wood-frame houses came apart mostly at the connections (roof to wall, wall to floor), not by the roof, walls or floor themselves breaking (H30).

## 1. SOURCE
H30, NIST NCSTAR 3 Finding 14: "Failures of residential wood-frame buildings predominantly involved failure of the connections between structural components, rather than of the components themselves (roof, walls, and floor)". No published drawing is traced: SCHEMATIC.

## 2. DATUM, SCALE, ORIENTATION
As the base: grade line y 660, floor y 640–660, walls y 400–640 at x 520–540 and 1380–1400, roof (480,400) – (960,220) – (1440,400). Schematic, no scale.

## 3. GEOMETRY
Assembled state (frame 0): the base shell, no partitions, no figure.
Joints: four rings, r 22 px, stroke `#c0392b` 3 px, no fill:
- J1 (530, 400) and J2 (1390, 400): roof to wall.
- J3 (530, 640) and J4 (1390, 640): wall to floor.
Exploded state:
- Roof: y −90 px, rotation −4° (svgOrigin (960, 400)). J1/J2 ring centres follow the opening gap (midpoint between the wall top and the roof underside).
- Walls: each lifts y −36 px and tilts 8° outward (left wall −8°, right wall +8°), pivot at its top inner corner (svgOrigin (540, 400) and (1380, 400)). J3/J4 ring centres follow the gap at the wall foot.
- Floor and foundation never move.
Labels (22 px diagram labels, `#93a3b2`, right-aligned, ending x 450): "Roof to wall" at y 395; "Wall to floor" at y 650. Leader line 1 px from each label to J1 / J3.
Chip (glass popup-chip, left 96, top 96): "THE JOINTS GAVE" 52 px. Source line (glass source-label, left 96, baseline ≤ 1026, 20 px): "NIST Finding 14".

## 4. MUST BE TRUE IN THE PICTURE
1. Roof, both walls and the floor stay whole: each moves as one rigid piece; no crack, break or bend inside any of them.
2. Every gap opens only at J1–J4.
3. The floor and foundation stay on the grade line, unmoved.
4. Each ring sits on its gap at three checked times (gap open start, mid, end), within ±10 px.
5. The labels never sit under a ring, a leader or a moving piece, including mid-tween.

## 5. PANEL TEXT (exact) and CUES (a3-s6.words.json)
Text: "THE JOINTS GAVE" · "Roof to wall" · "Wall to floor" · "NIST Finding 14".
Host: a3-s6 "mostly" @2.60 → "floor." @6.90 + 1.0.
- 2.60 "mostly": assembled house on from frame 0 (cut from the photo); source line in.
- 3.20 "gave": chip in.
- 3.80 "joints,": the four rings draw on (strokeDashoffset, 0.4 s, stagger 0.1 s).
- 4.78 "roof": roof lifts and tilts (0.7 s, power3.out); J1/J2 follow; "Roof to wall" label in at 5.2 (after the roof settles).
- 5.40 "walls": walls lift and tilt (0.7 s, power3.out); J3/J4 follow.
- 6.90 "floor.": J3/J4 pulse (scale 1 → 1.3 → 1); "Wall to floor" label in.
- Hold to host end: the exploded pieces drift (roof y ±3 px, walls ±1°), then a 0.4 s fade-through to the next picture.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-house-joints`, root id `g-a3-house-joints-root`.
