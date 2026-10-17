# BRIEF · g-a1-strip-sirens · "a real sounding about once a year, a test about once a week" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S4. Full-frame MG on the channel ground (no footage under it), from
a1-s4 0.00 to the wav end 14.64. Paul's full-frame clip A1-S5 follows on a cut.
Base: SIREN STRIP (`_list.md` "Shared bases"). This brief holds the strip's px table. `g-a1-strip-warnings` copies it
unchanged, so whatever is built here is what A1-S7 opens on. Exemplars: `library/inhouse/stat-timeline.html` (rail and
tick build), `library/inhouse/event-timeline.html` (per-event marks on a year axis).
Open numbers: none drawn. Every Monday tick is a calendar date (computed). The "weather permitting" skips (S5) are not known, so every Monday is drawn.

## 0. What this graphic claims
Outside the weekly one-minute test, Joplin's sirens sounded for a real storm three times from 2007 to 2009, and then not
again until 22 May 2011 (S6, S7). The test ran about 52 times a year (S4). The picture is a dense grey comb with
four lone red marks and one long empty stretch.

## 1. SOURCE
- S4 "approximately 52 times per year. Also, according to the Joplin-Jasper County emergency manager, the average has been once per year (at most) since 2007." NIST Sec. 4.3.4.
- S5 "tested on a weekly basis in Joplin, weather permitting, at 10 a.m. on Mondays ... for a period of 1 min". NIST Sec. 4.3.1.
- S6 "In 2007, the sirens sounded once in Joplin for severe thunderstorm winds in excess of 70 mph (on January 18, 2007). The next year, the sirens sounded for an EF-1 tornado that hit outside the Joplin city limits (on May 10, 2008)." NIST Sec. 4.3.4.
- S7 "Then, in 2009, the sirens sounded on May 8 due to winds in excess of 85 mph. The next time the sirens sounded, according to the emergency manager, was on May 22, 2011." NIST Sec. 4.3.4.
- Per the S9 CONFLICT, no label calls the soundings "wind events" as a group. Each label says its own cause.

## 2. DATUM, SCALE, ORIENTATION (the SIREN STRIP table, shared)
- Time runs left to right. Axis start 1 Jan 2007 at x = 200; axis end 1 Jun 2011 at x = 1720. That is 1,612 days, so
  0.9429 px per day and 344.2 px per 365-day year (computed by `python3`, 17 Oct 26).
- Strip datum: tick band y 380 to 420. Axis baseline y = 440, a 2 px line in Label grey `#93a3b2`, 60 % opacity, x 200 to 1720.
- Year boundaries (1 Jan) are 1 px ticks y 440 to 452 at x 200.0, 544.2, 889.3, 1233.4, 1577.6. The year labels are
  centred in each year's span at x 372.1 (2007), 716.7 (2008), 1061.4 (2009), 1405.5 (2010), 1648.8 (2011), on baseline y 482.
- Presenter circle: the strip stays out of x ≥ 1600, y ≥ 680, so the circle may stay on.

## 3. GEOMETRY
- **Test ticks:** one per Monday from 1 Jan 2007 to 16 May 2011, the last Monday before 22 May 2011. That is 229 ticks:
  53 in 2007, 52 each in 2008, 2009 and 2010, and 20 in 2011 (computed). x = 200 + days since 1 Jan 2007 × 0.9429, so
  ticks sit 6.6 px apart. First tick x 200.0, last x 1704.9. Each tick is 2 px wide, y 380 to 420, `#93a3b2` at 70 %.
  Compute the positions by script from this rule; never place them by eye.
- **Red marks (real soundings):** 6 px wide, y 356 to 444 (overshooting the band by 24 px above and below), Danger red 2
  `#e74c3c`, centred at x 216.0 (18 Jan 2007), 666.7 (10 May 2008), 1009.0 (8 May 2009), 1710.6 (22 May 2011).
- **Mark labels** sit above the strip and are left-aligned on the mark's x, except 2011, which is right-aligned ending at x 1730:
  date line Arial 700 30 `#f2f5f8` on baseline y 300; cause line Arial 700 22 `#93a3b2` tracking 3 on baseline y 334.
  Label bottoms ≤ 345. The 2011 label is one line only.
