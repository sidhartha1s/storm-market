Host: id=g-z1s05-title file=compositions/g-z1s05-title.html start=1169.43 (timeline-map.md table 1 as retimed 12 Oct 26, 19:13; the mount in index.html wins) duration=15.23 s (last sound at 11.23, then the 4.0 s end hold) track=2

# g-z1s05-title · Z1-S5 · the signature footnote over the channel title card: the outro (wave 5, close card)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building; the presenter circle is hidden under the close card). Outro rules: `DESIGN.md` "Outro" and "Signature closing footnote". Look: `mg_specs/00-design-sheet.md` section 2 for the ground and Headline white. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1): the library card's `fromTo` entrances are rewritten that way. The root is styled through its id and is never `id="root"` (rule 3): the library card's `#root` is renamed. No county code, no film label, no stamp and no source line belongs here.
**Spoken (Z1-S5):** "Disasters don't ask permission. But they do send warnings. Learn how yours will reach you, so when it comes, you already know what to do. This was The Warning Hour."
**One look:** the footnote's own words, two lines at a time, quiet on the channel ground; on "Warning" the channel's name lands under them and holds while the picture dies to black.

## 0. What this graphic claims
Nothing new. It carries the channel's closing footnote as spoken and lands the channel's name on the words "The Warning Hour". It is the outro: no recap, no summary, no episode fact.

## 1. Source
- `edit_script.md` Z1-S5: the channel's signature closing footnote (`DESIGN.md`), with "what yours sounds like" changed to "how yours will reach you" for this episode. Every on-screen line is the spoken line, word for word.
- `DESIGN.md`: "Outro: match-cut the channel title to the closing line; card does not sit." and the footnote "plays over the title card; it IS the outro (still no recap, no content summary)".
- The card: `library/inhouse/outro-brand.html` (worktree root), the "THE / WARNING / HOUR" brand outro. The variant that leads with spoken lines above the brand lockup is `episodes/ep6-katrina-2005/compositions/g-close.html` (worktree root); its two-line block over a brand block is the layout used here.

