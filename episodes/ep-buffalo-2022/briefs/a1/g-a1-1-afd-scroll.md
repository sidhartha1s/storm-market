# g-a1-1-afd-scroll · A1-S1 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `episodes/ep-buffalo-2022/compositions/g-intro-7-afd-card.html` (same episode, same AFD panel look, already in the channel palette) and `library/inhouse/bulletin-typewriter.html` for the leaf-span pattern. Change: the body is not typed, it SCROLLS inside a masked window; one sentence gets an amber marker highlight. FAMILY BASE for `g-a1-2-jet-section` (its first state is this comp's last frame) and `g-a1-8-afd-rare` (same panel, other product). Send it alone for a full-size read before those two are built.

## 0. What this graphic claims
Three days out (4:51 AM Tue 20 Dec 2022) the NWS Buffalo forecast discussion said, in its own words, "One could certainly describe this storm system as a once in a generation type of event." The sentence sits inside a long, ordinary technical product: that is why it is shown in the raw text, not as a quote card.

## 1. SOURCE
- NWS Buffalo Area Forecast Discussion FXUS61 KBUF 200951 (AFDBUF), "451 AM EST Tue Dec 20 2022". `research/nws.md` row 1.9 (PRIMARY); `factcheck/a1-r1.md` rows 1, 4, 6 (CONFIRMED). IEM: https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=AFDBUF&sdate=2022-12-18T12:00Z&edate=2022-12-22T12:00Z&fmt=text&limit=60
- Text below re-fetched from IEM by the brief writer 28 Oct 26; line breaks are the product's own. Do not retype from memory: copy these strings.

Header (top of the product):
```
Area Forecast Discussion
National Weather Service Buffalo NY
451 AM EST Tue Dec 20 2022
```
Scrolling body, lines B0 to B35 (the .LONG TERM section from its heading to "in the overall solution."; empty lines are kept as empty rows):
```
B0  .LONG TERM /THURSDAY NIGHT THROUGH MONDAY/...
B1  ...Incredibly Powerful Storm To Impact our Region Heading Into and
B2  THROUGH the Christmas Weekend...
B3
B4  An extremely amplified longwave pattern during this period will
B5  spawn one of the most intense storm systems in decades to impact the
B6  Mid West and Great Lakes region. This system will likely end up
B7  setting low pressure records once it passes north of the border and
B8  will have the potential to generate at least storm force winds over
B9  the Lower Great lakes.
B10
B11 As if the very real threat for damage producing winds were not
B12 enough...there will also be the risk for a prolonged...paralyzing
B13 heavy lake effect snow event. All of this coming in the days leading
B14 up to...and through Christmas. Headlines (watches) will likely be
B15 issued within the next few forecast cycles.
B16
B17 Explosive cyclogenesis will take place over the mid western states
B18 Thursday night and southern Ontario on Friday...as an anomalously
B19 strong 150kt H25 jet will pass through the base of a very deep
B20 longwave trough. This will support rapid deepening of a
B21 corresponding sfc low that will track from Indiana north-northeast
B22 to southern Ontario by late Friday. The low will deepen from roughly
B23 1000mb Thursday evening to roughly 968mb by Friday evening...easily
B24 meeting the definition of bombogenesis (24mb/24hrs). Such deepening
B25 is relatively rare in the Lower Great lakes...but more common across
B26 the Upper Great Lakes and certainly with Nor'easters along the coast.
B27 Some of the parameters of this intense storm are forecast to be
B28 climatologically 'off the charts'...such as MSLP and strength of
B29 both the low level and upper level jets. One could certainly
B30 describe this storm system as a once in a generation type of event.
B31 Its worth noting that the guidance continues to come into better
B32 agreement with the strengthening and track of this system with most
B33 of the packages coming into line with the consistent ECMWF solution
B34 of a few days ago. This agreement is allowing for increased confidence
B35 in the overall solution.
```
(The "Bn" prefixes are row ids for this brief, not on screen.) `g-a1-2` appends rows B36 to B51 (the next paragraph); build the scroll stack with all 52 rows now, B36 to B51 sitting below the window, so g-a1-2 copies it unchanged.

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed graphic, no geographic scale. Ground: channel radial gradient (tokens.md "Canvas") on a child `as-ground`, on from frame 0. Courier New 700 28 px has a 16.8 px advance (0.6 em): the longest row (B34, 70 chars) is 1176 px. Row pitch 44 px. Corner x >= 1600, y >= 680 stays empty (presenter circle).

