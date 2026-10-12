# mg_specs/timeline-map.md: where every act composition sits on the timeline (ep-palm-sunday-1965)

Read from `index.html` on 12 Oct 26 by a read-only script, after the mounts were typed by hand. `index.html` is the source: if a number here and a mount disagree, the mount wins and this file is corrected. Composition names are the ones in `acts-plan.md` section 2 and are never changed. Total length 1174.18 s. All times in seconds.

How the times were set (the hook and intro's own rules, nothing added):
- Wav lengths are `ffprobe` on `audio/*.wav`. First and last sound of each wav are a silence scan (`silencedetect`, -35 dB, 0.15 s); `words.json` writes 0.00 for a first word, so a first word is timed from the scan and every other word from `words.json`.
- 1.0 s from the last sound of one composition's voice to the first sound of the next composition's; 0.8 s between segments inside one composition; wavs never under 0.05 s or over 0.75 s apart.
- A composition starts on the first sound of its first segment and ends where the next picture starts. After black or after a Paul clip it starts on the cut instead, and the voice follows (first sound in table 5).
- Act seam: the last composition ends 1.0 s after its last sound, then 0.7 s of black, and the next act's first sound lands on the cut out of black.
- **A cue inside a composition** = the segment's "wav start inside the composition" (table 5) + the word's time in `audio/<seg>.words.json`. For a segment's first word use the "first sound" column.
- **Paul's five clips are placeholders** (the narrator wav's length). When a real clip lands, its slot is retimed and every later start in this file moves by the difference. Durations of compositions do not change, except that nothing else moves inside them.

