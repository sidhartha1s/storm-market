# g-a1-10-street-clock · A1-S10 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md`, `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, template `references/mg-brief-template.md`, `briefs/a1/g-a1-5-watch-timeline.md` (axis and lanes) and `briefs/a1/g-a1-9-update-card.md`.
Start from: the built `compositions/g-a1-9-update-card.html` (rail and three cards; prefix `sc-`).

## RULE CONFLICT, resolved here (orchestrator: confirm)
The Picture line puts chip "THU NIGHT · RAIN" over a Pexels street. `references/mg-quickref.md` template 7a item 7: a label naming a place, date or event must sit over footage of that place and date, "never stock". So in this brief: the street plays UNLABELLED (0 to 4.06 s, the comp transparent over it); "THU NIGHT · RAIN" is a marker on the timeline (designed ground), where it names a span of the axis, not the picture. The clock chip also sits on the designed ground. If the orchestrator wants the Picture line literally, it needs a Buffalo, Thu 22 Dec 2022 rain clip with a provenance row instead of stock.

## 0. What this graphic claims
On Thursday night at the Buffalo airport it was still raining, no snow yet; every product pointed at 7 AM Friday, when the warning took effect.

## 1. SOURCE
- BUF ASOS (IEM): no snow Thu 22 Dec; rain/drizzle 6:54 PM Thu to 6:18 AM Fri; first snow mixed with rain 6:58 AM Fri. `factcheck/a1-r1.md` rows 40 and 45. Rain span on the axis: 6:54 PM Thu (h 66.900, x 1259.1) to 6:58 AM Fri (h 78.967, x 1457.3), computed on the g-a1-5 scale.
- Warning effective 7 AM Fri: `research/nws.md` row 1.2; watch "Friday morning" VTEC 221223T1200Z (`factcheck/a1-r1.md` row 27).
- Footage under 0 to 4.06 s: `media/candidates/a1/A1-S10_c1_rain-night-street.mp4` (Pexels 12570193, 1920x1080, Pexels free licence; `provenance.csv` says faces and plates NOT checked: the orchestrator checks before mounting; c2/c3 are 9:16 and need a crop). The orchestrator mounts it on a lower track for the comp's first 4.6 s.

## 2-3. GEOMETRY (px)
- 0 to 4.06 s: comp transparent except nothing (no label over the street). Corner circle may show (only footage under it).
- Ground `sc-ground` (radial gradient) fades in over the street 4.06 to 4.66; rail, day labels, watch, warning and update cards return at 0.3 opacity (g-a1-5/6/9 positions), in-effect tick and label at full.
- Rain span: rail segment x 1259.1 to 1457.3 overlaid with a 10 px band `#5a768f` with falling rain ticks (1 x 10 px `#7fb2e5`, moving y +60 px/s, inside y 880 to 920). Label "THU NIGHT · RAIN" Arial 700 22 px `#7fb2e5` letter-spacing 2, centred x 1358, top 840 (box about 1240 to 1476; the update card's stem at 1257.4 is dimmed to 0.3, the label sits above the band and right of x 1240: check no overlap with the stem line, shift label right to start at x 1270 if it touches).
- Clock chip, top-left slot: line 1 "FRI DEC 23 · 7:00 AM" Arial Black 900 52 px `#e8c56a` left 200 top 110; line 2 "WARNING IN EFFECT" Arial 700 30 px `#e74c3c` letter-spacing 3, left 200, top 176. (The Picture's one chip "FRI DEC 23 · 7:00 AM · WARNING IN EFFECT" split in two lines because one line at 52 px runs past 1500 px.)
- Source line "Buffalo airport ASOS, IEM archive": Arial 19 `#c8d3e0`, left 96, bottom 54, in with the rain span.
- Type tiers: 52, 22 to 30, 19.

## 4. MUST BE TRUE
1. No place, date or weather label is visible over the stock street at any frame.
2. The rain span runs from 6:54 PM Thu to 6:58 AM Fri on the shared scale and ends at the in-effect tick (2 px apart at 1457.3 vs 1457.9).
3. The clock chip's time equals the in-effect tick's label (7 AM Fri).
4. The comp ends in black (hand-off to the A1 to A2 chapter blackout).
5. Corner x >= 1600, y >= 680 empty while the ground is up.

## 5. CUES (seconds from A1-S10 start, `audio/a1-s10.words.json`)
| t (s) | spoken word | action |
|---|---|---|
| 0.00 to 4.06 | "On Thursday night at the Buffalo airport, the snow still hadn't started." | street only (comp transparent; a 1 px `sc-tick` leaf is NOT needed: blank_scan reads the video under it) |
| 4.06 to 4.66 | "The watch" @4.06 to 4.14 | ground and dimmed timeline fade in (0.6, power2.out); watch card brightens to 0.8 at 4.14 then back to 0.3 at 5.0 |
| 4.80 to 5.08 | "Friday morning," | rain band draws `scaleX 0 -> 1` from x 1259.1 (0.5); rain ticks start; "THU NIGHT · RAIN" in; source line in |
| 6.16 to 6.68 | "the warning said seven." | warning card brightens to 0.8 then 0.3; in-effect tick pulses (scale 1 -> 1.4 -> 1); clock chip line 1 in at 6.40 (scale 1.2 -> 1, 0.4, power4.out), line 2 at 6.68 |
| 7.52 to 10.56 | "So what would that rapid switch from rain to snow do to a road?" | slow push toward the in-effect tick: whole ground layer `scale 1 -> 1.08`, transformOrigin 1457px 900px, 7.52 to 11.6, ease none (HUD chip stays fixed); rain ticks keep falling |
| 10.56 to 11.6 | tail | fade to black: everything `to(autoAlpha 0, 1.0, power1.in)` 10.6 to 11.6 |
Comp duration 11.6 s. Whisper heard the last word as "erode?" (@10.20): the spoken words are "a road?".

## 6-8
One file `compositions/g-a1-10-street-clock.html`, root `id="g-a1-10-street-clock-root"`, `data-composition-id="g-a1-10-street-clock"`, PAUSED timeline `window.__timelines["g-a1-10-street-clock"]`, prefix `sc-`. Done line item 7: the frame at 2.0 s is read composited over the street clip mounted under it, and the transparent span 0 to 4.06 names that clip. Tools, all seven 7a items and receipt as the template.
