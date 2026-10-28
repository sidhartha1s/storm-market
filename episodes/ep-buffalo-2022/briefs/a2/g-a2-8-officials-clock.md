# g-a2-8-officials-clock · A2-S7 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/stat-timeline.html` (horizontal chronology rail) for the lanes; the beige cite card of `library/inhouse/quote-card.html` for the two quoted sources.
FAMILY BASE for `g-a2-9-ban-bracket` (Opus) and `g-a2-11-both-lanes` (Sonnet). Section 3 is the shared table; build this first and send it alone for a full-size read.

## 0. What this graphic claims
1. Two clocks ran on Friday morning: the weather (7:24 rain, 8:06 gusts near 60 mph, 8:39 quarter-mile visibility) and the officials'. The statewide State of Emergency, declared Thursday, took effect at 6:00 AM, well before any of the weather rows, while it was still raining.
2. That order set no driving ban for Erie County; such decisions were left to local leaders, which a city-commissioned review said likely led to a wait-and-see approach.

## 1. SOURCE
- Weather markers: 7:24 RAIN · 38°F (`factcheck/a2-r1.md` row 1), 8:06 gust 52 kt = about 60 mph (row 5), 8:39 vis 1/4 mi (row 13); `research/nws.md` 2.2, 2.3.
- State of Emergency declared Thu 22 Dec, in effect 6 AM Fri 23 Dec: `research/response.md` section 1 (governor.ny.gov 24 Dec and 23 Dec releases, PRIMARY); `factcheck/a2-r1.md` rows 25 and 26 (CONFIRMED). Still raining at 6: row 26 (ASOS 6:01 to 6:37 AM rain).
- Release sentence on the cite card, verbatim (row 25, 23 Dec 2022 release, https://www.governor.ny.gov/news/governor-hochul-provides-update-states-response-efforts-winter-storm-impacting-holiday-travel): "On Thursday, Governor Hochul declared a statewide State of Emergency ahead of the event, which went into effect at 6 a.m. Friday." (The Picture asked for a screenshot of the page; none was captured, `media/candidates/a2/picks.md`. This typeset cite card replaces it.)
- Thruway commercial-vehicle ban from 6 a.m. Fri: row 27 (22 Dec release). Erie expressway closures being prepared from 6 a.m. Fri (SR 400, SR 219, I-290, I-190, SR 5): row 28 (22 Dec release, "preparing to close").
- No driving restriction in EO 26; local decision: rows 28 and 29.
- NYU Wagner review via AP, 2 Jun 2023 (SECONDARY), verbatim as fetched (row 30): "This likely led to a wait-and-see approach leading up to the blizzard". Commissioned by the City of Buffalo: `research/response.md` section 5.
- Source lines: "Buffalo airport ASOS, IEM archive" (weather lane) then "Office of the Governor, 22 to 24 Dec 2022" (the Picture said "23 and 24"; the truck ban and closures come from the 22 Dec release). Hidden while a cite card shows (the card carries its own attribution).

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed graphic, channel ground on the root from frame 0. One time axis shared by both lanes: x(t) = 200 + 5 px per minute after 5:30 AM. 5:30 = 200, 10:00 = 1550. Earlier is left.

## 3. GEOMETRY (px; SHARED with g-a2-9 and g-a2-11, do not change without saying so in the receipt)
Key x: 6:00 350 · 7:00 650 · 7:24 770 · 8:00 950 · 8:06 980 · 8:15 1025 · 8:39 1145 · 8:50 1200 · 9:00 1250 · 9:30 1400 · 10:00 1550.
- Weather lane:
  - Label "AIRPORT WEATHER LOG" Arial 700 22 px `#93a3b2` letter-spacing 6, left 200, top 150.
  - Axis 2 px `rgba(255,255,255,.3)` at y 470, x 200 to 1550. Hour ticks 8 px down at 350, 650, 950, 1250, 1550. Hour labels Arial 700 19 px `#93a3b2`, centred on the ticks, glyph box y 482 to 504: "6 AM" "7 AM" "8 AM" "9 AM" "10 AM".
  - Markers (tick 2 px `#93a3b2` from the label top down to the axis; label block left = tick x + 12; line 1 Courier New 700 26 px `#e8c56a`, line 2 Arial 700 24 px `#dfe7ee` 4 px below):
    | id | x | tick / label top y | line 1 | line 2 | label box |
    |---|---|---|---|---|---|
    | M1 | 770 | 220 | 7:24 AM | RAIN · 38°F | x 782 to ~950, y 220 to 282 |
    | M2 | 980 | 290 | 8:06 AM | GUSTS ~60 MPH | x 992 to ~1200, y 290 to 352 |
    | M4 | 1145 | 376 | 8:39 AM | VIS 1/4 MI | x 1157 to ~1310, y 376 to 438 |
    (M3, 8:15 "BELOW 32°F", hangs BELOW the axis and belongs to g-a2-9: tick x 1025 from y 470 to 516, label top 516, box x 1037 to ~1190, y 516 to 578.) No tick crosses another marker's label: verify on the frame.
- Officials lane:
  - Label "THE OFFICIALS' CLOCK" Arial 700 22 px `#93a3b2` letter-spacing 6, left 200, top 560.
  - Axis 2 px `rgba(255,255,255,.3)` at y 700, x 200 to 1550; hour ticks 8 px UP at the same x (no labels: the weather axis carries them).
  - Card row: every officials card top 600, height 76 (bottom 676), radius 10, connector 3 px from the card's anchor corner down to the axis (y 676 to 700). All officials cards stay at y < 680 so the corner rule holds even where x > 1600.
  - SoE card: left 350 (anchored at 6:00), fill `#15202b`, 1 px `rgba(255,255,255,.14)` border, 4 px `#d8a13a` left edge, padding 10 px 18 px. Line 1 "STATE OF EMERGENCY" Arial Black `font-weight:900` 26 px `#f2f5f8`; line 2 "DECLARED THU · IN EFFECT 6:00 AM FRI" Arial 700 19 px `#c8d3e0`. About x 350 to 820. Connector `#d8a13a` at x 350.
  - Dashed slot "NO ERIE COUNTY DRIVING BAN": left 880, width 420 (x 880 to 1300), y 600 to 676, 2 px dashed `#93a3b2` border (8/6), no fill, text Arial 700 22 px `#93a3b2` letter-spacing 2, centred. No connector (it is an absence, not a time).
  - Under-axis chips (this comp only, gone before it ends): left 350, Arial 700 19 px `#c8d3e0`, a 1 px `#93a3b2` hairline from (350, 700) down to each: C1 "THRUWAY TRUCK BAN · 6 AM" glyph box y 716 to 740; C2 "ERIE EXPRESSWAY CLOSURES PLANNED · 6 AM" y 750 to 774.
- Cite card zone (one card at a time): beige `rgba(232,222,200,.90)`, radius 14, x 410 to 1510, y 790 to 960, padding 26 px 40 px. Quote Georgia italic 30 px `#2a2622`, at most 2 lines; attribution Arial 700 19 px `#6b6257` letter-spacing 2, last line. Highlight = `rgba(216,161,58,.35)` bar behind the named words, drawn `scaleX 0 -> 1`, transformOrigin left.
  - Card G: quote as section 1 (governor), highlights on "declared a statewide State of Emergency" and "6 a.m. Friday"; attribution "OFFICE OF THE GOVERNOR · RELEASE, 23 DEC 2022".
  - Card N: "… likely led to a wait-and-see approach leading up to the blizzard …", highlight on "wait-and-see approach"; attribution "NYU WAGNER REVIEW FOR THE CITY OF BUFFALO · VIA AP, 2 JUN 2023".
- Source line Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px` (ends before x 700; card bottom 960).
- Type tiers: 26 to 30 mid, 19 to 24 small; big tier = none by design in the lanes. Declare `data-type-ok="two-lane timeline: mid/small tiers by design, big tier lives on the S8 ban card"` on the root ONLY if `graphics_qc` flat-type fails; otherwise none.
- Corner x >= 1600, y >= 680: empty.

## 4. MUST BE TRUE IN THE PICTURE
1. One time axis: a marker at time t sits at x(t) ±3 px on both lanes. The SoE card's anchor (x 350) is 420 px LEFT of the 7:24 marker (x 770): "well left of the 7:24 rain row".
2. Weather markers in time order left to right, each label beside its own tick, no tick through a label.
3. The SoE card names both days (declared THU, in effect 6:00 AM FRI).
4. The dashed slot reads as an empty place for a ban (no clock time, no colour of the S8 red card).
5. Quotes exactly as section 1, with ellipses on card N; quote marks not added inside the text.
6. One cite card at a time; the source line is hidden while a cite card is up.
7. Nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A2-S7 start, `audio/a2-s7.words.json`)
Strings: section 3 strings; sources `Buffalo airport ASOS, IEM archive` · `Office of the Governor, 22 to 24 Dec 2022`.
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0, "So" | ground only |
| 0.10 | "who" @0.16 | weather label in; weather axis draws left to right 0.6 s, power2.out; hour labels stagger 0.05; ASOS source line in |
| 0.70 / 1.00 / 1.30 | "told them to stay off the roads" | M1, M2, M4: tick `scaleY 0 -> 1` from the axis 0.3 s, then label `fromTo(autoAlpha 0, y:10 -> 0, 0.3)` |
| 2.68 | "officials" @2.68 | officials label in; officials axis draws 0.6 s |
| 4.08 | "clock." @4.08 | officials hour ticks pop, stagger 0.06 |
| 5.20 | "Kathy" @5.20 | source line out; card G `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)` |
| 6.12 | "declared" @6.12 | highlight 1 draws 0.8 s |
| 9.64 | "effect" @9.64 | highlight 2 draws 0.5 s |
| 10.18 | "six" @10.18 | SoE card `fromTo(y:-30 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; connector draws |
| 12.30 | "raining." @12.30 | M1 pulse `scale 1 -> 1.08 -> 1, 0.4`; card G out `to(y:30, autoAlpha 0, 0.5, power3.in)` 12.4 to 12.9; governor source line in at 12.9 |
| 15.28 | "banned" @15.28 | C1 hairline + text `fromTo(autoAlpha 0, x:-12 -> 0, 0.3)` |
| 20.14 | "close" @20.14 | C2 in, same |
| 22.04 | "six." @22.04 | SoE connector pulse (amber ring at (350, 700), scale 1 -> 2, fade, 0.8 s) |
| 22.90 | "But" @22.90 | C1, C2 out `to(autoAlpha 0, 0.3)` |
| 24.72 | "no" @24.72 | dashed slot: border draws (strokeDashoffset or 4 sides scaleX/Y) 0.5 s, then text in |
| 25.34 | "ban" @25.34 | slot text pulse `scale 1 -> 1.05 -> 1` |
| 29.38 | "A review" @29.38 | source line out; card N in (as card G) |
| 34.28 | "wait" @34.28 | highlight "wait-and-see approach" draws 0.6 s |
| whole window | | lane group float `y: 0 -> -3`, sine.inOut, finite yoyo; nothing holds still 4 s |
| 35.60 to 36.20 | after "approach." @35.14 | card N out `to(y:30, autoAlpha 0, 0.6, power3.in)`. Lanes, markers, SoE card and dashed slot STAY (they are g-a2-9's frame 0) |
Comp duration 36.20 s.

## 6. CONTRACT
One file `compositions/g-a2-8-officials-clock.html`, root `<div id="g-a2-8-officials-clock-root" data-composition-id="g-a2-8-officials-clock" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-8-officials-clock"]`. Ids/classes `oc-`. Marker x computed from x(t) in the script. Mark the shared block with a comment "LANE FAMILY BASE" so g-a2-9/11 copy it whole. Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-8-officials-clock`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-8-officials-clock`; `node scripts/overlap_check.mjs episodes/ep-buffalo-2022`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: print x(t) for every marker and card anchor in the receipt.

## 8. RECEIPT
As the template.
