# mg_specs/briefs: builder briefs for the acts, waves 1 to 5 (ep-palm-sunday-1965)

One brief per composition, on `references/mg-brief-template.md`. Plan and rules: `mg_specs/acts-plan.md`. Look: `mg_specs/00-design-sheet.md`. Times: `mg_specs/timeline-map.md`.

How to read the times in every brief:
- A cue is segment id, word index, the word, the word's time in `audio/<seg>.words.json`, and seconds from the composition's own start. Seconds from the start = the segment's "wav start inside the composition" (timeline-map.md table 5) plus the word's time; a segment's first word uses table 5's first sound.
- Durations are timeline-map.md table 1 (wavs plus gaps). They do not move when Paul's clips are retimed. A `start=` on a Host line is the map's value when the brief was written and does move: the mount in `index.html` wins.
- One form per string, by the lead's rulings of 12 Oct 26 after the fact pass (`research/fc-briefs.md`): the survey's source line is `Weather Bureau survey report, 1965, p. N`; photograph A3's caption is `Weather Bureau Communications Center, about 1955`; no county label is on screen other than those a Picture note names (`HOWARD` is struck from g-a5s07-marion).
- Zones, for the record, not a contradiction to fix: the clock stamps read `Eastern time` by the lead's ruling; the script's card and the page crops read EST because that is what the paper says.
- The presenter corner, for every brief: nothing travels through x >= 1600, y >= 680, entrances and exits included.
- A card, page or strip that reaches y 680 or lower never enters or leaves by the right edge: it rises in from below with a fade (`y:80` to 0, opacity 0 to 1) and leaves the way it came (`y:0` to 60, opacity 1 to 0), same cues and durations.
- Strip type (lead, 12 Oct 26): a quote strip is Georgia 52 px with a 26 px attribution wherever the text fits with 48 px or more to the strip's edge. Smaller type stays only where the text does not fit.
- Labels and lines: no painted line runs through a label's ink. Move the label 8 px or more clear; where no place exists, give it a hard 4 px halo in the ground colour. A line beside a label is accepted.
- Never force `visibility: visible`; use `autoAlpha`, or `visibility: "inherit"` where the element holds a partial opacity. A forced-visible band of g-a4s13-duty painted through the sirens film window after its host was hidden; four built files had it and are fixed.
- The table below is in build order (acts-plan.md section 5). Segments and durations are timeline-map.md table 1 as retimed 12 Oct 26, 19:13.
- Checked 12 Oct 26, 21:54, by script against the files on disk: 69 briefs for the 69 rows of table 1; 66 Host lines parse and their durations match table 1 (the three wave 1 briefs `g-a1s01-kc.md`, `g-a1s05-clocks.md` and `g-a2s17-funnels.md` write `start=(timeline-map.md)` and were not read by the script); 660 cue rows match words.json and table 5 within 0.02 s; every template heading is present in the 66. Three wave 1 Host lines still carry the start from before the 19:13 retime, 0.25 s early (`g-a1s15-offices.md`, `g-a2s06-headstart.md`, `g-a2s14-six.md`). One `media/` path named is not on disk yet: `media/stills/z1-book-cover.png`, which the builder of g-z1s4b-book stages.

