Host: id=g-a1s05-clocks file=compositions/g-a1s05-clocks.html start=(timeline-map.md) duration=9.13 s (wav sum 8.83 s plus gaps from timeline-map.md) track=2

# g-a1s05-clocks · A1-S5 · the office's clock and the family's clock (wave 1, second base of the clock family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 6, 7, 8, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3a row DR-09.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1; the built hook comps' `fromTo` at a cue is not copied). The root is styled through its id and is never `id="root"` (rule 3). A shared drawing is read alone at the size it is mounted (rule 11: the empty clock face at 186 px, the house at 364 px). A flash is a stroke or fill change, never a scale pop (rule 12: the pulse on "family").
**Spoken (A1-S5):** "Every forecast time in the study is the time a Weather Bureau office got it. It isn't the time a family heard it, and that's the clock to watch."
**One look:** a clock that reads 11:45 beside a clock with no hands at all, next to a dark house.

## 0. What this graphic claims
The times in the 1966 study are the times a forecast reached a Weather Bureau office. The study gives no time at which a family heard it: that clock is empty.

## 1. Source
- `edit_script.md` A1-S5, Rows [study printed p. 6, footnote: the SELS forecast times "refer to the time the forecast first entered the system via local Weather Bureaus, and not the time that the general public became aware of the threat"]. Picture note: "two clocks side by side. Left, the clock stamp 'an office · 11:45 AM EST', lit amber. Right, beside the drawn house, a clock face with no hands. Small source line 'Disaster Research Center, 1966, p. 6 (footnote)'. The empty clock face pulses once on 'family'."
- The time on the left clock is the forecast time of A1-S1, 11:45 AM Eastern (design sheet section 8, comp 07: hour hand 352.5 degrees, minute hand 270).
- The zone: the Picture note writes "EST". It does not fit beside the time in the stamp, so the place line carries it as `Eastern time`, the voice's own words in A1-S1 and the wording of the stamps in `mg_specs/briefs/g-a1s09-forecasts.md` and `mg_specs/briefs/g-a1s01-kc.md` (the lead may rule it back to `EST`).
- No photograph is mounted in this comp, so no `provenance.csv` row applies. The three drawing files were confirmed on disk on 12 Oct 26: `wall-clock.svg` 1,205 bytes, `wall-clock-nohands.svg` 825 bytes, `house.svg` 978 bytes.
- Drawings: `media/drawings/wall-clock.svg` (hands), `media/drawings/wall-clock-nohands.svg` (no hands; same viewBox and classes), `media/drawings/house.svg` (dark state: lines Label grey at 55 %, pre-mixed `#55606b`, windows Panel dark).