- **Empty-gap bracket:** a 3 px dashed line (dash 10, gap 8), `#e74c3c` at 70 %, y = 366, from x 1017.0 to 1702.6
  (8 px inside the 2009 and 2011 marks). It sits 21 px under the label bottoms and 14 px above the tick band.
- **Row label:** "Joplin's outdoor sirens", Arial 700 26 `#93a3b2` tracking 8, left at x 200, baseline y 214.
- **Chip zone:** top centre, glass chip centred at x 960, y 96 to 166. One chip at a time.
- **Source line:** bottom-left, x 96, baseline y 1010, Arial 700 20 `#c8d3e0`.
- Ground: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`, on from frame 0.
- Frame coverage: the strip block spans x 200 to 1730, y 200 to 490. The empty lower half is the space `g-a1-strip-warnings` fills in A1-S7.
  For these 14.6 s, centre the block instead: translate the whole strip group by +170 px in y (block y 370 to 660) and
  state that offset in the receipt. `g-a1-strip-warnings` opens at offset 0, with a 0.6 s rise from +170 to 0 at its frame 0.
  The table above is the offset-0 geometry.

## 4. MUST BE TRUE IN THE PICTURE
1. There are exactly 229 grey ticks, evenly spaced at 6.6 px ±0.3, and none falls after the 22 May 2011 red mark.
2. The red marks sit at their dates: the 2008 to 2009 mark gap (342.3 px) and the 2009 to 2011 gap (701.6 px) are in a ratio
   of 0.49 ±0.02. The empty stretch must read about twice as long as one year.
3. There are four red marks, never three or five. The first three land together, and the fourth lands later on its own.
4. No label calls all of them wind events. The 2008 label says EF1 and outside the city.
5. The bracket touches neither a label nor a tick.
6. No tick, mark or label leaves the text-safe frame (x 96 to 1824).

## 5. PANEL TEXT (exact) and CUES
| element | text | cue (a1-s4) |
|---|---|---|
| ground, axis, year labels, row label | "2007" "2008" "2009" "2010" "2011" · "Joplin's outdoor sirens" | frame 0. Axis draws left to right 0.00 to 0.70 (strokeDashoffset); labels rise 0.20 to 0.70 |
| test ticks | (none) | "test" 1.46: reveal left to right, finished on "week." 2.98 (0.0066 s per tick, or one clip-rect sweep) |
| chip 1 | "ABOUT 52 TESTS A YEAR" (S4) | "week." 2.98 |
| marks 2007, 2008, 2009 + labels | "Jan 2007" / "winds over 70 mph" · "May 2008" / "EF1 outside the city" · "May 2009" / "winds over 85 mph" | "three" 5.18: the three marks scaleY 0 to 1 from the baseline together (0.35 s, back.out), the labels rise 0.15 s after |
| chip 2 (replaces chip 1) | "3 REAL SOUNDINGS" (S6, S7) | "times" 5.46: chip 1 out (0.3 s), chip 2 in |
| source line | "dates per the county emergency manager · NIST Sec. 4.3.4" | "three" 5.18 |
| pulse 2007 + 2009 | (none) | "Twice" 7.80: marks scale 1 to 1.18 to 1 (0.5 s), labels brighten to `#f2f5f8` |
| pulse 2008 | (none) | "once" 9.44: same pulse |
| gap bracket | (none) | "nothing," 11.80: draws left to right over 0.70 s |
| mark 2011 + label | "May 22, 2011" (S7) | "May" 12.84: mark rises; label in at 13.02 ("22,") |
| hold | | to 14.64. The whole strip floats 3 px up and down over 4 s, and chip 2 drifts. Cut on the host end (full-frame scene, cut allowed) |

Gaps between moves stay under 4 s (longest: 2.98 to 5.18). Duration 14.64 = the wav end.

## 6 to 8
`references/mg-brief-template.md` §6 (contract), §7 (tools), §7a (done line, all seven), §8 (receipt). Per 7a item 6, the
receipt states the 229-tick count, the four mark x values and the +170 px offset, all computed by script.