## 1. Compositions (68)
| Composition | File | Segments | Start (s) | Duration (s) | End (s) |
|---|---|---|---|---|---|
| g-a1s01-kc | compositions/g-a1s01-kc.html | A1-S1 | 113.18 | 9.75 | 122.93 |
| g-a1s02-strip | compositions/g-a1s02-strip.html | A1-S2, A1-S3 | 122.93 | 20.56 | 143.49 |
| g-a1s04-wire | compositions/g-a1s04-wire.html | A1-S4 | 143.49 | 9.94 | 153.43 |
| g-a1s05-clocks | compositions/g-a1s05-clocks.html | A1-S5 | 153.43 | 9.13 | 162.56 |
| g-a1s06-low | compositions/g-a1s06-low.html | A1-S6 | 162.56 | 7.51 | 170.07 |
| g-a1s07-tracks | compositions/g-a1s07-tracks.html | A1-S7, A1-S8 | 170.07 | 26.08 | 196.15 |
| g-a1s09-forecasts | compositions/g-a1s09-forecasts.html | A1-S9, A1-S10, A1-S11, A1-S12 | 196.15 | 31.20 | 227.35 |
| g-a1s13-chain | compositions/g-a1s13-chain.html | A1-S13 | 227.35 | 5.75 | 233.10 |
| g-a1s15-offices | compositions/g-a1s15-offices.html | A1-S15, A1-S16, A1-S17 | 242.52 | 34.71 | 277.23 |
| g-a1s18-list | compositions/g-a1s18-list.html | A1-S18, A1-S19 | 277.23 | 11.68 | 288.91 |
| g-a2s01-radar | compositions/g-a2s01-radar.html | A2-S1, A2-S2 | 289.61 | 16.69 | 306.30 |
| g-a2s03-chain | compositions/g-a2s03-chain.html | A2-S3, A2-S4, A2-S5 | 306.30 | 21.92 | 328.22 |
| g-a2s06-headstart | compositions/g-a2s06-headstart.html | A2-S6, A2-S7 | 328.22 | 17.66 | 345.88 |
| g-a2s08-first | compositions/g-a2s08-first.html | A2-S8 | 345.88 | 6.69 | 352.57 |
| g-a2s09-countya | compositions/g-a2s09-countya.html | A2-S9, A2-S10 | 352.57 | 18.79 | 371.36 |
| g-a2s11-backup | compositions/g-a2s11-backup.html | A2-S11, A2-S12, A2-S13 | 371.36 | 22.96 | 394.32 |
| g-a2s14-six | compositions/g-a2s14-six.html | A2-S14 | 394.32 | 10.39 | 404.71 |
| g-a2s15-old | compositions/g-a2s15-old.html | A2-S15 | 404.71 | 10.91 | 415.62 |
| g-a2s16-huffman | compositions/g-a2s16-huffman.html | A2-S16 | 415.62 | 15.43 | 431.05 |
| g-a2s17-funnels | compositions/g-a2s17-funnels.html | A2-S17, A2-S18 | 431.05 | 18.96 | 450.01 |
| g-a2s19-log | compositions/g-a2s19-log.html | A2-S19 | 450.01 | 12.55 | 462.56 |
| g-a2s20-front | compositions/g-a2s20-front.html | A2-S20 | 462.56 | 8.07 | 470.63 |
| g-a2s21-list | compositions/g-a2s21-list.html | A2-S21 | 470.63 | 9.09 | 479.72 |
| g-a3s01-message | compositions/g-a3s01-message.html | A3-S1, A3-S2, A3-S3 | 480.42 | 18.73 | 499.15 |
| g-a3s04-links | compositions/g-a3s04-links.html | A3-S4 | 499.15 | 9.07 | 508.22 |
| g-a3s05-bremen | compositions/g-a3s05-bremen.html | A3-S5, A3-S6 | 508.22 | 19.92 | 528.14 |
| g-a3s07-calls | compositions/g-a3s07-calls.html | A3-S7, A3-S8 | 528.14 | 17.24 | 545.38 |
| g-a3s09-jam | compositions/g-a3s09-jam.html | A3-S9 | 545.38 | 10.26 | 555.64 |
| g-a3s10-towers | compositions/g-a3s10-towers.html | A3-S10 | 555.64 | 11.47 | 567.11 |
| g-a3s11-onoff | compositions/g-a3s11-onoff.html | A3-S11 | 567.11 | 12.69 | 579.80 |
| g-a3s12-seven | compositions/g-a3s12-seven.html | A3-S12 | 579.80 | 7.59 | 587.39 |
| g-a3s13-battery | compositions/g-a3s13-battery.html | A3-S13, A3-S14 | 587.39 | 21.23 | 608.62 |
| g-a3s15-desks | compositions/g-a3s15-desks.html | A3-S15, A3-S16, A3-S17 | 608.62 | 17.34 | 625.96 |
| g-a4s01-eyes | compositions/g-a4s01-eyes.html | A4-S1 | 662.18 | 6.71 | 668.89 |
| g-a4s02-countyb | compositions/g-a4s02-countyb.html | A4-S2, A4-S3, A4-S4, A4-S5 | 668.89 | 32.43 | 701.32 |
| g-a4s06-died | compositions/g-a4s06-died.html | A4-S6 | 701.32 | 5.16 | 706.48 |
| g-a4s08-chief | compositions/g-a4s08-chief.html | A4-S8 | 716.29 | 11.18 | 727.47 |
| g-a4s09-clock | compositions/g-a4s09-clock.html | A4-S9, A4-S10 | 727.47 | 21.86 | 749.33 |
| g-a4s11-farend | compositions/g-a4s11-farend.html | A4-S11, A4-S12 | 749.33 | 22.43 | 771.76 |
| g-a4s13-duty | compositions/g-a4s13-duty.html | A4-S13 | 771.76 | 13.98 | 785.74 |
| g-a4s14-eight | compositions/g-a4s14-eight.html | A4-S14 | 785.74 | 8.48 | 794.22 |
| g-a4s15-chain | compositions/g-a4s15-chain.html | A4-S15 | 794.22 | 9.92 | 804.14 |
| g-a4s16-fortwayne | compositions/g-a4s16-fortwayne.html | A4-S16 | 804.14 | 10.31 | 814.45 |
| g-a5s01-radar | compositions/g-a5s01-radar.html | A5-S1, A5-S2, A5-S3 | 815.15 | 31.67 | 846.82 |
| g-a5s04-berne | compositions/g-a5s04-berne.html | A5-S4, A5-S5 | 846.82 | 18.70 | 865.52 |
| g-a5s06-hold | compositions/g-a5s06-hold.html | A5-S6 | 865.52 | 15.98 | 881.50 |
| g-a5s07-marion | compositions/g-a5s07-marion.html | A5-S7, A5-S8 | 881.50 | 19.90 | 901.40 |
| g-a5s09-alto | compositions/g-a5s09-alto.html | A5-S9 | 901.40 | 5.99 | 907.39 |
| g-a5s10-alert | compositions/g-a5s10-alert.html | A5-S10, A5-S11 | 907.39 | 17.99 | 925.38 |
| g-a5s12-spotters | compositions/g-a5s12-spotters.html | A5-S12 | 925.38 | 8.02 | 933.40 |
| g-a5s14-noissue | compositions/g-a5s14-noissue.html | A5-S14 | 941.46 | 6.15 | 947.61 |
| g-a5s15-dark | compositions/g-a5s15-dark.html | A5-S15 | 947.61 | 7.71 | 955.32 |
| g-a5s16-toledo | compositions/g-a5s16-toledo.html | A5-S16, A5-S17 | 955.32 | 19.27 | 974.59 |
| g-a5s18-curran | compositions/g-a5s18-curran.html | A5-S18, A5-S19 | 974.59 | 20.33 | 994.92 |
| g-a5s20-team | compositions/g-a5s20-team.html | A5-S20 | 994.92 | 9.19 | 1004.11 |
| g-a5s21-end | compositions/g-a5s21-end.html | A5-S21 | 1004.11 | 2.62 | 1006.73 |
| g-a6s01-recs | compositions/g-a6s01-recs.html | A6-S1 | 1007.43 | 7.92 | 1015.35 |
| g-a6s02-floorplan | compositions/g-a6s02-floorplan.html | A6-S2 | 1015.35 | 10.15 | 1025.50 |
| g-a6s03-announcer | compositions/g-a6s03-announcer.html | A6-S3, A6-S4 | 1025.50 | 17.47 | 1042.97 |
| g-a6s05-wires | compositions/g-a6s05-wires.html | A6-S5, A6-S6 | 1042.97 | 16.94 | 1059.91 |
| g-a6s07-power | compositions/g-a6s07-power.html | A6-S7 | 1059.91 | 12.44 | 1072.35 |
| g-a6s08-spotters | compositions/g-a6s08-spotters.html | A6-S8 | 1072.35 | 12.71 | 1085.06 |
| g-a6s09-third | compositions/g-a6s09-third.html | A6-S9 | 1085.06 | 9.47 | 1094.53 |
| g-a6s10-watch | compositions/g-a6s10-watch.html | A6-S10 | 1094.53 | 13.79 | 1108.32 |
| g-a6s11-sirens | compositions/g-a6s11-sirens.html | A6-S11, A6-S12 | 1108.32 | 16.25 | 1124.57 |
| g-z1s02-row | compositions/g-z1s02-row.html | Z1-S2, Z1-S3 | 1134.52 | 20.39 | 1154.91 |
| g-z1s04-drill | compositions/g-z1s04-drill.html | Z1-S4 | 1154.91 | 7.05 | 1161.96 |
| g-z1s05-title | compositions/g-z1s05-title.html | Z1-S5 | 1161.96 | 12.22 | 1174.18 |

