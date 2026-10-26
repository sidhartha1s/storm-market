# ep-galveston-1900 · edit_script.md (TTS segment format)

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
**Picture:** Paul full frame at 0:00, holding a printed reproduction of the Galveston Daily News page of 16 July 1891; popfig "GALVESTON, TEXAS · SEPTEMBER 1900" inside the first second; the sound under him: newsprint unfolding, then rain on a window, no wind.
> This page of the Galveston paper, from July eighteen ninety-one, told readers no hurricane could send a storm wave big enough to badly damage their city.

Rows: sources-cline.md §1 and factcheck-E.md H1-S4 (same page: "impossible for any cyclone to create a storm wave which would materially injure the city"; "badly" accepted for "seriously/materially", factcheck-D.md H1-S2; "hurricane" for "cyclone").

### H1-S2 — narration
**Picture:** slow push to the column; chip "ABSURD DELUSION"; lower-third "ISAAC CLINE · GALVESTON WEATHER OFFICE, 1900". Source line: Isaac Cline, Galveston Daily News, 16 July 1891. [RS] [VE] (break one)
> Isaac Cline wrote part of it. He still ran the weather office in nineteen hundred.

Rows: sources-cline.md §1 and factcheck-E.md H1-S2 (Cline wrote part of the article); sources-cline.md §2 (Local Forecast Official, in Galveston from 1889); sources-cuba.md §4 (landfall 8 Sept 1900).

### H1-S3 — narration
**Picture:** hard cut to the NOAA 1900 map, Havana pinned, popfig "BELEN OBSERVATORY, HAVANA", one arrow northwest into the Gulf; then the telegraph line graphic, the Washington line lit, the Havana line dark. Source line: NOAA AOML, 2015. [RS] [VE] (break two)
> Over in Havana, the Jesuits at Belen Observatory had said the storm was moving northwest, into the Gulf of Mexico. NOAA says the Bureau decreed that only its forecasts would be carried over the telegraph.

