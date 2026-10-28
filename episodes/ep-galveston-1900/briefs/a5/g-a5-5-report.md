# g-a5-5-report · A5-S4 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `references/editing-patterns/g-cite-paper.html` (page with a lit line); lower-third as `compositions/g-intro-7-clines.html`.

## 0. Claim
Cline's own signed report, printed in the Weather Bureau's journal in September 1900, says the public was warned by telephone and verbally, and that he advised merchants on Strand Street. No ride.

## 1. Source
sources-cline.md §3: "The public was warned, over the telephone and verbally."; "I went down on Strand street and advised some wholesale commission merchants who had perishable goods on their floors to place them 3 feet above the floor." Heading "SPECIAL REPORT ON THE GALVESTON HURRICANE", MWR 28(9) (fact-check a5-r1 rows 16 to 19).

## 2. Datum, scale, orientation
Full-frame page comp: the comp mounts the MWR report page crop(s) itself (open item 6), because the lit bars must sit on measured line boxes. Two crops if the two sentences are on different pages; a cut between them at 7.98.
Archive Strand Street storefronts are not on disk (no LoC licence checked): the page is held, as the Picture line's fallback says.

## 3. Geometry (px)
- Page image: crop to the text column's full line width plus 24 px margin each side, scaled so the column is 1240 px wide, centred x 960. The sentence to be lit sits at y 420 to 520 at the end of each push.
- Push: scale 1.00 to 1.12 toward the first lit line (0 to 7.9), then 1.12 to 1.20 toward the second (8.0 to end). Under 1.5x, so linear is fine. No line may be cut at the frame edges: if the column at 1.20 is wider than 1728 px, narrow the crop, never cut words.
- Lit bars per `_list.md` shared rule; bar box measured on the image, stated in the receipt.
- Lower-third `left:110px; bottom:110px`: name "ISAAC CLINE" Arial Black 900 52 px `#f2f5f8`, role "SPECIAL REPORT · MWR, SEPT 1900" Arial 700 27 px `#f5d98b`, glass card.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900 (NWS Heritage reprint)".

## 4. Must be true in the picture
1. The lit text is exactly the report's words: line 1 contains "The public was warned, over the telephone and verbally"; line 2 contains "I went down on Strand street and advised some wholesale commission merchants". Whole lines lit, nothing else.
2. Only one bar is lit at a time: bar 1 fades to 0 before bar 2 draws.
3. The lower-third never covers a lit line (lit lines at y < 560; lower-third top ~ 830).
4. No word is cut by the frame at any push scale.
5. Nothing in x >= 1600, y >= 680 except the page (page text there means the circle goes off; report it).

## 5. Text and cues (a5-s4.words.json, segment 10.32 s)
- 0.00: page on, push starts; source line in.
- 0.64 ("report," 0.64) /* REPORT @0.64 */: lower-third in.
- 3.60 ("September." 3.60): lower-third out (slide left).
- 4.64 ("public" 4.64) /* PUBLIC @4.64 */: bar 1 draws; page dims to 0.55 around it. 5.66 ("telephone"): bar 1 at full.
- 7.98 ("and" 7.98): bar 1 fades, push moves to line 2.
- 8.54 ("Strand" 8.54) /* STRAND @8.54 */: bar 2 draws, done by 9.04; holds through "merchants." 10.00.
- Host: A5-S4 0.00 to 10.32 + 1.0 s land time.

## Motion for the whole window
The page push runs the whole host; lower-third and source line drift.

## Exit
Fade-through to the next segment's card: root to 0 over the last 0.4 s.

## Footage under it
None besides the page crops it mounts (MWR Sept 1900, NOAA, public domain).