## 3. GEOMETRY (px, 1920x1080)
- Chip "TUE DEC 20 · 4:51 AM": Arial Black `font-weight:900` 52 px `#e8c56a`, left 200, top 110. No card behind it.
- Panel `as-panel`: x 170 to 1530, y 200 to 900, radius 28, fill `linear-gradient(180deg, #15202b, #0b1016)`, 1 px `rgba(255,255,255,.14)` border. Its lower-right corner (1530, 900) is left of the circle zone (x < 1600).
- Header: Courier New 700 26 px `#93a3b2`, letter-spacing 0, left 230, tops 226, 262, 298 (the three header lines, mixed case exactly as the product).
- Product id "FXUS61 KBUF 200951": Courier New 400 19 px `#93a3b2`, right-aligned to x 1470, top 230.
- Divider: 1 px `rgba(255,255,255,.14)`, x 230 to 1470, y 344.
- Scroll window `as-win`: x 230 to 1470, y 364 to 872 (508 px tall, `overflow:hidden`), top and bottom 40 px feathered with a mask-image gradient so rows fade, never clip mid-glyph.
- Scroll stack `as-stack` inside the window: row Bn top = 364 + 12 + n*44 - offset (offset 0 at start). Body rows Courier New 700 28 px `#dfe7ee`, letter-spacing 0, left 230, `white-space:pre`. Heading rows B0 to B2 in `#93a3b2`.
- End offset 1100 px: row B30 then sits at top 364 + 12 + 1320 - 1100 = 596 (window middle). Row B29 at 552.
- Highlight `as-hl`: two rects behind the text, fill `#e8c56a`, radius 4, height 38, the text on them turning `#04070c` as the rect passes. Rect 1 covers "One could certainly" on B29 (chars 41 to 59 counted from 0, so x 230 + 41*16.8 = 918.8 to 230 + 60*16.8 = 1238, compute from the glyph boxes, do not trust this arithmetic over the measured box). Rect 2 covers the whole of B30 (x 230 to 230 + 67*16.8 = 1355.6). Both `scaleX 0 -> 1`, transformOrigin left center.
- Source line "NWS Buffalo Area Forecast Discussion, FXUS61 KBUF 200951, IEM archive": Arial 400 19 px `#c8d3e0`, left 96, bottom 54.
- Type tiers: 52 (chip), 26 to 28 (header, body), 19 (id, source). Three tiers.

## 4. MUST BE TRUE IN THE PICTURE
1. Every row on screen is the product's text character for character, with the product's line breaks. No word is cut at the left or right edge in any frame (rows are 1176 px max inside a 1240 px window).
2. The highlighted words are exactly "One could certainly" + "describe this storm system as a once in a generation type of event." and nothing else.
3. Header reads 451 AM EST Tue Dec 20 2022; chip reads TUE DEC 20 · 4:51 AM; they agree.
4. The highlight never runs ahead of the voice: each rect finishes no earlier than the last word it covers is spoken.
5. Rows enter and leave the window through the feathered edges, never sliced by a hard edge.
6. Corner x >= 1600, y >= 680 empty in every frame.

## 5. PANEL TEXT (exact) and CUES (seconds from A1-S1 start, `audio/a1-s1.words.json`)
Strings: `TUE DEC 20 · 4:51 AM` · the 3 header lines · `FXUS61 KBUF 200951` · rows B0 to B51 · `NWS Buffalo Area Forecast Discussion, FXUS61 KBUF 200951, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Tuesday," @0.00 | ground on at frame 0; chip `fromTo(autoAlpha 0, x:-40 -> 0, 0.5, power3.out)` from 0.05 |
| 0.90 | "December" @0.90 | panel `fromTo(y:60 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)`; source line in (autoAlpha, 0.4) |
| 2.18 | "451" @2.18 | header rows in one by one, `fromTo(autoAlpha 0, x:-20 -> 0, 0.35)` at 2.18, 2.50, 2.82; product id at 3.00 |
| 3.24 | "morning," @3.00 to 3.24 | divider `scaleX 0 -> 1, 0.5, power2.out`; body rows visible in the window from 3.40 (stack `autoAlpha 0 -> 1, 0.5`) |
| 5.74 | "Weather Service Office in Buffalo" @5.74 to 6.78 | header row 2 brightens to `#f2f5f8`, 0.3 s |
| 7.78 | "forecast discussion." @7.78 | header row 1 brightens to `#f2f5f8`, 0.3 s |
| 9.28 to 18.62 | "It was a long, semi-technical note ... It said," @9.28 to 18.74 | stack scrolls `y: 0 -> -1100`, `ease:"power1.inOut"`, 9.28 to 18.62 (about 118 px/s mid-scroll) |
| 19.64 to 20.50 | "One could certainly" @19.64 to 20.50 | rect 1 `scaleX 0 -> 1`, ease none |
| 20.50 to 23.62 | "describe ... type of event." @20.50 to 23.62 | rect 2 `scaleX 0 -> 1`, ease none (it tracks the voice across the row) |
| 23.94 | end of speech @23.94 | every row except B29 and B30 `to(opacity 0.35, 0.5)`; the highlight rects pulse `scaleY 1 -> 1.08 -> 1, 0.6` |
| 24.6 to 25.2 | tail | hold (ground drift: the panel floats `y 0 -> -4`, sine, 23.94 to 25.2) |
Comp duration 25.2 s. Spoken time in a comment at each tween.
Exit: none. The comp ends on its settled state (offset 1100, highlight on, other rows at 0.35) because `g-a1-2-jet-section` opens on exactly that frame (a cut between identical frames). Tell the orchestrator if the S1 to S2 pause on the timeline is over 1 s: the hold then needs the float to keep running.

## 6. CONTRACT
One file `compositions/g-a1-1-afd-scroll.html`, root `<div id="g-a1-1-afd-scroll-root" data-composition-id="g-a1-1-afd-scroll" data-width="1920" data-height="1080">`. PAUSED timeline at `window.__timelines["g-a1-1-afd-scroll"]`. Ids and classes prefixed `as-`. Start-hidden elements hidden in CSS too. Text pre-authored per row (one leaf per row; the highlighted rows split into leaf spans so the dark-on-amber text is a leaf). Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a1-1-afd-scroll`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a1-1-afd-scroll`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 3: frame 0 is the ground with the chip about to enter. Extra: frames at 9.28 and 18.62 (both ends of the scroll) show whole rows, no row cut at the window edges.

## 8. RECEIPT
As the template.
