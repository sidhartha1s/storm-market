# g-a3-8-abandoned-quotes · A3-S7 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the `.glasscard` quote card in `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass is the one treatment for text over footage). Card 2 is an addition the Picture line does not name (`_list.md` open item 2): build it as its own timeline block so the orchestrator can drop it cleanly.

## 0. What this graphic claims
On 26 Dec 2022 Gov. Kathy Hochul said there were still "scores and scores of vehicles that were abandoned"; the same day County Executive Mark Poloncarz said "The city of Buffalo is impassable in most areas." The card never says the people who left those cars are the ones found outside (`edit_script.md` A3-S7 row note).

## 1. SOURCE
- Hochul, full sentence: "We still have scores and scores of vehicles that were abandoned when people left during the storm": `research/response.md` section 2 (governor.ny.gov 26 Dec 2022 transcript, PRIMARY), https://www.governor.ny.gov/news/video-audio-photos-rush-transcript-governor-hochul-holds-virtual-storm-briefing-0 ; `factcheck/a3-r1.md` row 41 CONFIRMED.
- Poloncarz: `research/deaths.md` section 5 (AP via The Peninsula, 26 Dec 2022, SECONDARY), https://thepeninsulaqatar.com/article/26/12/2022/storm-deaths-rise-to-25-in-western-new-york-county ; `factcheck/a3-r1.md` row 44 CONFIRMED.
- Footage: Andre Carrotflower, "Abandoned vehicles on West Utica Street in the aftermath of the December 2022 blizzard", Tue 27 Dec 2022 2:09 PM, CC BY-SA 4.0, `research/cc-clips-r2.md` S3.

## 2. DATUM, SCALE, ORIENTATION
Overlay on footage, root transparent. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Quote card `aq-card1` and `aq-card2` (one at a time, same box): glass surface (tokens.md, radius 28), x 260-1500, top 300, height hugs text (about 300). Padding 48 px 64 px.
  - Quote Georgia italic 52 px `#f2f5f8`, line-height 70, max width 1110.
  - Card 1 lines: L1 `“scores and scores of vehicles` · L2 `that were abandoned”`
  - Card 2 lines: L1 `“The city of Buffalo is impassable` · L2 `in most areas.”`
  - Attribution under the quote, 24 px gap, Arial 700 26 px `#d8a13a` tracking 3: card 1 "GOV. KATHY HOCHUL · DEC 26, 2022"; card 2 "MARK POLONCARZ · ERIE COUNTY EXECUTIVE · DEC 26".
- Source pill `left:110px; bottom:54px` (as g-intro-2 `tc-src`), two leaves: S1 "Gov. Kathy Hochul, storm briefing, 26 Dec 2022, governor.ny.gov"; S2 "Mark Poloncarz, 26 Dec 2022, AP via The Peninsula".
- Photo credit, Arial 400 19 px `#c8d3e0` on a glass pill, `right:96px; top:54px`: "Photo: Andre Carrotflower / Wikimedia Commons / CC BY-SA 4.0" (whole window).
- Type tiers: 52, 26, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. Both quotes are exact substrings of the sourced sentences, inside curly quotes, no ellipsis needed (card 1 is a fragment of Hochul's sentence, quoted as a fragment).
2. No line on screen links the abandoned cars to the people found outside.
3. One card at a time; the source pill always matches the visible card.
4. The photo credit is on screen for the whole window (CC BY-SA requirement).
5. Over the cars the card is readable: glass, white text; the orchestrator checks the card does not hide the buried cars in the settled frame (move the card to top 160 if it does).

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S7 start, `audio/a3-s7.words.json`)
Strings: as §3.
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "A lot of people did the other thing." | photo credit visible from frame 0; nothing else (the footage carries the line) |
| 3.30 | "Governor Kathy Hochul" @3.30 | card 1 shell in `fromTo(y:30 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)` with the attribution only; S1 in |
| 6.46 | "scores and scores" @6.46 | L1 in `fromTo(autoAlpha 0, y:14 -> 0, 0.4, power3.out)` |
| 7.84 | "that were abandoned" @7.84-8.24 | L2 in (same) at 7.84 |
| 10.02-10.62 | after "storm." @10.02 | card 1 + S1 out `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
| 12.00 | "polling cars" (= Poloncarz) @12.00 | card 2 shell in with attribution; S2 in |
| 13.90 | "The city of Buffalo" @13.90 | L1 in |
| 15.04 | "impassable" @15.04 | L1 word "impassable" brightens to `#ffffff`; L2 in at 15.66 "in most areas" |
| whole window | | visible card floats y 0 -> -4, sine, yoyo, finite |
| 15.78-16.38 | after "areas." @16.00 | card 2, S2 and credit out `to(autoAlpha 0, 0.6, power3.in)` |
Comp duration 16.38 s.

## 6. CONTRACT
One file `compositions/g-a3-8-abandoned-quotes.html`, root `id="g-a3-8-abandoned-quotes-root"`, `data-composition-id="g-a3-8-abandoned-quotes"`, PAUSED timeline `window.__timelines["g-a3-8-abandoned-quotes"]`. Prefix `aq-`. Rest: `references/mg-quickref.md`.
Footage under it (mounted by the orchestrator, slow push in index.html): Carrotflower S3 still above (`media/` path to be set). Its push lives on the footage, never on the card.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-8-abandoned-quotes`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-8-abandoned-quotes`.

## 7a. DONE LINE
All seven items of the template 7a. Item 7: one frame per card composited over the still.

## 8. RECEIPT
As the template.
