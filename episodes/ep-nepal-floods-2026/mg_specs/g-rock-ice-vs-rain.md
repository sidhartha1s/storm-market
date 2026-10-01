# BRIEF — g-rock-ice-vs-rain · A4 · side-by-side, rock-ice slab vs plain rain landslide

## 0. Claim
Langtang (rock and ice, about 17,000 ft up) and the Kali Gandaki collapse (a rain landslide) are
different event types, side by side so the difference reads at a glance.

## 1. SOURCE
factcheck-B row 17 (Langtang rock-ice mechanism, CONFIRMED) + script A4 line "Langtang began about
seventeen thousand feet up" (consistent with factcheck-A's general Langtang framing; no single factcheck
row states the 17,000 ft figure directly, so this exact altitude is carried from the script as written —
flagged, not independently re-verified this pass). Kali Gandaki = the rain-triggered pore-pressure
mechanism already built in `g-pore-pressure`/`g-pore-pressure-a1` (factcheck-A row 11, factcheck-B row 7).
Both cross-sections are SCHEMATIC, NOT TO SCALE relative to each other (illustrative side-by-side, not a
literal shared datum).

## 2. DATUM, SCALE, ORIENTATION
- Stage 1920x1080, split down the centre at x=960 (a thin vertical divider #4a5560).
- LEFT (x96-940): Langtang mini rock-ice cross-section, reusing the g-rock-ice-mechanism visual language
  at smaller scale. RIGHT (x980-1824): Kali Gandaki mini rain-landslide cross-section, reusing the
  g-pore-pressure visual language at smaller scale.
- Each side's ground line at y=900.

## 3. GEOMETRY (px)
- LEFT: small rock face polygon (200,300)-(500,300)-(650,900)-(96,900), grey-brown gradient; a small
  slab+ice cap at the ledge (300,280)-(450,280)-(450,340)-(300,340); altitude tick "~17,000 FT" at (140,260)
  with a small upward arrow. Label below "LANGTANG · ROCK AND ICE" glass-card style chip.
- RIGHT: small slope polygon (1080,300)-(1780,900)-(980,900), soil gradient; a thin rising blue water line
  inside (matches g-pore-pressure-a1 visual language, no numbers). Label below "KALI GANDAKI · RAIN
  LANDSLIDE" chip.
- Divider line x=960, y 160-940, dashed #4a5560.

## 4. MUST BE TRUE
1. The LEFT side shows a slab with an ice cap (rock+ice) distinct in colour/texture from the RIGHT side's plain soil slope (no ice cap on the right).
2. The RIGHT side shows the rising blue water line inside the slope; the LEFT side does not have a rising water line (its mechanism is the falling slab, not pore pressure).
3. "LANGTANG · ROCK AND ICE · ABOUT 17,000 FT UP" sits under/beside the LEFT diagram only; "KALI GANDAKI · RAIN LANDSLIDE" sits under/beside the RIGHT diagram only — labels never cross the centre divider.
4. Both diagrams sit fully within their half of the frame (LEFT never crosses x=960, RIGHT never starts before x=960), respecting the 96/54 px text-safe margin on the outer edges.
5. Something moves on both sides for the whole window (LEFT: a small ambient shimmer on the ice cap; RIGHT: the water line still creeping).

## 5. PANEL TEXT (exact) and CUES
Labels (exact): "LANGTANG · ROCK AND ICE · ABOUT 17,000 FT UP", "KALI GANDAKI · RAIN LANDSLIDE".
Cues (s, local @175wpm, re-zeroed to this comp's mount point after g-social-mock exits — see script A4
paragraph, second half):
- divider draws + both mini cross-sections fade in together @0.4
- LEFT diagram detail (slab+ice, altitude tick) settles @0.0-1.5 (`/* CUE "Langtang began about seventeen thousand feet up" @est 7.89 (local 0.0) */`)
- LEFT label reveals @2.0
- RIGHT diagram detail (water line begins creep) @5.49 (`/* CUE "The Kali Gandaki collapse matches the rain landslide" @est 13.03 (local 5.49) */`)
- RIGHT label reveals @7.0
- both sides hold together, subtle emphasis pulse @13.03 (`/* CUE "closer to Langtang's type" @est 19.20 (local 13.03) */`)
- exit @24.5 (both halves slide out toward the divider then fade, power3.in)
Declared duration 27.5 s (local narration ~25.71 s + ~1.8 s tail).
