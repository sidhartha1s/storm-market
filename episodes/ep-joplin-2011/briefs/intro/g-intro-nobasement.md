# BRIEF · g-intro-nobasement · "most homes had no basement, and there was no public shelter" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, segment I1-S1. Full-frame MG. Host from i1-s1 "about" 3.52 to the wav end 14.56; CLIP 1
(`i1-s1_c1_dvids-aerial-residential-a.mp4`) plays before it from i1-s1 0.00 and the host cuts in over it.
Bases: HOUSE SECTION (`briefs/a3/g-a3-house-section.md` §2, §3: build and read that base first, same builder) and MASTER MAP
(`g-intro-map`'s BASEMAP block, copied verbatim; layers toggled, no geography added).
Open numbers: `_list.md` Open 3 ("2010 Census" not drawn). Nothing else.

## 0. What this graphic claims
Most Joplin homes had no basement, about 8 in 10 (H1); the city and county had no community shelter or safe room (H3, H4)
in a town of 50,150 (X21). The tornado crossed about 6 miles of the city in about 15 minutes (W3, W8). And having a basement was
not the whole story: some who had one were not down in it (H8), shown as an empty lit stair, no number.

## 1. SOURCE
- H1 "Also, 82 percent of the homes in Joplin lacked basements." NIST Finding 20.
- H3 "There were no community shelters or safe rooms in the City of Joplin or Jasper County at the time of the May 22, 2011, Joplin tornado." NIST Finding 20.
- H4 "the City did not own or operate any public storm shelters." NIST E.4.1.
- X21 "with a population of 50,150." NIST Sec. 1.1.
- W3 "on the ground for approximately 6 miles and 15 min in Joplin, Missouri, and created a damage path as much as a mile wide." NIST Sec. 1.3. W8 "approximately 15 minutes". W6 "roughly west-to-east path".
- H8 "NIST found that at least two of these three individuals did not access their basements before the storm hit." NIST Sec. 4.6.2.2 (the count is not shown; A3 spends it).

## 2. DATUM, SCALE, ORIENTATION
- House scene: the a3 house base unchanged (grade line y 660, schematic, no scale), **without** the a3 figure.
- Map scene: the base's `s`, centroid and framing (box x 200 to 1500, y 200 to 770), north up. Path, city and markers from the base layers.
- Inset: the same house geometry scaled 0.55 inside a glass card x 1120 to 1760, y 150 to 650 (computed: 960 × 0.55 = 528 px wide).
- Presenter circle: may stay on; nothing enters x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- **House scene** (3.52 to 6.14): the a3 base's house, foundation band, grade line, "Ground" label and dashed basement ghost
  with its label "No basement" at (960, 1004). Walls are outlines with the interior visible, never a solid block. No figure.
- Chip zone top centre y 96 to 166. Source line x 96, baseline 1010.
- **Map scene** (6.14 on): base layers grid, city, streets on; path layer hidden until its draw; sirens, markers, ring, below-ground line hidden.
  - Scan: a 2 px vertical line `#7fb2e5` at 50 % with a 60 px soft trail, sweeping x 200 → 1500 (1.26 s, ease none), finding nothing.
  - Shelter label: glass label centred x 960, y 96 to 166, Arial 700 30 `#f2f5f8`.
  - City label: outside the outline at its north-west, 20 px clear of the stroke: "Joplin" Arial 700 30 `#f2f5f8`, then "Population 50,150"
    Arial 700 22 `#93a3b2` tracking 3 on the line below.
  - Path: the base's polygon fades in (0.3 s) and its centre line draws west to east (strokeDashoffset, 1.3 s, ease power1.inOut).
  - Path labels, Arial 700 26 `#f2f5f8` tracking 2: "6 miles in Joplin" above the path's middle, "About 15 minutes in the city" below it,
    each 24 px clear of the polygon edge and inside the text-safe frame.
- **Inset** (11.34 on): glass card (tokens.md surface, radius 28) slides in from the right `fromTo(x:660 → 0, 0.7, power3.out)`; the map
  under it dims to 40 %. Inside: the house at 0.55 with a real basement (solid 2 px `#dfe7ee` box at the a3 ghost's rect, scaled) and a
  6-step stair from the floor's right third down to the basement floor, stroke `#d8a13a` 3 px. "Lit": basement fill `rgba(216,161,58,.18)`
  that fades up; "empty": nothing inside it. Diagram label "Basement" Arial 700 22 `#93a3b2` tracking 3, inside the basement, top-left.

## 4. MUST BE TRUE IN THE PICTURE
1. The house is never drawn as a solid block; the basement ghost is dashed and empty.
2. No shelter icon, marker or dot appears anywhere on the map (the markers layer stays hidden in this comp).
3. The path draws west to east and its in-city length is the base's 6 mi × s ±10 % (W3); the two path labels never touch the polygon.
4. The city label reads "Population 50,150" with no census year (Open 3).
5. The inset basement holds no figure and no number; its stair is lit.
6. One chip or label in the top-centre zone at a time.

## 5. PANEL TEXT (exact) and CUES (i1-s1)
| element | text | cue |
|---|---|---|
| house draws (walls stroke 0.5 s, roof 0.3 s), grade line, "Ground" | "Ground" | "about" 3.52 |
| chip | "8 IN 10: NO BASEMENT" (H1) | "8" 3.62 |
| basement ghost dashes in, label | "No basement" | "none." 4.62 |
| source line | "82% of Joplin homes · NIST Finding 20" (H1) | "none." 4.62 + 0.2 |
| chip out; fade-through to the map (0.4 s); source line out | | "And" 6.14 |
| scan sweeps | | "single" 6.74 to 8.00 |
| shelter label | "No community shelters or safe rooms · city or county" (H3, H4) | "shelter" 7.40 |
| source line | "NIST Finding 20" (H3) | "shelter" 7.40 |
| city label | "Joplin" | "town" 8.08 |
| population line | "Population 50,150" (X21) | "50" 8.68 |
| shelter label out; path polygon in, centre line draws W to E | | ",000." 9.10 to 10.40 |
| source line swaps | "NIST Sec. 1.1 · Sec. 1.3" (X21, W3) | ",000." 9.10 |
| path label 1 | "6 miles in Joplin" (W3, W4) | 9.90 (unspoken; after the draw passes mid-path) |
| path label 2 | "About 15 minutes in the city" (W3, W8) | 10.30 (unspoken) |
| path labels out (0.3 s) | | "Even" 10.62 + 0.3 |
| inset card in, map dims | | "had" 11.34 |
| source line swaps | "NIST Sec. 4.6.2.2" (H8) | "had" 11.34 |
| basement glow up | "Basement" | "basement" 11.66 |
| a soft light pulse runs down the stair (0.6 s) | | "down" 12.64 |
| hold | | to 14.56: card floats y ±3 px, map drifts scale +1 %; cut on the host end |

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (item 6: inset scale and path length by script), §8.
