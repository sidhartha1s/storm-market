# g-a2-5-janowicz: Vic Janowicz's field goal, Ohio State's only points (A2-S5)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/snippets/cards.css` `.polaroid` (beige `#f4f0e6` stock, `.pol-cap` `#2a2622`) for the portrait, `.namecard` for the name line, `.glasscard` for the chip. Goalpost scene is self-drawn SVG. Prefix `j5-`.
Sits over: nothing. Full-frame designed scene on track 2; channel radial background on from frame 0. The portrait `media/a2/A2-S5_c1_janowicz-1952-makio.png` (Commons PD, 1952 Makio yearbook, taken autumn 1951, 413 x 559, baked-in "VIC JANOWICZ" caption bar) is mounted INSIDE the comp as an `<img>`.

## 0. Claim
Ohio State's 3 points were Vic Janowicz's field goal through the blowing snow; the officials, barely able to see the posts, gave it to him.

## 1. Source
`factcheck/a2-r1.md` rows 18 (SABR: "His field goal gave Ohio State its only points."), 19 (SABR: "Michigan players protested that the kick was no good"; officials "peering through the swirling snow, guessed that it passed between the uprights"), 20 (Heisman announced 5 Dec 1950; voice only). Source line per Picture line: "SABR biography project".

## 2. Datum, scale, orientation
Left half: portrait card. Right half: goalpost scene, schematic (NOT a diagram of the kick; no distance: the spoken line gives none, factcheck "Not settled" 25 vs 38 yd). Goalpost drawn front-on.

## 3. Geometry (px, 1920 x 1080)
- Portrait card (left): polaroid frame 440 x 560, left 200, top 200, rotation -2° (set at 0 by `tl.set`, never in CSS), padding 22 px, bottom band 90 px. Image crop: show the face and shoulders only; crop OFF the baked "VIC JANOWICZ" caption bar (measure its top edge on the PNG; clip the img container above it) so the name appears once, in our type. Image area 396 x 446, `object-fit: cover`, `object-position: 50% 20%`, grade `.archgrade` values.
- Caption in the band (`.pol-cap`): "Vic Janowicz" Georgia italic 34 px `#2a2622`; second line "Ohio State · photo 1951" Arial 700 19 px `#6b6257`. (The photo is from 1951: the caption says so, so nothing implies game day.)
- Name card is the caption itself (edit_script "VIC JANOWICZ · OHIO STATE": same words, proper case in the serif caption plus the line below). No second name line elsewhere.
- Goalpost scene (right, x 900 to 1560, y 180 to 640): crossbar 1 line x 1060 to 1400 at y 470, uprights x 1060 and 1400 from y 180 to 470, post down from (1230, 470) to (1230, 640); 10 px strokes `#f2f5f8` at 85 %. A white snow veil over the scene: 3 stacked full-width rects with radial gradients `rgba(242,245,248,.0 → .55)` drifting x ±40 px (sine, finite repeats), so the uprights read half hidden; plus 90 flakes blowing left to right at 140 to 220 px/s (driving snow, precomputed array, finite repeats).
- Ball arc: a quadratic path from (980, 700) up through (1180, 260) to (1260, 330) (ends between the uprights, above the bar: inside the posts by about 30 px... the end point x 1260 is inside 1060 to 1400 and y 330 above the bar at 470). Ball: 28 x 18 px ellipse `#d8a13a` moving along the path by per-leg `attr` tweens (MotionPathPlugin not bundled), opacity 1 to 0.15 as it goes (fading into snow). Dash trail: path stroke 3 px `rgba(242,245,248,.5)`, dasharray `ceil(len)+1`.
- Chip (lower-third zone of the right half): glass card left 900, top 690? NO: keep it above the circle line: top 560, left 1000, padding 18 x 30, text "OHIO STATE'S ONLY POINTS" Arial Black 900 52 px `#f2f5f8` (card right edge about 1780 at y 560 to 650: right of x 1600 is allowed above y 680). Then put the scene's post bottom at y 540 instead of 640 so nothing sits under the chip.
- Source line "Source: SABR biography project" Arial 700 19 px `#c8d3e0`, left 110, bottom 60.
- Tiers: 52 / 34 / 19 (+ caption 19).

## 4. Must be true in the picture
1. The ball ends between the uprights and above the crossbar (x 1060 < 1260 < 1400, y 330 < 470), and is at most 15 % visible there: the kick is "given", not shown clearly.
2. The name appears once (baked caption cropped off).
3. Nothing dates the portrait to 1950.
4. No yardage number anywhere.
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a2-s5.words.json`, seconds from A2-S5 start; Whisper wrote "Genoix" for "Janowicz")
Text: `Vic Janowicz` · `Ohio State · photo 1951` · `OHIO STATE'S ONLY POINTS` · `Source: SABR biography project`
- 0.00 "Ohio": ground, snow veil and blowing flakes on; source line on. `/* OHIO @0.00 */`
- 1.76 "Vic": portrait card in (`fromTo` y 40 to 0, autoAlpha, rotation -2 fixed, 0.6 s, power3.out); caption lines 0.3 s later. `/* VIC @1.76 (Janowicz @1.96) */`
- 2.90 "kicked": ball launches along the arc, 1.4 s, power1.out, fading as it rises. `/* KICKED @2.90 */`
- 4.30 "snow.": ball reaches the end point at 15 % opacity.
- 5.90 "argued": goalposts flicker in the veil (veil opacity +.15 for 0.6 s, yoyo). `/* ARGUED @5.90 */`
- 8.38 "see": veil thickens to its max (.65). `/* SEE @8.38 */`
- 10.18 "gave": chip in (y 20 to 0, autoAlpha, 0.4 s, power3.out); veil clears to .35 so the posts read. `/* GAVE @10.18 */`
- 11.32 to exit: flakes keep blowing; portrait floats y 0 to -6.
- Exit: last 0.6 s: chip `to` x 980, autoAlpha 0; portrait `to` x -980, autoAlpha 0; scene fades with them (0.6 s, power3.in). Hard cut to g-a2-6 follows ("hard cut" per A2-S6 Picture line).
Host: data-start = A2-S5 start, duration = 13.66 + 0.40 = 14.06 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
