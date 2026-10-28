# g-a6-4-grade · A6-S3 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: official `stagger-lattice` (grid of cells filling in turn), `library/inhouse/then-now-scale.html` (one measured axis), house glyphs from `episodes/ep-galveston-1900/compositions/g-intro-6-island.html`.
This comp is the BASE of g-a6-7-flood (plan panel, colours, grid): send it alone for a full-size frame read before g-a6-7 copies it.

## 0. Claim
From 1903 to 1911 the city was raised: dredged sand from the harbor entrance was pumped in one diked section at a time; about 2,000 buildings were first jacked up by hand so the sand could go under them; the ground rose by up to 11 ft; one 3,000-ton church went up with its services kept on schedule.

## 1. Source
- ASCE (sources-a6.md §3): "from 1903-1911"; "quarter-mile-square sections" each enclosed by a dike; "Around 2,000 buildings were raised on hand-turned jackscrews"; sand through a canal by "four self-loading hopper dredges"; fill "from a few inches to eleven feet thick"; "The sand fill was dredged from the entrance to Galveston Harbor".
- TSHA (sources-a6.md §3): "2,146 buildings"; "a 3,000-ton church"; "church services were held on schedule".
- NOAA 200th: "heights varying from one to up to 11 feet" (factcheck a6-r1 rows 13, 17). TSHA/AOML "seventeen feet" is outvoted: never on screen.
- No row gives the section layout, their count, or the filling order: the plan is SCHEMATIC and says so.

## 2. Datum, scale, orientation
Two panels side by side.
- Plan panel (left), north up: x 96 to 1056, y 150 to 930. Island strip drawn as a band running WSW to ENE (Gulf along its south edge, bay along its north), city at the east end, harbor entrance off the east tip (right). SCHEMATIC, NOT TO SCALE: label "Schematic plan" Arial 700 20 px `#93a3b2` at left 120, top 940.
- Mechanism panel (right), a cross-section: x 1150 to 1824, datum (old ground) y 820, 20 px per ft vertical. 11 ft = 220 px (new ground y 600). Horizontal not to scale.

## 3. Geometry (px)
Plan panel:
- Bay fill top `#0b1016`, Gulf fill bottom `#0b1016`, island band `#15202b` with edge `#93a3b2` 2 px.
- The city grid: 6 columns x 3 rows of squares, 120 px each, 6 px gaps, top-left at (240, 380); each square has a 3 px `#5a768f` outline (the dike). Squares are "unfilled" `#15202b` and fill to sand `#c9a46b` in turn.
- Seawall: a 6 px `#c8d3e0` line along the grid's south edge (y 770), from x 230 to 1010, unlabelled (S2 named it).
- Harbor entrance: at (1010, 330) a small label "Harbor entrance" diagram tier Arial 700 22 px `#93a3b2`, right-aligned to x 1040, top 290. Sand pipe: a 6 px `#c9a46b` line from (1010, 340) into the grid's NE square, with 10 px sand dots flowing along it (dash offset tween, continuous).
- Fill order: by columns east to west, top to bottom within a column (18 squares). Each square fills 0.35 s, stepped so all 18 finish by 8.20 (computed by script, listed in the receipt).

