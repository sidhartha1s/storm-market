Host: id=g-a1s01-kc file=compositions/g-a1s01-kc.html start=(timeline-map.md) duration=9.75 s (timeline-map.md table 1) track=2

# g-a1s01-kc · A1-S1 · the forecast starts in Kansas City at 11:45 (wave 1, photograph family base)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 4, 8, 10, 11 and 12. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a row DR-01 and section 3e row PT-01.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the photograph shows, never the town the voice is talking about (rule 5). A flash is a stroke or fill change, never a scale pop (rule 12). Design sheet section 4: no card, chip or stamp sits over a face in this photograph, and a place or time label never sits bare on it.
**Spoken (A1-S1):** "A forecast in nineteen sixty five was a typed message, so follow it from the start. It starts in Kansas City at eleven forty five that morning, Eastern time."
**One look:** a Weather Bureau teletype room, drifting; a drawn teletype whose paper turns amber on "typed"; then the clock stamp from the intro comes back and its time lands on "eleven forty five".

## 0. What this graphic claims
A forecast in 1965 was a typed message, and this one started with the forecasters in Kansas City at 11:45 AM Eastern time. The photograph claims only that the Weather Bureau worked on teletype machines like these. It is not Kansas City and it is not 1965, so the place and the time live on the glass stamp (our label) and the photograph keeps its own true caption.

## 1. Source
- `edit_script.md` A1-S1, Rows [A1; study printed p. 6: "At 11:45 a.m. (EST)"]. Picture note: the teletype machines photograph (inventory A4, true caption in the credit corner); the clock stamp from the intro returns as a glass card, "FORECASTERS · 11:45 AM EST · Kansas City"; the drawn teletype icon of the chain lights amber, alone.
- Photograph: `media/stills/a4-teletype-room.jpg`, 1456 x 1080 px (read with PIL on 12 Oct 26), 79,997 bytes. Its `provenance.csv` row, quoted: type STILL; date "circa 1955"; title "Teletypewriters in action; transmitting and receiving weather data"; licence "The following images are all from various NOAA websites, as indicated for each. They are all in the public domain."; credit "NOAA Central Library, U.S. Weather Bureau, wea01821"; note "Row A4. Direct file: https://circuitousroot.com/images/artifice/telegraphy/tty/gallery/noaa/wea01821.jpg. Wide view of a Weather Bureau teletype room: row of teletype machines, operators, wall chart. Original 1612x1196 kept as a4-teletype-room-orig.jpg. Same mirror caveat as A3."
- What the row limits: the photograph is about 1955 and the row names no town. It is ten years older than the story and it is not Kansas City. It is 1456 px wide, so it may fill the frame (section 2). It is inventory A4, not the A3 photograph whose uses are counted by plan rule 9; this is A4's second use in the episode (the first is the built `compositions/g-i1s4-states.html`).
- True caption (plan section 3e, PT-01; design sheet section 4): "Weather Bureau teletypewriters, about 1955 · NOAA".
- Drawing: `media/drawings/teletype.svg` (DR-01, paper unlit) and its lit state `media/drawings/teletype-lit.svg`: object box 140 x 140, viewBox `-6 -6 152 152`, line 4. It is the same drawing as the chain's first station.

