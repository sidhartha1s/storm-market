# g-a5-4-pages · A5-S3 8.74 to end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `library/inhouse/split-shared-scale.html` (two-column split), `references/editing-patterns/g-cite-paper.html` (page card). This comp is the base g-a5-11-panel copies: send it alone for a full-size read first.

## 0. Claim
Cline left two accounts of his Saturday, and they do not match: his September 1900 report, and the ride told later.

## 1. Source
- Report: MWR 28(9) Sept 1900, "Special report on the Galveston hurricane", signed "Isaac M. Cline, Local Forecast Official and Section Director" (fact-check a5-r1 row 16; sources-cline.md §3).
- Later telling: TSHA Handbook, Cline "drove a horse-drawn cart around low areas warning people to leave" (sources-cline.md §4; fact-check row 20). Report and memoir do not match: fact-check row 15.

## 2. Datum, scale, orientation
Full-frame designed card (tokens radial background). Two page cards side by side, same size, with an empty gap between them that is the point of the picture.

## 3. Geometry (px)
- Left page L: `left:160px; top:150px; width:640px; height:760px`, the MWR report first page crop (open item 6) scaled to fit whole lines, slight rotation -1.5 deg, shadow `0 20px 60px rgba(0,0,0,.6)`.
- Right page R: `left:1120px; top:150px; width:640px; height:760px`, a typeset page in beige cite card `rgba(232,222,200,.90)`, dark text `#2a2622`, Georgia: heading "Galveston Hurricane of 1900" 34 px, then the one sentence "The Weather Bureau official in charge locally, Isaac M. Cline, drove a horse-drawn cart around low areas warning people to leave." 28 px, line-height 1.4, padding 56 px; foot "Handbook of Texas Online" 20 px `#6b6257`. Rotation +1.5 deg.
- Gap: x 800 to 1120 (320 px) stays empty: no line, no arrow, no label.
- Tag over each page, top 96: L "HIS REPORT · SEPT 1900" left-aligned x 160; R "LATER TELLING" left-aligned x 1120. Arial Black 900 34 px `#f2f5f8`.
- Page R must end by y 910 so x >= 1600, y >= 680 holds part of R: the presenter circle goes OFF for this comp (a page is under the corner). Report to the orchestrator.
- Source line top-left at top 54 would collide with the tags at top 96: put the source line bottom-left `left:96px; top:990px`: "Isaac Cline, Monthly Weather Review, Sept. 1900 · Texas State Historical Association".

## 4. Must be true in the picture
1. Left is the 1900 report, right is the later telling (time runs left to right).
2. The gap is empty and at least 300 px wide for the whole window.
3. The right page is visibly typeset (not dressed as a 1900 scan): it is a quotation, not a document facsimile.
4. No word of either page is cut at its box edge in any frame.
5. Nowhere does the 1891 article appear.

## 5. Text and cues (a5-s3.words.json; host starts at "The" 8.74)
Comp-local = word time − 8.74.
- 8.74 /* TWO @8.82 */: frame 0 shows background only; L slides in from x -700 (0.6 s power3.out) at 8.82 ("two"), R from x +700 at 8.98 ("accounts").
- 9.38 ("Klein" 9.38): tags in, 0.2 s stagger.
- 10.86 ("don't" 10.86) /* MATCH @11.24 */: the two pages ease apart by 20 px each (gap widens to 360), 10.86 to 11.40, power2.out.
- Host: 8.74 to 11.50 + gap to A5-S4 (pages hold; next comp g-a5-5 is the report page).

## Motion for the whole window
Both pages float (y ±4, opposite phase); a slow push on the whole card scale 1.00 to 1.03.

## Exit
Cut to A5-S4's report page: R slides out right `x:980, autoAlpha 0, 0.6 s power3.in` in the last 0.6 s while L stays (the next shot is the same report).

## Footage under it
None (full-frame card).
