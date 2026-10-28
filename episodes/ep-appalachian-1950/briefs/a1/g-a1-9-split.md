# g-a1-9-split: Newark's wind and Columbus's snow, same Saturday (A1-S12)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, pin style). The right half must match `briefs/a2/g-a2-1-columbus.md` §3 "Frame 0" (same map frame, pin, label, snow recipe). Prefix every id and class `sp9-`.
Sits over: nothing. Full-frame designed split map on track 2. The chapter blackout follows this comp, then g-a2-1 opens on the Columbus half.

## 0. Claim
On the same Saturday (25 Nov 1950) the wind was tearing at Newark (108 mph gust) while at noon Columbus, Ohio sat at 10°F with snow falling: one storm's two sides. Opens loop A1 into Act 2. Nothing joins the halves (L1 stays closed).

## 1. Source
`research/nws-facts.md` §1 JKL/PHI (P): Newark 108 mph gust (25 Nov entry); §3 ILN (P): Columbus 25 Nov noon 10°F, "Snow & Blowing Snow"; §4 row 113 (both hazards same time, dated entries); `factcheck/a1-r4.md` row 2. Source line "Source: NWS Mount Holly; NWS Wilmington OH".

## 2. Datum, scale, orientation
- Left half (x 0 to 958): frame A1-W, s 0.10, frame top-left (85093.2, 27271.1); Newark at (480, 560). Clip-path inset 0 962px 0 0.
- Right half (x 962 to 1920): frame A2-C shifted +480 px, s 0.10, frame top-left (44191.0, 31596.7); Columbus at (1180, 560). Clip-path inset 0 0 0 962px. This is g-a2-1's frame 0; keep it identical.
- Seam: 2 px `rgba(255,255,255,.14)` at x 960. North up on both.

## 3. Geometry (px, 1920 x 1080)
- Both halves: land `#0b1016`, water `#04070a`, outlines 1.5 px `rgba(255,255,255,.14)`.
- Left: Newark pin 16 px dot `#7fb2e5`, pulse ring every 1.5 s; label "NEWARK, NJ" Arial 700 26 px `#f2f5f8` tracking 3, 22 px right of the pin. Wind layer: 30 streaks (2 px, 60 to 160 px, `#7fb2e5` at .5) moving x +500 px/s across the left half only (clipped), finite repeats, seeded. Chip glass card left 300, top 610: "108 MPH" Arial Black 900 58 px `#f2f5f8` + "GUST" Arial 700 22 px `#93a3b2` tracking 6.
- Right: Columbus pin 18 px dot `#f2f5f8`, 2 px ring `#7fb2e5`, pulse ring scale 1 to 2.4, autoAlpha .6 to 0, every 1.5 s; label "COLUMBUS, OHIO" Arial 700 26 px `#f2f5f8` tracking 4, 22 px right of the pin. Snow: 70 flakes (2 to 5 px white circles, opacity .35 to .8) falling 60 to 120 px/s with x drift +40 to +90 px/s, clipped to the right half, seeded positions (g-a2-1's recipe).
- Clock chip (right half, glass card left 1010, top 90, padding 18 x 28): "NOON" Arial Black 900 58 px `#f2f5f8`; "SAT, NOV 25" Arial 700 22 px `#93a3b2` tracking 6.
- Chips right half: "10°F" glass card left 1220, top 600 (Arial Black 900 58 px `#f2f5f8`); "SNOWING" glass card left 1220, top 700 (Arial Black 900 52 px `#f2f5f8`; right edge must stay left of x 1600, so about x 1520).
- Source line left 110, bottom 90; "Basemap: Natural Earth" bottom 60.
- Tiers: 58 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Nothing crosses the seam: no line, arrow, band, streak or flake joins the halves; streaks stay left, flakes stay right.
2. Columbus pin at (1180, 560) ±4 px and label as g-a2-1 frame 0 (the handoff).
3. "108 MPH" only on the left, "10°F" and "SNOWING" only on the right.
4. Nothing in x >= 1600, y >= 680 (SNOWING card ends about x 1520).

## 5. Panel text (exact) and cues (`audio/a1-s12.words.json`, seconds from A1-S12 start)
Text: `NEWARK, NJ` · `108 MPH` · `GUST` · `COLUMBUS, OHIO` · `NOON` · `SAT, NOV 25` · `10°F` · `SNOWING` · `Source: NWS Mount Holly; NWS Wilmington OH` · `Basemap: Natural Earth`
- 0.00: left half on (map, Newark pin, label, streaks); right half dark `#04070c`; seam on. `/* THAT @0.00 */`
- 1.44 "tearing": streak set 2 fades in (density doubles). `/* TEARING @1.44 */`
- 1.94 "Newark,": "108 MPH" chip in (`fromTo` y 20 to 0, autoAlpha, 0.4 s, power3.out). `/* NEWARK @1.94 */`
- 2.84 "noon": right half opens from the seam (clip-path inset 0 0 0 1920px to 962px, 0.8 s, power3.inOut) with map, snow; clock chip in. `/* NOON @2.84 */`
- 3.30 "Columbus,": Columbus pin + label in. `/* COLUMBUS @3.30 */`
- 4.80 "10": "10°F" chip in. `/* 10 @4.80 */`
- 6.14 "snow": "SNOWING" chip in; second flake set fades in. `/* SNOW @6.14 */`
- 9.20 "other side.": both pins pulse once together (no link drawn). `/* OTHER @9.20 */`
- 10.28 "So how": left streaks fade to 20 % over 2.0 s and the "108 MPH" chip dims to .5 (wind fades to near silence); snow keeps falling to the last frame. `/* SO @10.28 */`
- 11.88 "both": chips hold; riser ends on the line's end (editor).
- Exit: the comp ends on a cut to the chapter blackout (a full-frame scene may end on a cut); left half chip slides out in the last 0.6 s (x -60, autoAlpha 0, power3.in).
Host: data-start = A1-S12 start, duration = 12.989 + 0.40 = 13.39 s.

## Open item
g-a2-1's frame 0 puts its clock chip at left 110, top 90 (left half). Here the left half is Newark, so the Columbus clock chip sits at left 1010, top 90. With the blackout between, either g-a2-1 moves its chip (x +900 at frame 0, slides to 110 with the opening) or the jump is accepted. Orchestrator decides.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
