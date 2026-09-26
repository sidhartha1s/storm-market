# MG brief worked example: g-slope (Krakatau #5, 2026-09-12)

> Note (26 Sep 26): this example predates the 96/54 px text-safe margin. When copying, move the edge labels (SW, SEA LEVEL, CALDERA FLOOR, BLOCKS UP TO 70 M) to x >= 96.


The filled-in brief behind `references/mg-brief-template.md`. The SOURCE figure paths under `AppData\Local\Temp` were scratch copies and are gone; re-fetch the figures from the cited papers.

# BRIEF v2 — g-slope · "It was gentler." · 30 s cross-section MG (The Warning Hour, Krakatau #5, act 3 payoff)

## 0. What this graphic claims (read twice before drawing)
The 22 Dec 2018 collapse removed the south-west half of Anak Krakatau above water, including the summit, and left the
island's underwater slope on that side gentler than before. Two facts carry the beat: summit 338 m → 110 m (above sea
level), and the underwater SW slope 24° → 16°. Everything else on screen serves those two.

## 1. SOURCE (trace these; do not invent geometry)
- Meredew et al. 2026, Bull. Volcanology, Fig. 10b (SW–NE transects, "2x vertical exaggeration", 500 m scale bar):
  `C:\Users\Sidhartha\AppData\Local\Temp\claude\next-video\papers\figs\meredew-fig10.png`. Text, confirmed: SW submarine
  slope ~24° pre-collapse → ~16° by Aug 2019 (reduced ~8°, base extended 250–300 m SW); SW subaerial slope ~27° pre →
  ~7° June 2023; collapse removed all subaerial SW material incl. the summit, "returning the vent to below sea level";
  caldera basin floor ~279 m below sea level.
- Hunt et al. 2021, Nature Comms, Fig. 2E (X–X' section, distance 0–6000 m, depth +400…−300 m):
  `C:\Users\Sidhartha\AppData\Local\Temp\claude\next-video\papers\figs\hunt-fig2.png`. Deposit 0.214 km³ emplaced
  >1.5 km into the basin SW of the island; blocks up to 70 m above the surrounding seabed.
- Summit heights: 338 m before, 110 m the morning after (BMKG via the 2018 tsunami record).

## 2. DATUM, SCALE, ORIENTATION (fixed numbers; the reviewer measures against them)
- Stage = left 1180 × 1080 px. **SW is LEFT, NE is RIGHT**; print "SW" at (30, 560) and "NE" at (1120, 560).
- **Sea level y = 520** (draw the line full width, label "SEA LEVEL" at (30, 490)).
- **Scale: 1 px = 2 m horizontal, 1 px = 1 m vertical → 2× vertical exaggeration, same as the paper.** Print a 250 px scale
  bar labelled "500 M" at bottom-left (x 40–290, y 1000) and the caption at (40, 1040):
  "2× VERTICAL EXAGGERATION · HEIGHTS ABOVE SEA LEVEL · ANGLES ON THE UNDERWATER SLOPE".
- **Caldera floor y = 799** (279 m below sea level), dashed, label "CALDERA FLOOR −279 M" at (30, 815).

## 3. GEOMETRY (px; hit these within ±10 px)
BEFORE (solid until 6.0 s, then fades out):
- Summit apex at (900, 182) → 338 m above the datum. Tick + label "338 M" at x 960, from y 520 up to 182.
- SW subaerial face: apex (900,182) → shoreline (568, 520). That is 27° real, 45° on screen.
- SW underwater slope: shoreline (568,520) → foot on the floor (255, 799). That is 24° real, 42° on screen. Dashed blue
  guide #7fb2e5 along exactly this segment, label "24°" at (300, 690), left of the line, never on it.
- NE side: apex → (1180, 520) any plausible gentler line; not the point of the graphic.
- Rock fill #5b4a3f→#2a221d gradient; sea #1d3b57→#07131f below y 520.
AFTER (fades in at 6.0 s; both profiles never fully visible together):
- Remnant peak at (1000, 410) → 110 m. Tick + label "110 M" at x 1060, y 520→410. The old "338 M" tick dims to 35 %.
- The vent/crater region sits AT sea level around x 760–900 (a flat notch at y 520–535, label "CRATER LAKE" small at (770, 545)).
- New SW shoreline at (760, 520). New underwater ramp: (760,520) → foot (225, 799): the average post-collapse SW submarine gradient (~16°, Meredew), drawn at ~27° on screen so the foot lands 30 px SW of the old foot (base extended SW). NOTE 2026-09-12: the earlier value (274,799) contradicted truth §4.5; a builder caught it. §4 wins over §3 when they conflict, and the builder reports the conflict.
  Dashed red guide #e74c3c along exactly this segment, label "16°" at (330, 740), left of the line, never on it. The 24°
  guide and its label are GONE (opacity 0) once the 16° guide appears.
- Debris: on the floor, x 0–250, mounds up to 70 px tall (70 m), colour #8e2020, label "BLOCKS UP TO 70 M" at (20, 720).
BLOCK (the falling piece, 5.2–6.7 s): polygon apex (900,182) – (568,520) – (760,520) – (930,330); slides down-left along
the 24° guide direction (Δx ≈ −520, Δy ≈ +330), rotation −18°, then fades as the debris fades in.

## 4. MUST BE TRUE IN THE PICTURE (reviewer checks these FIRST; any failure = FIX, layout is not scored)
1. After the collapse the island is still above water: a 110 m remnant peak at y ≈ 410, right of the notch. No frame shows the whole island submerged.
2. Both angle guides lie entirely BELOW y = 520 (underwater) and end on the floor line y = 799. No guide starts at the summit.
3. 24° guide (blue) visible before; 16° guide (red) visible after; never both at once; each carries exactly one label, placed left of its line.
4. Height ratio: the 338 M tick is ~3.1× the 110 M tick (338 px vs 110 px).
5. The 16° ramp is visibly shallower than the 24° guide (~27° vs 42° on screen) and its foot (x≈225) is left of the old foot (x=255): base extended SW.
6. Debris mounds sit ON the floor line, left (SW) of the ramp foot, ≤ 70 px tall; the falling block travels down-LEFT.
7. SW/NE, SEA LEVEL, CALDERA FLOOR −279 M, 500 M bar, and the exaggeration caption are all present and legible.

## 5. PANEL TEXT (exact) and CUES
Right panel (740 px, full height, gradient `linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0))`, padding 96px 96px 0 120px):
eyebrow "THE SLOPE IT FELL FROM" · headline "It was gentler." · italic sub "the fall took the steep face and left a ramp" ·
row 1 big "24°" (blue) label "UNDER WATER, BEFORE" sub "steep, overloaded" · row 2 big "16°" (red) label "UNDER WATER, AFTER"
sub "lower, wider ramp" · note "The island growing back today is growing on different ground than the one that fell."
Cues (s): headline 0.4 · "338 M" tick 2.0 · row 1 + 24° pulse 4.2 · block detaches 5.2, slides 5.6–6.8 · before→after crossfade 6.0–6.6 ·
row 2 + 16° guide + "110 M" 6.6 · ramp emphasis (stroke pulse) 9.8 · note 15.5 · panel exit 29.4 (x:980, autoAlpha 0, 0.6 s power3.in). Duration 30 s.