Every host is `id="host-<name without g->"`, track 2, 1920 x 1080.

## 2. Paul's clips (5), retime on arrival
| Paul clip | File | Segment | Start (s) | Placeholder duration (s) | End (s) | Status |
|---|---|---|---|---|---|---|
| ins-paul-2 | media/paul/ins-paul-2/ins-paul-2.mp4 | A1-S14 | 233.10 | 9.42 | 242.52 | retime on arrival |
| ins-paul-3 | media/paul/ins-paul-3/ins-paul-3.mp4 | A3-S18 | 625.96 | 9.81 | 635.77 | retime on arrival |
| ins-paul-4 | media/paul/ins-paul-4/ins-paul-4.mp4 | A4-S7 | 706.48 | 9.81 | 716.29 | retime on arrival |
| ins-paul-5 | media/paul/ins-paul-5/ins-paul-5.mp4 | A5-S13 | 933.40 | 8.06 | 941.46 | retime on arrival |
| ins-paul-6 | media/paul/ins-paul-6/ins-paul-6.mp4 | Z1-S1 | 1125.27 | 9.25 | 1134.52 | retime on arrival |

Track 1, own sound, no narration under them; the narrator wavs of these five segments are not mounted. Each clip is cut on his last sound, as `ins-paul-1` was. The chip "County B" over `ins-paul-4` is the overlay `ov-chip-countyb` in `index.html` (same window as the clip).

