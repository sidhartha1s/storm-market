Host: id=g-a2s01-radar file=compositions/g-a2s01-radar.html start=289.86 (timeline-map.md table 1; the mount in index.html wins) duration=16.69 s (wavs 16.29 s plus their gaps) track=2

# g-a2s01-radar · A2-S1, A2-S2 · what the 5:43 warning said, and where its radar news came from (wave 2, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). A flash is a stroke or fill change (rule 12). Map geometry comes from the file (rule 14). No map shows Alto; inlined map ids take this comp's prefix; line weight is read at both ends of the zoom (rule 20).
**Spoken (A2-S1):** "The warning said radar showed strong storm echoes near Michigan City and just west of Knox. It told people in three counties to be on the alert."
**Spoken (A2-S2):** "But South Bend had no radar. Its radar news came over the telephone, from operators at other Weather Bureau offices."
**One look:** the warning's own typed lines under a map that shows what they describe; then the map pulls back and the radar sets are all somewhere else.

## 0. What this graphic claims
The 5:43 PM warning named two radar echoes (near Michigan City, just west of Knox) and put LaPorte, Starke and Marshall counties on the alert. South Bend had no radar of its own: its radar reports came by telephone from operators at other Weather Bureau offices.

## 1. Source
- `edit_script.md` A2-S1, Rows [A6; survey printed p. 39]; A2-S2, Rows [H; study printed p. 13] · [H; IWX: "relying on phone conversations with radar operators in Chicago"].
- Page crop `media/docs/survey-p39-radar-crop.png` (1460 x 142, cut from `media/docs/survey-pdf-67-orig.png`, survey printed p. 39). Its four lines, read on the file: `Radar indicates some very strong storm echoes in the vicinity of Michigan City` / `Indiana and in an area just west of Knox Indiana. In these areas a tornado` / `may touch the ground. Residents in the counties of LaPorte Starke and Marshall` / `should be on the alert for possible tornadoes and severe thunderstorms for the`.
- The Picture note puts radar rings at Chicago, Fort Wayne and Indianapolis. Only Chicago is named by a source row as a place South Bend spoke to, so the telephone line runs from Chicago alone.
- Positions: `media/data/points.csv`; counties: `media/maps/indiana-counties.svg`.

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-1; the camera is its `viewBox` and its CSS box, tweened together.
| State | Box (left, top, width, height) | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| NORTH (family state) | 716, 62, 1080, 450 | `296 166 360 150` | 3.0 (screen x = 3u - 172, y = 3u - 436) | A2-S1 |
| WIDE (this comp's) | 558, 62, 803, 900 | `226 96 464 520` | 1.7306 (screen x = 558 + 1.7306 x (u - 226), y = 62 + 1.7306 x (u - 96)) | A2-S2 |
NORTH to WIDE is a pull back of 1.73 times in 0.8 s (power2.inOut), box and viewBox in one tween, end values set exactly; `preserveAspectRatio="xMidYMid meet"`. Indiana runs off the bottom of the WIDE box (clipped by the SVG); that is intended. In WIDE the box ends at x 1361: the presenter corner stays empty.
Underline box, measured on the crop by a row and column scan: `should be on the alert` is the first five words of the crop's last line, crop x 38 to 409, y 113 to 137.
The echo shapes are schematic: the warning gives a vicinity, not an outline.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | BM-1 groups inlined, ids prefixed `radar-`; county lines 1.5 px, Indiana's outline 3 px, non-scaling. Every `pt-` group hidden except the ones named below, each from its cue. Dot radius 6 px on screen: `r` 2 map units in NORTH, 3.47 in WIDE (tween `r` with the pull back) |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `5:43 PM` / `South Bend, Indiana`; hour hand 171.5 degrees, minute hand 258 degrees. Clock face: `media/drawings/wall-clock.svg` inline or the face of `compositions/g-t1s2-warning.html` |
| Document card | design sheet section 9: left 96, top 640, 1480 x 162; Beige polaroid border 10 px; the crop 1460 x 142 inside at (106, 650). Right edge 1576, clear of the corner |
| Underline | Popfig red 6 px under `should be on the alert`: screen x 144 to 515, y 791 to 797 (4 px under the line box; it lies on the card's lower border because the crop ends at its last line) |
| Unlit page | Panel dark at 45 % over the whole crop except the box x 136 to 523, y 759 to 791, fading in over 0.4 s as the underline starts |
| Document source | under the card, right aligned at x 1560, top 816: Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey report, 1965, p. 39` |
| Echo 1 | inside the map SVG, in map units so it rides the camera: two overlapping ellipses centred on (384, 186), `rx` 13 `ry` 9 turned -20 degrees and `rx` 8 `ry` 7 offset (+7, -4); fill Body light at 30 %, stroke Body light 2 px non-scaling. NORTH screen centre (980, 122) |
| Echo 2 | the same shape, centred on (403.4, 259.8): 14 map units due west of `pt-knox`. NORTH screen centre (1038, 343). Its east edge stops short of the Knox dot |
| Michigan City | dot NORTH (986.6, 111.8); label `Michigan City`, Arial 700 22 px, Body light, right aligned to x 930, top 100 |
| Knox | dot NORTH (1080.2, 343.4); label `Knox`, same type, left 1096, top 332 |
| County names (NORTH) | Arial 700 22 px, Headline white with the credit shadow, tracking 2, centred: `LAPORTE` (1046, 228), `MARSHALL` (1218, 324), `STARKE` (1050, 388): below echo 2, because LaPorte's outline reaches down to y 373 beside Starke |
| Lit county | fill Amber 2 at `fill-opacity` 0.45 on `radar-co-in-laporte`, `radar-co-in-starke`, `radar-co-in-marshall` (0.45 so echo 2 stays readable over Starke) |
| South Bend (WIDE) | dot (966.8, 222.1). Labels left 986, top 198: `South Bend` Arial 700 26 px Body light, and under it (top 230) `no radar` Arial 700 22 px Label grey |
| Radar rings (WIDE) | overlay SVG, at Chicago (655.3, 170.9), Fort Wayne (1214.1, 409.9), Indianapolis (993.8, 829.5): two circles radius 46 and 26, Body light 3 px, and one sweep line from the centre to the outer circle that turns one full turn in 2.4 s (ease none, one turn, then rests pointing up). Each town's dot sits at the centre |
| Ring labels | Arial 700 22 px, Body light, centred under each ring: `Chicago` (655, top 226), `Fort Wayne` (1214, top 466), `Indianapolis` (994, top 885) |
| Telephone line | overlay SVG, Body light 4 px solid, round caps, from Chicago (655.3, 170.9) to South Bend (966.8, 222.1), 316 px, drawn from Chicago with `strokeDashoffset`. Label `by telephone`, Arial 700 22 px, Label grey, centred on x 811, top 150 (above the line's midpoint) |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 13 · National Weather Service, Northern Indiana` (851 px wide at 22 px) |

## 4. Must be true in the picture
1. The card is the page's own image; nothing on it is retyped. The underline sits under `should be on the alert` and under no other word.
2. Echo 1 is at Michigan City (its dot is inside or on the edge of the echo). Echo 2 is west of the Knox dot and does not cover it. Neither echo carries a time, a speed or a track.
3. Exactly three counties light, and they are LaPorte, Starke and Marshall. Porter, St. Joseph, Elkhart and Kosciusko stay unlit in this comp.
4. The stamp reads 5:43 PM; hour hand between 5 and 6, minute hand between 8 and 9. It has left the frame before the pull back ends.
5. In WIDE, South Bend's dot has no ring. Rings sit only at Chicago, Fort Wayne and Indianapolis. The telephone line joins Chicago to South Bend and no other pair.
6. No ring radius is a range: the rings are all one size and none is labelled with miles.
7. Line weights and dot sizes are the same at both ends of the pull back (read both frames).
8. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680. The crop is on screen about 8.2 s and changes at 7.70 (underline and unlit page).

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `5:43 PM` · `South Bend, Indiana` · `Michigan City` · `Knox` · `LAPORTE` · `STARKE` · `MARSHALL` · `Weather Bureau survey report, 1965, p. 39` · `South Bend` · `no radar` · `by telephone` · `Chicago` · `Fort Wayne` · `Indianapolis` · `Disaster Research Center, 1966, p. 13 · National Weather Service, Northern Indiana`. Page words are the image.
Cue words and times are from `audio/a2-s1.words.json` and `audio/a2-s2.words.json` as they stood on 12 Oct 26 at 17:50, after the voice conversion's re-transcription. A2-S2 starts at 9.00 s (the wav length of A2-S1); the gap `mg_specs/timeline-map.md` puts between the two segments (not on disk yet) is added to every A2-S2 row. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S1 | 0 | The | 0.00 | 0.00 | first frame: ground and the map in NORTH, no dot, no label |
| 1 | A2-S1 | 1 | warning | 0.50 | 0.08 | clock stamp slides in from the left (0.6 s, power3.out), hands already at 5:43 |
| 2 | A2-S1 | 2 | said | 0.76 | 0.34 | document card slides in from the right (`x:660` to 0, 0.7 s, power3.out); document source fades in after it |
| 3 | A2-S1 | 9 | Michigan | 3.10 | 2.68 | Michigan City dot and label; echo 1 fades in (0.4 s) |
| 4 | A2-S1 | 15 | Knox | 5.00 | 4.58 | Knox dot and label; echo 2 fades in (0.4 s) |
| 5 | A2-S1 | 20 | three | 7.06 | 6.64 | LaPorte, Starke, Marshall fill in that order, 0.12 s apart (0.3 s each), each with its name |
| 6 | A2-S1 | 22 | to | 7.70 | 7.28 | unlit page fades in; underline draws under `should be on the alert` (0.5 s, left to right) |
| 7 | A2-S2 | 0 | But | 0.00 | 9.07 | card and document source exit right (`x:1900`, 0.5 s, power3.in); stamp exits left (0.5 s); county fills and names, town labels fade (0.3 s) |
| 8 | A2-S2 | 1 | South | 0.52 | 9.17 | pull back NORTH to WIDE (0.8 s); the two echoes stay on the map, smaller |
| 9 | A2-S2 | 5 | radar. | 1.40 | 10.05 | South Bend dot, `South Bend`, then `no radar` 0.15 s later |
| 10 | A2-S2 | 6 | Its | 2.60 | 11.25 | source line fades in (0.3 s) |
| 11 | A2-S2 | 12 | telephone | 3.90 | 12.55 | Chicago dot; the telephone line draws from Chicago to South Bend (0.6 s); `by telephone` fades in at its end |
| 12 | A2-S2 | 14 | operators | 4.88 | 13.53 | rings and labels at Chicago, Fort Wayne, Indianapolis, 0.25 s apart; each sweep line makes its one turn. Hold to the end |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a2s01-radar.html` is the only file the builder writes; `data-composition-id="g-a2s01-radar"`; id prefix `radar-`; root `<div id="radar-root" ...>` styled through `#radar-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (wave 1; brief `mg_specs/briefs/g-a2s14-six.md`): NORTH mount, stamp top left, paper card in the lower band, lit counties. Stamp and page card details from the built `compositions/g-t1s2-warning.html`. The state WIDE is this comp's own.
**Assets mounted (paths from the episode folder):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined. It holds Chicago, Fort Wayne and Indianapolis, so `media/maps/midwest-states.svg` is not mounted here.
- `media/docs/survey-p39-radar-crop.png` (PC-02, 1460 x 142).
- `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136), inlined for the stamp's face.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s01-radar`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page card (the scan's type beside ours): that is the family's accepted flag (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 9.9 (mid pull back) forward and backward and match the frames. Line 6: every dot, ring and line end of section 3 is computed from `media/data/points.csv` by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map only. Then one settled frame per cue: 1.60 (stamp and card), 3.80 (echo 1), 5.70 (echo 2 west of Knox), 7.60 (three counties and names), 8.50 (underline, unlit page), 9.45 and 10.36 (the two ends of the pull back: line weight, dot size), 11.00 (South Bend, no ring), 12.20 (source line), 13.70 (telephone line), 15.60 (three rings at rest, labels clear of rings).
