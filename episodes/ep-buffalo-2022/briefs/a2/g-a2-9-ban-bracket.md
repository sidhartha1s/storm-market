# g-a2-9-ban-bracket · A2-S8 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from the BUILT `compositions/g-a2-8-officials-clock.html` (after its full-size read): copy the "LANE FAMILY BASE" block whole, rename `oc-` to `bb-`. All lane px are `briefs/a2/g-a2-8-officials-clock.md` section 3; this brief adds to them.

## 0. What this graphic claims
1. Erie County's driving ban, from County Executive Mark Poloncarz, took effect at 9:30 AM: 84 minutes after the airport first logged gusts near 60 mph (8:06), and after the 8:39 quarter-mile row.
2. A local station's live blog posted it at 8:50, 40 minutes before it took effect.
3. Officials expected the snow band at 10 AM and waited partly so workers could get home before freezing; the airport had crossed freezing around 8:15. People who left at 7 were still on the road when it landed.

## 1. SOURCE
- Ban effective 9:30 AM Fri 23 Dec, issued by Poloncarz: `research/response.md` section 1 (WKBW, https://www.wkbw.com/news/local-news/erie-county-driving-ban-effective-9-30-a-m-friday, SECONDARY); `factcheck/a2-r1.md` row 31 (CONFIRMED).
- 8:06 to 9:30 = 84 min; gusts 52 to 58 kt from 8:06 on: `factcheck/a2-r1.md` row 32 (CONFIRMED, "8:06 to 9:30 = 84 min").
- WKBW live blog "Friday 8:50 a.m.: A driving ban will take effect for all of Erie County starting at 9:30 a.m. Friday": row 33 (CONFIRMED as a post time; 8:50 to 9:30 = 40 min). Chip wording from row 35 / the Picture: "POSTED 8:50 AM · WKBW LIVE BLOG".
- Expected the snow band at 10 a.m.; waited so workers could get home before freezing: row 34 (AP via ABC7, FETCHED; Poloncarz asked Wed 28 Dec).
- Air below 32°F about 8:15: row 10.
- Lower third: Mark Poloncarz, Erie County Executive (row 31).
- Source lines in turn: "Erie County driving ban, WKBW" · "AP via ABC7, 28 Dec 2022" · "Buffalo airport ASOS, IEM archive".

## 2. DATUM, SCALE, ORIENTATION
As g-a2-8: x(t) = 200 + 5 px per minute after 5:30 AM. 7:00 650, 8:06 980, 8:15 1025, 8:39 1145, 8:50 1200, 9:30 1400, 10:00 1550. Full-frame designed, ground on the root from frame 0.

## 3. GEOMETRY (px; additions to g-a2-8 section 3)
- Frame 0 = g-a2-8's end state: both lanes, hour labels, M1, M2, M4, SoE card, dashed slot, lane labels. No cite card, no source line, no C1/C2.
- Ban card (replaces the dashed slot; RIGHT edge anchored at 9:30 so it stays out of the corner): x 960 to 1400, y 600 to 676, fill `#8e2020` (Crimson), radius 10, padding 10 px 18 px. Clock icon 44 px at left (ring 3 px `#f4f0e8`, hands at 9:30). Line 1 "DRIVING BAN · 9:30 AM" Arial Black `font-weight:900` 26 px `#f4f0e8`; line 2 "ERIE COUNTY" Arial 700 19 px `#f4f0e8` letter-spacing 3. Connector 3 px `#c0392b` at x 1400 from y 676 to 700.
- 84 MIN bracket: path `M 1400 600 V 250 H 980 V 290`, 3 px `#c0392b`, drawn from the ban card back to the 8:06 tick top (strokeDashoffset, length = ceil(measured) + 1). It crosses the weather axis at (1400, 470) only. Label "84 MIN" Courier New 700 30 px `#e8c56a`, centred x 1190, glyph box y 206 to 236 (14 px above the bar, never on it).
- 8:39 is covered by the bracket span: M4's label brightens (`#dfe7ee` -> `#f2f5f8`, scale pulse) as the bar passes over x 1145. No extra drop tick (it would cut through M2's label).
- Lower third (glass card, tokens.md "Surfaces"): `left:110px; bottom:110px`, padding 18 px 30 px. Line 1 "MARK POLONCARZ" Arial Black `font-weight:900` 52 px `#f2f5f8`; line 2 "ERIE COUNTY EXECUTIVE" Arial 700 26 px `#dfe7ee` letter-spacing 2. About x 110 to 640, y 850 to 970.
- 8:50 chip: hairline 1 px `#93a3b2` x 1200 from y 700 to 740; chip centred x 1200, y 740 to 776 (about x 1030 to 1370), fill `rgba(147,163,178,.18)`, radius 10, padding 6 px 14 px, text "POSTED 8:50 AM · WKBW LIVE BLOG" Arial 700 19 px `#c8d3e0`.
- 40 MIN span: path `M 1200 786 V 796 H 1400 V 786`, 2 px `#e8c56a`; label "40 MIN" Courier New 700 26 px `#e8c56a`, centred x 1300, glyph box y 804 to 830.
- 10 AM marker (after the 8:50 chip and 40 MIN leave): dashed 2 px `#93a3b2` tick x 1550 from y 700 to 740; label "SNOW BAND EXPECTED · 10 AM" Arial 700 19 px `#c8d3e0`, right edge x 1550, glyph box y 744 to 768.
- M3 (below the weather axis): tick 2 px `#c0392b` x 1025 from y 470 to 516; label left 1037, top 516: "8:15 AM" Courier New 700 26 px `#e8c56a` / "BELOW 32°F" Arial 700 24 px `#7fb2e5`.
- Commute marker: tick 2 px `#e8c56a` x 650 from y 700 to 740; label "LEFT AT 7:00" Arial 700 19 px `#e8c56a`, centred x 650, glyph box y 744 to 768. Travel bar 4 px `#e8c56a` at y 716, x 650 to 1400, `scaleX 0 -> 1` from the left.
- Source line `left:96px; bottom:54px`, Arial 400 19 px `#c8d3e0`; never under the lower third (lower third bottom edge 970, source glyph box about 1002 to 1026).
- Type tiers: 52 (lower third), 26 to 30, 19 to 24. Corner x >= 1600, y >= 680 empty (10 AM label ends at x 1550).

