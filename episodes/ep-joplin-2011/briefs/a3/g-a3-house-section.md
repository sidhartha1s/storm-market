# BRIEF g-a3-house-section · A3-S1 · DEEP (Opus 5.5, high effort) · BASE of the a3 house family

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Exemplars: `episodes/ep8-krakatau-seabed/compositions/g-slope.html` (cross-section on a datum), `library/inhouse/radar-beam.html` (full-frame SVG physics diagram).
Family: g-a3-house-joints and g-a3-stair copy this comp's house geometry (§2, §3) verbatim. Send this base alone for a full-size read before either is copied.

**Open (left out of the drawing):** the foundation type. The Picture line says "crawl space"; no facts.md row says what non-basement homes stood on. Draw the neutral foundation band in §3, unlabelled, and do not draw a crawl space until the orchestrator confirms a row.

## 0. What this graphic claims
Most Joplin families had no basement, so the best spot was an interior room in the middle of a one-story house, above ground. Two facts carry it: 82 percent of homes lacked basements (H1), and people sheltered in interior bathrooms, closets and hallways (H2).

## 1. SOURCE
- H1, NIST NCSTAR 3 Finding 20: "Also, 82 percent of the homes in Joplin lacked basements."
- H2, NIST NCSTAR 3 Sec. 1.2: "only 18 percent of homes had basements, residents in homes without basements reportedly took shelter in internal (or centrally located) bathrooms, closets, laundry rooms, or hallways of their homes."
- H11 (one-story is the common case): "A majority of the fatalities (50 out of 59, or 85 percent) occurred in one-story homes".
- No published figure is traced: the house is SCHEMATIC, NOT TO SCALE, and nothing on it claims a dimension.

## 2. DATUM, SCALE, ORIENTATION
- Full frame 1920 × 1080, ground per tokens.md "Canvas" (radial gradient, never flat).
- **Grade line y = 660**, full width, stroke `#93a3b2` 2 px. Diagram label "Ground" at (110, 646), 22 px.
- Earth: y 660 → 1080, fill linear gradient `#2a3644` → `#04070c`.
- Schematic, no scale bar; no dimension label anywhere.

## 3. GEOMETRY (px, ±10)
- Foundation band (below grade): rect x 520–1400, y 660–700, fill `#4a5560`. Unlabelled.
- Floor: rect x 520–1400, y 640–660, stroke `#dfe7ee` 3 px.
- Exterior walls: x 520–540 and x 1380–1400, y 400–640, stroke `#dfe7ee` 3 px, fill rgba(223,231,238,.06).
- Ceiling line y 400. Gable roof polygon (480,400) – (960,220) – (1440,400), stroke `#93a3b2` 3 px, fill rgba(147,163,178,.10).
- Interior partitions: x 800–812 and x 1108–1120, y 400–640. The middle room (x 812–1108) is the bathroom: tub outline x 830–900, y 604–640.
- Figure: crouched person silhouette, bbox x 905–1015, y 530–640, fill `#d8a13a` (amber 1), feet on the floor top y 640.
- Basement ghost: dashed rect x 560–1360, y 720–960, stroke `#93a3b2` opacity .6, dash 14/10, no fill. Diagram label "No basement" centred at (960, 1004), 30 px Arial 700 `#dfe7ee`.
- Chip (glass popup-chip, tokens "Surfaces"): left 96, top 96, "8 IN 10: NO BASEMENT" Arial Black 900, 52 px `#f2f5f8`.
- Source line (glass source-label): left 96, bottom 54 (baseline ≤ 1026), 20 px `#c8d3e0`: "82% of Joplin homes · NIST Finding 20 · Sec. 1.2".
- Corner x ≥ 1600, y ≥ 680 holds only earth fill (the presenter circle may sit there).

## 4. MUST BE TRUE IN THE PICTURE
1. One storey: a single wall height (y 400–640); nothing above the ceiling but the roof.
2. The figure is above ground: its lowest pixel is at y 640, above the grade line y 660.
3. The figure is in the middle room: both partitions lie between it and each exterior wall (figure bbox inside x 812–1108).
4. Below the house there is nothing but the foundation band and the dashed, empty ghost: no fill, no stair, no figure inside it.
5. The only figures on screen are "8 IN 10" (chip) and "82%" (source line). No other number.

## 5. PANEL TEXT (exact) and CUES (a3-s1.words.json)
Text: "Ground" · "No basement" · chip "8 IN 10: NO BASEMENT" · source "82% of Joplin homes · NIST Finding 20 · Sec. 1.2".
(The Picture line's label "no basement · 82% of Joplin homes · NIST Finding 20" is split: the name stays on the ghost, the figure and finding go to the source line, so one reading target at a time.)
Host: a3-s1 "For" @0.00 → "to." @9.58 + 0.8.
- 0.00 grade line + earth on from frame 0; house draws on (walls strokeDashoffset 0.0–1.0, roof 0.8–1.4). Whole comp: slow push scale 1.00 → 1.06, linear, transformOrigin (960, 540).
- 3.20 "closet": the two interior partitions draw on (0.5 s).
- 4.98 "bathroom": middle room fills rgba(216,161,58,.12), tub draws on.
- 5.60 "middle": figure drops in (y −40 → 0, autoAlpha 0 → 1, 0.45 s, power3.out).
- 7.36 "Eight": chip in (popup-chip entrance per quickref "Motion and exits").
- 8.98 "basement": ghost dashes draw on (0.8 s); "No basement" label in at 9.4; source line in at 9.4.
- 10.38 (9.58 + 0.8): fade-through 0.4 s into g-a3-map-homes. Figure breathes (y ±3 px, 1.6 s, finite repeats) through every hold.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-house-section`, root id `g-a3-house-section-root`.
