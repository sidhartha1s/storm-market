# g-a2-3-record: Columbus 7.5 in on Sat 25 Nov, still the November record (A2-S3)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/snippets/cards.css` `.stamp` (crimson stamp card, `#f4f0e8` text) for the calendar card; `library/inhouse/quote-card.html` beige cite card for the NWS line. Prefix `r3-`.
Sits over: nothing. Full-frame designed card on track 2, channel radial background on from frame 0.

## 0. Claim
On Saturday 25 Nov 1950 Columbus got 7.5 in of snow, its greatest calendar-day November snowfall, and no November day has topped it since.

## 1. Source
`research/nws-facts.md` §2 ILN "Columbus OH, 25 Nov | 7.5 in, greatest calendar-day November snowfall" (P). `factcheck/a2-r1.md` row 6 (ILN: "Another 7.5 inches of snow fell on Columbus on the 25th"), row 7 (greatest calendar-day November record; intro-r1 row 25 "still stands").
WORDING: research holds a fetch summary of the record sentence, not verified verbatim (nws-facts.md header note). Default: the NWS line is set as attributed paraphrase WITHOUT quotation marks (text below). If the orchestrator confirms exact words on https://www.weather.gov/iln/19501125, the line may be set in quotes with those words.

## 2. Datum, scale, orientation
Text card, no scale. Two blocks: calendar card left half, cite card right half, chip under the cite card.

## 3. Geometry (px, 1920 x 1080)
- Calendar card (left): 520 x 560, left 200, top 220 (bottom 780), crimson `#8e2020`, radius 18, top band 90 px `#6e1818` with two binder rings (white 14 px circles at x 330 and 590 of the card's local... place at card-local x 130 and 390, y -10). Inside, centred:
  - "SAT · NOV 25" Arial 700 30 px `#f4f0e8` tracking 4 in the top band.
  - "7.5" Arial Black 900 180 px `#f4f0e8` (display tier), centre y about 470.
  - "IN" Arial Black 900 58 px `#f4f0e8` under it, then "COLUMBUS, OHIO" Arial 700 22 px `#f5d98b` tracking 6.
  The edit_script string "SAT · NOV 25 · 7.5 IN" is split across these lines; same words.
- Cite card (right): beige `rgba(232,222,200,.90)`, radius 18, left 840, top 300, width 780 (right edge 1620, inside the 1824 margin; bottom about 530, above the circle line y 680), padding 28 x 36. Text dark `#2a2622`:
  - eyebrow "NWS WILMINGTON, OHIO" Arial 700 22 px `#6b6257` tracking 6
  - line "Greatest calendar-day snowfall on record for any November day" Georgia italic 40 px `#2a2622`, max 2 lines, line-height 1.2. (no quotation marks unless §1 wording is confirmed)
- Chip under the cite card: glass card left 840, top 570, "STILL THE RECORD" Arial Black 900 52 px `#f2f5f8`, padding 18 x 30 (bottom about 660, clear of y 680).
- Source line "Source: NWS Wilmington OH" Arial 700 19 px `#c8d3e0` tracking 2, left 110, bottom 60.
- Tiers: 180 / 58 / 52 / 40 / 30 / 22 / 19.

## 4. Must be true in the picture
1. The card says 7.5 IN and SAT · NOV 25 together; no other snowfall figure on screen (the spoken "about 15" and "more than 20" stay voice-only: one number per frame).
2. The NWS line is attributed to NWS Wilmington and, without confirmed wording, carries no quotation marks.
3. "STILL THE RECORD" arrives on "since", after the record line.
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a2-s3.words.json`, seconds from A2-S3 start)
Text: `SAT · NOV 25` · `7.5` · `IN` · `COLUMBUS, OHIO` · `NWS WILMINGTON, OHIO` · `Greatest calendar-day snowfall on record for any November day` · `STILL THE RECORD` · `Source: NWS Wilmington OH`
- 0.00 "By": ground on, source line on; calendar card waits off-frame above (y -700, hidden). `/* BY @0.00 */`
- 0.62 "Saturday,": card top band with "SAT · NOV 25" drops in (y -700 to 0, 0.5 s, back.out(1.4)). `/* SATURDAY @0.62 */`
- 2.16 "seven": "7.5" stamps (scale 1.4 to 1, autoAlpha 0 to 1, 0.3 s, power4.out) + card shake x ±6 px 0.25 s; "IN" and "COLUMBUS, OHIO" follow 0.2 s later. `/* SEVEN @2.16 */`
- 4.70 "November": cite card slides in `fromTo` x 660 to 0, autoAlpha, 0.7 s, power3.out. `/* NOVEMBER @4.70 */`
- 6.18 "since.": chip "STILL THE RECORD" in (y 20 to 0, autoAlpha, 0.4 s, power3.out). `/* SINCE @6.18 */`
- 7.08 to exit (about 10 s hold through "15 inches", "more than 20", "50,000 people"): snow flakes drift down over the whole frame (40 flakes, 50 to 90 px/s, finite repeats, precomputed positions), calendar card floats y 0 to -6, sine yoyo; at 13.00 "And" the cite card and chip dim to 60 % (the beat turns to the crowd).
- Exit: last 0.6 s: cite card + chip `to` x 980, autoAlpha 0; calendar card `to` x -980, autoAlpha 0, 0.6 s, power3.in.
Host: data-start = A2-S3 start, duration = 17.28 + 0.40 = 17.68 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
