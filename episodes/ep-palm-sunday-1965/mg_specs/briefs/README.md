# mg_specs/briefs: builder briefs for the acts, waves 1 and 2 (ep-palm-sunday-1965)

One brief per composition, on `references/mg-brief-template.md`. Plan and rules: `mg_specs/acts-plan.md`. Look: `mg_specs/00-design-sheet.md`. Times: `mg_specs/timeline-map.md`.

How to read the times in every brief:
- A cue is segment id, word index, the word, the word's time in `audio/<seg>.words.json`, and seconds from the composition's own start. Seconds from the start = the segment's "wav start inside the composition" (timeline-map.md table 5) plus the word's time; a segment's first word uses table 5's first sound.
- Durations are timeline-map.md table 1 (wavs plus gaps). They do not move when Paul's clips are retimed. A `start=` on a Host line is the map's value when the brief was written and does move: the mount in `index.html` wins.
- Checked 12 Oct 26, 19:18: 24 briefs, every template heading present, every cue row matches the words.json and table 5 on disk within 0.02 s, every `media/` path named exists.

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
