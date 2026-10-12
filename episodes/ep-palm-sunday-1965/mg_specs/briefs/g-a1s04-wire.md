Host: id=g-a1s04-wire file=compositions/g-a1s04-wire.html start=143.49 (timeline-map.md table 1; the mount in index.html wins) duration=9.94 s (wav 9.51 s plus its gaps) track=2

# g-a1s04-wire · A1-S4 · the teletype circuit map, one pulse (wave 2, photograph family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 3, 4 and 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3e row PT-02.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the photograph shows, never the town the voice is talking about (rule 5). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A1-S4):** "It moved by teletype, which was a telephone line with a typewriter on each end. What Kansas City typed, a machine in South Bend typed out."
**One look:** the Weather Bureau's own circuit map, drifting toward the Midwest, and one soft amber wash when the far machine types.

## 0. What this graphic claims
A teletype was a telephone line with a typewriter on each end: what one office typed, a machine in another office typed out. The picture claims only that the Weather Bureau ran a national teletypewriter system and that this is its own map of it. It does not show the route the 11:45 forecast took.

## 1. Source
- `edit_script.md` A1-S4, Rows [NWS Heritage: "Teletypes, basically telephone lines connected to typewriters"].
- Photograph: `media/stills/a1-service-a-teletype.jpg` (1668 x 1212, inventory row A1, the Service A teletypewriter system map slide; row in `provenance.csv`). True caption: "Service A teletypewriter system, about 1960 · NOAA". It is a map of about 1960, not of April 1965. The slide prints its own circuit lines, circuit numbers and a legend; they are part of the photograph.

## 2. Datum, scale, orientation
One `<img>` at cover: the file is enlarged 1.1511 times to 1920 x 1395.1 px, so 22.6 % of its height (315.1 screen px) is outside the frame. `object-position: 50% 20%` keeps image rows y 54.7 to 993.0 at the start; the slide's printed title at the very bottom is outside the frame (our caption carries the name).
The push: scale 1.00 to 1.10 over the whole comp, `ease:"none"`, `transformOrigin: "1208.6px 397.4px"`. That screen point is image (1050, 400), between the map's Kansas City centre and the Great Lakes. At the last frame the frame shows image x 95.5 to 1611.8, y 86.1 to 939.0. The scale never goes under 1, so no edge of the photograph shows.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | `<img src="media/stills/a1-service-a-teletype.jpg">`, left 0, top 0, 1920 x 1080, `object-fit:cover; object-position:50% 20%`, moved by GSAP only (section 2). On from frame 0. Behind it the canvas gradient, so a late image never shows a transparent frame |
| Scrim | none over the map: it is the subject. One bottom band only, left 0, top 900, 1920 x 180, `linear-gradient(to bottom, rgba(3,5,8,0), rgba(3,5,8,0.55))`, so the caption reads on the orange slide |
| Caption | credit corner, left 96, bottom 60, the source-line type of design sheet section 10 (Arial 700 22 px, its colour and shadow): `Service A teletypewriter system, about 1960 · NOAA` |
| Amber wash | one `<div>` over the whole frame, left 0, top 0, 1920 x 1080, fill Amber 2, CSS `opacity:0`. It does not move and has no edge: the whole map lifts at once |

Nothing else is on screen: no arrow, no dot, no route line, no city label, no clock.

## 4. Must be true in the picture
1. No route is traced. Nothing of ours follows, highlights or points along any line on the slide, and nothing joins Kansas City to South Bend.
2. The amber wash covers the whole frame evenly. It is not a band, a sweep or a spot, so it reads as "the far machine typed", never as a path.
3. The only words of ours are the caption, and they are the photograph's true caption. No "Kansas City", no "South Bend", no "1965" is set on the photograph.
4. The wash is a change of opacity only: Amber 2 with a screen blend, opacity 0 to a peak of 0.50 and back to 0 (cue 8.23 s, 0.30 s up, 0.55 s down), over the whole frame. No scale pop, no shake. As fixed, 12 Oct 26: at the 0.26 this brief first gave, the wash moved the frame's mean luminance by 1.5 levels and failed its reader; at 0.50 with the screen blend it moves it by 22.5 levels at the peak.
5. The photograph never shows an edge and never scales under 1.
6. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680 (the caption ends well left of it; the bottom band is a scrim, not an object, but read the corner on a frame).
7. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `Service A teletypewriter system, about 1960 · NOAA`.
Cue words and times are from `audio/a1-s4.words.json` as it stood on 12 Oct 26 at 18:00, after the voice conversion's re-transcription (wav 9.508 s). The comp holds one segment, so the two time columns are equal; if `mg_specs/timeline-map.md` (not on disk yet) puts a gap before the segment, add it to every row. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S4 | 0 | It | 0.00 | 0.00 | first frame: the map at scale 1.00, the bottom band on. The push starts and runs to the last frame (1.00 to 1.10, 9.51 s, ease none) |
| 1 | A1-S4 | 3 | teletype, | 1.06 | 0.85 | caption fades in (0.3 s, `y:12` to 0) |
| 2 | A1-S4 | 24 | typed | 8.44 | 8.23 | the amber wash: opacity 0 to 0.26 in 0.30 s (`power2.out`), then to 0 in 0.55 s (`power1.in`); it is gone by 9.29 |
| 3 | A1-S4 | 25 | out. | 8.78 | 8.57 | no new element: the wash is at its peak inside this word (8.74). Hold to the cut at 9.51 |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.
Between steps 1 and 2 (7.4 s) the push is the only motion: it must be visible on the contact sheet as a steady drift. If the read says the frame looks frozen, raise the end scale to 1.14 with the same origin and report it.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a1s04-wire.html` is the only file the builder writes; `data-composition-id="g-a1s04-wire"`; id prefix `wire-`; root `<div id="wire-root" ...>` styled through `#wire-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the photograph family base `compositions/g-a1s01-kc.html` (wave 1; brief `mg_specs/briefs/g-a1s01-kc.md`) for the way one photograph is mounted, pushed and captioned; the photo ground of the built `compositions/g-i1s4-states.html` part B for the `<img>` and caption classes. No later composition copies this one.
**Assets mounted (paths from the episode folder):**
- `media/stills/a1-service-a-teletype.jpg` (1668 x 1212 px).

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s04-wire`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: the fill is the photograph at cover (state the figure). Line 6: the cover scale 1.1511 and the transform origin (1208.6, 397.4) are computed from the file's size by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the map fills the frame, no caption yet, no edge. Then one settled frame per cue: 1.50 (caption on, readable over the band), 5.00 (mid push: the frame has moved against 0.00), 8.74 (wash at its peak: the whole map lifted, nothing banded), 9.40 (wash gone, last look before the cut).
