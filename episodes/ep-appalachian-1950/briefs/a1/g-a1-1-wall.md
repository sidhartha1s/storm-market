# g-a1-1-wall: chapter card, then the viewer-comment wall (A1-S1)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/title-card.html` (chapter card), `library/inhouse/snippets/cards.css` `.glasscard` (chip). Prefix every id and class `w1-`.
Sits over: nothing. Full-frame designed card on track 2, ground on from frame 0 (the chapter blackout before A1 ends on this frame).

## 0. Claim
Under the other videos about this storm almost every shared memory is snow; hardly anyone mentions the wind.

## 1. Source
`research/teardown-footage.md` "Viewer comments": 8 of 192 (Iconography), 6 of 92 (Noles), 1 of 8 (Vintage) mention wind or the coast; items 1 (born Nov 1950 in N.C., brought home as it began to snow) and 2 (Pittsburgh, 10 years old). No count goes on screen.

## 2. Datum, scale, orientation
The wall is a schematic of the ratio: 48 rows, 2 lit blue (about 4 %, matching 15 of 292 = 5 %), 34 lit white, 12 left dim. Comment text is paraphrased, blurred and unreadable at size; no usernames, no avatars, no like counts.

## 3. Geometry (px, 1920 x 1080)
- Ground: radial gradient `#0b1016` centre to `#030507` at 78 %.
- Chapter card (0 to 2.0 s): "THE SIDE NOBODY REMEMBERS" Arial Black 900 76 px `#f2f5f8` centred at y 500; eyebrow above it "ACT ONE" Arial 700 22 px `#93a3b2` tracking 6 at y 420; a 3 px `#7fb2e5` rule under the title, 600 px, centred, y 560.
- Wall (from 1.8 s): 3 columns x 16 rows of comment rows, columns at x 140, 700, 1260, each 500 px wide; rows 52 px pitch from y 150 to y 930. Bottom-right column ends its rows at y 640 (circle corner clear: x >= 1600, y >= 680 empty). Each row: a 26 px grey dot (no avatar image) + one paraphrased line, Georgia 26 px `#dfe7ee`, `filter: blur(5px)`, opacity 0.35. Write 48 different short paraphrases (snow, power-company dads, stranded drivers, a birth); never a real username or verbatim comment.
- Lit snow row: opacity 1, colour `#f2f5f8`, a 2 px white left bar. Lit wind row: colour `#7fb2e5`, 2 px `#7fb2e5` left bar, glow `0 0 18px rgba(127,178,229,.6)`. Wind rows: column 2 row 9, column 3 row 4.
- Highlight rows: Pittsburgh memory = column 1 row 6; N.C. baby = column 2 row 3. Highlight = row scales 1 to 1.06 with a 2 px white outline box; still blurred (unreadable).
- Chip (title zone): glass card left 110, top 70, padding 18 x 30, radius 28: "MOST MEMORIES: SNOW" Arial Black 900 52 px `#f2f5f8`. The rows under the chip box are left out of the wall (start column 1 at y 230).
- Source line: "Source: viewer comments under three YouTube videos on this storm" Arial 700 19 px `#c8d3e0` tracking 2, left 110, bottom 60.
- Tiers: 76 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. No comment is readable at 1080p and no username appears in any frame.
2. Blue rows are 2 of 48; white rows outnumber blue many times over in every frame after 3.96.
3. The chip says SNOW, not WIND; nothing on screen claims a count.
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a1-s1.words.json`, seconds from A1-S1 start)
Text: `ACT ONE` · `THE SIDE NOBODY REMEMBERS` · `MOST MEMORIES: SNOW` · `Source: viewer comments under three YouTube videos on this storm` · 48 blurred paraphrase lines.
- 0.00: chapter card on (title `fromTo` y 30 to 0, autoAlpha, 0.6 s, power3.out; rule scaleX 0 to 1, 0.5 s). `/* UNDER @0.00 */`
- 1.34 "storm,": card exits (y 0 to -40, autoAlpha 0, 0.5 s, power3.in); wall rows rise in by column (`fromTo` y 24 to 0, autoAlpha 0 to .35, stagger 0.02, 0.5 s). `/* STORM @1.34 */`
- 2.70 "memory": wall drifts up 0 to -40 px over the rest of the host (ease none, motion for the whole window). `/* MEMORY @2.70 */`
- 3.96 "snow.": 34 snow rows light white (stagger 0.03); chip in (`fromTo` x -60 to 0, autoAlpha, 0.6 s, power3.out). `/* SNOW @3.96 */`
- 6.68 "Pittsburgh.": Pittsburgh row highlight on. `/* PITTSBURGH @6.68 */`
- 8.20 "baby,": Pittsburgh highlight off, N.C. row highlight on. `/* BABY @8.20 */`
- 11.12 "snow.": highlight off. `/* SNOW @11.12 */`
- 13.38 "wind,": the two wind rows light blue with a pulse (scale 1 to 1.08 to 1, 0.5 s). `/* WIND @13.38 */`
- 14.44 "coast,": every white row dims to .25; the blue rows stay lit. `/* COAST @14.44 */`
- 15.42 "wind": blue rows pulse again, glow grows. `/* WIND @15.42 */`
- Exit: last 0.6 s: chip slides out (x -60, autoAlpha 0, power3.in); wall fades to ground. Cut to g-a1-2.
Host: data-start = A1-S1 start, duration = 16.602 + 0.40 = 17.00 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
