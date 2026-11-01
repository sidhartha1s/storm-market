# g-a2-12-cold: Saturday's highs in West Virginia, about 40° below normal (A2-S12)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/split-shared-scale.html` (several columns on one shared scale). Thermometers are self-drawn SVG. Prefix `c12-`.
Sits over: nothing. Full-frame designed card on track 2, channel radial background on from frame 0.

## 0. Claim
On Saturday 25 Nov 1950 the high was 10°F at Elkins, 12°F at Charleston and 15°F at Huntington, each nearly 40° below normal for late November.

## 1. Source
`research/nws-facts.md` §3 RLX "WV highs 25 Nov | Elkins 10F, Charleston 12F, Huntington 15F, each nearly 40F below normal" (P). `factcheck/a2-r1.md` rows 39 ("The high temperature for the day in Elkins was just 10F, Charleston 12F, and Huntington 15F"), 40 ("nearly 40 degrees below normal"). Normals are not given as numbers: the ghost bar is "actual + 40", labelled NORMAL with no figure (the voice says "close to forty").

## 2. Datum, scale, orientation
Shared scale 0°F to 60°F, 8 px per °F: 0°F at y 860, 60°F at y 380. Highs: 10°F top y 780, 12°F y 764, 15°F y 740. Ghost (actual + 40): 50°F y 460, 52°F y 444, 55°F y 420. Gridlines at 0, 20, 40, 60 (y 860, 700, 540, 380).

## 3. Geometry (px, 1920 x 1080)
- Title: eyebrow "WEST VIRGINIA · SAT, NOV 25" Arial 700 22 px `#93a3b2` tracking 6, left 110, top 70; headline "HIGH FOR THE DAY" Arial Black 900 52 px `#f2f5f8`, left 110, top 104.
- Gridlines 1 px `#2a3644` across x 300 to 1500; labels "0°F" "20°F" "40°F" "60°F" Arial 700 22 px `#93a3b2` right-aligned at x 285.
- Three thermometers, tube 56 px wide, tops at y 360, bulb r 40 under y 860 (bulb bottom 940): centres x 560 (Elkins), 900 (Charleston), 1240 (Huntington). Tube stroke 3 px `#5a768f`, fill `#0b1016`.
- Liquid: `#7fb2e5`, rect from y 860 up to the value, `scaleY` origin bottom.
- Ghost bar: same tube width, from y 860 to actual + 40 (§2), stroke 2 px dashed `rgba(242,245,248,.45)`, no fill, behind the liquid. "NORMAL" Arial 700 20 px `#c8d3e0` tracking 6 above each ghost top (centre x of its tube). A bracket on Elkins only: vertical 2 px `#d8a13a` line from y 780 to 460 at x 610 with label "ABOUT 40° COLDER" Arial 700 26 px `#d8a13a` at x 625, centre y 620 (one instance, on the first city).
- Value labels above each liquid top, right of the tube (x centre + 40): "10°F" / "12°F" / "15°F" Arial Black 900 52 px `#f2f5f8`; city names under the bulbs, y 960: "ELKINS" / "CHARLESTON" / "HUNTINGTON" Arial 700 26 px `#dfe7ee` tracking 4. (edit_script "ELKINS 10°F", "CHARLESTON 12°F", "HUNTINGTON 15°F": same, split.) Bottom of city labels about y 990, inside the 1026 limit; the Huntington tube and label end at x <= 1400, clear of the corner.
- Source line "Source: NWS Charleston WV" Arial 700 19 px `#c8d3e0`, left 110, bottom 60 (clear of the city labels, which start about x 470).
- Tiers: 52 / 26 / 22 / 20 / 19.

## 4. Must be true in the picture
1. Liquid tops at y 780 / 764 / 740 and ghost tops at y 460 / 444 / 420, ±3 px: every ghost is exactly 320 px (40°) above its liquid.
2. No normal temperature number on screen (research gives none).
3. Huntington is shown but not voiced: it lands with "Both", after Charleston (one count per sentence, per the act's note).
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a2-s12.words.json`, seconds from A2-S12 start; Whisper dropped the opening "And")
Text: `WEST VIRGINIA · SAT, NOV 25` · `HIGH FOR THE DAY` · `0°F` `20°F` `40°F` `60°F` · `ELKINS` · `10°F` · `CHARLESTON` · `12°F` · `HUNTINGTON` · `15°F` · `NORMAL` ×3 · `ABOUT 40° COLDER` · `Source: NWS Charleston WV`
- 0.00 "the": ground, gridlines, three empty tubes, city names on; frost glints drift. `/* THE @0.00 */`
- 2.66 "Saturday,": eyebrow + headline in. `/* SATURDAY @2.66 */`
- 4.02 "Elkins": ELKINS name brightens `#f2f5f8`. 5.40 "10": Elkins liquid fills to 10°F (0.6 s, power3.out), "10°F" in. `/* 10 @5.40 */`
- 6.88 "Charleston": name brightens; 7.90 "12.": liquid to 12°F, "12°F" in. `/* 12 @7.90 */`
- 8.74 "Both": Huntington liquid to 15°F + "15°F" in; all three ghost bars draw up (stroke-dashoffset, 0.7 s, stagger 0.15). `/* BOTH @8.74 */`
- 9.60 "40": "NORMAL" labels in; Elkins bracket draws (`scaleY` origin bottom, 0.5 s) and "ABOUT 40° COLDER" in. `/* 40 @9.60 */`
- 10.64 to exit: ghost bars shimmer (dash offset crawl 10 px/s), liquid tops quiver ±2 px (sine).
- Exit: last 0.6 s: the card group `to` x -980, autoAlpha 0, power3.in.
Host: data-start = A2-S12 start, duration = 11.96 + 0.40 = 12.36 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
