# BRIEF — g-toll-counter · section I, "What fell" (0:22) · RHS stat panel over Lallantop river/rescue b-roll

## 0. What this graphic claims
Nepal's disaster agency counted twelve dead and seven missing on Sept 27; later press counts climbed to twenty
four by Sept 28. Two facts: the official same-day count, and that the press count moved up.

## 1. SOURCE
factcheck-A #4 (NewsBytes 24 dead/14 missing, Sept 28, nationwide) and script I: "Nepal's disaster agency counted
twelve people who didn't survive the storm, with seven more missing. Later press counts ran as high as twenty
four." Row 1 = the agency count (12/7); row 2 = the moved press count (24). Do not imply both are the same
scope — script already carries that caveat in A4's fuller ledger; this card is the teaser, two lines only.

## 2. DATUM, SCALE, ORIENTATION
RHS panel, right:0 top:0 bottom:0 width:820px (mg-quickref RHS stat panel spec), gradient
`linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0))`, padding 90px 96px 0 170px. No map/geometry;
two counter rows stacked vertically, eyebrow-first order per quickref: eyebrow, place, serif sub, rows, counter.

## 3. GEOMETRY (px)
- Panel: right 0, width 820, padding-top 90, left padding 170.
- Row 1 (agency count): top 360. Counter "12" Courier 84px #e74c3c, label below "LIVES LOST" 20px #c8d3e0; second
  inline counter "7" same tier, label "MISSING" — both inside one row, counters at x 170 and x 460.
- Source line under row 1 at top 470: "NEPAL DISASTER AGENCY · SEPT 27" 19px #93a3b2.
- Row 2 (press count): top 620, single counter "24" 84px #e74c3c landing after row 1 settles, label "PRESS COUNTS
  UP TO" 20px #c8d3e0 above the number, source line "SEPT 28" 19px #93a3b2 below.
- Headline above row 1 at top 260: "What the day counted." Arial Black 52px #f2f5f8.

## 4. MUST BE TRUE IN THE PICTURE
1. Row 1 shows 12 and 7 as two distinct counters, never merged into one number.
2. Row 1's source line reads "Nepal disaster agency" and "Sept 27" — never NewsBytes.
3. Row 2's counter animates 0 -> 24 and is captioned "press counts up to" (moved number, not a second official
   count) with "Sept 28".
4. Row 2 lands strictly after row 1 has settled (no simultaneous reveal of both counts).
5. No text inside the presenter keep-out (x>=1600 y>=680).

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "On the day it fell...")
Headline "What the day counted." · row 1 counters "12" / "7", labels "LIVES LOST" / "MISSING", source "NEPAL
DISASTER AGENCY · SEPT 27" · row 2 counter "24", label "PRESS COUNTS UP TO", source "SEPT 28".
Cues (s): panel in 0.0 · headline 0.3 · row 1 reveal + counters start 2.6 /* CUE "twelve people" @est 3.09 */ ·
source line 1 3.6 · row 2 reveal + counter start 5.4 /* CUE "seven more missing" @est 5.83 */ (row1 second counter
"7" lands here too) · row 2 counter climbs to 24 8.9 /* CUE "twenty four" @est 9.26 */, finishes 10.3 · hold to
11.5 · exit 11.9-12.5 (x:980, autoAlpha:0, 0.6s power3.in). Duration 12.5s (declared; retime after TTS per
mg-quickref "duration = max(declared, last cue + tail)").

## 6. CONTRACT
Standard: `<template>` root `#root` transparent, `data-composition-id="g-toll-counter"`, PAUSED gsap timeline at
`window.__timelines["g-toll-counter"]`. Prefix ids `tc-`. See mg-quickref "File contract".

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-nepal-floods-2026 --comp g-toll-counter`, then
`node scripts/graphics_qc.mjs episodes/ep-nepal-floods-2026`, `python3 scripts/run_gates.py episodes/ep-nepal-floods-2026`.

## 8. RECEIPT
See builder's final message.
