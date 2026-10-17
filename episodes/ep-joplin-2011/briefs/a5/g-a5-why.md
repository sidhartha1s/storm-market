# g-a5-why · A5-S10 · STANDARD (Sonnet 5.5, high)

Open numbers: none. Open assets: the two page images are not sourced yet (not in `media/candidates/a5/`): (1) NIST NCSTAR 3 Finding 47 as printed (Exec Summary E.4.2 or Sec. 5.1, same wording), (2) the NWS Assessment page with Finding 2d's "elderly, infirm, or disabled" sentence. Both are public-domain government pages; crop to the paragraph, no running header needed.
Full frame: the page images are this comp's own `<img>` layers on its ground, not footage under it. **Host start = a5-s10 0.00**, duration 18.36 s (wav 17.76 + 0.60).

## 0. Claim
NIST names three possible reasons and does not choose among them; the NWS adds that elderly, infirm or disabled people need more time or help to reach shelter.

## 1. Source
- C31: "Factors that may have contributed to this outcome include a lack of information flow to these individuals, a lack of supportive social networks among individuals, or inability of an individual to withstand or recover from tornado-induced trauma" (Finding 47).
- C37: "a significant number of fatalities in Joplin occurred in vulnerable populations such as the elderly, infirm, or disabled. These populations typically require additional time and/or assistance to get to the best available shelter" (NWS Assessment, Finding #2d).

## 2. Datum, scale, orientation
Page panel left: x 120 to 1120, the page image scaled to that width, a 1 px `rgba(255,255,255,.14)` edge, slight tilt 0 (no rotation: underlines must sit on the text lines). Chip column right: x 1200 to 1560, chips at top 300, 410, 520.

## 3. Geometry
- Underlines: hand-drawn stroke (catalog `hw-underline`), 5 px `#d8a13a`, under the exact words of each factor as they sit on the page image; the builder measures each line's baseline on the mounted image (+-6 px).
- Three chips stacked in the right column, each stays once in (a build, not a swap).
- On the swap, the NIST page and its chips slide out left (x -980) and the NWS page slides in from the right to the same panel position; chips stay off for the NWS part.
- Source line bottom-left, swapped with the pages.
- Nothing at x >= 1600, y >= 680; the chip column ends at y 600.

## 4. Must be true in the picture
1. Each underline sits under the words that match its chip: info flow -> `LESS WORD`, social networks -> `LESS HELP`, withstand or recover -> `HARDER TO RECOVER`.
2. Only Finding 47's three factors are underlined on the NIST page, nothing else.
3. The page text is legible on the frame at 1080p (if the crop is too small to read, push in on the paragraph; the underline must stay on its words).
4. On the NWS page only "elderly, infirm, or disabled" is underlined.

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| NIST page in, slow push 1.00 -> 1.03 | a5-s10 0.00 |
| source line `NIST Finding 47` | a5-s10 0.00 |
| underline 1 (information flow) | a5-s10 "warning"@4.50 |
| chip `LESS WORD` | a5-s10 "reached"@5.30 |
| underline 2 (social networks) | a5-s10 "fewer"@7.74 |
| chip `LESS HELP` | a5-s10 "help,"@8.78 |
| underline 3 (withstand or recover) | a5-s10 "take"@10.86 |
| chip `HARDER TO RECOVER` | a5-s10 "recover"@11.72 |
| swap to the NWS page; source line becomes `NWS Assessment, Finding 2d` | a5-s10 "And"@13.20 |
| underline `elderly, infirm, or disabled` | a5-s10 "disabled"@13.78 |
| exit: fade-through | 17.76 to 18.36 |
Motion 0 to 4.5: the page push runs the whole NIST span, so no 4 s still before the first underline.

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
