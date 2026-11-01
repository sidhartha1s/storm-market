# g-intro-1-date: date/place popfig on Paul's first clip (H1-S1)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/snippets/cards.css` `.popfig` / `.pf-big` / `.pf-sub` (copy the values into the comp; do not reuse the class names, index.html may use them) and the popfig half of `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`.
Sits over: `ins-paul-1`, Paul's full-frame Flow clip 1 (frame one of the video). PROVISIONAL hook: a different hook shape redoes this graphic.

## 0. Claim
The 108 mph Newark gust happened on Saturday, 25 November 1950, in Newark, New Jersey. The popfig fixes when and where; Paul's line carries the rest.

## 1. Source
- `research/nws-facts.md` §1 row "Newark gust, strongest ever there (25 Nov)" (PHI https://www.weather.gov/phi/hist_phi, Nov 25 entry: "The wind at Newark, NJ, gusted to 108 mph"); `factcheck/intro-r2.md` row 3 (25 Nov 1950 was a Saturday, computed; Thanksgiving was Thursday 23 Nov).

## 2. Datum, scale, orientation
Overlay text only, no drawn geometry. Frame 1920 x 1080. Text-safe margin 96 px left/right, 54 px top/bottom.

## 3. Geometry (px, 1920 x 1080)
- Big line "NOV 25, 1950": AbrilFig 150 px, `#d0121f`, letter-spacing 0.04em, the `.pf-big` text-shadow from cards.css. Centred on x = 960. Baseline block top at y = 640 (not the default 38 %: the default sits on Paul's face in a head-and-shoulders framing). Measured width at 150 px is about 1000 px, so it spans about x 460 to 1460; must stay inside x 96 to 1824.
- Sub line "SATURDAY · NEWARK, NEW JERSEY": Arial 700, 34 px, `#e8e3d8` with the `.pf-sub` shadow, centred, 12 px under the big line (top about y 812).
- Keep clear of the Flow logo patch centred at (1740, 900), 96 px wide: nothing right of x 1680 below y 840.
- If the frame read shows Paul's chin or mouth under the big line at y 640, move the whole block down in 20 px steps, never above y 600 and never below a sub-line bottom of 1010.

## 4. Must be true in the picture
1. Exactly two text lines; the big line reads "NOV 25, 1950" and nothing else (12 characters, 3 words).
2. Paul's eyes and mouth are never covered by any glyph in any frame.
3. The popfig is fully on before Paul finishes saying "Jersey".
4. No other graphic, chip or number appears on Paul's clip ("108 MPH" and "WINTER STORM" were moved/dropped by the section rule in `_list.md`).

## 5. Panel text (exact) and cues
Text: `NOV 25, 1950` · `SATURDAY · NEWARK, NEW JERSEY`
Cues from `audio/h1-s1.words.json` (seconds from the segment start). CAUTION: H1-S1 is Paul on camera; the clip's own audio replaces the TTS. When `ins-paul-1` exists, re-cue to its transcript (same words) and keep the comments.
- 0.28 "Newark," : big line in (`fromTo` autoAlpha 0 to 1, scale 1.25 to 1, 0.45 s, back.out(1.6)). `/* NEWARK @0.28 */`
- 0.82 "Jersey." : sub line in (`fromTo` autoAlpha 0, y 18 to 0, 0.4 s, power3.out). `/* JERSEY @0.82 */`
- 0.73 to 4.40: both lines float y 0 to -10 px, sine.inOut, 2 finite repeats yoyo (motion every second of the hold).
- 4.40 to 5.00: exit (`to` autoAlpha 0, y -40, scale 0.96, 0.6 s, power3.in). Out before "winter storm" (5.56) so the contradiction lands on Paul alone. `/* EXIT ends @5.00, before WINTER @5.56 */`
Host: data-start = clip start + 0.28 (first mark), duration 4.72 s. Root `id="g-intro-1-date-root"`, transparent.

## 6-8
Contract, tools, done line and receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 7: composite one frame at clip time 2.0 s over `ins-paul-1`; the label names a place and date, so the clip under it must be Paul's clip (not stock).
Must not: CSS @keyframes, `id="root"`, a glass card behind the popfig (popfig is bare Abril with its shadow by rule).
