# A5 graphics list: St. John's, Greenbriar and the age gap (ep-joplin-2011)

Source of every graphic: the **Picture:** lines of A5-S1 to A5-S11 in `edit_script.md` (lines 575 to 657). Numbers: `research/facts.md` rows. Cues: `audio/a5-s<n>.words.json`.
Real footage and photos are not listed as graphics; the brief names the file a graphic sits over (`media/candidates/a5/`, picks per `candidates.md`).

| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span s |
|---|---|---|---|---|---|
| g-a5-sjrmc-open | A5-S1 | chips "183 INSIDE", "HOSPITAL FOR 140,000", "4 TIMES THE RATE" + source line over the FEMA still, then the NIST towers photo | STANDARD | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | a5-s1 2.80 to 12.04 |
| g-a5-condition-gray | A5-S2 | drawn tower floor plan: beds roll from perimeter rooms into the central hallway, label "Condition Gray", clock "5:38 PM", chip "5 TO 7 MINUTES" + source chip, source line | DEEP | `library/inhouse/radar-beam.html` (full-frame SVG diagram), `svg-stroke-trace` (catalog) | a5-s2 0.00 to 23.36 |
| g-a5-cc-midmost | A5-S3 | comment card "Being in the upper floors..." | STANDARD (copy of the comment-card base) | the episode comment-card base; `library/inhouse/quote-card.html` | a5-s3 0.00 to 7.50 |
| g-a5-tower-wind | A5-S3 | chip "ABOUT 170 MPH" + source chip over the NIST generator-building photo | STANDARD | `ep6-glasscard-popfig-bfmg.html` | a5-s3 7.78 to 14.62 |
| g-a5-cc-standing | A5-S4 | comment card "the only tangible building standing was the hospital." | STANDARD (copy of the comment-card base) | comment-card base | a5-s4 0.00 to 6.60 |
| g-a5-map-sjrmc | A5-S4 | master map at St. John's: 12 dots, 4 marked "ICU", 7 turn hollow (lost later, elsewhere), chips "12 FROM THE STORM", "7 LOST LATER, ELSEWHERE", source line | DEEP (copy of the master-map base) | master-map base; `library/inhouse/master-map-us-canada.html`, `references/editing-patterns/ep3-map-route-fit.html` | a5-s4 6.60 to 18.60 |
| g-a5-windows | A5-S5 | fifth-floor band outlined on NIST Fig 3-10, red bracket on the broken band below, chip "IMPACT WINDOWS HELD", source line | STANDARD | `outline-draw` (catalog), `ep6-glasscard-popfig-bfmg.html` | a5-s5 0.86 to 7.00 |
| g-a5-cc-greenbrier | A5-S6 | comment card "I was in the greenbrier nursing home when it happened." | STANDARD (copy of the comment-card base) | comment-card base | a5-s6 7.60 to 10.30 |
| g-a5-greenbriar | A5-S6 | chip "19 OF 95 LOST" over the Greenbriar photo, then our one-story building drawing, inner hallway lit, doors close, hallway fills with rubble, source chip, source line | DEEP | `radar-beam.html`, `svg-stroke-trace` | a5-s6 10.20 to 28.08 |
| g-a5-map-meadows | A5-S7 | master map: Meadows outline at the path edge, pale EF-1 band, 2 dots, chip "EF1 WINDS · 2 LOST" | DEEP (copy of the master-map base) | master-map base | a5-s7 0.00 to 11.08 |
| g-a5-counter3 | A5-S7 | counter visit 3: "INSIDE A BUILDING 135 of 135" over "BELOW GROUND, NONE FOUND", glass card top right | STANDARD (copy of the counter-card base) | counter-card base; `library/inhouse/stat-panel.html`, `count-up` (catalog) | a5-s7 6.28 to 11.08 |
| g-a5-paul-rates | A5-S8 | two chips over Paul full frame: "60 AND OVER: 8 IN 1,000", "UNDER 60: 2 IN 1,000", source chip | STANDARD | `ep6-glasscard-popfig-bfmg.html` | a5-s8 0.96 to 8.80 |
| g-a5-age-gap | A5-S9 | [RS][VE] bar pair 8 against 2 per thousand; the hospital and nursing-home share drains from the taller bar, gap bracket stays, chip "THE GAP STAYS", source line | DEEP | `library/inhouse/ranked-bars.html`, `chart-story` (catalog) | a5-s9 0.00 to 21.80 |
| g-a5-why | A5-S10 | NIST Finding 47 page, three factors underlined one by one, chips "LESS WORD", "LESS HELP", "HARDER TO RECOVER"; then NWS page, "elderly, infirm, or disabled" underlined; source lines | STANDARD | `hw-underline`, `marker-highlight` (catalog) | a5-s10 0.00 to 18.36 |
| g-a5-recs-board | A5-S11 | 16 grey tiles numbered 1 to 16, chip "16 RECOMMENDATIONS", source line; the BASE that A6 copies to tick recommendations | STANDARD | `stagger-lattice`, `grid-card-assemble` (catalog) | a5-s11 0.00 to 6.80 |

