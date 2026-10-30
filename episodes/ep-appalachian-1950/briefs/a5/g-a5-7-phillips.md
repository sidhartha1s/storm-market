# g-a5-7-phillips: Norman Phillips and the 1958 paper (A5-S7)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `episodes/ep-1974-super-outbreak/compositions/g-cite-paper.html` (beige cite card, its 16 px attribution exception) and `library/inhouse/quote-card.html`; `.namecard` values from `library/inhouse/snippets/cards.css`. Prefix every id/class `a57-`.
Sits over: nothing. Full-frame comp on track 2. Ground: background radial gradient `#0b1016` to `#030507`, plus the chart image `media/a5/jkl-surface-1950-11-24.jpg` (same file as g-a5-1, cover-fit, `.archgrade`) at opacity 0.14, drifting x 0 to -40 and scale 1.00 to 1.05 over the comp (ease none): the storm "turned into homework".

## 0. Claim
Norman Phillips, a member of Charney's group, published a paper in 1958 on the errors in predicting what he called the Appalachian storm of November 1950.

## 1. Source
- AMS reference list (Kistler et al. 2004), https://ams.confex.com/ams/84Annual/webprogram/Paper73168.html: "Phillips, N. A. 1958: Geostrophic Errors in Predicting the Appalachian Storm of November 1950. Geophysica, 6, 389-405." `factcheck/a5-r2.md` rows 37, 39 (card text CONFIRMED; title case changed only). Member of Charney's group: row 36 (MIT obituary, joined the IAS group, doctorate 1951).
- Journal itself not reached (SECONDARY citation): the card shows the reference only, no abstract, no page image.

## 2. Datum, scale, orientation
Card layout only. Frame 1920 x 1080; text-safe 96/54 px; corner x >= 1600, y >= 680 kept empty.

## 3. Geometry (px)
- Name card (text only, no photo slot, no monogram): "NORMAN PHILLIPS" Arial Black 900 64 px `#f2f5f8`, centred, bottom 150, `.nc-name` text-shadow; sub "Charney's group, Princeton" Georgia italic 32 px `#e8c56a`, 10 px under. No card behind (dark designed ground, not footage).
- Citation card: beige `rgba(232,222,200,.90)`, radius 28, no shadow, left 260, right 260 (1400 wide), top 250, height fit to content + 56 px padding.
  - Line 1 (author, year): "Phillips, N. A., 1958" Arial Black 900 52 px `#2a2622`.
  - Line 2 (title, built in two spans): "Geostrophic errors in predicting" / "the Appalachian storm of November 1950" Georgia italic 44 px `#2a2622`, line-height 1.25, 18 px under line 1.
  - Line 3 (journal): "Geophysica 6, 389-405" Arial 700 26 px `#6b6257`, 22 px under.
  - Eyebrow at the card top: "PUBLISHED PAPER" Arial 700 20 px `#6b6257` tracking 6.
  - Underline under "the Appalachian storm of November 1950" only: `#d0121f` at 0.85, 5 px, scaleX 0 to 1 from the left, 0.6 s.
- Tiers: 64/52 (big), 44/32/26 (mid), 20 (small).

## 4. Must be true in the picture
1. Card text matches the edit_script line character for character: "Phillips, N. A., 1958 · Geostrophic errors in predicting the Appalachian storm of November 1950 · Geophysica 6, 389-405" split over the three lines above (the "·" separators become line breaks).
2. No word cut at the card edge; every child inside the card.
3. Name card and citation card never show together (one reading target).
4. "1958" and "1950" appear once each on screen.
5. The chart ground stays at 0.14 or less: its printed labels never compete with the card.

## 5. Panel text (exact) and cues
Text: `NORMAN PHILLIPS` · `Charney's group, Princeton` · `PUBLISHED PAPER` · `Phillips, N. A., 1958` · `Geostrophic errors in predicting` · `the Appalachian storm of November 1950` · `Geophysica 6, 389-405`
Cues from `audio/a5-s7.words.json`:
- 0.00: ground on (gradient + faint chart drifting).
- 0.62 "Charney's": name sub ready hidden.
- 1.64 "Norman": name in (`fromTo` autoAlpha 0, y 30 to 0, 0.5 s, power3.out), sub 0.3 s after. `/* NORMAN @1.64 */`
- 2.00 to 3.30: name float y 0 to -6.
- 3.30: name exits (`to` y 30, autoAlpha 0, 0.45 s, power3.in), gone by 3.75.
- 3.90 "1958,": card in (`fromTo` y 40 to 0, autoAlpha 0, 0.6 s, power3.out) with eyebrow and line 1. `/* 1958 @3.90 */`
- 6.08 "errors": title span 1 in (`fromTo` autoAlpha 0, y 20 to 0, 0.4 s). `/* ERRORS @6.08 */`
- 7.66 "Appalachian": title span 2 in. `/* APPALACHIAN @7.66 */`
- 9.16 "1950.": underline draws; journal line in 0.3 s later. `/* 1950 @9.16 */`
- 9.80 to 11.30: card float y 0 to -8, sine.inOut.
- 11.32 to 11.92 ("homework." 11.60): card exits (`to` x 980, autoAlpha 0, 0.6 s, power3.in), ending at host end. `/* HOMEWORK @11.60 */`
Host: data-start = A5-S7 audio start, duration 12.40 s. Root `id="g-a5-7-phillips-root"`.

## 6-8
Contract, tools, done line and receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
Must not: CSS @keyframes, `id="root"`, a photo or monogram for Phillips, an invented abstract or page image.
