# g-a2-2-belen-lt · A2-S1 5.32 to 21.06 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `compositions/g-intro-7-clines.html` (same lower-third card in this episode; copy its CSS, rename every id), official `lt-dark-card` for the accent rule.

## 0. Claim
The place in the picture is the Jesuit College of Belen in Havana, where the priests ran the weather observatory. This comp is the lower-third and the source lines only; the narration carries the rest.

## 1. Source
- Belen, Jesuit, Havana: sources-cuba.md §1 (NOAA AOML 2015); factcheck/a2-r1.md row 3 (cubamemorias.com "Fundado por los Padres Jesuítas en la Habana en 1857"); row 6 (lower-third and source line confirmed).
- Picture credits: `media/candidates/a2/provenance.csv`: Belen College engraving, "C. H. Tate, Munsey Magazine, December 1898" (verifier: an illustration drawn from a photograph, label it an illustration, never a photo; it shows the college building); Havana Cathedral, LOC cph.3a35359, dated 1900.

## 2. Datum, scale, orientation
Overlay comp, transparent root. Under it (orchestrator mounts, lower track, whole window):
- 5.32 to 13.56: `media/a2/belen-college-1898.jpg` (staged from `A2-S1_c1_belen-college-1898.jpg`, capped at 1920 x 1080), slow push.
- 13.56 to 21.06: `media/a2/havana-cathedral-1900.jpg` (staged from `A2-S1_c2_havana-cathedral-1900-loc.jpg`), slow drift. The cut sits on "That's" 13.56.
Comp-local time = segment time minus 5.32.

## 3. Geometry (px)
- Lower-third card `left:110px; bottom:110px` (Shared rules): name line "Belen Observatory" Arial Black 900 52 px `#f2f5f8`; role line "Jesuit College of Belen, Havana" Arial 700 27 px `#f5d98b`; a 3 px `#d8a13a` accent rule under the name that draws left to right (scaleX 0 to 1, transformOrigin left center, 0.5 s). Card padding 18px 28px; width hugs the text (about 560 px).
- Source line A (top-left, Shared rules): "Illustration: C. H. Tate, Munsey Magazine, December 1898".
- Source line B (same box position): "Havana Cathedral, 1900 · Library of Congress".
- Three tiers: 52 / 27 / 19 px.

## 4. Must be true in the picture
1. The lower-third is on screen only over the Belen engraving (5.32 to 13.56 segment time): it names that building, so it never sits over the cathedral photo (mg-quickref 7a item 7).
2. The word "photo" appears nowhere; source line A says "Illustration".
3. Source line A shows only over the engraving, B only over the cathedral; they never show together.
4. The card does not cover a face or the building's doorway in the frame read (if the orchestrator's push puts the building low in frame, the card stays put and the push is changed, not the card).
5. Nothing enters x >= 1600, y >= 680 (card right edge about 670).

## 5. Text and cues (a2-s1.words.json; times below are segment time, comp-local = minus 5.32)
- 5.32 ("Jesuit" 5.32): source line A in (y 8 to 0, autoAlpha 0 to 1, 0.4 s, power2.out). /* ENGRAVING @5.32 */
- 6.22 ("Belen" 6.22) /* BELEN @6.22 */: lower-third enters; accent rule draws 6.50 to 7.00; role line in at 6.58 ("there," 6.58) (y 10 to 0, autoAlpha 0 to 1, 0.35 s).
- 8.32 ("observatory." 8.32): accent rule brightens (opacity 0.6 to 1, 0.3 s) so the word lands on the card.
- 12.96 to 13.56: lower-third exits (`to x:-980, autoAlpha 0, 0.6, power3.in`), done before the cut.
- 13.56 ("That's" 13.56): source line A out (autoAlpha to 0, 0.2 s), source line B in (0.3 s) at the cut. /* CATHEDRAL @13.56 */
- 13.56 to 21.06: B holds with its drift.
- Host: A2-S1 5.32 to 21.062 (comp duration 15.742).

## Motion for the whole window
Card and source lines drift y +-4 px (2.4 s yoyo). Footage moves under it (push, drift). No gap of 4 s without motion: the drift runs the whole window.

## Exit
Source line B fades to 0 over the last 0.3 s (20.762 to 21.062), on the cut to the A2-S2 paper card.

## Footage under it
Belen College engraving (1898), then Havana Cathedral (1900), as §2. Both public domain by provenance.csv; both need staging (open item in `_list.md`).
