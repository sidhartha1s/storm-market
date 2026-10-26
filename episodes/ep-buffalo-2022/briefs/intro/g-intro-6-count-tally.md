# g-intro-6-count-tally · I1-S3 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/ranked-bars.html` (fill-animated rails on a shared scale). Deep because it carries the episode's angle claim across four changing states on one scale.

## 0. What this graphic claims
As the county's count climbed after Christmas (31, 37, 39, then 46 at the last report), "found outside" was the biggest group at every count that had a breakdown. It is the biggest group, never a majority: 18 of 46.

## 1. SOURCE
`research/deaths.md` section 1 (all SECONDARY), with the next-largest group used for the second bar:
| step | label on screen | outside | total | next-largest group (category as reported) | source |
|---|---|---|---|---|---|
| 1 | 27 DEC | 17 | 31 | 7 (lack of heat) | NPR via KAXE, county health department, 27 Dec evening: https://www.kaxe.org/news/news/2022-12-27/at-least-31-people-have-died-in-buffalos-erie-county-due-to-destructive-winter-storm |
| 2 | 28 DEC | 17 | 37 | 9 (lack of heat) | AP via Fox11, 28 Dec (source of the split not named): URL in `research/deaths.md` row 28 Dec |
| 3 | 30 DEC | 17 | 39 | 11 (inside unheated homes) | WBFO via btpm.org, Erie County ME office, 30 Dec: https://www.btpm.org/local/2022-12-30/after-national-guard-search-storm-death-toll-stands-at-39 |
| 4 | LAST REPORTED | 18 | 46 | 12 (no power or heat) | Poloncarz via WIVB (no date on page; three cases pending): URL in `research/deaths.md` row "final" |
Fact check: `factcheck/intro-r3.md` rows 24 and 26 (steps, values and next groups 7, 9, 11, 12 CONFIRMED; never "most"; last step undated and never "final"; categories were reshuffled between counts, so the second bar is labelled "NEXT LARGEST GROUP", never a category name).
The 26 Dec count (25) had no breakdown and is not shown.

## 2. DATUM, SCALE, ORIENTATION
- Full-frame designed graphic on the channel ground (`radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`) from frame 0.
- One shared bar scale for every step and both bars: 50 px per person, origin x = 220 (left edge of every bar). Bars grow rightward. Computed by script; state the lengths in the receipt.
- Corner x >= 1600, y >= 680 empty (presenter circle may be on).

