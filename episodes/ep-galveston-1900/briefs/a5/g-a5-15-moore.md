# g-a5-15-moore · A5-S10 0 to 9.94 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `references/editing-patterns/g-person-allen.html` in its text-only form (mg-quickref: a person card without a real photo drops the photo slot, no monogram).

## 0. Claim
No statement was found from Willis Moore saying Havana called the storm right; the storm's track (northwest, into the Gulf) matched what Belen had said.

## 1. Source
- No statement: sources-cuba.md §5 ("Moore or Bureau admitted Cuban view was right | UNSOURCED | none | No such statement found"); §2 (fact-check a5-r1 row 43). A search limit, so the chip says FOUND, not MADE.
- Track: AOML 2015, "the Belén forecasters said their observations indicated the storm moved to the northwest and into the Gulf of Mexico" (sources-cuba.md §1 and §5; row 44).
- Moore's title: as used in the intro (`briefs/intro/g-intro-8-track.md` Moore lower-third). Use that brief's exact title string; if it differs from "CHIEF, US WEATHER BUREAU", the intro's wins.

## 2. Datum, scale, orientation
0 to 4.62: full-frame designed card (tokens radial). 4.62 to 9.94: overlay over a still of `g-intro-8-track`'s settled end frame (open item 4), mounted by the orchestrator on the lower track; the comp's background goes transparent at 4.62 (cross-fade 0.4 s).

## 3. Geometry (px)
- Person card P (glass, text only), centred x 960, top 330, 900 x 200: name "WILLIS MOORE" Arial Black 900 72 px `#f2f5f8`; role "CHIEF, US WEATHER BUREAU" Arial 700 27 px `#f5d98b`.
- Chip C1 "NO STATEMENT FOUND", glass, centred x 960, top 580.
- Chip C2 over the track still, top-left anchored to avoid the track line: `left:96px; top:140px`, main "NORTHWEST, INTO THE GULF" Arial Black 900 44 px, tag "AS BELEN CALLED IT" Arial 700 22 px `#93a3b2` tracking 4. Check the still: C2 must not cover the track line or its labels; if it does, move C2 to the frame's emptiest quadrant above y 680 and say where.
- Source line top-left at top 54: "NOAA AOML, 2015" (from 4.62; before that "Search of Weather Bureau records, MWR 1900").

## 4. Must be true in the picture
1. No photo, no silhouette, no monogram of Moore.
2. C1 says FOUND (a search limit), never "NO STATEMENT" alone.
3. C2 sits over the track picture only, never over the person card.
4. "BELEN" spelled Belen (Whisper wrote "Bellin").
5. Corner x >= 1600, y >= 680 empty of text; the still's own labels there turn the circle off: say so.

## 5. Text and cues (a5-s10.words.json, segment 20.16 s)
- 0.00 ("I" 0.00): background; 0.12 source line (search wording) in.
- 1.60 ("Willis" 1.60) /* MOORE @1.60 */: P in (y 24 -> 0, back.out).
- 2.52 ("Havana" 2.52): nothing new (one target).
- 3.12 ("called" 3.12) /* NO STATEMENT @3.84 */: C1 in at 3.84 ("right.").
- 4.62 ("The" 4.62): P and C1 out (slide right), background cross-fades to transparent over the track still; source line swaps to "NOAA AOML, 2015".
- 6.60 ("northwest," 6.60) /* NORTHWEST @6.60 */: C2 main in; tag at 8.70 ("Bellin").
- Host: 0.00 to 9.94 (g-a5-16 cuts at "And" 9.94).

## Motion for the whole window
Cards drift; under the still a slow push 1.00 to 1.04 (on the still layer, orchestrator mount, or in this comp if the still is mounted inside it).

## Exit
C2 slides out right 9.34 to 9.94; cut to the island.

## Footage under it
4.62 to 9.94: still PNG of `g-intro-8-track` at its settled end (the real track into the Gulf toward Galveston), captured by the orchestrator after that comp passes its read.
