Host: id=g-a3s07-calls file=compositions/g-a3s07-calls.html start=528.39 (timeline-map.md table 1; the mount in index.html wins) duration=17.24 s track=2

# g-a3s07-calls · A3-S7, A3-S8 · the office asks people to stop calling, and "the poor observer" (wave 3, film window family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 4, 7, 8, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3d row FC-04, section 3e row PT-07. Times: `mg_specs/timeline-map.md` tables 1, 3 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). While a training film shot is on screen its own label `Civil defense training film, 1967` is the only chip in the frame (rule 4). A photograph's label names what the photograph shows, never the town the voice is talking about (rule 5). The teletype room photograph appears three times in A1 to Z1 and this is the third and last (rule 9). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window (rule 13). The film is mounted in `index.html` by the orchestrator, under this comp (rule 15).
**Spoken (A3-S7):** "Three minutes later the office was asking for help with its own phones. People should stop calling the Weather Bureau unless they had weather to report, because joke calls were tying up the lines."
**Spoken (A3-S8):** "The Weather Service's own history calls the man who typed that message "the poor observer.""
**One look:** a desk telephone in a period film, then the clock at 7:13 and the typed plea on paper, then a teletype room with three words on paper: the poor observer.

## 0. What this graphic claims
At 7:13 PM the South Bend Weather Bureau asked the public to stop telephoning it unless they had weather to report, because joke calls were tying up its lines. The National Weather Service's own history calls the man who typed that message "the poor observer". The film shot stands for a busy desk telephone of the time; the photograph shows a Weather Bureau teletype room about 1955. Neither is South Bend on April 11, 1965.

## 1. Source
- `edit_script.md` A3-S7, Rows [A12; survey printed p. 41]; A3-S8, Rows [E, the South Bend observer; IWX: "It was not a good day for the poor observer at the South Bend weather office. At 7:13pm he issued this statement"]. The name belongs to the 7:13 message only.
- Film: `media/films/cuts/a14-10-desk-telephone.mp4` (inventory A14, shot 14-10; `provenance.csv` row): a man in a jacket at a brick-wall desk with a black rotary telephone, a second man holds it by the end; one continuous shot; no sign in frame.
- Photograph: `media/stills/a3-teletype-operators.jpg` (inventory A3, NOAA Central Library wea01832): two operators seen from behind at their machines, about 1955; no face shows.
- The 7:13 PM entry (survey printed p. 41) is not on disk as a crop: its words appear on a quote strip with quotation marks and attribution, never set to look like the page.

## 2. Datum, scale, orientation
Frame 1920 x 1080. Three views, hard cuts between them, on the grid of the film base `mg_specs/briefs/g-a1s15-offices.md`:
| Band | Px | Holds |
|---|---|---|
| Film window (the hole) | x 480 to 1440, y 150 to 870 (960 x 720, 1.5 times the 640 x 480 cut) | view FILM |
| Film label | left 480, top 886, height 46 (y 886 to 932) | view FILM |
| Clock stamp | left 96, top 96, 590 x 200 | view DESK |
| Telephone | x 782 to 1139, y 200 to 571 | view DESK |
| Label chip of the photograph | left 96, top 578, height 46 | view ROOM |
| Strip band | left 96, top 640, 1480 x 170 (x 96 to 1576, y 640 to 810) | views DESK and ROOM |
| Presenter corner | x >= 1600 and y >= 680 | nothing of ours, ever |
The film is not this comp's: `index.html` mounts it on track 1 (class `filmwin`, left 480, top 150, 960 x 720, muted) and this comp sits above it with a transparent hole.
| Film mount (`timeline-map.md` table 3) | File | Starts in comp (s) | Mounted (s) | Window open in this comp (s) | Used of the file |
|---|---|---|---|---|---|
| `v-a3s7-telephone` | `media/films/cuts/a14-10-desk-telephone.mp4` (15.72 s) | 0.00 | 11.41 | 0.00 to 4.21 | the first 4.21 of 15.72 s |
The mount runs 7.20 s longer than the window; the comp, not the mount, decides the cut. From 4.21 the hole is opaque.
Clock hands, clockwise degrees from 12: 7:13 is hour 216.5, minute 78.

