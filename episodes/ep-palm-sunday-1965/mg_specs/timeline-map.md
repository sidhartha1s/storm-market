# mg_specs/timeline-map.md: where every act composition sits on the timeline (ep-palm-sunday-1965)

Read from `index.html` on 12 Oct 26 by a read-only script, after the mounts were typed by hand. `index.html` is the source: if a number here and a mount disagree, the mount wins and this file is corrected. Composition names are the ones in `acts-plan.md` section 2 and are never changed. Total length 1184.66 s. All times in seconds.

Retimed 12 Oct 26, 19:13, to Paul's five real clips, the new line Z1-S4b and a 4.0 s end hold. Nothing before 233.10 moved. Every later start moved by one amount per stretch: +0.25 from 242.52 (after `ins-paul-2`), -0.33 from 635.77 (after `ins-paul-3`), -0.64 from 716.29 (after `ins-paul-4`), +0.65 from 941.46 (after `ins-paul-5`), +1.11 from 1134.52 (after `ins-paul-6`); the close after Z1-S4 was laid out again. No composition changed length except `g-z1s04-drill` (7.05 to 7.10) and `g-z1s05-title` (12.22 to 15.23). Table 5's first and last sounds were scanned again after the voice conversion: they moved by -0.01 to +0.07 s against the first layout, and the wavs were not moved for that.

