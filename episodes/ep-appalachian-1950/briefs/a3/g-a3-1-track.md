# g-a3-1-track: the low went northwest (A3-S1)
Builder: Opus 5.5, high effort. Depth: deep (the act's visual event; closes cta-hinge and L1). Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief and `briefs/a3/_list.md` (chart camera C1 table).
Start from: `library/official` `svg-stroke-trace` (path draws from its measured length) and `references/editing-patterns/ep3-map-route-fit.html` (route over a map image). Prefix every id and class `a3t-`.
Sits over: nothing underneath; the chart still `media/a3/A3-S1_c1_nws-jkl-surface-1950-11-25.jpg` is mounted inside the comp as its ground, on from frame 0 (hard cut "straight out of the CTA").

## 0. Claim
The low formed over the Carolinas and, instead of riding the coast out to sea as such storms usually do, turned inland and was over Ohio by midday Sunday.

## 1. Source
- `research/nws-facts.md` §4 JKL "Low pressure quickly developed on the arctic front over the Carolinas on the 25th"; "The low tracked northwestward into Ohio by midday on the 26th" (https://www.weather.gov/jkl/appalachianstorm1950).
- Usual path: NWS Greenville-Spartanburg, nor'easters "develop over the ocean and track northeast along the coast" (factcheck a3-r1 row 3).
- Chart: NWS Jackson KY surface chart 25 Nov 1950 (`maps-forecast.md` §1 item 1; provenance row "weak low about 999 mb on the Virginia/Carolinas coast"). The red track is SCHEMATIC, not traced: no low position was read off any chart (`maps-forecast.md` "Could not confirm").
- Formation date disputed (JKL 25th vs others 24th, factcheck a3-r1 rows 2, 5): the pin reads "NOV 24–25" exactly as the Picture line writes it.

## 2. Datum, scale, orientation
Chart camera C1 (`_list.md`): screen = (chart px - (196, 110)) × 2.0, image top-left at (-392, -220), north up as printed. Points: Carolinas pin (1238, 660), turn near Washington (1298, 420), Pittsburgh (1078, 364), Columbus / Ohio end (910, 402), usual-path end (1768, 160). The builder zooms the JPEG, finds the printed station plots (Columbus label near chart (620, 300)) and corrects each point; report the measured values in the receipt (g-a3-2, -3 and -7 reuse them).

## 3. Geometry (px, 1920 x 1080)
- Chart image 2312 x 1518 at (-392, -220), static (no camera drift: text sits beside chart points and must not ride a move). Dim layer full frame `rgba(4,7,12,.38)`. Ambient motion for the whole window: the master-map scan line (2 px, 1180 px wide, `rgba(127,178,229,.30)`, centred x 960) sweeping top to bottom at 60 px/s, finite repeats covering the host, so no 4 s gap ever idles (0.66 to 3.50 has no other mover).
- Red track (one SVG path on the overlay layer in screen px, above the dim): cubic path from Carolinas (1238, 660) north to (1300, 430), bending left through (1180, 360) to end at Ohio (910, 400). 6 px `#d0121f`, round caps, glow `drop-shadow(0 0 6px rgba(208,18,31,.6))`. Dash length = ceil(getTotalLength())+1. Arrowhead 22 px triangle at the head, rides the path head (GSAP only, asserted at 3 times).
- Carolinas pin: core 18 px `#f2f5f8`, ring 34 px 3 px `#d0121f`, pulse every 1.4 s (finite repeats). Label glass chip (glass surface, radius 14, padding 10 x 18) left of the pin, right edge 24 px left of the dot: "CAROLINAS · NOV 24–25" Arial 700 26 px `#f2f5f8` tracking 3.
- Ghost arrow: path from the Carolinas pin (1238, 660) north-east up the coast through (1420, 430) to (1768, 160), 5 px `#93a3b2` opacity .55, dash 14 10, arrowhead at the end. Chip "THE USUAL PATH" Arial 700 26 px `#93a3b2` tracking 3, glass chip, anchored left of the path end, box right edge <= 1740, top y about 190.
- Headline chip (title zone, top-left): glass card left 110, top 90, padding 18 x 28, radius 28: "THE LOW WENT NORTHWEST" Arial Black 900 52 px `#f2f5f8`.
- "OHIO" end label: Arial 700 26 px `#f2f5f8` tracking 4, paint-order stroke `#04070c` 5 px, 24 px left of the track end (right edge at x 886), vertical centre y 400.
- Source line "Source: NWS Jackson, KY · track schematic" left 110, bottom 60.
- Tiers: 52 / 26 / 19.

## 4. Must be true in the picture
1. The red track starts at the Carolinas pin, heads north first, then bends LEFT (west) and ends over Ohio, west of Pittsburgh's station. It never touches the ocean east of the coastline after the bend.
2. The ghost path runs north-east, stays over or beside the coast and ends over open ocean (right of the printed coastline); it is visibly a different colour and dash from the red track.
3. Both paths begin at the same pin.
4. The headline lands on "low" @0.16, before any line moves; the red line is not complete before "Ohio." @15.38.
5. No number on screen except "24–25" in the pin chip; no wind arrows, no "H", no other city named (later segments own them).
6. Nothing of this comp in x >= 1600, y >= 680; all text inside 96/54 px margins.

## 5. Panel text (exact) and cues (`audio/a3-s1.words.json`, seconds from A3-S1 start)
Text: `THE LOW WENT NORTHWEST` · `CAROLINAS · NOV 24–25` · `THE USUAL PATH` · `OHIO` · `Source: NWS Jackson, KY · track schematic`
- 0.00 frame 0: chart dimmed, drift running, source line on. `/* THE @0.00 */`
- 0.16 "low": headline chip in (`fromTo` y 24 to 0, autoAlpha 0 to 1, 0.45 s, power3.out). `/* LOW @0.16 */`
- 0.66 "northwest.": red stub draws from the pin 0 to 12 % of its length (0.4 s) as a tease, the sound hit lands here. `/* NORTHWEST @0.66 */`
- 3.50 "center": Carolinas pin in (scale 0.4 to 1, back.out(1.6), 0.4 s). `/* CENTER @3.50 */`
- 6.32 "Carolinas.": pin chip "CAROLINAS · NOV 24–25" in (x -16 to 0). `/* CAROLINAS @6.32 */`
- 8.38 "rides": ghost path draws from the pin up the coast (2.4 s, power1.inOut). `/* RIDES @8.38 */`
- 10.42 "out": ghost reaches the sea end; chip "THE USUAL PATH" in. Headline dims to .35. `/* OUT @10.42 */`
- 11.88 "turned": ghost path and its chip dim to .3 (keep, g-a3-4 calls it back); red track draws from 12 % to 100 %: north leg then the left bend, 3.2 s, power2.inOut, arriving at 15.10. `/* TURNED @11.88 */`
- 15.38 "Ohio.": "OHIO" label in; pin at the track end flashes (ring 34 to 70 px, .5 s). Headline back to 1. `/* OHIO @15.38 */`
- Exit: none. The last frame (track complete, ghost dim, headline and chips at their states) continues in g-a3-2; at host end minus 0.5 s the headline and the pin chip slide out (`to` x -60, autoAlpha 0, 0.5 s, power3.in) so g-a3-2 opens on chart + track + ghost + "OHIO" only.
Host: data-start = A3-S1 start, duration = 15.74 + 0.40 = 16.14 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Receipt also lists the measured chart points (§2).
