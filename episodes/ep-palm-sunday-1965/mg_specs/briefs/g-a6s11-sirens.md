Host: id=g-a6s11-sirens file=compositions/g-a6s11-sirens.html start=1108.97 (timeline-map.md table 1 as retimed 12 Oct 26, 19:13; the mount in index.html wins) duration=16.25 s track=2

# g-a6s11-sirens · A6-S11, A6-S12 · nobody could say yet what the recommendations would do, and no siren sounded (wave 5, film family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 7 (the film row of this comp). Times: `mg_specs/timeline-map.md` tables 1, 3 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). While the training film shot is on screen its label `Civil defense training film, 1967` is the only chip in the frame (rule 4). **The siren horn is never shown sounding: no sound lines, no pulse, no shake, no siren audio, drawn or filmed (rule 6).** A flash is a stroke or fill change, never a scale pop (rule 12). The film cut is mounted in `index.html` by the orchestrator under this comp; the comp draws the ground with the 4:3 window, the frame and the label (rule 15).
**Spoken (A6-S11):** "The researchers wrote that it was impossible to tell yet what the recommendations would do."
**Spoken (A6-S12):** "But that evening, in most communities, no siren sounded. And when the researchers asked, most communities in northern and central Indiana still had no siren system."
**One look:** the study's own sentence on paper beside a horn drawn as a bare outline; the outline becomes a real horn on film, silent, under the line that none sounded; then the film is gone and the study's words say most places still had none.

## 0. What this graphic claims
The 1966 researchers wrote that it was too early to tell what the recommendations would do. On the evening itself no siren sounded in most communities, and when the researchers asked, most communities in northern and central Indiana still had no siren system.

## 1. Source
- `edit_script.md` A6-S11, Rows [study printed p. 31]. On paper, the Picture note's words: `It is presently impossible to tell what effect these recommendations will eventually have`, source line `Disaster Research Center, 1966, p. 31`.
- `edit_script.md` A6-S12, Rows [F, sirens row; study printed p. 33]. On paper: `have not gone to a siren system`, source line `Disaster Research Center, 1966, p. 33`.
- No crop of study pp. 31 or 33 is on disk (`mg_specs/acts-plan.md` section 3c lists none), so both quotes are retyped on quote strips, the lift of design sheet section 9. Nothing else from either page is retyped.
- Film: the 1967 civil defense training film (inventory A14), shot 14-01, a siren horn on a pole in tree branches. It stands for a siren of the time, not an Indiana one. `provenance.csv` row `media/films/cuts/a14-01-siren-horn.mp4`.
- The drawn horn: `media/drawings/horn-pole.svg` (DR-06). The Picture note: "an outline only, with no sound lines: a system some communities were looking into."

