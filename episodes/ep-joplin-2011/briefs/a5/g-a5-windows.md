# g-a5-windows · A5-S5 · STANDARD (Sonnet 5.5, high)

Open numbers: none. Open geometry: which window band is the fifth floor in the raw photo (NIST's printed Fig 3-10 marks it with a yellow oval that the raw image lacks).
Overlay, root transparent. **Host start = a5-s5 "fifth"@0.86**, duration 6.14 s (wav 6.40 + 0.60 exit).
Under it: `media/candidates/a5/a5-s5_c1_nist-5th-floor-south-fig3-10.jpg` (NIST Fig 3-10, West Tower south side, 936 x 585), mounted cover-fit 1920 wide: scale 2.0513, 1200 px tall, 60 px cropped top and bottom (computed, python).

## 0. Claim
On the fifth floor of the West Tower the impact-resistant windows mostly held; most regular windows broke.

## 1. Source
- C15: "The majority of the impact-resistant windows on the fifth floor (Behavioral Health Unit) of the West Tower of SJRMC remained intact, whereas most regular dual-pane insulated windows at SJRMC were broken" (Finding 18).
- Traced figure: NIST NCSTAR 3 Fig 3-10, "Intact windows on fifth floor of SJRMC's West Tower (south side)" (printed p. 98). Its yellow oval is the position of the band.

## 2. Datum, scale, orientation
Frame px of the mounted photo. My reading of the raw image (to confirm against the printed oval before drawing): the intact band is the left wing's row at raw y 300 to 340, frame y 555 to 637; the broken row below it is raw y 370 to 405, frame y 699 to 771.

## 3. Geometry
- Highlight: rounded rect, 3 px `#d8a13a` stroke, no fill, around the confirmed fifth-floor band of the left wing, frame x 0 to 820 (raw x 0 to 400), padded 8 px. Drawn on with strokeDashoffset (length ceil+1).
- Bracket: 3 px `#c0392b` line under the broken band below (frame y about 775), x 120 to 700.
- Chip: centred x 960, top 140 (above the facade bands, over the sky).
- Source line bottom-left. Nothing at x >= 1600, y >= 680; the highlight and bracket stop at x 820.

## 4. Must be true in the picture
1. The amber outline sits on the band NIST marks as the fifth floor in the printed Fig 3-10, within +-10 px of the oval's band; if the confirmed band differs from my reading, the printed figure wins and the builder reports it.
2. The band inside the outline shows intact glass on the frame; the bracketed band shows broken windows.
3. The chip says impact windows held, nothing about every window: "mostly" is the voice's, the chip never says "all".
4. No "Behavioral Health Unit" or floor-number label on the picture (not asked).

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| amber outline draws on (0.6 s) | a5-s5 "fifth"@0.86 |
| source line `NIST Finding 18` | a5-s5 "fifth"@0.86 |
| chip `IMPACT WINDOWS HELD` | a5-s5 "held."@3.30 |
| red bracket draws (0.5 s) | a5-s5 "regular"@4.84 |
| exit, everything | 6.40 to 7.00 |
Motion: the outline's glow breathes (stroke opacity 0.75 <-> 1, 1.2 s, finite repeats) from 1.5 to 6.4.

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