## 3. Film cuts under compositions (6 mounts)
Track 1, muted, class `filmwin`: left 480, top 150, 960 x 720 (the 4:3 window of `acts-plan.md` rule 15). The composition above draws the ground, the frame and the label, leaves the window open while the film shows, and covers it when the script says the window goes. A mount runs longer than the window needs so the composition, not the mount, decides the cut. No builder mounts a film.
| Film mount | File | Under composition | Start (s) | Duration (s) | Start inside the composition (s) |
|---|---|---|---|---|---|
| v-a1s15-room | media/films/cuts/a14-05-operations-room.mp4 | g-a1s15-offices | 242.52 | 12.99 | 0.00 |
| v-a1s16-announcer | media/films/cuts/a14-09-announcer.mp4 | g-a1s15-offices | 255.51 | 9.44 | 12.99 |
| v-a2s4-operators | media/films/cuts/a14-13-operators.mp4 | g-a2s03-chain | 312.44 | 7.84 | 6.14 |
| v-a3s7-telephone | media/films/cuts/a14-10-desk-telephone.mp4 | g-a3s07-calls | 528.14 | 11.41 | 0.00 |
| v-a5s11-call | media/films/cuts/a14-08-telephone-call.mp4 | g-a5s10-alert | 916.22 | 4.17 | 8.83 |
| v-a6s12-horn | media/films/cuts/a14-01-siren-horn.mp4 | g-a6s11-sirens | 1113.67 | 10.90 | 5.35 |

- `v-a1s16-announcer` ends 22.43 s into `g-a1s15-offices`; the window must be covered by then. "A few stations" is spoken at 21.47 s, so the first angle alone is enough and the two extra angle files are not mounted.
- `v-a5s11-call` is the whole 4.17 s file; the first sentence of A5-S11 ends 10.31 s into `g-a5s10-alert`, so the window is open for about 1.5 s.

