# BRIEF — g-monsoon-calendar · A2 open · June-October bar, pin lands Sept 27

## 0. What this graphic claims
Nepal's monsoon runs mid-June to early October; by late September the hillsides have been soaking for months. A red
pin lands on Sept 27, near the tail end of the wet season, not its peak.

## 1. SOURCE
factcheck-B#2: normal onset ~June 13, normal withdrawal ~Oct 2 (DHM-derived, travelhimalayanepal.com). Script line:
"usually arrives in mid June and starts leaving in early October".

## 2. DATUM, SCALE, ORIENTATION
Axis y=780, x 240 (June) to 1680 (Oct), 360px/month (5 month ticks: June/July/Aug/Sept/Oct at 240/600/960/1320/1680).
Full-frame diagram, RHS clear.

## 3. GEOMETRY (px)
- Axis line x 240-1680 y=780, stroke #5a768f 3px. 5 ticks + month labels 22px grey tracking3 at y=810.
- Onset mark: mid-June, x = 240+(15/30)*360 = 420. Vertical tick + label "ONSET" above at (420,700) 19px #7fb2e5.
- Normal-withdrawal mark: early Oct (~Oct2), x = 1680+(2/30)*360 = 1704. Vertical tick + label "NORMAL WITHDRAWAL"
  above at (1704,700) 19px #d8a13a (kept inside frame right margin, text right-anchored so it never runs past x=1824).
- Red pin: Sept 27, x = 1320+(27/30)*360 = 1644. Pin icon (teardrop, #d0121f) drops from y=600 to tip at y=780,
  label "SEPT 27" above pin at (1644,560) diagram-label tier.
- Wet-band: shaded band under the axis from onset(420) to withdrawal(1704), fill rgba(90,118,143,.15).

## 4. MUST BE TRUE
1. Onset mark sits strictly between June and July ticks (x 240-600), closer to the June end (mid-month).
2. Normal-withdrawal mark sits strictly at or just past the Oct tick (x>=1680).
3. The red pin lands between the Sept and Oct ticks, closer to Oct (x 1320-1680, specifically ~1644 for the 27th).
4. The pin is visibly LEFT of the normal-withdrawal mark (storm arrives before the season technically ends).
5. Wet-band shading spans the full onset-to-withdrawal range, establishing "soaking for months" visually.

## 5. PANEL TEXT (exact) and CUES
Text: "ONSET" · "NORMAL WITHDRAWAL" · "SEPT 27" · month labels JUNE/JULY/AUG/SEPT/OCT.
Cues (s, from "Nepal gets most of its rain..." sentence start, A2 open, 175 wpm est):
/* CUE "Nepal gets most of its rain from the summer monsoon" @est 0.3 */ axis + wet-band draw in (scaleX 0->1).
/* CUE "which usually arrives in mid June" @est 3.4 */ onset mark + label pop in.
/* CUE "and starts leaving in early October" @est 5.4 */ withdrawal mark + label pop in.
/* CUE "the hillsides have been soaking for more than three months" @est 9.9 */ wet-band pulses once (opacity breathe).
/* CUE "holding more water than at any other time" @est 14.2 */ red pin drops onto Sept 27, label reveals, hold.
Duration 19 s (whole diagram exits x:660->1400 autoAlpha 0 at 18.4, 0.6 s power3.in).
