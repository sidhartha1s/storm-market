# g-a5-4-tally-final · A5-S3 · deep · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-a3-6-tally-27dec.html` (A3-S4's tally: this is the same system returning, so match its ground, block style, colours, label style, halfway line and readout exactly, rescaled to 46 blocks) and `library/inhouse/ranked-bars.html` (fill animation). Brief of the original: `briefs/a3/g-a3-6-tally-27dec.md`.

## 0. What this graphic claims
By the last reported count, 46 people lost their lives in Erie County (47 with the Lockport man in Niagara County). Outside was still the biggest group, 18; with the 4 found in their cars that is 22 of 46: close to half, not half. Even against the 12 listed without power or heat, the street cost more lives.

## 1. SOURCE
- `research/deaths.md` section 1 row "final" and section 2: 46 Erie + 1 Niagara = 47; 18 outside, 12 no power or heat, 7 delayed EMS, 4 vehicles, 4 shovelling or snow-blowing, 1 hotel-pool drowning; sum 46. WIVB, Poloncarz; ME confirmed the last 3, https://www.wivb.com/weather-news/buffalo-blizzard-2022/erie-county-medical-examiner-confirms-three-more-blizzard-related-deaths-bringing-total-to-47/amp/ (SECONDARY). Same figures: `research/response.md` section 5 "Where people were found" row "final".
- `research/deaths.md` section 3: outdoors + vehicles = 22 of 46 = 48 % ("close to half", never "half" or "most"). `factcheck/a5-r1.md` rows 11, 12, 32 (CONFIRMED).
- "last reported count (3 cases pending)": `factcheck/intro-r3.md` row 8 and `factcheck/a3-r1.md` row 33 (WIVB states three pending cases; announcement date UNCONFIRMED).
- Other causes = 46 - 18 - 4 - 12 = 12 (7 EMS + 4 shovelling + 1 hotel pool, same row). Not spoken; shown as dim blocks named "OTHER CAUSES".

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `tf-ground`, frame 0). Scale: 1 block = 1 person. 46 blocks, pitch 30 px, block width 24, left to right, x 150-1524, y 470-590. Halfway datum = bar midpoint x 837 (23 blocks: the gap between block 22 and block 23, x 834-840). The Niagara block sits apart, after a 60 px gap. Corner x >= 1600, y >= 680 empty (bar ends at y 590; the Niagara block ends at x 1608 but y 590 < 680).

## 3. GEOMETRY (px) — compute every x from the formula with a script and print it in the receipt
- Block i (i = 0..45): rect x = 150 + 30 i, width 24, y 470, height 120, radius 5. Bar span x 150-1524.
- Runs, left to right (colour when lit / dim state):
  - OUTSIDE i 0-17 (18): x 150-684, centre 417, lit `#f2f5f8`.
  - IN THEIR CARS i 18-21 (4): x 690-804, centre 747, lit `#d8a13a`.
  - NO POWER OR HEAT i 22-33 (12): x 810-1164, centre 987, lit `#7fb2e5`, settled `#5a768f`.
  - OTHER CAUSES i 34-45 (12): x 1170-1524, centre 1347, `#2a3644` throughout.
  - Base fill before any colour: `#2a3644`. Unfilled: 1 px `rgba(255,255,255,.14)` outline, transparent fill.
- Niagara block N: x 1584, width 24, y 470, height 120, fill `#93a3b2` at 60 %. Tag "+1 NIAGARA" Arial 700 26 px `#93a3b2` tracking 4, centred x 1596, top 410 (about x 1520-1672). Must not touch the readout or the halfway tag.
- Halfway line `tf-half`: dashed 3 px `#e74c3c`, dash 10 8, x 837, y 430-610. Tag "HALF" Arial 700 22 px `#e74c3c` tracking 6, centred x 837, top 396.
- Run labels (Arial 700 26 px tracking 4, colour of their run), two rows so none collides; the builder measures each box and states it:
  - Row 1, top 620: "OUTSIDE · 18" centred 417 (about 299-535); "NO POWER OR HEAT · 12" centred 987 (about 761-1213).
  - Row 2, top 668: "IN THEIR CARS · 4" centred 747 (about 590-904) with a 2 px `#d8a13a` tick from the bar bottom (y 590) to y 662 at x 747; "OTHER CAUSES" `#93a3b2` at 70 % centred 1347 (about 1218-1476).
  - Gap of at least 24 px between any two labels, and no label under the halfway line (it ends at y 610; labels start at 620).
