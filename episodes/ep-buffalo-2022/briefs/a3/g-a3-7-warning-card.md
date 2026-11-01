# g-a3-7-warning-card · A3-S6 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `compositions/g-intro-7-afd-card.html` (this episode's NWS text card: panel, Courier header, highlight rule, source). Copy, prefix `wc-`, replace the text and cues. No typewriter this time: lines are already printed; the beat is the HIGHLIGHT.

## 0. What this graphic claims
The NWS Buffalo Blizzard Warning issued 2:09 PM Thu 22 Dec 2022 for Erie County said wind chills could cause frostbite in as little as 30 minutes, and told anyone stranded: stay with your vehicle.

## 1. SOURCE
- Product WWUS41 KBUF 221909 (WSWBUF), "209 PM EST Thu Dec 22 2022", zone NYZ001-002-010-011-085 (incl. Northern and Southern Erie, Buffalo). Re-fetched by the brief writer 28 Oct 26 from IEM: https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=WSWBUF&sdate=2022-12-22T19:00Z&edate=2022-12-22T19:20Z&fmt=text&limit=5
- Verbatim (product's own line breaks):
  ```
  * IMPACTS...Travel will be extremely difficult to impossible at
    times. ... The bitter wind chills as
    low as 10 to 20 below zero could cause frostbite on exposed
    skin in as little as 30 minutes.

  PRECAUTIONARY/PREPAREDNESS ACTIONS...
  ... Travel is strongly
  discouraged. If you must travel, have a winter survival kit with
  you. If you get stranded, stay with your vehicle.
  ```
- Fact check: `factcheck/a3-r1.md` rows 37 and 38 (PRIMARY, CONFIRMED); same line in 221628. "10 to 20 below zero" also `research/nws.md` 3.6.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `wc-ground`, frame 0). No scale. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Panel `wc-panel`: x 200-1500, y 190-790, radius 28, fill `linear-gradient(180deg, #15202b, #0b1016)`, 1 px `rgba(255,255,255,.14)`.
- Header, Courier New 700 26 px `#93a3b2` letter-spacing 2, left 260, tops 230 / 270: "Blizzard Warning · National Weather Service Buffalo NY" / "209 PM EST Thu Dec 22 2022". (Mixed case as the product.)
- Divider 1 px `rgba(255,255,255,.14)`, x 260-1440, y 322.
- Body, Courier New 700 32 px `#dfe7ee`, letter-spacing 0, left 260, line pitch 52. Each line is a whole clause, under 1180 px (about 19.2 px per character at 32 px, so 61 characters max):
  - B1 top 360: `The bitter wind chills as low as 10 to 20 below` (48 ch, about 922 px)
  - B2 top 412: `zero could cause frostbite on exposed skin in as` (48 ch)
  - B3 top 464: `little as 30 minutes.` (21 ch)
  - gap
  - B4 top 560: `PRECAUTIONARY/PREPAREDNESS ACTIONS...` (`#93a3b2`, 37 ch)
  - B5 top 612: `If you must travel, have a winter survival kit with` (51 ch, about 979 px)
  - B6 top 664: `you. If you get stranded, stay with your vehicle.` (49 ch)
  Line breaks are the builder's (product breaks run past the panel); the words and their order are the product's.
- Highlight 1 (frostbite): a band `rgba(216,161,58,.28)` (Amber 1 at 28 %) behind "frostbite on exposed skin in as" (B2) and "little as 30 minutes." (B3), measured from glyph boxes, drawn `scaleX 0 -> 1` left origin.
- Highlight 2 (stay): band `rgba(231,76,60,.30)` behind "If you get stranded, stay with your vehicle." on B6 (x from the glyph box of "If" to the period).
- Chips over the dark ground below the panel, one at a time, `left:200px; top:820px`, glass chip, Arial Black 900 52 px `#f2f5f8` (y about 820-928):
  - C1 "FROSTBITE IN AS LITTLE AS 30 MIN" (width about 1270 at about 37 px per Arial Black capital, x 200-1470; must end left of x 1600)
  - C2 "STAY WITH YOUR VEHICLE" (x about 200-930)
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "NWS Buffalo Blizzard Warning, 22 Dec 2022, IEM archive".
- Product id, Courier New 400 19 px `#93a3b2`, left 260, top 740: "WWUS41 KBUF 221909".
- Type tiers: 52 big, 32/26 mid, 19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Every body word is the product's, in order; no word cut at the panel edge in any frame (the push included).
2. Highlight 1 lands on "frostbite" (voice), highlight 2 on "Stay with your vehicle" (voice).
3. One chip at a time; C1 is gone before C2 enters. Chip text exactly as §5 ("30 MIN" on the chip is the product's "30 minutes").
4. Chips never cover the panel text (chip top 820 > panel bottom 790).
5. Header time reads "209 PM EST Thu Dec 22 2022" exactly as the product.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S6 start, `audio/a3-s6.words.json`)
Strings: header 2 lines, B1-B6, `WWUS41 KBUF 221909`, `FROSTBITE IN AS LITTLE AS 30 MIN`, `STAY WITH YOUR VEHICLE`, `NWS Buffalo Blizzard Warning, 22 Dec 2022, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "The Weather Service" | ground on frame 0; panel `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)` at 0.10; header lines at 0.40 and 0.60; source in |
| 1.10-3.12 | "told people what to do" | body lines B1-B6 fade up dim (`#dfe7ee` at 45 %) line by line, 0.25 s apart from 1.10 |
| 4.44 | "Thursday" @4.44 | header line 2 brightens to `#f2f5f8`, 0.3 s |
| 5.14 | "Frostbite" @5.14 | B1-B3 to full opacity; highlight 1 draws over 0.9 s (B2 part then B3 part) |
| 7.00 | "30" @7.00 | C1 in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` |
| 9.40 | "stranded" @9.40 | C1 out `to(x:-80, autoAlpha 0, 0.4, power3.in)`; B4-B6 to full opacity |
| 11.22 | "Stay with your vehicle." @11.22 | highlight 2 draws over 0.6 s; C2 in at 11.58 (as C1) |
| 12.68 | "Andal did exactly that." @12.68 | highlight 2 pulses once (opacity .30 -> .5 -> .30, 0.6 s) |
| 14.42-18.10 | "She wrote to her sisters ... if she got out." | panel slow push `scale 1 -> 1.04` (linear, centre origin; chips and source on a fixed HUD layer); no new text |
| 17.76-18.36 | after "out." @18.10 | C2, panel and source out `to(autoAlpha 0, y:30, 0.6, power3.in)`; ground stays |
Comp duration 18.36 s.

## 6. CONTRACT
One file `compositions/g-a3-7-warning-card.html`, root `id="g-a3-7-warning-card-root"`, `data-composition-id="g-a3-7-warning-card"`, PAUSED timeline `window.__timelines["g-a3-7-warning-card"]`. Prefix `wc-`. Text faded to 0 before it could leave the margin during the push (it cannot at 1.04, check). Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-7-warning-card`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-7-warning-card`. Dup-fact: "30" appears in B3 and C1 at once by design (the chip names the highlighted line): declare `data-repeat-ok="chip names the highlighted product line"` on the C1 leaf after the frame read.

## 7a. DONE LINE
All seven items of the template 7a.

## 8. RECEIPT
As the template.
