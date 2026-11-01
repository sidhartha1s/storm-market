# g-a5-8-memoir · A5-S5 12.52 to end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `library/inhouse/title-card.html`; popfig per `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`.

## 0. Claim
The ride is usually traced to Cline's memoir, Storms, Floods and Sunshine, published in 1945, 45 years after the storm.

## 1. Source
NOAA Works Consulted: "Cline, I.M. (1945). Storms, Floods and Sunshine. Gretna, LA: Pelican Publishing" (fact-check a5-r1 rows 22 to 23; sources-cline.md §4). Memoir pages unseen: no quote from the book appears.

## 2. Datum, scale, orientation
Full-frame designed card (tokens radial background). The spine is drawn, not a photo of the book (no scan exists); it must not pretend to be a photograph: flat, simple, no fake wear texture.

## 3. Geometry (px)
- Book spine standing vertical, centred x 760: `width:150px; height:760px; top:160px`, fill `#15202b`, 2 px `#93a3b2` border, radius 6.
- Spine title rotated -90 deg, reading bottom to top: "STORMS, FLOODS AND SUNSHINE" Arial Black 900 44 px `#f2f5f8`. Author at the spine foot, unrotated: "CLINE" Arial 700 22 px `#d8a13a` tracking 4.
- Popfig "1945" right of the spine, big line centre (1240, 470); sub line "HIS MEMOIR" Arial 700 32 px `#e8e3d8` at y 560.
- Source line top-left: "Texas State Historical Association Handbook · Wikipedia summary of later accounts" (as the Picture line; it covers S5 throughout).

## 4. Must be true in the picture
1. Title spelled "STORMS, FLOODS AND SUNSHINE" (no extra comma before AND, whatever Whisper wrote).
2. The popfig is beside the spine, never over it (popfig never over a card).
3. Nothing in x >= 1600, y >= 680.
4. No quotation from the memoir anywhere.

## 5. Text and cues (a5-s5.words.json; host starts at "The" 12.52)
Comp-local = word time − 12.52.
- 12.52: frame 0 shows the background; the spine rises in from y +120 (0.6 s power3.out) at 12.52.
- 14.06 ("memoir," 14.06) /* MEMOIR @14.06 */: spine title wipes on bottom to top (clip-path, 0.6 s); "CLINE" in at 14.40.
- 14.88 ("Storms," 14.88): a 0.3 s brightness pulse on the title; 15.86 ("Floods,"), 16.20 ("Sunshine,") the same, word by word as spoken (three spans).
- 17.70 ("1945." 17.70) /* 1945 @17.70 */: popfig in; sub at 17.90.
- Host: 12.52 to 18.46 + 1.0 s land time.

## Motion for the whole window
Spine sways 1 deg (rotate yoyo 3 s, sine.inOut); slow push on the whole card 1.00 to 1.04.

## Exit
Popfig out (scale 0.92, autoAlpha 0, 0.45 s) then the spine slides out right in the last 0.6 s.

## Footage under it
None (full-frame card).
