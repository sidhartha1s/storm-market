# g-intro-4-lga-chip: "DIKES BREACHED · LAGUARDIA" over LaGuardia footage (I1-S1, second half)
CONDITIONAL: build only if the sourcing lane lands a LaGuardia flood clip for November 1950 whose `provenance.csv` row allows it (public domain or licensed, era right, not "backup only"). Without it, g-intro-3-coast's schematic inset carries this beat and this comp is not mounted.
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/snippets/cards.css` `.lt` (lower-third anchor left 110, bottom 110) with the `.glasscard` surface; the glass-over-footage pattern in `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`. Copy values into the comp under the `lg4-` prefix; do not reuse index.html class names.
Sits over: the LaGuardia clip on track 1 (SOURCE TBD; the orchestrator names the file and its trim in the mount). Overlay on track 3.

## 0. Claim
The coastal flood breached the dikes at LaGuardia Airport. The chip names the place and the event over film of it.

## 1. Source
`research/nws-facts.md` §1 JKL "The resulting coastal flooding breached dikes at LaGuardia Airport in New York flooding runways." Fact-check intro-r2 rows 19, 20.

## 2. Datum, scale, orientation
Overlay text only. Lower-third zone, text-safe margin 96 / 54 px. The presenter circle may be on: nothing at x >= 1600, y >= 680.

## 3. Geometry (px, 1920 x 1080)
- Glass card: `rgba(10,16,24,.55)`, `backdrop-filter: blur(18px) saturate(1.15)`, 1 px `rgba(255,255,255,.14)` border, radius 28, padding 22 x 34. Anchor left 110, bottom 110 (`inset: auto`). Width hugs the text (`display: table`), about 900 px; right edge must stay at or left of x 1560.
- Line 1 (eyebrow, names the thing): "NEW YORK · NOVEMBER 1950" Arial 700 22 px `#93a3b2` tracking 6.
- Line 2: "DIKES BREACHED" Arial Black 900 58 px `#f2f5f8`.
- Line 3: "LaGuardia Airport" Georgia italic 30 px `#d8a13a`.
- A 3 px accent rule `#7fb2e5` under line 2, drawn left to right (scaleX 0 to 1, transformOrigin left center, 0.5 s).
- Three tiers: 58 / 30 / 22.

## 4. Must be true in the picture
1. The clip under every second of the card is LaGuardia flood footage from this storm by its `provenance.csv` row (the card names a place and an event). If the row says anything else, do not mount; report.
2. The card covers no face, no broadcaster mark and no burned-in caption of the clip; move it to the top-left zone (left 110, top 110) if the bottom-left is busy, and say so in the receipt.
3. The text reads over the brightest frame of the clip under it (glass blur behind it).
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues
Text: `NEW YORK · NOVEMBER 1950` · `DIKES BREACHED` · `LaGuardia Airport`
Note on wording: the edit_script chip "DIKES BREACHED · LAGUARDIA" is set as two lines (headline + serif sub) so the headline stays at 58 px inside the lower-third; same words.
Cues from `audio/i1-s1.words.json` (seconds from the I1-S1 segment start; the host starts at the first mark, so comp time = word time - 6.94):
- 6.94 "through": card in (`fromTo` x -60 to 0, autoAlpha 0 to 1, 0.6 s, power3.out), eyebrow on with it. `/* THROUGH @6.94 */`
- 7.34 "dikes": "DIKES BREACHED" in (`fromTo` y 20 to 0, autoAlpha, 0.4 s, power3.out), accent rule draws. `/* DIKES @7.34 */`
- 7.76 "LaGuardia": "LaGuardia Airport" in (0.4 s). `/* LAGUARDIA @7.76 */`
- 8.16 to end: card floats y 0 to -6 px, sine.inOut yoyo, finite repeats (motion through the hold).
- Exit: `to` x -980... no: slide out right per the rule, `to` x 980, autoAlpha 0, 0.6 s, power3.in, anchored to the host's last 0.6 s.
Host: data-start = I1-S1 start + 6.94, duration = 10.427 - 6.94 + 0.40 (gap) = 3.887 s, or the clip's end if earlier (then exit in its last 0.6 s).

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 7: one frame composited over the real clip at I1-S1 8.5 s, and the clip's provenance row quoted in the receipt.
