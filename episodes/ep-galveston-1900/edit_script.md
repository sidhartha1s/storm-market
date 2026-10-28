# ep-galveston-1900 · edit_script.md (TTS segment format)
Opening (26 Oct 26, batch A): hook (PROVISIONAL, shape object), tail and intro rewritten over 3 rounds; fact-check rounds factcheck/intro-r1..r3.md, 0 open [verify]; fresh Opus grade 6, 7, 7 (grades/intro-r1..r3.md): plateaued below the bar of 8 after 2 rewrite rounds, so rewriting stopped. Not locked: grade below 8 and owner approval pending. Voiced provisionally. Opening loops are the [loop] and [Q] tags on its segments; L-intro now opens in I1-S5.

Status: DRAFT 5, hook + hook tail + intro only (phase 3 owner gate). Acts below are briefs, no prose yet.
Gate state (26 Oct 26): fact-check fan-out rounds A to E (`research/factcheck-A.md` .. `factcheck-E.md`, run by checkers who are not the writer): 0 open `[verify]` markers; every CORRECTED line applied word for word; 0 UNVERIFIED lines left (the one UNVERIFIED claim, "went to bed on Friday night feeling safe", was cut). Skeptic grade (separate agent each round): hook 5, 6, 6, 6 of 10, so the hook does NOT lock yet (bar 8). Not yet locked, not yet owner-approved, no TTS.
Open before anything goes on screen: one human look at the 1891 page scan (Portal to Texas History is bot-gated; the wording comes from the Wikimedia Commons transcription); the Library of Congress record for the Broadway ruins film (loc.gov returned 403).
Angle: `episodes/ep-galveston-1900/angle.md` (owner lock, devq save 26 Oct 26 02:09:38, `t_galveston` "a3" + note).
Research: `episodes/ep-galveston-1900/research/` (sources-cline.md, sources-cuba.md, teardowns.md, footage-inventory.md).

## Packaging (drafted after the lock, per `references/packaging-rules.md`)
- Title: **Galveston 1900: He Said It Was Safe. It Was Not.** (48 characters; Name + Year in the first 16; `title_fre.py` 101.9)
- Thumbnail: school A (Name + Year documentary card): the Library of Congress ruins photograph, place name in frame, one fact line in two words ("ABSURD DELUSION"), with a Field Notes Paul variant for Test and Compare. Not drafted this round.
- Promise the hook must say aloud: the city's own weatherman wrote that a storm seriously damaging Galveston was "an absurd delusion"; nine years later the storm came.

## Runtime and structure
- Target: about 20 to 24 minutes (to be confirmed by the owner; no word budget run yet: needs two probe TTS segments, and this round has no TTS).
- Architecture: Detective (who told Galveston it was safe, and who said otherwise).
- Dominant question: if the warnings existed, why did so few people leave a warned city?

## Hook sound (reasoned, DESIGN.md "Cold-open hook contract")
No siren: this is not a tornado-siren story, and 1900 had none. The hook runs on wind and surf rising under Paul's line, a telegraph-key click on the 1891 newspaper reveal, and a low swell into the ruins film. No archive audio (none exists for 1900).