## 3. GEOMETRY (px)
- Step rail: 2 px line `#2a3644`, y 210, from x 220 to x 1240, drawn segment by segment as steps land. Markers: 14 px circles at x 220, 560, 900, 1240 (y 210). Labels centred under each marker, top 232, Arial 700 22 px, letter-spacing 3: "27 DEC", "28 DEC", "30 DEC", "LAST REPORTED". Active marker and label `#f2f5f8`; past ones `#93a3b2`. "LAST REPORTED" is about 230 px wide, so x about 1125 to 1355.
- Lead figure: left 220, top 300, Arial Black `font-weight:900` 84 px. Two leaves on one baseline: outside number in `#e74c3c` ("17", later "18") and " OF <total>" in `#f2f5f8` ("OF 31", "OF 37", "OF 39", "OF 46"). Pre-authored leaves per value, swapped with autoAlpha. Width of "18 OF 46" about 420 px.
- Sub line under it: "FOUND OUTSIDE, OF ALL COUNTED", Arial 700 22 px `#93a3b2`, letter-spacing 4, left 220, top 400.
- Bar 1 label: "OUTSIDE", Arial 700 26 px `#f2f5f8`, letter-spacing 8, left 220, top 462. Bar 1: y 500 to 560 (60 tall), radius 6, fill `linear-gradient(90deg, #c0392b, #e74c3c)`, `scaleX` from left: full length 900 px authored (18 people), so 17 = scaleX 0.9444 (850 px, right end x 1070) and 18 = scaleX 1 (900 px, right end x 1120).
- Bar 2 label: "NEXT LARGEST GROUP", Arial 700 26 px `#93a3b2`, letter-spacing 8, left 220, top 592. Bar 2: y 630 to 690, radius 6, fill `#5a768f`, authored 900 px with the same origin: 7 = 0.3889 (350 px), 9 = 0.5 (450 px), 11 = 0.6111 (550 px), 12 = 0.6667 (600 px, right end x 820). Bar 2's right end never passes x 820, far left of x 1600, so the corner stays clear.
- No numerals on the bars (lengths only; the lead figure carries the number, one fact once).
- Lead-at-every-count ticks: a 10 px `#e74c3c` dot appears just above each rail marker (y 186) at its cue in section 5.
- Sheen: a 120 px wide white gradient `rgba(255,255,255,.35)` clipped to bar 1, sweeping x 220 to 1120.
- Source line: "Erie County counts via NPR/KAXE, AP, WBFO; last reported count, Poloncarz via WIVB", Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`.
- Type tiers: 84 (big), 26 (mid), 19 to 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. At every step the OUTSIDE bar is longer than the NEXT LARGEST GROUP bar, by the true ratio: 17:7, 17:9, 17:11, 18:12 (850/350, 850/450, 850/550, 900/600 px, ±10 px).
2. The OUTSIDE bar does not change length across steps 1 to 3 (17 stays 17) and grows by exactly 50 px at step 4; only the totals climb. That is the picture of "kept climbing ... outside stayed the biggest group".
3. Nothing on screen says "most", "majority" or "final"; the last step reads "LAST REPORTED" with no date.
4. The lead figure always matches the active rail marker (31 with 27 DEC, 37 with 28 DEC, 39 with 30 DEC, 46 with LAST REPORTED).
5. Steps land in date order on the voice's words; the rail never shows a future date before its step.
6. Corner x >= 1600, y >= 680 empty; all text inside x 96 to 1824, y 54 to 1026.

## 5. PANEL TEXT (exact) and CUES (seconds from I1-S3 start, `audio/i1-s3.words.json`)
Strings: `27 DEC` `28 DEC` `30 DEC` `LAST REPORTED` · `17` `18` · `OF 31` `OF 37` `OF 39` `OF 46` · `FOUND OUTSIDE, OF ALL COUNTED` · `OUTSIDE` · `NEXT LARGEST GROUP` · source as section 3
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "The" @0.00 | ground on; bar labels and empty bar tracks (`rgba(255,255,255,.06)`, full 900 px) visible from frame 0 |
| 0.14 | "county's" @0.14 | step 1: marker 1 + "27 DEC" in (`fromTo(autoAlpha 0, y:10 -> 0, 0.3)`); lead "17" + "OF 31" in `fromTo(autoAlpha 0, y:24 -> 0, 0.4, power3.out)`; sub line in; bar 1 `scaleX 0 -> 0.9444`, bar 2 `scaleX 0 -> 0.3889`, both 0.6 s power3.out |
| 1.60 | "days" @1.60 | step 2: rail segment 1 to 2 draws (`scaleX`, 0.3); marker 2 + "28 DEC" in, "27 DEC" to `#93a3b2`; "OF 31" out `to(y:-20, autoAlpha 0, 0.2)`, "OF 37" in `fromTo(y:20 -> 0, autoAlpha 0 -> 1, 0.3)`; bar 2 `to(scaleX 0.5, 0.5, power3.out)` |
| 2.28 | "Christmas," @2.28 | step 3: same pattern to marker 3 "30 DEC", "OF 39", bar 2 to 0.6111 |
| 3.46 | "every" @3.46 | step 4: marker 4 "LAST REPORTED"; "17" -> "18" and "OF 39" -> "OF 46" (same roll); bar 1 `to(scaleX 1, 0.5, power3.out)`; bar 2 to 0.6667 |
| 3.76, 4.10, 4.38, 4.60 | "county" @3.76, "count" @4.10, "I" @4.38, "could" @4.60 | red lead dots on markers 1, 2, 3, 4 in turn: `fromTo(scale 0 -> 1, 0.25, back.out(2))` |
| 5.98 | "outside" @5.98 | "OUTSIDE" label to `#ffffff`; sheen sweeps bar 1, `fromTo(x:0 -> 900, 0.7, power2.inOut)` |
| 6.58 | "biggest" @6.58 | bar 1 `fromTo(scaleY 1 -> 1.12 -> 1, 0.4)` |
| 7.58 | "What none of those counts said" @7.58 | rail, markers, dots, lead figure, sub and bar 2 dim `to(opacity 0.4, 0.6)`; bar 1 and its label stay full |
| 7.6 to 11.1 | "... why so many people were out there in the first place." | bar 1 breathes `scaleY 1 -> 1.05`, `sine.inOut`, finite yoyo (about 0.9 s cycles); whole group drifts `y 0 -> -6`, ease none |
| 11.20 to 11.80 | after "place." @11.02 | exit, fade-through: all but the ground `to(autoAlpha 0, 0.6, power2.in)` |
Comp duration 12.0 s. Spoken time in a comment at each tween.

## 6. CONTRACT
One file `compositions/g-intro-6-count-tally.html`, root `<div id="g-intro-6-count-tally-root" data-composition-id="g-intro-6-count-tally" data-width="1920" data-height="1080">` with the ground on it. PAUSED timeline at `window.__timelines["g-intro-6-count-tally"]`. Ids prefixed `ct-`, classes `ct-*`. Bars animate `scaleX` with `transformOrigin:"left center"`, never `width`. Text pre-authored per value, toggled with autoAlpha. Start-hidden in CSS too. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-6-count-tally`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-6-count-tally`. Check section 4 on the contact sheet first.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: bar lengths from the section 1 table by script, stated in the receipt. Item 4 (seek order) at 0.14, 1.60, 2.28, 3.46, 5.98.

## 8. RECEIPT
As the template.