## 4. Black and the book ad
| Black | Start (s) | Duration (s) | End (s) |
|---|---|---|---|
| bo-i1 (after the intro, approved) | 112.48 | 0.70 | 113.18 |
| bo-a1 | 288.91 | 0.70 | 289.61 |
| bo-a2 | 479.72 | 0.70 | 480.42 |
| bo-cta-in (the ad's dip in) | 635.77 | 1.00 | 636.77 |
| bo-cta-out (the ad's dip out) | 661.18 | 1.00 | 662.18 |
| bo-a4 | 814.45 | 0.70 | 815.15 |
| bo-a5 | 1006.73 | 0.70 | 1007.43 |
| bo-a6 | 1124.57 | 0.70 | 1125.27 |

Book ad `ins-cta-paul` (`media/cta/paul-storm-ready-v7-oct10.mp4`): 636.77 for 24.417 s, 0.5423 of the total, inside the config window 0.40 to 0.60. It follows Paul's tease (A3-S18) and A4-S1 pays the tease on the cut out of the dip. A3 has no chapter blackout of its own.

## 5. Segments inside their compositions (107)
"Wav start inside the composition" can be negative: the wav's silent lead-in starts before the picture does.
| Segment | Composition | Wav start (s) | Wav start inside the composition (s) | First sound inside the composition (s) | Last sound inside the composition (s) |
|---|---|---|---|---|---|
| A1-S1 | g-a1s01-kc | 112.87 | -0.31 | 0.00 | 8.74 |
| A1-S2 | g-a1s02-strip | 122.68 | -0.25 | 0.00 | 8.59 |
| A1-S3 | g-a1s02-strip | 131.96 | 9.03 | 9.39 | 19.56 |
| A1-S4 | g-a1s04-wire | 143.28 | -0.21 | 0.00 | 8.93 |
| A1-S5 | g-a1s05-clocks | 153.03 | -0.40 | 0.00 | 8.13 |
| A1-S6 | g-a1s06-low | 162.07 | -0.49 | 0.00 | 6.50 |
| A1-S7 | g-a1s07-tracks | 169.65 | -0.42 | 0.00 | 11.50 |
| A1-S8 | g-a1s07-tracks | 181.93 | 11.86 | 12.32 | 25.07 |
| A1-S9 | g-a1s09-forecasts | 195.92 | -0.23 | 0.00 | 8.06 |
| A1-S10 | g-a1s09-forecasts | 204.62 | 8.47 | 8.87 | 17.55 |
| A1-S11 | g-a1s09-forecasts | 214.10 | 17.95 | 18.35 | 24.36 |
| A1-S12 | g-a1s09-forecasts | 220.88 | 24.73 | 25.15 | 30.20 |
| A1-S13 | g-a1s13-chain | 227.03 | -0.32 | 0.00 | 4.75 |
| A1-S15 | g-a1s15-offices | 242.67 | 0.15 | 0.47 | 12.19 |
| A1-S16 | g-a1s15-offices | 255.17 | 12.65 | 12.99 | 23.48 |
| A1-S17 | g-a1s15-offices | 266.43 | 23.91 | 24.28 | 33.71 |
| A1-S18 | g-a1s18-list | 276.82 | -0.41 | 0.00 | 7.63 |
| A1-S19 | g-a1s18-list | 285.27 | 8.04 | 8.48 | 10.68 |
| A2-S1 | g-a2s01-radar | 289.19 | -0.42 | 0.00 | 8.26 |
| A2-S2 | g-a2s01-radar | 298.26 | 8.65 | 9.07 | 15.69 |
| A2-S3 | g-a2s03-chain | 306.02 | -0.28 | 0.00 | 5.33 |
| A2-S4 | g-a2s03-chain | 312.15 | 5.85 | 6.14 | 13.19 |
| A2-S5 | g-a2s03-chain | 320.08 | 13.78 | 13.98 | 20.92 |
| A2-S6 | g-a2s06-headstart | 327.75 | -0.47 | 0.00 | 10.90 |
| A2-S7 | g-a2s06-headstart | 339.66 | 11.44 | 11.69 | 16.65 |
| A2-S8 | g-a2s08-first | 345.39 | -0.49 | 0.00 | 5.68 |
| A2-S9 | g-a2s09-countya | 352.26 | -0.31 | 0.00 | 12.39 |
| A2-S10 | g-a2s09-countya | 365.28 | 12.71 | 13.19 | 17.79 |
| A2-S11 | g-a2s11-backup | 371.20 | -0.16 | 0.00 | 7.49 |
| A2-S12 | g-a2s11-backup | 379.34 | 7.98 | 8.30 | 16.38 |
| A2-S13 | g-a2s11-backup | 388.32 | 16.96 | 17.18 | 21.96 |
| A2-S14 | g-a2s14-six | 394.06 | -0.26 | 0.00 | 9.39 |
| A2-S15 | g-a2s15-old | 404.32 | -0.39 | 0.00 | 9.91 |
| A2-S16 | g-a2s16-huffman | 415.33 | -0.29 | 0.00 | 14.42 |
| A2-S17 | g-a2s17-funnels | 430.55 | -0.50 | 0.00 | 12.30 |
| A2-S18 | g-a2s17-funnels | 443.79 | 12.74 | 13.10 | 17.96 |
| A2-S19 | g-a2s19-log | 449.78 | -0.23 | 0.00 | 11.55 |
| A2-S20 | g-a2s20-front | 462.24 | -0.32 | 0.00 | 7.07 |
| A2-S21 | g-a2s21-list | 470.07 | -0.56 | 0.00 | 8.09 |
| A3-S1 | g-a3s01-message | 479.87 | -0.55 | 0.00 | 5.90 |
| A3-S2 | g-a3s01-message | 486.87 | 6.45 | 6.70 | 13.64 |
| A3-S3 | g-a3s01-message | 494.49 | 14.07 | 14.44 | 17.74 |
| A3-S4 | g-a3s04-links | 498.76 | -0.39 | 0.00 | 8.07 |
| A3-S5 | g-a3s05-bremen | 507.75 | -0.47 | 0.00 | 11.18 |
| A3-S6 | g-a3s05-bremen | 519.94 | 11.72 | 11.98 | 18.88 |
| A3-S7 | g-a3s07-calls | 527.63 | -0.51 | 0.00 | 10.61 |
| A3-S8 | g-a3s07-calls | 539.30 | 11.16 | 11.41 | 16.23 |
| A3-S9 | g-a3s09-jam | 544.86 | -0.52 | 0.00 | 9.27 |
| A3-S10 | g-a3s10-towers | 555.26 | -0.38 | 0.00 | 10.47 |
| A3-S11 | g-a3s11-onoff | 566.66 | -0.45 | 0.00 | 11.69 |
| A3-S12 | g-a3s12-seven | 579.55 | -0.25 | 0.00 | 6.59 |
| A3-S13 | g-a3s13-battery | 587.17 | -0.22 | 0.00 | 8.43 |
| A3-S14 | g-a3s13-battery | 596.37 | 8.98 | 9.24 | 20.23 |
| A3-S15 | g-a3s15-desks | 608.27 | -0.35 | 0.00 | 5.60 |
| A3-S16 | g-a3s15-desks | 614.77 | 6.15 | 6.40 | 11.86 |
| A3-S17 | g-a3s15-desks | 621.04 | 12.42 | 12.67 | 16.34 |
| A4-S1 | g-a4s01-eyes | 661.87 | -0.31 | 0.00 | 5.71 |
| A4-S2 | g-a4s02-countyb | 668.49 | -0.40 | 0.00 | 9.26 |
| A4-S3 | g-a4s02-countyb | 678.73 | 9.84 | 10.06 | 13.98 |
| A4-S4 | g-a4s02-countyb | 683.41 | 14.52 | 14.77 | 23.18 |
| A4-S5 | g-a4s02-countyb | 692.46 | 23.57 | 24.14 | 31.43 |
| A4-S6 | g-a4s06-died | 701.05 | -0.27 | 0.00 | 4.17 |
| A4-S8 | g-a4s08-chief | 716.44 | 0.15 | 0.68 | 10.18 |
| A4-S9 | g-a4s09-clock | 726.96 | -0.51 | 0.00 | 7.47 |
| A4-S10 | g-a4s09-clock | 735.33 | 7.86 | 8.35 | 20.86 |
| A4-S11 | g-a4s11-farend | 748.91 | -0.42 | 0.00 | 9.79 |
| A4-S12 | g-a4s11-farend | 759.50 | 10.17 | 10.59 | 21.43 |
| A4-S13 | g-a4s13-duty | 771.31 | -0.45 | 0.00 | 12.97 |
| A4-S14 | g-a4s14-eight | 785.52 | -0.22 | 0.00 | 7.48 |
| A4-S15 | g-a4s15-chain | 793.85 | -0.37 | 0.00 | 8.92 |
| A4-S16 | g-a4s16-fortwayne | 803.93 | -0.21 | 0.00 | 9.31 |
| A5-S1 | g-a5s01-radar | 814.72 | -0.43 | 0.00 | 7.53 |
| A5-S2 | g-a5s01-radar | 823.21 | 8.06 | 8.33 | 18.51 |
| A5-S3 | g-a5s01-radar | 834.13 | 18.98 | 19.48 | 30.67 |
| A5-S4 | g-a5s04-berne | 846.82 | 0.00 | 0.00 | 12.56 |
| A5-S5 | g-a5s04-berne | 859.91 | 13.09 | 13.36 | 17.69 |
| A5-S6 | g-a5s06-hold | 865.09 | -0.43 | 0.00 | 14.99 |
| A5-S7 | g-a5s07-marion | 881.27 | -0.23 | 0.00 | 9.16 |
| A5-S8 | g-a5s07-marion | 891.46 | 9.96 | 9.96 | 18.89 |
| A5-S9 | g-a5s09-alto | 900.91 | -0.49 | 0.00 | 4.98 |
| A5-S10 | g-a5s10-alert | 907.12 | -0.27 | 0.00 | 7.96 |
| A5-S11 | g-a5s10-alert | 915.74 | 8.35 | 8.83 | 16.99 |
| A5-S12 | g-a5s12-spotters | 925.04 | -0.34 | 0.00 | 7.02 |
| A5-S14 | g-a5s14-noissue | 941.61 | 0.15 | 0.57 | 5.15 |
| A5-S15 | g-a5s15-dark | 947.61 | 0.00 | 0.00 | 6.71 |
| A5-S16 | g-a5s16-toledo | 954.88 | -0.44 | 0.00 | 11.92 |
| A5-S17 | g-a5s16-toledo | 967.61 | 12.29 | 12.72 | 18.28 |
| A5-S18 | g-a5s18-curran | 974.59 | 0.00 | 0.00 | 9.26 |
| A5-S19 | g-a5s18-curran | 984.23 | 9.64 | 10.12 | 19.34 |
| A5-S20 | g-a5s20-team | 994.51 | -0.41 | 0.00 | 8.19 |
| A5-S21 | g-a5s21-end | 1003.68 | -0.43 | 0.00 | 1.62 |
| A6-S1 | g-a6s01-recs | 1007.04 | -0.39 | 0.00 | 6.92 |
| A6-S2 | g-a6s02-floorplan | 1014.84 | -0.51 | 0.00 | 9.15 |
| A6-S3 | g-a6s03-announcer | 1025.09 | -0.41 | 0.00 | 7.01 |
| A6-S4 | g-a6s03-announcer | 1032.95 | 7.45 | 7.84 | 16.48 |
| A6-S5 | g-a6s05-wires | 1042.65 | -0.32 | 0.00 | 7.87 |
| A6-S6 | g-a6s05-wires | 1051.23 | 8.26 | 8.67 | 15.94 |
| A6-S7 | g-a6s07-power | 1059.58 | -0.33 | 0.00 | 11.44 |
| A6-S8 | g-a6s08-spotters | 1072.06 | -0.29 | 0.00 | 11.71 |
| A6-S9 | g-a6s09-third | 1084.83 | -0.23 | 0.00 | 8.47 |
| A6-S10 | g-a6s10-watch | 1094.32 | -0.21 | 0.00 | 12.79 |
| A6-S11 | g-a6s11-sirens | 1108.07 | -0.25 | 0.00 | 4.25 |
| A6-S12 | g-a6s11-sirens | 1113.08 | 4.76 | 5.35 | 15.25 |
| Z1-S2 | g-z1s02-row | 1134.67 | 0.15 | 0.61 | 9.09 |
| Z1-S3 | g-z1s02-row | 1144.08 | 9.56 | 9.89 | 19.38 |
| Z1-S4 | g-z1s04-drill | 1154.59 | -0.32 | 0.00 | 6.05 |
| Z1-S5 | g-z1s05-title | 1161.66 | -0.30 | 0.00 | 11.22 |

## 6. Could not be mounted as the plan or the script words it
- **Four wavs open without a silent lead-in** (A5-S4, A5-S8, A5-S15, A5-S18: the scan finds sound within 0.15 s of the file's start). They are placed like the rest; their first word may sit up to 0.15 s later than the table says.
- **A5-S21 is 2.62 s** as its own composition (`g-a5s21-end`): one line, "a slow push that holds on the microphone", then black. The brief has under 3 s to work with.
- **The script's second book note** (before Z1-S5, "the book, once, here") has no copy and no asset; nothing is mounted for it. The one book ad is the config file at 636.77.
- **A4-S1 after the ad** is a page crop (`g-a4s01-eyes`), a real page of the study. DESIGN.md asks for real footage, not a graphic, on the cut out of the ad; the plan's composition is mounted as planned.
- **The six film cuts have no audio stream.** They are mounted muted and untouched; `learnings/README.md` says every mounted video needs an audio stream, so the lead decides whether silence is muxed in before a render.
- **The video ends 1.0 s after the last sound of Z1-S5.** El Reno held its title card for 4.0 s; a longer hold is the lead's call.