## Paul on camera (planned, NOT generated this round; 6 full-frame clips of at most about 26 words each)
1. P1 = H1-S1, frame one, the hook sentence only.
2. P2 = end of A1 (the 1891 article turns from opinion into the city's belief).
3. P3 = end of A2 (Havana says Gulf, Washington says recurve).
4. P4 = the `cta-hinge` tease, last line before the book ad.
5. P5 = A5 turn (Cline's own report against his later story).
6. P6 = editor's choice, held for the close.
Budget per `references/mg-quickref.md` "Paul on screen": 6 clips x 15 credits = 90 credits, one take each. Owner sign-off needed before any clip runs.

## CTA hinge (DESIGN.md "CTA contract", `config.yaml channel.cta.window` 0.40 to 0.60)
- Segment before: last A3 segment, ending on the tease (P4, at most 25 words): the telegram Isaac Cline sent Washington at half past three on Saturday afternoon.
- Segment after: A4-S1 opens with the telegram's words as the payoff.
- Estimated position: about 10:30 of about 22:00 (0.48).

## Loop registry (plant / pay)
| Loop | Planted | Paid |
|---|---|---|
| E1 episode loop: why did so few people leave a warned city? | H1 | A6 close |
| L-intro: why would Galveston's own weatherman write that a storm seriously damaging the city was an absurd delusion? | intro (I1-S6) | A1 |
| cta-hinge: what Cline told Washington at three thirty | A3 last segment | A4-S1 |

## H · Hook (0:00)
Hook shape: object (2026-10-26)
PROVISIONAL (26 Oct 26): orchestrator's default pick from `hook_options.md`, owner pick pending; if he picks another shape only the hook and intro are redone.

### H1-S1 — Paul on camera
**Picture:** Paul full frame at 0:00, plain Omni clip, no prop in his hands (owner 16:02: "Instead of Paul holding it, you can show a snippet of it ... do the omni as it is"); the Galveston Daily News page of 16 July 1891 shows as an on-screen panel to his side, the column snippet, never in his hands; popfig "GALVESTON, TEXAS · JULY 1891" inside the first second; the sound under him: newsprint unfolding, then rain on a window, no wind. [HOOK] [VE]
> Nine years before the storm, an article in Galveston's own newspaper told its readers no hurricane could badly damage their city.

Rows: sources-cline.md §1 and factcheck-E.md H1-S4 (same page: "impossible for any cyclone to create a storm wave which would materially injure the city"; belief the city "will at some time be seriously damaged ... is simply an absurd delusion"); "badly" for "seriously/materially" accepted in factcheck-D.md H1-S2; "hurricane" for "cyclone". Date "from July eighteen ninety-one" moved to the popfig (grade fix 2). Twenty-one words (owner 16:02 rewrite: no "This page", Paul holds nothing). "Nine years before the storm": 16 July 1891 to 8 Sept 1900. "Galveston's own newspaper" = the Galveston Daily News. H1-S2's "part of it" now points at "an article".

### H1-S2 — narration
**Picture:** slow push to the column; chip "ABSURD DELUSION"; lower-third "ISAAC CLINE · GALVESTON WEATHER OFFICE". Source line: Isaac Cline, Galveston Daily News, 16 July 1891 (Wikimedia Commons transcription). Telegraph-key click on "absurd delusion". [RS] [VE] (break one)
> The man who wrote part of it was Isaac Cline, Galveston's own weatherman. He called that fear an absurd delusion.

Rows: sources-cline.md §1 and factcheck-E.md H1-S2 (Cline wrote the part of the 16 July 1891 article with "simply an absurd delusion"); factcheck-E.md H1-S2 / factcheck intro-r1 row 24 ("its own weatherman", CONFIRMED SECONDARY; in Galveston by 1889, NOAA VLab). "That fear" = the belief the city would be seriously damaged by a storm, as in factcheck-D.md I1-S6 "a storm like this ... absurd delusion" (fair).

### H1-S3 — narration
**Picture:** hard cut to the Library of Congress ruins photograph of Galveston, September 1900; popfig "SATURDAY · SEPT 8, 1900"; chip "AT LEAST 6,000 LIVES" with small tag "CLINE'S OWN COUNT"; low swell under the cut. Source line: Isaac Cline, Monthly Weather Review, September 1900; NOAA Heritage; NOAA AOML. [RS] [VE] [PAY] (toll ends at spoken word 59: about 19 s at 185 wpm, about 24 s at 150 wpm; probe-TTS decides)
> Nine years later, on a Saturday night in September, a hurricane came ashore at Galveston. At least six thousand people there lost their lives.

Rows: sources-cuba.md §4 (AOML "On the evening of September 8, 1900, a major hurricane struck Galveston"); factcheck intro-r2 rows 7 to 9 (Saturday verified; "at least 6,000" NOAA Heritage, Cline's MWR count 6,000 "conservative"; "lost their lives" alternative); "Nine years later" = 16 July 1891 page to 8 September 1900 (nine years, two months) · Commons 1891 page date, AOML 1900 date]; "Saturday night" as the spoken form of AOML "evening of September 8" (storm wave about 6:30 p.m. TSHA, landfall about 8:00 p.m. CST Wikipedia) · https://www.tshaonline.org/handbook/entries/galveston-hurricane-of-1900]. "That night" dropped here so it is spoken once, in H1-S5 (round 3, grade r2 fix 4: date stack cut, nine-year gap spoken, toll earlier).

### H1-S4 — narration
**Picture:** NOAA 1900 weather map, Havana pinned, popfig "BELEN OBSERVATORY, HAVANA", one arrow northwest into the Gulf; then the telegraph line graphic, the Washington line lit, the Havana line dark. Source line: NOAA AOML, 2015 (on screen: "NOAA: the Bureau 'decreed that only its forecasts would be carried over the telegraph'"). [RS] [VE] (break two)
> Over in Havana, the Jesuit forecasters at Belen Observatory said the storm was moving northwest, into the Gulf of Mexico. But the Weather Bureau in Washington ruled that the telegraph would carry only its forecasts. So the only forecasts on the wire to Galveston were Washington's.

Rows: sources-cuba.md §1 (AOML "the Belén forecasters said their observations indicated the storm moved to the northwest and into the Gulf of Mexico"; Jesuit, cubamemorias.com via factcheck-B.md I1-S3); sources-cuba.md §2 (AOML "the USWB decreed that only its forecasts would be carried over the telegraph"; "NOAA says" moved to the on-screen source line, grade fix 3; "the storm" now follows the hurricane named in H1-S3; "the Weather Bureau in Washington" replaces the unintroduced "the Bureau"); "ruled that the telegraph would carry only its forecasts" as the active-voice form of AOML "decreed that only its forecasts would be carried over the telegraph" · https://web.archive.org/web/2023/https://www.aoml.noaa.gov/hurricane_blog/115th-anniversary-of-the-great-galveston-hurricane/]; last sentence moved verbatim from old I1-S3, factcheck intro-r2 row 30 (CONFIRMED, fair extension; AOML "Only the Weather Bureau prognostication was carried over the wires"). Round 3, grade r2 fix 3: decree ends on what it meant for Galveston, spent once, "own" and "had said/had decreed" cut.

### H1-S5 — narration
**Picture:** back to the 1891 page, the light on it dimming; cut to the Monthly Weather Review report page, slow push to the line about his wife. Source line: Isaac Cline, Monthly Weather Review, September 1900. [VE] [HUMAN]
> Among the people Galveston lost that night was Isaac Cline's own wife.

Rows: sources-cline.md §3 ("Among the lost was my wife, who never rose above the water after the wreck of the building"); "that night" now set up by H1-S3.

## HT · Hook tail

### T1-S1 — narration
**Picture:** hold one beat on the Monthly Weather Review page, then cut to the self-made island elevation graphic of Galveston, sea level line rising to the island's top; chips "ABOUT 38,000 PEOPLE" and "HIGHEST POINT ABOUT 8.7 FT"; last line over the same graphic, chip "WARNED" then "FEW HAD LEFT". Source line: Texas State Historical Association; National Park Service. [VE] [Q] [loop E1 open] (why did so few people leave a warned city?)
> Galveston was an island city off the Texas coast, home to about thirty-eight thousand people. Its highest ground was less than nine feet above the sea. The city had been warned. Still, few people left.

Rows: factcheck-A.md / factcheck-C.md / factcheck-D.md T1-S1 (TSHA "the city of 38,000 inhabitants"; NPS "the highest elevation on Galveston Island was 8.7 feet"); factcheck intro-r1 row 18 (TSHA "On the previous day Galveston had been placed under a storm warning"); factcheck-C.md and factcheck-D.md H1-S5 (NPS "comparatively few people had evacuated the city", chip FEW HAD LEFT CONFIRMED). E1 now spoken, not only tagged (grade fix 4). "Off the Texas coast": TSHA "Galveston, Texas" / NPS "Galveston Island" (round 3, grade r2 fix 7: Texas spoken once).

## I · Intro

### I1-S1 — narration
**Picture:** Monthly Weather Review, September 1900, the report's byline; lower-thirds "ISAAC CLINE · LOCAL FORECAST OFFICIAL, GALVESTON" then "JOSEPH CLINE · OBSERVER"; then NOAA 1900 weather maps, September 2 to 4, the storm stepping across Cuba, chip "CROSSES CUBA · SEPT 4"; last line, a dotted arrow off western Cuba labelled "WASHINGTON ?". Source line: Isaac Cline, Monthly Weather Review; Monthly Weather Review, September 1900. [VE] [HUMAN] [Q] [loop q1 open] (where did Washington think it would go?) [loop E1 still open]
> If you lived in Galveston in nineteen hundred, Isaac Cline still ran your weather office. His brother Joseph worked beside him as the observer. The storm crossed Cuba on the fourth of September. And Washington's forecasters had a different track in mind.

Rows: factcheck-D.md I1-S1 (NOAA VLab "the senior Weather Bureau employee present at Galveston"; MWR "Local Forecast Official"); sources-cline.md §2 and factcheck-B.md I1-S1 (Joseph Cline, brother, "Mr. J. L. Cline, Observer"); factcheck-C.md / factcheck-D.md I1-S1 (MWR "crossed northward over the western central part of Cuba during the 4th"); sources-cuba.md §3 (AOML "The USWB forecasters expected the storm to recurve to the northeast"). Cline's job is spoken here once more as 1900 fact (H1-S2 said 1891); the old third spend in I1-S6 is gone (grade fix 8). "a different track" = AOML recurve northeast vs Belen northwest into the Gulf · AOML 2015, factcheck intro-r2 rows 11 and 23]. Round 3, grade r2 fixes 5 and 6: "its own idea" and "it'd" cut; q1 now asks which track, since the hook no longer says Washington disagreed, only that its forecast was the one on the wire.

### I1-S2 — narration
**Picture:** western Cuba on the NOAA map; the dotted "WASHINGTON" arrow resolves, curving northeast; lower-third "WILLIS MOORE · CHIEF, US WEATHER BUREAU"; the Havana arrow from the hook (northwest into the Gulf) fades back in beside it; then the track line pushes northwest into the Gulf and the Washington arrow fades out; chip "STEAMER LOUISIANA · SEPT 6". Source line: NOAA AOML, 2015; Monthly Weather Review, September 1900. [RS] [VE] [PAY] [loop q1 closes]
> Willis Moore's Weather Bureau expected it to curve away to the northeast, the way many storms did once they got that far north. It didn't. On the sixth, the steamer Louisiana passed right through its center, out in the eastern Gulf.

Rows: factcheck-D.md I1-S2 (AOML "The USWB forecasters expected the storm to recurve to the northeast, as many storms did near this latitude"; Wikipedia "Bureau director Willis Luther Moore", SECONDARY for the title); factcheck intro-r1 row 12 ("went Havana's way", storm did not recurve, AOML/Wikipedia); factcheck-B.md I1-S5 and factcheck-E.md I1-S4 (MWR "On the 6th the Cromwell Line steamer Louisiana passed through the center of the hurricane in the middle-eastern part of the Gulf"); "out in the eastern Gulf" CONFIRMED in factcheck intro-r2 row 27 (marker dropped; Halsey "about half way across the Gulf", Wikipedia "In the eastern Gulf of Mexico on September 6"). Summary tag "So two forecasts pointed two different ways" cut (grade fix 6). "once they got that far north" as the spoken form of AOML "as many storms did near this latitude" · AOML 2015] (round 3, grade r2 fix 6).

### I1-S3 — narration
**Picture:** NOAA map, the track line running west-northwest across the Gulf toward the island elevation graphic; the telegraph line graphic from the hook returns, only the Washington line lit, a pulse running down it toward Galveston. Source line: Monthly Weather Review, September 1900. [VE] [Q] [loop q2 open] (what did the wire tell Galveston as it came?)
> It kept coming across the Gulf, toward the island. And Washington's wire was telling Galveston what to expect.

Rows: factcheck-E.md I1-S5 and factcheck intro-r2 row 29 ("It kept coming across the Gulf, toward the island"); MWR, Cline: "Warning messages were received from the Central Office at Washington on September 4, 5, 6,7, and 8" (factcheck intro-r2 row 32). Round 3, grade r2 fix 3: the decree restatement moved into H1-S4 so it is spent once; this line now only opens q2 as a statement (no rhetorical question).

### I1-S4 — narration
**Picture:** the Monthly Weather Review report page, slow push to the line listing warning messages from the Central Office; chips stack one per day "SEPT 4 · 5 · 6 · 7 · 8", then "STORM WARNING: SEPT 7", then "'MODERATE STORM'" in quote marks with tag "WASHINGTON, FRIDAY MIDDAY". Source line: Isaac Cline, Monthly Weather Review, September 1900; Texas State Historical Association; Ohio State University, Origins. [VE] [PAY] [loop q2 closes] [loop E1 still open]
> Washington's messages reached Galveston every day from the fourth to the eighth. By Friday the seventh, the city was under a storm warning. But even Friday's midday warning called it a moderate storm.

Rows: factcheck intro-r1 Apply list ("Galveston was not left in the dark. Messages from Washington came in every day from the fourth to the eighth"; MWR "Warning messages were received from the Central Office at Washington on September 4, 5, 6,7, and 8", Cline's report); factcheck intro-r1 row 18 (TSHA storm warning 7 Sept, Friday verified); factcheck intro-r1 row 19 (OSU Origins "that warning still called the storm a moderate one, not a hurricane", SECONDARY, named on the source line). Round 3, grade r2 fixes 1 and 5: the generic first-person "I read Cline's own report" line and "left in the dark" cut (also clears the borderline reveal-flip); opens on the record, MWR "received from the Central Office at Washington on September 4, 5, 6,7, and 8". The warning Galveston got was Washington's view, which lands the Claim's "did not ignore a warning" (grade fix 5).

### I1-S5 — narration
**Picture:** slow return to the Galveston Daily News page of 1891, popfig "JULY 16, 1891", "ABSURD DELUSION" chip back on. Telegraph-key click on the last line. [Q] [loop L-intro open] (carried into A1)
> Long before any of those messages, the city had Cline's word, in print. Why would he once have called the fear of a storm like this an absurd delusion?

Rows: sources-cline.md §1 and factcheck-E.md H1-S2 (Cline wrote the part of the 16 July 1891 article with "simply an absurd delusion"); factcheck-D.md I1-S6 ("a storm like this ... absurd delusion", CONFIRMED fair). Old "nine years earlier, from its own weatherman" and the "So" opener dropped (grade fix 8). Old I1-S5 (landfall and toll) removed: both now spoken in H1-S3 (grade fix 1). Round 3, grade r2 fix 8: "already" dropped; "the fear of a storm like this" kept as the factcheck intro-r2 row 37 wording (it names the fear, matching H1-S2, and needs no antecedent two minutes back).

## Act briefs (text only, written before prose; `references/script-scaling.md` "Act brief")
- **A1 · "An absurd delusion" (1891).** Purpose: show the belief was given to the city by its expert, in print. Question: why would a weatherman say that? Reveal: his reasoning (the shallow shelf and the low land to the north would spread the water). Visual: the 16 July 1891 Galveston Daily News page, the island elevation map (highest point about 8.7 ft). Exit hook: nine years later, the same man was in charge of warning the city.
- **A2 · Havana.** Purpose: the people who read the storm right. Belen Observatory, Father Benito Vines, Father Lorenzo Gangoiti; the US Weather Bureau moves its warning centre to Cuba after the war; NOAA: the Bureau "decreed that only its forecasts would be carried over the telegraph". Exit hook: Havana says northwest into the Gulf; Washington says it will turn.
- **A3 · The turn that never came (4 to 7 September).** Meteorology layer: why storms near that latitude usually recurve, and why this one did not. The steamer Louisiana passes through the centre in the Gulf on 6 September. Warnings from Washington on 4 to 8 September; storm warning at Galveston on the 7th. Ends on the `cta-hinge` tease.
- **CTA** (book ad, `config.yaml channel.cta`).
- **A4 · Saturday (8 September).** Payoff: "Gulf rising, water covers streets of about half of city." Cline drives to the Gulf and times the swells; barometer falls to twenty-eight point four eight inches; Cora Cline lost.
- **A5 · Two stories.** The Library of Congress films of the ruins. At least six thousand lives lost in Cline's own count (eight thousand most cited; six to twelve thousand range). Cline's own report against his later memoir; what Larson disputes. Cuban press criticism of the Bureau in October and November 1900.
- **A6 · After.** The seawall and the grade raising (to be researched and verified before writing). Close: answer E1, dated forward window, signature line.

<!-- LOCKED ACTS (spliced from acts/*.md; edit the act file, then re-splice) -->

## A2 · Havana
Chapter card: Purpose · show who read this storm right: the Jesuit observatory at Belen, its record under Father Benito Viñes and Father Lorenzo Gangoiti, and how the Weather Bureau came to sit beside it in Havana and own the wire.
Chapter card: Question · if Havana had the better storm readers, why couldn't their read of this storm reach Galveston?
Chapter card: Reveal · after the war the Bureau moved its hurricane warning center into Havana itself; by one Cuban account Belen was barred from publishing forecasts from eighteen ninety-eight; the island's lines carried no weather messages and the Bureau's own Havana office reported only through Washington; so what Gangoiti saw on the third had no road to Galveston.
Chapter card: Visual event · Havana map with two pins in one city (BELEN · WEATHER BUREAU); the arrow from Jamaica to Havana; three dated cards for the decree that will not stack; the Havana line rerouted through Washington; Belen's line going dark short of the Galveston island graphic; the two arrows from the hook side by side on 4 September.
Chapter card: Exit hook · Paul (P3): the Bureau's own man in Havana found it "not severe"; so why was Washington so sure it would curve away? (loop L-A2, paid in A3-S1).

### A2-S1 — narration
**Picture:** self-made map, slow pan south from the Galveston island graphic across the Gulf to the Florida Straits; Key West pinned, Havana pinned below it, chip "ABOUT 100 MILES"; popfig "HAVANA · CUBA"; lower-third "BELEN OBSERVATORY · JESUIT COLLEGE OF BELEN". Source line: NOAA AOML, 2015; self-made map. (No Belen photograph confirmed: footage-inventory.md. Request to the inventory pass: one public-domain period Havana view, e.g. Library of Congress, or a reproduction of the 4 September weather map, for one real image in the act; nothing sourced yet.) [VE] [RS] [Q] (who were these people?)
> Now cross the water from Galveston to Havana, about a hundred miles south of Key West. At the Jesuit college of Belen there, the priests ran a weather observatory. They'd been recording Caribbean storms since before the Weather Bureau existed. That's the office that read this storm right. Remember Belen, because what its priests saw on the third of September never reached Galveston.

Rows: about a hundred miles: factcheck/a2-r1.md rows 1 and 2 (Wikipedia Straits of Florida, 106 miles Havana to Key West). Belen, Jesuit, Havana: sources-cuba.md §1 (AOML); factcheck/a2-r1.md row 3 (cubamemorias.com "Fundado por los Padres Jesuítas en la Habana en 1857"). "since before the Weather Bureau existed": factcheck/a2-r1.md row 4 (Bureau 1890; Viñes directing Belen from 1870; founding year conflicts, none spoken). "read this storm right": sources-cuba.md §1 and §4 (AOML Belen northwest into the Gulf; the track went into the Gulf); factcheck/a2-r1.md row 5.

### A2-S2 — narration
**Picture:** text card on aged paper, "P. BENITO VIÑES, S.J. · DIRECTOR FROM 1870" (no portrait confirmed, footage-inventory.md); self-made sky graphic: clouds ahead of a storm, a long swell line, a barometer needle; chip "1875: A WARNING BEFORE THE STORM"; chip "FATHER HURRICANE"; then the "VIÑES" card slides left and a second card slides in, "P. LORENZO GANGOITI · DIRECTOR, 1900". Source line: Belen history (1925, reprinted); Wikipedia; NOAA AOML, 2015. [VE] [RS] [HUMAN]
> Its big name was Father Benito Viñes, who took charge of the observatory in eighteen seventy. He spent years on the signs a hurricane sends out ahead of itself: the clouds, the long swell, the barometer. In eighteen seventy-five he warned Havana that a hurricane was coming before it arrived. People in Havana called him Father Hurricane. He also wrote up his findings in a book on West Indian hurricanes. Viñes died in eighteen ninety-three. Father Lorenzo Gangoiti took over, and Belen kept up Viñes's storm forecasting around Cuba.

Rows: book on West Indian hurricanes (findings, audience not claimed): factcheck/a2-r2.md row 1. Viñes d. 23 Jul 1893, Gangoiti successor and director in 1900: sources-cuba.md §1 (cubamemorias.com "a quien sucedió el Director, el P. Lorenzo Gangoiti"); factcheck/a2-r1.md rows 12 to 14. "carried on the work of Fr. Benito Viñes in forecasting storms in the vicinity of Cuba": sources-cuba.md §1 (AOML); factcheck/a2-r1.md row 15; a2-r2.md row 2. Viñes head from 1870: sources-cuba.md §1 (cubamemorias.com "En 1870 se puso al frente del Observatorio el P. Benito Viñes"); factcheck/a2-r1.md row 7. Signs list: factcheck/a2-r1.md row 8 (Wikipedia quoting NOAA, swell, waves, barometer data; wording as corrected). 1875 warning: factcheck/a2-r1.md row 9 (Wikipedia "On September 11, 1875, Viñes very likely issued the first-ever hurricane warning"; the line does not say "first"). Father Hurricane in Havana: factcheck/a2-r1.md row 10 (SECONDARY, Rubiera via cubamemorias.com/?p=25235). TTS: probe "Viñes" (vin-YES) before voicing; respell only if the probe fails (references/homographs.md rule).

(A2-S3 folded into A2-S2 in round 3; numbering kept so other files' references stay valid.)

### A2-S4 — narration
**Picture:** Caribbean map, an arrow lifts from Kingston, Jamaica, and lands on Havana; chip "1898: SPANISH-AMERICAN WAR"; chip "BUREAU WARNING CENTER · JAMAICA → HAVANA"; then a Havana close-up with two pins, "BELEN" and "US WEATHER BUREAU · STOCKMAN"; lines run from the Bureau pin to Jamaica, Haiti, Santo Domingo, Puerto Rico and ships; one long line runs north to a "WASHINGTON" pin, and from there down to the Galveston island graphic, which lights. Source line: NOAA AOML, 2015; Monthly Weather Review, September 1900. [VE] [RS] [Q] (two offices, one wire: whose forecast travels?)
> Then came the Spanish-American War, in eighteen ninety-eight. Afterward, with the United States running Cuba, the Weather Bureau moved its hurricane warning center from Jamaica to Havana. Its man there was a forecaster named Stockman, and his office kept the islands and the ships informed. So now one city had two weather offices, and only one of them answered to Washington. That Washington line was the one Galveston listened to.

Rows: warning center moved Jamaica to Cuba after the war: sources-cuba.md §2 (AOML "the United States Weather Bureau (USWB) moved its hurricane warning center from Jamaica to Cuba"); factcheck/a2-r1.md rows 17, 18 (war dated, not the move), 22 (US military government). Stockman: factcheck/a2-r1.md row 19 (MWR "W. B. Stockman, Forecast Official"). Islands and ships informed: sources-cuba.md §2 (MWR Sep 1900 "Stations in Cuba, Jamaica, Haiti, Turks Island, Santo Domingo, and Porto Rico and shipping interests were fully informed"); row 20. Two offices: row 21. "That Washington line was the one Galveston listened to" and the picture's Washington-to-Galveston line: sources-cuba.md §3 (MWR "Warning messages were received from the Central Office at Washington").

### A2-S5 — narration
**Picture:** two index cards drop onto the desk one at a time and refuse to stack: "1898 · RUBIERA: BELEN BARRED FROM PUBLISHING FORECASTS" (lands first, stays on top), "AUG 28, 1900 · LARSON, ISAAC'S STORM: MOORE TO WESTERN UNION, 'GREATLY ANNOYED BY INDEPENDENT OBSERVATORIES'" (tag "AS QUOTED BY ERIK LARSON"); chip "DECREE: DATE?". Source line: José Rubiera, OnCuba, 2015; Erik Larson, Isaac's Storm (via Econlib); also a Moore to Eckert letter of 20 September 1900 (Pietruska, 2016; citation only, contents unseen). [VE] [RS] [PAY] (whose forecast travels: not Belen's)
> José Rubiera, a Cuban meteorologist, writes that in eighteen ninety-eight Belen was barred from publishing its forecasts. Then, less than two weeks before the storm, Willis Moore wrote the head of Western Union. He said the Bureau in Cuba was greatly annoyed by independent observatories.

Rows: Rubiera 1898 bar: sources-cuba.md §2 ("se le prohíbe dar a conocer públicamente sus pronósticos", SECONDARY, attributed); factcheck/a2-r1.md rows 28, 29 ("Cuban meteorologist"). "the country's only weather institution": sources-cuba.md §2 (Rubiera "única institución meteorológica existente en ese entonces en el país", SECONDARY, inside his attribution). Letters in August and September 1900: sources-cuba.md §2 and Conflicts 1 (Larson via Econlib, 28 Aug, factcheck rows 30, 31; Pietruska fn 86, Moore to Eckert 20 Sept 1900, citation only, row 32). Card quote: sources-cuba.md §2 (Econlib quoting Larson). Twelve days = 8 to 20 September, computed (row 33). Spoken Larson sentence keeps checked wording (factcheck/a2-r1.md row 30: head of Western Union, "greatly annoyed by independent observatories"). The 20 Sept archive letter stays on the card only (content unseen). Hook H1-S4 spent the rule itself; this segment adds only its disputed dates. Merges r1 S5 and S6.

### A2-S6 — narration
**Picture:** the telegraph line graphic over a map of Cuba: the island's government lines drawn in, a stamp "WAR DEPARTMENT" lands on them, then a chip "NO WEATHER MESSAGES"; a direct line Havana to New Orleans is drawn, then cut, and the message reroutes up to the "WASHINGTON" pin and back down to New Orleans; chip "WASHINGTON DECIDES". Source line: Al Roker, HistoryNet (secondary); NOAA AOML, 2015. [VE] [RS] [Q] (what did that leave Belen?)
> On the island itself, the government telegraph lines were run by the American War Department. At the Bureau's request, it banned weather messages from them. Moore also stopped his own Havana office from wiring New Orleans directly. Havana's reports went to Washington first, so Washington decided what New Orleans was told.

Rows: all SECONDARY (Roker, HistoryNet; byline confirmed, factcheck/a2-r1.md row 35), named on the source line, not spoken (grade fix 4 and fix 7, matching A2-S9). War Department lines: row 36 ("the U.S. War Department controlled all of Cuba's government-owned telegraph lines"). Ban at the Bureau's request: row 37. Havana to New Orleans cut: row 38. "Havana would report directly to Washington, and Washington would decide what information to give New Orleans": row 39 (the plain-words reason for the routing). sources-cuba.md §2, Conflicts 2.

### A2-S7 — narration
**Picture:** back to the Havana close-up, the "BELEN" pin; the Viñes and Gangoiti cards from A2-S2 return beside it; chip "MON SEPT 3 · BELEN: A NEW STORM"; a thin line leaves the Belen pin north across the Gulf toward the Galveston island graphic and stops short of it, while the island stays lit only by the Washington line from A2-S4. Source line: Al Roker, HistoryNet (secondary); NOAA AOML, 2015. [VE] [RS] [HUMAN]
> Gangoiti had the instruments, the records and thirty years of method. On Monday the third of September, he observed a new storm. He read the sky by Viñes's model. He'd been writing to Willis Moore since late eighteen ninety-eight, and the Bureau was still writing to him that August. So the Americans could hear him. Galveston couldn't. His forecast never left Havana.

Rows: "the instruments, the records" mirrors A1-S8 on Cline; thirty years = 1870 to 1900, computed (factcheck/a2-r1.md row 16). Gangoiti observed a new storm Mon 3 Sep: sources-cuba.md §1 (Roker "On Monday, September 3, Father Lorenzo Gangoite ... observed a new storm", SECONDARY); factcheck/a2-r1.md row 41. Letters: factcheck/a2-r1.md rows 23 and 25 (Gangoiti to Moore 30 Nov 1898, Moore to Gangoiti 12 Dec 1898; Blythe to Gangoiti 1 Aug 1900, said as "the Bureau"; contents unseen, the line claims none). "So the Americans could hear him": letters plus Rubiera "comunica a los meteorólogos norteamericanos" (row 51, SECONDARY). Sources: sources-cuba.md §1 (Rubiera, Gangoiti "comunica a los meteorólogos norteamericanos", SECONDARY; paid in A2-S8). "no road across the Gulf to Galveston" = the consequence of the rule spent in H1-S4; Galveston's warnings came only from Washington: sources-cuba.md §3 (MWR "Warning messages were received from the Central Office at Washington"); factcheck/a2-r1.md row 42.

### A2-S8 — narration
**Picture:** NOAA 1900 weather map for 4 September, the storm over western Cuba, Galveston pinned at the top left of the frame; a dashed Washington arrow toward south Florida, chip "WASHINGTON, SEPT 4: SOUTH FLORIDA"; then the Belen arrow from the hook, northwest into the Gulf, aimed across the water at the Galveston pin, chip "BELEN: NORTHWEST, INTO THE GULF"; last chip "RUBIERA: 'STRENGTHEN IN THE GULF'". Source line: NOAA AOML, 2015; Al Roker, HistoryNet (secondary); José Rubiera, OnCuba, 2015. [VE] [RS] [HUMAN]
> Then the storm reached Cuba. Washington's note, dated the fourth, had it moving over western Cuba toward the south Florida coast. At Belen, they read the same storm going northwest, into the Gulf of Mexico. And Rubiera writes that Gangoiti told the Americans it would grow stronger out there and threaten their coast.

Rows: Washington's 4 Sep note "A tropical disturbance was moving over western Cuba and heading for the south Florida coast", signed Moore: sources-cuba.md §3 (SECONDARY, Roker; attribution on the source line, matching A2-S6); factcheck/a2-r1.md row 49. Belen northwest into the Gulf: sources-cuba.md §1 (AOML); row 50. Gangoiti to the Americans, stronger, threat to the coast: sources-cuba.md §1 (Rubiera, SECONDARY, attributed aloud); row 51. "curve quietly back out into the Atlantic": Rubiera "Piensan que el huracán recurvará tranquilamente para el Atlántico"; row 52. Crossing on the fourth is spent in I1-S1; this line adds what each office made of it.

### A2-S9 — Paul on camera
**Picture:** Paul full frame (P3) alone at an empty desk, holding and showing nothing (Omni prompt: empty desk); the NOAA 4 September map with both arrows drawn on it is an on-screen graphic panel beside him, composited over the frame, not part of the clip; chip in the first second "STOCKMAN, MWR: 'NOT SEVERE IN THE WEST INDIES'". [HUMAN] [Q] [loop L-A2 open] (why was Washington so sure it would curve away? paid A3-S1) [loop L-A1 still open, paid A4] [loop E1 still open]
> Stockman, the Bureau's own man in Havana, later reported it was not severe in the West Indies. So why was Washington so sure it would curve away?

Rows: "The storm was not severe in the West Indies although the rains were, in places, torrential": sources-cuba.md §4 (Stockman, MWR Sep 1900); factcheck/a2-r1.md row 48. Washington expected the turn: sources-cuba.md §3 (AOML "expected the storm to recurve to the northeast, as many storms did near this latitude"); row 53. Chapter-exit question (the one allowed); A3-S1 answers it: "Washington's call had a real reason behind it." Twenty-two words.

## A5 · Two stories
Chapter card: Purpose · after the night, show that the record and the retelling split twice: Cline's own September report against the ride later told about him, and the Bureau's own journal against the Havana papers.
Chapter card: Question · which version of what happened did Cline, and Washington, put their names to?
Chapter card: Reveal · Cline's signed report has telephones and Strand Street merchants and no ride; the ride shows up later and no other survivor is known to have backed it; the Bureau's journal printed praise and never named Belen, while the Havana papers wrote about its man Stockman and Washington kept the clippings.
Chapter card: Visual event · the Library of Congress film of men searching the Broadway ruins; the toll chips stacking from Cline's 6,000 to the 6,000 to 12,000 range; two pages side by side, the MWR report and the later retelling.
Chapter card: Exit hook · Galveston was still a sand island under nine feet high, with a city to put back on it (loop L-A5b, paid A6).

### A5-S1 — narration
**Picture:** Library of Congress paper print film, Edison Manufacturing Co. film, camera Albert E. Smith, men working through the wreckage on Broadway (title not shown on screen: it carries flag words); popfig "SUNDAY · SEPT 9, 1900"; chip "FILMED IN THE RUINS DAYS LATER · ©SEPT 24, 1900"; low wind bed, no music. Source line: Library of Congress, paper print collection. [VE] [RS] [HUMAN]
> By Sunday morning, the ninth, the storm had passed and daylight came up over the island. What it left, you can still watch. In the days after, a film company shot men searching the wreckage along Broadway for people who did not survive. The film was copyrighted on the twenty-fourth of September. The Library of Congress keeps a print of it.

Rows: film, Edison Manufacturing Co. (camera Albert E. Smith), LoC paper print, copyright 24 Sep 1900, filmed probably 11 to 19 Sep 1900, so days after Sunday the ninth: LoC item loc.gov/item/00694301 (fact-check a5-r1 rows 2 to 5; open the loc.gov page in a browser once before the source line goes on screen, it returns 403 to scripts). Storm had passed by the morning of Sunday 9 Sep 1900: TSHA "September 9 dawned on desolation" (fact-check a5-r1 row 1). Sunday = 9 Sept 1900 (8 Sept was Saturday, edit_script H1-S3 Rows).

### A5-S2 — narration
**Picture:** the MWR report page, push to the toll sentence in the report (the sentence reads "conservative estimates place the loss of life at the appalling figure, 6,000"); chip "6,000 · CLINE'S REPORT"; then chips stack beside it: "8,000 · MOST CITED" and "6,000 TO 12,000 · RANGE". Source line: Isaac Cline, Monthly Weather Review, September 1900; National Hurricane Center. [VE] [PAY] [loop L-A5 open] (Cline left two accounts of his Saturday: which one holds?)
> Cline's own report put the loss of life at six thousand, and called the estimates conservative. Today the National Hurricane Center says about eight thousand. Cline left two accounts of his Saturday. Which one holds?

Rows: Cline's MWR sentence "conservative estimates place the loss of life at the appalling figure, 6,000": fact-check a5-r1 rows 7 to 9 ("at least" and "few hours' time" are NOAA's editor, not Cline). NHC "8,000 deaths (estimates range from 6,000 to 12,000)": sources-cline.md §5, https://www.nhc.noaa.gov/outreach/history/.

### A5-S3 — narration
**Picture:** self-made map of Galveston Island, the city at its east end lit in one tone, the rest of the island in a second tone; chips "CITY: 6,000 TO 8,000" and "WHOLE ISLAND: 10,000 TO 12,000"; then the 1891 page and the MWR report page slide in, side by side, an empty gap between them. Source line: Texas State Historical Association; National Park Service. [VE] [Q] [loop L-A5 open]
> The numbers differ because some count the city and some count the whole island. Even the lowest of them is about one person in every six who lived in the city. The two accounts Cline left of his own Saturday don't match.

Rows: city 6,000 to 8,000, whole island 10,000 to 12,000: sources-cline.md §5 (TSHA "Between 6,000 and 8,000 people in the city of Galveston had died"; whole island 10,000 to 12,000, TSHA and NPS). "Two accounts": sources-cline.md §3 (his own report) and §4 (later claims). Dual scope named in the same sentence (quickref "dual-scope stats"). "Two accounts": report (MWR) against Cline's first-person cart quote on the NOAA 200th page, tied to the 1945 memoir by Wikipedia and NOAA's Works Consulted (fact-check a5-r1 row 15; memoir page text unseen).. One in six: 6,000 of the city's 38,000 (TSHA "the city of 38,000 inhabitants", factcheck-A.md T1-S1) = 15.8 %, about one in six (python3: 6000/38000 = 0.158).

### A5-S4 — narration
**Picture:** the MWR report, slow push to "The public was warned, over the telephone and verbally" and then to "I went down on Strand street and advised some wholesale commission merchants"; lower-third "ISAAC CLINE · SPECIAL REPORT · MWR, SEPT 1900"; archive Strand Street storefronts (Library of Congress, if licensed; else the report page held). Source line: Isaac Cline, Monthly Weather Review, September 1900 (NWS Heritage reprint). [VE] [RS]
> The first is his report, printed in the Weather Bureau's own journal that September. The public was warned by telephone and word of mouth, he wrote, and he went to Strand Street to advise some merchants.

Rows: sources-cline.md §3: "The public was warned, over the telephone and verbally."; "I went down on Strand street and advised some wholesale commission merchants". Byline signed "Isaac M. Cline, Local Forecast Official and Section Director": factcheck-B.md I1-S1. Printed in MWR Sept 1900: sources-cuba.md header (MWR 28(9)).

### A5-S5 — narration
**Picture:** Texas State Historical Association Handbook entry, the sentence about the horse-drawn cart lit; a self-made sketch-line of a cart running through low streets on the elevation map; then a second line along the beach, chip "LATER TELLINGS: ON HORSEBACK"; book spine "STORMS, FLOODS AND SUNSHINE · 1945". Source line: Texas State Historical Association Handbook; Wikipedia summary of later accounts. [VE] [HUMAN]
> The second story grew over the years. Texas's state history handbook says he drove a horse-drawn cart through the low parts of town, warning people to leave. Other tellings put him on horseback, riding the beach. The ride is usually traced to his memoir, Storms, Floods and Sunshine, which came out in nineteen forty-five.

Rows: TSHA: Cline "drove a horse-drawn cart through low areas warning people to leave": sources-cline.md §4. Horseback along the beach: sources-cline.md §4 (Wikipedia 1900 article "reportedly rode along the beach on horseback to warn residents", SECONDARY). Memoir title and 1945: sources-cline.md §4 (Wikipedia Isaac Cline). Ride tied to the 1945 memoir by Wikipedia (two articles) and the NOAA first-person quote; memoir pages unseen, hence "usually traced" (fact-check a5-r1 rows 20 to 22).

### A5-S6 — narration
**Picture:** cover of Erik Larson, Isaac's Storm (1999), lower-third "ERIK LARSON · AUTHOR, ISAAC'S STORM"; chip "NO OTHER SURVIVOR KNOWN TO BACK IT"; then back to the MWR report, every page flicking past, chip "NO RIDE IN THE REPORT". Source line: Erik Larson, Isaac's Storm, 1999 (as summarised by Wikipedia), and Larson in Salon, 29 Sept 1999; Isaac Cline, Monthly Weather Review, September 1900. [VE] [RS] [PAY]
> Erik Larson, who wrote the nineteen ninety-nine book Isaac's Storm, says no other survivor is known to have backed that ride up. He told an interviewer that Cline most likely warned some people on the beach. He could not see how Cline warned six thousand. And the report Cline signed that September doesn't have a ride in it at all. It has the drive to the Gulf, the telephone and the merchants.

Rows: Larson: "no other survivors are known to have corroborated these accounts" and "no eyewitnesses reported seeing Cline personally warning people along the beach": sources-cline.md §4 (Wikipedia citing Larson, CONFIRMED as reported by Wikipedia). Isaac's Storm (1999): sources-cline.md §4. Own report has no beach ride, only "I drove to the Gulf", the telephone and Strand Street: sources-cline.md §3 and §4 ("NWS Heritage reprint of Cline's own report does not contain a beach ride"). "The drive to the Gulf" named only as a line in the report; A4 narrates the drive itself. Larson in Salon, 29 Sep 1999 (https://www.salon.com/1999/09/29/larson/): "Most likely [Isaac] did go to the beach and warn some people — but did he warn 6,000? I don't see how that is possible." (fact-check a5-r1 rows 24 to 27). The Wikipedia "did not warn anyone" line is dropped.

### A5-S7 — Paul on camera
**Picture:** Paul full frame (P5), Paul at an empty desk; the MWR report page and the TSHA page appear as an on-screen graphic beside him, side by side, the report's merchants and telephones lines lit. Popfig "SEPT 1900 · LATER" in the last second. [HUMAN] [PAY] [loop L-A5 closes]
> Put the two side by side. The ride only shows up later, and no one else is known to have backed it up.

Rows: report content: sources-cline.md §3. Ride later, uncorroborated: sources-cline.md §4 (TSHA states it; Wikipedia/Larson "no other survivors are known to have corroborated"). "No one else is known to have backed it up" follows Larson's "not known to have corroborated" (fact-check a5-r1 row 30).

### A5-S8 — narration
**Picture:** the Monthly Weather Review, September 1900, page 376, the reprinted Boston Herald editorial of 17 September, the sentence "It was not through any lack of attention on the part of the forecasters" lit; then a search box graphic over the year's MWR issues I could open, "BELEN" typed in, every one returning nothing; chip "BELEN: 0 · ISSUES READ". Source line: Monthly Weather Review, 1900 (Boston Herald, 17 Sept 1900, as reprinted). [VE] [RS] [Q] [loop L-A5a open] (did anyone say Washington got it wrong?)
> Washington told its own story in that same journal. It reprinted a Boston newspaper piece that said the forecasters had not failed the Texas coast for lack of attention. I searched that year's issues for Belen. In every one I could read, its name never comes up.

Rows: MWR p. 376, Boston Herald 17 Sep 1900: "It was not through any lack of attention on the part of the forecasters": sources-cuba.md §5. "Belen"/"Belén"/"Gangoiti" appear nowhere in any 1900 MWR issue grepped (Feb to Oct; Jan, Nov, Dec not retrievable): sources-cuba.md header. "Every one I could read" keeps that limit in the spoken line. Herald full sentence: "It was not through any lack of attention on the part of the forecasters that the victims of the hurricane on the Texas coast were overtaken by such a terrible disaster" (MWR Sept 1900 p. 376; fact-check a5-r1 row 31). Three issues unretrievable (row 33).

### A5-S9 — narration
**Picture:** Havana newspaper mastheads, La Discusión and Diario de la Marina, 1900 (archive, if found; else typeset mastheads on a self-made card); chips "LA DISCUSIÓN · OCT 27 · NOV 14, 1900" and "DIARIO DE LA MARINA · OCT 30, 1900"; then a National Archives box label graphic, "RG 27 · BOX 1475". Source line: National Archives, Weather Bureau records, RG 27, box 1475, as cited by historian Jamie L. Pietruska (2016). [VE] [RS] [PAY] [loop L-A5a closes]
> In Havana, the papers had Stockman on their pages. That October and November, La Discusión and the Diario de la Marina ran pieces about the Bureau's man there. Clippings of them still sit in the Weather Bureau's own files at the National Archives. So within two months of the storm, the Bureau's man in Havana was in the Cuban papers, and Washington kept the clippings.

Rows: La Discusión 27 Oct and 14 Nov 1900, Diario de la Marina 30 Oct 1900, about Stockman (tone unseen), clipping in box 1475, NARA RG 27: sources-cuba.md §5 and §6 (Pietruska 2016, JGAPE 15(4), fn 83, 87; CONFIRMED as archive citation only, text unseen). Author "Jamie L. Pietruska" (Crossref, fact-check a5-r1 row 41). [settled: wording cut to what Pietruska fn 83, 87 support, fact-check a5-r1 rows 35 to 39; tone of the clippings unseen]. "Stockman, the Bureau's man in Havana": acts/a2.md A2-S4 (MWR "W. B. Stockman, Forecast Official"). "Within two months": 8 Sept to 27 Oct 1900 is seven weeks (first La Discusión clipping), writer's inference from the citation dates.

### A5-S10 — narration
**Picture:** a portrait card for Willis Moore (if a public-domain portrait is found; else his name on the lower-third card from the intro), chip "NO STATEMENT FOUND"; slow return to the island elevation graphic from the hook tail, the sea-level line at the island's top, chip "HIGHEST POINT ABOUT 8.7 FT", the ruined city drawn in grey on it. Source line: NOAA AOML, 2015; National Park Service. [VE] [Q] [loop L-A5b open] (what does a city do on ground the Gulf just went over? paid A6) [loop E1 still open]
> I couldn't find a single statement from Willis Moore saying Havana had called this storm right. The track had already said it for him: northwest, into the Gulf, the way Belen called it. And the island hadn't moved. Galveston was still a sand island, under nine feet at its highest point, with a whole city to put back on it. So what do you do with ground the Gulf has just gone over?

Rows: no Moore or Bureau admission found: sources-cuba.md §5 ("Moore or Bureau admitted Cuban view was right | UNSOURCED | none | No such statement found"); sources-cuba.md §2 ("Moore's own words defending a ban ... Not found in any fetchable primary"). Highest point 8.7 ft: factcheck-A.md T1-S1 (NPS "the highest elevation on Galveston Island was 8.7 feet"). Chapter-exit question (quickref exception); A6 answers it (seawall, grade raising) and is not narrated here. Track northwest into the Gulf as Belen said: sources-cuba.md §1 (AOML "the storm moved to the northwest and into the Gulf of Mexico") and §5 ("the track facts (Gulf, not recurve) show the Belen side matched the track").

## A6 · After
Chapter card: Purpose · show what Galveston built once it stopped believing the Gulf could not reach it, test it against the next big storm, then answer the episode loop in the Claim's terms.
Chapter card: Question · would a wall and a raised city have changed the count, and why did so few leave in nineteen hundred?
Chapter card: Reveal · in August nineteen fifteen a hurricane with a sixteen point two foot surge hit a walled, raised city that had a day's warning: a dozen or fewer lives lost inside the city; in nineteen hundred the warning on the wire said moderate, the city's own expert had called the danger a delusion, and Havana's track was kept off the wire.
Chapter card: Visual event · cross-section graphic of the curved seawall beside the old 8.7 ft island line; archive photographs of buildings on jackscrews and the dredge fill; the schooner on top of the wall in 1915; Paul (P6) full frame for the answer.
Chapter card: Exit hook · none (last act): dated forward window, then the signature line over the title card.

### A6-S1 — narration
**Picture:** Rosenberg Library or Library of Congress photograph of the 1900 ruins fading to a blank engineering sheet; lower-thirds one after another "HENRY MARTYN ROBERT", "ALFRED NOBLE", "HENRY CLAY RIPLEY", tag "BOARD OF ENGINEERS · 1901 TO 1902"; chip "REPORT · JAN 25, 1902". Source line: Rosenberg Library; American Society of Civil Engineers. [VE] [Q] [loop L-A6 open] (could anything built by hand hold back that water?)
> Galveston stayed on its island and called in three engineers. They drew up a two-part plan to keep the water out. Nobody could know yet whether it would hold.

Rows: sources-a6.md §1 (Rosenberg: board "From September 1901 to January 1902", names; ASCE: three-member board, report 25 Jan 1902). "Stayed on its island" is the writer's framing of the city rebuilding in place (sources-a6.md §2 and §3). "Two parts" = seawall and grade raising, Rosenberg "drafted plans for the Seawall and grade raising".

### A6-S2 — narration
**Picture:** self-made cross-section graphic: the curved concrete face rising from the beach, chips "17 FT" and "16 FT WIDE AT BASE"; the A1 island line returns beside it, "HIGHEST POINT IN 1900: 8.7 FT", the wall standing about twice its height; then a period photograph of the wall under construction (Rosenberg Library or Library of Congress, if cleared); chip "3.3 MILES · 1902 TO 1904". Source line: Rosenberg Library; American Society of Civil Engineers; National Park Service. [VE] [RS]
> The first part was a wall. Work began in September of nineteen oh two. By nineteen oh four the city had three point three miles of curved concrete along its Gulf beach. It stood seventeen feet above low tide, about twice the height of the highest ground on the island in nineteen hundred.

Rows: sources-a6.md §2 (Rosenberg: "commenced in September 1902"; "3.3 miles long, 17 feet high, and measured 16 feet wide at the base"; ASCE "Built between 1902 and 1904", "17 feet above mean low water"). "Above low tide" = "above mean low tide", qualifier on the source line. Highest ground 8.7 ft: edit_script.md T1-S1 rows (NPS). "About twice" = 17 against 8.7 (1.95). "Curved concrete": ASCE "the curved concrete section".

### A6-S3 — narration
**Picture:** archive photographs of Galveston houses up on jackscrews, a dredge pipe pouring wet sand between them (Rosenberg Library, Library of Congress, if cleared); self-made map, the city cut into quarter-mile squares, each one filling in turn; chips "1903 TO 1911", "ABOUT 2,000 BUILDINGS", "UP TO 11 FT"; last beat, a church on jacks, chip "ABOUT 3,000 TONS". Source line: Texas State Historical Association; American Society of Civil Engineers. [VE] [RS] [HUMAN]
> The second part was bigger. Starting in nineteen oh three, dredges pumped sand from the harbor entrance into the city, one walled-off section at a time. About two thousand buildings were jacked up by hand first, so the sand could go underneath. In places the ground rose as much as eleven feet. One church weighed about three thousand tons, and its services kept to schedule while it went up.

Rows: sources-a6.md §3 (ASCE: "from 1903-1911", "quarter-mile-square sections" each enclosed by a dike, "Around 2,000 buildings were raised on hand-turned jackscrews", hopper dredges; TSHA: "sand pumped from the Gulf floor raised the grade as much as seventeen feet", "2,146 buildings", "a 3,000-ton church", "church services were held on schedule"). Sand source: ASCE "The sand fill was dredged from the entrance to Galveston Harbor"; NOAA 200th "sand dredged from Galveston's ship channel" (TSHA's "Gulf floor" outvoted; factcheck a6-r1 row 10). Buildings: TSHA 2,146 vs ASCE "Around 2,000 ... hand-turned jackscrews", so "about" (row 12). Height: ASCE fill "from a few inches to eleven feet thick"; NOAA 200th "heights varying from one to up to 11 feet" against TSHA and AOML seventeen, so "as much as eleven" (rows 13, 17). "Bigger" is the writer's framing (city-wide fill against a 3.3 mile wall).

### A6-S4 — narration
**Picture:** NOAA-style track map, August 1915, a storm line coming ashore southwest of Galveston, popfig "AUGUST 1915"; then the cross-section graphic from A6-S2 with the water rising up the curved face, chips "SURGE 16.2 FT" and "WAVES 21 FT"; then a photograph of the schooner Crockett wrecked on top of the wall (Rosenberg Library, if found and cleared), chip "2 SMALL CHIPS". Source line: National Weather Service Houston/Galveston; Rosenberg Library. [VE] [RS] [PAY] [loop L-A6 closes]
> Then in August of nineteen fifteen, another big hurricane came ashore, about thirty miles southwest of the city. The surge reached sixteen point two feet. Waves crested at twenty-one feet. A four-masted schooner was thrown over the wall and pounded apart on top of it. The wall itself came out of it with two small chips.

Rows: sources-a6.md §4 (NWS HGX 1910s: "made landfall 30 miles southwest of Galveston"; "storm surge reached 16.2' with wave crests of 21'"; "two small chips near 39th street where the four-masted schooner 'Crockett' was blown over the wall"; "pounded to pieces on top of the wall"; "first real test of the Galveston seawall"; Rosenberg "the hurricane of August 16, 1915"). "The wall came out of it with two small chips" follows NWS "The seawall's only damage was two small chips"; embankment and top pavement loss from 6th to 18th Street is on the NWS page and not spoken (the wall itself, not its embankment).

### A6-S5 — narration
**Picture:** aerial-style map of the city with flood shading in the low parts, chip "FLOODED 40 HOURS";  then two count chips side by side, "ALONG THE COAST: AT LEAST 275" and "INSIDE GALVESTON: 12 OR FEWER"; then a telegraph graphic, chip "WARNING · 24 HOURS AHEAD". Source line: National Weather Service Houston/Galveston; Galveston and Texas History Center, Rosenberg Library. [VE] [RS] [PAY] [Q] [loop E1 still open]
> The water still got in. Parts of the city sat flooded for forty hours. At least two hundred seventy-five people lost their lives along the coast in that storm. Inside the city of Galveston, the toll was a dozen or fewer. And this time the Weather Bureau's warning went out a full day ahead.

Rows: sources-a6.md §4 (NWS HGX: "The storm surge flooded parts of the city for 40 hours"; beach "afterwards, it was completely gone"; "275 lives were lost even though the Weather Bureau had issued warnings 24 hours in advance"; Galveston and Texas History Center: "The hurricane caused 12 deaths ... in the city"). City toll spread: Rosenberg history center 12 (galvestonhistorycenter.org/research/1915-storm); Wikipedia citing Monthly Weather Review Aug 1915, 11; NOAA 200th "only six deaths in the city of Galveston" plus 42 on unprotected parts of the island; so "a dozen or fewer" (factcheck a6-r1 row 26; spread kept in sources-a6.md Conflicts). Coast: NWS HGX 275, AOML about 400, NHC 403 to 405 whole path, so "at least" and "along the coast" (row 25). Scope named in each sentence ("in that storm" vs "inside the city") per the dual-scope rule.

### A6-S6 — narration
**Picture:** the three earlier pieces return in a row on a dark card: the 1875 high-water tag from A3, the "NO BRICK-DUST SKY" chip, the "'MODERATE STORM'" chip from I1-S4; then the telegraph line graphic from the hook, the Havana line dark. Source line: Isaac Cline, Monthly Weather Review, September 1900; Ohio State University, Origins. [VE] [HUMAN]
> Galveston had a warning in nineteen hundred too. It called the storm moderate. Many people had built their houses above the high water of eighteen seventy-five. And the brick-dust sky that Cline's office watched for never showed.

Rows: 1875 line: A3-S9 rows (MWR p. 376, Evening Sun, "having built their houses after that event so that the first floor was above the level of danger then"); sky: A3-S7 rows (MWR p. 372, "The brick-dust sky was not in evidence"); moderate storm: edit_script.md I1-S4 rows (OSU Origins, Friday midday warning). "Galveston had a warning in nineteen hundred too" = TSHA storm warning Friday 7 Sept (edit_script.md I1-S4 rows); "It called the storm moderate" = OSU Origins Friday midday warning, SECONDARY.

### A6-S7 — Paul on camera
**Picture:** Paul full frame (P6), plain Omni clip, nothing in his hands; popfig "GALVESTON · 1891 / 1900" in the first second. [HUMAN] [PAY] [loop E1 closes]
> Its weatherman called the danger a delusion, and Havana's forecast was kept off the wire. Galveston wasn't ignoring a warning. It got Washington's, the wrong one.

Rows: angle.md Claim (owner lock): "Galveston did not ignore a warning; the city's own Weather Bureau man had told it in print that a storm seriously damaging Galveston was 'an absurd delusion', and ... the forecasters in Havana who said the storm was heading into the Gulf were kept off the telegraph by the US Weather Bureau"; sources-cline.md §1; sources-cuba.md §1 and §2 (AOML "decreed that only its forecasts would be carried over the telegraph"). Twenty-six words (wc -w). Answers E1 ("why did so few people leave a warned city?") with the Claim.

### A6-S8 — narration
**Picture:** present-day Galveston seawall and its long sidewalk at dawn (Pexels or Pixabay stock), chip "OVER 10 MILES TODAY"; then a calendar graphic, chips "HURRICANE SEASON · JUNE 1 TO NOV 30" and "PEAK · SEPT 10". Source line: Rosenberg Library; NOAA National Hurricane Center. [VE]
> The wall still stands, more than ten miles of it now. The next Atlantic hurricane season opens on the first of June, twenty twenty-seven. Its peak falls around the tenth of September.

Rows: sources-a6.md §2 (Rosenberg "54,790 feet", "10 continuous miles"; ASCE "extends over 10 miles"); sources-a6.md §5 (NHC: season "June 1 to November 30", "The peak of the Atlantic hurricane season is September 10"). "The date this storm came ashore" = 8 September 1900, edit_script.md H1-S3 rows (AOML). "The next season ... twenty twenty-seven" is the dated forward window, true for a publish date between 1 Dec 2026 and 31 May 2027; if the episode ships before 30 Nov 2026 the line needs the current season (editor check against publish date).

### A6-S9 — narration
**Picture:** title card, The Warning Hour; under it, the 1891 page and the telegraph line fade out. Signature closing footnote (DESIGN.md), plays over the title card. [VE]
> Disasters don't ask permission. But they do send warnings. Learn what yours sounds like, and who is sending it, so when it comes, you already know what to do. This was The Warning Hour.

Rows: DESIGN.md "Signature closing footnote" canonical line, tweaked per episode ("and who is sending it" ties it to the Claim: Washington's wire against Havana's forecast). No fact.
