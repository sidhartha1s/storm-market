# g-a4-1-stuck-quote · A4-S1 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-intro-2-toll-chips.html` (chip and source pill: copy the surface, padding and float exactly) and `.quotecard.glasscard` in `library/inhouse/snippets/cards.css` with the phrase reveal of `library/inhouse/quote-card.html`.

## 0. What this graphic claims
1. About two of every three snow-clearing machines sent out got stuck (county executive Mark Poloncarz, Mon 26 Dec 2022).
2. The governor saw plows and rescue vehicles "in ditches, buried in snow" herself the same day. This is the payoff of the CTA hinge: it lands in the first three words.

## 1. SOURCE
- Two-thirds stuck: CBS Miami page quoting Poloncarz on CNN "on Monday" (26 Dec): "two-thirds of the equipment that was dispatched to help clear snow during the height of the storm got stuck." `research/deaths.md` section 5 (SECONDARY); `factcheck/a4-r1.md` rows 3, 4, 9 (CONFIRMED, date corrected to 26 Dec).
- Hochul quote, verbatim, 26 Dec 2022 storm briefing transcript, governor.ny.gov (PRIMARY): `research/response.md` section 2; `factcheck/a4-r1.md` row 1.
- Footage: DVIDS 7571852, 174th Attack Wing Airmen running a runway snowblower on I-90, Buffalo, 26 Dec 2022, courtesy photo: `research/response.md` section 7 row 2, https://www.dvidshub.net/image/7571852/new-york-national-guard-responses-christmas-snowstorm (accepted in `research/cc-clips-r2.md` header).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, overlay on footage. Lower-third anchor `left:110px; bottom:110px` (tokens.md "Canvas"). Presenter circle may be on: nothing in x >= 1600, y >= 680. No scale.

## 3. GEOMETRY (px)
- Chip C1: glass surface exactly as g-intro-2 (`rgba(10,16,24,.55)`, `backdrop-filter: blur(18px) saturate(1.15)`, 1 px `rgba(255,255,255,.14)` border, radius 28), `left:110px; bottom:110px`, padding 22 px 34 px, hugs its text. One baseline-aligned line of five spans: "ABOUT " (Arial Black `font-weight:900` 38 px `#dfe7ee`), "2" (Arial Black 900, 84 px `#f2f5f8`, line-height 1), " OF EVERY " (38 px `#dfe7ee`), "3" (84 px `#f2f5f8`), " STUCK" (38 px `#e74c3c`). Box about x 110 to 900, y 842 to 970.
- Red rule under "STUCK": 4 px `#e74c3c`, the word's width, 6 px under its baseline.
- Quote card: glass surface as C1 but no shadow, `left:260px; right:400px` (x 260 to 1520, clear of the corner), `bottom:150px`, padding 28 px 48px, text centred. Line 1 the quote, Georgia italic 44 px `#f2f5f8`, line-height 1.35, one line (about 1,000 px). Line 2 attribution, Arial 700 24 px `#d8a13a`, letter-spacing 3, 12 px below. Card about y 760 to 930.
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`, one line. Two pre-authored pills (S-A, S-B) in the same slot, never both visible. S-B is about x 110 to 820.
- Type tiers: 84 / 52-plus (big), 38 and 44 (mid), 19 and 24 (small).
- Nothing in x >= 1600, y >= 680.

## 4. MUST BE TRUE IN THE PICTURE
1. The chip's numerals are 2 and 3 and read "ABOUT 2 OF EVERY 3 STUCK": no "%" and no "two-thirds" spelt out. The "2" is fully landed by "thirds" @0.52.
2. The chip and the quote card are never on screen together; the chip is gone before "The same day" @8.78.
3. The quote text is verbatim and complete, with curly quotes: “I saw them myself in ditches, buried in snow.” Each word appears on its own spoken word, never before it.
4. One source pill at a time; S-A (Poloncarz) belongs to the chip, S-B (Hochul) to the card. S-B is never visible before "Governor" @9.98.
5. Over the photo, the chip and card do not cover the snowblower's working end (the orchestrator checks the settled frame; if covered, the card moves up to `bottom:300px`, still clear of the corner).

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S1 start, `audio/a4-s1.words.json`)
Strings: chip `ABOUT 2 OF EVERY 3 STUCK` · quote `“I saw them myself in ditches, buried in snow.”` · attribution `GOV. KATHY HOCHUL` · S-A `Mark Poloncarz, 26 Dec 2022, CNN, via CBS News` · S-B `Gov. Kathy Hochul, storm briefing, 26 Dec 2022, governor.ny.gov`

| t (s) | spoken word | action |
|---|---|---|
| 0.08 | "About" @0.00 (hard cut out of the CTA) | C1 in: `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; S-A in: `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power2.out)` |
| 0.24 | "two" @0.24 | "2" `fromTo(scale 1.3 -> 1, 0.35, power4.out)` |
| 0.52 | "thirds" @0.52 | "3" same pop |
| 2.92 | "stuck." @2.92 | red rule `fromTo(scaleX 0 -> 1, 0.45, power2.out, transformOrigin left center)` |
| 5.66 | "Mark" @5.66 | S-A text brightens to `#f2f5f8` 0.25 s, back to `#c8d3e0` at 7.2 |
| 7.95 to 8.30 | after "Christmas." @7.74 | C1 and S-A out: `to(x:-80, autoAlpha 0, 0.35, power3.in)` |
| 9.98 | "Governor" @9.98 | S-B in (as S-A) |
| 16.10 | before "I" @16.30 | card shell + attribution in: `fromTo(y:24 -> 0, autoAlpha 0 -> 1, 0.35, power3.out)`, all quote words still hidden |
| 16.30 / 16.44 / 16.64 / 16.80 / 17.14 / 17.36 / 18.24 / 18.50 / 18.72 | "I" "saw" "them" "myself" "in" "ditches," "buried" "in" "snow." | each word span (pre-authored, the opening quote mark rides with "I", the closing one with "snow.") `fromTo(autoAlpha 0 -> 1, y:6 -> 0, 0.14, power2.out)` at its time |
| whole window | | the visible chip, pill or card floats `y: 0 -> -4`, `sine.inOut`, yoyo, finite repeats (keeps 9.98 to 16.10 alive) |
| 19.30 to 19.90 | after "snow." ends @19.00 | card and S-B out: `to(x:980, autoAlpha 0, 0.6, power3.in)` |

Comp duration 19.9 s (wav 19.21 + land). The orchestrator mounts the host 19.9 s long and starts S2 at least 0.7 s after S1's wav ends; if S2 must start earlier, the hard cut into the full-frame g-a4-2 carries the card off and the exit row is cut to fit. Spoken time in a comment at each tween.

## 6. CONTRACT
One file `compositions/g-a4-1-stuck-quote.html`, root `<div id="g-a4-1-stuck-quote-root" data-composition-id="g-a4-1-stuck-quote" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-1-stuck-quote"]`. Ids prefixed `sq-`; classes `sq-chip`, `sq-num`, `sq-card`, `sq-word`, `sq-src` (never `.lt`, `.glasscard`, `.quotecard`, `.srclab`: index.html uses them). Root transparent. Start-hidden in CSS too. Everything else: `references/mg-quickref.md` and the template section 6.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-1-stuck-quote`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-1-stuck-quote`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: one frame at 2.0 s (chip) and one at 18.9 s (full quote) composited over DVIDS 7571852 once it is mounted.

## 8. RECEIPT
As the template.
