# g-a6-mercy · STANDARD (Sonnet 5.5, high) · a6-s5 3.80 to 8.22 · TEXT HELD

Open numbers: N7. Every line of this comp carries Mercy's "250 mph", which is not a facts.md row (source: mercy.net Joplin tornado history, edit_script A6-S5 Rows). Build the card, the motion and the cues with the text slots empty; the orchestrator drops in the text below once a facts.md row exists. Until then this comp does not mount.
Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass card over footage, BFMG).
Overlay: glass card over the NIST photograph of the old West Tower's fifth floor (A5-S5 still, reused), running s4 8.66 to s5 end. g-a6-cmt-nurse has exited at 3.80.

## 0. Claim
Mercy, which ran St. John's, says its new hospital has a window system designed to withstand 250 mph winds. A design claim in Mercy's words, never "rated for", never "all windows".

## 1. Source
- C15, NIST NCSTAR 3 E.4.2 Finding 18 (the photo beneath, context only): "The majority of the impact-resistant windows on the fifth floor (Behavioral Health Unit) of the West Tower of SJRMC remained intact".
- C16, NIST: "Mercy, the parent organization of SJRMC, decided to raze the entire facility" (ties Mercy to St. John's).
- The card's own words: mercy.net (not in facts.md, N7).

## 2. Datum, scale, orientation
Glass card in the centre popup zone, left/right 260 px, vertical centre y 470 so the photo's fifth floor stays visible: read the photo first and move the card to the zone that leaves the intact windows uncovered.

## 3. Geometry
- Card: glass surface (tokens.md), radius 28. One text slot at a time (one fact, one instance):
  - Slot Q (serif sub tier, Georgia italic, Amber 1, 2 lines max): Mercy's quoted words.
  - Slot A (attribution, row label tier): "Mercy".
  - Slot H (headline tier, Arial Black 900 52 px, Headline white): the chip text, which replaces slot Q in the same card, never beside it.
- Source line: bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- Motion: card in `fromTo(y:40, autoAlpha 0 → y 0, 1)` 0.5 s power3.out; Q builds line by line; Q lifts out (y -24, autoAlpha 0, 0.35 s) as H drops in (scale 0.92 to 1, 0.4 s, back.out); exit slide `x:980, autoAlpha:0, 0.6, power3.in` in the last 0.6 s.

## 4. Must be true in the picture
1. The words say "designed", never "rated", and never "all windows".
2. Slot Q and slot H are never visible together (same figure twice otherwise).
3. The photo's intact fifth-floor windows are not covered.
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (held until N7 is released) and cues (a6-s5.words.json)
| Element | Exact text (held) | Cue (word @ start s) |
|---|---|---|
| Card in, slot Q line 1 | a window system designed | "has" @ 3.80 |
| Slot Q line 2 | to withstand 250 mph winds | "designed" @ 4.66 |
| Slot A | Mercy | "designed" @ 4.66 |
| Source line | mercy.net, Joplin tornado history | "has" @ 3.80 |
| Q lifts, H in | DESIGNED FOR 250 MPH | "winds." @ 6.54 |
| Exit | none | 7.62 to 8.22 ("Did" @ 8.22) |

## 6 to 8
Template §6 to §8, COMPID `g-a6-mercy`.