Mechanism panel:
- Old ground line y 820 x 1150 to 1824, `#93a3b2` 3 px, label "1900 ground" diagram tier at (1170, 836).
- House glyph (scaled-up g-intro-6 house: 220 x 180 px, `#4a5560`, roof `#93a3b2`), centred x 1480, sitting on y 820.
- Jackscrews: 4 vertical posts (8 x 60 px, `#d8a13a`) under the house at x 1400, 1450, 1510, 1560.
- Lift: the house and screws move up together to stand on y 600 (house bottom at y 600; screws stretch by scaleY from their base, `transformOrigin` bottom).
- Sand fill: a `#c9a46b` block from y 820 up to y 600 slides in from the left under the house after it is up (scaleY from the bottom), wrapping the screws.
- Bracket: `#f2f5f8` 3 px at x 1250 from y 820 to y 600, ticks 30 px; chip "UP TO 11 FT" glass, left edge x 1180, top 450 (above the bracket top, left of the house roof which starts about x 1370).
- Church: at the church beat the house cross-fades to a church glyph (nave 260 x 170 px with a 110 px steeple, same colours) on the raised ground, and a second, shorter set of 4 jacks shows under it lifting it 30 px (schematic of "went up"; no height number for the church).
Chips (glass, shared spec):
- C1 "1903 TO 1911": left edge x 120, top 170 (over the bay, top of the plan panel).
- C2 "ABOUT 2,000 BUILDINGS": right panel, left edge x 1180, top 150.
- C3 "UP TO 11 FT" as above.
- C4 "ABOUT 3,000 TONS": right panel, left edge x 1180, top 150 (C2's place; C2 gone by then).
- Source line top-left above C1 would collide: source line goes to `left:96px; top:54px`, C1 moves to top 150; the plan panel starts y 230 for its bay band. Text: "American Society of Civil Engineers · Texas State Historical Association".

## 4. Must be true in the picture
1. The plan carries "Schematic plan"; no square count, block count or street name is printed.
2. Sand enters from the harbor-entrance side (east, right), never from the Gulf: TSHA's "Gulf floor" was outvoted (factcheck a6-r1 row 10).
3. Squares fill one at a time in sequence, never all at once ("one walled-off section at a time").
4. In the mechanism, the house goes up BEFORE the sand goes under it (jacked first, sand after).
5. Bracket = 220 px = 11 ft at 20 px/ft ±3 px; chip says UP TO 11 FT. No 17 anywhere.
6. "ABOUT 2,000" (not 2,146) and "ABOUT 3,000 TONS".
7. Corner x >= 1600, y >= 680 holds the raised ground and sand block (unlabelled base): the circle may stay if the frame read agrees; the house's right edge must stay left of x 1600 (house right = 1590).

## 5. Text and cues (a6-s3.words.json, 21.460 s; host 0.00 to 21.460)
Frame 0: plan panel drawn (island, grid unfilled, seawall line) and the mechanism panel with the house on old ground; source line in at 0.20.
- 0.84 ("bigger."): grid outlines pulse once (opacity 0.6 to 1 to 0.8).
- 2.10 ("1903,") /* 1903 @2.10 */: C1 in.
- 3.54 ("dredges") /* SAND @3.54 */: sand pipe draws from the entrance (3.54 to 4.40); "Harbor entrance" label at 4.78 ("harbor").
- 5.82 ("city,"): first square fills; then the stepped fill runs to 8.20; C1 out at 6.56 ("one").
- 6.56 ("one walled-off section"): the square filling at that moment flashes its dike outline `#f2f5f8` (one beat).
- 8.90 ("2" 8.90) /* 2,000 @8.90 */: C2 in.
- 10.16 ("jacked") /* JACKS @10.16 */: jacks appear 10.16; house lifts 10.54 to 11.80 (power2.inOut), screws stretching.
- 11.94 ("so") to 12.86 ("underneath."): sand block slides in under the house, 12.28 to 13.20.
- 13.64: C2 out.
- 14.56 ("rose") /* 11 FT @15.50 */: bracket draws up 14.56 to 15.40; C3 in at 15.50 ("11").
- 16.40: C3 out.
- 16.84 ("church") /* CHURCH @16.84 */: house cross-fades to the church (0.5 s).
- 17.70 ("3" 17.70) /* 3,000 @17.70 */: C4 in.
- 19.52 ("services"): church lifts 30 px on its jacks 19.52 to 21.10 (`ease:none`, slow: it "went up" while the services ran); a small window glow on the nave (`#f5d98b`, opacity 0.4 to 0.8) from 19.52.
- Host end 21.460 (+ land time to the A6-S4 cut).

## Motion for the whole window
Sand dots run along the pipe for the whole host (finite repeats). Grid fill 5.82 to 8.20; mechanism moves 10.16 to 13.20 and 19.52 to 21.10; in the gaps (0 to 2.10, 13.20 to 16.84) the plan panel pushes slowly (scale 1.00 to 1.03 linear) and the chips float.

## Exit
Cut to g-a6-5 (map): root fades to 0 over the last 0.4 s.

## Footage under it
None: full-frame designed diagram. If jackscrew, dredge or church photographs clear later, the orchestrator intercuts them between this comp's beats (not inside it).
