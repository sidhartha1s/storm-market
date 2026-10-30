# g-a3-5-steele-quote · A3-S3 10.80-17.50 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/quote-card.html` (full-frame beige cite card over dark ground, verbatim quote revealed phrase by phrase). Rename every id and `#root`.

## 0. What this graphic claims
Her mother, Wanda Brown Steele, said: "I want to get to the bottom of why the city was unable to help." Verbatim, attributed.

## 1. SOURCE
- Quote and attribution: `research/deaths.md` section 4 (CBS/CNN wire, updated 28 Dec 2022, SECONDARY); relation: `factcheck/a3-r1.md` "New evidence" ("Wanda Brown Steele -- Taylor's mother -- told CNN.").
- URL: https://www.cbsnews.com/miami/news/woman-in-buffalo-found-dead-in-her-car-after-getting-trapped-by-snow-family-says/

## 2. DATUM, SCALE, ORIENTATION
Full-frame: channel radial gradient ground (layer `sq-ground`, on from frame 0), beige cite card centred. Corner x >= 1600, y >= 680 empty (card ends left of x 1600 or above y 680; see geometry).

## 3. GEOMETRY (px)
- Card `sq-card`: x 260-1500 (1240 wide), y 250-690, radius 20, fill `rgba(232,222,200,.90)` (tokens.md beige cite card), no border.
- Quote, Georgia 400 52 px `#2a2622`, line-height 72, left 340, width 1080, tops 320 / 392 / 464, fixed breaks:
  - L1 `“I want to get to the bottom`
  - L2 `of why the city`
  - L3 `was unable to help.”`
  (curly quotes; each line under 1080 px at about 26 px per character)
- Attribution, Arial 700 26 px `#6b6257` tracking 3, left 340, top 580: "WANDA BROWN STEELE · HER MOTHER".
- Source line, Arial 400 19 px `#c8d3e0` on the dark ground, `left:96px; bottom:54px`: "Wanda Brown Steele, to CNN, via CBS News, Dec 2022".
- Card right edge x 1500 and bottom y 690: clear of the circle corner.
- Type tiers: 52, 26, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. The quote is verbatim, word for word, with nothing added, cut or reordered.
2. Each line appears on its spoken words (below), never ahead of the voice.
3. The attribution names her as her mother and is on screen before the quote starts.
4. Dark text only on the beige card; no bare text on the dark ground except the source line.

## 5. PANEL TEXT (exact) and CUES (segment seconds, `audio/a3-s3.words.json`; host starts at 10.80, comp-local = t - 10.80)
Strings: `“I want to get to the bottom` · `of why the city` · `was unable to help.”` · `WANDA BROWN STEELE · HER MOTHER` · `Wanda Brown Steele, to CNN, via CBS News, Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 10.80 | (before "Her mother" @10.82) | ground on from frame 0 |
| 10.92 | "mother," @10.92 | card `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)` |
| 11.70 | "Wanda Brown Steele" @11.70 | attribution `fromTo(autoAlpha 0, x:-20 -> 0, 0.4, power2.out)`; source line in |
| 13.78 | "I want" @13.78 | L1 in `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power3.out)` |
| 14.86 | "of why the city" @14.86 | L2 in (same) |
| 15.64 | "was unable to help." @15.64 | L3 in (same); at 16.28 "help" a 3 px `#8e2020` rule draws under "unable to help" `scaleX 0 -> 1, 0.5, power2.out` |
| whole window | | card floats y 0 -> -5, sine.inOut, yoyo, finite |
| 16.90-17.50 | after "help." ends @16.52 | card and source out `to(y:30, autoAlpha 0, 0.6, power3.in)`; ground stays |
Comp duration 6.70 s (runs 0.98 s past the wav end into the gap before A3-S4; trim the tail to the real gap if shorter).

## 6. CONTRACT
One file `compositions/g-a3-5-steele-quote.html`, root `id="g-a3-5-steele-quote-root"`, `data-composition-id="g-a3-5-steele-quote"`, PAUSED timeline `window.__timelines["g-a3-5-steele-quote"]`. Prefix `sq-`. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-5-steele-quote`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-5-steele-quote`.

## 7a. DONE LINE
All seven items of the template 7a.

## 8. RECEIPT
As the template.
