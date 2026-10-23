# g-a2-map-close · DEEP (Opus 5.5, high) · act a2, a2-s10 tail, a2-s11, a2-s12

**Open numbers (left out of the drawing):** the 5:34 touchdown point (E13's fraction of a mile is garbled in the
extraction, facts.md NOTE), so the chapter card's "touchdown dot at 5:34" is not drawn here.

**Base, never redrawn:** the master map and its siren ring (T1-S2), the residential layer if the base has one (I1-S8
dots by location type), and the thin "below ground" line (T1-S3). Same builder as g-a2-countdown; the ring states
(lit, dark) are the ones built there. If the base has no residential layer, report; never draw neighbourhoods by eye.
**Host:** a2-s10 "And" @14.62 (under g-a2-doc-cues' exit) to the end of a2-s12 plus 1.0 s; the chapter blackout follows (editor).
**Cue clock:** `segment offset + word start`; offsets = each segment's narration `data-start` minus host `data-start`.
**Over:** designed full-frame map. Corner circle stays on where the corner is free: nothing enters x >= 1600, y >= 680.

## 0. What this graphic claims
The second siren meant opposite things to different people, and the city's sirens had no all-clear signal; at 5:38
most people went to the best spot they had, and what was under that spot is the next question.

## 1. SOURCE (confirmed rows, quoted)
- E14 (NWS Table 1): "538 pm CDT - Second 3 minute siren alert sounded for Jasper County and Joplin."
- S26 (NIST Sec. 4.7.1.2): "Their interpretations of the second siren ranged from it being a warning for a situation that was more dangerous than before to an "all clear" from danger."
- S25 (NIST Sec. 4.7.1.2): "Joplin survivors were unsure why the second siren had been initiated, since this had been perceived by many as never happening in the past."
- S33 (NIST Sec. 4.3.1): "The City of Joplin's system was not designed to issue an "all-clear" message via the sirens or any kind of public address announcement."
- H23 (NWS Finding #2d): "the majority of surveyed Joplin residents took shelter in the most appropriate location available to them. This included basements, interior rooms or hallways, or crawl spaces."

## 2. DATUM, SCALE, ORIENTATION
- The base's projection, north up; the ring centred on the city centroid as in g-a2-countdown.
- HUD fixed: source line right 96, top 54; chip slot left 110, bottom 110.
- Camera: still for a2-s11 (labels on the HUD layer must not ride a move); from a2-s12 "best" a push 1.00 to 1.12 toward the lit residential area, ease power2.inOut, ending 1.0 s before the host end; then a slow drift.

## 3. GEOMETRY
- Ring: lit state, stamped "5:38 PM" (the base's stamp style).
- Split: two leader lines (`#dfe7ee` 3 px) from the ring's west and east edges, 140 px out, each ending at a glass chip label: west "A worse warning", east "All clear", Arial Black 900 40 px #f2f5f8. The east label's right edge stays left of x 1600; both sit above y 680 or left of x 1600.
- Crossed icon: a siren horn glyph (SVG, 56 px, `#dfe7ee` 3 px strokes) just right of or under the "All clear" chip; a red `#e74c3c` 5 px strike draws through the glyph, corner to corner, scaleX 0 to 1, 0.35 s.
- Chip: glass, Arial Black 900 40 px: "NO ALL-CLEAR SIGNAL".
- Source line text: "NIST Sec. 4.7.1.2 · Sec. 4.3.1".
- Residential lit: the base's residential blocks inside the damage path to `#d8a13a` at 70 % fill, staggered by 0.05 s west to east, 0.6 s total.
- Below-ground line: the T1-S3 line, `#93a3b2` 2 px, drawn left to right under the lit area, label "Below ground" diagram label (Arial 700 22 #93a3b2 tracking 3) at its left end; the line stays empty (no dots, no marks).
- Hold motion: the ring's pulse continues through a2-s11 (finite repeat); a2-s12 has the push, then drift.

## 4. MUST BE TRUE IN THE PICTURE
1. Both labels come off the same 5:38 ring: one siren, two readings (S26).
2. "All clear" never stands alone: from "signal" on, the strike and the chip say the system had no all-clear signal (S33).
3. The ring is the second sounding: stamped 5:38 PM (E14), not 5:11.
4. The "Below ground" line is empty: no dot, icon or number on or under it.
5. Labels sit on the fixed HUD layer and do not move with the a2-s12 push (they are gone before it starts).
6. Nothing enters x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s10 · "And" · 14.62 | map ground up under g-a2-doc-cues' exit |
| a2-s10 · "second" · 15.18 | 5:38 ring lights with its stamp "5:38 PM", pulse starts |
| a2-s11 · "depended" · 0.42 | source line "NIST Sec. 4.7.1.2 · Sec. 4.3.1" |
| a2-s11 · "worse" · 3.02 | west leader draws, chip "A worse warning" |
| a2-s11 · "all" · 5.02 | east leader draws, chip "All clear" |
| a2-s11 · "all" · 8.02 | crossed siren icon in, strike draws |
| a2-s11 · "signal." · 8.48 | chip "NO ALL-CLEAR SIGNAL" |
| a2-s12 · "538," · 0.76 | labels, icon, chip and source line exit (0.5 s); the ring pulses once more |
| a2-s12 · "best" · 2.46 | residential area lights; push starts |
| a2-s12 · "underneath" · 6.36 | below-ground line draws, label "Below ground" |
| a2-s12 · "spot." · 7.22 | hold 1.0 s on the finished state (drift only); the editor's chapter blackout follows |

## 6 to 8
As `references/mg-brief-template.md` §6, §7, §7a, §8. File `compositions/g-a2-map-close.html`, timeline
`window.__timelines["g-a2-map-close"]`, root id `a2mc-root`.
