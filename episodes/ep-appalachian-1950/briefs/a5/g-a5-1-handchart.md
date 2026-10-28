# g-a5-1-handchart: forecast by hand on the 24 Nov 1950 chart (A5-S1)
Builder: Opus 5.5, high effort. Depth: deep (a drawn line on a real chart is a claim about the chart). Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: popfig half of `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (copy values, not class names); stroke draw as in catalog `svg-line-draw-loader` (strokeDashoffset, dash length `ceil(len)+1` computed in script). Prefix every id/class `a51-`.
Sits over: nothing. Full-frame comp on track 2 straight out of the A4/A5 chapter blackout. Its ground is the chart image.
Asset: `media/candidates/a5/A5-S1_c1_jkl-surface-1950-11-24.JPG` (1179 x 760, PD, NWS Jackson KY, `provenance.csv` verified Y, date matches). The orchestrator copies it to `media/a5/jkl-surface-1950-11-24.jpg` before dispatch; mount that path only.

## 0. Claim
In 1950 a forecast was made by hand: forecasters plotted station reports and drew the pressure lines themselves. The picture is that act, done on the real chart of the storm's eve.

## 1. Source
- Chart: `research/maps-forecast.md` §1 item 1, https://www.weather.gov/images/jkl/PastEvents/19501124Surface.JPG ("Surface Chart 1:30 am November 24 1950", provenance row).
- Hand practice: `factcheck/a5-r2.md` rows 1-4 (AMS "manually derived forecasts"; NOAA "forecasts being produced manually"). "Station reports plotted onto a map by hand", "drew the fronts and the pressure lines themselves": rows 2, 3.

## 2. Datum, scale, orientation
- Image cover-fit: scale k = 1920 / 1179 = 1.6285 → 1920 x 1238 px; centred, so screen = (src_x × 1.6285, src_y × 1.6285 - 79). North up. Every traced point is given in source px and converted with this formula by script.
- Slow push 1.00 to 1.06 over the whole comp, origin at screen (960, 540) (linear is fine under 1.5x). The pencil, trace and dots live INSIDE the pushed group so they stay on the chart's lines.

## 3. Geometry (px)
- Ground: chart image, `filter: sepia(0.28) contrast(1.08) brightness(0.96) saturate(0.8)` (`.archgrade`), plus a dim layer `rgba(3,5,8,X)`: X = 0.82 at frame 0 (near black), to 0.30 by 3.2 s ("chart comes up"). Frame 0 shows the chart at 0.82 dim, not black (ground on from frame 0).
- Isobar trace: pick ONE isobar the chart itself draws, the 1020 line labelled "1020" near source (1125, 212) on the right edge, which runs down the Atlantic side and curves back west of the "HIGH" over the Carolinas coast. Read the image, list at least 12 points along that drawn line in source px (put the list in a comment), convert by formula. Stroke `#2a2622` (pencil graphite) 3.5 px, round caps, opacity 0.9, drawn over the printed line (±6 px of it at every point). Draw only the on-screen part, top to bottom.
- Pencil: self-made SVG, about 300 px long, yellow-ochre body `#c8b98a`, graphite tip `#2a2622`, tilted 35°, its tip glued to the stroke head (assert the tip sits on the path head at three times). A simple flat hand silhouette `#4a5560` at 0.85 opacity holding the pencil top is optional; no face, no skin detail.
- Station dots: 10 dots, 9 px, `#d0121f` at 0.9, each placed on an existing station circle printed on the chart (read positions from the image near the traced line and the eastern seaboard, e.g. the Washington, Philadelphia and Pittsburgh plots; list source px in a comment). Each pops in (scale 0 to 1.25 to 1, 0.25 s) and keeps a 2 px ring.
- Popfig: big "1950" AbrilFig 150 px `#d0121f`, `.pf-big` text-shadow, centred x 960, block top y 360; sub "FORECAST BY HAND" Arial 700 32 px `#e8e3d8` `.pf-sub` shadow, 12 px under.
- Source line (bottom-left, left 110, bottom 60): "Chart: NWS Jackson, KY · Nov 24, 1950" Arial 700 20 px `#c8d3e0`, glass pill (tokens.md glass surface, radius 14, padding 6 x 14).
- Three tiers: 150 (display), 32 (mid), 20 (small).

## 4. Must be true in the picture
1. The drawn line lies on a line the chart itself prints (the 1020 isobar), within ±6 px at every listed point, through the whole push. A free-hand squiggle not on a printed isobar = FIX.
2. Every red dot sits on a printed station circle (±5 px). No dot on open ocean or on a text label.
3. The popfig is fully gone before the chart reaches 0.5 dim or lower: it never sits over a readable chart (popfig never over a map).
4. No date or place text other than "1950", "FORECAST BY HAND" and the source line. No "LOW"/"HIGH" labels added (the chart's own printed ones stay as printed).
5. Nothing in the corner x >= 1600, y >= 680 except chart texture (no dots, pencil or trace end there; if the 1020 line runs there, stop the trace above y 680).

## 5. Panel text (exact) and cues
Text: `1950` · `FORECAST BY HAND` · `Chart: NWS Jackson, KY · Nov 24, 1950`
Cues from `audio/a5-s1.words.json` (seconds from segment start):
- 0.00: comp on, chart at 0.82 dim, push starts.
- 0.18 "1950,": big line in (`fromTo` autoAlpha 0 to 1, scale 1.25 to 1, 0.45 s, back.out(1.6)). `/* 1950 @0.18 */`
- 1.48 "forecast": sub in (`fromTo` autoAlpha 0, y 18 to 0, 0.4 s, power3.out). `/* FORECAST @1.48 */`
- 0.63 to 2.62: popfig floats y 0 to -8, sine.inOut.
- 2.62 "pencil.": popfig exits (`to` autoAlpha 0, y -40, scale 0.96, 0.5 s, power3.in); dim 0.82 to 0.30 over 2.62-3.20; pencil slides in from the right edge (x +400 to 0, 0.5 s, power3.out) to the trace start. `/* PENCIL @2.62 */`
- 3.00: source line in (`fromTo` autoAlpha 0, x -20 to 0, 0.4 s).
- 5.24 "station": station dots pop one by one, 0.28 s apart (5.24 to 7.76), ending near "hand." 7.42. `/* STATION @5.24 */`
- 9.34 "pressure": trace starts drawing; pencil tip rides the head; draw runs 9.34 to 12.50 (power1.inOut). `/* PRESSURE @9.34 */`
- 12.14 "low" to 13.16 "experience.": pencil lifts (y -30, rotation +8, 0.5 s) and drifts off right (x +500, 0.6 s, power3.in) by 13.40. `/* EXPERIENCE @13.16 */`
- 13.40 to end: dim to 0.70 over the last 0.5 s, so the cut into g-a5-2 (same image, heavy dim) is continuous.
Host: data-start = A5-S1 audio start, duration 14.00 s (13.62 + tail). Root `id="g-a5-1-handchart-root"`.

## 6-8
Contract, tools, done line and receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 6: compute the source-to-screen conversion of every traced point and dot by script and print it in the receipt. Done line 7: the chart is a dated place picture; its `provenance.csv` row is the A5-S1_c1 row above.
Must not: CSS @keyframes, `id="root"`, a glass card behind the popfig, a scale bar, any added pressure number.
