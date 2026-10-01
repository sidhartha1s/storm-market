# BRIEF — g-sensor-gap-a5 · A5 teaser (gauge lit, slope dark) · icon pair

## 0. What this graphic claims
Across both months, Nepal's warning system measured one thing well (rivers), and it was the thing that moved last.
Two icons say it without a sentence: river gauge glowing, slope icon dark. This is the cta-hinge line — the payoff (g-sensor-gap) comes after the CTA.

## 1. SOURCE
Sets up factcheck-D#1 (49/77 districts) and factcheck-C#17-19 (system built for river floods, gauges swept away
before warning). No new numbers in THIS teaser — icons only, numbers land in the A6 payoff.

## 2. DATUM, SCALE, ORIENTATION
Centred pair, full 1920x1080 stage, icons on the mid-line y=460, clear of the presenter corner (both icons x<1600).

## 3. GEOMETRY (px)
- Gauge icon: circle centre (760,460) r=100, stroke #3fa15a 4px, fill rgba(63,161,90,.12), inner wave glyph (simple
  sine path), glow filter (drop-shadow 0 0 24 rgba(63,161,90,.6)).
- Slope icon: triangle centre (1160,460) (apex (1160,380), base (1080,540)-(1240,540)), fill #2a3644, stroke
  #4a5560 2px, no glow (dim/grey, opacity 0.55).
- Label under gauge (760,600) "RIVER GAUGES" 22px #dfe7ee tracking3.
- Label under slope (1160,600) "SLOPE SENSORS" 22px #93a3b2 tracking3, opacity 0.6.

## 4. MUST BE TRUE
1. The gauge icon is visibly lit/glowing (green, pulsing); the slope icon is visibly dim/grey — the contrast is the whole point.
2. No number or claim text appears (icons + two short labels only; the payoff numbers belong to g-sensor-gap).
3. Both icons sit left of x=1600 (presenter keep-out respected).
4. Something pulses continuously (gauge glow breathing) for the whole 7 s window.

## 5. PANEL TEXT (exact) and CUES
Text: "RIVER GAUGES" · "SLOPE SENSORS" (no numbers, no headline — narration carries the line).
Cues (s, from "Across both months..." sentence start, A5, 175 wpm est):
/* CUE "Across both months, Nepal's warning system measured one thing well" @est 0.3 */ gauge icon pops in, glow starts (continuous pulse begins immediately).
/* CUE "and it was the thing that moved last" @est 3.4 */ slope icon fades in dim, label reveals under both.
Duration 7.0 s (both icons exit scale 1->0.85 autoAlpha 0 at 6.4, 0.5 s power3.in — CTA hard-cuts right after).
