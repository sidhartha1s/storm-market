# BRIEF — g-insar-creep · A3 full payoff (radar finishes, then empty over Kali Gandaki) · SCHEMATIC swath

## 0. What this graphic claims
In August, ICIMOD's radar measured the Langtang slope creeping up to 30 cm (about 12 in) over 3-4 weeks before it
failed. For the Kali Gandaki wall and the Himlung face, no agency has published anything like that as of Sept 29 —
the strip returns EMPTY over a Kali Gandaki outline with a "?" stamp.

## 1. SOURCE
ICIMOD / Discover Magazine, quoted: "satellite radar showed the slope slid up to twelve inches in three to four
weeks" (factcheck-B#20, script A3). "No agency had published radar from before September twenty seventh"
(factcheck-B#22, confirmed by a full search sweep). Channel rule: US units first on screen (inches primary, cm secondary).

## 2. DATUM, SCALE, ORIENTATION
RHS-rail layout like g-radar.html: radar box left 90 top 170 w1180 h700; RHS rail 1180-1920 gradient per tokens.
No real map geometry exists for this schematic slope; label it so.

## 3. GEOMETRY (px)
- Radar box: schematic ridge silhouette (simple triangular slope outline, single peak at (600,260), base y=820,
  x 90-1270), fill #15202b, stroke #4a5560.
- Colour ramp overlay: horizontal band across the slope face, local rect (150,300)-(1050,520), gradient green
  #3fa15a -> amber #d8a13a -> red #c0392b, left to right = low to high displacement.
- "3 TO 4 WEEKS" bracket: horizontal bracket line y=860, x 150-1050, tick ends, label centred below at (600,900).
- ICIMOD text card: small glass card top-left of radar box, local (140,190) w360 h110: "ICIMOD" big 30px, "KATHMANDU"
  sub 19px grey.
- RHS rail: eyebrow "SATELLITE RADAR" · counter Courier 700 84px #e74c3c "ABOUT 12 IN" (primary, US units first) ·
  sub Courier 400 30px #93a3b2 "30 CM" (secondary, smaller) · counter label "LANGTANG · AUG 2026".
- Empty-state (second half): radar box content crossfades: ridge outline relabels "KALI GANDAKI", colour ramp fades
  to 0 (flat grey #2a3644 fill, no gradient), a red "?" stamp (AbrilFig 120px, #d0121f, circle border) pops at
  centre of the box (660,500).

## 4. MUST BE TRUE
1. The big on-screen number is "ABOUT 12 IN", never "30 CM" alone as the primary (US units first, channel rule).
2. The "3 TO 4 WEEKS" bracket is visible under the colour ramp before the counter finishes climbing.
3. "ICIMOD" and "KATHMANDU" both appear as the text card (matches the Picture line's literal instruction).
4. The empty second state shows NO colour ramp and IS labelled "KALI GANDAKI", with a "?" stamp, not a number.
5. Both states never appear simultaneously (crossfade, not a split screen).

## 5. PANEL TEXT (exact) and CUES
Text: text card "ICIMOD" / "KATHMANDU" · counter "ABOUT 12 IN" / "30 CM" · label "LANGTANG · AUG 2026" · bracket
"3 TO 4 WEEKS" · empty state label "KALI GANDAKI · SEPT 27" · stamp "?".
Cues (s, from "In August, someone did measure..." paragraph start, A3, 175 wpm est):
/* CUE "In August, someone did measure the Langtang slope" @est 0.3 */ radar box + slope outline draw in, colour ramp reveals left-to-right start.
/* CUE "ICIMOD is a mountain research center in Kathmandu" @est 4.1 */ ICIMOD text card pops in.
/* CUE "the slope slid up to twelve inches in three to four weeks" @est 10.5 */ counter climbs 0->12(in)/0->30(cm), bracket draws under it, ease power2.out ~2.2s.
/* CUE "no agency had published radar from before September twenty seventh" @est 15.0 */ crossfade to empty state: ramp fades out, outline relabels KALI GANDAKI, "?" stamp slams in (power4.in).
/* CUE "the reports couldn't even agree on how many people" @est 21.0 */ hold, stamp breathes once (scale 1.05 yoyo).
Duration 26 s (rail exits x:660->1400 autoAlpha 0 at 25.4, 0.6 s power3.in).
