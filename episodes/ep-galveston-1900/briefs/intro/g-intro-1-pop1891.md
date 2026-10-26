# g-intro-1-pop1891 · H1-S1 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (this folder). Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (popfig block only) and cards.css `.popfig`.

## 0. Claim
The page Paul holds is from Galveston, Texas, July 1891. Date and place only; no other text in the hook's first frame.

## 1. Source
sources-cline.md §1: Commons file "Galveston_Daily_News_-_July_16,_1891.jpg", "Date: 16 July 1891" (cites Portal to Texas History metapth466111 p.5). Place: the Galveston Daily News. Edit script H1-S1 Picture line: popfig "GALVESTON, TEXAS · JULY 1891" inside the first second.

## 2. Datum, scale, orientation
Overlay on Paul's full-frame clip 1 (`ins-paul-1`, not generated yet). Start frame `assets/paul/paul-start-frame-omni.jpg`, measured at 1920 width: his head and face fill x 790 to 1120, y 80 to 545; hands and shirt below to y 1000; left of x 700 is a dark warm bookshelf; right of x 1130 are bright radar monitors (a red hurricane swirl at about 1300, 320). So the popfig sits in the LEFT column over the shelf, never centre (it would cover his face) and never right (red on a red-orange radar).

## 3. Geometry (px)
- Popfig block left-aligned (override `.popfig`'s centring): `left:110px; top:300px; text-align:left`.
- Big line "JULY 1891": Abril 118 px (display tier floor; 150 does not fit the column). Its right edge must be at or left of x 700. Measure the rendered width; if it passes 700, drop to 110 px, never below.
- Sub line "GALVESTON, TEXAS" above the big line (place first, it reads in order with the spoken "Galveston"), Arial 700 32 px `#e8e3d8`, letter-spacing 3 px, same left edge, 12 px gap.
- Behind both, a local scrim: radial gradient `rgba(4,7,12,0.55)` to 0, ellipse 760 x 420 px centred on the text block, so the red reads over the lit shelf lamp (at about 255, 300).

## 4. Must be true in the picture
1. Nothing of the popfig crosses x 760 (40 px clear of his hair) in any frame, including the 1.35 scale-in (scale from the left edge: `transformOrigin:"left center"`).
2. The date reads JULY 1891. The day (16) is not on this popfig; it appears in I1-S5's popfig.
3. Exactly two text lines on screen; no source line (the hook's first frame carries only the hook sentence and this popfig).
4. The bottom-right corner stays empty (Flow logo at 1740, 900 is baked into the clip).

## 5. Text and cues (h1-s1.words.json; PROVISIONAL: retime to the Paul clip's own words.json once clip 1 exists, the TTS times below are a stand-in)
- "GALVESTON, TEXAS" in at 0.76 ("Galveston" 0.76). /* GALVESTON @0.76 */
- "JULY 1891" in at 1.00 (within the first second, the edit script's ask; it follows the sub by 0.24 s).
- Both drift (+-4 px) to 3.50 ("damage" 3.50), then exit together 3.50 to 3.95, so the frame is clean for "their city" 3.90 to 4.49.
- Host: 0.76 to 4.49 (3.73 s). Exit anchored to the last 0.6 s.

## Motion for the whole window
The scrim breathes (opacity 0.85 to 1, 1.2 s yoyo); the text drifts +-4 px. Window is under 4 s, so no idle gap is possible, but the drift starts at land time anyway.

## Exit
Scale 1 to 0.92 with autoAlpha 0, 0.45 s, power2.in, ending at 3.95 (host continues empty to 4.49 only if the host cannot end earlier; prefer host end = 3.95 + 0.05).

## Footage under it
`ins-paul-1` (Paul full frame, track 1, his own audio). Until the clip exists, read the frame over `assets/paul/paul-start-frame-omni.jpg` mounted as a still.
