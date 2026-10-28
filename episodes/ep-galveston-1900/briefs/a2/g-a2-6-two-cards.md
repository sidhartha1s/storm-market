# g-a2-6-two-cards · A2-S5 (whole) · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (paper card, chip, source line). Exemplars: `library/inhouse/quote-card.html` (quote typography on a card), official `physical-exit` (drop with momentum; use its drop curve for the entrances, not its exit).

## 0. Claim
The record gives the shut-out two different dates that will not line up: a Cuban meteorologist puts Belen's publishing ban in 1898; a letter Larson quotes, dated 28 August 1900, has Moore complaining of "independent observatories". The two cards refuse to stack: the date is in dispute.

## 1. Source
- Card 1: sources-cuba.md §2 (Rubiera, OnCuba 2015: in 1898 Belen "se le prohíbe dar a conocer públicamente sus pronósticos", SECONDARY, attributed); factcheck/a2-r1.md rows 28, 29 ("Cuban meteorologist"); a2-r2 row 3.
- Card 2: sources-cuba.md §2 (Econlib quoting Larson, Isaac's Storm: Moore "wrote to Gen. Thomas T. Eckert, president of Western Union", "On August 28"; quote "The United States Weather Bureau in Cuba has been greatly annoyed by independent observatories"); rows 30, 31; a2-r2 rows 5 to 8 ("AUG 28, 1900" confirmed, row 8).
- Source line extra: Pietruska fn 86, "Moore to Thomas T. Eckert, Sept. 20, 1900" (citation only, contents unseen; row 32).
- Chip "DECREE: DATE?": sources-cuba.md Conflicts 1 (1898 vs Aug 1900 vs Sept 20, 1900, unresolved).

## 2. Datum, scale, orientation
Full-frame designed desk seen from above. No scale. Desk ground: the canvas radial gradient plus a desk plane `#15202b` (full frame) with 6 faint grain lines `rgba(255,255,255,0.03)` 2 px across it, static. Paper cards per Shared rules.

## 3. Geometry (px; boxes before rotation)
- Card 1 rest: x 120 to 900, y 140 to 520 (780 x 380), rotation -3 deg, z above card 2. Padding 48 px. Text, top to bottom: "1898" Arial Black 900 64 px `#2a2622`; "Rubiera: Belen barred from publishing forecasts" Georgia 34 px `#2a2622`, max width 684 (two lines); tag "José Rubiera, OnCuba, 2015" Arial 700 20 px `#6b6257` tracking 2.
- Card 2 rest: x 820 to 1580, y 470 to 900 (760 x 430), rotation +4 deg, under card 1 where they meet (card 1 covers card 2's top-left corner, about 80 x 50 px). Padding 100 px left (so no text sits under card 1), 48 px elsewhere. Text: "Aug 28, 1900" Arial Black 900 64 px `#2a2622`; "Larson, Isaac's Storm: Moore to Western Union" Arial 700 26 px `#2a2622`, max width 612; quote "“greatly annoyed by independent observatories”" Georgia italic 32 px `#2a2622` (the reading target), max width 612; tag "As quoted by Erik Larson" Arial 700 20 px `#6b6257`.
- Chip "DECREE: DATE?" (Shared rules chip, no tag): left 1060, top 160 (clear of both cards and of the source line).
- Source line (top-left, two lines): "José Rubiera, OnCuba, 2015 · Erik Larson, Isaac's Storm (via Econlib) · Also: Moore to Eckert, Sept. 20, 1900 (Pietruska, 2016; citation only)". It sits above card 1 (card 1 top 140; the source box must end above y 130; if it wraps to three lines, move card 1 and card 2 down by the overflow and say so).
- Tiers: 64 (dates), 34 / 32 / 26 (bodies), 20 / 19 (tags, source).

## 4. Must be true in the picture
1. Card 1 lands first and stays on top; card 2 never covers any text on card 1, and card 1 never covers text on card 2, in any frame including the drop and the bump.
2. The two cards never come to rest stacked (aligned edges): they rest offset and at different angles.
3. The quote on card 2 is exactly "greatly annoyed by independent observatories" inside curly quotes, with "As quoted by Erik Larson" under it.
4. No "Sept. 20" on either card: that letter is on the source line only (contents unseen).
5. Nothing in x >= 1600, y >= 680 (card 2 right edge 1580 before rotation; check the rotated corner stays left of 1600).

## 5. Text and cues (a2-s5.words.json)
- 0.00: desk on; source line in. Desk plane drifts (scale 1.00 to 1.03 over the whole comp, ease none).
- 1.36 ("Cuban" 1.36): card 1 shadow appears on the desk (autoAlpha 0 to 0.5), the card falls in from above (y -700 to 0, rotation -10 to -3, 0.55 s, power3.in then a 0.15 s settle) landing at 3.70 ("1898," 3.70) /* 1898 @3.70 */, with "1898" visible; the body line in at 4.96 ("Belen" 4.96); tag at 6.74 ("forecasts." 6.74).
- 11.32 ("Willis" 11.32) /* MOORE LETTER @11.32 */: card 2 drops from above toward card 1's centre (rotation 8 deg), hits card 1's lower-right edge at 11.80 (card 1 jolts 10 px and back, rotation -3 to -5 to -3, 0.35 s), and skids to its rest, 11.80 to 12.30, power3.out. "Aug 28, 1900" visible as it lands.
- 12.56 ("Western" 12.56): card 2's Larson line in.
- 12.86 ("Union." 12.86) /* DATE? @12.86 */: chip DECREE: DATE? enters.
- 15.12 ("greatly" 15.12) /* GREATLY ANNOYED @15.12 */: quote in, word by word on the spoken words (greatly 15.12, annoyed 15.40, by 15.88, independent 16.12, observatories 16.64); tag at 16.64.
- 17.672: end.
- Host: A2-S5 0.00 to 17.672.

## Motion for the whole window
Desk drift for the whole comp; card drops, bump; cards and chip float y +-4 px from landing. Longest gap between beats 6.74 to 11.32, covered by the desk drift and the card float.

## Exit
Cut to the A2-S6 map: the whole root fades to 0 over the last 0.35 s (17.322 to 17.672).

## Footage under it
None: full-frame designed (coverage 100 %).
