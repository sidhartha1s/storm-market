# mg_specs/acts-plan.md: the build plan for acts A1 to A6 and the close Z1 (ep-palm-sunday-1965)

Written 12 Oct 26 from the final `edit_script.md` (112 segments, A1 to Z1), the twelve built comps in `compositions/`, `media/drawings/README.md`, `research/film-shot-log.md`, `provenance.csv` and `00-design-sheet.md`. No brief is written yet; this file says what each brief will cover and what must exist before a builder starts. Paths are relative to the episode folder. E is that folder, W the worktree root.

**The number:** 69 compositions carry the 108 narrated segments (A1 10, A2 13, A3 10, A4 10, A5 13, A6 9, Z1 4; the 69th, g-z1s4b-book for the new line Z1-S4b, was added 12 Oct 26). 5 segments are Paul's clips. A new composition starts only where the picture's world changes (map, chain, list, page, photograph, room); inside one composition every spoken line has its own visible change.

## 1. Rules every brief inherits (stated once)
From the opening round and the lead's list:
1. A start-hidden element is hidden in CSS (`opacity` or `visibility`); its transforms are set in the timeline at 0. A move from rest is a plain `to()`.
2. Text printed on a moving object fades before it leaves the text-safe margin.
3. The root is styled through its id, never a class, and the id is never `root`.
4. While a training film shot is on screen, its own label `Civil defense training film, 1967` is the only chip in the frame.
5. A photograph's label names what the photograph shows, never the town the voice is talking about if they differ.
6. The siren horn is never shown sounding: no sound lines, no pulse, no siren audio.
7. No page crop holds past about 8 seconds without a visible change (underline, lift, dim, a second mark).
8. The study's hidden counties are labelled `County A` and `County B` only. They never share a frame.
9. The teletype room photograph (inventory A3) appears three times in A1 to Z1 and no more: A1-S18 with A1-S19, A2-S21, A3-S8. Every other list frame sits on the canvas gradient.
10. Five graphics in the opening use two type sizes by design (three typed sheets, two page crops with a quote strip); that stays, and the acts' typed sheets and page crops follow them.
From the design sheet, unchanged: paper is their words, glass is our label, a line drawing only where no photograph exists, red means nobody was told, amber means light and time; presenter corner x >= 1600, y >= 680 empty; cues are words (`cue: "<word>"`, `t=` blank until the voice lands).
Added for the acts:
11. A shared drawing is read alone on a test sheet at every size it will be mounted, before any comp mounts it (`learnings/mg.md`, 12 Oct 26).
12. A flash is a stroke or fill change, never a scale pop.
13. A beat count is checked against its spoken window when the brief is written (count times beat length), not at build.
14. Map geometry comes from a file (list 2, base maps). Nothing on a map is placed by eye from a picture.
15. A film cut is mounted in `index.html` by the orchestrator, under its composition; the composition draws the ground with a 4:3 window (x 480 to 1440, y 150 to 870, the cut shown at 1.5x of 640 x 480), the frame and the label. This is the one case where a comp is not opaque over its whole frame.
Rulings on the wave 0 assets (lead, 12 Oct 26):
16. The operations room shot (`media/films/cuts/a14-05-operations-room.mp4`) keeps its desk placards; they are ordinary office placards. It is shown only under the label `Civil defense training film, 1967`; frame toward the wall board where the layout allows. Its first 2 s are placard-free.
17. The announcer shot (`media/films/cuts/a14-09-announcer.mp4`) is 9.44 s, the first angle only. A composition that needs the announcer longer runs the three angle files in sequence (then `media/films/cuts/a14-09b-announcer-shoulder.mp4`, then `media/films/cuts/a14-09c-announcer-microphone.mp4`), never a slowed or looped single shot.
18. The 6:24 PM bulletin crop (`media/docs/survey-p40-624pm-crop.png`) has a sliver of the next line at its bottom edge: its card masks the bottom 4 px (lead, 12 Oct 26: 4 px, not 12; the sliver is file rows 126 to 128 and a 12 px mask cut the third line's descenders).
19. The "excellent" crop (`media/docs/survey-p1-excellent-crop.png`) carries a third line (the toll approaching 200): it stays in frame.
20. Maps: Alto has no dot (it is not in the source) and no map may show Alto. Donaldson and Plymouth sit close: a graphic showing both places its own labels by hand. Inlined map ids get the composition's prefix. Every map graphic's first frame read checks line weight after any zoom.
21. The three log crops of A2-S19 (`media/docs/survey-p39-623pm-crop.png`, `media/docs/survey-p40-624pm-crop.png`, `media/docs/survey-p40-635pm-crop.png`) are 1460 px wide, not 900: their cards are sized from the real file.
22. Coverage holds at every step of the build-up, not only in the last frame (lead, 12 Oct 26, after g-a2s06-headstart left the lower 57 % of the frame black for 12 s; `references/mg-quickref.md` "Frame coverage": no empty block over about a third of the frame for more than about 3 s). Where a brief's reveal order leaves such a block (one card alone, a column or a row that arrives with a later sentence), the builder keeps the brief's last-frame geometry and every cue time, and stages the earlier steps: what is on screen sits centred in the frame (a lone element may be up to 1.5 times its size), then moves to its briefed place over about 0.5 s, starting on the cue of the element that needs the room. Nothing appears before its word, the corner x >= 1600, y >= 680 stays empty at every step, and a hold longer than about 3 s carries a slow push (1.00 to 1.03). The builder's report gives the largest empty block, in per cent and seconds, before and after. The brief's must-be-true list still wins where it is stricter.
23. The cut out of the book ad's black (661.85 s) lands on film: `media/films/cuts/a14-05-operations-room.mp4` from 20.0 s, for the first 3.15 s of g-a4s01-eyes (DESIGN.md "CTA contract"). g-a4s02-countyb has no film.

## 2. Compositions per act
Columns: comp id · segments · kind · what the viewer sees and what changes on each segment · assets (existing path, or an id from list 3) · reuses (built file) · wave (list 5).

### A1 · They saw it coming (10 compositions, 18 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-a1s01-kc | A1-S1 | photo | Teletype machines photograph; clock stamp "FORECASTERS · 11:45 AM EST · Kansas City" lands on the time; the teletype icon lights amber, alone | `media/stills/a4-teletype-room.jpg`, `PT-01`, `DR-01` | `compositions/g-i1s4-states.html` (part B ground and stamp) | 1 |
| g-a1s02-strip | A1-S2, A1-S3 | map | S2: Midwest map, a band drawn from northeastern Missouri to north central Indiana, then a small source card. S3: push in to Indiana, stamp 12:20 PM South Bend, Starke, Laporte and southern Porter light, the 12:20 entry on a paper card with its underline | `BM-2`, `BM-1`, `PC-01` | `compositions/g-t1s2-warning.html` (stamp, page card) | 1 |
| g-a1s04-wire | A1-S4 | photo | The Service A map slide, slow push toward the Midwest; one soft amber pulse over the whole map on "typed out" | `media/stills/a1-service-a-teletype.jpg`, `PT-02` | `compositions/g-i1s4-states.html` (photo ground) | 2 |
| g-a1s05-clocks | A1-S5 | graphic | Left: clock stamp "an office · 11:45 AM EST", amber. Right: the house and a clock face with no hands, which pulses once on "family"; source line | `media/drawings/house.svg`, `DR-09` | `compositions/g-t1s2-warning.html` (clock face) | 1 |
| g-a1s06-low | A1-S6 | map | US map: an L over the northern plains, wind arrows turning; the real Daily Weather Map in a card with its label | `BM-3`, `media/stills/b5-surface-map-1965-04-11.png`, `PT-03` | none | 2 |
| g-a1s07-tracks | A1-S7, A1-S8 | map | S7: the track map brightens west to east; glass labels "supercell: a thunderstorm that rotates", then "single storms lasted up to 4.5 hours"; one arrow "about 45 mph". S8: the map dims, a row of plain county tiles with hand-off marks; marks go grey and three drop out | `media/stills/b7-tornado-track-map.jpg`, `PT-04`, `DR-03` | `compositions/g-i1s4-states.html` (part A) | 2 |
| g-a1s09-forecasts | A1-S9, A1-S10, A1-S11, A1-S12 | graphic | S9: stamp 2:00 PM, Forecast 68 card, strip "ONE OR TWO TORNADOES", three states light. S10: stamp 5:20 PM, Forecast 69 card, two strips in turn, northern Indiana lights. S11: stamp 5:30 PM South Bend, seven counties one by one. S12: Fort Wayne dot, unlit teletype icon, paper card, push in | `BM-2`, `BM-1`, `media/stills/a9-sels-forecast-68.png`, `media/stills/a9-sels-forecast-69.png`, `PT-05`, `PT-06`, `DR-01` | `compositions/g-i1s3-cloud.html` (quote strip) | 2 |
| g-a1s13-chain | A1-S13 | graphic | The intro's chain: Kansas City and South Bend lit with a tick over each; paper card "gave adequate forewarning"; all after the list unlit | `DR-01`, `media/drawings/telephone-lifted.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-i1s9-chain.html` | 1 |
| g-a1s15-offices | A1-S15, A1-S16, A1-S17 | film | S15: film window (operations room); it dims and "inaction" lifts onto a strip. S16: film window (announcer); it empties to the drawn microphone, lamp off, with a paper card. S17: lamp red, dotted link to the house, one window amber, then two paper strips side by side | `FC-01`, `FC-02` (then `FC-02b` and `FC-02c` in that order, only if the announcer window outruns the 9.44 s of `FC-02`), `media/drawings/microphone.svg`, `media/drawings/house.svg`, `media/drawings/house-lit.svg` | `compositions/g-i1s5-onair.html` (lamp), `compositions/g-t1s3-list.html` (microphone and house) | 1 |
| g-a1s18-list | A1-S18, A1-S19 | photo | S18: teletype room photograph, stamp 5:43 PM South Bend, the eight-row list slides in, rows plain. S19: hold; the minute hand starts to move | `media/stills/a3-teletype-operators.jpg`, `PT-07` | `compositions/g-t1s2-warning.html`, `compositions/g-t1s3-list.html` | 2 |

### A2 · One message, one telephone list (13 compositions, 21 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-a2s01-radar | A2-S1, A2-S2 | map | S1: Indiana, drawn echo blobs near Michigan City and west of Knox, three counties light, the 5:43 entry's body on a paper card, underline on "should be on the alert". S2: pull back; radar rings at Chicago, Fort Wayne, Indianapolis; South Bend a bare dot; a telephone line Chicago to South Bend | `BM-1`, `PC-02` | `compositions/g-t1s2-warning.html` (page card) | 2 |
| g-a2s03-chain | A2-S3, A2-S4, A2-S5 | graphic | S3: the chain gains a station in front of South Bend, a radar scope on a solid link. S4: film window (operators); on "office after office" the window goes and the list takes the frame. S5: back to the chain with its clock; an amber arc "at least 10 minutes" grows from 5:43 while light crawls from list to microphone | `DR-02`, `DR-01`, `DR-09`, `FC-03`, `media/drawings/telephone-lifted.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-i1s9-chain.html`, `compositions/g-t1s3-list.html` | 2 |
| g-a2s06-headstart | A2-S6, A2-S7 | graphic | S6: two glass cards with clock faces, "5:45 PM · Starke County" and "about 6:00 PM · Marshall County", each with its own source, each on its own sentence. S7: the amber bar "at least 10 minutes" laid against 2 minutes and against 17 | `DR-09` | `compositions/g-t1s2-warning.html` (clock face) | 1 |
| g-a2s08-first | A2-S8 | map | Indiana: a path from Koontz Lake in Starke County to just south of South Bend; then the toll on glass "10 lives lost · this tornado" | `BM-1`, `DR-03` | `compositions/g-t1s1-toll.html` (toll type) | 2 |
| g-a2s09-countya | A2-S9, A2-S10 | graphic | S9: stamp 5:50 PM, chip "County A · the study's own name for it", a lifted telephone joined to the teletype, light running telephone to teletype; then the p. 20 page as a small card. S10: microphone, lamp dark, beside bare ground; three tornado marks land; the lamp turns red after the third | `media/drawings/telephone-lifted.svg`, `DR-01`, `DR-03`, `media/drawings/microphone.svg`, `media/docs/study-p20-police-crop.png` | `compositions/g-i1s6-page.html`, `compositions/g-i1s9-chain.html` | 2 |
| g-a2s11-backup | A2-S11, A2-S12, A2-S13 | drawing | S11: the house at dusk, a clock by its door "20 minutes after", a quote strip. S12: pull back to County A's chain, microphone and house, with a dotted path from a civil defense desk; a tornado mark crosses first, then the path lights; "too late". S13: through the window to the living room; the screen cuts from programme to idle, then the window light goes. Chip "County A" throughout | `media/drawings/house.svg`, `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/television.svg`, `DR-09`, `DR-03` | `compositions/g-i1s1-house.html` (room, push through the window) | 2 |
| g-a2s14-six | A2-S14 | map | Indiana, stamp 6:00 PM South Bend; St. Joseph, Marshall, Elkhart, Kosciusko light; the 6:00 entry on a paper card with its underline; then tornado marks at Plymouth, Argos and Donaldson only | `BM-1`, `PC-03`, `DR-03` | `compositions/g-t1s2-warning.html` | 1 |
| g-a2s15-old | A2-S15 | page | Study p. 24 crop, "15-30 minutes" underlined; then the words lift onto a strip and the microphone comes in beside it | `PC-04`, `media/drawings/microphone.svg` | `compositions/g-i1s3-cloud.html` | 2 |
| g-a2s16-huffman | A2-S16 | map | Northern Indiana: a dot for Elkhart, name card "Paul Huffman · photographer, The Elkhart Truth"; then a dot for Nappanee, a tornado mark northwest of it, an arrow northeast | `BM-1`, `DR-03` | `compositions/g-i1s2-station.html` (name card) | 2 |
| g-a2s17-funnels | A2-S17, A2-S18 | photo | S17: Huffman's twin funnels, slow push, chip "6:32 PM", credit, place label "Midway Trailer Court"; toll on glass on the third sentence. S18: cut to the Sunnyside photograph in a framed card, its place label, slow push | `media/stills/c1-elkhart-twin-funnel.jpg`, `media/stills/c2-dunlap-sunnyside-damage.jpg`, `PT-08`, `PT-09` | `compositions/g-t1s1-toll.html` | 1 |
| g-a2s19-log | A2-S19 | map | Indiana; three log cards land on their times, 6:23, 6:24, 6:35; Plymouth, Bremen and Goshen light in turn | `BM-1`, `PC-05`, `PC-06`, `PC-07` | `compositions/g-t1s2-warning.html` | 2 |
| g-a2s20-front | A2-S20 | graphic | The chain's front end: house, lifted telephone, police desk, a link to South Bend; light runs toward the Weather Bureau | `media/drawings/house.svg`, `media/drawings/telephone-lifted.svg`, `media/drawings/desk.svg` | `compositions/g-i1s9-chain.html` | 2 |
| g-a2s21-list | A2-S21 | photo | Teletype room photograph, stamp 6:50 PM, the list with its blank ninth row and cursor; then a blank sheet slides in where the next page will come | `media/stills/a3-teletype-operators.jpg`, `PT-07` | `compositions/g-t1s3-list.html` | 2 |

### A3 · The wires (10 compositions, 17 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-a3s01-message | A3-S1, A3-S2, A3-S3 | page | S1: survey p. 40, the 6:50 entry, two underlines as spoken, stamp 6:50 PM, the words on a strip. S2: the television with its station card comes in beside a paper strip of the message's own words. S3: the television gives way to Indiana, its north central part filling amber | `PC-08`, `media/drawings/television.svg`, `BM-1` | `compositions/g-i1s2-station.html` (station card), `compositions/g-i1s3-cloud.html` | 3 |
| g-a3s04-links | A3-S4 | graphic | The chain: the links between South Bend and the list flicker, go dotted, go dark one at a time; the list and all after it lose their light | `DR-01`, `media/drawings/telephone-lifted.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-i1s9-chain.html` | 3 |
| g-a3s05-bremen | A3-S5, A3-S6 | map | S5: stamp 7:10 PM, a red ring on Bremen, a tornado mark just west, the telephone link dark, paper card. S6: one dotted broadcast arc from the microphone toward the town; then a plug and cord under the microphone and under the house | `BM-1`, `DR-03`, `DR-08`, `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-a2s14-six.html` after wave 1 | 3 |
| g-a3s07-calls | A3-S7, A3-S8 | film | S7: film window (desk telephone); then our ground, stamp 7:13 PM and a quote strip. S8: the teletype room photograph with its label on the frame, slow push, strip "the poor observer" | `FC-04`, `media/stills/a3-teletype-operators.jpg`, `PT-07` | `compositions/g-a1s15-offices.html` after wave 1 | 3 |
| g-a3s09-jam | A3-S9 | graphic | A row of dark houses, each with a telephone, lines piling up at one busy mark; then two office desks on the far side, their line stopped by the same mark | `media/drawings/house.svg`, `media/drawings/telephone.svg`, `media/drawings/desk.svg` | none | 3 |
| g-a3s10-towers | A3-S10 | graphic | The list close, the power company's row lit; then 54 small steel towers falling one after another while a count runs to 54, "11 breaks in major lines" above | `DR-04` | `compositions/g-i1s5-onair.html` (lit row) | 3 |
| g-a3s11-onoff | A3-S11 | drawing | The microphone, "a station"; the lamp goes red to dark, then blinks; a quote strip on the second sentence | `media/drawings/microphone.svg` | `compositions/g-i1s5-onair.html` (lamp) | 3 |
| g-a3s12-seven | A3-S12 | graphic | Two clock faces, 7:00 and 7:45, an amber arc between them, "a station", a quote strip. Kept apart from g-a3s11-onoff: the study does not say the two accounts are one station | `DR-09` | `compositions/g-a2s06-headstart.html` after wave 1 | 3 |
| g-a3s13-battery | A3-S13, A3-S14 | drawing | S13: the living room in the evening, window dark, screen idle, the table radio alone with a small amber dial. S14: another evening room: the screen cuts from programme to idle, then the window light goes; name card "Kathy Selzer Miller · Fort Wayne" | `media/drawings/television.svg` | `compositions/g-i1s1-house.html` (living room) | 3 |
| g-a3s15-desks | A3-S15, A3-S16, A3-S17 | drawing | S15: two police desks, a radio arc that goes dotted, then dark; an empty generator outline beside each. S16: a road as one line, a tornado mark moving toward a desk, ticks "30 minutes out", "10", "1". S17: pull back to the chain with its dark links; one dotted amber radio arc between two desks is the only light | `media/drawings/desk.svg`, `DR-05`, `DR-03` | `compositions/g-i1s9-chain.html` | 3 |

### A4 · The desk where it stopped (10 compositions, 15 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-a4s01-eyes | A4-S1 | page | Study p. 21 crop, "with his own eyes" underlined, chip "County B"; beside it the clock stamp sweeps a quarter turn from "about 7:15 PM" to "about 7:30 PM" | `PC-09`, `DR-09` | `compositions/g-i1s6-page.html` | 3 |
| g-a4s02-countyb | A4-S2, A4-S3, A4-S4, A4-S5 | graphic | S2: a plain drawn map, a river line, two marks at its bank, then a tornado mark from the west; County B's chain waits unlit to the east. S3: the chain comes up desk by desk, the civil defense desk amber. S4: a dotted radio arc to the police desk, the light crosses, stamp "about 7:30 PM". S5: a grey ghost of the light runs on ahead, never amber | `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg`, `DR-03`, `DR-09` | `compositions/g-i1s9-chain.html` | 1 |
| g-a4s06-died | A4-S6 | page | Study p. 22 crop, one sentence underlined in red as spoken; beside it the chain: the ghost fades, the light stays on the police desk, a red stop mark lands; hold | `PC-10`, `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-a4s02-countyb.html` after wave 1, `compositions/g-i1s6-page.html` | 3 |
| g-a4s08-chief | A4-S8 | page | Study p. 22 crop, "I don't like to panic them." underlined; the words lift onto a strip; the underline moves to "might panic unnecessarily"; chip "County B" | `PC-11` | `compositions/g-i1s7-sheriff.html` (two underlines, strip swap) | 3 |
| g-a4s09-clock | A4-S9, A4-S10 | graphic | S9: County B's chain held on the police desk and its stop mark; the clock runs "about 7:30 PM" to "8:07 PM", an amber arc "the study says: about 35 minutes". S10: every light goes out, the police desk last; the sheriff's words return as a small strip | `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg`, `DR-09`, `media/docs/study-p22-sheriff-crop.png` | `compositions/g-a4s02-countyb.html` after wave 1 | 3 |
| g-a4s11-farend | A4-S11, A4-S12 | graphic | S11: a chain of three, police desk amber, a dotted link that never lights, the microphone dark; chip "a station · county not given in the study"; the station's words on a strip. S12: the chip and desk leave; microphone and house with one link, and two dotted grey ways in, a horn on a pole and a police car; the car blinks amber once, the horn stays grey | `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg`, `DR-06`, `DR-07` | `compositions/g-i1s9-chain.html` | 3 |
| g-a4s13-duty | A4-S13 | graphic | The list close: light on the city police row, then on the stations row; a strip with the chief's words on the forecast; the strip changes; every row but the stations row goes plain | none | `compositions/g-i1s10-list.html` | 3 |
| g-a4s14-eight | A4-S14 | graphic | Eight plain squares, no names: seven fill amber on "seven", the eighth takes a red outline on "one"; source line | none | none | 3 |
| g-a4s15-chain | A4-S15 | graphic | The whole chain as in I1-S9: three stations lit, the desk with its stop mark, microphone and house dark; a quote strip on the second sentence | `DR-01`, `media/drawings/telephone-lifted.svg`, `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-i1s9-chain.html` | 3 |
| g-a4s16-fortwayne | A4-S16 | map | Indiana: South Bend's dot dims, Fort Wayne's lights with the teletype icon and a paper strip coming out; then a tornado mark passes a town dot and a message card lands behind it | `BM-1`, `DR-01`, `DR-03` | `compositions/g-a2s14-six.html` after wave 1 | 3 |

### A5 · Warnings for storms already gone (13 compositions, 20 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-a5s01-radar | A5-S1, A5-S2, A5-S3 | map | S1: Indiana, Fort Wayne's dot and the unlit teletype of A1-S12; a radar ring rises round Fort Wayne, none at South Bend. S2: name card John Curran; push into the ring, which becomes a large drawn scope with a sweep and a fading smear. S3: stamp 8:40 PM Fort Wayne, a hook west of a dot labelled Berne, then the 8:40 entry on a paper card | `BM-1`, `DR-01`, `DR-02`, `PC-12` | `compositions/g-i1s2-station.html` (name card) | 4 |
| g-a5s04-berne | A5-S4, A5-S5 | map | S4: the Indiana and Ohio line from true positions; a tornado mark at Linn Grove "8:40 PM" moves to the line "near 8:52 PM"; chip "John Curran's recollection" under the first sentence only. S5: a long amber bar "warning: the next 30 to 60 minutes" over a short red bar "12 minutes" | `BM-1`, `DR-03` | `compositions/g-a2s14-six.html` after wave 1 | 4 |
| g-a5s06-hold | A5-S6 | photo | The 1947 teletype room photograph, stamp 9:00 PM Fort Wayne; the typed line lifts onto a strip as it is said | `media/stills/a5-teletype-room-1947.jpg`, `PT-10` | `compositions/g-t1s2-warning.html` | 4 |
| g-a5s07-marion | A5-S7, A5-S8 | map | S7: central and eastern Indiana, one storm path through Marion to Linn Grove and the line; stamp 9:20 PM and the 9:20 entry on a paper card. S8: the map dims; a wall clock stopped at 8:10 beside the stamp at 9:20; a strip between them | `BM-1`, `PC-13`, `DR-09` | `compositions/g-a2s06-headstart.html` after wave 1 | 4 |
| g-a5s09-alto | A5-S9 | photo | The tornado photograph with its caption, cut on "twenty five" to the Alto aerial with its label; toll on glass | `media/stills/c6-alto-tornado-cover.jpg`, `media/stills/c5-alto-aerial-damage.jpg`, `PT-11`, `PT-12` | `compositions/g-t1s1-toll.html` | 4 |
| g-a5s10-alert | A5-S10, A5-S11 | map | S10: Wells, Adams, Blackford, Jay light with "9:20 PM · on alert"; then the track across three of them to the line, "8:52 PM · already in Ohio". S11: film window (a telephone call) over the map; then the window goes and stamp 9:07 PM lands beside Marion's dot | `BM-1`, `FC-05`, `DR-03` | `compositions/g-a1s15-offices.html` after wave 1 | 4 |
| g-a5s12-spotters | A5-S12 | graphic | The chain's front end: a town, a telephone, a dotted link to the Weather Bureau, nothing between; a strip with Curran's words | `media/drawings/house.svg`, `media/drawings/telephone.svg`, `media/drawings/desk.svg` | `compositions/g-i1s9-chain.html` | 4 |
| g-a5s14-noissue | A5-S14 | page | Survey p. 44 crop, one line underlined in red; the frame round the page dims almost to black while the line stays lit; stamp 9:30 PM | `PC-14`, `DR-09` | `compositions/g-i1s6-page.html` | 4 |
| g-a5s15-dark | A5-S15 | drawing | Three houses at night, every window dark; one leaning steel tower behind; small line "John Curran's recollection, not a log" | `media/drawings/house.svg`, `DR-04` | none | 4 |
| g-a5s16-toledo | A5-S16, A5-S17 | map | S16: Ohio with a dot for Toledo, stamp "9:30 PM · Toledo, Ohio", chip "Toledo had its own Weather Bureau office", then the toll on glass. S17: Columbus appears, a dotted line between the two, chip "Columbus weather office · a mention, ten minutes before" | `BM-2`, `DR-09` | `compositions/g-t1s1-toll.html` | 4 |
| g-a5s18-curran | A5-S18, A5-S19 | drawing | S18: Curran's name card; a wall clock at 4:00 PM, the house with a dark window, the clock at 10:30 PM and the window lit. S19: a dark room, two teletypes lit amber, one cord along the floor, out of the door, down a hall to a box "FAA Flight Service Station" | `DR-09`, `DR-01`, `media/drawings/house.svg`, `media/drawings/house-lit.svg` | `compositions/g-i1s2-station.html` (name card) | 4 |
| g-a5s20-team | A5-S20 | page | Date label "April 12, 1965"; the memo page crop with its underline; then a tighter crop of printed p. 1, "excellent" underlined | `PC-15`, `PC-16` | `compositions/g-i1s6-page.html` | 4 |
| g-a5s21-end | A5-S21 | graphic | The end of the chain: the list, the dark microphone, the house; a slow push that holds on the microphone | `media/drawings/microphone.svg`, `media/drawings/house.svg` | `compositions/g-t1s3-list.html` (Everything state) | 4 |

### A6 · What they fixed, and what they didn't (9 compositions, 12 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-a6s01-recs | A6-S1 | page | The recommendations page whole, date label "May 2, 1965", name card "P. H. Kutschenreuter · chairman, Weather Bureau survey team"; then a tight crop on recommendation 1 | `PC-17`, `PC-18` | `compositions/g-i1s6-page.html`, `compositions/g-i1s2-station.html` (name card) | 5 |
| g-a6s02-floorplan | A6-S2 | graphic | A floor plan: a teletype in one room, three doors, the announcer's booth with the microphone; then a bell mark on the teletype, a line through the doors to a lamp by the microphone, the lamp amber; a small paper card | `DR-01`, `media/drawings/microphone.svg` | none | 5 |
| g-a6s03-announcer | A6-S3, A6-S4 | graphic | S3: the hook tail's frame, list, blank row, microphone and house; this time the microphone is lit, the house dark. S4: push to the microphone and its lamp; the lamp goes back to an empty outline, chip "when the researchers came"; then four dark marks in a row | `media/drawings/microphone.svg`, `media/drawings/house.svg`, `media/drawings/desk.svg`, `media/drawings/telephone.svg` | `compositions/g-t1s3-list.html` | 5 |
| g-a6s05-wires | A6-S5, A6-S6 | graphic | S5: the chain; a solid link drawn from the teletype straight to a desk, twice, both desks light. S6: the dark telephone links of A3-S4 return; an amber radio arc from office to office; a small paper card for recommendation 7 | `DR-01`, `media/drawings/desk.svg` | `compositions/g-i1s9-chain.html` | 5 |
| g-a6s07-power | A6-S7 | drawing | A dark drawn office, no place label; a generator mark comes in and the room lights. Then the map: a small screen at South Bend's dot joined by one line to another city's radar ring; paper cards for recommendations 8 and 5 | `DR-05`, `DR-02`, `BM-2` | none | 5 |
| g-a6s08-spotters | A6-S8 | graphic | The front end of A5-S12: spotter marks drawn one by one between town and Weather Bureau, each lights; a paper card for recommendation 3; then "SKYWARN" on glass with its source | `media/drawings/house.svg`, `media/drawings/telephone.svg`, `media/drawings/desk.svg` | `compositions/g-i1s9-chain.html` | 5 |
| g-a6s09-third | A6-S9 | graphic | A circle in three parts, one fills amber on "a third"; then two generator marks fill under two desks (the outlines of A3-S15) | `DR-05`, `media/drawings/desk.svg` | none | 5 |
| g-a6s10-watch | A6-S10 | graphic | The microphone, lamp lit, two paper strips "TORNADO FORECAST" and "TORNADO WARNING"; then on glass "TORNADO FORECAST" struck through and "TORNADO WATCH" | `media/drawings/microphone.svg` | `compositions/g-i1s5-onair.html` (lamp) | 5 |
| g-a6s11-sirens | A6-S11, A6-S12 | graphic | S11: a paper card with the researchers' sentence; beside it a horn on a pole, outline only. S12: the film window (a siren horn, silent) where the drawing stood; then the window goes and a quote strip comes in | `DR-06`, `FC-06` | `compositions/g-a1s15-offices.html` after wave 1 | 5 |

### Z1 · Close (4 compositions, 5 segments)
| Comp | Segments | Kind | Viewer sees, and the change per segment | Assets | Reuses | Wave |
|---|---|---|---|---|---|---|
| g-z1s02-row | Z1-S2, Z1-S3 | graphic | S2: the list and its blank ninth row, nothing typed; the chain comes up under it with the police desk and its stop mark. S3: a cell tower rises behind the house, a cell phone beside it; light runs from the Weather Bureau desk to the tower and the phone, past the list; the house window turns amber for the first time | `media/drawings/desk.svg`, `media/drawings/house.svg`, `media/drawings/house-lit.svg`, `media/drawings/microphone.svg`, `DR-10`, `DR-11` | `compositions/g-t1s3-list.html`, `compositions/g-i1s9-chain.html` | 5 |
| g-z1s04-drill | Z1-S4 | map | Indiana: every county lights amber in one sweep from the Weather Bureau's dot; label "statewide tornado drill · each spring"; no date | `BM-1` | `compositions/g-a2s14-six.html` after wave 1 | 5 |
| g-z1s05-title | Z1-S5 | graphic | The channel title card under the signature footnote; it is the outro | none | none (copy `library/inhouse/outro-brand.html` from W) | 5 |
| g-z1s4b-book | Z1-S4b | graphic | Added 12 Oct 26 for the new line; it plays between g-z1s04-drill and g-z1s05-title. The book's front cover standing on the channel ground, shown whole, with the one line `first link in the description` under it; no price, no offer, no other text | `media/stills/z1-book-cover.png` (720 x 1080; the builder stages it from `landing/assets/cover.png`, 1024 x 1536, which stays untouched) | none | 5 |

## 3. Assets (made in wave 0, 12 Oct 26; every row names the file on disk)
Checked 12 Oct 26 with a folder listing, `ffprobe` on every cut and the pixel size of every crop. A brief names the file path from these rows, never an id alone. A row marked "ordered" is checked again before a brief uses it.

### 3a. Drawings (11, plus 4 state files), in `media/drawings/`
Mount rules, classes and the test sheet are in `media/drawings/README.md` ("Drawings for the acts"); that file wins over any number here. The object box starts at (0, 0) and the viewBox adds 6 units a side. A state file shares its viewBox and classes with its base file: a picture mount swaps the file, an inline mount tweens the classed part. The files carry classes only; a comp adds ids under its own prefix.
| Id | File | State file | Shows, and the part a comp changes | Object box | viewBox (x y w h) | Line (units) | Needed by |
|---|---|---|---|---|---|---|---|
| DR-01 | `media/drawings/teletype.svg` (paper unlit) | `media/drawings/teletype-lit.svg` (paper Amber 2, bars Caption dark) | Body, keyboard slab, a paper strip with three typed bars. `dw-lamp` paper fill, `dw-type` bars stroke | 140 x 140 | -6 -6 152 152 | 4 | a1s01, a1s09, a1s13, a2s03, a2s09, a3s04, a4s15, a4s16, a5s01, a5s18, a6s02, a6s05 |
| DR-02 | `media/drawings/radar-scope.svg` | none | A round scope with a rim, a centre dot, one sweep line and an amber afterglow wedge behind the sweep; no map lines. `dw-sweep` turns about (100, 100); `dw-glow` may be hidden | 200 x 200 | -6 -6 212 212 | 4 | a2s03, a5s01, a6s07 |
| DR-03 | `media/drawings/tornado-mark.svg` | none | A map mark: three bars of falling width over a point. Group stroke only, never red | 60 x 80 | -6 -6 72 92 | 6 | a1s07, a2s08, a2s09, a2s11, a2s14, a2s16, a3s05, a3s15, a4s02, a4s16, a5s04, a5s10 |
| DR-04 | `media/drawings/steel-tower.svg` | none | A lattice transmission tower. The whole group tips about the base centre (40, 160) | 80 x 160 | -6 -6 92 172 | 4, braces 3 | a3s10, a5s15 |
| DR-05 | `media/drawings/generator.svg` (outline: the one that is not there) | `media/drawings/generator-filled.svg` (box and housing Amber 2) | A box on skids with a round housing, one pipe and a bolt mark. `dw-lamp` fills, `dw-ink` strokes | 120 x 80 | -6 -6 132 92 | 4, bolt and hub 3 | a3s15, a6s07, a6s09 |
| DR-06 | `media/drawings/horn-pole.svg` | none | A pole and one flared horn, outline. Group stroke only; no sound lines, ever | 80 x 220 | -6 -6 92 232 | 4 | a4s11, a6s11 |
| DR-07 | `media/drawings/police-car.svg` | none | A 1960s sedan, side elevation, one roof speaker, no markings. An amber blink is the `dw-body` fill | 240 x 90, speaker up to y -6 | -6 -14 252 114 | 4, windows and speaker 3 | a4s11 |
| DR-08 | `media/drawings/plug-cord.svg` | none | A two-pin plug and a short cord. Group stroke | 60 x 40 | -6 -6 72 52 | 4 | a3s05 |
| DR-09 | `media/drawings/wall-clock.svg` (both hands at 12) | `media/drawings/wall-clock-nohands.svg` | Circle, twelve ticks, centre dot, two hands. `dw-hour` and `dw-minute` turn about (62, 62) | 124 x 124 | -6 -6 136 136 | 4, ticks 3, hands 5 | a1s05, a2s03, a2s06, a2s11, a3s12, a4s01, a4s02, a4s09, a5s07, a5s14, a5s16, a5s18 |
| DR-10 | `media/drawings/cell-phone.svg` (screen dark) | `media/drawings/cell-phone-lit.svg` (screen Amber 2) | A plain slab phone, front elevation. `dw-lamp` screen fill | 60 x 110 | -6 -6 72 122 | 4, screen and button 3 | z1s02 |
| DR-11 | `media/drawings/cell-tower.svg` | none | A mast with three panel antennas. Group stroke | 60 x 240 | -6 -6 72 252 | 4, arms 3 | z1s02 |

What a brief carries from the README for these:
- Line weight by size: keep the file's weight between about half and twice the object box. Smaller, set `stroke-width` on the `dw-...` group so a line stays near 2 px (the 54 towers of A3-S10 at about 26 px wide: `stroke-width="6"`, 4.5 on the two brace paths). Larger, thin it so a line stays near 6 px (the scope of A5-S2 at 420 px wide: `stroke-width="3"`).
- Light ground (rooms, paper): the group's `stroke` is `#15202b`, and every `dw-body` and unlit `dw-lamp` fill takes the ground's colour.
- Turning parts (`dw-sweep`, `dw-hour`, `dw-minute`, the tower) carry no transform in the file. Inline, give the part an id and tween `rotation` with `svgOrigin` set once before any tween. Clock angles are clockwise degrees from 12.
- Dots drawn as zero-length round-capped lines (the clock hub, the car's wheel hubs) and the scope's wedge fade in; they take no draw-on.
- Two things the builder added to this plan's wording, both kept: the scope's rim and afterglow wedge (a bare circle with one line reads as a clock face), and the generator's bolt mark.

### 3b. Base maps (3), in `media/maps/`
Built by `media/maps/build_maps.py` from two US Census files in `media/data/` (`cb_2023_us_county_500k.zip`, `2023_Gaz_place_national.zip`; town table `media/data/points.csv`). Projection, ids, the points table, colours and line weights are in `media/maps/README.md`; that file wins over any number here. All three files share one coordinate space (one unit is one pixel of `compositions/g-i1s2-station.html`), so a push from one map into another is a camera move. Today's county lines stand in for 1965. The files carry no labels: a composition sets type.
| Id | File | viewBox (x y w h) | Largest fit inside the text-safe area | Units with an id | Town dots | Needed by |
|---|---|---|---|---|---|---|
| BM-1 | `media/maps/indiana-counties.svg` | 96 100 664 880 | scale 1.1045, 733 x 972 px, left 593, top 54 | 92 counties `co-in-<name>`, Indiana's outline `st-in`, neighbours `st-il st-mi st-oh st-ky` cut to the window | 21: South Bend, Michigan City, Knox, Koontz Lake, Plymouth, Argos, Donaldson, Bremen, Goshen, Elkhart, Dunlap, Nappanee, Fort Wayne, Berne, Linn Grove, Marion, Indianapolis, Kokomo, Russiaville, Greentown, Chicago | a1s02, a1s09, a2s01, a2s08, a2s14, a2s16, a2s19, a3s01, a3s05, a4s16, a5s01, a5s04, a5s07, a5s10, z1s04 |
| BM-2 | `media/maps/midwest-states.svg` | -980 -1280 2220 2560 | scale 0.3797, 843 x 972 px, left 539, top 54 | 9 states: `st-mo st-ia st-il st-wi st-in st-mi st-oh st-ky st-mn` | 7: Kansas City, Chicago, South Bend, Fort Wayne, Indianapolis, Toledo, Columbus | a1s02, a1s09, a5s16, a6s07 |
| BM-3 | `media/maps/us-states.svg` | -4490 -1300 7470 4720 | scale 0.2059, 1538 x 972 px, left 191, top 54 | 48 states and DC, `st-<postal code>`; the L of A1-S6 sits over `st-nd st-sd st-mn` | none | a1s06 |

What a brief carries for every map graphic:
- **Mount box.** To match the built station graphic, BM-1 mounts at left 96, top 100, 664 x 880 px (one unit per pixel). The "largest fit" column is the most a map can fill inside the margins, centred; a composition with a card beside the map picks its own box and keeps the aspect. From the BM-2 fit to the BM-1 fit is a push of 2.909 times; from BM-3 to BM-2, 1.844 times.
- **Ids.** A town is `pt-<name>` (a group holding one circle). A composition that inlines map paths puts its own prefix on every id. Two pairs read alike: `co-in-marion` is Marion County (Indianapolis) while the city of Marion is `pt-marion` in `co-in-grant`; `co-in-knox` is a county in the south-west while the town of Knox is `pt-knox` in `co-in-starke`.
- **Alto has no dot.** It is not in the source file, none was guessed, and no map may show Alto. The photograph of A5-S9 keeps its own label; nothing marks the place on a map.
- **Donaldson and Plymouth sit close:** 16.0 units apart, 17.7 px at the largest fit. A graphic that shows both (A2-S14) places their two labels by hand and reads them in a frame.
- **Line weight after any zoom.** Every path carries `vector-effect="non-scaling-stroke"`, so the weights are screen pixels at any mount size. Whether a CSS scale on a wrapper (a camera push) also leaves the weight alone is not yet checked: every map graphic's first frame read checks line weight at both ends of each zoom.
- **Lighting.** A county or state lights by its fill (a flash is a fill change). `st-in` on BM-1 has no fill, so lit counties show through; "all of Indiana" on BM-1 is the 92 counties (Z1-S4), on BM-2 it is `st-in`.
- **Southern Porter** (A1-S3): `co-in-porter` runs y 182.4 to 272.9 in map units; the schematic split is its mid line, y 227.6.
- **Clipping.** BM-1's neighbour outlines are cut 30 units outside its viewBox; a composition that copies them into a wider SVG clips them to the window x 96 to 760.

### 3c. Page crops (18), in `media/docs/`
Cut from 300 dpi page images in the same folder; each has a `provenance.csv` row with its crop box in page pixels. Printed survey log pages sit at PDF page = printed page + 28. Printed p. 1 is PDF p. 7 and printed p. 2 is PDF p. 8; the memo is PDF p. 3. Study printed page = PDF page less 2. Page images made in wave 0: `media/docs/survey-pdf-03-orig.png`, `media/docs/survey-pdf-07-orig.png`, `media/docs/survey-pdf-08-orig.png`, `media/docs/survey-pdf-65-orig.png`, `media/docs/survey-pdf-68-orig.png`, `media/docs/survey-pdf-71-orig.png`, `media/docs/survey-pdf-72-orig.png`, `media/docs/study-pdf-23-orig.png`, `media/docs/study-pdf-26-orig.png`.
| Id | File | Size (px) | Printed page | What the file holds | Ruling or note for the brief | Needed by |
|---|---|---|---|---|---|---|
| PC-01 | `media/docs/survey-p37-1220pm-crop.png` | 1460 x 353 | survey p. 37 | The 12:20 PM entry, "Issued at 12:20 PM EST" to "Starke and southern Porter and Laporte Counties.", 9 lines | Nine lines: the card shows them all, the underline finds "several tornadoes are expected" | a1s02 |
| PC-02 | `media/docs/survey-p39-radar-crop.png` | 1460 x 142 | survey p. 39 | 4 lines, "Radar indicates" to "should be on the alert" | none | a2s01 |
| PC-03 | `media/docs/survey-p39-600pm-crop.png` | 1460 x 283 | survey p. 39 | The 6:00 PM entry, "Issued at 6:00 PM EST." to "during the next 30 to 60 minutes.", 7 lines | none | a2s14 |
| PC-04 | `media/docs/study-p24-media-crop.png` | 1460 x 434 | study p. 24 | 8 lines, from "Media personnel typically commented as follows:" through the "15-30 minutes" quote | The manpower quote sits between the heading and the spoken quote: it is dimmed with the unlit page, never underlined | a2s15 |
| PC-05 | `media/docs/survey-p39-623pm-crop.png` | 1460 x 90 | survey p. 39 | The 6:23 PM entry: time line and first line | 1460 px wide, not 900: the card is sized from the file | a2s19 |
| PC-06 | `media/docs/survey-p40-624pm-crop.png` | 1460 x 129 | survey p. 40 | The 6:24 PM entry: time line and 2 lines naming Bremen | 1460 px wide, not 900. A sliver of the next line shows at the bottom edge: the card masks the bottom 4 px (rule 18) | a2s19 |
| PC-07 | `media/docs/survey-p40-635pm-crop.png` | 1460 x 128 | survey p. 40 | The 6:35 PM entry: time line and 2 lines naming Goshen | 1460 px wide, not 900: the card is sized from the file | a2s19 |
| PC-08 | `media/docs/survey-p40-650pm-crop.png` | 1460 x 240 | survey p. 40 | The 6:50 PM entry whole, 6 lines | none | a3s01 |
| PC-09 | `media/docs/study-p21-eyes-crop.png` | 1460 x 299 | study p. 21 | 4 lines: "with his own eyes" (lines 2 and 3) with a line above and below | The crop prints the study's code "County B" once; it matches the chip | a4s01 |
| PC-10 | `media/docs/study-p22-died-crop.png` | 1460 x 225 | study p. 22 | The page's first three lines, ending "The information died with the police." | Names no county | a4s06 |
| PC-11 | `media/docs/study-p22-chief-crop.png` | 1460 x 529 | study p. 22 | "The Chief of Police was afraid..." and both paragraphs of his quote, to "they panic right now.", 10 lines | Names no county | a4s08 |
| PC-12 | `media/docs/survey-p43-840pm-crop.png` | 1460 x 202 | survey p. 43 | The 8:40 PM Fort Wayne entry whole, 4 lines | none | a5s01 |
| PC-13 | `media/docs/survey-p43-920pm-crop.png` | 1460 x 377 | survey p. 43 | The 9:20 PM entry whole, 9 lines | none | a5s07 |
| PC-14 | `media/docs/survey-p44-nowarn-crop.png` | 1460 x 591 | survey p. 44 | "No issuances between 9:30 PM EST and 10:30 PM EST due to power failure.", the page heading above it and the whole 10:45 PM entry below | The page has no entry above the line: the heading is what sits above it | a5s14 |
| PC-15 | `media/docs/survey-memo-p3-crop.png` | 1460 x 868 | memo (PDF p. 3) | Memo heading, the date May 2, 1965 and the first paragraph | The memo's own date is May 2; the label "April 12, 1965" is ours and sits on glass | a5s20 |
| PC-16 | `media/docs/survey-p1-excellent-crop.png` | 1460 x 169 | survey p. 1 | 3 whole lines holding "were excellent." | The third line (the toll approaching 200) stays in frame: the page is skewed and a rectangle cannot hold two lines alone. Only "excellent" is underlined | a5s20 |
| PC-17 | `media/docs/survey-p2-recs-page.png` | 835 x 1080 | survey p. 2 | The recommendations page whole | none | a6s01 |
| PC-18 | `media/docs/survey-p2-rec1-crop.png` | 1460 x 290 | survey p. 2 | Recommendation 1 alone, 7 lines | none | a6s01 |
On disk from the opening and reused as they are: `media/docs/study-p20-police-crop.png` (1460 x 647; a2s09), `media/docs/study-p22-sheriff-crop.png` (1460 x 642; a4s09).

Sizing a card from the file: the card is the crop at one scale s, so it is 1460 x s wide and the file's height x s tall, on the Beige border of design sheet section 9. The three log cards of A2-S19 share a frame with the map, so their brief picks s from the layout and proves the typed line clears the 19 px floor at that s; if it does not, the card in voice sits large and the earlier ones step back.

### 3d. Film cuts (8 files for 6 shots), in `media/films/cuts/`
All from `media/films/a14-eoc-radef.mp4` (inventory A14). Lengths are `ffprobe` on the files, 12 Oct 26. Every file is 640 x 480 with no audio stream, cut 0.3 s inside each logged edge, and has a `provenance.csv` row.
| Id | Shot | File | Length (s) | Source in to out (s) | In frame | Needed by |
|---|---|---|---|---|---|---|
| FC-01 | 14-05 | `media/films/cuts/a14-05-operations-room.mp4` | 31.53 | 74.1 to 105.6 | Wide of the operations room, slow zoom out, a man writing on the wall board. Ordinary desk placards are in frame from about 2 s to the end | a1s15 |
| FC-02 | 14-09, first angle | `media/films/cuts/a14-09-announcer.mp4` | 9.44 | 384.2 to 393.65 | The announcer reading a sheet at a microphone, front on | a1s15 |
| FC-02b | 14-09, second angle (ordered; on disk at this check) | `media/films/cuts/a14-09b-announcer-shoulder.mp4` | 7.17 | 393.95 to 401.12 | The announcer from behind, over the shoulder; the sheet shows no readable text | a1s15 |
| FC-02c | 14-09, third angle (ordered; on disk at this check) | `media/films/cuts/a14-09c-announcer-microphone.mp4` | 7.84 | 401.46 to 409.30 | Close on the microphone, the announcer's ear and glasses | a1s15 |
| FC-03 | 14-13 | `media/films/cuts/a14-13-operators.mp4` | 15.21 | 701.8 to 717.0 | Women in headsets in booths on telephones; one continuous pan | a2s03 |
| FC-04 | 14-10 | `media/films/cuts/a14-10-desk-telephone.mp4` | 15.72 | 468.3 to 484.0 | A man at a desk with a black rotary telephone; a second man holds it by the end | a3s07 |
| FC-05 | 14-08 | `media/films/cuts/a14-08-telephone-call.mp4` | 4.17 | 259.8 to 264.0 | Close on a man talking on a black telephone, a wall map behind | a5s10 |
| FC-06 | 14-01 | `media/films/cuts/a14-01-siren-horn.mp4` | 11.71 | 33.6 to 45.3 | A siren horn on a pole in tree branches, static then a slow push | a6s11 |
Rulings on the cuts:
- **FC-01 keeps its desk placards** (ordinary office placards: HEALTH & MEDICAL, RESOURCES, EMERGENCY INFORMATION, MAYOR). It is shown only under the label `Civil defense training film, 1967`; frame toward the wall board where the layout allows. Its first 2 s are placard-free.
- **FC-02 is 9.44 s, the first angle only.** A composition that needs the announcer longer runs the three angle files in sequence (FC-02, FC-02b, FC-02c: 24.46 s in all), never a slowed or looped single shot. FC-02b and FC-02c were ordered after the first six and are used only when the window outruns FC-02; a brief checks both files exist before it names them.
- A film window never runs past its file's length. Section 7 holds each window's length against the voice.

### 3e. Photograph treatments (12): nothing to cut, the rule each brief follows
A picture under 1000 px wide sits in a card at its own size. A picture at 1000 px or more may fill the frame only if cover loses under 35 % of it; otherwise it is fitted to the frame's height over a blurred, dimmed copy of itself.
| Id | File | Size (px) | Label on screen | How it sits | Needed by |
|---|---|---|---|---|---|
| PT-01 | `media/stills/a4-teletype-room.jpg` | 1456 x 1080 | "Weather Bureau teletypewriters, about 1955 · NOAA" | cover, `.dim`, no card over a face | a1s01 |
| PT-02 | `media/stills/a1-service-a-teletype.jpg` | 1668 x 1212 | "Service A teletypewriter system, about 1960 · NOAA" | cover, slow push toward the Midwest | a1s04 |
| PT-03 | `media/stills/b5-surface-map-1965-04-11.png` | 1503 x 1200 | "Surface weather map · 1:00 AM EST" | in a card, shrunk to 950 x 758, never enlarged | a1s06 |
| PT-04 | `media/stills/b7-tornado-track-map.jpg` | 1396 x 1046 | "Courtesy: Dr. Russell Schneider, SPC" | fitted by height as in the intro (x 251 to 1549) | a1s07 |
| PT-05 | `media/stills/a9-sels-forecast-68.png` | 702 x 914 | "Severe Weather Forecast 68 · Weather Bureau" | card at its own size | a1s09 |
| PT-06 | `media/stills/a9-sels-forecast-69.png` | 672 x 872 | "Severe Weather Forecast 69 · Weather Bureau" | card at its own size | a1s09 |
| PT-07 | `media/stills/a3-teletype-operators.jpg` | 1370 x 1080 | "Weather Bureau Communications Center, about 1955 · NOAA"; in a3s07 the note's own label "Weather Bureau teletype room, about 1955" on the frame instead, one label only | cover, `object-position:50% 40%`, three uses in all | a1s18, a2s21, a3s07 |
| PT-08 | `media/stills/c1-elkhart-twin-funnel.jpg` | 1188 x 1068 | "Midway Trailer Court"; credit "Paul Huffman, The Elkhart Truth · April 11, 1965"; chip "6:32 PM" | fitted to height over a blurred copy (list 6, item 9) | a2s17 |
| PT-09 | `media/stills/c2-dunlap-sunnyside-damage.jpg` | 800 x 647 | "Sunnyside · Dunlap, Indiana" | framed card at its own size, crop inside the faded edge, slow push inside the card | a2s17 |
| PT-10 | `media/stills/a5-teletype-room-1947.jpg` | 1820 x 1220 | "Teletypes and operator, about 1947 · NOAA" | cover, `.dim` | a5s06 |
| PT-11 | `media/stills/c6-alto-tornado-cover.jpg` | 1414 x 1080 | "Tornado over Alto, toward Kokomo · Kokomo Morning Times, April 16, 1965" | cover | a5s09 |
| PT-12 | `media/stills/c5-alto-aerial-damage.jpg` | 1543 x 1080 | "Alto, Indiana" | cover | a5s09 |

## 4. Paul's five clips (full-frame video, not compositions)
Mounted as `ins-paul-<n>` in `index.html` with the logo over the Flow mark (`references/mg-quickref.md` "Paul on screen"). The hook's clip is `ins-paul-1`, so these run 2 to 6.
| Segment | Clip | On-screen label the Picture note asks for |
|---|---|---|
| A1-S14 | ins-paul-2 | none |
| A3-S18 | ins-paul-3 | none; cut to the book ad on his last word |
| A4-S7 | ins-paul-4 | chip "County B" for the whole clip |
| A5-S13 | ins-paul-5 | none |
| Z1-S1 | ins-paul-6 | none |
The book ad sits between A3-S18 and A4-S1. It is mounted from `config.yaml channel.cta` and is not built here.

## 5. Build order
At most five builders at a time. A builder owns whole files; no file is in two builders' hands. Assets first; then the base of each family, read at full size before the family copies it; then the acts in order.
| Wave | Builder | Files |
|---|---|---|
| 0 (assets) | 0-a drawings | DR-01 to DR-11, the test sheet, the README rows |
| 0 | 0-b maps | BM-1, BM-2, BM-3 and `media/maps/README.md` (BM-1 starts when list 6 items 1 and 2 are closed) |
| 0 | 0-c pages | the 300 dpi page renders, PC-01 to PC-18, their provenance rows |
| 0 | 0-d film | FC-01 to FC-06, their provenance rows |
| 1 (bases, 9 comps) | 1-a map base | g-a2s14-six, g-a1s02-strip |
| 1 | 1-b chain base | g-a4s02-countyb, g-a1s13-chain |
| 1 | 1-c film base | g-a1s15-offices |
| 1 | 1-d photo base | g-a2s17-funnels, g-a1s01-kc |
| 1 | 1-e clock base | g-a2s06-headstart, g-a1s05-clocks |
| 2 (15 comps) | 2-a maps | g-a1s06-low, g-a1s09-forecasts, g-a2s01-radar |
| 2 | 2-b maps | g-a2s08-first, g-a2s16-huffman, g-a2s19-log |
| 2 | 2-c chain | g-a2s03-chain, g-a2s09-countya, g-a2s20-front |
| 2 | 2-d photo and page | g-a1s04-wire, g-a1s07-tracks, g-a2s15-old |
| 2 | 2-e list and house | g-a1s18-list, g-a2s21-list, g-a2s11-backup |
| 3 (19 comps) | 3-a maps | g-a3s05-bremen, g-a4s16-fortwayne |
| 3 | 3-b chain | g-a3s04-links, g-a3s15-desks, g-a4s06-died, g-a4s09-clock |
| 3 | 3-c chain and list | g-a4s11-farend, g-a4s13-duty, g-a4s15-chain, g-a3s10-towers |
| 3 | 3-d film and page | g-a3s07-calls, g-a3s01-message, g-a4s01-eyes, g-a4s08-chief |
| 3 | 3-e drawings | g-a3s09-jam, g-a3s11-onoff, g-a3s12-seven, g-a3s13-battery, g-a4s14-eight |
| 4 (13 comps) | 4-a maps | g-a5s01-radar, g-a5s04-berne, g-a5s07-marion |
| 4 | 4-b maps | g-a5s10-alert, g-a5s16-toledo |
| 4 | 4-c photo and page | g-a5s06-hold, g-a5s09-alto, g-a5s14-noissue, g-a5s20-team |
| 4 | 4-d drawings | g-a5s15-dark, g-a5s18-curran |
| 4 | 4-e chain and list | g-a5s12-spotters, g-a5s21-end |
| 5 (13 comps) | 5-a page and plan | g-a6s01-recs, g-a6s02-floorplan |
| 5 | 5-b list and microphone | g-a6s03-announcer, g-a6s10-watch, g-z1s02-row |
| 5 | 5-c chain | g-a6s05-wires, g-a6s08-spotters |
| 5 | 5-d map and drawing | g-a6s07-power, g-a6s09-third, g-z1s04-drill |
| 5 | 5-e film, title and book | g-a6s11-sirens, g-z1s05-title, g-z1s4b-book |
Wave 0 finished 12 Oct 26: its files are the rows of section 3. Wave 0's four jobs ran together. Waves 1 to 5 each wait for the verifier's read of the wave before; a comp that "reuses ... after wave 1" copies a wave 1 base only once that base has passed.

## 6. Picture notes that cannot be built as written, and the smallest change
The script is not changed; these are changes to how a note is drawn.
1. **County outlines (every "our Indiana map" note).** The repo holds state outlines only. Smallest change: one public-domain county boundary file (US Census cartographic boundaries) is pulled into `media/data/` with a provenance row; BM-1 is built from it by script. Until then no map comp that lights a county can start. **Closed 12 Oct 26:** `media/data/cb_2023_us_county_500k.zip`, built into `media/maps/indiana-counties.svg`.
2. **Town positions (the same notes).** No table of longitude and latitude is on disk for the 16 named points of BM-1 or the 7 of BM-2. Smallest change: a `media/data/points.csv` from the US Census gazetteer, with its provenance row. **Closed 12 Oct 26:** `media/data/points.csv` holds 24 towns. Alto is not in the gazetteer and has no dot (rule 20).
3. **Page images.** Nine pages are needed at 300 dpi and are on disk only as the fact check's working copies in `.qc-tmp/sources/`: survey PDF pp. 3, 65, 68, 71, 72 and the pages printed 1 and 2; study PDF pp. 23 and 26. Smallest change: render them the way `survey-pdf-67-orig.png` was rendered. **Closed 12 Oct 26:** the nine page images are in `media/docs/`; printed p. 1 is PDF p. 7 and printed p. 2 is PDF p. 8.
4. **A1-S7, "the tracks light from west to east".** The tracks are ink in a picture; lighting one track means tracing it by eye. Smallest change: an amber wipe from west to east brightens the whole map, so the tracks come up in that order and none is singled out.
5. **A1-S8, "county lines come up under one track".** Nothing registers the track map to county geometry. Smallest change: a row of plain, unnamed county tiles drawn over the dimmed map (the squares of A4-S14), with the hand-off marks between them.
6. **A2-S8, the 5:45 track "from the Weather Service table's coordinates".** The table's coordinates are not on disk. Smallest change: on BM-1, a path between the table's two named ends, Koontz Lake and a point just south of South Bend, with no claim about the line between; the track map is not used here.
7. **A5-S16, "the Toledo track lit".** Same cause: no source says which red line is Toledo's. Smallest change: our own Ohio map with a dot for Toledo carries the stamp and the toll, and runs on into A5-S17's Ohio map; the track map is not shown.
8. **A1-S3, "only the southern part of Porter lights".** No source gives the line. Smallest change: Porter's southern half by the county's mid latitude, labelled "southern Porter"; the brief marks the split as schematic.
9. **A2-S17, the Huffman photograph "full frame".** At cover the 1188 x 1068 file loses 37 % of its height, past the 35 % the crop gate allows, and the cut falls on the funnels. Smallest change: fitted to the frame's height over a blurred copy of itself, slow push.
10. **A1-S9 and A1-S10, state and half-state fills.** A whole state filled says more than "parts of Wisconsin, Iowa and Illinois" or "portions of northern Indiana". Smallest change: a light fill with the scan's own words on the chip ("parts of", "portions of").
11. **A3-S3, "the whole north central part fills".** No boundary exists for the phrase. Smallest change: a soft-edged amber band across the north central third of the state, clipped to the outline, with no county edge inside it.
12. **A1-S6, "one warm front and one cold front".** No source gives their positions, and the real map sits in the same frame. Smallest change: the L placed over the Dakotas and Minnesota from state geometry, wind arrows round it, and the fronts as short textbook stubs marked schematic; or the fronts are left to the real map in the card.
13. **A5-S7, "one storm path ... through Marion and on to Linn Grove".** Drawn as straight legs between the survey's named places (Howard County, Marion, Linn Grove, the state line), labelled as the survey's list of places, not a surveyed track.
14. **The other list frames** (A2-S4, A3-S10, A4-S13, A5-S21, A6-S3, Z1-S2) sit on the canvas gradient, not on the teletype room photograph, to keep that photograph at three uses.
15. **Film inside a composition** (six shots): the cut is mounted in `index.html` under the comp, which carries the window, the frame and the label (rule 15).

## 7. After wave 0: rows whose length or picture changed (12 Oct 26)
Cut lengths are `ffprobe` on the files. Voice times are from the draft voice in `audio/` (segment wav and words.json), read on 12 Oct 26; the final voice may move them, so each brief measures again before it sets a cue.
| Comp | Segment | Film file and length (s) | Film window in the draft voice (s) | Verdict |
|---|---|---|---|---|
| g-a1s15-offices | A1-S15 | `media/films/cuts/a14-05-operations-room.mp4`, 31.53 (plan said 32.1) | 0 to 12.32, the whole segment; it dims at 6.48 | Fits. The window starts at the file's start so its first 2 s are placard-free; placards are in frame after that under the one label (rule 16) |
| g-a1s15-offices | A1-S16 | `media/films/cuts/a14-09-announcer.mp4`, 9.44 (plan said 25.7) | 0 to 8.82, until the last sentence | **Length changed.** Fits with 0.62 s to spare. If the final voice moves that cue past 9.44 s the row needs a second picture: a hard cut to `media/films/cuts/a14-09b-announcer-shoulder.mp4` (7.17), then `media/films/cuts/a14-09c-announcer-microphone.mp4` (7.84), 24.46 in all (rule 17) |
| g-a2s03-chain | A2-S4 | `media/films/cuts/a14-13-operators.mp4`, 15.21 (plan said 15.8) | 0 to 5.98, until "office after office" | Fits |
| g-a3s07-calls | A3-S7 | `media/films/cuts/a14-10-desk-telephone.mp4`, 15.72 (plan said 16.3) | 0 to 4.70, the first sentence | Fits |
| g-a5s10-alert | A5-S11 | `media/films/cuts/a14-08-telephone-call.mp4`, 4.17 (plan said 4.8) | 0 to 1.96, the first sentence | Fits. The window is under 2 s: the brief reads whether the film registers at that length |
| g-a6s11-sirens | A6-S12 | `media/films/cuts/a14-01-siren-horn.mp4`, 11.71 (plan said 12.3) | 0 to 4.44, the first sentence | Fits |

Rows whose picture changed, with no film in them:
- **g-a2s19-log (A2-S19):** the three log cards are cut 1460 px wide (file heights 90, 129 and 128 px), not 900. Three cards and a map cannot all sit at full size; the cards are sized from the files (section 3c) and the 6:24 PM card masks its bottom 12 px.
- **g-a2s14-six (A2-S14):** Plymouth and Donaldson are 17.7 px apart at the map's largest fit, closer than a readable tornado mark is wide. The row needs a push in on Marshall County before the three marks land, and hand-placed labels for the two towns.
- **g-a5s20-team (A5-S20):** the tight crop of printed p. 1 is three lines, not one sentence; the third line stays in frame and only "excellent" is underlined.
- **g-a5s09-alto (A5-S9):** no change to the row. Alto appears as the photograph's label only; no map inset may be added to place it.

Not on disk: nothing. Every file named in section 3 exists; the two extra announcer angles arrived during this check.

Rows the wave 1 and 2 briefs proved wrong or made exact (12 Oct 26, evening; the brief named holds the numbers):
- **g-a2s01-radar:** it does not need the Midwest map. The Indiana map holds Chicago, Fort Wayne and Indianapolis; the row and the BM-2 row are corrected above.
- **g-a2s14-six (section 7 line above):** no extra push is needed. In the map family's NORTH state (3 px per map unit) Plymouth and Donaldson are 48 px apart; the labels are still placed by hand.
- **g-a2s19-log (section 7 line above):** the three log cards do fit at their full 1460 px width under the map in the NORTH state (stack y 560 to 983).
- **g-a2s21-list:** the list and the blank sheet cannot share the frame with the stamp; the list leaves on "typed" before the blank sheet lands.
- **PT-05, PT-06 (forecast scans):** each card shows the typed text only (file y 0 to 312 and y 0 to 334). The figure below it carries marks added later by the page's author, some for tornadoes after the forecast time.
- **PT-09 (Sunnyside):** the clean print inside the faded edge is file x 20 to 780, y 22 to 626; it runs 0.95 to 1.00 in a 722 x 574 window and is never enlarged.
- **PC-04:** the page prints "too old--i.e. 15-30 minutes--" on one single-spaced line, so its underline is 4 px at 2 px under the line, not 6 px at 4 px.
- **PC-06 and rule 18:** the next line's sliver is rows 126 to 128 of the file; the third typed line's descenders run to row 123. A 12 px mask cuts rows 117 to 128; a 4 px mask would remove the sliver alone. The brief follows the ruling and has the verifier read that edge.
- **Stamp zone:** "EST" does not fit beside an 84 px time in the 590 px card; the briefs write the zone in the place line as `Eastern time`.
- **Family bases:** no "Reuses" cell names g-a2s17-funnels or g-a1s05-clocks; their briefs name the later comps that copy them.

Rows the wave 3, 4 and 5 briefs proved wrong or made exact (12 Oct 26, night; the brief named holds the numbers):
- **g-a4s09-clock:** the sheriff page crop cannot run whole as a small strip; the brief shows two page lines at 0.6 of their size with the quote typed again beside them. 7:30 to 8:07 is 37 minutes; the label stays the study's "about 35 minutes".
- **Section 6, item 13 (the straight leg through Marion):** a straight leg through Marion's dot misses Blackford County; the briefs route the path 8 map units south and call it schematic.
- **g-a3s09-jam:** it mounts `media/drawings/telephone-lifted.svg`, not `media/drawings/telephone.svg`.
- **g-a6s07-power:** it also mounts the desk and the teletype drawings.
- **g-a6s01-recs:** the page is single-spaced, so its underline is 3 px.
- **g-a3s10-towers:** the 54 marks fall 0.03 s apart, 1.62 s in a 1.69 s spoken window.
- **g-a4s01-eyes:** no film opens it. A film cut could hold at most 3.15 s there (`media/films/cuts/a14-08-telephone-call.mp4`), it would contradict "He waited", and each shot is used once (rule 4); the brief carries the variant in case the lead rules for film.
- **g-a5s10-alert:** the film window is open for 2.20 s. **g-a3s07-calls:** the film is mounted for 11.41 s and its window shows 4.21 s.
- **g-a5s09-alto:** the first photograph is on screen for 0.97 s only.
- **g-a6s05-wires:** the teletype's label reads `Weather Bureau teletype` there, not `Kansas City forecasters`; the study's p. 29 is cited and not shown, because it prints the county letters.
- **g-a6s08-spotters:** the house label reads `a town`, not `Marion`; the spotter mark is a ring with a mast, drawn in the composition, with no file.
- **g-z1s02-row:** the chain stands under a centred list (sheet x 580 to 1340), not beside it, so the new light can pass between them; the Reuses cell's chain is redrawn at that size.
- **g-z1s4b-book:** the staged cover needs a `provenance.csv` row, which is the orchestrator's to add.
