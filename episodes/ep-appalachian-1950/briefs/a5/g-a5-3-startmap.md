# g-a5-3-startmap: the starting point looks small (A5-S3)
Builder: Opus 5.5, high effort. Depth: deep (a continental map whose shapes are claims). Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: `library/inhouse/master-map-us-canada.html`. Copy to `compositions/g-a5-3-startmap.html`; keep the basemap paths, projection and camera rig (single camera group, svgOrigin based). Delete the Enderlin swath/track, survey points, RHS rail cards and every Enderlin label. Prefix every id/class `a53-`.
Sits over: nothing. Full-frame designed map on track 2, ground on from frame 0.

## 0. Claim
When researchers later rebuilt the opening conditions, the storm-to-be was only a weak ripple of low pressure over Minnesota, sitting on the leading edge of arctic air over southwestern Canada. Nothing yet over the Carolinas, where the damaging low would form later.

## 1. Source (quoted, with rows)
- AMS abstract (Kistler, Uccellini, Kocin 2004), https://ams.confex.com/ams/84Annual/techprogram/paper_73168.htm: "The initial conditions depict a weak cyclonic wave over Minnesota, along the leading edge of a very cold air mass over southwestern Canada." `factcheck/a5-r2.md` rows 12-14, 17: the start state belongs to a modern reanalysis re-forecast, UNDATED. So the map carries no date of any kind.
- Low forms later on the arctic front over the Carolinas, then turns northwest: NWS JKL, rows 15, 16 (spoken only; not drawn here: Act 3 owns the track).
- Basemap: Natural Earth 50m admin-1 (public domain) inside the exemplar.

## 2. Datum, scale, orientation
- North up, no rotation. Projection: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213).
- Frame N (open): s 0.00645, top-left (-143524.0, -68772.7). Frame N2 (end): s 0.008385, top-left (-66952.8, -27407.5) (a 1.3x push, linear power2.inOut is fine under 1.5x).
- Points (lat, lon → map units → screen in N; N2):
  - Minnesota ripple centre (46.3, -94.2) → (12967.2, 1794.5) → N (1009, 455); N2 (670, 245)
  - Arctic mass core, SW Canada (52.0, -115.0) → (-66925.6, -30040.0) → N (494, 250); N2 (0, -22), off frame
  - Carolinas (35.3, -79.3) → (70198.1, 63229.5) → N (1379, 851); N2 (1150, 760)
  - Pittsburgh (40.4406, -79.9959) → N (1361, 666) (reference only, no pin)
  All computed by python3 from the formula (28 Oct 26). Recompute in the build and print them.
- The air mass outline and swirl size have no confirmed numbers: SCHEMATIC, NOT TO SCALE (said in the source line).

## 3. Geometry (px, frame N unless stated)
- Basemap as the exemplar: state fills `#0b1016` to `#15202b`, state/province lines `#2a3644` 1.2 px non-scaling, coastline `#4a5560` 1.6 px, background radial gradient. "Basemap: Natural Earth" folds into the source line.
- Arctic mass: one soft-edged shape, fill `#5a768f` at 0.55 with a 40 px feathered edge (SVG gaussian blur 18) and a brighter core `#7fb2e5` at 0.35 around the core point. Outline polygon through these screen points (N): (300,130) (560,110) (760,190) (930,330) (995,435) (900,430) (700,380) (470,360) (330,300) (260,210), smoothed (Catmull-Rom). Its south-east tip is the LEADING EDGE and ends on the ripple's north-west side (995, 435).
- Ripple: a faint counterclockwise swirl, 2 open arcs, radius 22 and 34 px, stroke `#dfe7ee` 2.5 px at 0.65, centre (1009, 455). It rotates counterclockwise slowly (−30°/s) the whole comp (finite repeats).
- Chips (glass surface, radius 14, padding 10 x 18, Arial Black 900 40 px `#f2f5f8`):
  - "WEAK RIPPLE": left edge 40 px right of the ripple, vertically centred on it: box about x 1070 to 1400, y 425 to 485.
  - "ARCTIC AIR": text `#7fb2e5`, box centred under the mass core: about x 330 to 620, y 300 to 360 (inside the mass, high contrast on glass).