Rows: sources-cuba.md §1 (Belen: northwest into the Gulf; Jesuit, cubamemorias.com via factcheck-B.md I1-S3); sources-cuba.md §2 (decree, NOAA's words with spoken attribution: "only its forecasts would be carried over the telegraph").

### H1-S4 — narration
**Picture:** back to the 1891 page, the light on it dimming; cut to the Monthly Weather Review report page, slow push to the line about his wife. Source line: Isaac Cline, Monthly Weather Review, September 1900. [VE] [HUMAN] [loop E1 open]
> Among the people Galveston lost that night was Isaac Cline's own wife.

Rows: sources-cline.md §3 ("Among the lost was my wife, who never rose above the water after the wreck of the building"); sources-cuba.md §4 (landfall on the evening of 8 Sept).

## HT · Hook tail
### T1-S1 — narration
Visual: self-made island elevation graphic of Galveston, sea level line rising to the island's top; chips "ABOUT 38,000 PEOPLE" and "HIGHEST POINT ABOUT 8.7 FT"; then cut to the NOAA 1900 weather map, Havana pinned, popfig "BELEN OBSERVATORY, HAVANA". Source line: Texas State Historical Association; National Park Service. [VE] [Q] q1 open (what did Havana see?)
> Galveston was an island city of about thirty-eight thousand people. Its highest ground was less than nine feet above the sea. And in Havana, forecasters saw this storm heading somewhere Washington said it wouldn't go.

## I · Intro
### I1-S1 — narration
Visual: Monthly Weather Review, September 1900, the report's byline; lower-third "ISAAC CLINE · LOCAL FORECAST OFFICIAL, GALVESTON"; then NOAA 1900 weather maps, September 2 to 4, the storm stepping across Cuba. Source line: Isaac Cline, Monthly Weather Review; Monthly Weather Review, September 1900. [VE]; q1 still open
> If you lived in Galveston in nineteen hundred, your weatherman was Isaac Cline. He ran the Weather Bureau office on the island. The storm that would hit his city crossed Cuba on the fourth of September.

### I1-S2 — narration
Visual: two arrows drawn from western Cuba: one northwest into the Gulf labelled "HAVANA", one curving northeast labelled "WASHINGTON". Popfig "BELEN OBSERVATORY, HAVANA"; lower-third "WILLIS MOORE · CHIEF, US WEATHER BUREAU". Source line: NOAA AOML, 2015. [RS] [VE] [PAY] q1 closes; [Q] q2 open (which forecast was right?)
> In Havana, the Jesuit forecasters at Belen Observatory said it was moving northwest, into the Gulf of Mexico. Washington's Weather Bureau, run by Willis Moore, expected it to curve away to the northeast.

### I1-S3 — narration
Visual: hold the two arrows; a telegraph line graphic carries only the Washington arrow's label; chip with NOAA's words "only its forecasts would be carried over the telegraph". Source line: NOAA AOML, 2015. [VE]; q2 still open
> NOAA says the Bureau decreed that only its forecasts would go over the telegraph. So the wire carried Washington's version.

### I1-S4 — narration
Visual: NOAA map, the storm's track pushing west-northwest into the Gulf, the Washington arrow fading out; chip "STEAMER LOUISIANA · SEPT 6". Source line: Monthly Weather Review, September 1900. [RS] [VE] [PAY] q2 closes; [Q] q3 open (what was Galveston told as it came?)
> The storm went Havana's way. On the sixth, the steamer Louisiana passed through its center, in the middle eastern part of the Gulf.

### I1-S5 — narration
Visual: the island elevation graphic again, the track line closing on the island; chips "STORM WARNING: SEPT 7" then "'MODERATE STORM'". Source line: Texas State Historical Association; Ohio State University, Origins. [VE] [PAY] q3 closes
> It kept coming across the Gulf, toward the island. By Friday the seventh, Galveston was under a storm warning. Even then, the midday warning called it a moderate storm.

### I1-S6 — narration
Visual: slow return to the Galveston Daily News page of 1891, popfig "JULY 16, 1891", "ABSURD DELUSION" chip back on. Telegraph-key click on the last line. [loop L-intro open] (carried into A1)
> So why would the man running Galveston's weather office once have called a storm like this, in print, an absurd delusion?

## Act briefs (text only, written before prose; `references/script-scaling.md` "Act brief")
- **A1 · "An absurd delusion" (1891).** Purpose: show the belief was given to the city by its expert, in print. Question: why would a weatherman say that? Reveal: his reasoning (the shallow shelf and the low land to the north would spread the water). Visual: the 16 July 1891 Galveston Daily News page, the island elevation map (highest point about 8.7 ft). Exit hook: nine years later, the same man was in charge of warning the city.
- **A2 · Havana.** Purpose: the people who read the storm right. Belen Observatory, Father Benito Vines, Father Lorenzo Gangoiti; the US Weather Bureau moves its warning centre to Cuba after the war; NOAA: the Bureau "decreed that only its forecasts would be carried over the telegraph". Exit hook: Havana says northwest into the Gulf; Washington says it will turn.
- **A3 · The turn that never came (4 to 7 September).** Meteorology layer: why storms near that latitude usually recurve, and why this one did not. The steamer Louisiana passes through the centre in the Gulf on 6 September. Warnings from Washington on 4 to 8 September; storm warning at Galveston on the 7th. Ends on the `cta-hinge` tease.
- **CTA** (book ad, `config.yaml channel.cta`).
- **A4 · Saturday (8 September).** Payoff: "Gulf rising, water covers streets of about half of city." Cline drives to the Gulf and times the swells; barometer falls to twenty-eight point four eight inches; Cora Cline lost.
- **A5 · Two stories.** The Library of Congress films of the ruins. At least six thousand lives lost in Cline's own count (eight thousand most cited; six to twelve thousand range). Cline's own report against his later memoir; what Larson disputes. Cuban press criticism of the Bureau in October and November 1900.
- **A6 · After.** The seawall and the grade raising (to be researched and verified before writing). Close: answer E1, dated forward window, signature line.