## 3. Geometry (screen px)
View FILM (0.00 to 4.21):
| Element | Px |
|---|---|
| Ground with window | the canvas gradient as four opaque panels around a transparent hole at x 480 to 1440, y 150 to 870, each panel carrying the full 1920 x 1080 gradient offset by its own left and top (no seam), exactly as the base |
| Frame | 4 px Body light rectangle on the hole's edge (outer edge x 476 to 1444, y 146 to 874), on from frame 0 |
| Film label | glass chip, left 480, top 886, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Civil defense training film, 1967`. On from frame 0, off with the window at 4.21 |
View DESK (4.21 to 11.41):
| Element | Px |
|---|---|
| Hole cover | a fifth opaque panel, the same gradient at the same offset, over x 480 to 1440, y 150 to 870: on in one frame at 4.21 and never off again. Frame and film label go off in that frame |
| Clock stamp | design sheet section 8, as the built `compositions/g-t1s2-warning.html`: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `7:13 PM` / `South Bend, Indiana`; hour hand 216.5, minute hand 78 |
| Telephone | `media/drawings/telephone.svg` inline (handset on the cradle), ids prefixed `call-`, at 3.5 times: SVG box 357 x 371 at left 782, top 200; `stroke-width="1.6"` on the `dw-phone` group (5.6 px lines, README "Large"); lines Body light, bodies Panel dark. Screen x = 782 + 3.5 x (object x + 6), y = 200 + 3.5 x (object y + 58) |
| Ring arcs | two arcs each side of the handset's ends, radius 40 and 64 px, 4 px Body light, as the built `compositions/g-t1s2-warning.html`; centres are the handset's two ends, computed from the inlined file by the formula above |
| Strip E (the plea) | quote strip as the base's strip (Beige polaroid, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, radius 2): left 96, top 640, 1480 x 170. Quote `“numerous poor joke calls and they tie up the lines”`, Georgia 40 px, Caption dark, one line if it measures 1400 px or less, else two lines. Attribution: Arial 700 22 px, Caption dark sub, tracking 2: `Weather Bureau, South Bend · 7:13 PM` |
View ROOM (11.41 to 17.24):
| Element | Px |
|---|---|
| Photograph | `media/stills/a3-teletype-operators.jpg`, one `<img>` at cover, `object-position:50% 40%`, on in one frame at 11.41 over the whole frame; scale 1.00 to 1.04 from 11.41 to 17.24, `ease:"none"`, GSAP only |
| Scrim | `rgba(3,5,8,0.45)` over the photograph, under everything else |
| Photograph label | glass chip, left 96, top 578, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Weather Bureau Communications Center, about 1955`. On in the cut frame; it is the one label of this view (no second caption in the credit corner) |
| Strip E | stays in its box across the cut, until step 9 |
| Strip F | same box, left 96, top 640, 1480 x 170. Quote `“the poor observer”`, Georgia 52 px, Caption dark. Attribution: `National Weather Service, Northern Indiana` |
The stamp and the telephone go off in the cut frame at 11.41: the photograph is not South Bend, so no South Bend stamp sits on it.

