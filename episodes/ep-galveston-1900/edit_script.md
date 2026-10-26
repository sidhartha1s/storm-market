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
**Picture:** Paul full frame at 0:00, holding a printed reproduction of the Galveston Daily News page of 16 July 1891; popfig "GALVESTON, TEXAS · JULY 1891" inside the first second; the sound under him: newsprint unfolding, then rain on a window, no wind. [HOOK] [VE]
> This page of the Galveston paper told readers no hurricane could badly damage their city.

Rows: sources-cline.md §1 and factcheck-E.md H1-S4 (same page: "impossible for any cyclone to create a storm wave which would materially injure the city"; belief the city "will at some time be seriously damaged ... is simply an absurd delusion"); "badly" for "seriously/materially" accepted in factcheck-D.md H1-S2; "hurricane" for "cyclone". Date "from July eighteen ninety-one" moved to the popfig (grade fix 2). Fifteen words.

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
