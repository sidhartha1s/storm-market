# g-a4-2-sinking-fleet · A4-S2 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/moves/` (`moves.js` settle and dust helpers, README) for the sinking and the snow puffs; the one-at-a-time build of `library/inhouse/ef-ladder.html` for the rows. Name card and chip: the chip surface of the built `compositions/g-intro-2-toll-chips.html`.

## 0. What this graphic claims
1. The snow-clearing fleet was stuck: about two of every three (S1's figure, shown here as 8 of 12 plow icons, two in every group of three).
2. The NYU review (led by Sarah Kaufman) found the same on the emergency side: rescue vehicles stuck or frozen to the ground, and most Buffalo Fire Department vehicles stuck at some point.
3. So an ambulance could not get down a street a plow was stuck on.

## 1. SOURCE
- Two-thirds stuck (the plow row): `factcheck/a4-r1.md` row 4 (CBS Miami quoting Poloncarz, SECONDARY), `research/deaths.md` section 5.
- NYU Wagner "Lessons Learned from the Buffalo Blizzard", June 2023 (authors Kaufman and Zimmerman), read as full text: "Rescue vehicles got stuck in the snow or frozen to the ground" (`factcheck/a4-r1.md` row 6) and "most of their vehicles becoming stuck in ice and snow at some point during the blizzard" (row 7, CONFIRMED in the report itself). `research/response.md` section 2 NYU row (released 2 Jun 2023).
- "Most" carries no number in any source. The engine row is a picture of "a majority", never a ratio: no count is printed.

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed ground, 1920 x 1080. No map. Icon scale fixed: plow icon 96 x 64 px, engine icon 110 x 64 px. Snow surface lines: row 1 at y 372, row 2 at y 656. Presenter circle may be on: nothing in x >= 1600, y >= 680 (the corner stays empty ground).

## 3. GEOMETRY (px)
- Ground: channel radial gradient (tokens.md "Canvas") on the root from frame 0.
- Falling snow: 40 dots, 2 to 4 px, `#dfe7ee` at 0.5 to 0.8 opacity, fall 20 px/s with a slight sideways drift, finite repeats over the whole window (this is the always-moving layer).
- Row 1, plows: 12 flat silhouettes (`#dfe7ee` body, `#93a3b2` blade, no logo, no text), left edges x = 250 + 118 i (i = 0 to 11, last ends at 1644), standing on y 372 (icon y 308 to 372). Row label "PLOWS SENT OUT", Arial 700 22 px `#93a3b2`, letter-spacing 3, left edge x 250, baseline y 270.
- Drift 1: snow band in FRONT of row 1, x 200 to 1700, from y 372 to 430, fill `#dfe7ee` at 0.92 with a soft wavy top edge (amplitude 6 px). A sunk icon is hidden by it below y 372.
- Row 2, fire engines: 10 silhouettes (`#c0392b` body, `#dfe7ee` ladder line, no lettering), left edges x = 250 + 134 i (i = 0 to 9, last ends at 1566), standing on y 656 (icon y 592 to 656). Row label "BUFFALO FIRE DEPT.", Arial 700 22 px `#93a3b2`, letter-spacing 3, left edge x 250, baseline y 552.
- Drift 2: as drift 1, x 200 to 1590 (stops short of the corner), y 656 to 706.
- Sink move (one icon): `to(y:+40, rotation: ±7 (alternate sign), 0.55, power2.in)` then a 0.2 s settle `y +2 -> 0`; at contact, 6 snow-puff dots burst from the drift top at the icon's centre (moves.js dust), gone in 0.5 s. A sunk icon then dims to `#5a768f` (plows) or `#8e2020` (engines) over 0.3 s. Standing icons keep their colour.
- Which sink: row 1 icons i = 1, 2, 4, 5, 7, 8, 10, 11 (two in every group of three; i = 0, 3, 6, 9 stay up). Row 2 icons i = 0, 1, 2, 4, 5, 7, 8 (7 of 10; i = 3, 6, 9 stay up).
- Frost (row 2): each engine gets two 14 px wheel rings `#7fb2e5` and a 0.35-opacity `#7fb2e5` sheen over its lower half.
- Lower-third slot (HUD, one element at a time), glass surface as g-intro-2, `left:110px; bottom:110px`, padding 22 px 34 px:
  - Name card: "SARAH KAUFMAN" Arial Black `font-weight:900` 52 px `#f2f5f8` + " · NYU WAGNER" Arial 700 32 px `#e8c56a`, one baseline. About x 110 to 900, y 860 to 970.
  - Chip: "MOST" Arial Black 900 52 px `#e74c3c` + " FIRE VEHICLES STUCK" Arial Black 900 38 px `#dfe7ee`. About x 110 to 860.
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Street beat (14.22 on): both rows and drifts dim to opacity 0.18 and their labels go to 0. Centre lane: a road strip `#2a3644` x 360 to 1440, y 560 to 600, with a drift `#dfe7ee` mound at x 860 to 1100, y 470 to 600. In it, one plow (icon scale 1.5, 144 x 96) sunk to half its height, front at x 1080. Ambulance silhouette (scale 1.5, 165 x 96, `#f2f5f8` body, one `#e74c3c` stripe, NO red cross or star emblem) enters from x 120 and stops with its front at x 840 (a 20 px gap to the drift), resting on y 600.
- Type tiers: 52 (big), 32 and 38 (mid), 19 and 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 8 of the 12 plows are sunk at the end of the plow sequence, and in every group of three (i = 0-2, 3-5, 6-8, 9-11) exactly two are sunk.
2. 7 of 10 engines sink: clearly more than half, and no number appears anywhere in this comp (the chip says "MOST" in words).
3. A sunk icon is hidden below its drift's surface line (y 372 or y 656); nothing pokes through the drift.
4. Each sink lands on or after its cue; none sinks before "same" @4.24 (row 1) or "most" @11.06 (row 2).
5. Labels never sit on an icon or a drift; the name card and the chip are never on screen together; no text rides the dim or the ambulance move.
6. The ambulance stops before the drift and never overlaps the plow; it carries no red cross.
7. The corner x >= 1600, y >= 680 holds nothing but ground and falling snow.

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S2 start, `audio/a4-s2.words.json`)
Strings: `PLOWS SENT OUT` · `BUFFALO FIRE DEPT.` · name card `SARAH KAUFMAN · NYU WAGNER` · chip `MOST FIRE VEHICLES STUCK` · source `NYU Wagner review for the City of Buffalo, via AP and Firehouse, Jun 2023`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Months" @0.00 | ground, snow and drift 1 on from frame 0; row 1 icons in `fromTo(y:-20 -> 0, autoAlpha 0 -> 1, 0.35, power3.out)` stagger 0.05 from 0.05; label "PLOWS SENT OUT" in at 0.30 |
| 1.88 | "Sarah" @1.88 | name card in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; source pill in `fromTo(autoAlpha 0, y:16 -> 0, 0.4)` |
| 4.24 to 6.34 | "same thing on the emergency side" @4.24 to 5.34 | 8 plows sink in index order 1, 2, 4, 5, 7, 8, 10, 11 at 4.24, 4.54, 4.84, 5.14, 5.44, 5.74, 6.04, 6.34 |
| 5.60 to 5.95 | after "side." @5.34 | name card out `to(x:-80, autoAlpha 0, 0.35, power3.in)` |
| 6.54 | "Rescue vehicles" @6.54 | row 2 + drift 2 in (as row 1), stagger 0.05 |
| 8.36 | "froze" @8.36 | frost rings and sheen on all 10 engines `fromTo(autoAlpha 0 -> 1, scale 0.6 -> 1, 0.4, back.out(1.4))`, stagger 0.03 |
| 11.06 | "most" @11.06 | chip in (as name card); "MOST" `fromTo(scale 1.3 -> 1, 0.4, power4.out)` |
| 11.20 to 13.18 | "most of the Buffalo Fire Department's own trucks were stuck too" | engines 0, 1, 2, 4, 5, 7, 8 sink at 11.20, 11.53, 11.86, 12.19, 12.52, 12.85, 13.18 |
| 11.46 | "Buffalo" @11.46 | label "BUFFALO FIRE DEPT." in `fromTo(autoAlpha 0, y:10 -> 0, 0.35)` |
| 13.90 to 14.25 | after "too." @13.48 | chip out (as name card) |
| 14.22 | "If" @14.22 | rows and drifts to opacity 0.18, labels to 0, 0.5 s power2.inOut |
| 14.48 | "plow" @14.48 | lane, mound and half-buried plow in `fromTo(autoAlpha 0 -> 1, y:20 -> 0, 0.5, power3.out)` |
| 16.38 to 16.94 | "ambulance" @16.38, "no way" @16.94 | ambulance `fromTo(x:120 -> 840 (front edge), autoAlpha 0 -> 1, 0.56, power3.out)`, then a 4 px rock `rotation 0 -> -1.5 -> 0, 0.3` at 16.94 |
| whole window | | falling snow; standing icons bob `y 0 -> -2`, sine, finite repeats |
| 17.90 | wav end | comp ends on the hard cut into the S3 footage (full-frame scene: a cut is allowed, nothing vanishes mid-frame before it) |

Comp duration 17.9 s. Spoken time in a comment at each tween.

## 6. CONTRACT
One file `compositions/g-a4-2-sinking-fleet.html`, root `<div id="g-a4-2-sinking-fleet-root" data-composition-id="g-a4-2-sinking-fleet" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-2-sinking-fleet"]`. Ids prefixed `sf-`; classes prefixed `sf-`. Inline SVG icons; a sinking icon's group has no static `transform=` attribute (all transforms from `tl.set` at 0). Ground on from frame 0. Everything else: `references/mg-quickref.md` and the template section 6.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-2-sinking-fleet`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-2-sinking-fleet`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: icon x positions and the sink lists computed from section 3's formulas by a script, stated in the receipt. Full-frame: no footage under it.

## 8. RECEIPT
As the template.
