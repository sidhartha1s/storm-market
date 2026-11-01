# g-a5-6-reviews · A5-S5 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/quote-card.html` (panel, Georgia italic quote, phrase reveal) for both report cards and the quote card. The official catalog block `split-tilt-cards` (two cards arriving from opposite wings) is the motion reference only: it is not in `library/official/`, so read it with `npx hyperframes catalog --query "split tilt cards"` and never install it into the episode.

## 0. What this graphic claims
Two reviews came the next summer: the city's, by an NYU Wagner team, out 2 Jun 2023; the state's, by Guidehouse, out 4 Aug 2023 with 12 recommendations. One of the state's lines, eight words: "Clearly communicate the risks associated with weather events."

## 1. SOURCE
- NYU Wagner "Lessons Learned from the Buffalo Blizzard", led by Sarah Kaufman, commissioned by the City of Buffalo, released 2 Jun 2023: `research/response.md` section 5 table row 1 (PDF 403; via AP/Spectrum, SECONDARY); `factcheck/a5-r1.md` row 19.
- NYS After-Action Review, Guidehouse, commissioned by Gov. Hochul, announced by NYS DHSES 4 Aug 2023, 12 recommendations in four groups, includes "Clearly communicate the risks associated with weather events": https://www.dhses.ny.gov/node/16646, `research/response.md` section 5 row 2 and the "NYS Guidehouse" line (PRIMARY, FETCHED); `factcheck/a5-r1.md` row 20; word count 8 CONFIRMED, `factcheck/a5-r2.md` row 2.
- Cards are self-made title cards: no PDF art, no logos, no cover scans.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `rv-ground`, frame 0). Two scenes in one comp: A (two cards side by side, 0 to 15.8 s) and B (quote card, 15.8 s to end). Corner x >= 1600, y >= 680 empty in both scenes. No scale.

