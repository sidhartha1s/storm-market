# g-a5-7-county-plan · A5-S6 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: official `mk-specs-list` (`library/official/`: left-aligned checklist rows slide in staggered with an accent underline), set on the panel look of `library/inhouse/stat-panel.html` (eyebrow, headline, rows).

## 0. What this graphic claims
After the blizzard Erie County's own plan called for three things: tracked vehicles that carry patients, ambulances teamed with them, and more driving bans called before a storm. The third one is about timing ("the clock").

## 1. SOURCE
- WIVB, "Erie County announces several changes for blizzard preparedness", posted 14 Aug 2023, Poloncarz announced "on Monday", https://digital-release.wivb.com/?p=1518271: "purchase of tracked rescue vehicles and other equipment to transport medical patients"; "Ambulances will also be teamed up with tracked vehicles to get to patients who need assistance"; "a new policy will also be created to increase pre-emptive driving bans": `factcheck/a5-r1.md` row 21 and its "New evidence" block (CONFIRMED, SECONDARY).
- Row strings are the Picture line's, which paraphrase these three quotes; no row adds a number, a vehicle count or a date beyond the source line.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `cp-ground`, frame 0). One panel, left-centre. Corner x >= 1600, y >= 680 empty. No scale.

## 3. GEOMETRY (px)
- Panel (`#15202b` at 94 %, 1 px `rgba(255,255,255,.14)` border, radius 24), x 200-1440, y 200-820. Content left x 270.
- Eyebrow "ERIE COUNTY · AFTER THE BLIZZARD" Arial 700 22 px `#93a3b2` tracking 6, top 250.
- Headline "THE COUNTY'S PLAN" Arial Black 900 52 px `#f2f5f8`, top 288.
- Rows (each: a 44 px check box at x 270 with a 2 px `#93a3b2` outline, radius 8; a check mark path 4 px `#e8c56a` drawn by stroke-dashoffset, dash `ceil(len)+1`; row text Arial Black 900 38 px `#dfe7ee` at x 340; a 2 px underline `#e8c56a` under the text, `scaleX 0 -> 1` from left):
  - Row 1, centre y 440: "TRACKED VEHICLES FOR PATIENTS".
  - Row 2, centre y 560: "AMBULANCES PAIRED WITH THEM".
  - Row 3, centre y 680: "MORE DRIVING BANS BEFORE THE STORM" (about x 340-1390 at 38 px; if the measured width passes x 1390, set 36 px on all three rows and state it).
- Clock icon (self-drawn SVG: 72 px circle, 3 px `#e8c56a` stroke, two hands), outside the panel, centre (1500, 680), right edge 1536 < 1600, level with row 3. The minute hand turns once on "clock".
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "Erie County plan, via WIVB, 14 Aug 2023".
- Type tiers: 52 big, 38 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Row strings exactly as §5; no count of vehicles, no cost, no "NEW POLICY" wording added.
2. Each row and its tick land on the voice: row 1 on "tracked vehicles", row 2 on "ambulances", row 3 on "more driving bans"; ticks after each row's phrase ends.
3. On "the second one is about the clock" only row 3 stays at full brightness (rows 1-2 at 45 %) and the clock icon is next to row 3, nowhere else.
4. Nothing in x >= 1600, y >= 680; text 96 px from the edges.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S6 start, `audio/a5-s6.words.json`)
Strings: `ERIE COUNTY · AFTER THE BLIZZARD` · `THE COUNTY'S PLAN` · `TRACKED VEHICLES FOR PATIENTS` · `AMBULANCES PAIRED WITH THEM` · `MORE DRIVING BANS BEFORE THE STORM` · `Erie County plan, via WIVB, 14 Aug 2023`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "The county" @0.14 | ground on frame 0; panel in `fromTo(x:-120 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)` at 0.10; eyebrow at 0.34 |
| 0.98 | "plan too." @0.98-1.60 | headline `fromTo(x:-40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`; source in at 1.30; three empty check boxes `fromTo(autoAlpha 0, scale 0.8 -> 1, 0.3)`, stagger 0.1, at 1.40 |
| 2.54 | "tracked vehicles" @2.54-3.32 | row 1 text `fromTo(autoAlpha 0, x:-24 -> 0, 0.4, power3.out)` |
| 4.82 | "deep snow," @4.56-5.24 | row 1 tick draws 0.35 s; underline at 4.95 |
| 5.72 | "ambulances" @5.72-6.34 | row 2 text in (as row 1) |
| 6.88 | "teamed up with them." @6.34-7.28 | row 2 tick at 7.04; underline at 7.15 |
| 8.26 | "more driving bans," @8.26-9.40 | row 3 text in (as row 1) |
| 10.00 | "ahead of a storm." @10.00-10.76 | row 3 tick at 10.44; underline at 10.55 |
| 13.16 | "went wrong that Friday," @12.68-13.70 | all three ticks pulse `scale 1 -> 1.15 -> 1` (0.4 s), stagger 0.1 |
| 14.48 | "the second one is about the clock." @14.48-15.50 | rows 1-2 to 45 % (0.4 s); row 3 text to `#f2f5f8`; clock icon `fromTo(autoAlpha 0, scale 0.6 -> 1, 0.35, back.out)` at 14.84; minute hand turns 360° (0.9 s, power2.inOut) at 15.10 |
| whole window | | panel floats y 0 -> -4 (sine, yoyo, finite); no 4 s gap without a tween |
| 16.20 to 16.80 | after "clock." @15.50 | panel and clock out `to(x:-160, autoAlpha 0, 0.6, power3.in)`; source out |

Comp duration 16.80 s (1.07 s past the wav end; trim to the real gap, keeping at least 0.7 s after the clock turn ends at 16.00).

## 6. CONTRACT
One file `compositions/g-a5-7-county-plan.html`, root `id="g-a5-7-county-plan-root"`, `data-composition-id="g-a5-7-county-plan"`, PAUSED timeline `window.__timelines["g-a5-7-county-plan"]`. Prefix `cp-`. Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-7-county-plan`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-7-county-plan`.

## 7a. DONE LINE
All seven items of the template 7a. Read settled frames at 11.5 s and 15.8 s.

## 8. RECEIPT
As the template.
