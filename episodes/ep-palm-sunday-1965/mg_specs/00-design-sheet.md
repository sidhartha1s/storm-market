# mg_specs/00-design-sheet.md: one world for the hook tail and the intro (ep-palm-sunday-1965)

Read this before any brief in this folder. It is the one home of every recurring piece: the telephone list, the chain,
the drawn house and living room, the clock stamp, the document card, the source line. A brief names a piece and gives
only what is new in its own beat. Rules: `references/mg-quickref.md`. Hex, fonts, tiers: `library/inhouse/snippets/tokens.md`
(tokens are named here, never restated as new values). Written 12 Oct 26. The study's page scans (comps 06, 09, 10) are not on disk yet; every other photograph is (section 4).

## 1. The world in four sentences
- **Paper is their words.** Anything the 1966 study or the Weather Bureau wrote sits on paper: the telephone list sheet, the page scans, the lifted quote strip.
- **Glass is our label.** Clock stamp, place label, name card: the channel glass card (tokens.md "Surfaces").
- **A line drawing stands only where no photograph exists:** house, living room, television, table radio, microphone, desk, telephone, teletype icon. One line weight, straight on, no people.
- **Red means "nobody was told". Amber means light and time.** Red (Crimson, Popfig red) is never used for a tick, a pin or decoration. A lit window, a lit screen, a clock time and the travelling light in the chain are amber.

## 2. Palette pick (10 tokens) and surfaces
| Use | Token |
|---|---|
| Headlines, lit drawing lines | Headline white |
| Row values, labels on glass, drawing lines at rest | Body light |
| Eyebrows, unlit drawing lines, dotted chain line | Label grey |
| The toll figure, the date label | Popfig red |
| Underline on a page, the mark on a list row, the ON AIR lamp | Crimson |
| Lit window, lit screen, clock time, travelling light | Amber 2 |
| Paper stock (list sheet, page border, quote strip) | Beige polaroid |
| Ink on paper, ticked rows | Caption dark |
| Grey ink on paper (rows not spoken), rules on paper | Caption dark sub |
| Body fill of a drawn object (covers lines behind it) | Panel dark (RHS stat panel) |

Surfaces, not counted: canvas ground (BG gradient center to BG gradient edge, radial, never flat), glass card, `.dim` and `.dim-heavy` scrims (tokens.md "Scrim").
Fonts: Courier New 700 for everything typed on the list sheet and for clock times; Arial 700 and Arial Black (always `font-weight:900`) for our labels; Georgia for lifted quotes; AbrilFig for the two popfigs only.

## 3. Frame rules every brief inherits
- Text at least 96 px from left and right, 54 px from top and bottom.
- **Presenter corner: nothing of ours in x >= 1600 and y >= 680**, in every comp, hook included. Paper edges and drawings count, not only text.
- Every comp is full frame with its own ground (a photograph or the canvas gradient) on from frame 0. No transparent comp in this set, so no comp depends on a still mounted in `index.html` (a still held over 6 s fails sweep check 9).
- A photograph inside a comp is one `<img>` at cover, moved by GSAP only (slow push, `ease:"none"`), with a scrim `<div>` above it. Its drift is the motion that carries every hold.
- Text never rides the camera: labels that name a place or a source sit on a fixed HUD layer. The list sheet's typed rows are the one exception: they are the object being filmed.
- Cues are words, not seconds. The voice is not recorded: every brief writes `cue: "<word>"` with `t=` blank; the builder fills `t=` from `audio/<seg>.words.json` and keeps the word in a comment (`/* list @t */`).