## 4. MUST BE TRUE IN THE PICTURE
1. The ban card's right edge and connector sit at x 1400 (9:30) ±3; the bracket's two ends sit at x 1400 and x 980 (8:06): 420 px = 84 min at 5 px/min.
2. The 40 MIN span runs x 1200 to 1400 = 200 px = 40 min.
3. The 8:15 marker sits at x 1025, left of 8:39 and well left of 9:30; the 10 AM marker at x 1550, right of the ban.
4. The ban card is visibly not a weather row (crimson, on the officials lane only).
5. One source line at a time and it names what just landed; lower third gone before the 8:50 chip lands.
6. No label under the bracket, the travel bar or another label (check frames at 10, 16, 31, 36 s).
7. Nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A2-S8 start, `audio/a2-s8.words.json`; Whisper spells the name "Paulenkars")
Strings: section 3 strings; sources `Erie County driving ban, WKBW` · `AP via ABC7, 28 Dec 2022` · `Buffalo airport ASOS, IEM archive`.
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0 | g-a2-8 end state |
| 0.68 | "ban" @0.68 | dashed slot border pulse (anticipation) |
| 2.22 | "Mark" @2.22 | lower third `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`, line 2 0.15 later |
| 4.38 | "9" @4.38 | dashed slot `to(autoAlpha 0, 0.25)`; ban card `fromTo(y:-40 -> 0, autoAlpha 0 -> 1, 0.45, back.out(1.3))`; connector draws; WKBW source in |
| 6.58 | "logging" @6.58 | M2 label pulse `scale 1 -> 1.06 -> 1` |
| 6.86 to 9.16 | "gusts near 60 ... an hour" | bracket draws from the ban card back to 8:06 (2.3 s, power1.inOut); M4 label brightens as the bar passes x 1145 |
| 9.16 | "an hour and a half" @9.16 | "84 MIN" `fromTo(autoAlpha 0, y:8 -> 0, 0.35, power3.out)` |
| 7.20 to 7.80 | | lower third out `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
| 12.36 | "posted" @12.36 | 8:50 hairline draws, chip `fromTo(autoAlpha 0, y:10 -> 0, 0.35)` |
| 15.34 | "40" @15.34 | 40 MIN span draws 0.5 s; label in |
| 18.20 to 18.50 | before "Paulenkars" @18.40 | 8:50 chip, hairline, 40 MIN span and label out (0.3 s); bracket and "84 MIN" fade to 0.4 |
| 18.40 | "Paulenkars said" | source swaps to "AP via ABC7, 28 Dec 2022" |
| 22.06 | "until 10." @22.06 | 10 AM tick + label in |
| 25.96 | "before the temperature dropped below freezing" | 10 AM label pulse |
| 28.22 | "but" @28.22 | 10 AM marker to 0.5 opacity; source swaps to ASOS |
| 30.64 | "8 .15" @30.64 | M3 tick draws down 0.3 s, label in |
| 33.10 | "7," @33.10 | commute tick + "LEFT AT 7:00" in |
| 34.22 | "landed" @34.22 | ban card pulse `scale 1 -> 1.04 -> 1` |
| 35.48 | "still on the road" @35.48 | travel bar draws 650 -> 1400, 0.8 s, power2.out |
| whole window | | lane float `y: 0 -> -3` finite yoyo; nothing holds still 4 s |
| 36.40 to 37.00 | after "road." @35.96 | exit fade-through: all but ground `to(autoAlpha 0, 0.6, power2.in)` |
Comp duration 37.00 s.

## 6. CONTRACT
One file `compositions/g-a2-9-ban-bracket.html`, root `<div id="g-a2-9-ban-bracket-root" data-composition-id="g-a2-9-ban-bracket" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-9-ban-bracket"]`. Ids/classes `bb-`. Bracket and span endpoints computed from x(t). Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-9-ban-bracket`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-9-ban-bracket`; `node scripts/overlap_check.mjs episodes/ep-buffalo-2022`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: print the bracket and span px from x(t) in the receipt.

## 8. RECEIPT
As the template.
