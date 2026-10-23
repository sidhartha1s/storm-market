# BRIEF · g-a1-finding31 · "the record: no false-alarm problem with the sirens" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S6. The host runs from a1-s6 0.00 to the wav end 12.96. It is full-frame (the page on the channel ground),
entered on a cut from Paul's full-frame clip A1-S5. `g-a1-strip-warnings` follows on a cut.
Base: PAGE UNDERLINE (the intro's I1-S5 base, if built). Exemplar `library/official/vox-annotate.html`.
Open numbers: none.

## 0. What this graphic claims
NIST checked the record and found no evidence of high false-alarm rates for Joplin's outdoor sirens, despite public perception (S1).
A siren false alarm is a sounding with no severe weather in Joplin (S15). The sentence itself is the graphic.

## 1. SOURCE
- S1 "Despite public perception, no evidence was found of high false-alarm rates for Joplin's outdoor siren system." NIST NCSTAR 3, E.4.2 Finding 31.
- Page image: `media/candidates/a1/a1-s6_c1_nist-exec-summary-finding31.jpg` (NCSTAR 3 Executive Summary p iii, PDF p54). It holds Findings 30, 31 and 32.

## 2. DATUM, SCALE, ORIENTATION
- Ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` from frame 0.
- Page box x 300 to 1560, y 200 to 940. **Crop to Finding 31 only**: Finding 30 on the same page prints "78 percent (14 out of 18)",
  which A1-S7 reveals 13 s later. Choose the crop so the sentence's capital letters are at least 28 px tall on screen.
- Chip zone top centre x 960, y 96 to 166. Source line x 96, baseline 1010. Nothing enters x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- Page: a 1 px `rgba(255,255,255,.14)` edge and a soft shadow (0 20px 60px rgba(0,0,0,.5)).
- Underline: 6 px Amber 1 `#d8a13a` bars, 6 px below the baseline, ±4 px glyph to glyph, in three strokes that follow the voice:
  - S1 "Despite public perception,"
  - S2 "no evidence was found"
  - S3 "of high false-alarm rates for Joplin's outdoor siren system." (one bar per line if it wraps, in reading order)
- Chip: glass chip, "NO FALSE-ALARM PROBLEM" in Arial Black 900 52 `#f2f5f8`, tracking 2.
- Source line: "NIST NCSTAR 3 · Finding 31", Arial 700 20 `#c8d3e0`.

## 4. MUST BE TRUE IN THE PICTURE
1. No part of Finding 30 (the 78 percent, the 14 out of 18) is visible in any frame.
2. The three strokes underline only the Finding 31 sentence, in voice order.
3. The chip does not cover the page text.

## 5. PANEL TEXT (exact) and CUES (a1-s6)
| element | text | cue |
|---|---|---|
| ground + page in (y 30 → 0, autoAlpha, 0.6 s) + source line | "NIST NCSTAR 3 · Finding 31" | frame 0. The source line rises on "record." 1.60 |
| stroke 1 | | "Despite" 2.68 to "believed," 3.24 + 0.4 s |
| stroke 2 | | "no" 5.34 to "evidence" 5.74 + 0.4 s |
| stroke 3 | | "Joplin's" 6.46 to "problem." 8.74 + 0.3 s |
| chip | "NO FALSE-ALARM PROBLEM" (S1) | "problem." 8.74 |
| page slow push (scale 1.00 to 1.03, `to()`) | | 0.60 to 12.96, continuous |
| exit: page and chip fade through to the ground | | 12.36 to 12.96 |

"Then where did all the false alarms people remember come from?" (9.66 to 12.14) holds on the finished page with the push running.
Known gate issue: page crops may flag flat-type or undesigned (`learnings/mg.md` 12 Oct 26). Report it, do not pad.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8.