## 2. Datum, scale, orientation
Frame 1920 x 1080. Three views, hard cuts between them, on the film family's grid (`mg_specs/briefs/g-a1s15-offices.md` section 2):
| Band | Px | Holds |
|---|---|---|
| Film window (the hole) | x 480 to 1440, y 150 to 870 (960 x 720, 1.5 times the 640 x 480 cut) | view FILM |
| Film label | left 480, top 886, height 46 | view FILM |
| Drawing band | y 191 to 539, centred on x 960 | views PAPER and AFTER: the drawn horn stands where the filmed horn will stand |
| Strip band | left 96, top 640, width 1480 | views PAPER and AFTER |
| Presenter corner | x >= 1600 and y >= 680 | nothing of ours, ever |
The film is not this comp's: `index.html` mounts it on track 1 (class `filmwin`, left 480, top 150, 960 x 720, muted) and this comp sits above it with a hole that is open only in view FILM.
| Film mount (`timeline-map.md` table 3) | File | Starts in comp (s) | Mounted (s) | Ends in comp (s) | Window open in this comp (s) | Used of the file |
|---|---|---|---|---|---|---|
| `v-a6s12-horn` | `media/films/cuts/a14-01-siren-horn.mp4` (11.71 s) | 5.35 | 10.90 | 16.25 | 5.35 to 9.20 | the first 3.85 s |
The mount runs to the comp's last frame, so the hole is covered from 9.20 to 16.25 without a gap. Before 5.35 nothing is mounted under the hole, so it is covered then too.
Views: PAPER 0.00 to 5.35 · FILM 5.35 to 9.20 · AFTER 9.20 to 16.25.
Colours (the built set's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Label grey `#93a3b2`; Body light `#dfe7ee`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground with window | as the film base: the canvas gradient as four opaque panels around a hole at x 480 to 1440, y 150 to 870, each panel carrying the full 1920 x 1080 gradient at its own offset so no seam shows. The base's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) runs the whole comp on the panels to carry the holds |
| Hole cover | a fifth opaque panel, same gradient at the same offset, over the hole. **On** from frame 0 to 5.35, **off** 5.35 to 9.20, **on** from 9.20 to the last frame. Each change is one frame |
| Frame | 4 px Body light rectangle on the hole's edge (outer edge x 476 to 1444, y 146 to 874). On only in view FILM |
| Film label | glass chip, left 480, top 886, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Civil defense training film, 1967`. On only in view FILM |
| Drawn horn | `media/drawings/horn-pole.svg` inline, ids prefixed `sir-`, at 1.5 times: object box 120 x 330 at x 900 to 1020, y 200 to 530 (SVG box 138 x 348 at left 891, top 191); line 6 px. Stroke Label grey `#93a3b2`; every `dw-body` fill `none`, so it is an outline and nothing else. No arc, ring, ray or tick is drawn near the horn's mouth, in any frame |
| Strip A (view PAPER) | quote strip as the built `compositions/g-i1s3-cloud.html` `.cloud-strip` (Beige polaroid, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, radius 2): left 96, top 640, 1480 x 200 (bottom 840). Quote in two lines, Georgia 40 px, line height 52, Caption dark, left 136, top 660: `“It is presently impossible to tell what effect` / `these recommendations will eventually have”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 786: `Disaster Research Center, 1966, p. 31` |
| Strip B (view AFTER) | same strip, left 96, top 640, 1480 x 170. Quote on one line, Georgia 52 px, Caption dark, left 136, top 652: `“have not gone to a siren system”`. Attribution, left 136, top 730: `Disaster Research Center, 1966, p. 33` |
No source line in the credit corner: each strip carries its own attribution (design sheet section 10). No stamp, no county chip, no place label.

## 4. Must be true in the picture
1. **The horn never sounds.** No sound lines, arcs, rings or rays; no pulse, shake, scale or glow on the drawn horn or over the film; no `<audio>` in this comp. The drawn horn changes only by being drawn on and by being hidden. (For the verifier, outside this file: no siren sound sits under 1108.97 to 1125.22 in `index.html`.)
2. Whenever a film pixel shows (5.35 to 9.20) `Civil defense training film, 1967` is on screen and is the only chip. No strip, no quote, no place, town, county, date or time is over the film.
3. The film is the first 3.85 s of its file, never frozen, slowed, looped or reversed. It sits only under the sentence that no siren sounded: the window opens on "But" and is gone on "And".
4. The hole is opaque from 0.00 to 5.35 and from 9.20 to 16.25 (read 0.00, 5.30, 9.24 and 16.20 over the real mounts: no black, no film).
5. The drawn horn is a grey outline: never amber, never red, never filled. It stands where the film's horn stands, so the cut reads as the same object. It carries no label; it is not called an Indiana siren or any town's.
6. Strip A holds the study's sentence as the Picture note gives it, in quotation marks, nothing added. Strip B holds `“have not gone to a siren system”` and is not on screen with its quote before "still".
7. No `County A`, no `County B`, no town, no county name, no time of day.
8. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680; all text at least 96 px from the sides and 54 px from top and bottom; the ground shows no seam.
Beat check (rule 13): strip A's quote is settled 1.57 to 5.35 (13 words, 3.78 s). The film runs 3.85 s. Strip B's quote is settled 13.72 to 16.25 (7 words, 2.53 s). From 9.72 to 13.42 the frame holds the horn and the strip with its attribution; the sweep band carries that hold.

## 5. Text (exact) and cues
Text: `“It is presently impossible to tell what effect these recommendations will eventually have”` · `Disaster Research Center, 1966, p. 31` · `Civil defense training film, 1967` · `“have not gone to a siren system”` · `Disaster Research Center, 1966, p. 33`.
Cue words and times are from `audio/a6-s11.words.json` and `audio/a6-s12.words.json` as on disk 12 Oct 26, 19:27 (wavs 4.96 and 10.87 s). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A6-S11 -0.25, A6-S12 4.76) plus the word's time; a first word uses the table's "first sound" (0.00 and 5.34). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S11 | 0 | The | first sound 0.25 | 0.00 | first frame, view PAPER: ground, hole covered, strip A on with its attribution and no quote yet. No horn |
| 1 | A6-S11 | 6 | impossible | 1.52 | 1.27 | the quote lands on strip A, both lines together (fade with `y: 16` to 0, 0.3 s) |
| 2 | A6-S11 | 12 | recommendations | 3.36 | 3.11 | the horn draws on with `strokeDashoffset`, pole first (0.6 s). It is complete by 3.71 |
| 3 | A6-S12 | 0 | But | first sound 0.58 | 5.34 | hard cut to view FILM on the film mount's first frame (5.35): strip A and the drawn horn off, hole cover off, frame and film label on, all in one frame |
| 4 | A6-S12 | 9 | And | 4.44 | 9.20 | hard cut to view AFTER: hole cover on, frame and film label off, the drawn horn back at rest in the same frame |
| 5 | A6-S12 | 10 | when | 4.56 | 9.32 | strip B enters with its attribution and no quote (`y: 60` to 0 with the fade, 0.4 s, power3.out) |
| 6 | A6-S12 | 21 | still | 8.66 | 13.42 | `“have not gone to a siren system”` lands on strip B (fade with `y: 16` to 0, 0.3 s). Hold to the last frame (16.25); the act's black follows in `index.html` |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a6s11-sirens.html` is the only file the builder writes; `data-composition-id="g-a6s11-sirens"`, `data-duration="16.25"`; id prefix `sir-`; root `<div id="sir-root" ...>` styled through `#sir-root` (plan rule 3 overrides the template's `id="root"`). The comp is opaque over the whole frame except the film window from 5.35 to 9.20. It mounts no video and no audio: the film mount `v-a6s12-horn` is the orchestrator's, already typed in `index.html`.
**Family base it copies:** `compositions/g-a1s15-offices.html` (wave 1, brief `mg_specs/briefs/g-a1s15-offices.md`): the ground with the hole, the frame, the label chip, the hole cover and its one-frame cuts, pasted as that comp's film-view block. The strips are that comp's strip A. It copies no microphone, no lamp, no house.
**Assets (paths from the episode folder; read from the files 12 Oct 26):**
- `media/films/cuts/a14-01-siren-horn.mp4` (FC-06, 640 x 480, 11.71 s, a silent audio stream): under the comp, not mounted by it.
- `media/drawings/horn-pole.svg` (DR-06, object box 80 x 220, viewBox -6 -6 92 232, line 4), inlined. Mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a6s11-sirens`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. Read alone, the contact sheet shows the hole empty from 5.35 to 9.20: that is expected there and a defect anywhere else.

## 7a. Done line
All seven lines of template section 7a. Line 3 here: frame 0 is the ground with strip A, the hole covered. Line 4: seek to 5.35 and 9.20 forward and backward and match the frames. Line 7: frames at 6.50 and 8.80 composited over the real film (one chip, a silent horn), and frames at 5.30, 9.24 and 16.20 over the mount to prove the hole is covered.

## 8. Receipt
As template section 8, plus: the measured width of each quote line and a one-line statement that no element near the horn's mouth exists in the file.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground, strip A with attribution, hole covered, no horn. Then settled frames: 1.70 (strip A's quote, both lines), 4.00 (horn outline complete, grey, no sound lines), 5.30 (last PAPER frame, hole covered), 5.40 and 7.50 over the film (window open, frame, one chip, nothing else), 9.16 (last FILM frame), 9.24 (hole covered, drawn horn back), 9.90 (strip B with attribution, no quote), 13.90 (quote settled), 16.20 (last frame: horn, strip B, corner empty).
