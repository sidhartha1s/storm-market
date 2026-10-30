# g-a4-7-guard-bars · A4-S6 (8.80 s to end) · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file, "RHS stat panel" in particular), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/stat-panel.html` (RHS panel and its slide) with bar rails from `library/inhouse/ranked-bars.html`; `references/editing-patterns/ep5-glass-stat-panel.html` for the glass look over a photo.

## 0. What this graphic claims
The Guard started small and grew: 54 on duty on Christmas Eve, a peak of 701 on duty on 29 December, and 849 called up in all. Three counts at different times, on one scale.

## 1. SOURCE
- DVIDS news 436223, Eric Durr, 3 Jan 2023 (PRIMARY): "The mission kicked off Christmas Eve morning, December 24, with 54 personnel on duty." "By Dec. 29 the number of troops on duty reached its peak at 701." "Eight hundred and forty-nine Soldiers and Airmen took part". `research/response.md` section 4 final row; `factcheck/a4-r1.md` rows 20, 21, 22 (CONFIRMED). The three totals are different points in time, not conflicts (`research/response.md` section 4 caution). 849 is on screen only, never spoken.
- Footage under it: DVIDS D1, 7572835, 107th Attack Wing (Niagara Falls) Airmen help rescue a motorist and his dog stuck in drifts near Buffalo, 24 Dec 2022, courtesy photo: `research/cc-clips-r2.md` row D1, https://www.dvidshub.net/image/7572835.

## 2. DATUM, SCALE, ORIENTATION
Overlay over the D1 photo. RHS panel per `references/mg-quickref.md` "RHS stat panel": `right:0; top:0; bottom:0; width:820px`, gradient `linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0))`, padding 90 px 96 px 0 170 px. Solid text zone x 1270 to 1824.
Bar scale: one shared axis, 849 people = 500 px, so 0.5889 px per person. Bars start at x 1270.
Presenter circle may be on: all text and bars stay above y 660; nothing new in x >= 1600, y >= 680.

## 3. GEOMETRY (px)
- Eyebrow "NEW YORK NATIONAL GUARD": Arial 700 22 px `#93a3b2`, letter-spacing 6, left x 1270, baseline y 160.
- Row 1: header line baseline y 262: "DEC 24 · " Arial 700 30 px `#93a3b2` + "54" Arial Black `font-weight:900` 52 px `#f2f5f8`. Bar y 282 to 310, fill `#dfe7ee`, width 31.8 px (54 x 0.5889).
- Row 2: header baseline y 392: "DEC 29 · " Arial 700 30 px `#93a3b2` + "701" Arial Black 900 52 px `#e74c3c` + " ON DUTY" Arial 700 30 px `#dfe7ee`. Bar y 412 to 440, fill `#e74c3c`, width 412.8 px (701 x 0.5889).
- Row 3 (ghost): header baseline y 522: "849" Arial Black 900 52 px `#93a3b2` + " CALLED UP" Arial 700 30 px `#93a3b2`. Ghost bar y 542 to 570: no fill, 2 px dashed (8/6) `#93a3b2` outline, width 500 px.
- Axis: a 1 px `#2a3644` vertical line at x 1270 from y 276 to 576 (the shared zero).
- Source pill: glass (as `g-intro-2-toll-chips`), radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0` (on the photo side, outside the panel).
- Type tiers: 52 (big), 30 (mid), 19 and 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. All three bars share one zero at x 1270 and one scale: widths 31.8, 412.8 and 500 px (±2 px), ratios 54 : 701 : 849.
2. The 54 bar is visibly tiny next to 701 ("it started small").
3. 849 is the ghost (outline only, grey) and reads as a different kind of count from "ON DUTY"; it is never spoken and never coloured like the 701.
4. Every text and bar sits inside the solid zone (x >= 1270) and above y 660.
5. The panel leaves the left 1,100 px of the photo clear: the airmen, the driver and the dog stay visible (the orchestrator checks a settled frame; if they sit right of x 1100, the index reframes the photo, not this comp).

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S6 start, `audio/a4-s6.words.json`; comp-local = S6 time - 8.80)
Strings: `NEW YORK NATIONAL GUARD` · `DEC 24 · 54` · `DEC 29 · 701 ON DUTY` · `849 CALLED UP` · source `New York National Guard, DVIDS, 3 Jan 2023`

| S6 t (s) | local | spoken word | action |
|---|---|---|---|
| 8.86 | 0.06 | "That was Christmas Eve" @8.86 | panel in `fromTo(x:660 -> 0, 0.7, power3.out)`; eyebrow in at 9.20 `fromTo(autoAlpha 0, y:16 -> 0, 0.4)`; source pill in |
| 9.20 | 0.40 | "Christmas" @9.20 | row 1 header "DEC 24 · " in `fromTo(autoAlpha 0, y:24 -> 0, 0.4)` |
| 10.42 | 1.62 | "54" @10.42 | "54" `fromTo(scale 1.3 -> 1, autoAlpha 0 -> 1, 0.4, power4.out)`; bar 1 `scaleX 0 -> 1, 0.5, power2.out, transformOrigin left center` |
| 13.38 | 4.58 | "December" @13.38 | row 2 header "DEC 29 · " in (as row 1) |
| 14.60 to 15.30 | 5.80 to 6.50 | "701" @15.08 | bar 2 `scaleX 0 -> 1, 0.6, power2.out` from 14.70; "701" counts on a leaf from 54 (first tick) to 701, `power4.out`, lands 15.30; " ON DUTY" in at 15.20 |
| 15.90 | 7.10 | before "but" @16.36 | row 3: ghost bar outline draws (dashoffset, 0.5 s), "849 CALLED UP" in `fromTo(autoAlpha 0, y:24 -> 0, 0.4)` |
| whole window | | | rows float `y 0 -> -3`, sine, finite repeats; a 2 px `#dfe7ee` scan glint travels along bar 2 every 2.5 s (finite repeats) |
| 18.24 to 18.84 | 9.44 to 10.04 | after "rescue." @18.40 | panel and pill out `to(x:980, autoAlpha 0, 0.6, power3.in)` |

Comp duration 10.04 s (host = A4-S6 start + 8.80 to the end of the S6 wav, 18.84). The photo runs alone 0 to 8.80.

## 6. CONTRACT
One file `compositions/g-a4-7-guard-bars.html`, root `<div id="g-a4-7-guard-bars-root" data-composition-id="g-a4-7-guard-bars" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-7-guard-bars"]`. Ids prefixed `gb-`; classes prefixed `gb-`. Root transparent. Counter writes only a leaf span. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-7-guard-bars`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-7-guard-bars`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: bar widths computed from 0.5889 px per person by a script. Item 7: one frame at local 7.8 composited over DVIDS 7572835.

## 8. RECEIPT
As the template.