## 3. GEOMETRY (px)
Scene A — two report cards (panel `#15202b` at 94 %, 1 px `rgba(255,255,255,.14)` border, radius 20, padding 40 px; a 6 px top rule in the card's accent colour):
- Card 1 (city, accent `#93a3b2`): x 200-840, y 250-640. Lines, left-aligned at x 240:
  - "LESSONS LEARNED FROM THE BUFFALO BLIZZARD" Arial Black 900 40 px `#f2f5f8`, line-height 48, wraps to 3 lines inside 560 px (top 300).
  - "NYU WAGNER" Arial 700 26 px `#93a3b2` tracking 6, top 480.
  - "JUN 2, 2023" Arial Black 900 52 px `#d8a13a`, top 540.
- Card 2 (state, accent `#e8c56a`): x 1000-1580, y 250-640 (right edge 1580: clear of x 1600). Lines at x 1040:
  - "NYS AFTER-ACTION REVIEW" Arial Black 900 40 px `#f2f5f8`, 2 lines inside 500 px (top 300).
  - "GUIDEHOUSE" Arial 700 26 px `#93a3b2` tracking 6, top 480.
  - "AUG 4, 2023" Arial Black 900 52 px `#d8a13a`, top 540.
- Chip "12 RECOMMENDATIONS" (same panel, radius 20, padding 16 px 26 px), left x 1000, top 670 (about x 1000-1500, y 670-740): "12" Arial Black 900 52 px `#f2f5f8` + "RECOMMENDATIONS" Arial 700 26 px `#dfe7ee` tracking 4. Right edge < 1600.
Scene B — quote:
- Both report cards and the chip have left; the attribution line names the review, so no reference card is kept (a shrunken card would put text under the 19 px floor).
- Quote card (panel `#15202b` at 94 %, border as above, radius 28, padding 48 px 64 px), x 260-1560, y 400-690 (quote lines y about 448-580, attribution 600-630). Quote in Georgia italic 52 px `#f2f5f8`, line-height 66, centred, two lines: "Clearly communicate the risks" / "associated with weather events." Each of the 8 words is its own span.
- Word slots: before each word shows, its span shows a placeholder bar 6 px high `#2a3644` at the word's own width, sitting on the baseline (pre-authored, same span box, so the word replaces its own bar in place; no text written at runtime).
- Attribution under the quote, Georgia italic 26 px `#d8a13a`, centred, top 600: "NYS after-action review, Guidehouse, Aug 4, 2023".
- Source (both scenes from 12.94 s), Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "NYS DHSES release, 4 Aug 2023".
- Type tiers: 52 big, 40/26 mid, 19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Quote exactly: "Clearly communicate the risks associated with weather events." 8 words, 8 slots, nothing added (no quote marks inside the words beyond typographic open/close quotes on the first and last word, if used at all).
2. Card 1 says NYU WAGNER and Jun 2, 2023; card 2 says GUIDEHOUSE and Aug 4, 2023; "12 RECOMMENDATIONS" sits under card 2 only (the state's review), never under card 1.
3. Each word appears on its spoken word (±0.05 s), in order.
4. No logo, seal, PDF art or cover scan; no "NYU" on card 2 or "NYS" on card 1.
5. One reading target at a time: card 1 lands before card 2; the quote words build after card 1 has gone.
6. Nothing in x >= 1600, y >= 680; text 96 px from the edges.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S5 start, `audio/a5-s5.words.json`)
Strings: `LESSONS LEARNED FROM THE BUFFALO BLIZZARD` · `NYU WAGNER` · `JUN 2, 2023` · `NYS AFTER-ACTION REVIEW` · `GUIDEHOUSE` · `AUG 4, 2023` · `12` · `RECOMMENDATIONS` · `Clearly` `communicate` `the` `risks` `associated` `with` `weather` `events.` · `NYS after-action review, Guidehouse, Aug 4, 2023` · `NYS DHSES release, 4 Aug 2023`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "The reviews came the next summer." | ground on frame 0; two empty card outlines (border only, 30 %) fade in 0.0-0.6 at their scene-A boxes |
| 3.42 | "New York University" @3.42-4.22 | card 1 fills and slides in `fromTo(x:-120 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)`; its title at 3.60, "NYU WAGNER" at 3.90 (`fromTo(autoAlpha 0, y:12 -> 0, 0.4)`) |
| 6.08 | "June 2nd, 2023." @6.08-8.06 | "JUN 2, 2023" `fromTo(scale 1.2 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| 8.60 | "governor's office" @8.60-9.24 | card 2 fills and slides in `fromTo(x:120 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)`, title at 8.80 |
| 10.82 | "Guidehouse." @10.82 | "GUIDEHOUSE" in |
| 12.94 | "August 4th," @12.94-13.94 | "AUG 4, 2023" in (as the June date); source in |
| 14.14 | "12 recommendations." @14.14-14.96 | chip in `fromTo(y:20 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; "12" `fromTo(scale 1.3 -> 1, 0.4, power4.out)` |
| 15.82 | "One line in the state's review" @15.82-17.16 | card 1 and the chip out `to(x:-160, autoAlpha 0, 0.5, power3.in)`; card 2 out `to(x:160, autoAlpha 0, 0.5, power3.in)` at 16.02 |
| 16.84 | "review" @16.84 | quote card in `fromTo(y:30 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`, empty (no slots yet) |
| 20.64 | "eight words." @20.64-21.40 | the 8 slot bars draw `scaleX 0 -> 1` from left, stagger 0.08; attribution in at 21.10 |
| 22.34 | "Clearly" @22.34 | word 1 `fromTo(autoAlpha 0, y:10 -> 0, 0.25, power2.out)`, its bar `to(autoAlpha 0, 0.15)` |
| 22.62 / 23.00 / 23.36 / 23.62 / 24.22 / 24.46 / 24.72 | "communicate" / "the" / "risks" / "associated" / "with" / "weather" / "events." | words 2-8, same move each, on these exact times |
| whole window | | cards and quote card float y 0 -> -4 (sine, yoyo, finite); the empty-slot window 21.4-22.34 has the attribution entrance; no 4 s gap without a tween (check 0.6-3.42 and 17.4-20.64: the empty outlines and the empty quote card float, amplitude 4 px, period 2.4 s) |
| 25.90 to 26.50 | after "events." @25.06 | quote card `to(y:-20, autoAlpha 0, 0.6, power3.in)`; source out with it |

Comp duration 26.50 s (1.20 s past the wav end; trim to the real gap, keeping at least 0.8 s after 25.06).

## 6. CONTRACT
One file `compositions/g-a5-6-reviews.html`, root `id="g-a5-6-reviews-root"`, `data-composition-id="g-a5-6-reviews"`, PAUSED timeline `window.__timelines["g-a5-6-reviews"]`. Prefix `rv-`; never `.quotecard` or `.glasscard` (index classes). Moves are transforms only (no `width`/`height` tweens). Repeat note: "Aug 4, 2023" is on card 2 and in the attribution; card 2 is fully out (16.52) before the attribution enters (21.10), so they never share a frame. Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-6-reviews`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-6-reviews`.

## 7a. DONE LINE
All seven items of the template 7a. Item 4: capture each of the 8 word times twice (seek order). Read settled frames at 14.6 s and 25.3 s.

## 8. RECEIPT
As the template.
