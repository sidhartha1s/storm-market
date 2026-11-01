# g-a6-11-season · A6-S8 3.44 to end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `episodes/ep-nepal-floods-2026/compositions/g-monsoon-calendar.html` (season strip on a month axis).

## 0. Claim
The next Atlantic hurricane season runs June 1 to November 30 and peaks around September 10.

## 1. Source
- NOAA National Hurricane Center climatology (sources-a6.md §5): "The official hurricane season for the Atlantic basin is from June 1 to November 30"; "The peak of the Atlantic hurricane season is September 10".
- The year (2027) is spoken only: no year on screen (`_list.md` change 8), so a publish-date change re-voices one line and touches nothing here.

## 2. Datum, scale, orientation
A month axis left to right, January to December, x 160 to 1760 (1600 px for 365 days: 4.384 px per day). Axis line y 620, 3 px `#93a3b2`; month ticks at each month's first day; month labels (Jan, Feb ... Dec) Arial 700 22 px `#93a3b2` centred under each month at y 650. Day positions computed by a script (x = 160 + (day of year − 1) × 1600/365, 2027 is not a leap year) and listed in the receipt: June 1 = day 152 → x 821.9 (non-leap); Nov 30 = day 334 → x 1619.7; Sept 10 = day 253 → x 1264.7.

## 3. Geometry (px)
- Ground: tokens.md radial gradient (full-frame designed).
- Season band: rect from x 821.9 to 1619.7, y 560 to 620, fill `#2f5d86` opacity 0.8, scaleX 0 to 1 from the left (June 1 edge).
- Activity curve (optional shape): a smooth hump inside the band peaking at x 1264.7; SCHEMATIC shape (no climatology counts are in the research), drawn as a 3 px `#7fb2e5` line, and labelled nothing. If the builder prefers, drop it; the peak marker carries the claim.
- Peak marker: vertical line `#d0121f` 3 px at x 1264.7 from y 480 to 620, a 14 px dot at its top.
- Chip C1 "HURRICANE SEASON · JUNE 1 TO NOV 30": glass, eyebrow "HURRICANE SEASON" Arial 700 24 px `#93a3b2` tracking 4, main line "JUNE 1 TO NOV 30" Arial Black 900 56 px; centred x 1221 (band centre), top 260.
- Chip C2 "PEAK · SEPT 10": glass, eyebrow "PEAK", main "SEPT 10" Arial Black 900 56 px `#f5d98b`; centred on x 1264.7, top 700 (below the axis labels, which end about y 672; C2 bottom about 800).
- Presenter circle: C2 spans about x 1115 to 1415 and everything else ends above y 680, so the corner (x >= 1600, y >= 680) holds only ground: the circle may stay; the frame read decides.
- Source line top-left: "NOAA National Hurricane Center".

## 4. Must be true in the picture
1. Band edges at x 821.9 ±3 (June 1) and 1619.7 ±3 (Nov 30); peak at x 1264.7 ±3 (Sept 10). All three from the script.
2. No year on screen.
3. Peak marker lies inside the band.
4. No storm counts on the curve (none sourced).

## 5. Text and cues (a6-s8.words.json, 10.675 s; host starts at "The" 3.44)
Comp-local = word time − 3.44. Frame 0: axis and month labels drawn.
- 3.44: source line in.
- 4.22 ("hurricane") : C1 eyebrow in.
- 5.12 ("opens") /* JUNE 1 @5.82 */: band grows from the June 1 edge 5.12 to 6.80 (power2.out); C1 main line in at 5.82 ("1st").
- 7.02 ("2027.") : band edge pulses once.
- 8.52 ("peak") /* PEAK @8.52 */: peak marker rises from the axis 8.52 to 9.10; curve (if kept) draws 8.52 to 9.40.
- 9.68 ("10th") /* SEPT 10 @9.68 */: C2 in.
- Host end 10.675 + land time 1.0 s (the chapter's last beat before the close card).

## Fallback (no seawall footage: g-a6-10 dropped)
Host starts at 0.00: the "OVER 10 MILES · TODAY" chip of g-a6-10 §3 (eyebrow kept: on a designed ground it names the subject, not a picture) sits centred, top 260, 0.12 to 3.20 (cues g-a6-10 §5), slides out, then the cues above.

## Motion for the whole window
A soft scan line `#7fb2e5` opacity 0.25 sweeps along the axis left to right at 200 px/s, finite repeats; chips float.

## Exit
Cut to the close card g-a6-12: root fades to 0 over the last 0.4 s.

## Footage under it
None: full-frame designed.
