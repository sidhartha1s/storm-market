# g-a5-10-noride · A5-S6 14.02 to end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/moves/moves.js` (page flick move), `library/inhouse/stat-timeline.html` (rows ticking on).

## 0. Claim
The report Cline signed in September 1900 has no ride in it. It has the drive to the Gulf, the telephone and the merchants.

## 1. Source
grep of the MWR issue text: no "horse", "cart" or beach ride in the report; it holds "I drove to the Gulf", the telephone line and the Strand Street merchants (fact-check a5-r1 row 26; sources-cline.md §3 and §4).

## 2. Datum, scale, orientation
Full-frame comp with the MWR report page crops it mounts (open item 6): only pages of Cline's Special Report, never other MWR articles.

## 3. Geometry (px)
- Page stack, left half: pages 600 x 780, `left:200px; top:150px`, each page flicks (rotateY 0 -> -100 deg around its left edge, 0.35 s, power2.in) to reveal the next; slight shadow.
- Right column, x 980 to 1600, three glass rows, each 100 px tall, gap 24, top 260: a tick box (36 px, `#7fb2e5` stroke) and Arial Black 900 40 px `#f2f5f8`: "DRIVE TO THE GULF", "TELEPHONE", "MERCHANTS".
- Chip "NO RIDE IN THE REPORT", glass, left edge 980, top 150; tag line Arial 700 22 px `#93a3b2` "ISAAC CLINE · MWR, SEPT 1900".
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900".

## 4. Must be true in the picture
1. Only Cline's report pages flick; the last page shown is the signed last page ("Isaac M. Cline, Local Forecast Official and Section Director" visible).
2. No word of a resting page is cut (mid-flick blur frames are exempt only while rotating).
3. The three rows appear in spoken order and each only on its word.
4. Rows column bottom (260 + 3 x 124 = 632) < 680: corner clear.

## 5. Text and cues (a5-s6.words.json; host starts at "And" 14.02)
Comp-local = word time − 14.02.
- 14.02: frame 0 shows the first report page resting; source line on.
- 14.24 ("report" 14.24): flicks begin, one page every 0.45 s through 16.40.
- 16.00 ("doesn't" 16.00) /* NO RIDE @16.70 */: chip in at 16.70 ("ride"); tag 17.08.
- 16.40: the signed last page rests.
- 18.56 ("drive" 18.56) /* GULF @19.18 */: row 1 in, tick draws at 19.18.
- 20.08 ("telephone," 20.08): row 2 in + tick.
- 21.26 ("merchants." 21.26): row 3 in + tick.
- Host: 14.02 to 21.50 + gap to A5-S7 (Paul clip; hard cut).

## Motion for the whole window
Flicks 14.24 to 16.40, then a slow push on the resting page 1.00 to 1.04; rows drift.

## Exit
Hard cut to Paul's full-frame clip: everything slides out right in the last 0.6 s (rows, chip), page stack fades 0.3 s.

## Footage under it
None besides the page crops it mounts (MWR Sept 1900, public domain).
