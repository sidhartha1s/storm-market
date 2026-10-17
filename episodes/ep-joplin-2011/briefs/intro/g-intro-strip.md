# BRIEF · g-intro-strip · "a test most Mondays; for a real storm, about once a year" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, segments I1-S2, I1-S3 and I1-S4. Full-frame MG on the channel ground. One host from i1-s2 0.00 to the i1-s4
wav end 6.96 (comp-local times for i1-s3 and i1-s4 = their `nx-` data-start − host data-start + word time). It comes in on a cut from
`g-intro-nobasement` and cuts to `g-intro-page-sirens`.
Bases: MASTER MAP (`g-intro-map` BASEMAP block, copied verbatim; its siren layer is revealed here for the first time) and SIREN STRIP
(the px table in `briefs/a1/g-a1-strip-sirens.md` §2 and §3, used unchanged; this comp is that table's first use on screen, so the
a1 strip comps match whatever is built here). Same Opus builder as `g-intro-map`. Exemplar: `library/inhouse/stat-timeline.html`.
Open: `_list.md` Open 1 (no 23/1/1 split drawn), Open 2 (icon positions from NIST Fig. 4-2; if the figure is not supplied, stop and report), Open 5 (warnings undated).

## 0. What this graphic claims
The 25 sirens (S2) were tested most Monday mornings, 10 a.m., one minute (S5). Outside that test they sounded for a real storm
about once a year at most since 2007 (S2, S4): 18 Jan 2007, 10 May 2008, 8 May 2009, then nothing until 22 May 2011 (S6, S7).
The emergency manager did not sound them for every tornado warning (S8): the 12 warnings of the five years before the storm (S13)
are a separate set, never paired with the siren marks.

## 1. SOURCE
- S2 "Since 2007, the average rate of activation of the 25-siren outdoor warning system in Joplin was once per year (at most), not including the test activations (1 minute in duration) that occurred weekly." NIST Finding 31.
- S5 "tested on a weekly basis in Joplin, weather permitting, at 10 a.m. on Mondays ... for a period of 1 min". NIST Sec. 4.3.1.
- S4 "according to the Joplin-Jasper County emergency manager, the average has been once per year (at most) since 2007." NIST Sec. 4.3.4.
- S6 "(on January 18, 2007) ... (on May 10, 2008)"; S7 "in 2009, the sirens sounded on May 8 ... The next time ... was on May 22, 2011." NIST Sec. 4.3.4.
- S8 "the emergency manager for Joplin was not sounding the sirens for every tornado warning". NIST Sec. 4.3.4.
- S13 "Of these 12 warnings, only 1 (May 10, 2008) was verified" (the five years before 22 May 2011). NIST Sec. 4.3.4. Only the count is drawn.
- Per the S9 CONFLICT, no label calls the soundings wind events.

## 2. DATUM, SCALE, ORIENTATION
- SIREN STRIP table (a1 §2, §3), quoted: axis 1 Jan 2007 at x 200 to 1 Jun 2011 at x 1720, 0.9429 px/day; band y 380 to 420, axis y 440,
  year labels baseline 482, mark labels baseline 300, row label baseline 214 (all at offset 0).
- I1-S2 offset: the strip group sits at y + 440 (computed: row label 654, band 820 to 860, axis 880, year labels 922).
- I1-S3 and I1-S4: offset 0, the same layout `g-a1-strip-warnings` opens on.
- Map in I1-S2: the base framing scaled 0.70 about (850, 200) (computed: map box x 395 to 1305, y 200 to 599), so it clears the row label at 654.
- Warnings row (I1-S4): the `g-a1-strip-warnings` recount pitch, mark i (0 to 11) left = 200 + 64·i, 40 px wide, band y 670 to 740.
- Presenter circle: may stay on; nothing enters x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- Map (I1-S2 only): base layers grid, city, streets, path (drawn, as I1-S1 left it) on; `-l-sirens` revealed here. Icons counter-scaled
  so each is 28 px tall on screen at the 0.70 framing.
- Test ticks: one per Monday, 2 px wide, y 380 to 420 (+offset), `#93a3b2` at 70 %. 53 in 2007 (computed; first x 200.0, last x 543.2),
  229 in all to 16 May 2011 (computed). Positions by script from the a1 rule, never by eye.
- Axis: 2 px `#93a3b2` at 60 %. In I1-S2 it runs x 200 to 544.2 (2007 only) with the year label "2007"; in I1-S3 it extends to 1720 and "2008" to "2011" rise.
- Test label (I1-S2): Arial 700 22 `#93a3b2` tracking 3, left x 580, baseline 848.
- Red marks: 6 px wide, y 356 to 444, `#e74c3c`, at x 216.0, 666.7, 1009.0, 1710.6 (a1 table). Date labels Arial 700 30 `#f2f5f8`
  on baseline 300, left-aligned on the mark x; the 2011 label right-aligned ending x 1730. Dates only, no cause line.
