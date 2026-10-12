Host: id=g-a5s01-radar file=compositions/g-a5s01-radar.html start=814.51 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=31.67 s track=2

# g-a5s01-radar · A5-S1, A5-S2, A5-S3 · Fort Wayne had a radar: the scope, the hook west of Berne, the 8:40 warning (wave 4, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a rows DR-01 and DR-02, section 3c row PC-12. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). A flash is a stroke or fill change, never a scale pop (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids take this comp's prefix; line weight is read on the first frame (rule 20). This comp names a real office and a real town from the Weather Bureau's public record, so `County A` and `County B` never appear in it.
**Spoken (A5-S1):** "Fort Wayne is the office that didn't pass on the five twenty forecast. It had something South Bend didn't have, a radar of its own."
**Spoken (A5-S2):** "A man who worked there, John Curran, remembers it as a set built in World War Two to spot aircraft. Its small scope had no map on it, and the picture faded fast."
**Spoken (A5-S3):** "At eight forty that scope showed a strong hook shape about five miles west of the town of Berne, moving east. Fort Wayne told Berne to take immediate precautions for the next thirty to sixty minutes."
**One look:** the unlit teletype in Fort Wayne gets a radar ring that South Bend lacks; the ring gives way to one large bare scope with a sweep and a picture that fades; a hook appears west of Berne and the office's own typed warning comes in under it.

## 0. What this graphic claims
Fort Wayne's Weather Bureau office had its own radar and South Bend's did not. John Curran, who worked there, recalls a wartime set with a small scope, no map on it and a picture that faded fast. At 8:40 PM the office's radar showed a strong hook echo about 5 miles west of Berne, moving east, and the office told the Berne area to take precautions "for the next 30 to 60 minutes".

