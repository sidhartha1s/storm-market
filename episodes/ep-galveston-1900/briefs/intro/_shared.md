# Intro section: rules shared by every brief in this folder (ep-galveston-1900, 26 Oct 26)
Every brief here points at this file for the parts that are the same for all ten graphics. Read it with the brief, then `references/mg-quickref.md`, `library/inhouse/snippets/tokens.md` and `learnings/mg.md` before building.

## Status of the words this section is timed to
- All cue times are seconds from the start of that segment's wav, read from `episodes/ep-galveston-1900/audio/<seg>.words.json` (whisper writes digits: "6 ,000", "38 ,000", "4th", "1900,"). Durations are `audio/manifest.json` (tempo 0.94).
- The hook (H1-S1 to H1-S5) is a PROVISIONAL pick. If the owner picks another hook shape, only g-intro-1 to g-intro-5 are redone; g-intro-6 to g-intro-10 stand unless the tail or intro text changes.
- The section is not locked (grade 7 of 8, owner approval pending). A changed segment means its words.json changes: retime from the new file, never by offset.
- Whisper spells Cline as "Klein"/"Kline" in the words files. On screen it is always CLINE.

## Segment-to-host time
A comp that sits inside one segment: host `data-start` = that segment's narration `data-start` in index.html plus the first cue named in the brief. A comp spanning several segments (g-intro-8): comp-local time of a word = (that segment's narration `data-start` − host `data-start`) + the word time. Read the `nx-<seg>` mounts in index.html; never assume the gaps between segments.

## Common placement (1920 x 1080)
- Source line: TOP-LEFT in this whole section, `left:96px; top:54px`, Arial 700 19 px, `#c8d3e0`, on the glass surface (tokens.md "Surfaces", radius 12 for this small size), padding 6px 14px, max width 900 px, two lines allowed. Reason: the bottom-right corner (x >= 1600, y >= 680) belongs to the presenter circle from the intro on, and the bottom-left is the lower-third zone.
- Lower-third: `left:110px; bottom:110px` (cards.css `.lt`), name line Arial Black 900 52 px `#f2f5f8`, role line Arial 700 27 px `#f5d98b`, both on one glass card (no bare text on footage). Enter `fromTo(x:-60, autoAlpha 0 -> x 0, autoAlpha 1, 0.6, power3.out)`; exit `to(x:-980, autoAlpha 0, 0.6, power3.in)`.
- Chip: one glass card (tokens.md surfaces, radius 28), Arial Black 900 44 px `#f2f5f8` main line, optional tag line Arial 700 22 px `#93a3b2` tracking 4 under it. Position named per brief. Enter `fromTo(y:24, autoAlpha 0 -> y 0, autoAlpha 1, 0.45, back.out(1.6))` plus `scale 0.94 -> 1`; exit `to(x:980, autoAlpha 0, 0.6, power3.in)`.
- Popfig: cards.css `.popfig` (Abril `AbrilFig` from `fonts/AbrilFatface-Regular.ttf`, vendor it into the episode `fonts/` from `references/editing-patterns/fonts/`), big line `#d0121f` with the cards.css text-shadow, sub line Arial 700 32 px `#e8e3d8`. Big line 16 characters or fewer, 3 words or fewer. Enter `fromTo(scale 1.35, autoAlpha 0 -> scale 1, autoAlpha 1, 0.5, power4.out)`; exit `to(scale 0.92, autoAlpha 0, 0.45, power2.in)`. Never over a card or a map comp.
- Drift so nothing idles: every visible text card floats `y` +-4 px, `sine.inOut`, 2.4 s yoyo with finite repeats sized to the host, from its land time. Overlay comps have no background (root transparent): the footage named in the brief sits on a lower track for the whole host window.
- One text element per zone at a time; a chip exits before the next chip in the same zone enters unless the brief says they stack.

## 6. CONTRACT, 7. TOOLS, 7a. DONE LINE, 8. RECEIPT
As `references/mg-brief-template.md` sections 6 to 8, word for word, with COMPID = the comp id named in the brief and slug `ep-galveston-1900`. Root id is `<comp id>-root`, never `root` (mg-quickref "File contract"). Edit only your own `compositions/<comp id>.html`.