## 2. Datum, scale, orientation
One `<img>` at cover: the file is enlarged 1.3187 times to 1920 x 1424.2 px, so 24.2 % of its height is outside the frame (under the 35 % of the crop gate). `object-position: 50% 50%`, as the intro mounted it: image rows y 130.5 to 949.5 are in the frame at the start. Screen px from image px at the start: x = 1.3187 x image x; y = 1.3187 x image y minus 172.1.
The push: scale 1.00 to 1.06 across the whole comp (9.75 s), `ease:"none"`, a plain `to()` from rest, `transformOrigin: "1700px 600px"`. The origin sits by the seated man at the right so that his face does not slide out of the frame; the left edge of the picture travels 102 px (10.5 px a second), which reads as a drift. At the last frame the frame shows start-frame screen x 96.2 to 1907.5 and y 34.0 to 1052.8. The scale never goes under 1, so no edge of the photograph shows.
Faces and the wall clock, read off the file by eye (plus or minus 20 px; the builder reads them again on a frame):
| Thing in the photograph | Image px | Screen at 0.00 | Screen at 9.75 |
|---|---|---|---|
| Man bending, far left | (25, 530) | (33, 527) | (-67, 522), out of frame |
| Woman, left | (130, 610) | (171, 632) | (80, 634) |
| Man standing at the machines, seen from behind | (650, 460) | (857, 435) | (807, 425) |
| Man seated, right | (1415, 600) | (1866, 619) | (1876, 620) |
| Wall clock (no readable hands on the file) | (890, 400) | (1174, 355) | (1142, 341) |
The stamp, the icon tile and the caption are a fixed layer over the photograph: they do not ride the push.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | `<img src="media/stills/a4-teletype-room.jpg">`, left 0, top 0, 1920 x 1080, `object-fit:cover; object-position:50% 50%`, moved by GSAP only (section 2). On from frame 0. Behind it the canvas gradient of `g-i1s4-states.html` (`radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`), so a late image never shows a transparent frame |
| Scrim | `.dim` under this comp's own class name: left 0, top 0, 1920 x 1080, `rgba(3,5,8,0.45)`. On from frame 0, fixed |
| Caption | credit corner, left 96, bottom 60, the source-line type of design sheet section 10 (Arial 700 22 px, `rgba(244,240,232,0.88)`, `letter-spacing:0.04em`, its text shadow): `Weather Bureau teletypewriters, about 1955 · NOAA`. On from frame 0: the photograph is never on screen without it |
| Icon tile | glass plate (fill `rgba(10,16,24,0.55)`, `backdrop-filter:blur(18px) saturate(1.15)`, border 1 px `rgba(255,255,255,0.14)`, radius 28): left 96, top 330, 200 x 200. It covers start-frame screen x 96 to 296, y 330 to 530: an equipment rack, no face (the woman's head is 60 px below it at 0.00 and moves left, away from it) |
| Teletype | `media/drawings/teletype.svg` inline inside the tile, ids prefixed `kc-`, at scale 1: the 152 x 152 SVG at tile-local left 24, top 24, so the object box is screen x 126 to 266, y 360 to 500. Lines Body light `#dfe7ee`, 4 px. Unlit: paper (`dw-lamp`) fill Panel dark `#15202b`, typed bars (`dw-type`) stroke Body light. Lit: paper fill Amber 2 `#e8c56a`, bars stroke Caption dark `#2a2622` (the values of `teletype-lit.svg`) |
| Clock stamp | glass plate, same values: left 96, top 96, 680 x 200 (the intro's stamp is 590 wide; this one is 90 px wider to hold `EST`). It covers screen x 96 to 776, y 96 to 296: ceiling lamps and wall, no face |
| Clock face | inside the stamp, as built in `g-i1s4-states.html`: centre stamp-local (95, 100) = screen (191, 196), radius 62, ring 4 px Body light, twelve ticks 3 px (8 px long, the four quarter ticks 14 px), hour hand 34 px and minute hand 52 px, both 5 px Headline white `#f2f5f8`, round caps, centre dot radius 5 Amber 2. Hour hand 352.5 degrees, minute hand 270 degrees at rest (clockwise from 12) |
| Eyebrow | `FORECASTERS`: stamp-local left 188, top 20 (screen 284, 116), Arial 700 20 px, Label grey `#93a3b2`, letter-spacing 6 px |
| Time | `11:45 AM`: stamp-local left 188, top 46 (screen 284, 142), Courier New 700 84 px, Amber 2, letter-spacing -4 px. Computed width 371 px, so it ends near screen x 655 |
| Zone | `EST`: stamp-local left 574, top 96 (screen 670, 192), Arial 700 26 px, Body light. Computed width 51 px, ending near screen x 721, 55 px inside the stamp's right edge. Measure the time's real width on a frame and keep 15 px between `AM` and `EST`; its foot sits on the time's baseline |
| Place | `Kansas City`: stamp-local left 190, top 148 (screen 286, 244), Arial 700 26 px, Body light |

Nothing else is on screen: no arrow, no route, no second station of the chain, no label under the icon, no paper strip, no year.

## 4. Must be true in the picture
1. The photograph is never labelled as Kansas City or as 1965. `Kansas City` and `11:45 AM` `EST` are inside the glass stamp only; the only words set on the photograph itself are its true caption, `Weather Bureau teletypewriters, about 1955 · NOAA`, and the caption is on in every frame the photograph is on, from frame 0 (design sheet S8).
2. No plate covers a face at any frame, start to end of the push. Read the stamp and the icon tile against the four people at 0.00, 5.00 and 9.70. If section 3's numbers put a plate on a face, this line wins: move the plate, keep the face clear, report it.
3. The teletype icon is alone: one drawing, no link line, no telephone, no microphone, no house, no label under it. Its paper is dark until "typed" and Amber 2 after it.
4. The icon lights by a fill and stroke change only (rule 12): no scale pop, no glow pulse, no shake.
5. The time reads `11:45 AM`, with `EST` beside it, and the clock face reads 11:45 (hour hand just short of 12, minute hand on the 9). No hand is on the face before the word "eleven".
6. Nothing appears before its spoken word: the stamp is not on screen before "Kansas", the time is not on screen before "eleven", `EST` is not on screen before "Eastern".
7. The photograph never shows an edge and never scales under 1. The man at the right is whole in the last frame.
8. Nothing of ours in x >= 1600, y >= 680 (the photograph itself is ground, not ours; read the corner on a frame).

## 5. Text (exact) and cues
Text: `Weather Bureau teletypewriters, about 1955 · NOAA` · `FORECASTERS` · `11:45 AM` · `EST` · `Kansas City`. Every word is from the Picture note of A1-S1 or the photograph's caption. No other word, number or time is on screen.
Cue words and times are from `audio/a1-s1.words.json` as it stood on 12 Oct 26 at 17:44 (wav 9.42 s). `mg_specs/timeline-map.md` table 5: the wav starts at -0.31 s inside this comp, the first sound is at 0.00 and the last at 8.74; the comp is 9.75 s long. So t from comp start = the word's time minus 0.31, and the first word is at 0.00. Retime from the word, never from the seconds. The transcriber writes "1965" as one word and "11" ".45" as two.
| Step | Segment | Word index | Word | t in words.json (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S1 | 0 | A | 0.00 | 0.00 | first frame: the photograph at scale 1.00, the scrim and the caption. The push starts and runs to the last frame (1.00 to 1.06, 9.75 s, ease none) |
| 1 | A1-S1 | 1 | forecast | 0.40 | 0.09 | the icon tile slides in from the left with the unlit teletype in it (`fromTo` x:-420 to 0, autoAlpha 0 to 1, 0.5 s, `power3.out`) |
| 2 | A1-S1 | 6 | typed | 2.48 | 2.17 | the paper turns Amber 2 and the three typed bars turn Caption dark (0.3 s, `power2.out`). It stays lit to the end |
| 3 | A1-S1 | 17 | Kansas | 5.98 | 5.67 | the stamp slides in from the left (`fromTo` x:-800 to 0, autoAlpha 0 to 1, 0.6 s, `power3.out`) carrying the clock ring and ticks, `FORECASTERS` and `Kansas City`. The time line is empty and the face has no hands |
| 4 | A1-S1 | 20 | 11 | 6.84 | 6.53 | `11:45 AM` rises in (autoAlpha 0 to 1, y:16 to 0, 0.3 s, `power3.out`); the two hands fade in (0.15 s) and the minute hand sweeps from 240 to 270 degrees (0.5 s, `power3.out`, ends 7.03, inside ".45") |
| 5 | A1-S1 | 24 | Eastern | 8.16 | 7.85 | `EST` fades in (autoAlpha 0 to 1, y:8 to 0, 0.25 s) |
| 6 | exit | none | (0.6 s before the cut) | none | 9.15 | the stamp and the icon tile slide out left (`to` x:-980, autoAlpha 0, 0.6 s, `power3.in`); the photograph and its caption hold to the cut at 9.75 |
Longest stretch with no new element: 2.47 to 5.67 (3.2 s), with the push moving all through it. If the contact sheet reads frozen there, raise the end scale to 1.08 with the same origin, check line 7 of section 4 again and report it.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a1s01-kc.html` is the only file the builder writes; `data-composition-id="g-a1s01-kc"`; id prefix `kc-`; root `<div id="kc-root" ...>` styled through `#kc-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Every class name is this comp's own (`kc-...`): never a class of `index.html` or of another comp.
**Style reference it matches:** the built `compositions/g-i1s4-states.html`, part B (`.st6-bg`, `.st6-scrim`, `.st6-stamp`, `.st6-eye`, `.st6-time`, `.st6-place`, `.st6-cap`, and the clock face drawn in its script): copy the values under `kc-` names. The chain look of `compositions/g-i1s9-chain.html` is where the teletype drawing comes from; nothing else of the chain is used here.
**Family base role (plan section 5, wave 1, builder 1-d, with `compositions/g-a2s17-funnels.html`):** this is the base for one photograph mounted at cover with a scrim, a slow push, its true caption in the credit corner and our labels on glass. Later compositions copy it: `g-a1s04-wire` (wave 2, named in its brief), `g-a1s07-tracks` (wave 2, caption and push habits) and the wave 4 photograph comps `g-a5s06-hold` and `g-a5s09-alto` (plan section 3e rows PT-10 to PT-12). Send it alone for a full-size read before anything copies it (template section 7a, last line).
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/stills/a4-teletype-room.jpg` (1456 x 1080 px). Never the `-orig` file.
- `media/drawings/teletype.svg` (object 140 x 140, viewBox -6 -6 152 152, 784 bytes), inlined; `media/drawings/teletype-lit.svg` (689 bytes) is the reference for the lit colours and is not mounted.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s01-kc`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: the fill is the photograph at cover (state the figure). Line 3: the photograph, the scrim and the caption are all on at frame 0. Line 4: seek to 6.80 (the minute hand mid sweep) forward and backward and match the frames; the hands' `svgOrigin` is set once at build, never only in a `from`. Line 6: the cover scale 1.3187, the crop loss 24.2 % and the five rows of section 2's table are computed from the file's size by a script and stated in the receipt. Line 7 does not apply as an overlay (the comp is full frame), but its last sentence does: the caption is the only label on the photograph and it matches the `provenance.csv` row.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the photograph fills the frame, scrim and caption on, no plate, no edge. Then one settled frame per cue: 1.00 (icon tile in, paper dark), 2.80 (paper amber, bars dark), 5.00 (mid push, no face under the tile), 6.40 (stamp in: `FORECASTERS`, `Kansas City`, no time, no hands), 7.40 (`11:45 AM` and the hands at 11:45), 8.40 (`EST` on, 15 px clear of `AM`), 9.70 (plates gone, photograph and caption alone, the man at the right whole).
