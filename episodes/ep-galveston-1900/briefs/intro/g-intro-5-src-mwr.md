# g-intro-5-src-mwr · H1-S5 + first beat of T1-S1 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: cards.css `.srclab` (restyled to the glass surface and moved top-left per `_list.md` "Shared rules").

## 0. Claim
The line about his wife comes from Isaac Cline's own report in the Monthly Weather Review, September 1900. This comp is the source line only: the human beat carries itself (edit script H1-S5 [HUMAN]; no chip, no popfig).

## 1. Source
sources-cline.md §3: "Among the lost was my wife, who never rose above the water after the wreck of the building." (Cline, Special Report, MWR Sept 1900, reprinted by NWS Heritage, vlab.noaa.gov).

## 2. Datum, scale, orientation
Overlay comp, transparent root, over: the 1891 page with its light dimming (0.00 to about 1.2), then the MWR report page with a slow push to the wife line (to the end of H1-S5), then held one beat into T1-S1 (0.00 to 0.88 of T1-S1) before g-intro-6 cuts in.

## 3. Geometry (px)
- One glass card top-left `left:96px; top:54px`, padding 6px 14px. Line "Isaac Cline, Monthly Weather Review, Sept. 1900" Arial 700 19 px `#c8d3e0`.
- To pass the three-tier rule with fewer than 4 text nodes the gate does not apply (one text node); no exemption needed.

## 4. Must be true in the picture
1. The source line is not on screen over the 1891 page (it would credit the wrong document): it enters only once the MWR page is the picture.
2. Nothing else on screen: the wife line on the page is the reading target.
3. The card does not cover the pushed-to line on the page; the push ends with that line at y > 300 (orchestrator's push), else the card moves to `top:960px; left:96px` and the receipt says so.

## 5. Text and cues (h1-s5.words.json, segment 3.795 s; t1-s1.words.json)
- In at the cut to the MWR page. The cut sits at 1.22 ("lost" 1.22) unless the orchestrator's index.html says otherwise: fade and rise (y 8 to 0, autoAlpha 0 to 1, 0.4 s, power2.out) at 1.22. /* MWR PAGE @1.22 */
- Holds through "wife" 3.26 to the segment end 3.795, then through T1-S1 0.00 to 0.88 ("island" 0.88, where g-intro-6 cuts in).
- Host: H1-S5 1.22 to T1-S1 0.88 (comp-local length = the gap read from index.html + 2.575 + 0.88).

## Motion for the whole window
The card drifts y +-4 px (2.4 s yoyo); the window is about 3.5 to 4 s.

## Exit
Fade to 0 in the last 0.3 s, ending on the cut at T1-S1 0.88 (the island graphic is a full-frame cut, so a slide would be cut off).

## Footage under it
MWR September 1900 report page scan (archive.org `sim_monthly-weather-review_1900-09_28_9`, or the NOAA library PDF in footage-inventory.md), page with "Among the lost was my wife". Public domain (NOAA).
