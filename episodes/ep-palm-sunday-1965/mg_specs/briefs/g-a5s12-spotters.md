Host: id=g-a5s12-spotters file=compositions/g-a5s12-spotters.html start=924.74 (timeline-map.md table 1; the mount in index.html wins) duration=8.02 s (wav 7.72 s plus its gaps) track=2

# g-a5s12-spotters · A5-S12 · almost no trained spotters: the office waits on a telephone call (wave 4, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 6, 7, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county chip belongs in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A5-S12):** "There was almost no trained spotter network. For Marion, the warning office was waiting on a telephone call, like everyone else."
**One look:** an office at one end, a town at the other, and one long dotted line between them with nothing on it.

## 0. What this graphic claims
In 1965 there was almost no network of trained spotters between a town and its Weather Bureau office. For Marion, the warning office had no way to know sooner than a telephone call from the town.

## 1. Source
- `edit_script.md` A5-S12, Rows [E, Curran: "The trained spotter network was primitive, mostly nonexistent."] and [C16; the fact check's wording].
- Quote strip words, from the Picture note: "primitive, mostly nonexistent", attribution "John Curran, on the trained spotter network".
- Layout: the chain's front end of `mg_specs/briefs/g-a2s20-front.md` (A2-S20), which stands on the intro chain's slots (design sheet section 6, built `compositions/g-i1s9-chain.html`).

## 2. Datum, scale, orientation
The chain line is y 520. The town's house and its telephone stand exactly where `g-a2s20-front` put them (house in the intro's station 5 slot). The office desk stands at the far left, in the intro's station 1 slot, so the line between them is as long as the frame allows: 815 px with nothing on it. Five spotter slots are fixed on that line, 140 px apart, and stay empty here; `g-a6s08-spotters` fills the same five.
| Spotter slot | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Centre x (y 520) | 470 | 610 | 750 | 890 | 1030 |

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window |
| Office desk | `media/drawings/desk.svg` inline, `translate(96 490) scale(0.85)` (box x 96 to 351, y 490 to 618; top surface y 524; its own telephone x 186 to 262, y 487 to 524, handset on the cradle); lines Body light |
| Desk label | `the warning office`, Arial 700 22 px, Label grey, left 96, top 676 |
| Long link | y 520, x 351 to 1166, dotted (4 px dots, 14 px gap: `stroke-dasharray="0.1 14"`, round caps), Label grey. Nothing is drawn on it: no dot, no mark, no ring at any of the five slots |
| Town telephone | `media/drawings/telephone.svg` inline (handset on the cradle), `translate(1166 537.2) scale(1.2)` (body x 1166 to 1274, base y 590, handset top y 516); lines Body light |
| Short link | y 520, x 1274 to 1400, solid, 4 px, Label grey (the town's own telephone) |
| House | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)` (box x 1400 to 1577, y 430 to 600, aerial to y 407); `stroke-width="5"` on the group (3.4 px lines); lines Body light, windows Panel dark |
| House label | `Marion`, Arial 700 22 px, Label grey, centred on x 1488, top 676 |
| Quote strip | Beige polaroid, left 96, top 780, 960 x 124 (right 1056, bottom 904), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote, Georgia 52 px, Caption dark, left 136, top 792: `“primitive, mostly nonexistent”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 862: `John Curran, on the trained spotter network`. Measure the quote's width in a frame and state it; it must end at least 40 px inside the strip's right edge |
| Source line | none: the strip's attribution is the frame's source (design sheet section 10) |

## 4. Must be true in the picture
1. Between the desk and the town's telephone there is one dotted line and nothing else. No spotter mark, no dot, no person, no car, no radio arc.
2. No light travels any link in this comp. The call has not come: both handsets are on their cradles from first frame to last.
3. The desk is at the left and the town at the right, the same way round as `g-a2s20-front`; the house and the town telephone are within 2 px of that comp's positions.
4. The house is labelled `Marion`, the town the narration names. The desk is labelled `the warning office`, the narration's words; no other office or town is named.
5. The quote reads `“primitive, mostly nonexistent”` and carries Curran's name. It is his description of the spotter network, and the attribution says so.
6. No time, no clock, no stamp: the 9:07 PM report belongs to `g-a5s10-alert`.
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680 (the house label ends left of x 1600; the strip ends at x 1056).

## 5. Text (exact) and cues
Text: `the warning office` · `Marion` · `“primitive, mostly nonexistent”` · `John Curran, on the trained spotter network`.
Cue words and times are from `audio/a5-s12.words.json` as it is on disk on 12 Oct 26 (19:32). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A5-S12 -0.34) plus the word's time; the first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S12 | 0 | There | 0.34 | 0.00 | first frame: ground, the office desk and its label |
| 1 | A5-S12 | 3 | no | 0.80 | 0.46 | the long dotted link draws from the desk to x 1166 (0.9 s, ease none): a long line with nothing on it |
| 2 | A5-S12 | 6 | network. | 1.90 | 1.56 | the quote strip rises (`y:60` set at 0, to 0, with the fade, 0.4 s, power3.out) |
| 3 | A5-S12 | 8 | Marion, | 3.02 | 2.68 | the house draws on (0.6 s, longest line first), label `Marion` |
| 4 | A5-S12 | 11 | office | 4.28 | 3.94 | the desk's lines turn Headline white (0.3 s) and stay |
| 5 | A5-S12 | 13 | waiting | 4.82 | 4.48 | the telephone on the desk turns Amber 2 and back to Headline white three times (0.5 s each, finite): the office is listening for it |
| 6 | A5-S12 | 16 | telephone | 5.36 | 5.02 | the town's telephone draws on with its short solid link to the house (0.4 s), handset down |
| 7 | A5-S12 | 19 | everyone | 6.52 | 6.18 | the desk's lines return to Body light (0.3 s). Hold to 8.02: the long link still grey and empty |
Pulse check (rule 13): three pulses of 0.5 s from 4.48 end at 5.98, before step 7 at 6.18.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s12-spotters.html` is the only file the builder writes; `data-composition-id="g-a5s12-spotters"`; id prefix `spot-`; root `<div id="spot-root" ...>` styled through `#spot-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the chain family base `compositions/g-a1s13-chain.html` (wave 1; brief `mg_specs/briefs/g-a1s13-chain.md`) for links, dotted style and the strip; the front end of `compositions/g-a2s20-front.html` (wave 2; brief `mg_specs/briefs/g-a2s20-front.md`) for the house and town telephone positions. **Copied by:** `g-a6s08-spotters` (wave 5) keeps every box of section 3 and draws its spotter marks at the five slot centres of section 2.
**Assets (paths from the episode folder):** `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, line 4), `media/drawings/telephone.svg` (viewBox -6 -58 102 106, line 3), `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, line 4, telephone 3): inlined, ids under `spot-`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s12-spotters`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the house, telephone and slot positions are the numbers of `g-a2s20-front` and of section 2, copied, and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): desk and label only. Then settled frames: 1.45 (the long link whole, empty), 2.10 (strip, quote inside its right margin), 3.40 (house and `Marion`), 4.30 (desk white), 4.75 and 5.00 (one pulse: telephone amber, then white), 5.50 (town telephone and short link, handset down), 6.60 and 7.90 (desk back to Body light, link empty).