- Eyebrow, top-left zone (left 110, top 80): "REBUILT STARTING CONDITIONS" Arial 700 22 px `#93a3b2` tracking 6. No date beside it.
- Source line (bottom-left, left 110, bottom 60), Arial 700 20 px `#c8d3e0`, glass pill: "Kistler et al., AMS 2004 · Schematic · Basemap: Natural Earth".
- Scan line: the exemplar's `.mm4`-style scan (2 px, 1180 px wide) top to bottom at about 60 px/s, opacity 0.30, whole comp.
- Tiers: 40 (mid), 22/20 (small) and none big → declare `data-type-ok="map labels: two tiers by design"` on the root, or make "WEAK RIPPLE" 52 px if it fits (box then about x 1070 to 1470); prefer 52 px.

## 4. Must be true in the picture
1. The ripple sits over Minnesota (state outline around it) within ±10 px of the computed point; the mass core sits over Alberta/BC, north-west of the ripple.
2. The mass's south-east tip touches the ripple (gap 0 to 15 px): the ripple is ON the leading edge, not floating in clear air and not buried inside the mass.
3. No date, day, time or year anywhere on the map. No "L", no front line, no track, no isobar, no pressure number.
4. Nothing over the Carolinas in any frame: no pin, ring, glow, label or arrow there, through the push to N2.
5. One reading target at a time: "ARCTIC AIR" lands only after "WEAK RIPPLE" has dimmed to 0.35.
6. Corner x >= 1600, y >= 680 empty in both frames (only basemap and ocean).
7. No text rides the push: both chips are faded to 0 before the push starts.

## 5. Panel text (exact) and cues
Text: `REBUILT STARTING CONDITIONS` · `WEAK RIPPLE` · `ARCTIC AIR` · `Kistler et al., AMS 2004 · Schematic · Basemap: Natural Earth`
Cues from `audio/a5-s3.words.json` (note: the TTS word list starts at "the starting point"; the edit_script line begins "And", which Whisper dropped or the voice omitted, either way the times hold):
- 0.00: frame N on, basemap and scan line on, source line on, ripple and mass hidden. Slow drift 1.00 to 1.02 (0 to 11.4).
- 2.98 "rebuilt": eyebrow in (`fromTo` autoAlpha 0, x -20 to 0, 0.4 s, power3.out). `/* REBUILT @2.98 */`
- 5.70 "weak": ripple fades up (autoAlpha 0 to 0.65, scale 0.6 to 1, 0.6 s, power2.out). `/* WEAK @5.70 */`
- 5.92 "ripple": chip "WEAK RIPPLE" in (`fromTo` autoAlpha 0, x -16 to 0, 0.35 s, back.out(1.4)). `/* RIPPLE @5.92 */`
- 7.32 "Minnesota.": ripple one pulse (ring 34 to 60 px, opacity 0.6 to 0, 0.8 s). `/* MINNESOTA @7.32 */`
- 8.44 "Arctic": "WEAK RIPPLE" dims to 0.35; mass grows in from its core (scale 0.4 to 1 about the core point via svgOrigin, autoAlpha 0 to 1, 1.0 s, power2.out), its tip reaching the ripple at 9.44. `/* ARCTIC @8.44 */`
- 9.96 "southwestern": chip "ARCTIC AIR" in. `/* SOUTHWESTERN @9.96 */`
- 11.46 "The": both chips and the eyebrow fade to 0 (0.3 s). `/* THE LOW @11.46 */`
- 11.80 to 13.30: push N to N2 (power2.inOut). `/* LATER @12.72 */`
- 13.30 to 16.72: slow drift on N2 (scale +2 %, ease none), mass edge breathing (opacity 0.55 to 0.45, sine) so something moves; Carolinas stay empty. `/* CAROLINAS @14.34 */` `/* NORTHWEST @16.38 */`
- End: hold to 17.40 (land time), cut to g-a5-4.
Host: data-start = A5-S3 audio start, duration 17.40 s. Root `id="g-a5-3-startmap-root"`.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 6: compute every point from the formula and frame table by script and print them. Report any §4 vs §3 conflict instead of choosing.
