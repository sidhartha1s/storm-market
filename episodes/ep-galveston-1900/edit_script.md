# ep-galveston-1900 · edit_script.md (TTS segment format)

Status: DRAFT 1, hook + hook tail + intro only (phase 3 owner gate). Acts below are briefs, no prose yet.
Angle: `episodes/ep-galveston-1900/angle.md` (owner lock, devq save 26 Oct 26 02:09:38, `t_galveston` "a3" + note).
Research: `episodes/ep-galveston-1900/research/` (sources-cline.md, sources-cuba.md, teardowns.md, footage-inventory.md).

## Packaging (drafted after the lock, per `references/packaging-rules.md`)
- Title: **Galveston 1900: He Said It Was Safe. It Was Not.** (48 characters; Name + Year in the first 16; `title_fre.py` 101.9)
- Thumbnail: school A (Name + Year documentary card): the Library of Congress ruins photograph, place name in frame, one fact line in two words ("ABSURD DELUSION"), with a Field Notes Paul variant for Test and Compare. Not drafted this round.
- Promise the hook must say aloud: the city's own weatherman wrote that a storm seriously damaging Galveston was "an absurd delusion"; nine years later the storm came.

## Runtime and structure
- Target: about 20 to 24 minutes (to be confirmed by the owner; no word budget run yet: needs two probe TTS segments, and this round has no TTS).
- Architecture: Detective (who told Galveston it was safe, and who said otherwise).
- Dominant question: if the warnings existed, why did Galveston go to bed on Friday night thinking it was fine?

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
### H1-S1 — narration
Visual: Paul full frame, on camera, the hook line only. Popfig inside the first second: "GALVESTON, TEXAS · SEPTEMBER 1900". Sound: wind and surf rising under the line. [HOOK] [Q] (the viewer answers: the weatherman)
> A hurricane's coming for your town, and you get one person to tell you how bad it'll be, so who do you trust?

### H1-S2 — narration
Visual: Galveston Daily News, July 16, 1891, page 5, slow push to the line; chip "ABSURD DELUSION"; telegraph-key click on the reveal. Source line: Galveston Daily News, 16 July 1891. [RS] [VE] (contradiction one)
> You'd trust the weatherman, and Galveston's weatherman had told the city in print that a storm seriously damaging Galveston was an absurd delusion.

### H1-S3 — narration
Visual: cut on the swell to the Library of Congress 1900 film of the ruins on Broadway, Galveston; chip "AT LEAST 6,000 LIVES". Source line: Isaac Cline, Monthly Weather Review, September 1900. [RS] [VE]
> He wrote that in eighteen ninety-one, and nine years later, at least six thousand people there lost their lives in a few hours.

### H1-S4 — narration
Visual: NOAA 1900 weather map, Cuba to the Gulf, Havana pinned; popfig "BELEN OBSERVATORY, HAVANA"; chip "KEPT OFF THE TELEGRAPH". Source line: NOAA AOML, 2015. [RS] [VE] (contradiction two)
> And in Havana, forecasters had said this storm was heading into the Gulf, but his own Weather Bureau kept them off the telegraph.

### H1-S5 — narration
Visual: Library of Congress damage photograph, slow push; then the Monthly Weather Review page listing the warnings from Washington. Sound: low swell under the kicker. [loop E1 open] [Q]
> He said it was safe. It was not. Washington sent Galveston warnings all that week. So I wanted to know why a warned city still went to bed on Friday night feeling safe [verify: Galveston residents not alarmed on the Friday night before landfall].

## HT · Hook tail
### T1-S1 — narration
Visual: self-made island elevation graphic of Galveston, sea level line rising to the island's top; chips "ABOUT 38,000 PEOPLE" and "HIGHEST POINT ABOUT 8.7 FT". Source line: Texas State Historical Association; National Park Service. [VE] [Q] q1 open (who was the man)
> Galveston was an island city of about thirty-eight thousand people, and its highest ground stood less than nine feet above the sea. The man who wrote those words had the job of warning it.

## I · Intro
### I1-S1 — narration
Visual: Monthly Weather Review, September 1900, the report's byline; lower-third "ISAAC CLINE · LOCAL FORECAST OFFICIAL, GALVESTON"; then "JOSEPH CLINE · OBSERVER". [PAY] q1 closes; [Q] q2 open (did anyone warn the city)
> If you lived in Galveston in nineteen hundred, your weatherman was Isaac Cline. He was the senior Weather Bureau man on the island, there since about eighteen eighty-nine. His brother Joseph worked in the same office as an observer. The first thing I checked was whether anybody warned the city at all.

