# g-a5-2-quote: "unable to anticipate" (A5-S2)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/quote-card.html` (structure) and `episodes/ep-1974-super-outbreak/compositions/g-cite-paper.html` (beige cite card values). Copy values, rename every id/class to `a52-`.
Sits over: nothing. Full-frame comp on track 2, cut from g-a5-1-handchart. Ground: the same chart image `media/a5/jkl-surface-1950-11-24.jpg` (cover-fit 1920 x 1238, centred, `.archgrade` filter) under `rgba(3,5,8,0.70)` dim at frame 0 (matches g-a5-1's last frame) easing to 0.78 by 1.0 s. No trace or dots on it.

## 0. Claim
Looking back in 2004, three meteorologists wrote that the hand forecasts of 1950 could not anticipate this storm. The card shows their exact words with their names.

## 1. Source
- Kistler, Uccellini, Kocin, "Thanksgiving Weekend Storm of 1950", 84th AMS Annual Meeting, 15 Jan 2004, https://ams.confex.com/ams/84Annual/techprogram/paper_73168.htm: "the manually derived forecasts of the day were unable to anticipate this extreme event." Exact wording confirmed: `factcheck/a5-r2.md` rows 5, 6, 7, 11; `research/maps-forecast.md` §2.

## 2. Datum, scale, orientation
Card layout only. Frame 1920 x 1080; text-safe 96 px left/right, 54 px top/bottom; corner x >= 1600, y >= 680 kept empty.

## 3. Geometry (px)
- Beige cite card: `rgba(232,222,200,.90)`, radius 28, no box-shadow, left 260, right 260 (1400 wide), top 300, height about 420 (fit to text + 56 px padding all round).
- Quote: Georgia italic 52 px, `#2a2622`, line-height 1.25, left-aligned inside the card, max 3 lines. Text built line by line (3 pre-authored line spans, break the quote at: "…the manually derived forecasts" / "of the day were unable to anticipate" / "this extreme event.").
- Attribution: Arial 700 26 px `#6b6257`, 24 px under the quote: "Kistler, Uccellini, Kocin · AMS, 2004".
- Eyebrow above the quote inside the card: Arial 700 20 px `#6b6257` tracking 6: "LOOKING BACK".
- Marker underline under "unable to anticipate": `#d0121f` at 0.85, 6 px tall, drawn left to right (scaleX 0 to 1, transformOrigin left center, 0.5 s) under those words only.
- Chip "MISSED": glass surface (tokens.md), radius 14, padding 10 x 22, Arial Black 900 58 px `#f2f5f8`; centred x 960, bottom edge 24 px above the card top (about y 190 to 276).
- Three tiers: 58/52 (big), 26 (mid), 20 (small).

## 4. Must be true in the picture
1. The quote reads exactly "…the manually derived forecasts of the day were unable to anticipate this extreme event." (leading ellipsis, nothing added or cut), with the three authors and "AMS, 2004" under it.
2. No word is cut at a card edge in any frame; every child stays inside the card.
3. "MISSED" never overlaps the card or the quote; it appears only after the spoken "missed" (10.12).
4. The chart under the card stays dimmed to 0.70 or darker: no chart label reads through next to the card text.
5. Corner x >= 1600, y >= 680 empty.

## 5. Panel text (exact) and cues
Text: `LOOKING BACK` · `…the manually derived forecasts` · `of the day were unable to anticipate` · `this extreme event.` · `Kistler, Uccellini, Kocin · AMS, 2004` · `MISSED`
Cues from `audio/a5-s2.words.json`:
- 0.00 to 19.78: ground push 1.00 to 1.04, linear (motion every second).
- 2.98 "Looking": card in (`fromTo` y 40 to 0, autoAlpha 0 to 1, 0.6 s, power3.out), eyebrow with it. `/* LOOKING @2.98 */`
- 3.60 "2004,": attribution in (`fromTo` autoAlpha 0, y 12 to 0, 0.4 s). `/* 2004 @3.60 */`
- 6.86 "forecasts": quote line 1 in (`fromTo` autoAlpha 0, y 24 to 0, 0.4 s, power3.out). `/* FORECASTS @6.86 */`
- 7.70 "day,": line 2 in. `/* DAY @7.70 */`
- 8.64 "worked": line 3 in. `/* WORKED @8.64 */`
- 10.12 "missed": underline draws under "unable to anticipate"; chip "MISSED" in (`fromTo` autoAlpha 0, scale 1.3 to 1, 0.35 s, back.out(1.8)). `/* MISSED @10.12 */`
- 10.50 to 18.90: card and chip float y 0 to -8, sine.inOut, finite yoyo repeats.
- 18.98 "see" to 19.58: chip out (`to` autoAlpha 0, y -20, 0.3 s); card exits (`to` x 980, autoAlpha 0, 0.6 s, power3.in) ending at host end. `/* COMING @19.58 */`
Host: data-start = A5-S2 audio start, duration 20.30 s. Root `id="g-a5-2-quote-root"`.

## 6-8
Contract, tools, done line and receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
Must not: CSS @keyframes, `id="root"`, a second quote, any number other than "2004".