## 4. Photograph grounds
Files landed in `media/stills/` at 03:15 on 12 Oct 26 and were opened for this sheet; rows in `provenance.csv`. Mount the 1080-fit copy named here, never an `-orig` file (media budget), except where a brief names a crop to be cut from one.
| Ground | Inventory row | File (`media/stills/`) and size | Used by | Scrim | True caption (HUD credit) |
|---|---|---|---|---|---|
| Teletype room | A3 (wea01832) | `a3-teletype-operators.jpg`, 1370 x 1080. Two operators seen from behind at their machines; no face shows | 02, 03, 08, 12 | `.dim` under 02; tween to `.dim-heavy` when paper arrives | "Weather Bureau Communications Center, about 1955 · NOAA" |
| Teletype machines | A4 (wea01821) | `a4-teletype-room.jpg`, 1456 x 1080. Wide room, a row of machines, three people with faces, a wall clock | 07 | `.dim` | "Weather Bureau teletypewriters, about 1955 · NOAA" |
| Damage, Dunlap | C2 | `c2-dunlap-sunnyside-damage.jpg`, 800 x 647 only, with a faded white edge | 01 | none; popfig carries its own local scrim | place label, section 11 |
| Damage, Alto | C5 | `c5-alto-aerial-damage.jpg`, 1543 x 1080 | 01 | none | place label |
| Damage, Pittsfield | C7 | `c7-pittsfield-damage-aerial.jpg`, 1887 x 1080, newspaper halftone | 01 | none | place label |
| Track map | B7 | `b7-tornado-track-map.jpg`, 1396 x 1046. White ground, grey county lines, red tracks; it prints no state name | 07 | none | "Courtesy: Dr. Russell Schneider, SPC" |
| Survey page | B1 | `b1-south-bend-warning-page-orig.png`, 2550 x 3300 (the 835 x 1080 copy is too small for text) | 02 | none | section 9 |
At cover, A3 is enlarged 1.40x and loses 28.6 % of its height, A4 1.32x, C2 2.4x (soft: read it on a frame). No card, chip or stamp may sit over a face in A4.

A3 and A4 are not South Bend, not Kansas City and not 1965. **A place or time label never sits bare on them.** The place and time live on the clock stamp (a glass card, our label), and the photograph carries its own true caption in the credit corner. See template section 7a.7.
Teletype room continuity (comps 02 then 03 are a match cut): the `<img>` runs scale 1.00 to 1.06 across comp 02; comp 03 opens at scale 1.06 and runs to 1.14 across its window. Same `object-position: 50% 40%` in every comp that uses A3.

## 5. The telephone list sheet (comps 03, 08, 12; miniature in 11)
The list is the study's own list of who South Bend telephoned (study printed p. 14). It is a sheet of typed paper.

