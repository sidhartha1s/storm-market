# g-a5-sjrmc-open · A5-S1 · STANDARD (Sonnet 5.5, high)

Open numbers: none. Ambiguity: "HOSPITAL FOR 140,000" is on the Picture line but not in the narration (see §5).
Overlay, root transparent. **Host start = a5-s1 "183"@2.80** (first mark), duration 9.24 s (ends at wav end 11.44 + 0.60 exit).
Under it (lower track, the whole window): `media/candidates/a5/a5-s1_c1_fema-total-loss.jpg` (FEMA, Jace Anderson, 24 May 2011) until a5-s1 "and"@6.02, then `a5-s1_c6_nist-east-tower-fig3-14.jpg` (NIST Fig 3-14). The cut point is the orchestrator's; this brief assumes 6.02.

## 0. Claim
St. John's held 183 people that evening, and one group of Joplin was lost at about four times the rate of people under sixty (which group stays hidden until A5-S8).

## 1. Source
- C8: "the 183 patients and staff who were at the hospital on May 22, 2011" (NIST Sec. 1.2).
- C9: "providing jobs to more than 1,700 people and care for 140,000 area residents" (NIST Sec. 1.2).
- C29: "approximately 8 fatalities ... per thousand people in Joplin aged 60 years and over compared with 2 fatalities per thousand people in Joplin under 60 years" (Finding 47). 8 / 2 = 4.0 (computed, python), so "4 TIMES".

## 2. Datum, scale, orientation
No scale. Chips in the centre-popup zone: one chip at a time, centred on x = 960, top edge y = 760. Source line bottom-left (see `_list.md`).

## 3. Geometry
- Chip box: auto width, padding 18 x 34 px, text 40 px; centred at x 960, top 760, so it ends near y 840.
- Source line: left 96, bottom 54.
- Nothing at x >= 1600, y >= 680.

## 4. Must be true in the picture
1. One chip on screen at a time; the outgoing chip has left (autoAlpha 0) before the next is at opacity 0.15.
2. "4 TIMES THE RATE" names no age group (the loop pays in A5-S8).
3. "183 INSIDE" sits over the FEMA still or the NIST towers photo, never over black.
4. No chip covers the hospital towers' upper floors in either photo; read a frame of each and move the chip down to top 800 at most if it does.

## 5. Panel text and cues
| text (exact) | in | out |
|---|---|---|
| `183 INSIDE` | a5-s1 "183"@2.80 | slides out a5-s1 "evening,"@5.16 |
| `HOSPITAL FOR 140,000` | 5.36 (after "evening,"@5.16; no spoken trigger) | slides out a5-s1 "four"@8.52 |
| `4 TIMES THE RATE` | a5-s1 "four"@8.52 | exit 11.44 to 12.04 |
| source line `NIST Sec. 1.2` | a5-s1 "183"@2.80 | exit 11.44 to 12.04 |
Ambiguity for the orchestrator: the 140,000 chip has no spoken word; drop it if the read says it fights "that evening". Motion: each chip floats y +-4 px over 3 s between entrances (no 4 s idle).

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
