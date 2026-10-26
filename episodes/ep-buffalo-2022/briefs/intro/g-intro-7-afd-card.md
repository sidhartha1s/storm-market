# g-intro-7-afd-card · I1-S4 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/bulletin-typewriter.html` (verbatim bulletin typed on the voice, blinking cursor, onUpdate writing one leaf span). Change from the exemplar: retint from CRT green to the channel palette below (an episode uses 10 palette colours or fewer; the greens are not in tokens.md), rename `#root` and every `bultype-` id, and move its source label off the bottom-right corner (the presenter circle sits there) and inside the 54 px margin.

## 0. What this graphic claims
Five days before the blizzard, at 4:10 AM on Sunday 18 Dec 2022, the National Weather Service office in Buffalo was already writing that "a very large and powerful storm system" would hit the eastern half of the country later that week. The forecast was early; the episode's question is why it still ended with so many people found outside.

## 1. SOURCE
- NWS Buffalo Area Forecast Discussion, product FXUS61 KBUF 180910 (AFDBUF), issued 410 AM EST Sun Dec 18 2022, IEM archive (`research/nws.md` rows 1.8 and 1.10, PRIMARY): https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=AFDBUF&sdate=2022-12-15T00:00Z&edate=2022-12-20T00:00Z&fmt=text&limit=100
- Verbatim product text (re-fetched by the brief writer 26 Oct 26, .SYNOPSIS section, line breaks are the product's):
  ```
  Area Forecast Discussion
  National Weather Service Buffalo NY
  410 AM EST Sun Dec 18 2022
  ...
  benign weather can be expected for Tuesday and Wednesday...a very
  large and powerful storm system will impact the bulk of the eastern
  half of the country later in the week.
  ```
- "5 DAYS OUT": 4:10 AM Sun 18 Dec to the warning's 7 AM Fri 23 Dec start = about 5 days 3 hours (`research/nws.md` 1.2, 1.8, 1.10).
- Fact check: `factcheck/intro-r3.md` row 31 (card, product id and time, chip, source CONFIRMED; "show the sentence through 'later in the week' on the card so the eastern-half scope is visible").

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed graphic. Ground: channel radial gradient (tokens.md "Canvas") on a child layer `af-ground` (it fades with the card at the end, toward the Act 1 blackout), on from frame 0. No scale. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Chip "5 DAYS OUT": Arial Black `font-weight:900` 52 px `#e8c56a` (Amber 2), left 200, top 110 (glyph box about 110 to 166). No card behind it (it sits on the dark ground).
- Panel `af-panel`: x 200 to 1500, y 210 to 790, radius 28, fill `linear-gradient(180deg, #15202b, #0b1016)`, 1 px `rgba(255,255,255,.14)` border.
- Header, Courier New 700 26 px `#93a3b2`, letter-spacing 2, left 260, line pitch 40, tops 250, 290, 330: "Area Forecast Discussion" / "National Weather Service Buffalo NY" / "410 AM EST Sun Dec 18 2022". (Mixed case exactly as the product; do not upper-case.)
- Divider: 1 px `rgba(255,255,255,.14)`, x 260 to 1440, y 390.
- Body, Courier New 700 36 px `#dfe7ee`, letter-spacing 1, left 260, line pitch 64, tops 430, 494, 558. Fixed line breaks (each line under 1180 px at about 21.6 px a character):
  - L1 `...a very large and powerful storm system` (41 chars, about 886 px)
  - L2 `will impact the bulk of the eastern half` (40 chars, about 864 px)
  - L3 `of the country later in the week.` (33 chars, about 713 px)
  The leading "..." is the product's own punctuation (it follows "Tuesday and Wednesday").
- Cursor: 20 x 40 px block `#dfe7ee` at the end of the typed text.
- Product id: "FXUS61 KBUF 180910", Courier New 400 19 px `#93a3b2`, left 260, top 740.
- Highlight rule: 4 px `#d8a13a` under "very large and powerful" on L1 (x about 368 to 757 for the four words, compute from the glyph boxes), y 476.
- Source line: "NWS Buffalo Area Forecast Discussion, 18 Dec 2022, IEM archive", Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`.
- Type tiers: 52 (big), 26 to 36 (mid), 19 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. The body text is the product's words character for character (only the line breaks differ), from "...a very" through "later in the week."
2. The header shows 410 AM EST Sun Dec 18 2022 and Buffalo NY; the chip says 5 DAYS OUT, consistent with that date (Sun 18 to Fri 23 Dec).
3. Typing finishes each line no later than the voice finishes the matching words (the voice paraphrases "would hit ... later that week"; the card keeps the product's "will impact ... later in the week").
4. The card's text never touches the panel edge (whole lines, no cut words at either side in any frame).
5. The end fades everything, ground included, to black by the host end: a hand-off to the Act 1 blackout, not a hard cut.
6. Corner x >= 1600, y >= 680 empty.

## 5. PANEL TEXT (exact) and CUES (seconds from I1-S4 start, `audio/i1-s4.words.json`)
Strings: `5 DAYS OUT` · header lines and body lines exactly as section 3 · `FXUS61 KBUF 180910` · `NWS Buffalo Area Forecast Discussion, 18 Dec 2022, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Five" @0.00 | ground on at frame 0; chip "5 DAYS OUT" `fromTo(autoAlpha 0, scale 1.2 -> 1, 0.4, power4.out, transformOrigin left center)` from 0.05 |
| 0.44 | "out," @0.44 | panel in `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`; source line in; cursor starts blinking (`steps(1)` yoyo, finite repeats, to the end) |
| 1.32 | "Sunday" @1.32 | header types line by line, ease none: line 1 1.32 to 1.70, line 2 1.70 to 2.10, line 3 2.10 to 2.70 (it carries "Sun Dec 18 2022" as the voice says "the Sunday before Christmas," @1.32 to 1.92) |
| 2.82 | "Buffalo's" @2.82 | header line 2 brightens to `#f2f5f8`, 0.3 s; divider `scaleX 0 -> 1, 0.4` |
| 5.02 to 6.90 | "a very large and powerful storm system" @5.02 to 6.76 | L1 types, ease none |
| 7.12 to 8.40 | "would hit the eastern half" @7.12 to 7.88 | L2 types |
| 8.40 to 9.40 | "of the country later that week." @8.24 to 9.42 | L3 types; product id in at 9.40 |
| 9.4 to 10.5 | gap | cursor blinks; panel drifts `scale 1 -> 1.02` over 9.4 to 13.9, ease none (continuous) |
| 10.86 | "forecast" @10.86 | amber rule under "very large and powerful" `fromTo(scaleX 0 -> 1, 0.5, power2.out, transformOrigin left center)` |
| 11.62 | "early" @11.62 | chip pulse `scale 1 -> 1.08 -> 1, 0.5` |
| 13.90 to 15.50 | "found outside in the snow?" @13.48 to 14.88 | slow fade toward black: chip, panel, text, source and `af-ground` `to(autoAlpha 0, 1.6, power1.in)` |
Comp duration 15.6 s. Spoken time in a comment at each tween. Typing writes one leaf span per line from the timeline's onUpdate (as the exemplar); never text written in onStart/onComplete/`tl.call`.

## 6. CONTRACT
One file `compositions/g-intro-7-afd-card.html`, root `<div id="g-intro-7-afd-card-root" data-composition-id="g-intro-7-afd-card" data-width="1920" data-height="1080">`. PAUSED timeline at `window.__timelines["g-intro-7-afd-card"]`. Ids prefixed `af-`, classes `af-*`. Start-hidden in CSS too. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-7-afd-card`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-7-afd-card`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 3: frame 0 shows the ground with the chip about to enter (not black).

## 8. RECEIPT
As the template.
