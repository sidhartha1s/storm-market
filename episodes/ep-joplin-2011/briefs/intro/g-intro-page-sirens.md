# BRIEF · g-intro-page-sirens · "people said the sirens went off all the time" · STANDARD (Sonnet 5.5, high) · PAGE UNDERLINE BASE

Episode ep-joplin-2011, segment I1-S5. Full-frame MG on the channel ground. Host from i1-s5 "But" 0.00 to the wav end 6.20; it comes in
on a cut from `g-intro-strip`. Paul speaks the line; no actor's voice.
**This comp is the PAGE UNDERLINE base.** `g-intro-page-survivors`, `g-a1-gutter`, `g-a1-numb` (page half), `g-a1-finding31` and
`g-a1-bubble-page` copy its card, shadow, underline bar and push. Send it alone for a full-size read before any copy (template 7a).
Exemplar: `library/official/vox-annotate.html` (annotation drawn on the voice).
Open numbers: none.

## 0. What this graphic claims
Residents told the NWS that they "hear sirens all the time and [sirens] go off for dark clouds" (S17). The words are theirs, on the
government's own page; the underline follows Paul's voice.

## 1. SOURCE
- S17 "Many noted that they "hear sirens all the time and [sirens] go off for dark clouds," ..." NWS Assessment, Finding #2b.
- Page: `media/candidates/intro/i1-s5_c1_nws-assessment-p13-sirens-quote.png` (NWS Assessment PDF p13, printed page 7; US government, public domain), 1105 × 1430 px.
  The quote line is the page's native text band y 663 to 683 (pixel scan, 17 Oct 26); "hear sirens all the time" spans native x 412 to 611,
  "and [sirens] go off for dark clouds" x 620 to 916.

## 2. DATUM, SCALE, ORIENTATION (the PAGE UNDERLINE base values; copies change only the crop and the phrase boxes)
- Crop: native x 118 to 988, y 596 to 746 (the paragraph's five lines). Scale 1.85. Card centred x 960, centre y 500.
- Computed (python, 17 Oct 26): card 1609.5 × 277.5 px at left 155.2, top 361.2 (right 1764.8, bottom 638.8). The quote line's text band lands at y 485.2 to 522.2.
- Push: uniform scale 1.00 → 1.04 about (960, 500) over the host; at 1.04 the card spans x 123.1 to 1796.9, y 355.7 to 644.3, inside the text-safe frame.
- Presenter circle: may stay on (card bottom < 680).

## 3. GEOMETRY
- Ground: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`, on from frame 0.
- Card: the cropped page image (an `<img>` in a clip box, object-position computed from the crop), radius 6, `box-shadow: 0 24px 60px rgba(0,0,0,.55)`.
  The paper stays as printed (no tint). A soft dark wash `rgba(4,7,12,.35)` over the card's lines other than the quote line, faded in on the first underline, so the quote line is the brightest.
- Underline bar: 6 px tall, Danger red 2 `#e74c3c`, radius 3, 4 px under the quote band (y 529.6 at push 1.00, computed), drawn with
  `scaleX 0 → 1`, `transformOrigin: "left center"`. It sits inside the card group so it moves with the push.
  Bar 1 x 699.1 to 1067.3, bar 2 x 1084.0 to 1631.6 (computed).
- Source line: x 96, baseline 1010, Arial 700 20 `#c8d3e0`.
- Entrance: card `fromTo(y:40, autoAlpha 0 → 0, 1, 0.5, power3.out)`. End: the scene cuts (no element vanishes alone).

## 4. MUST BE TRUE IN THE PICTURE
1. The bars sit under exactly "hear sirens all the time" and "and [sirens] go off for dark clouds" (±6 px at both ends), never under "Many noted that they" or "they".
2. No bar crosses a glyph: 4 px clear under the descenders of the quote line.
3. The page reads as printed; no word is retyped on top of it.
4. The card stays inside x 96 to 1824 through the push.

## 5. PANEL TEXT (exact) and CUES (i1-s5)
| element | text | cue |
|---|---|---|
| card in; push starts (ease none, to the host end) | | "But" 0.00 |
| source line | "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b" (S17) | "But" 0.00 + 0.3 |
| bar 1 draws (to "time," 4.08 + 0.2) | | "sirens" 2.86 |
| wash over the other lines fades in (0.4 s) | | "sirens" 2.86 |
| bar 2 draws (0.6 s) | | "even" 4.60 |
| hold | | to 6.20; the push carries motion; cut on the host end |

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (item 6: crop, card and bar positions by script from the native boxes above), §8.