World coordinates (1 world px = 1 screen px in the "everything" frame, before the camera's `ty`):
| Element | World px |
|---|---|
| Sheet | left 64, top 60, width 760, height 590 (right 824, bottom 650). Fill Beige polaroid, no border, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, corner radius 2 |
| Eyebrow | x 96, y 84, Courier New 700 19 px, Caption dark sub, tracking 2: `WEATHER BUREAU · SOUTH BEND, INDIANA` |
| Title | x 96, y 118, Courier New 700 30 px, Caption dark: `Warnings telephoned to:` |
| Telephone glyph | drawn telephone (section 7), handset on hook, at 0.5 scale, box x 730 to 790, y 96 to 150, Caption dark lines 2 px |
| Rule | y 172, x 96 to 792, 2 px, Caption dark sub at 40 % |
| Row n (n = 1 to 9) | centre y = 214 + 48 x (n - 1): 214, 262, 310, 358, 406, 454, 502, 550, 598. Row box 44 tall |
| Tick box | x 96 to 124, 28 px square, 2 px Caption dark sub outline |
| Row text | x 150, Courier New 700 26 px, one line |
| Row rule | 1 px, Caption dark sub at 25 %, under each row at centre y + 24 |

Rows, in the study's order, exact spelling:
| n | Text | Spoken in T1-S3 |
|---|---|---|
| 1 | State Police | yes ("State Police") |
| 2 | Sheriffs' Departments | yes ("Sheriffs") |
| 3 | City Police Departments | yes ("City police") |
| 4 | Indiana and Michigan Electric Company | no |
| 5 | Red Cross | no |
| 6 | Specified radio and TV stations | yes ("Named radio and television stations") |
| 7 | Flying services | no |
| 8 | Airlines | no |
| 9 | (blank) | the row with no name |

Row states (the same six in every comp):
- **Typed:** text Caption dark sub. All eight rows are typed before any is ticked.
- **Ticked:** a pen tick drawn in the tick box (one 2-segment path, 4 px, Caption dark, `strokeDashoffset`, 0.25 s), text turns Caption dark. A tick means "telephoned". It is never red.
- **Grey:** rows 4, 5, 7, 8 stay Caption dark sub with an empty tick box. Still readable: contrast on Beige polaroid is the test, read on a frame.
- **Lit (08 only):** an Amber 2 band at 35 % behind the row, `scaleX` 0 to 1 from the left.
- **Marked (12 only):** a Crimson 5 px line under the row text, plus a Crimson ring round the tick box.
- **Pulse (12 only):** the Amber 2 band at 25 % wipes across a row and leaves; nothing stays.
- **Blank row 9:** a tick box and a row rule like the others, no text, a Courier cursor block (14 x 28 px, Caption dark) at x 150 that blinks with finite repeats (on 0.5 s, off 0.5 s). It has no tick, ever.

Camera states (one transform on the world container, origin top left; screen = s x world + t):
| State | s | tx | ty | Sheet on screen | Row text size | Used by |
|---|---|---|---|---|---|---|
| Close | 1.6 | 147.6 | -66 | x 250 to 1466, y 30 to 974 | 41.6 px | 03 (T1-S3), 08, 12 |
| Everything | 1.0 | 0 | 110 | x 64 to 824, y 170 to 760 | 26 px | 03 (T1-S4, T1-S5 start) |
| Push | 1.2 | 27.2 | -157.6 | blank row centre lands at (560, 560) | 31.2 px | 03 (T1-S5 end) |

Close-state row centres on screen: 276.4, 353.2, 430.0, 506.8, 583.6, 660.4, 737.2, 814.0, 890.8. Tick box left edge 301.2; row text left edge 387.6; eyebrow renders at 30.4 px, title at 48 px. In the Everything state the eyebrow is 19 px, the floor.
Close to Everything is a 1.6x move: use `logZoom` (`library/inhouse/snippets/helpers.js`).
Source line for the list (HUD, fixed): `Disaster Research Center, 1966 · list of offices the Weather Bureau telephoned` at left 96, bottom 60 (section 11).

**Never the whole system.** The sheet never carries a row count, "all", "every", "complete" or "the warning system". The title is "Warnings telephoned to:" and nothing wider. No teletype, siren or newspaper is added to it.

## 6. The chain (comp 03 right half; comp 11 whole frame)
Hook version, world px, same world as the sheet:
| Element | World px |
|---|---|
| Dotted line | y 598 (the blank row's centre), x 824 to 1030 and x 1150 to 1300; 4 px dots, 14 px gap, Label grey |
| Microphone | box x 1030 to 1150, y 400 to 630 (section 7) |
| Label "an announcer" | centred x 1090, y 664, Arial 700 26 px, Body light |
| House | box x 1300 to 1560, y 380 to 630 (section 7) |
| Label "a family" | centred x 1430, y 664, Arial 700 26 px, Body light |

The microphone is **apart from the paper**: 206 px of ground between the sheet's edge and the microphone, no tick box, no row rule, not on beige. It stands for any station. No call letters, no station name, no frequency.
"Dark" for the microphone and the house means: lines Label grey at 55 %, windows and lamp filled Panel dark, no amber anywhere on them.

Intro version (comp 11), five stations on one line, centre y 520, screen px:
| Station | Box (x, y) | Drawing | Label under it (Arial 700 22 px, Label grey, top 676) |
|---|---|---|---|
| 1 | 96 to 236, 450 to 590 | teletype icon | Kansas City forecasters |
| 2 | 316 to 460, 490 to 590 | telephone at 1.6 scale, handset off the hook | Weather Bureau · South Bend |
| 3 | 540 to 800, 350 to 650 | miniature list sheet: Beige polaroid 260 x 300, 8 Caption dark sub bars 170 x 10 px with 8 tick boxes, a ninth empty tick box, no words | the list |
| desk | 840 to 1095, 490 to 618 | desk at 0.85 scale, telephone at 0.85 scale on it (x 930 to 1006, y 487 to 524; the desk's top surface is y 524), handset on the hook | none |
| 4 | 1170 to 1272, 420 to 616 | microphone at 0.85 scale | an announcer |
| 5 | 1400 to 1577, 430 to 600 | house at 0.68 scale (aerial rises to y 407) | a family |
Links at y 520, 4 px, Label grey: 236 to 316 and 460 to 540 solid; 800 to 840 solid; 1095 to 1170 and 1272 to 1400 dotted. The desk is not drawn until its cue; until then the 800 to 1170 stretch is one dotted line.

## 7. Drawings: period-plain line
Rules that keep them off clip art and off AI art:
- One line weight: 4 px at world scale, round caps and joins. On screen a line is never thinner than 3 px.
- Straight on (front elevation). No perspective, no shadow, no gradient, no texture, no hatching, no curve other than a circular arc or a rounded corner.
- At most 16 path segments per object. Right angles, plus one roof pitch of 30 degrees.
- Two fills only: Panel dark for a body (so lines behind do not show through), Amber 2 for a lit window or screen.
- No person, no face, no hand, no silhouette at a window. No brand, no logo, no text on an object except "WEATHER BUREAU" on the television card and "ON AIR" on the lamp.
- Drawn on with `strokeDashoffset` (dash = `ceil(len)+1`), longest line first, 0.5 to 0.8 s per object.

Objects, in px inside each object's own box (origin top left):
| Object | Box | Lines |
|---|---|---|
| House | 260 x 250 | roof: (0,80) to (130,5) to (260,80). walls: rect x 20 to 240, y 80 to 250. door: rect x 112 to 148, y 170 to 250. two windows: rect x 44 to 92 and x 168 to 216, y 120 to 168, each with one vertical and one horizontal bar. chimney: rect x 186 to 208, y 22 to 50. rooftop television aerial: mast (70,40) to (70,-34), crossbars 32 px wide at y -28 and 22 px wide at y -14. The aerial is the 1965 marker |
| Microphone | 120 x 230 | capsule: rounded rect x 30 to 90, y 0 to 112, radius 30. three grille lines x 40 to 80 at y 30, 56, 82. neck: (60,112) to (60,182). base: (30,182), (90,182), (108,230), (12,230), closed. Lamp: circle radius 9 at (104, 20), outside the capsule |
| Television | 300 x 240 | cabinet: rounded rect 0 to 300, 0 to 200, radius 6. screen: rounded rect x 20 to 212, y 20 to 180, radius 24. two dials: circles radius 14 at (256,62) and (256,112). speaker: four lines x 236 to 276 at y 146, 156, 166, 176. legs: (40,200) to (28,240) and (260,200) to (272,240) |
| Table radio | 150 x 90 | body: rounded rect, radius 8. dial: circle radius 22 at (112,45), one pointer line. speaker: five vertical lines x 20, 32, 44, 56, 68, y 20 to 70 |
| Desk | 300 x 150 | top: rect x 0 to 300, y 40 to 52. legs: rects x 14 to 26 and x 274 to 286, y 52 to 150. drawer: rect x 190 to 264, y 62 to 100, handle line 16 px |
| Telephone | 90 x 44 | body: (0,44), (90,44), (78,14), (12,14), closed. dial: circle radius 9 at (45,29). handset on hook: rounded bar x 4 to 86, y 0 to 10, two 10 x 8 px ear blocks under its ends. Off the hook: the bar raised 26 px and turned -20 degrees, cord of three small arcs back to the body |
| Teletype icon | 140 x 140 | body: rect x 0 to 140, y 50 to 140. keyboard: rect x 14 to 126, y 112 to 132. paper: rect x 34 to 106, y 0 to 50, three typed bars 44, 52, 36 px wide at y 14, 26, 38 |
| Living room | full frame | floor line y 820, x 96 to 1560. window frame (seen from inside): rect x 180 to 520, y 220 to 600, one vertical and one horizontal bar, fill Amber 2 at 30 % (afternoon). television at 1.5 scale, box x 760 to 1210, y 460 to 820. side table: desk object without drawer at 0.8 scale, x 1260 to 1500, y 700 to 820; table radio at 1.2 scale on it, x 1290 to 1470, y 592 to 700 |

Television screen states (the screen area only, clipped to the screen's rounded rect):
- **Off:** fill Panel dark, one 2 px Label grey reflection arc. Nothing moves on it.
- **Programme (plain frame):** fill Amber 2 at 22 %, with three soft horizontal bars (Headline white at 10 %, 190 px wide, 22 px tall) that drift down the screen at 30 px/s on finite repeats. No figure, no animal, no landscape, no title. It reads as "a show is on" and as nothing else.
- **Break-in card:** fill Panel dark, the words `WEATHER BUREAU` in Arial Black 900, Headline white, two lines, centred; at 1.5 scale the letters are 34 px tall. One 2 px Headline white frame line 10 px inside the screen edge.
A switch between states is a hard cut with one 0.1 s white flash at 30 %, never a fade.

## 8. Clock stamp (comps 02, 07)
Glass card, left 96, top 96, 590 x 200. Inside:
- Clock face: circle radius 62, centre (191, 196), 4 px Body light, twelve ticks 8 px long (the four quarter ticks 14 px), hands 5 px, round caps, hour hand 34 px, minute hand 52 px, centre dot radius 5.
- Eyebrow: x 284, y 116, Arial 700 20 px, Label grey, tracking 6.
- Time: x 284, y 142, Courier New 700 84 px, Amber 2.
- Place: x 286, y 244, Arial 700 26 px, Body light.
| Comp | Eyebrow | Time | Place | Hour hand | Minute hand |
|---|---|---|---|---|---|
| 02 | WEATHER BUREAU | 5:43 PM | South Bend, Indiana | 171.5 degrees | 258 degrees |
| 07 | FORECASTERS | 11:45 AM | Kansas City | 352.5 degrees | 270 degrees |
Angles are clockwise from 12. Entrance: card `fromTo(x:-660 to 0, 0.6, power3.out)`; the minute hand sweeps its last 30 degrees into place (0.5 s, power3.out) so the time lands on the spoken word. Exit: `to x:-980, autoAlpha:0, 0.6, power3.in`.
Exemplar: El Reno `compositions/g-a4s13-clock.html` (`.worktrees/ep-el-reno-v4b/episodes/ep4-el-reno/`), copy the face and hands, retune.

## 9. Document card and quote strip (comps 02, 06, 09, 10)
A real page, shown as the page. Never retyped to look like a page.
- **Card:** the page image cropped to the full width of its text column (never a word cut at an edge), on a Beige polaroid border 10 px, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Screen box per brief; standard box left 96, top 116, 1480 x 450 (right 1576, bottom 566, clear of the corner).
- **Scale rule:** scale = card inner width / text column width in page px. The builder measures the column and the sentence's line boxes on the page image first, writes them into the comp as constants in page px, and multiplies by the scale (El Reno `mg_specs/docs.md` section 2 is the method). If a text line would be under 34 px tall on screen, crop fewer lines, never a narrower column.
- **Unlit page:** four Panel dark rects at 45 % cover everything on the card except the sentence's line boxes, fading in over 0.4 s as the underline starts.
- **Underline:** Crimson, 6 px, 4 px below each line box, drawn left to right with `scaleX` (`transformOrigin:"left center"`), one line box at a time, on the voice.
- **Quote strip (the lift):** the underlined words retyped, because a page line is too small for a television across the room. Beige polaroid strip, left 96, top 606, 1480 x 220 (bottom 826, right 1576). Quote in Georgia, Caption dark, with quotation marks, 52 px for up to 8 words, 40 px in two or three lines above that. Attribution under it: Arial 700 22 px, Caption dark sub, tracking 2. The strip enters `fromTo(y:60 to 0, autoAlpha 0 to 1, 0.4, power3.out)` on the sentence's last underlined word, never before the underline is complete.
- **County label:** glass chip above the card, left 96, top 54, height 46, padding 0 x 22, Arial 700 26 px, Body light: `one Indiana county` (09) or `a different county` (10). The two never share a frame.
- Exit: card and strip slide out together, `to x:1900, autoAlpha:0, 0.6, power3.in`.
- The study scan is not a row of the picture inventory and its rights line is unread: every page brief waits for the scan and its `provenance.csv` row.
Exemplars: El Reno `compositions/g-a4s11-page.html` (page crop, unlit page, lit sentence) and `library/inhouse/quote-card.html` (beige quote, phrase by phrase).

## 10. Source line
One per frame, in the credit corner, fixed HUD: left 96, bottom 60, Arial 700 22 px, `rgba(244,240,232,0.88)`, `letter-spacing:0.04em`, `text-shadow: 0 0 10px rgba(0,0,0,0.95), 0 2px 4px #000` (the values of El Reno `index.html` `.credit`, baked into the comp under the comp's own class name). Proper case. Enters with a 0.3 s fade plus `y:12 to 0`; leaves with the comp.
A page brief's source line is the attribution on the quote strip instead; the frame then has no second source line.

## 11. Labels on photographs
- **Place label (01):** glass chip at left 110, bottom 110, padding 14 x 26, one line, Arial Black 900 34 px, Headline white. One chip per photograph, each pre-authored, toggled with `autoAlpha`.
- **Date label on Paul's clip (H1-S1, an `index.html` overlay built by the orchestrator, not a comp):** the channel popfig, big line `April 11, 1965` (14 characters), sub line `Indiana`, inside the first second, out before T1-S1. Wrapped in a timed `<section>`. The script's Picture note gives the sub line as `one Indiana county`; the orchestrator's accepted wording is `Indiana`. Either fits; the big line does not change.

## 12. Standing truths (every brief's section 4 includes these by reference)
S1. No county or town is named as "the one". County labels read `one Indiana county` and `a different county`, never in the same frame.
S2. The eight-row list is never shown as the complete warning system (section 5).
S3. The toll reads 271 with its source line; no other toll figure is larger than the source line's type.
S4. No station from the study's row C8 is drawn as a member of the South Bend list: the microphone has no name and sits off the paper.
S5. No real person is drawn. No frame, title card, logo or character of the real "Lassie" show appears; the word "Lassie" is never on screen.
S6. Nothing appears before its spoken word.
S7. Nothing of ours in x >= 1600, y >= 680.
S8. A3 and A4 are never labelled as South Bend, Kansas City or 1965 by a bare label on the photograph.