15 comps: 5 DEEP (Opus 5.5, high effort or above), 10 STANDARD (Sonnet 5.5, high effort).

## Rules that hold for every a5 brief (written once here)
- **Cue notation:** `a5-sN "word"@t` = the word's `start` in that segment's words.json, seconds from the start of its wav. Each brief gives its **host start** as a segment word time; comp-local time = t minus the host start. The orchestrator sets each segment's timeline offset when it mounts the host.
- Whisper wrote some words wrong in these files; the cue still uses the word as written: a5-s6 "class."@17.76 is "glass", a5-s6 "War."@26.96 is "were", a5-s7 "list"@8.14 is "lose", a5-s8 "he"@7.04 is "it", a5-s2 "538."@13.48 is "five thirty-eight".
- **§6 to §8** (contract, tools, done line, receipt) are `references/mg-brief-template.md` as written; every rule not stated in a brief is `references/mg-quickref.md`.
- **Chips:** glass chip values from `library/inhouse/snippets/cards.css` `.popup` (Arial 700 40 px `#f2f5f8`, radius 14, glass surface; fine line 21 px `#c8d3e0`), copied under the comp's own class names (never `.popup`: css_collision). Enter `fromTo(autoAlpha 0, y 24 -> 0, 0.4, power3.out)`, slow float after, exit `to(x:980, autoAlpha 0, 0.6, power3.in)`.
- **Source line:** `.srclab` values (Arial 19 px, `rgba(200,211,224,.75)`, glass, radius 14) but placed **bottom-left** (`left:96px; bottom:54px`). Reason: the presenter circle owns the corner x >= 1600, y >= 680 in every a5 narration segment, and `.srclab`'s shipped bottom-right spot sits inside it.
- **Corner:** nothing enters x >= 1600, y >= 680 in any a5 comp except g-a5-paul-rates (Paul full frame, circle off).
- **Shared bases, never redrawn:** the master map (first drawn at I1-S2), the comment card (first used at A1-S3), the counter card (visit 1 at the end of A3). Each a5 instance is a copy of that base file renamed to its a5 id, with only the a5 layers added ("a family built on one base"). The base ids are whatever `briefs/i1|a1|a3/_list.md` name them; no base was written when these briefs were (17 Oct 26), so the builder copies the base once it exists and reads the base's own brief for geometry, palette and dot style. g-a5-recs-board is itself a base: A6 copies it.

## Open numbers (not in facts.md, so left out of every drawing)
1. Comment-card like counts: 671 (A5-S3), 58 (A5-S4), 193 (A5-S6). They are in `research/comments-for-writer.md` lines 40, 49, 47 and `research/comment-beats.json`, not in facts.md. The cards draw the likes slot empty until the orchestrator accepts that file as the source.
2. The age-gap rates after NIST removed hospital and nursing-home deaths. C30 says only that the gap "remains". NIST Fig 4-19 ("Comparison of fatality rates per thousand people within two populations") may carry them; not extracted. The drained bar carries no number and no readable scale.
3. EF-1 wind-speed range. facts.md has EF-3 and EF-4 ranges (W10) and the EF-0 floor (W22), not EF-1. The band is labelled "EF-1" only.
4. Map positions of St. John's, the Greenbriar and Meadows Healthcare: no coordinates in facts.md. They come from the master-map base, traced from NIST Fig 4-23 (fatality locations labelled by structure) and Fig 4-24 (EF polygons). Positions only; the GeoEye/Pictometry aerials under those figures are never shown.