## 4. Must be true in the picture
1. While the film window is open (0.00 to 4.21) the only chip, stamp, strip or label in the frame is `Civil defense training film, 1967`. No clock, no time, no South Bend.
2. The hole is opaque from 4.21 to the end, although the mount under it runs to 11.41. A frame at 5.00 read over the mount shows no film.
3. The clock reads 7:13 PM: hour hand between 7 and 8, minute hand between the 2 and the 3 (78 degrees). The strip's attribution says `7:13 PM` too.
4. Strip E's words are the message's as the script quotes them, in quotation marks with the attribution. Nothing on screen is set to look like the survey page.
5. The photograph's only label is `Weather Bureau Communications Center, about 1955`: the inventory's caption for photograph A3, the one form everywhere by the lead's ruling of 12 Oct 26 (this brief said `teletype room` before). It is never labelled South Bend, 1965 or 7:13 PM by a bare label, and the stamp is gone before it shows.
6. Nobody in the photograph is named. `“the poor observer”` sits on paper with its own attribution, beside the photograph's label, so neither operator is read as the observer. No person is drawn anywhere.
7. The ring arcs pulse three times and no more: 3 times 0.4 s is 1.2 s, from 5.53 to 6.73, inside the clause that ends on "report," (7.51).
8. This is the third and last use of the teletype room photograph in A1 to Z1.
9. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `Civil defense training film, 1967` · `WEATHER BUREAU` · `7:13 PM` · `South Bend, Indiana` · `“numerous poor joke calls and they tie up the lines”` · `Weather Bureau, South Bend · 7:13 PM` · `Weather Bureau Communications Center, about 1955` · `“the poor observer”` · `National Weather Service, Northern Indiana`.
Cue words and times are from `audio/a3-s7.words.json` and `audio/a3-s8.words.json` as they stood on 12 Oct 26 at 19:30. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A3-S7 -0.51, A3-S8 11.16) plus the word's time; a segment's first word uses table 5's first sound. Retime from the word index and the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S7 | 0 | Three | 0.00 | 0.00 | first frame: ground, open window on the desk telephone shot, frame, film label |
| 1 | A3-S7 | 13 | People | 4.72 | 4.21 | hard cut inside the comp: hole cover on, frame and film label off, in one frame; the clock stamp slides in from the left (`x:-660` set at 0, to 0; 0.6 s, power3.out), the minute hand sweeping its last 30 degrees, 48 to 78 |
| 2 | A3-S7 | 16 | calling | 5.44 | 4.93 | the telephone draws on (0.6 s, longest line first); from 5.53 the ring arcs pulse three times (0.4 s each, finite) |
| 3 | A3-S7 | 26 | because | 8.84 | 8.33 | the ring arcs come on again and stay, Body light (a stroke change, 0.2 s) |
| 4 | A3-S7 | 27 | joke | 9.20 | 8.69 | strip E rises (`y:60` set at 0, to 0 with the fade; 0.4 s, power3.out) with its quote and attribution |
| 5 | A3-S7 | 30 | tying | 9.98 | 9.47 | the telephone's lines and the arcs turn Label grey (0.3 s): the line is tied up |
| 6 | A3-S8 | 0 | The | 0.00 | 11.41 | hard cut inside the comp: photograph, scrim and the photograph label on; stamp, telephone and arcs off; strip E stays. The slow push starts |
| 7 | A3-S8 | 9 | typed | 2.56 | 13.72 | strip E's attribution line takes a Popfig red 4 px underline under `7:13 PM` (`scaleX` 0 to 1, 0.3 s): "that message" |
| 8 | A3-S8 | 12 | the | 3.98 | 15.14 | strip E fades out (0.2 s) |
| 9 | A3-S8 | 13 | poor | 4.06 | 15.22 | strip F rises in the same box (0.4 s, power3.out) with `“the poor observer”` and its attribution. Hold to the cut at 17.24 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s07-calls.html` is the only file the builder writes; `data-composition-id="g-a3s07-calls"`; id prefix `call-`; root `<div id="call-root" ...>` styled through `#call-root` (plan rule 3 overrides the template's `id="root"`). The comp is opaque over the whole frame except the film window from 0.00 to 4.21. It mounts no video and no audio: the film mount is the orchestrator's, already typed in `index.html`.
**Family base it copies:** the film view (ground with hole, frame, label chip, the hard cut that covers the hole) and the strip of `compositions/g-a1s15-offices.html` (wave 1; brief `mg_specs/briefs/g-a1s15-offices.md`). Clock stamp and the telephone with ring arcs from the built `compositions/g-t1s2-warning.html`; photograph ground and scrim from the built `compositions/g-t1s3-list.html`. No later composition copies this one.
**Assets (paths from the episode folder):**
- `media/films/cuts/a14-10-desk-telephone.mp4` (FC-04, 640 x 480, 15.72 s): under the comp, not mounted by it.
- `media/stills/a3-teletype-operators.jpg` (1370 x 1080 px), mounted by the comp.
- `media/drawings/telephone.svg` (viewBox -6 -58 102 106, line 3), inlined.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s07-calls`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. The contact sheet shows the hole as empty when the comp is read alone: expected from 0.00 to 4.21 and a defect after 4.21.

## 7a. Done line
All seven lines of template section 7a. Line 3 here: frame 0 is the open window with frame and label, the ground on around it. Line 4: seek to 4.21, 5.90 (mid pulse) and 11.41 forward and backward and match the frames. Line 6: the handset ends and arc centres are computed by a script from the inlined telephone and stated in the receipt. Line 7: a frame at 2.00 composited over the real film (the label is the only chip) and a frame at 5.00 over the mount to prove the hole is covered; at 12.50 the label `Weather Bureau Communications Center, about 1955` sits on a photograph whose `provenance.csv` row says that.

## 8. Receipt
As template section 8, plus the measured width of strip E's quote and the line count chosen.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): window open, frame, one label, no seam in the ground. Then one settled frame per cue: 2.00 (over the film: desk telephone, one label), 4.25 (hole covered), 5.00 (stamp at 7:13, hands right), 5.60 (telephone drawn), 5.95 (arcs mid pulse), 8.60 (arcs held), 9.20 (strip E with attribution), 9.90 (telephone and arcs grey), 11.45 (photograph, scrim, label chip, strip E; no stamp, no telephone), 14.20 (underline under `7:13 PM`), 15.80 (strip F settled, strip E gone), 17.10 (last look).
