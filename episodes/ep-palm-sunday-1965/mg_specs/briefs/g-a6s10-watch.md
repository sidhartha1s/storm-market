Host: id=g-a6s10-watch file=compositions/g-a6s10-watch.html start=1095.18 (timeline-map.md table 1; the mount in index.html wins) duration=13.79 s track=2

# g-a6s10-watch · A6-S10 · forecast and warning, and the word that was changed (wave 5, drawing family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 1, 2, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: the lamp of the built `compositions/g-i1s5-onair.html` and `mg_specs/briefs/g-a1s15-offices.md` (A1-S17, microphone with its lamp red).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). A flash is a stroke or fill change, never a scale pop (rule 12). Paper is their words, glass is our label (design sheet section 1).
**Spoken (A6-S10):** "Radio, TV and newspapers were already explaining the difference between a forecast and a warning. Many people, the Weather Service says, had taken a warning for a mere update, so the tornado forecast was renamed the tornado watch."
**One look:** a microphone on the air beside two typed strips, FORECAST over WARNING; then, on glass, FORECAST struck through and WATCH under it.

## 0. What this graphic claims
The 1966 study found the media already explaining the difference between a tornado forecast and a tornado warning. The National Weather Service says many people took a warning for an update, and that the term "tornado forecast" was changed to "tornado watch". No year is given for the change.

## 1. Source
- `edit_script.md` A6-S10, Rows [G; study printed p. 30] and [G; LOT, read by the fact check: "they simply thought a warning was an 'update'"; "the term 'tornado forecast' was changed to 'tornado watch'"] (a Weather Service statement; no year given, no 1965 document read).

## 2. Datum, scale, orientation
The microphone is `media/drawings/microphone.svg` at scale 1.6 (object box 192 x 368) at x 220 to 412, y 300 to 668. The two paper strips are the study's two terms, so they are paper; the renamed pair is the Weather Service's later statement in our setting, so it is glass. The two groups never overlap: paper x 520 to 1140, glass x 1200 to 1800, both above y 680.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Microphone | `media/drawings/microphone.svg` inline, `translate(220 300) scale(1.6)`, `stroke-width="2.5"` on the group (4 px lines); lines Body light, body Panel dark. Lamp (`dw-lamp`) Panel dark at rest, Popfig red when on the air, as the built `g-i1s5-onair.html` lamp. No station name, no call letters |
| Strip 1 | Beige polaroid, left 520, top 330, 620 x 110 (right 1140, bottom 440), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Text Courier New 700 56 px, Caption dark, left 560, top 354: `TORNADO FORECAST` |
| Strip 2 | same, top 470 (bottom 580). Text top 494: `TORNADO WARNING` |
| Pulse | an Amber 2 band at 25 % the size of strip 2, wiped left to right with `scaleX` and gone (design sheet section 5 "Pulse") |
| Source A | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 30` |
| Glass card | glass plate as the clock stamp's, left 1200, top 300, 600 x 300 (right 1800, bottom 600) |
| Glass line 1 | Courier New 700 44 px, Headline white, left 1240, top 350: `TORNADO FORECAST` |
| Strike | a Body light line, 4 px, round caps, across glass line 1 at its mid height (y 376), from x 1232 to the text's measured right edge plus 8 px; drawn left to right with `strokeDashoffset` |
| Glass line 2 | Courier New 700 44 px, Headline white, left 1240, top 470: `TORNADO WATCH` |
| Source B | same place as source A, a second pre-authored element: `National Weather Service, Chicago` |
Text widths are estimates until read on a frame: strip text about 540 px, glass text about 425 px. Each must end 30 px or more inside its plate.

## 4. Must be true in the picture
1. The two terms on paper are the study's: `TORNADO FORECAST` and `TORNADO WARNING`, forecast above warning.
2. The struck word is `TORNADO FORECAST` and the new word is `TORNADO WATCH`. `TORNADO WARNING` is never struck, dimmed or replaced.
3. The renamed pair is on glass, not paper, and its source reads `National Weather Service, Chicago`. No year is on screen.
4. The strike is Body light, not red: red means "nobody was told".
5. One source line per frame, and it names the source of what is newest on screen.
6. Nothing in x >= 1600 and y >= 680 (the glass card ends at y 600). Nothing appears before its spoken word.

## 5. Text (exact) and cues
Text: `TORNADO FORECAST` (twice: once on paper, once on glass) · `TORNADO WARNING` · `TORNADO WATCH` · `Disaster Research Center, 1966, p. 30` · `National Weather Service, Chicago`.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: -0.21) plus the word's time; the first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S10 | 0 | Radio, | 0.00 | 0.00 | first frame: the microphone, lamp at rest; it is drawn already (no empty frame) |
| 1 | A6-S10 | 1 | TV, | 0.98 | 0.77 | the lamp turns Popfig red (0.2 s) |
| 2 | A6-S10 | 6 | explaining | 2.60 | 2.39 | source A fades in (0.3 s, `y:12` to 0) |
| 3 | A6-S10 | 11 | forecast | 4.18 | 3.97 | strip 1 rises (`y:40` to 0 with the fade, 0.35 s, power3.out) |
| 4 | A6-S10 | 14 | warning. | 5.00 | 4.79 | strip 2 rises the same way |
| 5 | A6-S10 | 18 | Weather | 6.86 | 6.65 | source A gives way to source B (0.3 s cross fade) |
| 6 | A6-S10 | 24 | warning | 8.56 | 8.35 | the pulse wipes across strip 2 (0.5 s) and leaves |
| 7 | A6-S10 | 29 | so | 10.14 | 9.93 | the glass card rises with glass line 1 on it (`y:40` to 0 with the fade, 0.35 s) |
| 8 | A6-S10 | 34 | renamed | 11.46 | 11.25 | the strike draws across glass line 1 (0.4 s) |
| 9 | A6-S10 | 36 | Tornado | 12.10 | 11.89 | glass line 2 fades in (0.25 s) |
| 10 | end | | | | 13.79 | comp ends on the hold |
The longest stretch without a new mark is 3.56 s (4.79 to 8.35); the source swap at 6.65 sits inside it.

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a6s10-watch.html` only. Id prefix `wat-`, root id `wat-root`. Base it copies: the lamp of the built `compositions/g-i1s5-onair.html`; the glass plate values of `compositions/g-a1s01-kc.html` (wave 1). Asset mounted: `media/drawings/microphone.svg`, inline. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. State the frame coverage figure; if it is under the floor of `references/mg-quickref.md` "Frame coverage", enlarge the two groups about their centres and report the new boxes.

## 8. Receipt
As the template's section 8, plus: the measured widths of the four text lines and the strike's end x.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 1.10 (lamp red); 2.80; 4.40 (strip 1); 5.20 (both strips); 7.00 (source B); 8.60 (pulse mid wipe); 10.40 (glass card); 11.70 (strike); 12.30 (both glass lines); last frame 13.70.