| Brief | Composition | Wave | Family | Segments | Duration (s) |
|---|---|---|---|---|---|
| `g-a2s14-six.md` | g-a2s14-six | 1 | map (base) | A2-S14 | 10.39 |
| `g-a1s02-strip.md` | g-a1s02-strip | 1 | map (base) | A1-S2, A1-S3 | 20.56 |
| `g-a4s02-countyb.md` | g-a4s02-countyb | 1 | chain (base) | A4-S2, A4-S3, A4-S4, A4-S5 | 32.43 |
| `g-a1s13-chain.md` | g-a1s13-chain | 1 | chain (base) | A1-S13 | 5.75 |
| `g-a1s15-offices.md` | g-a1s15-offices | 1 | film window (base) | A1-S15, A1-S16, A1-S17 | 34.71 |
| `g-a2s17-funnels.md` | g-a2s17-funnels | 1 | photograph (base) | A2-S17, A2-S18 | 18.96 |
| `g-a1s01-kc.md` | g-a1s01-kc | 1 | photograph (base) | A1-S1 | 9.75 |
| `g-a2s06-headstart.md` | g-a2s06-headstart | 1 | clock (base) | A2-S6, A2-S7 | 17.66 |
| `g-a1s05-clocks.md` | g-a1s05-clocks | 1 | clock (base) | A1-S5 | 9.13 |
| `g-a1s06-low.md` | g-a1s06-low | 2 | map | A1-S6 | 7.51 |
| `g-a1s09-forecasts.md` | g-a1s09-forecasts | 2 | map | A1-S9, A1-S10, A1-S11, A1-S12 | 31.20 |
| `g-a2s01-radar.md` | g-a2s01-radar | 2 | map | A2-S1, A2-S2 | 16.69 |
| `g-a2s08-first.md` | g-a2s08-first | 2 | map | A2-S8 | 6.69 |
| `g-a2s16-huffman.md` | g-a2s16-huffman | 2 | map | A2-S16 | 15.43 |
| `g-a2s19-log.md` | g-a2s19-log | 2 | map | A2-S19 | 12.55 |
| `g-a2s03-chain.md` | g-a2s03-chain | 2 | chain, film window | A2-S3, A2-S4, A2-S5 | 21.92 |
| `g-a2s09-countya.md` | g-a2s09-countya | 2 | chain | A2-S9, A2-S10 | 18.79 |
| `g-a2s20-front.md` | g-a2s20-front | 2 | chain | A2-S20 | 8.07 |
| `g-a1s04-wire.md` | g-a1s04-wire | 2 | photograph | A1-S4 | 9.94 |
| `g-a1s07-tracks.md` | g-a1s07-tracks | 2 | photograph | A1-S7, A1-S8 | 26.08 |
| `g-a2s15-old.md` | g-a2s15-old | 2 | page | A2-S15 | 10.91 |
| `g-a1s18-list.md` | g-a1s18-list | 2 | list on photograph | A1-S18, A1-S19 | 11.68 |
| `g-a2s21-list.md` | g-a2s21-list | 2 | list on photograph | A2-S21 | 9.09 |
| `g-a2s11-backup.md` | g-a2s11-backup | 2 | house and chain | A2-S11, A2-S12, A2-S13 | 22.96 |
| `g-a3s05-bremen.md` | g-a3s05-bremen | 3 | map | A3-S5, A3-S6 | 19.92 |
| `g-a4s16-fortwayne.md` | g-a4s16-fortwayne | 3 | map | A4-S16 | 10.31 |
| `g-a3s04-links.md` | g-a3s04-links | 3 | chain | A3-S4 | 9.07 |
| `g-a3s15-desks.md` | g-a3s15-desks | 3 | chain | A3-S15, A3-S16, A3-S17 | 17.34 |
| `g-a4s06-died.md` | g-a4s06-died | 3 | page over the County B chain | A4-S6 | 5.16 |
| `g-a4s09-clock.md` | g-a4s09-clock | 3 | county chain | A4-S9, A4-S10 | 21.86 |
| `g-a4s11-farend.md` | g-a4s11-farend | 3 | county chain | A4-S11, A4-S12 | 22.43 |
| `g-a4s13-duty.md` | g-a4s13-duty | 3 | list | A4-S13 | 13.98 |
| `g-a4s15-chain.md` | g-a4s15-chain | 3 | chain | A4-S15 | 9.92 |
| `g-a3s10-towers.md` | g-a3s10-towers | 3 | list | A3-S10 | 11.47 |
| `g-a3s07-calls.md` | g-a3s07-calls | 3 | film window | A3-S7, A3-S8 | 17.24 |
| `g-a3s01-message.md` | g-a3s01-message | 3 | page | A3-S1, A3-S2, A3-S3 | 18.73 |
| `g-a4s01-eyes.md` | g-a4s01-eyes | 3 | page | A4-S1 | 6.71 |
| `g-a4s08-chief.md` | g-a4s08-chief | 3 | page | A4-S8 | 11.18 |
| `g-a3s09-jam.md` | g-a3s09-jam | 3 | drawing | A3-S9 | 10.26 |
| `g-a3s11-onoff.md` | g-a3s11-onoff | 3 | drawing | A3-S11 | 12.69 |
| `g-a3s12-seven.md` | g-a3s12-seven | 3 | clock | A3-S12 | 7.59 |
| `g-a3s13-battery.md` | g-a3s13-battery | 3 | living room | A3-S13, A3-S14 | 21.23 |
| `g-a4s14-eight.md` | g-a4s14-eight | 3 | drawing | A4-S14 | 8.48 |
| `g-a5s01-radar.md` | g-a5s01-radar | 4 | map | A5-S1, A5-S2, A5-S3 | 31.67 |
| `g-a5s04-berne.md` | g-a5s04-berne | 4 | map | A5-S4, A5-S5 | 18.70 |
| `g-a5s07-marion.md` | g-a5s07-marion | 4 | map | A5-S7, A5-S8 | 19.90 |
| `g-a5s10-alert.md` | g-a5s10-alert | 4 | map, film window | A5-S10, A5-S11 | 17.99 |
| `g-a5s16-toledo.md` | g-a5s16-toledo | 4 | map | A5-S16, A5-S17 | 19.27 |
| `g-a5s06-hold.md` | g-a5s06-hold | 4 | photograph | A5-S6 | 15.98 |
| `g-a5s09-alto.md` | g-a5s09-alto | 4 | photograph | A5-S9 | 5.99 |
| `g-a5s14-noissue.md` | g-a5s14-noissue | 4 | page (tempo 0.85) | A5-S14 | 6.15 |
| `g-a5s20-team.md` | g-a5s20-team | 4 | page | A5-S20 | 9.19 |
| `g-a5s15-dark.md` | g-a5s15-dark | 4 | drawing | A5-S15 | 7.71 |
| `g-a5s18-curran.md` | g-a5s18-curran | 4 | drawing | A5-S18, A5-S19 | 20.33 |
| `g-a5s12-spotters.md` | g-a5s12-spotters | 4 | chain | A5-S12 | 8.02 |
| `g-a5s21-end.md` | g-a5s21-end | 4 | list | A5-S21 | 2.62 |
| `g-a6s01-recs.md` | g-a6s01-recs | 5 | page | A6-S1 | 7.92 |
| `g-a6s02-floorplan.md` | g-a6s02-floorplan | 5 | drawing (plan) | A6-S2 | 10.15 |
| `g-a6s03-announcer.md` | g-a6s03-announcer | 5 | list | A6-S3, A6-S4 | 17.47 |
| `g-a6s10-watch.md` | g-a6s10-watch | 5 | drawing | A6-S10 | 13.79 |
| `g-z1s02-row.md` | g-z1s02-row | 5 | list and chain | Z1-S2, Z1-S3 | 20.39 |
| `g-a6s05-wires.md` | g-a6s05-wires | 5 | chain | A6-S5, A6-S6 | 16.94 |
| `g-a6s08-spotters.md` | g-a6s08-spotters | 5 | chain | A6-S8 | 12.71 |
| `g-a6s07-power.md` | g-a6s07-power | 5 | drawing, then map | A6-S7 | 12.44 |
| `g-a6s09-third.md` | g-a6s09-third | 5 | drawing | A6-S9 | 9.47 |
| `g-z1s04-drill.md` | g-z1s04-drill | 5 | map | Z1-S4 | 7.10 |
| `g-a6s11-sirens.md` | g-a6s11-sirens | 5 | film window | A6-S11, A6-S12 | 16.25 |
| `g-z1s05-title.md` | g-z1s05-title | 5 | close card | Z1-S5 | 15.23 |
| `g-z1s4b-book.md` | g-z1s4b-book | 5 | card on the channel ground (added 12 Oct 26) | Z1-S4b | 6.31 |
