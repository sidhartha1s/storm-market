# BRIEF — g-insar-creep-i · I section teaser (radar strip freezes mid-count) · SCHEMATIC swath

## 0. What this graphic claims
Someone WAS tracking the Langtang slope by radar before it fell; the counter starts climbing but freezes before
telling the viewer the final number (paid off later in g-insar-creep). Compact card, shares the frame with the
other builder's g-aug-vs-sep teaser.

## 1. SOURCE
ICIMOD / Discover Magazine: satellite radar showed the slope slid up to 30 cm (about 12 in) in 3-4 weeks before the
Aug 26 Langtang collapse (factcheck-B#20). This teaser shows the counter mid-climb, not the final figure (freezes early).

## 2. DATUM, SCALE, ORIENTATION
Compact card, NOT full frame: left 700, top 560, width 600, height 380 (clears the presenter keep-out x>=1600,y>=680
entirely, and leaves the upper-left/upper-right free for the co-running g-aug-vs-sep teaser).

## 3. GEOMETRY (px, card-local then +700/+560 stage offset)
- Card bg glass rgba(10,16,24,.55) blur18, border 1px rgba(255,255,255,.14), radius 20, inset the 600x380 box.
- Radar swath rect: local (24,70) w552 h130, colour ramp fill (green #3fa15a -> amber #d8a13a -> red #c0392b, left to
  right), clipped by a reveal mask that only shows 0-40% of the ramp width when frozen (never reaches red).
- Counter: local (24,230), Courier 700 64px #e74c3c, value climbs 0 -> 18 (cm) then STOPS (never reaches 30).
- Label small: local (24,300) "LANGTANG SLOPE · CM / WEEK" 19px grey tracking3.
- Eyebrow: local (24,28) "SATELLITE RADAR" 22px grey tracking6.

## 4. MUST BE TRUE
1. The counter never reaches its confirmed final value (30 cm / 12 in) — it visibly stops short and holds a partial number.
2. The colour ramp reveal also stops short (never paints past ~40% width) in sync with the counter freeze.
3. The card sits entirely left of x=1300 and above y=940 (clear of the presenter corner and the right edge).
4. No specific final claim ("12 in", "30 cm") appears anywhere in this file — that number is g-insar-creep's payoff, not this teaser's.

## 5. PANEL TEXT (exact) and CUES
Text: eyebrow "SATELLITE RADAR" · label "LANGTANG SLOPE" · counter (climbs, freezes ~18).
Cues (s, from the "Nepal hadn't finished counting..." paragraph start, I section, 175 wpm est):
/* CUE "In August, satellite radar had caught the Langtang slope moving" @est 22.0 */ card pops in (scale 1.12->1, 0.4s), eyebrow + label reveal.
/* CUE "moving for weeks before it fell" @est 25.5 */ counter starts climbing 0->18, colour ramp reveal syncs, ease power2.out.
/* CUE "no agency has published anything like that" @est 29.5 */ counter/ramp FREEZE (tl.to duration 0, hard stop), small pulse on the frozen digits (scale 1.06 yoyo).
Duration 9.0 s (freeze holds ~2.5 s then card exits x:600->1300 autoAlpha 0 at 8.4, 0.5 s power3.in).
