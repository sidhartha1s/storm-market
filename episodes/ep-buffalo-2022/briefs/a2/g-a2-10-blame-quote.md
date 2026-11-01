# g-a2-10-blame-quote · A2-S9 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/quote-card.html` (beige cite card, phrase-by-phrase reveal) and the `.popfig` of `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (Abril font: `@font-face` from `fonts/AbrilFatface-Regular.ttf`, already in `episodes/ep-buffalo-2022/fonts/`). Lower third pairing as `g-a2-9-ban-bracket` section 3.

## 0. What this graphic claims
1. Five days after the storm began (28 Dec 2022), Poloncarz said of the ban's timing: "If anyone is to be blamed, you can blame me."
2. The city's later review found the travel bans were inadequately conveyed.

## 1. SOURCE
- Quote, exact: WAMC/NPR, 28 Dec 2022 (FETCHED): https://www.wamc.org/2022-12-28/dozens-have-died-in-the-buffalo-area-as-national-guard-begins-door-to-door-checks; `research/response.md` sections 1 and 3; `factcheck/a2-r1.md` row 38 (CONFIRMED, "Quote exact", about the timing of the 9:30 ban).
- 23 to 28 Dec = 5 days: row 37 (CONFIRMED). Popfig "5 DAYS LATER".
- "Inadequately conveyed": NYU Wagner review via AP (WHEC, Spectrum), 2 Jun 2023, SECONDARY; rows 40 and 41: AP's sentence "stranded drivers who were either unaware of or ignored travel bans that were inadequately conveyed" is AP's paraphrase of the report (PDF 403). So the phrase is shown as a finding, WITHOUT quote marks.
- Source lines: "NPR via WAMC, 28 Dec 2022" · "NYU Wagner review for the City of Buffalo, via AP, 2 Jun 2023" (Picture).

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed graphic, channel ground on the root from frame 0. No scale.

## 3. GEOMETRY (px)
- Popfig "5 DAYS LATER": 'AbrilFig' 150 px `#d0121f` with the popfig text-shadow (tokens / ep6 pattern), centred (960, 470), one line (about x 450 to 1470). Never over a card: it leaves before the card enters.
- Quote card (beige cite card): `rgba(232,222,200,.90)`, radius 14, x 260 to 1660, y 250 to 640, padding 56 px 80 px. Quote Georgia italic 60 px `#2a2622`, two pre-authored lines, left-aligned at x 340: line Q1 "“If anyone is to be blamed," (glyph box about y 330 to 400), line Q2 "you can blame me.”" (about y 420 to 490). Curly quote marks are part of the leaves. A 4 px `#8e2020` rule under "blame me" (x from the start of "blame" to the end of "me", y 500) drawn at its word.
- Lower third (glass card): `left:110px; bottom:110px`, padding 18 px 30 px; "MARK POLONCARZ" Arial Black `font-weight:900` 52 px `#f2f5f8`; "28 DEC 2022" Arial 700 26 px `#dfe7ee` letter-spacing 2. About x 110 to 640, y 850 to 970. Below the card (card bottom 640).
- Finding (no card, on the ground): eyebrow "CITY OF BUFFALO REVIEW · THE TRAVEL BANS" Arial 700 22 px `#93a3b2` letter-spacing 6, centred x 960, glyph box y 380 to 406; "INADEQUATELY CONVEYED" Arial Black `font-weight:900` 84 px `#f2f5f8`, centred x 960, glyph box about y 430 to 520 (about x 340 to 1580); underline 4 px `#c0392b`, y 540, same width as the line.
- Source line Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`; one at a time.
- Type tiers: 150/84/60/52 big, 26 mid, 19 to 22 small. Corner x >= 1600, y >= 680 empty (card right edge 1660 is at y < 680).

## 4. MUST BE TRUE IN THE PICTURE
1. Quote text exactly "If anyone is to be blamed, you can blame me." split after the comma; no other words added.
2. The quote is attributed on screen (lower third + source line) for as long as it shows.
3. "INADEQUATELY CONVEYED" has no quote marks and never shares a frame with the Poloncarz quote.
4. The popfig never overlaps a card; the lower third never overlaps the quote card.
5. Nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A2-S9 start, `audio/a2-s9.words.json`; Whisper splits the name "Paul and Kars")
Strings: `5 DAYS LATER` · `“If anyone is to be blamed,` `you can blame me.”` · `MARK POLONCARZ` `28 DEC 2022` · `CITY OF BUFFALO REVIEW · THE TRAVEL BANS` `INADEQUATELY CONVEYED` · `NPR via WAMC, 28 Dec 2022` · `NYU Wagner review for the City of Buffalo, via AP, 2 Jun 2023`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0, "Five" @0.00 | ground only |
| 0.05 | "Five days" | popfig `fromTo(scale 1.3 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| 0.5 to 3.0 | hold | popfig drift `scale 1 -> 1.03`, ease none |
| 3.00 to 3.40 | before "Paul" @3.52 | popfig out `to(autoAlpha 0, scale 0.96, 0.4, power2.in)` |
| 3.52 | "Paul" @3.52 | quote card `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)` (empty); lower third `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`; WAMC source in |
| 6.16 | "If" @6.16 | Q1 `fromTo(autoAlpha 0, y:14 -> 0, 0.4, power3.out)` |
| 7.68 | "you" @7.68 | Q2 in, same |
| 8.00 | "blame" @8.00 | rule under "blame me" `scaleX 0 -> 1, 0.4, transformOrigin left center` |
| 3.5 to 8.9 | hold | card float `y: 0 -> -4`, sine, finite yoyo |
| 8.70 to 9.20 | "The city's" @8.90 | card and lower third out `to(x:980 for the card / x:-80 for the lower third, autoAlpha 0, 0.5, power3.in)`; WAMC source out |
| 9.36 | "review" @9.36 | eyebrow in; NYU source in |
| 11.10 | "inadequately" @11.10 | "INADEQUATELY CONVEYED" `fromTo(autoAlpha 0, scale 1.12 -> 1, 0.45, power4.out)` |
| 11.80 | "conveyed." @11.80 | underline `scaleX 0 -> 1, 0.5, transformOrigin left center` |
| 12.3 to 17.4 | "Some of the drivers ... ignored them." | finding float `y: 0 -> -4`, sine, finite yoyo; underline brightness pulse at "unaware" @15.32 and "ignored" @16.62 (`opacity 1 -> 0.5 -> 1, 0.4`) |
| 17.40 to 18.00 | after "them." @16.90 | exit fade-through: all `to(autoAlpha 0, y:-16, 0.6, power2.in)` |
Comp duration 18.00 s.

## 6. CONTRACT
One file `compositions/g-a2-10-blame-quote.html`, root `<div id="g-a2-10-blame-quote-root" data-composition-id="g-a2-10-blame-quote" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-10-blame-quote"]`. Ids/classes `bq-`. Do not reuse `.popfig` or any index.html class name: scope it `bq-popfig`. Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-10-blame-quote`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-10-blame-quote`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a.

## 8. RECEIPT
As the template.
