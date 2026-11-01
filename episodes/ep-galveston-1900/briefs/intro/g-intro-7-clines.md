# g-intro-7-clines · I1-S1 (0.00 to 8.10) · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `episodes/ep-1974-super-outbreak/compositions/g-person-allen.html` (text-only person card, no photo slot, light band drift) and library/official `lt-stack-bars` (two names in sequence).

## 0. Claim
In 1900 Isaac Cline was Galveston's Local Forecast Official; his brother Joseph worked beside him as the observer.

## 1. Source
- factcheck-D.md I1-S1 and sources-cline.md §2: MWR byline "Local Forecast Official and Section Director" (NOAA VLab reprint); "the senior Weather Bureau employee present at Galveston".
- sources-cline.md §2 and factcheck-B.md I1-S1: "Mr. J. L. Cline, Observer"; brother via Wikipedia.
- No portrait of either man was found (footage-inventory.md): text-only cards, no photo slot, no monogram.

## 2. Datum, scale, orientation
Overlay comp, transparent root, over the MWR September 1900 report page at its byline (track 1, slow push). Zones: lower-third (one card, two names in turn), source line top-left.

## 3. Geometry (px)
- Lower-third glass card at `left:110px; bottom:110px` (`_list.md` "Shared rules"). Name 1 "ISAAC CLINE" Arial Black 900 52 px; role 1 "Local Forecast Official, Galveston" Arial 700 27 px `#f5d98b`.
- Name 2 "JOSEPH CLINE" and role 2 "Observer · his brother" in the same card position, replacing name 1 (a line swap: line A exits up 40 px through the card's overflow, line B enters from 40 px below; the card stays and resizes its width by scaleX on an inner background, never by `width`).
- A light band (`linear-gradient` 120 px wide, rgba(255,255,255,0.08)) drifts across the card left to right and back, 3 s each way, finite repeats over the host.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900".

## 4. Must be true in the picture
1. One name on screen at a time.
2. The card does not cover the byline on the page; the orchestrator's push keeps the byline in the top 60 % of frame (y < 640). Card top edge is at about y 840.
3. Role 2 says "Observer" (MWR's word); "his brother" is from Wikipedia (secondary) and is spoken in the narration, so it may go; if the orchestrator wants primary-only text, drop "· his brother".
4. Nothing in x >= 1600, y >= 680 (the presenter circle is on from here).

## 5. Text and cues (i1-s1.words.json, segment 14.274 s)
- Source line in at 0.00.
- 2.74 ("Isaac" 2.74) /* ISAAC @2.74 */: card in with name 1; role 1 at 4.04 ("weather" 4.04).
- 5.24 ("His" 5.24): line swap begins; name 2 lands at 5.60 ("Joseph" 5.60) /* JOSEPH @5.60 */; role 2 at 7.20 ("observer" 7.20).
- 7.50 to 8.10: card exits (slide left `x:-980`, autoAlpha 0, power3.in), the source line fades with it; at 8.10 ("The storm" 8.10) g-intro-8-track cuts in full frame.
- Host 0.00 to 8.10.

## Motion for the whole window
0.00 to 2.74 only the source line (it drifts; under 4 s). Then the card, the band drift and the swap.

## Exit
As above, slide out ending 8.10.

## Footage under it
MWR September 1900 report page with Cline's byline (archive.org `sim_monthly-weather-review_1900-09_28_9` or the NOAA library PDF; public domain).
