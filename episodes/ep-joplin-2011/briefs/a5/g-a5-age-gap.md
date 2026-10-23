# g-a5-age-gap · A5-S9 · DEEP (Opus 5.5, high or above) · [RS] [VE], the act's visual event

Open numbers: the two rates after NIST removed every hospital and nursing-home death (C30 gives none; NIST Fig 4-19 may, not extracted). So the drained bar has no number and no readable scale.
Ambiguity: the Picture line drains only the taller bar. Draining only the 60-and-over bar implies every removed death was 60 or older, which facts.md does not say. This brief follows the Picture line and hides every value during the drain; the orchestrator decides whether the under-60 bar also loses an unnumbered sliver.
Full frame, ground on from frame 0. **Host start = a5-s9 0.00**, duration 21.80 s (wav 21.20 + 0.60).
Opening span: a5-s9 0.00 to 7.0 is the Meadows answer ("NIST's answer is only a maybe", C27), with no picture of its own on the Picture line; the bars build here, straight after Paul's two numbers.

## 0. Claim
Older people in Joplin were lost at about 8 per thousand against 2 per thousand under 60, and the gap stayed after NIST removed every death in the hospital and the nursing homes.

## 1. Source
- C29: "approximately 8 fatalities occurred per thousand people in Joplin aged 60 years and over compared with 2 fatalities per thousand people in Joplin under 60 years" (Finding 47).
- C30: "This disproportionate result remains even after removing all hospital and nursing home deaths" (Finding 47).
- C27: Meadows, "One possibility is that the tornado, even at lower wind speeds ... cause[d] individuals who were already relatively frail to pass away" (Sec. 4.6.2.1): voice only, no text.
- Published figure: NIST Fig 4-19, "Comparison of fatality rates per thousand people within two populations". Before drawing, the orchestrator extracts it; if it prints the after-removal rates, those become the after-state (and leave Open numbers).

## 2. Datum, scale, orientation
- Baseline y 860, x 520 to 1400, 2 px `#93a3b2`.
- Scale 60 px per 1 death per 1,000 people (computed: 8 -> 480 px, 2 -> 120 px, ratio 4.0).
- Axis: left of the bars at x 500, ticks at 0, 2, 4, 6, 8 per 1,000 (y 860, 740, 620, 500, 380), labels 22 px; axis title `per 1,000 people` (22 px `#93a3b2`) at x 500, y 330.

## 3. Geometry
- Bar A (60 and over): x 640 to 860, top y 380 (480 px tall), fill `#c0392b`.
- Bar B (under 60): x 1060 to 1280, top y 740 (120 px tall), fill `#5a768f`.
- Value labels: `8` above bar A at y 340, `2` above bar B at y 700, 52 px Arial Black 900 `#f2f5f8`.
- Group labels under the baseline at y 900: `60 and over` under A, `Under 60` under B (30 px `#dfe7ee`).
- Gap guide: dashed 2 px `#93a3b2` line from bar B's top (y 740) across to bar A's right edge (x 860 to 1060), and a vertical bracket on bar A's right side from y 740 up to the top of bar A.
- Drain: the top slice of bar A (the hospital and nursing-home share) separates as its own rect and drains up and out (y -60, autoAlpha 0). Its height is unknown: draw it 60 px, and before it moves fade the axis ticks, axis labels and the `8` label to 0 so no value can be read off the after state. The bracket follows bar A's new top.
- Chip `THE GAP STAYS`: centred x 960, top 140.
- Source line bottom-left. Nothing at x >= 1600, y >= 680.

## 4. Must be true in the picture
1. Before the drain, bar A is exactly 4.0 times bar B's height (480 / 120 px, +-4 px).
2. After the drain, bar A's top is still above bar B's top by at least 200 px, so the gap visibly stays (C30).
3. After the drain no number, tick or axis label is visible: the after-state rates are not in facts.md.
4. Bar B is unchanged by the drain (Picture line) unless the orchestrator rules otherwise (see Ambiguity).
5. The `8` and `2` match A5-S8's chips (same figures, same base).
6. No age group other than "60 and over" and "Under 60" (the 80+ and 29- rates in C34 are a different base).

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| baseline, axis, group labels in | a5-s9 0.00 |
| bars grow (scaleY 0 -> 1, transformOrigin bottom, 0.8 s, A then B 0.3 s later) | a5-s9 0.00 to 1.4 |
| value labels `8`, `2` | with each bar's landing |
| source line `NIST Finding 47` | a5-s9 0.00 |
| bars breathe (scaleY 1 <-> 1.01, finite repeats) under the Meadows answer | 1.4 to 8.14 |
| gap guide + bracket draw on | a5-s9 "age"@10.94 |
| `8` label, axis ticks and labels fade to 0 | a5-s9 "took"@13.30 |
| top slice of bar A drains out, bracket follows | a5-s9 "hospital"@14.92 to "homes,"@16.04 + 0.4 |
| chip `THE GAP STAYS` | a5-s9 "gap"@16.94 |
| bracket pulses (scaleX 1 <-> 1.15, finite) | a5-s9 "Why"@18.80 to 21.20 |
| exit: fade-through | 21.20 to 21.80 |

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
