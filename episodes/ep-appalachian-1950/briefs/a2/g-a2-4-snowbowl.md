# g-a2-4-snowbowl: Snow Bowl popfig and chips over the game still (A2-S4)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (red Abril popfig over footage, then glass chips); `library/inhouse/snippets/cards.css` `.popfig`, `.lt`, `.glasscard`. Copy values under the `s4-` prefix. Abril font: `@font-face { font-family: 'AbrilFig'; src: url('fonts/AbrilFatface-Regular.ttf'); }` (vendored in `episodes/ep-appalachian-1950/fonts/`).
Sits over: `media/a2/A2-S4_c1_harry-allis-extra-point-1950.png` on track 1 (Commons, public domain, photo dated 1950-11-25, 1147 x 707; provenance row: Michigan's Harry Allis kicking in the Snow Bowl). The orchestrator mounts it scaled to cover 1920 x 1080 with a slow push (scale 1.00 to 1.06 over the segment) on track 1. Overlay on track 3. Snow Bowl film is still SOURCE TBD; if licensed film lands, this overlay sits over it unchanged.

## 0. Claim
This is the Snow Bowl, Ohio Stadium, 25 Nov 1950: 45 punts between the teams, Michigan won 9 to 3.

## 1. Source
`factcheck/a2-r1.md` rows 11 (ILN: Michigan "9-3"; game named by Wikipedia and The Lantern), 12 (Lantern: Michigan 24 punts, Ohio State 21 = 45; chip "45 PUNTS" ok), 15 (ILN: "9-3 without ever earning a first down"), 17 (chip "MICHIGAN 9 · OHIO STATE 3" CONFIRMED). Date and place: nws-facts.md §3 ILN "Columbus 25 Nov (Snow Bowl)".

## 2. Datum, scale, orientation
Overlay text only. Zones: centre popup (popfig), lower-third (chips). Text-safe 96 / 54 px. Corner x >= 1600, y >= 680 empty.

## 3. Geometry (px, 1920 x 1080)
- Popfig (centre zone): big line "NOV 25, 1950" 'AbrilFig' 150 px `#d0121f`, text-shadow `0 4px 24px rgba(0,0,0,.65), 0 0 2px rgba(0,0,0,.9)`, centred at (960, 470). Sub line "OHIO STADIUM" Arial Black 900 40 px `#f2f5f8` tracking 6, same shadow, centred 30 px under the big line. A local scrim behind it: radial ellipse 1100 x 420 at (960, 500), `rgba(3,5,8,.55)` to transparent. (edit_script "OHIO STADIUM · NOV 25, 1950" breaks the popfig limit: big line 12 characters, 3 words; the place goes on the sub line, same words.)
- Chip 1 (lower-third): glass card anchored left 110, bottom 110 (`inset: auto`), padding 22 x 34, `display: table`. Line 1 "45 PUNTS" Arial Black 900 58 px `#f2f5f8`; line 2 "MICHIGAN 24 · OHIO STATE 21" is NOT used (not asked; one fact per frame). Single line only.
- Chip 2 (same lower-third slot, replaces chip 1): two lines, "MICHIGAN 9" and "OHIO STATE 3", each Arial Black 900 52 px `#f2f5f8`, with a 22 px label above "FINAL" Arial 700 22 px `#93a3b2` tracking 6. Scoreboard look: a 2 px `rgba(255,255,255,.14)` rule between the two team lines. Card right edge <= 900.
- Source line "Photo: Michiganensian 1951 (public domain)" Arial 700 19 px `#c8d3e0`, left 110, bottom 60. (The still's credit; the scores rest on NWS Wilmington, named in the description credits.)
- Tiers: 150 / 58 / 52 / 40 / 22 / 19.

## 4. Must be true in the picture
1. The picture under every second of the popfig and chips is the 25 Nov 1950 Snow Bowl still (provenance row) or cleared Snow Bowl film; never the postcard (`A2-S4_c2`, a 1950s card, not the game).
2. Popfig never overlaps a chip: popfig exits before chip 1 enters.
3. Chips cover no face and no player's kicking leg: read the frame; if the bottom-left covers the kicker, move both chips to top-left (left 110, top 110) and say so.
4. "45 PUNTS" lands on "45"; scoreboard lands on "won".
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a2-s4.words.json`, seconds from A2-S4 start)
Text: `NOV 25, 1950` · `OHIO STADIUM` · `45 PUNTS` · `FINAL` · `MICHIGAN 9` · `OHIO STATE 3` · `Photo: Michiganensian 1951 (public domain)`
- 0.00 "That": source line in. `/* THAT @0.00 */`
- 0.36 "Ohio": popfig big line in (scale 1.25 to 1, autoAlpha 0 to 1, 0.45 s, power4.out), scrim with it; sub line 0.25 s later. `/* OHIO @0.36 */`
- 0.36 to 3.74: popfig drifts scale 1 to 1.03 (ease none).
- 3.74 "Bowl.": popfig out (scale to 0.94, autoAlpha 0, 0.4 s, power3.in). `/* BOWL @3.74 */`
- 5.22 "45": chip 1 in (`fromTo` x -60 to 0, autoAlpha, 0.6 s, power3.out). `/* 45 @5.22 */`
- 5.82 to 15.42: chip 1 floats y 0 to -6, sine yoyo, finite repeats.
- 16.20 (0.5 s before "Michigan"): chip 1 out (`to` x -60, autoAlpha 0, 0.4 s, power3.in).
- 16.76 "won": chip 2 in: "FINAL" first, then "MICHIGAN 9" on 17.00 "9", "OHIO STATE 3" on 17.30 "-3" (each y 20 to 0, autoAlpha, 0.35 s). `/* WON @16.76 */ /* 9 @17.00 */ /* 3 @17.30 */`
- 17.70 to exit: chip 2 floats y 0 to -6.
- Exit: chip 2 `to` x 980, autoAlpha 0, 0.6 s, power3.in in the host's last 0.6 s.
Host: data-start = A2-S4 start, duration = 20.84 + 0.40 = 21.24 s. The still under it spans the same window (orchestrator mount).

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 7: one frame composited over the real still at A2-S4 5.8 s and at 18.0 s.
