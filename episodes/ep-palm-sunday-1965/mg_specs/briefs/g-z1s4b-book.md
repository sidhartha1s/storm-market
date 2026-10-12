Host: id=g-z1s4b-book file=compositions/g-z1s4b-book.html start=1163.12 (timeline-map.md table 1 as retimed 12 Oct 26, 19:13; the mount in index.html wins) duration=6.31 s (wav 6.06 s plus its gaps) track=2

# g-z1s4b-book · Z1-S4b · the book, once: its cover and where to find it (wave 5, card on the channel ground)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2 and 3. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21 (this composition was added on 12 Oct 26 by the lead's order; its row is added at the end of section 2 by the director). Times: `mg_specs/timeline-map.md` tables 1 and 5 and section 6 ("The script's second book note").
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the picture shows (rule 5): the one line here names where the book is, nothing else. Pictures under 1000 px wide sit in a card at their own size or smaller, never enlarged (section 3e's rule): the cover is shown below its own size. No county code, no film label, no stamp.
**Spoken (Z1-S4b):** "My book, The Storm-Ready Home, is the checklist for your house, first link in the description."
**One look:** the book's front cover standing on the channel ground, and under it one line saying where it is.

## 0. What this graphic claims
The book is called The Storm-Ready Home, and the link to it is the first link in the video's description. The picture claims nothing else: no price, no offer, no deadline.

## 1. Source
- `edit_script.md` Z1-S4b, Rows [`config.yaml channel.cta`: the book's name and `first_link`] · [ad transcript `assets/cta/paul-storm-ready-v7-oct10.txt`]. The Picture note: "the book's front cover (repo file `landing/assets/cover.png`, 'The Storm-Ready Home'; not yet staged in this episode's `media/`, the builder copies it in) standing on the channel ground, with one line under it: `first link in the description`. No price, no QR code (the code lives in the ad), no page from inside the book."
- The cover, read 12 Oct 26: `landing/assets/cover.png` under the worktree root, 1024 x 1536 px (2 to 3), 2,012,741 bytes. It prints `STORM MARKET FIELD MANUAL`, the title `THE STORM-READY HOME`, a subtitle, a line of four counts and `PAUL RAYMOND`, over a painted house under a dome with the author standing in front. All of that is the cover and is shown whole.
- The one book ad is the config file mounted at 636.44; this comp is not the ad and copies nothing from it.

## 2. Datum, scale, orientation
Frame 1920 x 1080, one view, everything centred on x 960.
| Element | Px |
|---|---|
| Staged copy | 720 x 1080 (0.7031 of the 1024 x 1536 original: no source asset may be taller than the frame, `media_budget.py`) |
| Cover on screen | 480 x 720 (0.6667 of the staged copy), left 720, top 96, bottom 816 |
| Line | centred on x 960, top 856 |
| Presenter corner | x >= 1600 and y >= 680: nothing of ours |
The cover's own title is the only place the book's name is printed; it is not retyped. Read it on the first frame: if `THE STORM-READY HOME` does not read at 480 x 720, say so in the receipt and change nothing.
Colours: ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Headline white `#f2f5f8`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, full frame, on from frame 0 |
| Cover | one `<img>` of the staged copy, 480 x 720 at left 720, top 96, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, corner radius 2, no border, no tilt, no reflection, no mock-up of a physical book. `transform-origin: 50% 50%` |
| Slow push | the cover's scale runs 1.00 to 1.03 over the whole 6.31 s, ease none (`scale: 1` set in the timeline at 0, then a plain `to()`); at 1.03 it is 494 x 742, y 85 to 827, 29 px above the line |
| Line | `first link in the description`, Arial 700 40 px, Headline white, one line, centred on x 960, top 856 (it ends near y 902). No arrow, no underline, no button shape, no chip |
Nothing else is on screen: no price, no URL, no QR code, no logo, no countdown, no "now", no badge, no inside page, no source line, no stamp.

## 4. Must be true in the picture
1. The cover is shown whole and unaltered: not cropped, recoloured, tilted or retouched, and never larger than the staged copy (0.667 to 0.687 of it).
2. The only words of ours on screen are `first link in the description`, exactly, in lower case as written.
3. No price, no discount, no URL, no QR code, no urgency device (timer, "limited", "today", a flashing or pulsing element), no page from inside the book.
4. The line does not appear before "First" is spoken (4.16). The cover is on from the first frame, under "My book".
5. The cover moves only by the slow push; the line does not ride it (it sits on a fixed layer).
6. Nothing of ours in x >= 1600, y >= 680; the line is at least 96 px from the sides and 54 px from the bottom.
7. No `<audio>` in this comp.
Beat check (rule 13): two beats in 6.31 s (the cover at 0.00, the line at 4.16); the push carries the 4.16 s between them. The line is settled 4.46 to 6.31 (5 words, 1.85 s).

## 5. Text (exact) and cues
Text: `first link in the description` (the cover's printed words are the image).
Cue words and times are from `audio/z1-s4b.words.json` as on disk 12 Oct 26, 19:27 (wav 6.06 s, 17 words). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (Z1-S4b -0.44) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | Z1-S4b | 0 | My | first sound 0.44 | 0.00 | first frame: ground and the cover at scale 1.00, already on (a hard cut in on the first word); the push starts |
| 1 | Z1-S4b | 12 | First | 4.60 | 4.16 | the line rises (`y: 16` set at 0, to 0 with the fade, 0.3 s, power2.out). Hold to the last frame (6.31) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: the builder writes two files and no other: `compositions/g-z1s4b-book.html`, and the one staged copy of the cover, `media/stills/z1-book-cover.png`. `data-composition-id="g-z1s4b-book"`, `data-duration="6.31"`; id prefix `bk-`; root `<div id="bk-root" ...>` styled through `#bk-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. The host is mounted in `index.html` as `host-z1s4b-book`; do not edit `index.html`.
**Staging the cover (once, by a one-line command, not by hand):** scale `landing/assets/cover.png` (worktree root, 1024 x 1536) to 720 x 1080 with a smooth filter (Lanczos), no crop, no other change, and save it as `media/stills/z1-book-cover.png` in the episode folder. Do not edit, move or rename the file under `landing/`. State the staged file's size in the receipt. A `provenance.csv` row for it is the orchestrator's to add (source: the repo's own `landing/assets/cover.png`, the owner's book); name the need in the receipt and do not edit `provenance.csv`.
**Family base it copies:** the framed print of `compositions/g-a2s17-funnels.html` (wave 1, brief `mg_specs/briefs/g-a2s17-funnels.md`): a picture shown at or under its own size on the ground with the paper shadow and a slow push inside the hold. It copies no chip, credit, toll or place label from it.
**Assets:**
- `landing/assets/cover.png` (worktree root; 1024 x 1536): the source, read only.
- `media/stills/z1-book-cover.png` (episode folder; 720 x 1080): the staged copy this comp mounts. It does not exist until the builder makes it.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-z1s4b-book`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965` (its media budget check reads the staged copy's size).

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill; the cover is 480 px of a 1920 px frame by design, the Picture note's "standing on the channel ground". Line 3: frame 0 shows the ground and the cover. Line 4: seek to 4.30 (mid rise) forward and backward and match the frames; the cover's scale and the line's `y` are set at timeline 0.

## 8. Receipt
As template section 8, plus: the staged file's pixel size and bytes, and the line's measured width.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground and the whole cover, sharp, its title readable, nothing else. Then settled frames: 2.50 (cover alone, pushed a little, no line), 4.60 (line settled under the cover, not touching it), 6.28 (last frame: cover, line, corner empty, nothing else on screen).