## 1. Source
- `edit_script.md` A5-S1, Rows [A5; study printed p. 10] · [A20; survey printed p. 43: "The Weather Bureau radar at Baer Field"]. A5-S2, Rows [H, Curran; "built in WWII for the purpose of detecting aircraft"; "a rapid decay rate with no map background"]. A5-S3, Rows [A20; survey printed p. 43].
- Page crop `media/docs/survey-p43-840pm-crop.png` (PC-12, 1460 x 202, survey printed p. 43). Its five single-spaced lines, read on the file: `Issued at 8:40 PM EST.` / `The Weather Bureau radar at Baer Field shows a strong hook echo about 5 miles` / `west of Berne Indiana and moving eastward. Residents in the Berne area should` / `take immediate precautions for personal safety for a strong possibility of a` / `tornado for the next 30 to 60 minutes.`
- Positions, map units (`media/data/points.csv`): `pt-fort-wayne` (605.1, 297.0), `pt-south-bend` (462.2, 188.5), `pt-berne` (629.0, 376.8). Berne lies 23.9 units east and 79.8 units south of Fort Wayne (15.8 km east, 47.9 km south by the README's 1.5123 and 1.6651 units per km).
- No 1965 radar scope picture exists (inventory D9): the scope is our drawing, `media/drawings/radar-scope.svg`. The hook's shape is SCHEMATIC; only its place (about 5 miles west of Berne) is from the entry.

## 2. Datum, scale, orientation
North is up on the map and on the scope.
| View | What | Numbers |
|---|---|---|
| MAP (A5-S1 and the start of A5-S2) | BM-1 in the family state NORTH, no camera move | box left 716, top 62, 1080 x 450; viewBox `296 166 360 150`; 3.0 px per map unit (screen x = 3u - 172, y = 3u - 436) |
| SCOPE (from A5-S2 word 11 to the end) | the drawn scope alone, the map gone | centre (1220, 340); screen circle radius 180.6 px, rim 205.8 px; scope scale 1.7 px per map unit about Fort Wayne (the edge of the screen is about 64 km north to south) |
On the scope Berne's dot is at centre + 1.7 x (23.9, 79.8) = (1260.6, 475.7), 141.6 px from the centre. Five miles is 8.05 km, 12.17 map units east to west, 20.7 px: the hook's centre is (1239.9, 475.7).
Underline box, measured on the crop by a row and column scan: the last line is y 159 to 184; `for the next 30 to 60 minutes.` is its words 2 to 8, crop x 183 to 700.
The sweep turns clockwise, 2.4 s a turn. It starts pointing up at 14.98, so at "picture" (17.26) it points to 342 degrees: the smear sits on that bearing so the line lights it as it passes.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `fwr-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px, non-scaling. Every `pt-` group hidden except Fort Wayne (from frame 0) and South Bend (from its cue). Dot radius 6 px (`r` 2 map units), fill Body light. No county is lit in this comp |
| Fort Wayne | dot (1643.3, 455.0); label `Fort Wayne`, Arial 700 22 px, Body light, right aligned to x 1585, top 444 (12 px clear of the ring's west edge at x 1597) |
| Teletype | `media/drawings/teletype.svg` inline inside the map SVG, exactly as `g-a1s09-forecasts` left it in NORTH: `translate(612 240) scale(0.25)` in map units, screen box x 1664 to 1769, y 284 to 389; lines Label grey, `stroke-width` 3 non-scaling, paper (`dw-lamp`) Panel dark: unlit |
| Office chip | glass chip, left 96, top 96, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Weather Bureau · Fort Wayne` |
| South Bend | dot (1214.6, 129.5); labels left 1232: `South Bend` Arial 700 22 px Body light, top 106; `no radar` Arial 700 22 px Label grey, top 132 |
| Radar ring | overlay SVG centred on Fort Wayne's dot (1643.3, 455.0), as `g-a2s01-radar`: two circles radius 46 and 26, Body light 3 px, and one sweep line from the centre to the outer circle. Ring box x 1597 to 1689, y 409 to 501: under the teletype (bottom 389), above the box's edge (512) |
| Name card | glass plate as `compositions/g-i1s2-station.html` `.stn-card`: left 96, top 96, 590 x 260 (bottom 356). `John Curran`: Arial Black 900 52 px, Headline white, left 138, top 118. Sub, Georgia italic 30 px, Amber 2, left 140: `observer, Fort Wayne` top 198, `Weather Bureau, 1965` top 236. Small lines, Arial 700 20 px, Label grey, left 140: `his recollection, published by` top 290, `the National Weather Service` top 316 |
| Scope | `media/drawings/radar-scope.svg` inline in an overlay SVG: `translate(1010 130) scale(2.1)`, `stroke-width="3"` on the `dw-scope` group (6.3 px lines); box x 1010 to 1430, y 130 to 550. The `dw-sweep` group (line and afterglow wedge together) turns about (1220, 340): give it an id and set `svgOrigin` once before any tween. `dw-glow` is hidden in CSS until the sweep starts |
| Smear | inside the screen circle: an ellipse `rx` 26 `ry` 14 centred (1182.9, 225.9), turned -18 degrees, fill Body light, opacity 0 at rest. SCHEMATIC: it stands for "the picture", not for a storm |
| Hook | centred (1239.9, 475.7): one filled comma, 14 px wide and 20 px tall, its tail curling south and west, fill Body light at 85 %. Its east edge (x 1247) stays 8 px clear of Berne's dot |
| Berne on the scope | dot radius 5 px at (1260.6, 475.7), Body light. Label `Berne`, Arial 700 22 px, Body light, left 1270, top 442 (above and east of the dot, inside the screen circle). The label is ours: the scope itself had no map |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `8:40 PM` / `Fort Wayne, Indiana`; hour hand 260 degrees, minute hand 240 degrees (clockwise from 12). Face: `media/drawings/wall-clock.svg` inline or the face of `compositions/g-t1s2-warning.html` |
| Document card | design sheet section 9, the family's lower band: left 96, top 640, 1480 x 222 (bottom 862); Beige polaroid border 10 px; the crop 1460 x 202 inside at (106, 650) |
| Underline | Popfig red 6 px under `for the next 30 to 60 minutes.`: screen x 289 to 806, y 838 to 844 (4 px under the line box; the crop ends at y 852, so it stays on paper) |
| Unlit page | Panel dark at 45 % over the whole crop except the box x 281 to 814, y 805 to 838, fading in over 0.4 s as the underline starts |
| Document source | under the card, right aligned at x 1560, top 876: Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey report, 1965, p. 43` |
The name card and the stamp use the same corner and are never on screen together. The scope's box ends at x 1430 and the card at x 1576: the presenter corner (x >= 1600, y >= 680) stays empty. The ring and the teletype are right of x 1600 but above y 512.

## 4. Must be true in the picture
1. Fort Wayne has a radar ring; South Bend has a dot, its name and `no radar`, and no ring. No other town has a ring.
2. The teletype beside Fort Wayne is unlit from first to last frame: no amber, no pulse, no paper moving. It is the same drawing, place and size as at the end of A1-S12's NORTH view.
3. The name card reads `John Curran`, `observer, Fort Wayne Weather Bureau, 1965`, and credits `his recollection, published by the National Weather Service`. No portrait, no drawn person.
4. The scope carries no map line, no range ring, no county and no compass letter. The only words on it are our label `Berne`, set in our label type, from its spoken word.
5. The smear lights only as the sweep line crosses it (17.26) and is gone by 18.40. Nothing else on the scope fades in and out.
6. The hook is west of Berne's dot, on the same height, 20.7 px from it (5 miles at the scope's scale), and Berne's dot is south and a little east of the scope's centre (bearing about 163 degrees). The hook appears on "hook", Berne on "Berne": neither before its word.
7. The stamp reads `8:40 PM`: hour hand between 8 and 9, minute hand on the 8.
8. The card is the page's own image; nothing on it is retyped. The underline sits under `for the next 30 to 60 minutes.` and under no other words.
9. The sweep never freezes mid turn before the last second: it turns from 14.98 to 31.18 (6.75 turns) and rests pointing west.
10. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680; all text at least 96 px from the sides and 54 px from top and bottom. The crop is on screen 4.2 s (27.46 to 31.67) and changes at 28.66.
11. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `Fort Wayne` · `Weather Bureau · Fort Wayne` · `South Bend` · `no radar` · `John Curran` · `observer, Fort Wayne` / `Weather Bureau, 1965` · `his recollection, published by` / `the National Weather Service` · `Berne` · `WEATHER BUREAU` · `8:40 PM` · `Fort Wayne, Indiana` · `Weather Bureau survey report, 1965, p. 43`. Page words are the image.
Cue words and times are from `audio/a5-s1.words.json`, `a5-s2.words.json` and `a5-s3.words.json` as they stood on 12 Oct 26 (wavs 8.32, 10.87 and 11.98 s). t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A5-S1 -0.43, A5-S2 8.06, A5-S3 18.98) plus the word's time; a segment's first word uses table 5's first sound (0.00, 8.33, 19.48). Retime from the word, never from the seconds. The transcriber writes "eight forty" as words 1 and 2 of A5-S3, "8" and ".40", and Berne as "Bern".
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S1 | 0 | Fort | first sound 0.43 | 0.00 | first frame: ground, the map in NORTH (lines only), Fort Wayne's dot and label |
| 1 | A5-S1 | 1 | Wayne | 0.62 | 0.19 | chip `Weather Bureau · Fort Wayne` fades in (0.3 s, `y: 12` to 0) |
| 2 | A5-S1 | 4 | office | 1.20 | 0.77 | the teletype draws on beside the dot (0.5 s, `strokeDashoffset`), unlit |
| 3 | A5-S1 | 15 | South | 5.16 | 4.73 | South Bend's dot, `South Bend`, then `no radar` 0.15 s later (0.3 s fades) |
| 4 | A5-S1 | 20 | radar | 6.94 | 6.51 | the ring rises round Fort Wayne: outer circle, then inner (0.4 s, `strokeDashoffset`); the sweep line turns one turn (2.4 s, ease none, to 8.91) and rests pointing up |
| 5 | A5-S2 | 0 | A | first sound 0.27 | 8.33 | the office chip fades (0.2 s) |
| 6 | A5-S2 | 5 | John | 1.76 | 9.82 | name card slides in from the left (`x: -660` to 0, 0.6 s, power3.out): name, sub 0.15 s later, small lines 0.15 s after that |
| 7 | A5-S2 | 11 | set | 3.58 | 11.64 | the map, both dots, their labels, the teletype and the ring fade out (0.4 s); the scope draws on at centre right (0.7 s, rim first, then the screen circle, the centre dot fades in), sweep at rest pointing up, wedge hidden |
| 8 | A5-S2 | 20 | Its | 6.92 | 14.98 | the afterglow wedge fades in (0.3 s) and the sweep starts: one tween, rotation 0 to 2430 degrees, 16.2 s, ease none (ends 31.18) |
| 9 | A5-S2 | 30 | picture | 9.20 | 17.26 | the smear lights as the line crosses it (opacity 0 to 0.8 in 0.1 s) |
| 10 | A5-S2 | 31 | faded | 9.54 | 17.60 | the smear fades to 0 (0.7 s, power1.out; gone by 18.30) |
| 11 | A5-S3 | 0 | At | first sound 0.50 | 19.48 | name card leaves to the left (`x: -700`, 0.3 s, power3.in) |
| 12 | A5-S3 | 2 | .40 | 0.88 | 19.86 | clock stamp slides in from the left (`x: -660` to 0, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees onto the 8 |
| 13 | A5-S3 | 8 | hook | 2.54 | 21.52 | the hook fades in on the scope (0.3 s) |
| 14 | A5-S3 | 18 | Bern, | 5.02 | 24.00 | Berne's dot, then its label 0.1 s later (0.3 s fades) |
| 15 | A5-S3 | 26 | take | 8.48 | 27.46 | document card slides in from the right (`x: 660` to 0, 0.7 s, power3.out); the document source fades in after it |
| 16 | A5-S3 | 29 | for | 9.68 | 28.66 | unlit page fades in (0.4 s); the underline draws left to right (0.6 s). Hold to the last frame (31.67) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s01-radar.html` is the only file the builder writes; `data-composition-id="g-a5s01-radar"`; id prefix `fwr-`; root `<div id="fwr-root" ...>` styled through `#fwr-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (brief `mg_specs/briefs/g-a2s14-six.md`) for the NORTH mount, the inlining and the prefixing, the stamp at top left and the paper card in the lower band; the radar ring and the `no radar` label from `compositions/g-a2s01-radar.html`; Fort Wayne's dot, label and unlit teletype from `compositions/g-a1s09-forecasts.html` (its NORTH numbers); the name card's glass plate and type from the built `compositions/g-i1s2-station.html` (`.stn-card`, `.stn-name`, `.stn-sub`). The scope view is this comp's own: `g-a2s03-chain` and `g-a6s07-power` mount the same drawing small.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/drawings/teletype.svg` (DR-01, object box 140 x 140, viewBox -6 -6 152 152), inlined. `media/drawings/teletype-lit.svg` is not used.
- `media/drawings/radar-scope.svg` (DR-02, object box 200 x 200, viewBox -6 -6 212 212, line 4), inlined once.
- `media/docs/survey-p43-840pm-crop.png` (PC-12, 1460 x 202).
- The stamp's clock face: `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136) inline, or the face of `compositions/g-t1s2-warning.html`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s01-radar`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page card (the scan's type beside ours): that is the family's accepted flag (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 7.70 (ring sweep mid turn), 12.00 (map out, scope drawing on) and 17.40 (smear lit, sweep turning) forward and backward and match the frames; the sweep's rotation is one tween from a state set at 0, so a backward seek lands on the same angle. Line 6: Berne's place on the scope, the hook's offset and the smear's bearing are computed from `media/data/points.csv` with the section 2 numbers by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus: the measured distance between the hook's centre and Berne's dot in a frame (20.7 px asked), and whether the 6.3 px scope line reads as the family's weight beside the 3 px map lines it replaces.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map lines in NORTH, Fort Wayne's dot and label, line weights. Then one settled frame per cue: 0.60 (chip), 1.40 (teletype), 5.30 (South Bend, `no radar`), 7.10 (ring up, sweep turning), 9.00 (ring at rest, chip gone), 10.70 (name card), 12.60 (scope alone), 15.60 (sweep and wedge), 17.30 (smear lit under the line), 18.40 (smear gone), 20.60 (stamp at 8:40, name card gone), 22.00 (hook), 24.50 (Berne and its label), 28.30 (card and source), 29.50 (underline complete, unlit page), 31.60 (last frame, sweep at rest).
