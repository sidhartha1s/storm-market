# g-a3-9-exit: one track through the split map, off into Canada (A3-S7, 15.20 to end)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (frame A2-X), `briefs/intro/g-intro-2-hookmap.md` §3 (pin styles), then this brief.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, projection); pins and labels as `g-intro-2-hookmap`. Prefix every id and class `a3x-`.
Sits over: nothing. Full-frame designed map, fades in over g-a3-8's last 0.6 s (host starts at A3-S7 + 14.60).

## 0. Claim
The storm finally weakened and slid off into Canada on 29 and 30 Nov; one track joins the wind side (Newark), the snow side (Pittsburgh) and warm Buffalo.

## 1. Source
- `research/nws-facts.md` §4 JKL "finally weakened and exited into Canada on the 29th and 30th".
- Pins: as g-a3-3 / the hook (sources there). The exit direction into Canada is SCHEMATIC (JKL gives no heading); drawn due north-north-east from Lake Erie into Ontario.

## 2. Datum, scale, orientation
Frame A2-X: s 0.03, top-left (42191.8, 15852.5). Newark (1431, 511), Pittsburgh (760, 560), Buffalo (889, 150), Lake Erie centre (621, 265), Ohio 40.2N 82.8W (437, 600). Track (the act's shape, the Carolinas start is below the frame): north from (900, 1100) to (900, 640), left through (700, 520) to Lake Erie centre (621, 265) with a small 1-turn loop there (radius 30), then the exit as a dotted line from the loop north-north-east to the top edge at about (760, 54) and beyond (off-frame, toward 45.5N 78.5W). The track passes between Pittsburgh and the coast, not through any pin; thin connectors join it to each pin as in g-a3-3.

## 3. Geometry (px)
- Basemap styled as g-a3-4; credit "Basemap: Natural Earth" left 110, bottom 60.
- Pins (core 18 / ring 34 / 3 px): Newark wind blue `#7fb2e5` with a pulse ring every 1.4 s; Pittsburgh snow white `#f2f5f8` with a soft glow; Buffalo orange `#d8a13a`. Labels Arial 700 26 px `#dfe7ee`, stroke `#04070c` 5 px: "NEWARK" left of its pin, "PITTSBURGH" right of its pin, "BUFFALO" right of its pin. All on from comp 0.60 (when the map has faded in).
- Red track `#d0121f` 6 px with glow; connectors 4 px `#d0121f` .6 dash 8 6 to each pin. Exit line: same red, dotted (dash 2 12, round caps), 6 px.
- Chip (glass chip, radius 14, padding 10 x 18): "EXITS · NOV 29–30" Arial Black 900 40 px `#f2f5f8`, box left 820, top 70 (right of the dotted line's top; right edge <= 1300).
- Source line "Source: NWS Jackson, KY; NWS Charleston, WV · track schematic" left 110, bottom 90.
- Tiers: 40 / 26 / 19 (flat-type: 3 tiers met).

## 4. Must be true in the picture
1. Buffalo north of Pittsburgh, Newark on the coast east: positions from the formula ±10 px.
2. The track is continuous from the south edge to the Lake Erie loop; the exit leaves the loop northward into Canada and off the frame, dotted.
3. Pin colours: Newark blue, Pittsburgh white, Buffalo orange, all three at once by "slid" (16.40).
4. "NOV 29–30" lands on "29th" (17.82), never before; no other number.
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a3-s7.words.json`; segment time, then comp time = segment time - 14.60)
Text: `NEWARK` · `PITTSBURGH` · `BUFFALO` · `EXITS · NOV 29–30` · `Source: NWS Jackson, KY; NWS Charleston, WV · track schematic` · `Basemap: Natural Earth`
- seg 14.60 / comp 0.00: map fades in (0.6 s); pins and labels already placed, red track already drawn to the Lake Erie loop with connectors. `/* FADE @14.60 */`
- seg 15.46 "finally" / comp 0.86: loop arrowhead circles once slowly. `/* FINALLY @15.46 */`
- seg 15.76 "weakened" / comp 1.16: track and loop glow dims from 1 to .6 (weakening, 0.8 s). `/* WEAKENED @15.76 */`
- seg 16.40 "slid" / comp 1.80: dotted exit line draws north from the loop to the top edge (1.2 s, power2.in), its dots then keep marching (dashoffset, finite repeats). `/* SLID @16.40 */`
- seg 17.08 "Canada" / comp 2.48: the dotted line's head passes the top edge. `/* CANADA @17.08 */`
- seg 17.82 "29th" / comp 3.22: chip "EXITS · NOV 29–30" in (y 16 to 0, autoAlpha, 0.4 s, power3.out). `/* 29TH @17.82 */`
- Hold to host end with the dots marching, Newark pulsing (sound bed thins here). The next segment (A3-S8, g-a3-10) opens on this frame.
- Exit: last 0.5 s: chip `to` y -16, autoAlpha 0 (0.5 s, power3.in); map stays (g-a3-10 continues on it).
Host: data-start = A3-S7 start + 14.60, duration = (18.90 - 14.60) + 0.40 = 4.70 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 6: compute pins and track points from the formula by script.