## 2. Datum, scale, orientation
Frame 1920 x 1080. Everything is centred on x 960. Two stacked blocks, both on screen at the end:
| Block | Px | Holds |
|---|---|---|
| Footnote lines | top 300 to about 440 | one pair of lines at a time |
| Wordmark | centred on y 620 (box about y 548 to 692) | `THE WARNING HOUR` |
The presenter circle is hidden under the close card (`references/mg-quickref.md`), so the corner rule does not bind here; nothing is placed in x >= 1600, y >= 680 all the same except the wordmark's last letters if it measures that wide (see section 3).
Colours: ground, the canvas gradient `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` (the library card's flat `#030507` is its outer stop); Headline white `#f2f5f8`; Amber 1 `#d8a13a` (the brand card's own amber, copied with the card; it is not one of this episode's ten working tokens and is used nowhere else); black `#000` for the final fade.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, full frame, on from frame 0 |
| Stage | one wrapper holding both blocks, `transform-origin: 50% 50%`; it breathes from scale 1.000 to 1.025 over the whole 15.23 s, ease none (the Katrina close's slow breathing; set `scale: 1` in the timeline at 0, then a plain `to()`) |
| Line a (pairs 1 and 2) | Georgia italic 52 px, line height 70, Headline white, centred on x 960, top 300 |
| Line b (pairs 1 and 2) | Georgia italic 36 px, line height 48, Amber 1, centred on x 960, top 392 |
| Pair 1 | a: `Disasters don’t ask permission.` b: `But they do send warnings.` |
| Pair 2 | a: `Learn how yours will reach you,` b: `so when it comes, you already know what to do.` |
| Wordmark | `THE WARNING HOUR` as `library/inhouse/outro-brand.html` `.twh`: Arial Black, `font-weight:900`, 120 px, letter-spacing 6 px, Headline white, the word `WARNING` in Amber 1; one line, centred on (960, 620). Measure its width in a frame and state it; it must sit inside x 96 to 1824. If it does not, drop to 112 px and say so |
| Final black | a full-frame `#000` div above everything, opacity 0 until the fade |
Each pair is its own pre-authored block, toggled by opacity; pair 1 and pair 2 occupy the same two boxes and are never both visible. A typographic apostrophe is used in `don’t`.

## 4. Must be true in the picture
1. Every line on screen is the spoken line, word for word, and no line appears before its first word is spoken.
2. The wordmark lands on the spoken word "Warning" (10.53), not before and not after the sentence.
3. No blank frame between the footnote and the wordmark: pair 2 stays on screen, dimmed, when the wordmark lands (the library's blank scan once found a 0.75 s hole in a close card at this seam).
4. No episode number, no episode title, no tag line, no "subscribe", no link, no book, no recap line. The library card's two sample lines (`.ep`, `.tag`) are not copied.
5. The card does not sit: the stage breathes for the whole comp and the picture is black by the last frame. The fade starts 2.80 s after the last sound and takes 1.2 s.
6. The comp stays opaque to its last frame (the black div covers it; the root is never faded), so nothing under the host shows.
7. No `<audio>` in this comp; the score and its end are the orchestrator's.
8. All text at least 96 px from the sides and 54 px from top and bottom.
Beat check (rule 13): six beats in 10.53 s, the closest two 0.78 s apart (9.75 and 10.53); every entrance is 0.5 s or less. Pair 1 is read for 4.71 s (9 words), pair 2 for 5.04 s before it dims (16 words).
9. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `Disasters don’t ask permission.` · `But they do send warnings.` · `Learn how yours will reach you,` · `so when it comes, you already know what to do.` · `THE WARNING HOUR`.
Cue words and times are from `audio/z1-s5.words.json` as on disk 12 Oct 26, 19:27 (wav 11.89 s, 30 words). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (Z1-S5 -0.31) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | Z1-S5 | 0 | Disasters | first sound 0.31 | 0.00 | first frame: ground and pair 1's line a, already on (a hard cut in on the first word) |
| 1 | Z1-S5 | 4 | but | 2.58 | 2.27 | pair 1's line b rises (`y: 14` set at 0, to 0 with the fade, 0.5 s, power2.out) |
| 2 | Z1-S5 | 9 | Learn | 5.02 | 4.71 | pair 1 fades out (0.25 s); pair 2's line a rises from 4.86 (`y: 16` to 0 with the fade, 0.5 s, power2.out) |
| 3 | Z1-S5 | 15 | so | 6.62 | 6.31 | pair 2's line b rises (0.5 s) |
| 4 | Z1-S5 | 25 | This | 10.06 | 9.75 | pair 2 dims to opacity 0.45 (0.3 s). It stays on screen |
| 5 | Z1-S5 | 28 | Warning | 10.84 | 10.53 | the wordmark lands: opacity 0 in CSS, `scale: 1.14` set at 0, a plain `to()` to opacity 1 and scale 1 (0.45 s, power3.out), as the library card |
After the last word there is no cue word: the last sound is at 11.23, the wordmark holds, and at 14.03 (15.23 less 1.2) the black div fades in (1.2 s, power2.in) so the last frame is black.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-z1s05-title.html` is the only file the builder writes; `data-composition-id="g-z1s05-title"`, `data-duration="15.23"`; id prefix `ttl-`; root `<div id="ttl-root" ...>` styled through `#ttl-root` (plan rule 3 overrides the template's and the library card's `id="root"`). Full frame, own ground on from frame 0, opaque to the last frame. The host is mounted in `index.html` as `host-z1s05-title`; do not edit `index.html`.
**What is copied from `library/inhouse/outro-brand.html` (hand-copied and retuned, never script-generated, as its header says):** the `.twh` wordmark (font, weight, size, letter-spacing, the amber word) and its entrance (a 0.45 s settle from 1.14 to 1, power3.out).
**What is not copied:** the `.ep` episode line and the `.tag` line (sample copy; this close speaks neither), the flat ground, the `#root` id, the `fromTo` and time-0 `set()` calls, and the card's own times (0.55, 1.8, 3.0, 6.8).
**What is retimed to this segment:** the wordmark moves from 0.55 to 10.53, the spoken "Warning"; the fade moves from 6.8 to 14.03 and is a black cover, not a fade of the wrapper.
**What is added from `episodes/ep6-katrina-2005/compositions/g-close.html`:** the two-line Georgia italic block above the brand (its sizes 52 and 36 px, its amber second line) and the slow breathing. Its letter-spacing tween and its sub line are not copied.
**Assets:** none. No image, no video, no audio, no drawing.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-z1s05-title`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `node scripts/blank_scan.mjs` with the episode's absolute path must name no hole inside this comp before 14.03.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: this is a type card on the channel ground; state the measured fill and say so. Line 3: frame 0 shows the ground and pair 1's first line. Line 4: seek to 4.80 (mid swap), 10.60 (mid landing) and 14.60 (mid fade) forward and backward and match the frames; the wordmark's scale and the lines' `y` are set at timeline 0, never only in a later tween's from vars.

## 8. Receipt
As template section 8, plus the wordmark's measured width and the size used.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground and `Disasters don’t ask permission.` Then settled frames: 1.50 (line a alone), 3.00 (pair 1 complete), 5.50 (pair 2 line a; pair 1 gone), 7.00 (pair 2 complete), 10.20 (pair 2 dimmed, no wordmark, frame not blank), 11.10 (wordmark settled under the dimmed pair, both readable, no overlap), 13.80 (the hold: still breathing), 14.60 (mid fade), 15.20 (last frame: black).