## 2. Datum, scale, orientation
- One centre line, y 540: the stamp's clock face, the empty clock face and the house all sit on it.
- The stamp is design sheet section 8 at 1.4 times: every number of that section (and of the built `.st6-stamp` in `compositions/g-i1s4-states.html`) multiplied by 1.4. Card 826 x 280.
- Empty clock face: the drawing at scale 1.5 (object box 186 x 186, lines 6 px). House: the drawing at scale 1.4 (object box 364 x 350, lines 5.6 px, aerial rising 47.6 px above the box).
- Hands, clockwise degrees from 12: hour 352.5, minute 270.
- Everything ends left of x 1600 (the house's right edge is x 1584), so the presenter corner is empty.

## 3. Geometry (screen px)
Ground: the canvas gradient (design sheet section 2) on the root, on from frame 0.
| Element | Px |
|---|---|
| Stamp card | glass card (tokens.md "Surfaces"), left 110, top 400, 826 x 280 (right 936, bottom 680) |
| Stamp clock face | `wall-clock.svg` inline in a full-frame `<svg>`, `<g transform="translate(156.2 453.2) scale(1.4)">`: object box 173.6 px, centre (243, 540), lines 5.6 px, ticks 4.2, hands 7. Rim fill Panel dark, lines Body light. Hour hand at 352.5 degrees, minute hand at 270, set once, never moved |
| Stamp eyebrow | left 373, top 428, Arial 700 28 px, Label grey, `letter-spacing:8.4px`, upper case: `AN OFFICE` |
| Stamp time | left 373, top 464, Courier New 700 118 px, Amber 2, `letter-spacing:-5.6px`, `line-height:1`: `11:45 AM` (about 520 px wide, ends near x 893, inside the card) |
| Stamp place line | left 376, top 607, Arial 700 36 px, Body light: `Eastern time` |
| Empty clock face | `wall-clock-nohands.svg` inline, `<g transform="translate(990 447) scale(1.5)">`: object box x 990 to 1176, y 447 to 633, centre (1083, 540), lines 6 px, ticks 4.5. Group stroke Label grey, rim fill Panel dark. No hands, no digits |
| House | `house.svg` inline, `<g transform="translate(1220 365) scale(1.4)">`: object box x 1220 to 1584, y 365 to 715; aerial top y 317.4; lines 5.6 px in the file's dark stroke, windows Panel dark |
| House label | centred on x 1402, top 729, Arial 700 26 px, Body light: `a family` (design sheet section 6 wording) |
| Source line | design sheet section 10: left 96, bottom 60: `Disaster Research Center, 1966, p. 6 (footnote)` |
The empty bands are 29.4 % of the frame above the aerial and 30.1 % below the house label.

## 4. Must be true in the picture
1. The left clock reads 11:45: hour hand just short of 12, minute hand on 9. The typed time beside it says the same, in Amber 2.
2. **The right clock has no hands, no time and no digits, at any frame.** No question mark, no dashes, no "unknown": the face is empty because the study gives nothing to put on it.
3. The stamp says `AN OFFICE`. It names no city: not Kansas City, not South Bend. The place line is `Eastern time` and nothing else.
4. The house is dark for the whole comp: no amber window, no lit line. Nobody in it has heard.
5. No line, arrow or link joins the two clocks or the stamp and the house. They are two separate things side by side.
6. The pulse on "family" is a stroke colour change on the empty face (Label grey to Headline white and back), never a change of size (rule 12).
7. No person is drawn; the house has no figure at a window.
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `AN OFFICE` · `11:45 AM` · `Eastern time` · `a family` · `Disaster Research Center, 1966, p. 6 (footnote)`.
Cue words and times are from `audio/a1-s5.words.json` as it stood on 12 Oct 26 at 18:55, after the voice conversion's re-transcription (wav 8.827 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (-0.40) plus the word's time; the first word takes the "first sound" column (0.00). The gap is therefore already in the last time column. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S5 | 0 | Every | 0.00 | 0.00 | first frame: ground and the stamp, already in place: card, clock at 11:45, `11:45 AM`, `Eastern time`. The eyebrow is not on yet. Nothing on the right |
| 1 | A1-S5 | 5 | study | 1.68 | 1.28 | source line fades in (`y:12` set at 0, then `to y:0, autoAlpha:1`, 0.3 s) |
| 2 | A1-S5 | 12 | office | 3.26 | 2.86 | eyebrow `AN OFFICE` fades in (0.3 s) |
| 3 | A1-S5 | 15 | It | 5.10 | 4.70 | the house draws on (`strokeDashoffset`, longest line first, 0.6 s); the empty clock face draws on beside it from 4.85 (0.5 s; its hub fades in, it is a zero-length line) |
| 4 | A1-S5 | 20 | family | 5.96 | 5.56 | `a family` rises under the house (`y:16` set at 0, then `to`, 0.3 s); the empty face pulses once: its group stroke goes Label grey to Headline white (0.25 s), then back to Label grey (0.5 s) |
| 5 | A1-S5 | 26 | clock | 7.56 | 7.16 | the stamp (card, face, text) goes to opacity 0.45 (0.4 s); the empty face's stroke goes to Body light and stays (0.4 s). Hold to the last frame (9.13) |
Step 5 is not in the Picture note. It is there so the last clause ("that's the clock to watch") has a visible change; if the lead strikes it, the comp holds on step 4.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a1s05-clocks.html` is the only file the builder writes; `data-composition-id="g-a1s05-clocks"`; id prefix `clk-`; root `<div id="clk-root" ...>` styled through `#clk-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**This comp is a family base (clock family, with `g-a2s06-headstart`).** `acts-plan.md` section 5 puts both in wave 1. What later comps take from this one, once it has passed its read: the clock stamp built on the drawing file (`wall-clock.svg` inline, hands set by `rotation` with `svgOrigin`) and a drawn clock standing beside a drawn object. The comps that use it are `g-a5s07-marion` (A5-S8, a stopped wall clock beside a stamp) and `g-a5s18-curran` (wave 4). Keep the stamp in its own block of CSS and markup so it lifts out whole, and write its numbers as the design sheet's times a single factor (1.4) so a copy can set the factor back to 1. Send it alone for a full-size read before anything copies it (template section 7a, last line).
It copies the stamp's values from the built `compositions/g-i1s4-states.html` (`.st6-stamp`, `.st6-time`, `.st6-place`, and the 11:45 hand angles), under this comp's class names, with the face taken from the drawing file in place of that comp's scripted face.
Inline mounts: copy each file's `<g class="dw-...">` into the comp's own `<svg>` inside the static `<g transform=...>` wrapper given in section 3; GSAP touches only the children. Give the hands ids and set `svgOrigin` once at build, before any tween, in screen px: (243, 540). The files carry classes only: every id takes the `clk-` prefix.
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136), inlined at scale 1.4.
- `media/drawings/wall-clock-nohands.svg` (DR-09 state file, same viewBox), inlined at scale 1.5.
- `media/drawings/house.svg` (dark state, object box 260 x 250, viewBox -6 -42 272 298), inlined at scale 1.4.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s05-clocks`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the measured bands against the 29.4 % and 30.1 % of section 3. Line 3: frame 0 shows the stamp complete (less its eyebrow), not a bare ground. Line 6: the stamp's numbers are the design sheet's section 8 numbers times 1.4, computed by a script and stated in the receipt with the two hand angles. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the stamp at 11:45 on both, no eyebrow, nothing on the right. Then one settled frame per cue: 1.70 (source line), 3.30 (`AN OFFICE`), 5.45 (house and empty face drawn, face in Label grey, no hands), 5.80 (the pulse at its brightest: stroke only, same size as at 5.45), 6.50 (face back to Label grey, `a family` on), 7.70 (stamp dimmed, empty face Body light), 9.10 (last frame). Each cue second in both seek orders.