How the times were set (the hook and intro's own rules, nothing added):
- Wav lengths are `ffprobe` on `audio/*.wav`. First and last sound of each wav are a silence scan (`silencedetect`, -35 dB, 0.15 s); `words.json` writes 0.00 for a first word, so a first word is timed from the scan and every other word from `words.json`.
- 1.0 s from the last sound of one composition's voice to the first sound of the next composition's; 0.8 s between segments inside one composition; wavs never under 0.05 s or over 0.75 s apart.
- A composition starts on the first sound of its first segment and ends where the next picture starts. After black or after a Paul clip it starts on the cut instead, and the voice follows (first sound in table 5).
- Act seam: the last composition ends 1.0 s after its last sound, then 0.7 s of black, and the next act's first sound lands on the cut out of black.
- **A cue inside a composition** = the segment's "wav start inside the composition" (table 5) + the word's time in `audio/<seg>.words.json`. For a segment's first word use the "first sound" column.
- **Paul's five clips are the real files**, each cut where his sound ends (table 2). A clip starts 1.0 s after the last sound before it (on the cut out of black for Z1-S1); the next wav starts 0.15 s after the cut and the next composition starts on the cut.
- **The video ends 4.0 s after the last sound of Z1-S5** (1180.66), over `g-z1s05-title`.

## 1. Compositions (69)
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
| g-a1s15-offices | compositions/g-a1s15-offices.html | A1-S15, A1-S16, A1-S17 | 242.77 | 34.71 | 277.48 |
| g-a1s18-list | compositions/g-a1s18-list.html | A1-S18, A1-S19 | 277.48 | 11.68 | 289.16 |
| g-a2s01-radar | compositions/g-a2s01-radar.html | A2-S1, A2-S2 | 289.86 | 16.69 | 306.55 |
| g-a2s03-chain | compositions/g-a2s03-chain.html | A2-S3, A2-S4, A2-S5 | 306.55 | 21.92 | 328.47 |
| g-a2s06-headstart | compositions/g-a2s06-headstart.html | A2-S6, A2-S7 | 328.47 | 17.66 | 346.13 |
| g-a2s08-first | compositions/g-a2s08-first.html | A2-S8 | 346.13 | 6.69 | 352.82 |
| g-a2s09-countya | compositions/g-a2s09-countya.html | A2-S9, A2-S10 | 352.82 | 18.79 | 371.61 |
| g-a2s11-backup | compositions/g-a2s11-backup.html | A2-S11, A2-S12, A2-S13 | 371.61 | 22.96 | 394.57 |
| g-a2s14-six | compositions/g-a2s14-six.html | A2-S14 | 394.57 | 10.39 | 404.96 |
| g-a2s15-old | compositions/g-a2s15-old.html | A2-S15 | 404.96 | 10.91 | 415.87 |
| g-a2s16-huffman | compositions/g-a2s16-huffman.html | A2-S16 | 415.87 | 15.43 | 431.30 |
| g-a2s17-funnels | compositions/g-a2s17-funnels.html | A2-S17, A2-S18 | 431.30 | 18.96 | 450.26 |
| g-a2s19-log | compositions/g-a2s19-log.html | A2-S19 | 450.26 | 12.55 | 462.81 |
| g-a2s20-front | compositions/g-a2s20-front.html | A2-S20 | 462.81 | 8.07 | 470.88 |
| g-a2s21-list | compositions/g-a2s21-list.html | A2-S21 | 470.88 | 9.09 | 479.97 |
| g-a3s01-message | compositions/g-a3s01-message.html | A3-S1, A3-S2, A3-S3 | 480.67 | 18.73 | 499.40 |
| g-a3s04-links | compositions/g-a3s04-links.html | A3-S4 | 499.40 | 9.07 | 508.47 |
| g-a3s05-bremen | compositions/g-a3s05-bremen.html | A3-S5, A3-S6 | 508.47 | 19.92 | 528.39 |
| g-a3s07-calls | compositions/g-a3s07-calls.html | A3-S7, A3-S8 | 528.39 | 17.24 | 545.63 |
| g-a3s09-jam | compositions/g-a3s09-jam.html | A3-S9 | 545.63 | 10.26 | 555.89 |
| g-a3s10-towers | compositions/g-a3s10-towers.html | A3-S10 | 555.89 | 11.47 | 567.36 |
| g-a3s11-onoff | compositions/g-a3s11-onoff.html | A3-S11 | 567.36 | 12.69 | 580.05 |
| g-a3s12-seven | compositions/g-a3s12-seven.html | A3-S12 | 580.05 | 7.59 | 587.64 |
| g-a3s13-battery | compositions/g-a3s13-battery.html | A3-S13, A3-S14 | 587.64 | 21.23 | 608.87 |
| g-a3s15-desks | compositions/g-a3s15-desks.html | A3-S15, A3-S16, A3-S17 | 608.87 | 17.34 | 626.21 |
| g-a4s01-eyes | compositions/g-a4s01-eyes.html | A4-S1 | 661.85 | 6.71 | 668.56 |
| g-a4s02-countyb | compositions/g-a4s02-countyb.html | A4-S2, A4-S3, A4-S4, A4-S5 | 668.56 | 32.43 | 700.99 |
| g-a4s06-died | compositions/g-a4s06-died.html | A4-S6 | 700.99 | 5.16 | 706.15 |
| g-a4s08-chief | compositions/g-a4s08-chief.html | A4-S8 | 715.65 | 11.18 | 726.83 |
| g-a4s09-clock | compositions/g-a4s09-clock.html | A4-S9, A4-S10 | 726.83 | 21.86 | 748.69 |
| g-a4s11-farend | compositions/g-a4s11-farend.html | A4-S11, A4-S12 | 748.69 | 22.43 | 771.12 |
| g-a4s13-duty | compositions/g-a4s13-duty.html | A4-S13 | 771.12 | 13.98 | 785.10 |
| g-a4s14-eight | compositions/g-a4s14-eight.html | A4-S14 | 785.10 | 8.48 | 793.58 |
| g-a4s15-chain | compositions/g-a4s15-chain.html | A4-S15 | 793.58 | 9.92 | 803.50 |
| g-a4s16-fortwayne | compositions/g-a4s16-fortwayne.html | A4-S16 | 803.50 | 10.31 | 813.81 |
| g-a5s01-radar | compositions/g-a5s01-radar.html | A5-S1, A5-S2, A5-S3 | 814.51 | 31.67 | 846.18 |
| g-a5s04-berne | compositions/g-a5s04-berne.html | A5-S4, A5-S5 | 846.18 | 18.70 | 864.88 |
| g-a5s06-hold | compositions/g-a5s06-hold.html | A5-S6 | 864.88 | 15.98 | 880.86 |
| g-a5s07-marion | compositions/g-a5s07-marion.html | A5-S7, A5-S8 | 880.86 | 19.90 | 900.76 |
| g-a5s09-alto | compositions/g-a5s09-alto.html | A5-S9 | 900.76 | 5.99 | 906.75 |
| g-a5s10-alert | compositions/g-a5s10-alert.html | A5-S10, A5-S11 | 906.75 | 17.99 | 924.74 |
| g-a5s12-spotters | compositions/g-a5s12-spotters.html | A5-S12 | 924.74 | 8.02 | 932.76 |
| g-a5s14-noissue | compositions/g-a5s14-noissue.html | A5-S14 | 942.11 | 6.15 | 948.26 |
| g-a5s15-dark | compositions/g-a5s15-dark.html | A5-S15 | 948.26 | 7.71 | 955.97 |
| g-a5s16-toledo | compositions/g-a5s16-toledo.html | A5-S16, A5-S17 | 955.97 | 19.27 | 975.24 |
| g-a5s18-curran | compositions/g-a5s18-curran.html | A5-S18, A5-S19 | 975.24 | 20.33 | 995.57 |
| g-a5s20-team | compositions/g-a5s20-team.html | A5-S20 | 995.57 | 9.19 | 1004.76 |
| g-a5s21-end | compositions/g-a5s21-end.html | A5-S21 | 1004.76 | 2.62 | 1007.38 |
| g-a6s01-recs | compositions/g-a6s01-recs.html | A6-S1 | 1008.08 | 7.92 | 1016.00 |
| g-a6s02-floorplan | compositions/g-a6s02-floorplan.html | A6-S2 | 1016.00 | 10.15 | 1026.15 |
| g-a6s03-announcer | compositions/g-a6s03-announcer.html | A6-S3, A6-S4 | 1026.15 | 17.47 | 1043.62 |
| g-a6s05-wires | compositions/g-a6s05-wires.html | A6-S5, A6-S6 | 1043.62 | 16.94 | 1060.56 |
| g-a6s07-power | compositions/g-a6s07-power.html | A6-S7 | 1060.56 | 12.44 | 1073.00 |
| g-a6s08-spotters | compositions/g-a6s08-spotters.html | A6-S8 | 1073.00 | 12.71 | 1085.71 |
| g-a6s09-third | compositions/g-a6s09-third.html | A6-S9 | 1085.71 | 9.47 | 1095.18 |
| g-a6s10-watch | compositions/g-a6s10-watch.html | A6-S10 | 1095.18 | 13.79 | 1108.97 |
| g-a6s11-sirens | compositions/g-a6s11-sirens.html | A6-S11, A6-S12 | 1108.97 | 16.25 | 1125.22 |
| g-z1s02-row | compositions/g-z1s02-row.html | Z1-S2, Z1-S3 | 1135.63 | 20.39 | 1156.02 |
| g-z1s04-drill | compositions/g-z1s04-drill.html | Z1-S4 | 1156.02 | 7.10 | 1163.12 |
| g-z1s4b-book | compositions/g-z1s4b-book.html | Z1-S4b | 1163.12 | 6.31 | 1169.43 |
| g-z1s05-title | compositions/g-z1s05-title.html | Z1-S5 | 1169.43 | 15.23 | 1184.66 |

Every host is `id="host-<name without g->"`, track 2, 1920 x 1080.

## 2. Paul's clips (5), real files
| Paul clip | File | Segment | Start (s) | Duration (s) | End (s) | First sound in the clip (s) |
|---|---|---|---|---|---|---|
| ins-paul-2 | media/paul/ins-paul-2/ins-paul-2.mp4 | A1-S14 | 233.10 | 9.67 | 242.77 | 0.41 |
| ins-paul-3 | media/paul/ins-paul-3/ins-paul-3.mp4 | A3-S18 | 626.21 | 9.23 | 635.44 | 0.60 |
| ins-paul-4 | media/paul/ins-paul-4/ins-paul-4.mp4 | A4-S7 | 706.15 | 9.50 | 715.65 | 0.19 |
| ins-paul-5 | media/paul/ins-paul-5/ins-paul-5.mp4 | A5-S13 | 932.76 | 9.35 | 942.11 | 0.50 |
| ins-paul-6 | media/paul/ins-paul-6/ins-paul-6.mp4 | Z1-S1 | 1125.92 | 9.71 | 1135.63 | 0.36 |

Track 1, own sound, no narration under them; the narrator wavs of these five segments are not mounted. Every file is 10.000 s, 1920 x 1080, with the logo burned in. Each clip is cut where his sound ends, as `ins-paul-1` was (silence scan at -30 dB, 0.08 s). `ins-paul-4` is cut at 9.50 from a -25 dB scan: at -30 dB its sound runs to 9.91, room noise after his last word (`words.json` ends "office." at 9.24). The chip "County B" over `ins-paul-4` is the overlay `ov-chip-countyb` in `index.html` (same window as the clip). `ins-paul-3` ends on "What did he do?" and the book ad's dip-in starts on that cut.

## 3. Film cuts under compositions (7 mounts)
Track 1, muted, class `filmwin`: left 480, top 150, 960 x 720 (the 4:3 window of `acts-plan.md` rule 15). The composition above draws the ground, the frame and the label, leaves the window open while the film shows, and covers it when the script says the window goes. A mount runs longer than the window needs so the composition, not the mount, decides the cut. No builder mounts a film.
| Film mount | File | Under composition | Start (s) | Duration (s) | Start inside the composition (s) |
|---|---|---|---|---|---|
| v-a1s15-room | media/films/cuts/a14-05-operations-room.mp4 | g-a1s15-offices | 242.77 | 12.99 | 0.00 |
| v-a1s16-announcer | media/films/cuts/a14-09-announcer.mp4 | g-a1s15-offices | 255.76 | 9.44 | 12.99 |
| v-a2s4-operators | media/films/cuts/a14-13-operators.mp4 | g-a2s03-chain | 312.69 | 7.84 | 6.14 |
| v-a3s7-telephone | media/films/cuts/a14-10-desk-telephone.mp4 | g-a3s07-calls | 528.39 | 11.41 | 0.00 |
| v-a4s2-room | media/films/cuts/a14-05-operations-room.mp4 | g-a4s02-countyb | 668.56 | 4.00 | 0.00 |
| v-a5s11-call | media/films/cuts/a14-08-telephone-call.mp4 | g-a5s10-alert | 915.58 | 4.17 | 8.83 |
| v-a6s12-horn | media/films/cuts/a14-01-siren-horn.mp4 | g-a6s11-sirens | 1114.32 | 10.90 | 5.35 |

- `v-a1s16-announcer` ends 22.43 s into `g-a1s15-offices`; the window must be covered by then. "A few stations" is spoken at 21.47 s, so the first angle alone is enough and the two extra angle files are not mounted.
- `v-a4s2-room` (added 12 Oct 26, 19:30, on the lead's order) is the first film after the book ad: the operations room from 20.0 s into the file (`data-media-start="20"`), for the first 4.0 s of `g-a4s02-countyb`, which must leave the window open for those 4.0 s. It is the file's second use (the first is its first 12.99 s under `g-a1s15-offices`), so the mount carries `data-callback="payoff cut after the book ad: real footage"`.
- `v-a5s11-call` is the whole 4.17 s file; the first sentence of A5-S11 ends 10.31 s into `g-a5s10-alert`, so the window is open for about 1.5 s.

## 4. Black and the book ad
| Black | Start (s) | Duration (s) | End (s) |
|---|---|---|---|
| bo-i1 (after the intro, approved) | 112.48 | 0.70 | 113.18 |
| bo-a1 | 289.16 | 0.70 | 289.86 |
| bo-a2 | 479.97 | 0.70 | 480.67 |
| bo-cta-in (the ad's dip in) | 635.44 | 1.00 | 636.44 |
| bo-cta-out (the ad's dip out) | 660.85 | 1.00 | 661.85 |
| bo-a4 | 813.81 | 0.70 | 814.51 |
| bo-a5 | 1007.38 | 0.70 | 1008.08 |
| bo-a6 | 1125.22 | 0.70 | 1125.92 |

Book ad `ins-cta-paul` (`media/cta/paul-storm-ready-v7-oct10.mp4`): 636.44 for 24.417 s, 0.5372 of the total, inside the config window 0.40 to 0.60. It follows Paul's tease (A3-S18) and A4-S1 pays the tease on the cut out of the dip. A3 has no chapter blackout of its own.

## 5. Segments inside their compositions (108)
"Wav start inside the composition" can be negative: the wav's silent lead-in starts before the picture does.
| Segment | Composition | Wav start (s) | Wav start inside the composition (s) | First sound inside the composition (s) | Last sound inside the composition (s) |
|---|---|---|---|---|---|
| A1-S1 | g-a1s01-kc | 112.87 | -0.31 | 0.00 | 8.74 |
| A1-S2 | g-a1s02-strip | 122.68 | -0.25 | 0.00 | 8.60 |
| A1-S3 | g-a1s02-strip | 131.96 | 9.03 | 9.39 | 19.56 |
| A1-S4 | g-a1s04-wire | 143.28 | -0.21 | 0.00 | 8.93 |
| A1-S5 | g-a1s05-clocks | 153.03 | -0.40 | 0.00 | 8.13 |
| A1-S6 | g-a1s06-low | 162.07 | -0.49 | -0.01 | 6.50 |
| A1-S7 | g-a1s07-tracks | 169.65 | -0.42 | 0.00 | 11.50 |
| A1-S8 | g-a1s07-tracks | 181.93 | 11.86 | 12.32 | 25.07 |
| A1-S9 | g-a1s09-forecasts | 195.92 | -0.23 | -0.01 | 8.06 |
| A1-S10 | g-a1s09-forecasts | 204.62 | 8.47 | 8.87 | 17.55 |
| A1-S11 | g-a1s09-forecasts | 214.10 | 17.95 | 18.35 | 24.36 |
| A1-S12 | g-a1s09-forecasts | 220.88 | 24.73 | 25.15 | 30.20 |
| A1-S13 | g-a1s13-chain | 227.03 | -0.32 | 0.00 | 4.75 |
| A1-S15 | g-a1s15-offices | 242.92 | 0.15 | 0.47 | 12.19 |
| A1-S16 | g-a1s15-offices | 255.42 | 12.65 | 12.99 | 23.48 |
| A1-S17 | g-a1s15-offices | 266.68 | 23.91 | 24.28 | 33.71 |
| A1-S18 | g-a1s18-list | 277.07 | -0.41 | 0.00 | 7.63 |
| A1-S19 | g-a1s18-list | 285.52 | 8.04 | 8.48 | 10.68 |
| A2-S1 | g-a2s01-radar | 289.44 | -0.42 | 0.00 | 8.26 |
| A2-S2 | g-a2s01-radar | 298.51 | 8.65 | 9.07 | 15.69 |
| A2-S3 | g-a2s03-chain | 306.27 | -0.28 | 0.00 | 5.33 |
| A2-S4 | g-a2s03-chain | 312.40 | 5.85 | 6.14 | 13.19 |
| A2-S5 | g-a2s03-chain | 320.33 | 13.78 | 13.98 | 20.92 |
| A2-S6 | g-a2s06-headstart | 328.00 | -0.47 | -0.01 | 10.90 |
| A2-S7 | g-a2s06-headstart | 339.91 | 11.44 | 11.69 | 16.65 |
| A2-S8 | g-a2s08-first | 345.64 | -0.49 | 0.00 | 5.68 |
| A2-S9 | g-a2s09-countya | 352.51 | -0.31 | 0.00 | 12.39 |
| A2-S10 | g-a2s09-countya | 365.53 | 12.71 | 13.19 | 17.79 |
| A2-S11 | g-a2s11-backup | 371.45 | -0.16 | 0.00 | 7.49 |
| A2-S12 | g-a2s11-backup | 379.59 | 7.98 | 8.30 | 16.38 |
| A2-S13 | g-a2s11-backup | 388.57 | 16.96 | 17.18 | 21.96 |
| A2-S14 | g-a2s14-six | 394.31 | -0.26 | 0.00 | 9.39 |
| A2-S15 | g-a2s15-old | 404.57 | -0.39 | 0.00 | 9.91 |
| A2-S16 | g-a2s16-huffman | 415.58 | -0.29 | 0.00 | 14.42 |
| A2-S17 | g-a2s17-funnels | 430.80 | -0.50 | -0.01 | 12.30 |
| A2-S18 | g-a2s17-funnels | 444.04 | 12.74 | 13.10 | 17.96 |
| A2-S19 | g-a2s19-log | 450.03 | -0.23 | 0.00 | 11.55 |
| A2-S20 | g-a2s20-front | 462.49 | -0.32 | 0.00 | 7.07 |
| A2-S21 | g-a2s21-list | 470.32 | -0.56 | 0.00 | 8.09 |
| A3-S1 | g-a3s01-message | 480.12 | -0.55 | 0.00 | 5.90 |
| A3-S2 | g-a3s01-message | 487.12 | 6.45 | 6.70 | 13.64 |
| A3-S3 | g-a3s01-message | 494.74 | 14.07 | 14.44 | 17.74 |
| A3-S4 | g-a3s04-links | 499.01 | -0.39 | 0.00 | 8.07 |
| A3-S5 | g-a3s05-bremen | 508.00 | -0.47 | 0.00 | 11.18 |
| A3-S6 | g-a3s05-bremen | 520.19 | 11.72 | 11.98 | 18.88 |
| A3-S7 | g-a3s07-calls | 527.88 | -0.51 | 0.00 | 10.61 |
| A3-S8 | g-a3s07-calls | 539.55 | 11.16 | 11.41 | 16.23 |
| A3-S9 | g-a3s09-jam | 545.11 | -0.52 | 0.00 | 9.27 |
| A3-S10 | g-a3s10-towers | 555.51 | -0.38 | 0.00 | 10.47 |
| A3-S11 | g-a3s11-onoff | 566.91 | -0.45 | 0.00 | 11.69 |
| A3-S12 | g-a3s12-seven | 579.80 | -0.25 | 0.00 | 6.59 |
| A3-S13 | g-a3s13-battery | 587.42 | -0.22 | 0.00 | 8.43 |
| A3-S14 | g-a3s13-battery | 596.62 | 8.98 | 9.24 | 20.23 |
| A3-S15 | g-a3s15-desks | 608.52 | -0.35 | 0.00 | 5.60 |
| A3-S16 | g-a3s15-desks | 615.02 | 6.15 | 6.40 | 11.86 |
| A3-S17 | g-a3s15-desks | 621.29 | 12.42 | 12.67 | 16.34 |
| A4-S1 | g-a4s01-eyes | 661.54 | -0.31 | 0.00 | 5.71 |
| A4-S2 | g-a4s02-countyb | 668.16 | -0.40 | 0.00 | 9.26 |
| A4-S3 | g-a4s02-countyb | 678.40 | 9.84 | 10.06 | 13.98 |
| A4-S4 | g-a4s02-countyb | 683.08 | 14.52 | 14.77 | 23.18 |
| A4-S5 | g-a4s02-countyb | 692.13 | 23.57 | 24.14 | 31.43 |
| A4-S6 | g-a4s06-died | 700.72 | -0.27 | 0.00 | 4.17 |
| A4-S8 | g-a4s08-chief | 715.80 | 0.15 | 0.68 | 10.18 |
| A4-S9 | g-a4s09-clock | 726.32 | -0.51 | 0.00 | 7.47 |
| A4-S10 | g-a4s09-clock | 734.69 | 7.86 | 8.35 | 20.86 |
| A4-S11 | g-a4s11-farend | 748.27 | -0.42 | 0.00 | 9.79 |
| A4-S12 | g-a4s11-farend | 758.86 | 10.17 | 10.59 | 21.43 |
| A4-S13 | g-a4s13-duty | 770.67 | -0.45 | 0.00 | 12.97 |
| A4-S14 | g-a4s14-eight | 784.88 | -0.22 | -0.01 | 7.47 |
| A4-S15 | g-a4s15-chain | 793.21 | -0.37 | 0.00 | 8.92 |
| A4-S16 | g-a4s16-fortwayne | 803.29 | -0.21 | 0.00 | 9.31 |
| A5-S1 | g-a5s01-radar | 814.08 | -0.43 | 0.00 | 7.53 |
| A5-S2 | g-a5s01-radar | 822.57 | 8.06 | 8.33 | 18.51 |
| A5-S3 | g-a5s01-radar | 833.49 | 18.98 | 19.48 | 30.67 |
| A5-S4 | g-a5s04-berne | 846.18 | 0.00 | 0.00 | 12.56 |
| A5-S5 | g-a5s04-berne | 859.27 | 13.09 | 13.36 | 17.69 |
| A5-S6 | g-a5s06-hold | 864.45 | -0.43 | 0.00 | 14.99 |
| A5-S7 | g-a5s07-marion | 880.63 | -0.23 | 0.00 | 9.16 |
| A5-S8 | g-a5s07-marion | 890.82 | 9.96 | 9.96 | 18.89 |
| A5-S9 | g-a5s09-alto | 900.27 | -0.49 | 0.00 | 4.98 |
| A5-S10 | g-a5s10-alert | 906.48 | -0.27 | 0.00 | 7.96 |
| A5-S11 | g-a5s10-alert | 915.10 | 8.35 | 8.83 | 16.99 |
| A5-S12 | g-a5s12-spotters | 924.40 | -0.34 | 0.00 | 7.02 |
| A5-S14 | g-a5s14-noissue | 942.26 | 0.15 | 0.57 | 5.15 |
| A5-S15 | g-a5s15-dark | 948.26 | 0.00 | 0.00 | 6.71 |
| A5-S16 | g-a5s16-toledo | 955.53 | -0.44 | 0.00 | 11.92 |
| A5-S17 | g-a5s16-toledo | 968.26 | 12.29 | 12.72 | 18.28 |
| A5-S18 | g-a5s18-curran | 975.24 | 0.00 | 0.00 | 9.26 |
| A5-S19 | g-a5s18-curran | 984.88 | 9.64 | 10.12 | 19.33 |
| A5-S20 | g-a5s20-team | 995.16 | -0.41 | 0.00 | 8.19 |
| A5-S21 | g-a5s21-end | 1004.33 | -0.43 | 0.00 | 1.62 |
| A6-S1 | g-a6s01-recs | 1007.69 | -0.39 | 0.01 | 6.92 |
| A6-S2 | g-a6s02-floorplan | 1015.49 | -0.51 | 0.00 | 9.15 |
| A6-S3 | g-a6s03-announcer | 1025.74 | -0.41 | 0.00 | 7.01 |
| A6-S4 | g-a6s03-announcer | 1033.60 | 7.45 | 7.83 | 16.48 |
| A6-S5 | g-a6s05-wires | 1043.30 | -0.32 | 0.00 | 7.87 |
| A6-S6 | g-a6s05-wires | 1051.88 | 8.26 | 8.68 | 15.96 |
| A6-S7 | g-a6s07-power | 1060.23 | -0.33 | 0.00 | 11.44 |
| A6-S8 | g-a6s08-spotters | 1072.71 | -0.29 | 0.01 | 11.73 |
| A6-S9 | g-a6s09-third | 1085.48 | -0.23 | -0.01 | 8.48 |
| A6-S10 | g-a6s10-watch | 1094.97 | -0.21 | 0.00 | 12.79 |
| A6-S11 | g-a6s11-sirens | 1108.72 | -0.25 | 0.00 | 4.31 |
| A6-S12 | g-a6s11-sirens | 1113.73 | 4.76 | 5.34 | 15.30 |
| Z1-S2 | g-z1s02-row | 1135.78 | 0.15 | 0.62 | 9.10 |
| Z1-S3 | g-z1s02-row | 1145.19 | 9.56 | 9.89 | 19.39 |
| Z1-S4 | g-z1s04-drill | 1155.70 | -0.32 | 0.07 | 6.11 |
| Z1-S4b | g-z1s4b-book | 1162.68 | -0.44 | 0.00 | 5.31 |
| Z1-S5 | g-z1s05-title | 1169.12 | -0.31 | 0.00 | 11.23 |

## 6. Could not be mounted as the plan or the script words it
- **Four wavs open without a silent lead-in** (A5-S4, A5-S8, A5-S15, A5-S18: the scan finds sound within 0.15 s of the file's start). They are placed like the rest; their first word may sit up to 0.15 s later than the table says.
- **A5-S21 is 2.62 s** as its own composition (`g-a5s21-end`): one line, "a slow push that holds on the microphone", then black. The brief has under 3 s to work with.
- **The script's second book note** is now the line Z1-S4b (`audio/z1-s4b.wav`, 6.062 s) under `g-z1s4b-book`, between the drill line and the title card. The composition file is the builder's to make; the host is mounted for it. The one book ad is the config file at 636.44.
- **A4-S1 after the ad** is a page crop (`g-a4s01-eyes`), a real page of the study. DESIGN.md asks for real footage, not a graphic, on the cut out of the ad; the plan's composition is mounted as planned.
- **The six film cuts have no audio stream.** They are mounted muted and untouched; `learnings/README.md` says every mounted video needs an audio stream, so the lead decides whether silence is muxed in before a render.
- **Paul starts speaking 0.19 to 0.60 s into each new clip** (table 2); `ins-paul-1` has no such lead-in. The clips are mounted from their first frame, so the silence before his first word is 1.0 s plus that lead-in.
