# g-a1-3-quote · A1-S2 (whole) · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/quote-card.html` (glass quote card), official `testimonial-proof-card` (per-line reveal; restyle to the glass card), chip from `compositions/g-intro-2-cline1891.html`.

## 0. Claim
Cline's full 1891 sentence, in his words: people who feared a damaging storm were unacquainted with the conditions; the fear was "an absurd delusion" that came from the imagination, not from reasoning.

## 1. Source
- Words typed from the scan itself (column 3, page 5, read at 3x on 28 Oct 26; `_list.md` change 2). Commons transcription: factcheck/a1-r1.md row 8, factcheck/a1-r2.md row 3; sources-cline.md §1. The scan and the transcription differ in four small words; the scan wins on screen.
- HOLD (act A1-S2): this comp does not ship until one human reads the scan and confirms the text below.

## 2. Datum, scale, orientation
Overlay comp, transparent root, over g-a1-1-page at its K2 framing (column 3 at screen x 120 to 940, lit lines y 449 to 643). This comp owns the right half: x 1000 to 1824. No scale.

## 3. Geometry (px)
- Quote card: glass (tokens.md), `left:1000px; top:140px; width:824px`, padding 36px 40px, radius 28, box-sizing border-box, bottom ≤ 510.
- Quote text, Georgia italic 28 px, line-height 40 px, unlit colour `#93a3b2`, lit colour `#f2f5f8`; about 6 lines. Pre-author it as six phrase spans (exact text, scan wording, keep the semicolon off the end):
  - P1 "The opinion held by some,"
  - P2 "who are unacquainted with the actual conditions of things,"
  - P3 "that Galveston will at some time be seriously damaged by some such disturbance,"
  - P4 "is simply an absurd delusion" (the words "absurd delusion" carry a 3 px `#d0121f` underline that draws when lit)
  - P5 "and can only have its origin in the imagination"
  - P6 "and not from reasoning"
- Attribution under the text, 16 px gap: "Isaac Cline · Galveston Daily News, July 16, 1891" Arial 700 20 px `#d8a13a` letter-spacing 2.
- Chip zone under the card: `left:1000px; top:560px`.
  - Chip A "ABSURD DELUSION": Arial Black 900 56 px `#f2f5f8`, one line, about 640 wide, padding 22px 36px.
  - Chip B "IMAGINATION," / "NOT REASONING": same type, two lines (line-height 1.1), about 560 wide, bottom ≈ 727, right edge ≤ 1580.
- Tiers: 56 / 28 / 20.

## 4. Must be true in the picture
1. The card's text is exactly the six spans above, in order, no quote marks, no ellipsis (the whole sentence is shown, as the Picture line asks).
2. A phrase is lit only on or after the spoken words that carry it (cues below); the unspoken P3 lights with "fear" because "that fear" stands for it.
3. Card and chips stay right of x 1000 (column 3 on the page ends at 940) and out of x >= 1600, y >= 680 (chip B's right edge ≤ 1580).
4. One chip at a time: A has left before B enters.
5. No text of this comp is over the page's lit lines.

## 5. Text and cues (a1-s2.words.json, segment 8.766 s)
- 0.58 ("people"): card in (fromTo x:60, autoAlpha 0 → x 0, autoAlpha 1, 0.6, power3.out), all text unlit; attribution in with it. /* CARD @0.58 */
- 1.06 ("held"): P1 lit (colour tween 0.35 s). /* HELD @1.06 */
- 1.46 ("fear"): P3 lit.
- 2.04 ("unacquainted"): P2 lit. /* UNACQUAINTED @2.04 */
- 4.80 ("Such"): P4 lit, red underline draws under "absurd delusion" (scaleX 0 → 1, 0.5 s); chip A in. /* ABSURD @4.80 */
- 5.94 ("could"): P5 lit.
- 6.30 to 6.70: chip A out (on-diagram exit `y:-24`, 0.4 s).
- 6.72 ("imagination,"): chip B in, line "IMAGINATION," first, "NOT REASONING" at 7.92 ("not") (y 16 → 0, autoAlpha, 0.35 s). /* IMAGINATION @6.72 */
- 7.74 ("and"): P6 lit. 8.28 ("reasoning."): P6 brightens to `#f5d98b` for 0.4 s and back.
- Host: A1-S2 0.58 to 8.766 plus 0.6 s if the edit leaves a gap; else the exit is anchored inside 8.766.

## Motion for the whole window
Card and chip drift y ±4 px; phrase lights land about every 1 to 2 s; nothing idles 4 s.

## Exit
Card and chip B slide out together `to x:980, autoAlpha 0, 0.6, power3.in`, ending on the host end (S3 opens on a cut).

## Footage under it
g-a1-1-page (column 3, sentence lit) for the whole window.
