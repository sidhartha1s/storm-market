# g-a4-11-door-quote · A4-S10 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `g-a4-1-stuck-quote` (same quote card, word reveal and source slot; build it first and copy it) and the chip of `g-a4-3-day-chip`.

## 0. What this graphic claims
1. In the days after, Erie County's executive warned that some people "may have perished living alone".
2. The Weather Service warning had said "Travel is strongly discouraged": staying home was the advice. The door is the question the act ends on.

## 1. SOURCE
- Poloncarz "may have perished living alone": WBFO via btpm.org, 30 Dec 2022 (SECONDARY): "We are fearful that there are individuals who may have perished living alone". Undated in the source, spoken as "in the days after". `research/deaths.md` section 5; `factcheck/a4-r1.md` rows 38, 39.
- "Travel is strongly discouraged.": NWS Buffalo Blizzard Warning WSWBUF 220854, 3:54 a.m. 22 Dec 2022 (PRIMARY), `research/nws.md` 6.3; `factcheck/a4-r1.md` row 40. The chip prints the warning's own words, in grey (a quoted line, not our claim).
- Footage under it: Andre Carrotflower, "Snowy door ... 20221224.jpg", own work, Wikimedia Commons, CC BY-SA 4.0 (accepted, `research/cc-clips-r2.md` header, devq copy `cc-snowy-door.jpg`). CC BY-SA needs the credit on screen and in the description: the on-screen credit is in this comp.

## 2. DATUM, SCALE, ORIENTATION
Overlay over the door still (slow push toward the door, index work). Lower-third anchor `left:110px; bottom:110px`. Presenter circle may be on: nothing in x >= 1600, y >= 680. No scale.

## 3. GEOMETRY (px)
- Quote card: as `g-a4-1-stuck-quote` (glass, no shadow, `left:260px; right:400px`, `bottom:150px`, padding 28 px 48 px, centred). Line 1 the quote, Georgia italic 44 px `#f2f5f8`, one line (about 640 px); line 2 attribution Arial 700 24 px `#d8a13a`, letter-spacing 3. Card about y 760 to 930.
- Chip (glass as g-a4-3, padding 22 px 34 px, `left:110px; bottom:110px`, hugs text): "TRAVEL IS" + " STRONGLY DISCOURAGED", Arial Black `font-weight:900` 52 px `#c8d3e0` (grey: the warning's words, quoted), one line, two spans. About x 110 to 1290, y 860 to 970.
- Source slot: glass pill, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`; S-A and S-B, one at a time.
- Photo credit: glass pill, radius 14, padding 5 px 12 px, `right:96px; top:54px` (top-right corner, outside the presenter corner), Arial 400 19 px `#c8d3e0`, the whole window.
- Type tiers: 52 (big), 44 (mid), 19 and 24 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. The quote is verbatim, lower-case as spoken, in curly quotes: “may have perished living alone”; each word appears on its spoken word.
2. The quote card and the chip are never on screen together; the chip reads exactly "TRAVEL IS STRONGLY DISCOURAGED", in grey, never red or amber.
3. Nothing covers the door itself at any point of the push (the orchestrator checks frames at 6.6 s and 10.0 s; if the card or chip covers it, the card moves to `bottom:300px` or the chip to `left:auto; right:400px`, still clear of the corner).
4. The credit is on screen from frame 0 to the end and names author and licence.
5. From 13.04 ("So what happened") the only things on screen are the photo, the credit and the source line: the question plays over the door.

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S10 start, `audio/a4-s10.words.json`)
Strings: quote `“may have perished living alone”` · attribution `MARK POLONCARZ · ERIE COUNTY EXECUTIVE` · chip `TRAVEL IS STRONGLY DISCOURAGED` · S-A `Mark Poloncarz, via WBFO, 30 Dec 2022` · S-B `NWS Buffalo Blizzard Warning, 22 Dec 2022` · credit `Photo: Andre Carrotflower, Wikimedia Commons, CC BY-SA 4.0`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "In the days after" @0.00 | credit on from frame 0 (no entrance tween; it is there with the cut) |
| 3.52 | "Polonkars" (Poloncarz) @3.52 | card shell + attribution in `fromTo(y:24 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`, quote words hidden; S-A in `fromTo(autoAlpha 0, y:16 -> 0, 0.4)` |
| 5.02 / 5.72 / 5.94 / 6.32 / 6.60 | "may" "have" "perished" "living" "alone." | each word span `fromTo(autoAlpha 0 -> 1, y:6 -> 0, 0.14, power2.out)` (opening quote mark with "may", closing with "alone") |
| 7.10 to 7.45 | before "The Weather Service" @7.50 | card and S-A out `to(x:980, autoAlpha 0, 0.35, power3.in)` |
| 7.60 | "Weather Service warning" @7.60 to 8.14 | S-B in |
| 8.94 | "travel" @8.94 | chip in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` with "TRAVEL IS" |
| 9.60 | "strongly discouraged" @9.60 | " STRONGLY DISCOURAGED" span in `fromTo(autoAlpha 0, x:-10 -> 0, 0.35)` |
| 12.30 to 12.90 | after "advice." @12.04 | chip out `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
| whole window | | visible card, chip and pills float `y 0 -> -3`, sine, finite repeats |
| 14.43 to 15.03 | after "home?" @14.54 | S-B and credit fade `to(autoAlpha 0, 0.6, power2.in)` as the index fades the picture toward the Act 5 blackout |

Comp duration 15.03 s (wav length). The fade to the blackout itself is index work.

## 6. CONTRACT
One file `compositions/g-a4-11-door-quote.html`, root `<div id="g-a4-11-door-quote-root" data-composition-id="g-a4-11-door-quote" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-11-door-quote"]`. Ids prefixed `dq-`; classes prefixed `dq-` (never `.quotecard`, `.glasscard`, `.srclab`). Root transparent. Start-hidden in CSS too (the credit starts visible). Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-11-door-quote`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-11-door-quote`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: frames at 6.8 s (quote) and 10.2 s (chip) composited over `cc-snowy-door.jpg` at its pushed framing.

## 8. RECEIPT
As the template.
