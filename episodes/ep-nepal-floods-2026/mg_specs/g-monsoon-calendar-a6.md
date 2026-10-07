# BRIEF — g-monsoon-calendar-a6 · A6 return · pin moves Sept 27 -> today, trekking bar opens

## 0. What this graphic claims
Two days on (Sept 29, "today" in-episode), the pin has barely moved; the normal-withdrawal mark is still ahead;
trekking permits reopened and the Himlung-style climbing season runs on into October, crews already deployed.

## 1. SOURCE
Episode date = Sept 29, 2026 (script Z: "twelve missing on the twenty ninth"). factcheck-C#22: Annapurna trekking
permits suspended 3 days, reopened Sept 27 (cautious). factcheck-C#23: Himlung-type climbing season runs through
October, crews already on the mountains when the avalanche struck. factcheck-C#21: normal withdrawal ~Oct 2, but
missed that date all 4 of the last 4 years (withdrew Oct 10-16 each year) — "still ahead" reads honest either way.

## 2. DATUM, SCALE, ORIENTATION
Same axis as g-monsoon-calendar (x240-1680, y780, 360px/month). Reuses that comp's end-state as its start-state.

## 3. GEOMETRY (px)
- Pin moves from Sept27 (x=1644) to "TODAY" Sept29 (x = 1320+(29/30)*360 = 1668); label swaps "SEPT 27" -> "TODAY ·
  SEPT 29"; withdrawal mark (x=1704, unchanged) stays visibly right of the pin the whole time.
- Trekking-season bar: new element, horizontal band y=860, x 1680-1850 (Oct opening, extends toward the frame edge,
  a soft fade-to-transparent at x=1850 signals "continues beyond frame"), fill rgba(216,161,58,.28), stroke
  #d8a13a 2px dashed. Label "CLIMBING & TREKKING SEASON OPEN" at (1680,895), left-anchored, 22px #d8a13a tracking3.

## 4. MUST BE TRUE
1. The pin's new position (x~1668) is strictly LEFT of the withdrawal mark (x=1704) — the season isn't officially over.
2. The pin visibly moves (a tween, not a jump-cut) from 1644 to 1668, matching "moves from Sept 27 to today".
3. The trekking-season band starts at or after the Oct tick (x>=1680) and reads clearly "OPEN", not implying the whole autumn already elapsed.
4. Both the pin's old and new labels are never shown at once (crossfade the text, not a stack).

## 5. PANEL TEXT (exact) and CUES
Text: "TODAY · SEPT 29" (replaces "SEPT 27") · "CLIMBING & TREKKING SEASON OPEN".
Cues (s, from "Trekking permits for the Annapurna trails..." sentence start, A6 tail, 175 wpm est):
/* CUE "Trekking permits for the Annapurna trails reopened" @est 0.3 */ pin begins sliding 1644->1668 (0.8s power2.inOut), label crossfades to "TODAY · SEPT 29".
/* CUE "after a three day pause for the rain" @est 3.1 */ hold, withdrawal mark pulses once (still ahead, emphasised).
/* CUE "The climbing season on peaks like Himlung runs through October" @est 8.2 */ trekking-season band draws in (scaleX 0->1, transformOrigin left).
/* CUE "crews are already on those mountains" @est 11.0 */ band label reveals.
/* CUE "the tents had been up for days" @est 14.5 */ hold, small pulse tying back to the camp (loop L7 open), exit begins.
Duration 18 s (whole diagram exits x:660->1400 autoAlpha 0 at 17.4, 0.6 s power3.in).