### I1-S2 — narration
Visual: Monthly Weather Review page, the warning dates highlighted one by one; chips "SEPT 4, 5, 6, 7, 8" then "STORM WARNING: SEPT 7" then "'MODERATE STORM'". Source line: Isaac Cline, Monthly Weather Review; Texas State Historical Association; Ohio State University, Origins. [PAY] q2 closes; [Q] q3 open (where was the storm all week)
> Somebody did. Washington sent Galveston warning messages on the fourth, fifth, sixth, seventh and eighth of September. On the seventh, Galveston went under a storm warning. Even Friday's midday warning still called it a moderate storm. That sent me after the storm itself.

### I1-S3 — narration
Visual: NOAA 1900 weather maps, September 2 to 8, stepped across Cuba; popfig "BELEN OBSERVATORY, HAVANA"; two arrows drawn from western Cuba: one northwest into the Gulf labelled "HAVANA", one curving northeast labelled "WASHINGTON". Lower-third "WILLIS MOORE · CHIEF, US WEATHER BUREAU". Source line: NOAA AOML, 2015. [PAY] q3 closes; [RS] [VE]; [Q] q4 open (which forecast was right)
> It crossed Cuba on the fourth of September. In Havana, the Jesuit forecasters at Belen Observatory said it was moving northwest, into the Gulf of Mexico. The United States Weather Bureau, run from Washington by Willis Moore, expected it to curve away to the northeast.

### I1-S4 — narration
Visual: hold the two arrows; a telegraph line graphic carries only the Washington arrow's label; chip with NOAA's words "only its forecasts would be carried over the telegraph". Source line: NOAA AOML, 2015. [VE]; q4 still open
> After the Spanish-American War, the Bureau had decreed that only its forecasts would be carried over the telegraph. So two forecasts pointed two different ways, and only one of them was allowed on the wire.

### I1-S5 — narration
Visual: NOAA map, the storm's track pushing northwest into the Gulf; chip "STEAMER LOUISIANA · SEPT 6"; then a slow return to the Galveston Daily News page of 1891, "ABSURD DELUSION" chip back on. Telegraph-key click on the last line. [PAY] q4 closes; [loop L-intro open] (carried into A1)
> The storm went Havana's way. On the sixth, the steamer Louisiana passed through its center, in the middle of the Gulf. And waiting in Galveston was the same man who'd called a storm like this an absurd delusion. Which brings me back to that newspaper, and why a weatherman would ever write those words.

## Act briefs (text only, written before prose; `references/script-scaling.md` "Act brief")
- **A1 · "An absurd delusion" (1891).** Purpose: show the belief was given to the city by its expert, in print. Question: why would a weatherman say that? Reveal: his reasoning (the shallow shelf and the low land to the north would spread the water). Visual: the 16 July 1891 Galveston Daily News page, the island elevation map (highest point about 8.7 ft). Exit hook: nine years later, the same man was in charge of warning the city.
- **A2 · Havana.** Purpose: the people who read the storm right. Belen Observatory, Father Benito Vines, Father Lorenzo Gangoiti; the US Weather Bureau moves its warning centre to Cuba after the war; NOAA: the Bureau "decreed that only its forecasts would be carried over the telegraph". Exit hook: Havana says northwest into the Gulf; Washington says it will turn.
- **A3 · The turn that never came (4 to 7 September).** Meteorology layer: why storms near that latitude usually recurve, and why this one did not. The steamer Louisiana passes through the centre in the Gulf on 6 September. Warnings from Washington on 4 to 8 September; storm warning at Galveston on the 7th. Ends on the `cta-hinge` tease.
- **CTA** (book ad, `config.yaml channel.cta`).
- **A4 · Saturday (8 September).** Payoff: "Gulf rising, water covers streets of about half of city." Cline drives to the Gulf and times the swells; barometer falls to twenty-eight point four eight inches; Cora Cline lost.
- **A5 · Two stories.** The Library of Congress films of the ruins. At least six thousand lives lost in Cline's own count (eight thousand most cited; six to twelve thousand range). Cline's own report against his later memoir; what Larson disputes. Cuban press criticism of the Bureau in October and November 1900.
- **A6 · After.** The seawall and the grade raising (to be researched and verified before writing). Close: answer E1, dated forward window, signature line.
