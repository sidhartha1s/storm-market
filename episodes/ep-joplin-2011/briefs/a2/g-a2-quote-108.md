# g-a2-quote-108 · STANDARD (Sonnet 5.5, high) · act a2, segment a2-s4

**Open numbers:** none.

**Under it:** a NIST ground photograph (credit line checked at sourcing; file named at dispatch), full frame on a lower
track for the whole host, over g-a2-countdown. The card is an overlay: footage must span the whole host window.
**Host:** a2-s4 narration start to a2-s4 end plus the gap before a2-s5 (at least 1.0 s after "went" lands).
**Cue clock:** `segment offset + word start`; offset = a2-s4 narration `data-start` minus host `data-start`, read at dispatch.
Corner circle stays on: nothing enters x >= 1600, y >= 680.

## 0. What this graphic claims
After the first siren there was little to see, and at least one survivor went back to dinner: the first siren did not
look like a threat from the doorstep.

## 1. SOURCE (confirmed rows, quoted)
- E34 (NIST Sec. 4.7.1.2, NIST Interview 108): "The tornado sirens went off once, we walked outside and you couldn't really, didn't really see nothing then, and we went back in and finished eating."
- E7 (NIST E.3): "there were few environmental clues to suggest that severe weather was imminent."

## 2. DATUM, SCALE, ORIENTATION
No scale. Fixed px layout on 1920 x 1080; all text at least 96 px from left/right and 54 px from top/bottom.

## 3. GEOMETRY
- Quote card: `.quotecard.glasscard` (tokens.md glass surface, radius 28, no shadow), x 160 to 1520, y 600 to 960, padding 40 x 56.
- Quote: Georgia italic 40 px #f2f5f8, three pre-authored lines (P1 to P3 below), line height 1.3.
- Attribution: Arial 700 22 px #d8a13a tracking 2, under the quote: "A survivor · NIST Interview 108".
- Chip: glass chip top-left, left 96, top 54, Arial Black 900 52 px #f2f5f8 tracking 2: "NOTHING TO SEE".
- Source line: glass pill top-right, right 96, top 54, Arial 700 20 px #c8d3e0: "NIST E.3: few environmental clues".
- Motion: card in y 40 to 0 + autoAlpha 0.5 s power3.out; each quote line autoAlpha 0 to 1 with y 16 to 0, 0.4 s; the card floats y 0 to -6 to 0 (sine, finite repeat) through the hold; exit slide x 0 to 980 + autoAlpha 0, 0.6 s power3.in in the host's last 0.6 s; chip and source line exit with it.

## 4. MUST BE TRUE IN THE PICTURE
1. The quote is E34 word for word, including "didn't really see nothing"; no word fixed or trimmed.
2. The attribution names NIST Interview 108 and no name, age or place (none is in the source).
3. The photograph under the card is a NIST ground photograph per its `provenance.csv` row; no face sits under the card text.
4. Nothing enters x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s4 · "see." · 2.76 | chip "NOTHING TO SEE"; source line "NIST E.3: few environmental clues" |
| a2-s4 · "One" · 3.76 | card in with attribution "A survivor · NIST Interview 108" |
| a2-s4 · "walked" · 5.36 | P1 "The tornado sirens went off once, we walked outside" |
| a2-s4 · "didn't" · 7.00 | P2 "and you couldn't really, didn't really see nothing then," |
| a2-s4 · "went" · 8.14 | P3 "and we went back in and finished eating." |
| host end minus 0.6 s | exit |

## 6 to 8
As `references/mg-brief-template.md` §6, §7, §7a (all seven; item 7: one frame over the real photograph), §8.
File `compositions/g-a2-quote-108.html`, timeline `window.__timelines["g-a2-quote-108"]`, root id `a2q-root`.
