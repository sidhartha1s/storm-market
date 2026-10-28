# g-a3-1-ban-namecard · A3-S1 0.00-11.60 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the ban chip `#mm-ban` in `compositions/g-intro-4-morning-map.html` (crimson card, Arial Black 38 "DRIVING BAN · 9:30 AM") and the glass chip + source pill in `compositions/g-intro-2-toll-chips.html`. Copy, rename every id/class, retime.

## 0. What this graphic claims
The 9:30 AM Friday driving ban (closing loop L2 from A2) shrinks away as the story narrows to one person: Anndel Taylor, 22.

## 1. SOURCE
- Ban 9:30 a.m. Fri 23 Dec: `research/response.md` section 1 row "Erie County ban effective time" ("effective 9:30 a.m. Friday", WKBW, SECONDARY): https://www.wkbw.com/news/local-news/erie-county-driving-ban-effective-9-30-a-m-friday
- Anndel Taylor, 22: `research/deaths.md` section 4 (CBS/CNN wire, updated 28 Dec 2022, SECONDARY): https://www.cbsnews.com/miami/news/woman-in-buffalo-found-dead-in-her-car-after-getting-trapped-by-snow-family-says/
- No photo of her is used (no licensed photo exists: `edit_script.md` A3-S1 row note). Text only, no monogram.

## 2. DATUM, SCALE, ORIENTATION
Overlay on footage, 1920 x 1080, root transparent. No scale. Presenter circle may be on: nothing at x >= 1600, y >= 680.

## 3. GEOMETRY (px)
- Ban chip `bn-ban`: box 670 x 80, radius 10, fill `#8e2020`, text "DRIVING BAN · 9:30 AM" Arial Black `font-weight:900` 38 px `#f4f0e8`, padded 96 px left as in `#mm-ban`. Start state (frame 0): left 110, top 110, scale 1. Corner state: `transformOrigin:"left top"`, scale 0.55, at left 96, top 54 (box then about 369 x 44, x 96-465, y 54-98).
- Name card `bn-name`: glass surface (tokens.md "Surfaces", radius 28), `left:110px; bottom:110px`, padding 22 px 34 px, hugs its text. One line: "ANNDEL TAYLOR" Arial Black 900 52 px `#f2f5f8`, then a span " · 22" Arial Black 900 52 px `#e8c56a`. Width about 560 px (x 110-670), y about 862-970.
- Source pill `bn-src` (as `tc-src`): glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`. Two pre-authored leaves toggled with autoAlpha: S-A "Erie County driving ban, WKBW"; S-B "CNN via CBS News, 28 Dec 2022".
- Type tiers: 52 (big), 38 (mid), 19 (small).
- Nothing right of x = 1100.

## 4. MUST BE TRUE IN THE PICTURE
1. Frame 0 shows the ban chip at full size, readable, top-left (continuity with A2's ban card).
2. The chip never overlaps the name card or the source pill, mid-tween included.
3. "ANNDEL TAYLOR" is spelled exactly so (Whisper writes "Andal"); "22" appears on the spoken "22", not before.
4. One source line visible at a time; S-B replaces S-A when the name card enters.
5. No photo, silhouette or monogram of her.
6. Over the soft-focus street the card reads: white on glass.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S1 start, `audio/a3-s1.words.json`)
Strings: `DRIVING BAN · 9:30 AM` · `ANNDEL TAYLOR` · ` · 22` · `Erie County driving ban, WKBW` · `CNN via CBS News, 28 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "One" @0.00 | ban chip and S-A visible from frame 0 (set in CSS + `tl.set` at 0) |
| 0.90 | "follow" @0.90 | ban chip `to(scale 0.55, x/y to corner, 0.8, power3.inOut)` |
| 2.12 | "Andal Taylor." @2.12 | name card in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` with "ANNDEL TAYLOR" only; S-A out / S-B in (0.3 s crossfade) |
| 3.68 | "22" @3.68 | " · 22" span `fromTo(autoAlpha 0, y:10 -> 0, 0.35, back.out(1.6))` |
| 9.16 | "driving" @9.16 | ban chip pulses once (`scale 0.55 -> 0.58 -> 0.55`, 0.5 s) |
| whole window | | name card floats `y 0 -> -4`, sine.inOut, yoyo, finite repeats; something moves at least every 4 s |
| 11.00-11.60 | after "car" @12.56 is the map's; exit before "The snow" @11.72 | all out: `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
Comp duration 11.60 s.

## 6. CONTRACT
One file `compositions/g-a3-1-ban-namecard.html`, root `id="g-a3-1-ban-namecard-root"` with `data-composition-id="g-a3-1-ban-namecard" data-width="1920" data-height="1080"`, PAUSED timeline at `window.__timelines["g-a3-1-ban-namecard"]`. Ids/classes prefixed `bn-` (never `.lt`, `.glasscard`, `.srclab`, `#root`). Start-hidden in CSS too. Rest: `references/mg-quickref.md`.
Footage under it (orchestrator mounts on a lower track for the whole window): `cc-laurel-street` (Andre Carrotflower, Corner of Main and Laurel Streets, Fri 23 Dec 2022 about 10:30 AM, CC BY-SA 4.0, `research/cc-clips-r2.md` V1), soft-focus blur applied in index.html. On-screen credit for that clip is the orchestrator's (description + corner credit per `cc-clips-r2.md` caveat 2).

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-1-ban-namecard`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-1-ban-namecard`.

## 7a. DONE LINE
All seven items of the template 7a. Item 7: a frame at 4.5 s composited over the blurred street clip.

## 8. RECEIPT
As the template.
