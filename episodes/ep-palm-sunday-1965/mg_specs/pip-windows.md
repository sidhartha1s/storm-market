# Corner circle windows (12 Oct 26)

Rule: `references/mg-quickref.md` "Corner circle" (it wins over this table). Times are read from `index.html` as it stood on 12 Oct 26.
Face passes (made on the ZBook, `media/pip/`): A = `paul-pip-A.mp4`, first frame at timeline 9.870 s, narration to 635.44 s. B = `paul-pip-B.mp4`, first frame at 668.160 s, narration to 1184.66 s.
Each window is its own file `media/pip/paul-w<n>.mp4`. Windows 2 to 11 are cut with `scripts/circle_cut.py`'s own `cut_args` (the recipe's framing: crop 0.868 square, left 0.066, top 0.0125 of the pass width, so hands and the pass's frozen bottom edge are out of view; 240x240, 25 fps, h264 crf 23, silent stereo AAC stream per learnings/render.md; the narration in the pass files is not carried over). circle_cut.py's `main()` reads the windows from `<video id="pip-w<n>" class="pip">` mounts in index.html, which do not exist yet, so the cut called its function with the seek and length of this table; the ffmpeg call is the script's, unedited. Each file is one frame (0.04 s) longer than its window by design (`PAD`), plus up to one frame of rounding: mount with `data-duration` = the window length below. Mount each from 0 (`data-media-start` stays 0): offset below is where it was cut from the pass. Window 1 was cut before the ruling, 512x512 uncropped; it is cut, not mounted.

| n | timeline start (s) | timeline end (s) | length (s) | face | offset in pass (s) | file length (s) | starts because | ends because |
|---|---|---|---|---|---|---|---|---|
| 1 | 37.60 | 112.48 | 74.88 | A | 27.73 | 74.88 | first intro graphic (g-i1s1-house), after the full-frame opening and the tease | blackout bo-i1 |
| 2 | 113.18 | 233.10 | 119.92 | A | 103.31 | 119.92 | blackout over | ins-paul-2 starts (full-frame, circle off) |
| 3 | 242.77 | 289.16 | 46.39 | A | 232.90 | 46.40 | ins-paul-2 over (film window v-a1s15 starts) | blackout bo-a1 |
| 4 | 289.86 | 479.97 | 190.11 | A | 279.99 | 190.12 | blackout over | blackout bo-a2 |
| 5 | 480.67 | 626.21 | 145.54 | A | 470.80 | 145.56 | blackout over | ins-paul-3 starts |
| 6 | 668.16 | 706.15 | 37.99 | B | 0.00 | 38.00 | first narration line after the ad (a4-s1), over the film window and g-a4s01-eyes | ins-paul-4 starts |
| 7 | 715.65 | 813.81 | 98.16 | B | 47.49 | 98.16 | ins-paul-4 over (g-a4s08-chief starts) | blackout bo-a4 |
| 8 | 814.51 | 932.76 | 118.25 | B | 146.35 | 118.28 | blackout over | ins-paul-5 starts |
| 9 | 942.11 | 1007.38 | 65.27 | B | 273.95 | 65.28 | ins-paul-5 over (g-a5s14-noissue starts) | blackout bo-a5 |
| 10 | 1008.08 | 1125.22 | 117.14 | B | 339.92 | 117.16 | blackout over | blackout bo-a6 |
| 11 | 1135.63 | 1169.43 | 33.80 | B | 467.47 | 33.80 | ins-paul-6 over (g-z1s02-row starts) | close card g-z1s05-title starts |

OFF by rule, no window: 0 to 37.60 (full-frame opening ins-paul-1 0 to 9.72, then the tease T1 9.72 to 37.60); blackouts 112.48, 289.16, 479.97, 813.81, 1007.38, 1125.22 (0.70 s each); ins-paul-2 to 6 (233.10 to 242.77, 626.21 to 635.44, 706.15 to 715.65, 932.76 to 942.11, 1125.92 to 1135.63); the book ad with its dips 635.44 to 661.85; the close card 1169.43 to 1184.66. Silent stretch 661.85 to 668.16: face B has no face before its first line.

## Readings and flags
- Hook and intro graphics (T1 and I1), corner x >= 1600, y >= 680, read on existing frames (28 frames between 37.6 and 109.2 s from `.qc-tmp/lintfix-after`, `mg-docs-r2`, `mg-docs-r3`, `lead-final-1`; sheet `.qc-tmp/pip-corner/intro-corners.jpg`): corner empty in all 28 (blank wall or ground, dark base). No existing frame of g-i1s4-states (66.95 to 77.02) or g-i1s5-onair (77.02 to 81.66) or the end of g-i1s10-list (109.29 to 112.48): read from the older draft `renders/ep-palm-sunday-1965-preview-v1-draft.mp4` at 60, 64, 68, 72, 76, 78, 80, 81.4, 110, 111.5 s (`.qc-tmp/pip-corner/draft-corners.jpg`): wall, sky, black, and photographs with no label or figure of ours. That draft is older than the current compositions, so these are readings of the draft, not of the current files.
- Film windows (7 cuts under v-a1s15, v-a1s16, v-a2s4, v-a3s7, v-a4s1, v-a5s11, v-a6s12), 3 frames each (`.qc-tmp/pip-corner/film-corners.jpg`): no broadcaster mark or text in the corner.
- Act graphics: not read; the lead's brief says each is built to keep the corner empty. 17 mounted hosts have no composition file yet, so the corner is unchecked for them and must be read when they are built: g-a2s11-backup, g-a3s09-jam, g-a3s11-onoff, g-a3s13-battery, g-a4s06-died, g-a4s09-clock, g-a4s11-farend, g-a4s14-eight, g-a5s04-berne, g-a5s07-marion, g-a5s10-alert, g-a5s16-toledo, g-a6s05-wires, g-a6s07-power, g-a6s08-spotters, g-z1s04-drill, g-z1s4b-book.
- Window 11 runs to the close card. g-z1s4b-book (1163.12 to 1169.43, the book cover with one line) is unbuilt: if its cover sits in the corner, mount window 11 with `data-duration` 27.49 (ends 1163.12). The file is long enough either way.
- Window 6 starts at 668.16, the start of the first line after the ad, not on a graphic cut (the next cut is 668.56). Mount from 668.56 with offset 0.40 if a cut is preferred.
- "The first card" in the recipe is read as the first intro graphic at 37.60 s (reading, the agent's). If the owner means the first act card (113.18 s), window 1 is dropped and the circle first appears in window 2.
- The tail of each pass video runs past its wav (A 0.35 s, B 0.94 s); windows 5 and 11 end well before those tails.
