Host: id=g-a3s11-onoff file=compositions/g-a3s11-onoff.html start=567.36 (timeline-map.md table 1; the mount in index.html wins) duration=12.69 s (wav 12.40 s plus its gaps) track=2

# g-a3s11-onoff · A3-S11 · a station on emergency power, on the air and off it (wave 3, drawing)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county chip belongs in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). The blink count is checked against the spoken window (rule 13).
**Spoken (A3-S11):** "With the power went radio and TV, in many areas. One station told the researchers all power to its studio and transmitter was out, and it broadcast on and off from emergency power."
**One look:** one microphone, its ON AIR lamp going out, then coming back in fits.

## 0. What this graphic claims
When the power failed, radio and television went with it in many areas. One station, not named, told the researchers that all power to its studio and transmitter was out and that it broadcast only on and off, from emergency power.

## 1. Source
- `edit_script.md` A3-S11, Rows [D; study printed p. 16] and [D; study printed p. 24], with the writer's note: no time, no name and no county in the study.
- Quote strip words, from the Picture note: "broadcasting was on an intermittent basis", attribution "media personnel · Disaster Research Center, 1966". The page is not shown.
- Microphone: `media/drawings/microphone.svg`. ON AIR lamp: the built `compositions/g-i1s5-onair.html` (`.air-lamp`), in the off state defined in `mg_specs/briefs/g-a1s15-offices.md`.

## 2. Datum, scale, orientation
One object, centred on x 960. The microphone is 2.6 times its file size. There is no clock and no time in this comp: the study gives none. The lamp is the only thing that changes state after the strip arrives; "on" and "off" are the two lamp states, and the blink has no fixed rhythm that could be read as a signal.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window |
| Microphone | `media/drawings/microphone.svg` inline, `translate(804 170) scale(2.6)` (object box x 804 to 1116, y 170 to 768), `stroke-width="2.3"` on the `dw-...` group (6 px lines). Lit: lines Body light, body fills Panel dark. Dark: lines `#55606b` (Label grey at 55 %, pre-mixed, as the drawings README) |
| Microphone's small lamp | the file's `dw-lamp` circle, object (104, 20): screen centre (1074.4, 222), radius 23.4. Popfig red when the ON AIR lamp is on, Panel dark when it is off; it changes with the ON AIR lamp in the same tween |
| ON AIR lamp | the `.air-lamp` of the built `compositions/g-i1s5-onair.html` (130 x 36, radius 6, 2 px outline, Arial Black 900 18 px, letter-spacing 1 px) at 2 times: 260 x 72, radius 12, 4 px outline, Arial Black 900 36 px, letter-spacing 2 px, text `ON AIR`. Left 830, top 70 (x 830 to 1090, y 70 to 142), centred over the microphone. **On** = the built lamp's lit state (Popfig red fill, its letters as built). **Off** = no fill, outline and letters `#55606b` |
| Label | `a station`, Arial 700 26 px, Body light, centred on x 960, top 786 |
| Quote strip | Beige polaroid, left 96, top 850, 1480 x 130 (right 1576, bottom 980), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote, Georgia 52 px, Caption dark, left 136, top 862: `“broadcasting was on an intermittent basis”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 932: `media personnel · Disaster Research Center, 1966`. Measure the quote's width in a frame and state it; it must end at least 40 px inside the strip's right edge |
| Source line | none: the strip's attribution is the frame's source (design sheet section 10) |

## 4. Must be true in the picture
1. The lamp is on in the first frame and goes off on "went". It is never on between that cue and the word "on" of "on and off".
2. From "on" to the end the lamp changes six times in all: on, off, on, off, on, off. It ends off and stays off to the last frame.
3. Every lamp change is a fill and letter colour change in 0.15 s. No scale, no glow, no sound lines, no rays.
4. The microphone has no name, no call letters, no frequency and no county. The label reads `a station` and nothing more. No time is printed: the study gives none.
5. Nothing in this comp says which station this is or ties it to the station of the next comp (`g-a3s12-seven`): no clock, no "7:00", no "7:45", no transmitter drawing.
6. The quote strip carries its attribution and enters only in the second sentence.
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680 (the strip ends at x 1576).

## 5. Text (exact) and cues
Text: `ON AIR` · `a station` · `“broadcasting was on an intermittent basis”` · `media personnel · Disaster Research Center, 1966`.
Cue words and times are from `audio/a3-s11.words.json` as it is on disk on 12 Oct 26 (19:32). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S11 -0.45) plus the word's time; the first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S11 | 0 | With | 0.45 | 0.00 | first frame: ground, the microphone lit (Body light), ON AIR lamp on, small lamp red |
| 1 | A3-S11 | 3 | went | 1.06 | 0.61 | the lamp goes off (0.15 s); the small lamp goes Panel dark with it |
| 2 | A3-S11 | 11 | station | 4.54 | 4.09 | label `a station` comes in (0.3 s, `y:12` set at 0, to 0, with the fade) |
| 3 | A3-S11 | 14 | researchers | 5.32 | 4.87 | the quote strip rises (`y:60` set at 0, to 0, with the fade, 0.4 s, power3.out) |
| 4 | A3-S11 | 23 | out | 8.34 | 7.89 | the microphone's lines fall from Body light to `#55606b` (0.4 s): the whole object is dark |
| 5 | A3-S11 | 27 | on | 9.68 | 9.23 | the lamp comes on (0.15 s) and the microphone's lines return to Body light with it |
| 6 | A3-S11 | 29 | off | 10.60 | 10.15 | the lamp goes off and the lines go dark (0.15 s) |
| 7 | A3-S11 | 31 | emergency | 11.08 | 10.63 | the lamp comes on; then off 0.40 s after this cue (11.03), on at 0.80 s (11.43), off at 1.20 s (11.83). The lines follow the lamp each time. It stays off to 12.69 |
Blink check (rule 13): three on states after "on" (0.92 s, 0.40 s, 0.40 s long); the last change is at 11.83, 0.86 s before the comp ends at 12.69. Finite: every change is its own tween at an absolute time, no `repeat`.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s11-onoff.html` is the only file the builder writes; `data-composition-id="g-a3s11-onoff"`; id prefix `onoff-`; root `<div id="onoff-root" ...>` styled through `#onoff-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the microphone and ON AIR lamp group of `compositions/g-a1s15-offices.html` (wave 1; brief `mg_specs/briefs/g-a1s15-offices.md`, its A1-S16 and A1-S17 views) for the lamp's two states; the lamp itself from the built `compositions/g-i1s5-onair.html`; the strip from `compositions/g-a1s13-chain.html` (wave 1). No later comp copies this one. `g-a6s10-watch` shows the same lamp lit and takes its numbers from `g-a1s15-offices`, not from here.
**Assets (paths from the episode folder):** `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, line 4): inlined, ids under `onoff-`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s11-onoff`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 11.25 forward, then seek 0, 12.5 and back to 11.25; the lamp must be off in both captures. Line 6: the six lamp change times are stated in the receipt beside the words.json times they came from.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): microphone lit, lamp on. Then settled frames: 0.90 (lamp off), 4.50 (label), 5.40 (strip, quote inside its right margin), 8.40 (whole object dark), 9.50 (lamp on, lines bright), 10.40 (off), 10.85 (on), 11.25 (off), 11.65 (on), 12.30 and 12.65 (off, holding).