- Readout (one zone, three pre-authored states, one visible at a time): centred x 837, top 270, Arial Black 900 84 px: "46" `#f2f5f8`; "47" `#f2f5f8`; "22" `#f2f5f8` + " OF 46" `#93a3b2`.
- Title zone: eyebrow "ERIE COUNTY" Arial 700 22 px `#93a3b2` tracking 6, `left:96px; top:96px`; headline "THE LAST REPORTED COUNT" Arial Black 900 52 px `#f2f5f8`, left 96, top 132 (about x 96-926, y 132-196). Only these two lines top-left.
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "Poloncarz via WIVB, last reported count (3 cases pending)".
- Type tiers: 84/52 big, 26 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 46 blocks in the bar, equal size and pitch, plus exactly 1 block apart. Count them on the settled frame: 18 white, 4 amber, 12 blue, 12 dim.
2. The white + amber run (22 blocks) ends at x 804, LEFT of the halfway line x 837: 22 < 23. The line falls in the gap after block 22, one block past the lit run ("close to half", never half).
3. The halfway line is the bar's true midpoint (x 837 ± 2), never moved to touch the lit run.
4. "47" shows only while the Niagara block is lit; when "22 OF 46" shows, the Niagara block is dimmed to 25 % (it is outside the 46).
5. OUTSIDE (18) is visibly the longest single run, longer than NO POWER OR HEAT (12): 540 px vs 360 px.
6. No percentage, no "MOST", no 31 or 39 on screen. Numerals on screen, words in the voice.
7. No label touches a block, the line, the tick or another label; nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S3 start, `audio/a5-s3.words.json`)
Strings: `ERIE COUNTY` · `THE LAST REPORTED COUNT` · `46` · `47` · `22` · ` OF 46` · `+1 NIAGARA` · `HALF` · `OUTSIDE · 18` · `IN THEIR CARS · 4` · `NO POWER OR HEAT · 12` · `OTHER CAUSES` · `Poloncarz via WIVB, last reported count (3 cases pending)`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "the last count" @0.00-0.74 | ground on frame 0; 46 empty outlines fade in 0.0-0.6 (stagger 0.012); eyebrow at 0.22, headline at 0.50 `fromTo(x:-40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)` |
| 0.96 | "46" @0.96 | all 46 blocks fill `#2a3644`, `scaleY 0 -> 1` from bottom, stagger 0.02 (0.9 s); readout "46" `fromTo(scale 1.2 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)`; source in at 1.20 |
| 3.62 | "Lockport," @3.62-4.04 | Niagara block in `fromTo(x:40 -> 0, autoAlpha 0 -> 1, 0.45, back.out)`; "+1 NIAGARA" in at 3.80 |
| 4.70 | "47." @4.70 | readout "46" out / "47" in (cross-swap 0.3 s, `y` 12 -> 0) |
| 5.86 | "outside" @5.86 | readout "47" out at 6.20 (0.4 s) |
| 8.30 | "18" @8.30 | blocks 0-17 recolour white, left to right, stagger 0.03 (0.54 s), each `scale 1 -> 1.08 -> 1`; "OUTSIDE · 18" in at 8.64 `fromTo(autoAlpha 0, y:10 -> 0, 0.4, power3.out)` |
| 9.86 | "4" @9.86, "cars" @10.70 | blocks 18-21 recolour amber, stagger 0.08; tick draws `scaleY 0 -> 1` at 10.40; "IN THEIR CARS · 4" in at 10.70 |
| 12.20 | "22." @12.20 | blocks 0-21 pulse together `scale 1 -> 1.1 -> 1`, 0.5 s; Niagara block dims to 25 %; readout "22 OF 46" `fromTo(scale 1.2 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| 13.52 | "Out of 46," @13.22-13.98 | "OTHER CAUSES" in at 70 % (0.4 s) |
| 14.52 | "close to half." @14.52-15.22 | halfway line draws top to bottom `scaleY 0 -> 1`, 0.5 s; "HALF" in at 14.92 |
| 16.54 | "dark, cold houses," @16.54-17.78 | blocks 22-33 recolour `#7fb2e5`, stagger 0.04; "NO POWER OR HEAT · 12" in at 17.06 |
| 18.36 | "the streets still cost more lives" @18.36-19.94 | blue run settles to `#5a768f` (0.6 s); a sheen sweeps the white + amber run x 150 -> 804 (0.7 s) at 18.66; "OUTSIDE · 18" to `#ffffff` |
| whole window | | after each step the newest group floats y 0 -> -3 (sine, yoyo, finite); no 4 s gap without a tween (check 0.6-3.6 and 6.2-8.3) |
| 21.10 to 21.70 | after "else." ends @20.82 | whole layer pulls back `scale 1 -> 0.96`, autoAlpha 0, 0.6, power3.in; ground stays |

Comp duration 21.70 s (0.63 s past the wav end; trim to the real gap).

## 6. CONTRACT
One file `compositions/g-a5-4-tally-final.html`, root `id="g-a5-4-tally-final-root"`, `data-composition-id="g-a5-4-tally-final"`, PAUSED timeline `window.__timelines["g-a5-4-tally-final"]`. Prefix `tf-` (never `ty-`, which g-a3-6 uses: two comps share the page). Blocks positioned by `tl.set` from the formula (a loop over i is fine; the brief's table is the source). Repeat notes: "46" appears in the readout "46" and later in "22 OF 46", never in the same frame; "OUTSIDE" and "18" also appear in A3-S4 and the intro (other comps, minutes earlier): a callback, not a per-frame repeat; `data-callback="A5 completes the A3 tally"` goes on the index mount. Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-4-tally-final`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-4-tally-final`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print every block's x, the four run spans, the Niagara block x and the midpoint from the page. Build this before `g-a5-9-ban-card` (it copies this system at a smaller pitch).

## 8. RECEIPT
As the template.
