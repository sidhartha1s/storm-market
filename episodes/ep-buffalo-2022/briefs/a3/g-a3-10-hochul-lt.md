# g-a3-10-hochul-lt · A3-S9 3.20-6.70 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the `.lt` lower-third in `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass surface). Rename every class (index.html uses `.lt`).
BLOCKED on a picture: no licensed Hochul briefing still exists in `research/` yet (`_list.md` open item 3). Build it; the orchestrator mounts it only over a cleared still.

## 0. What this graphic claims
The speaker is Kathy Hochul, Governor of New York, at the 26 Dec 2022 storm briefing (the same briefing as A3-S7).

## 1. SOURCE
- Briefing: `research/response.md` section 2 (governor.ny.gov rush transcript, 26 Dec 2022, PRIMARY), https://www.governor.ny.gov/news/video-audio-photos-rush-transcript-governor-hochul-holds-virtual-storm-briefing-0
- The "DEC 26 BRIEFING" words are a claim about the picture: the still under it must be from that briefing by its `provenance.csv` row. If the still is any other Hochul photo, use the fallback sub-line below.

## 2. DATUM, SCALE, ORIENTATION
Overlay on a still, root transparent. Lower-third anchor `left:110px; bottom:110px` (tokens.md "Canvas"). Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Card `hl-card`: glass surface (radius 28), `left:110px; bottom:110px`, padding 22 px 34 px, hugs text, 4 px `#d8a13a` bar on its left edge (inside the radius).
  - Name: "KATHY HOCHUL", Arial Black 900 52 px `#f2f5f8`, line-height 1.
  - Sub: "GOVERNOR OF NEW YORK · DEC 26 BRIEFING", Arial 700 26 px `#e8c56a` tracking 3, 10 px below. Fallback sub (still not from that briefing): "GOVERNOR OF NEW YORK".
  - Width about 760 (x 110-870), height about 140 (y about 830-970).
- Source pill `left:110px; bottom:54px`: "Gov. Kathy Hochul, storm briefing, 26 Dec 2022".
- Type tiers: 52, 26, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. Spelling "KATHY HOCHUL" (Whisper writes "Hochschild").
2. Card enters on her name, not before.
3. The card does not cover her face in the settled frame over the still (orchestrator read; move to the right side, x <= 1560 and y < 680, if it does).

## 5. PANEL TEXT (exact) and CUES (segment seconds, `audio/a3-s9.words.json`; host starts at 3.20, comp-local = t - 3.20)
Strings: `KATHY HOCHUL` · `GOVERNOR OF NEW YORK · DEC 26 BRIEFING` · `Gov. Kathy Hochul, storm briefing, 26 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 3.20 | (before "Hochschild" @3.30) | nothing visible at frame 0 (CSS hidden too) |
| 3.30 | "Hochschild" (= Hochul) @3.30 | card `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; gold bar `scaleY 0 -> 1` 0.3 s |
| 3.70 | "told the story" @3.52 | sub-line `fromTo(autoAlpha 0, y:10 -> 0, 0.35)`; source pill in |
| 3.70-6.10 | "...surgeon from Erie County Medical Center." | card floats y 0 -> -4, sine, yoyo, finite |
| 6.10-6.70 | before "He was stuck" @6.74 | card and pill out `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
Comp duration 3.50 s.

## 6. CONTRACT
One file `compositions/g-a3-10-hochul-lt.html`, root `id="g-a3-10-hochul-lt-root"`, `data-composition-id="g-a3-10-hochul-lt"`, PAUSED timeline `window.__timelines["g-a3-10-hochul-lt"]`. Prefix `hl-`. Both sub-line versions pre-authored; the fallback hidden unless the orchestrator flips a class at mount (no runtime text writes). Rest: `references/mg-quickref.md`.
Footage under it: Hochul 26 Dec 2022 briefing still (governor.ny.gov), file and licence TBD; it also covers S9 0.00-3.20 with no graphic.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-10-hochul-lt`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-10-hochul-lt`.

## 7a. DONE LINE
All seven items of the template 7a; item 7 waits for the still.

## 8. RECEIPT
As the template.