- Gap bracket: 3 px dashed (10/8) `#e74c3c` at 70 %, y 366, x 1017.0 to 1702.6 (a1 table).
- Row label: "Joplin's outdoor sirens", Arial 700 26 `#93a3b2` tracking 8, left x 200, baseline 214 (+offset).
- Name card (I1-S4): glass card x 1000 to 1600, y 500 to 600; "Joplin-Jasper County" Arial Black 900 34 `#f2f5f8`, then "Emergency manager"
  Georgia italic 26 `#e8c56a`.
- Warnings row (I1-S4): 12 marks, 3 px stroke Amber 1 `#d8a13a`, fill `#d8a13a` at 30 % (neither a1's hollow "unverified" nor its
  filled "verified": no outcome is claimed here). Row label "Tornado warnings · the 5 years before May 22, 2011", Arial 700 26 `#d8a13a`
  tracking 4, left x 200, baseline 640, right end ≤ 990. No year axis under the row.
- Chip zone top centre y 96 to 166 (used only once the map has left). Source line x 96, baseline 1010.

## 4. MUST BE TRUE IN THE PICTURE
1. 25 siren icons appear at once, all inside the frame, at their Fig. 4-2 places (S2); no text gives a split of the 25.
2. The I1-S2 strip shows exactly 53 ticks (2007 only); after the stretch there are exactly 229, 6.6 px ±0.3 apart, none after the 2011 mark.
3. Four red marks at their dates: the 2008 to 2009 gap and the 2009 to 2011 gap are in a ratio of 0.49 ±0.02; the first three land together, the 2011 mark later, alone.
4. No label calls the soundings wind events.
5. The warnings row has 12 marks, no dates and no year axis; it never reads as one mark per siren sounding.
6. The map never overlaps the strip (map bottom ≤ 610); the name card overlaps neither row label.
7. One chip at a time; no text rides a move (the test label is gone before the strip rises).

## 5. PANEL TEXT (exact) and CUES
| element | text | cue |
|---|---|---|
| map at the base framing, path drawn, drifting | | i1-s2 frame 0 |
| 25 siren icons pop in together (scale 0 → 1, 0.3 s, back.out) | | i1-s2 "sirens?" 4.06 |
| map scales to 0.70 about (850, 200), 0.6 s, power2.inOut | | i1-s2 "most" 5.82 |
| strip slides up from +300 px into the +440 offset (0.6 s, power3.out); axis 2007 draws; 53 ticks reveal left to right by 6.90 | "Joplin's outdoor sirens" · "2007" | i1-s2 "Monday" 6.08 |
| test label | "Test · 10 AM · 1 minute · weather permitting" (S5) | i1-s2 "mornings," 6.42 |
| all icons pulse once (scale 1 → 1.25 → 1, 0.5 s, stagger 0.02) | | i1-s2 "25" 8.20 |
| source line | "25 sirens in Joplin's outdoor system · NIST Finding 31" (S2) | i1-s2 "25" 8.20 |
| hold: map drift scale +1 %, icons bob ±2 px | | to the i1-s2 end |
| test label out (0.2 s); map exits up (y −800, 0.6 s, power3.in); strip rises +440 → 0 (0.7 s, power3.out) | | i1-s3 "Outside" 0.00 |
| axis extends to 1720; ticks 2008 to May 2011 reveal left to right; "2008" to "2011" rise | | i1-s3 0.30 to "test," 1.12 |
| chip | "ABOUT ONCE A YEAR" (S2, S4) | i1-s3 "about" 2.16 |
| three red marks (scaleY 0 → 1 from the baseline, 0.35 s, back.out) + date labels 0.15 s after | "Jan 18, 2007" · "May 10, 2008" · "May 8, 2009" (S6, S7) | i1-s3 "once" 2.24 |
| source line swaps | "Once a year at most since 2007 · NIST Finding 31 and Sec. 4.3.4, from the county emergency manager" (S2, S4) | i1-s3 "once" 2.24 |
| gap bracket draws left to right (0.5 s) | | i1-s3 "if" 3.28 |
| 2011 mark + label | "May 22, 2011" (S7) | i1-s3 3.60 (after "that." 3.32) |
| chip out (0.3 s) | | i1-s4 "Why'd" 0.00 |
| marks pulse once (scale 1 → 1.18 → 1, 0.5 s) | | i1-s4 "rarely?" 1.54 |
| name card in (x +80 → 0, 0.5 s, power3.out) | "Joplin-Jasper County" / "Emergency manager" (S4) | i1-s4 "emergency" 3.54 |
| warnings row: 12 marks rise, stagger 0.04 s | | i1-s4 "every" 5.44 |
| warnings row label | "Tornado warnings · the 5 years before May 22, 2011" (S13) | i1-s4 "tornado" 5.66 |
| source line swaps | "Not every warning got a siren · NIST Sec. 4.3.4" (S8) | i1-s4 "warning." 6.00 |
| hold | | to 6.96: both rows float 3 px; cut on the host end |
Longest gap between moves: under 4 s (the i1-s2 hold carries drift and bob).

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (item 6: tick counts, mark x values, offsets and the map scale computed by script and stated), §8.
