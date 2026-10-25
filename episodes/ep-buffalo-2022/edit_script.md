# ep-buffalo-2022 · edit_script.md (Buffalo blizzard, Erie County, New York, 23 to 27 December 2022)

Lane: documentary (`/storm-episode`). Angle: `angle.md` (owner delegated the pick 26 Oct 26 02:09:38, "angle is your call"; wording tightened by the research pass: "more ... than anywhere else", not "most").
Research: `research/deaths.md`, `research/nws.md`, `research/response.md` (every fact with a URL, PRIMARY or SECONDARY).
Status (26 Oct 26): structure + act briefs by the orchestrator; hook, tail and intro by a separate writer; fact-check in `fact_check.md`; grade in `grade_hook.md`. Nothing is locked: the hook+intro waits for the owner's explicit sign-off. No TTS, no clips, no renders this round.
Publish target: near Christmas, the anniversary window 23 to 27 Dec 26 (owner: "lets drop it near christmas").

## Runtime and shape
- Target: about 20 min (proposal; the owner sets length per episode). 5 acts of 3 to 4.5 min plus hook/intro (about 2 min), close (about 0.5 min), the CTA (24.0 s) and blackouts. `word_budget.py` sizes it once probe TTS exists.
- Architecture: Detective with a twist. Dominant question: **"The warning came days early. So why were so many of the people who lost their lives found outside, and not at home?"**
- Script concept (Claim line, copied): It wasn't people trapped at home: more of the people who lost their lives in Erie County were found outside, in the snow, than anywhere else, eighteen of forty-six, with four more in their cars.
- Ruled out as the lead: snow totals / "blizzard of the century"; raw whiteout drive-through footage; "they froze at home without heat". The twelve no-heat deaths appear inside Act 5, never in the hook.
- Chapters in stakes order: the forecast that was right → Friday morning (the flash freeze and the ban that came as the whiteout did) → outside (the eighteen, Anndel Taylor) → nobody could come (the plows, ambulances, the 911 backlog, the seven) → home was not safe either, and what changed.

## Paul on camera (Christmas touch, owner "santa paulclaus presents....")
Paul wears a Santa hat in every full-frame clip (hook line at 0:00 plus up to 5 turning points, one of them the cta-hinge tease) and on the thumbnail. Note for the Flow/Omni round only; nothing is generated now. The start-frame rule (`scripts/paul_start_frame.py`: every Paul clip from the same start frame) means the hat needs a new start frame, to be raised with the owner at the clip sign-off.

## Hook sound (DESIGN.md "Cold-open hook contract": reasoned per episode)
Wind, not a siren: a self-made or licensed whiteout wind bed fades up under Paul's line, ducks under the narrator, and drops to near silence on the cut to the first "found outside" image. No archive or broadcast audio in the hook.

## Loop table
| id | planted | paid | line |
|---|---|---|---|
| E | H1 (hook) | A3 + A5 | found outside, not at home → why they were out, and why nobody came |
| L0 | T1 (tail) | I1 | (writer sets: the tail's one open gap, paid inside the intro) |
| L1 | I1 end | A1 / A2 | carried into Act 1 (writer sets) |
| L2 | A2 end | A3-S1 | Friday 9:30 a.m.: the ban, and where the people already on the road were |
| cta-hinge | A3 last seg | A4-S1 | tease (≤25 words, Paul full frame): the people who called for help were not the only ones stuck → CTA → payoff in A4-S1's first words (the plows and ambulances in the same drifts) |
| L4 | A4 end | A5 | the seven who waited for an ambulance; and the people who stayed home |

## Act briefs (orchestrator; one writer per act next round, each pasting the Angle block + its brief)

> **ACT 1 — Once in a generation · ~3.5 min**
> **Job:** prove the warning was out early and loud, with the NWS Buffalo product times (18 Dec "very large and powerful storm"; 20 Dec 4:51 a.m. "once in a generation"; Winter Storm Watch 2:22 p.m. Tue 20 Dec; Blizzard Warning 3:54 a.m. Thu 22 Dec, effective 7 a.m. Fri; "True blizzard conditions are rare in Western NY"). The meteorology layer: the bomb cyclone (forecast 1000 to 968 mb in about a day), lake Erie, the wind as the danger, not the snow.
> **In / out:** the forecast desk → Thursday night, rain at 38°F, people heading out Friday for the last workday before Christmas (L1).

> **ACT 2 — Friday morning · ~4 min**
> **Job:** the flash freeze and the timing. Airport: 38°F at 7:24 a.m. to 12°F at 12:54 p.m.; visibility at a quarter mile by 8:39 a.m.; gusts to 69 mph; state of emergency 6 a.m.; the county driving ban effective 9:30 a.m. (SECONDARY, WKBW) after the whiteout had already arrived. Poloncarz: "If anyone is to be blamed, you can blame me." (28 Dec).
> **In / out:** 7:24 a.m. → 9:30 a.m., the ban; the people already on the road (L2 plant).

> **ACT 3 — Outside · ~4 min**
> **Job:** pay E (first half). The eighteen found outside, four in vehicles; the 27 Dec count (17 of 31); Anndel Taylor, 22, stranded about six minutes from home, called 911, nobody could reach her (CBS/CNN). Hochul 26 Dec: "scores and scores of vehicles that were abandoned". NWS warning: frostbite in "as little as thirty minutes"; the stay-with-your-vehicle line [verify for the Erie zone].
> **In / out:** the stalled cars → cta-hinge tease, Paul full frame.

> **CTA** (`config.yaml channel.cta`, 24.0 s) between A3's last segment and A4-S1. Estimate: hook+intro ~2:00, A1 ~3:30, A2 ~4:00, A3 ~4:00 minus a little: CTA about 9:30 to 10:30 of 20 min = 0.48 to 0.52, inside 0.40 to 0.60.

> **ACT 4 — Nobody could come · ~4 min**
> **Job:** the plows, ambulances and fire trucks in the same drifts (Hochul: "I saw them myself in ditches"; DVIDS: the Guard digging out an AMR ambulance 26 Dec); the 911 backlog of 1,100 (NYU Wagner report via Firehouse, SECONDARY); seven Erie County deaths tied to unanswered calls (NYU report via AP); the Guard: 849 mobilized, 124 rescued from stranded cars, 3,755 households checked (DVIDS).
> **In / out:** payoff first words → the seven, and the people who never left home (L4).

> **ACT 5 — Home was not safe either, and what changed · ~3 min**
> **Job:** pays L4 and E. The twelve with no power or heat; the four shoveling; the three-year-old in the hotel pool (family left a dark house); the final count, 46 in Erie County plus one in Niagara County, 47; the 1977 comparison (23 in western New York by the Army Corps count, 29 by the NWS count). The NYU review (2 Jun 23) and the state review (Guidehouse, 4 Aug 23). Close: fact + dated forward window, then the signature line (DESIGN.md "Signature closing footnote"). Christmas lands here, plainly, no sentiment adjectives.

## Packaging (candidates only; the owner picks at the packaging gate)
Not written this round. Title rule: ≤52 chars, Name + Year in the first 40 (`references/packaging-rules.md`). Thumbnail: Paul in a Santa hat (owner idea), school per video type.

---

<!-- HOOK, TAIL, INTRO: written by the writer below this line -->

## H1 · Hook

### H1-S1 — Paul on camera
**Picture:** Paul full frame at 0:00 in a Santa hat, the one hook sentence. Popfig "BUFFALO, NY · DEC 23, 2022" inside the first second. Wind bed fades up under him. [HOOK] [Q] [loop E open]
> A blizzard warning goes out for your town the week of Christmas, and you already know the safest place to ride it out is home.

*register: 8/10*

### H1-S2 — narration
**Picture:** cut on "Buffalo" to a snow-buried street of stalled cars: NY National Guard photo, DVIDS 7571852 (174th Attack Wing runway snowblower on I-90, Buffalo, 26 Dec 2022), public domain. Wind drops to near silence on the cut. Chip "18 FOUND OUTSIDE", then "+4 IN THEIR CARS". Source line: "Erie County Medical Examiner, final count, via WIVB". [VE] [RS] [PAY]
> In Buffalo, New York, two days before Christmas in twenty twenty-two, the record says otherwise. Forty-six people lost their lives in Erie County, and the largest group of them, eighteen, were found outside, in the snow. [verify: final Erie County count 46, 18 found outside, Medical Examiner via WIVB, secondary] Four more were found in their cars. [verify: 4 in vehicles, same final count, secondary]

*register: 8/10*

### H1-S3 — narration
**Picture:** NWS Buffalo forecast discussion text, typed on as a glass card, the phrase highlighted: "a once in a generation type of event". Source line: "NWS Buffalo Area Forecast Discussion, 4:51 a.m. Tue 20 Dec 2022 (IEM archive, FXUS61 KBUF 200951)". Chip "3 DAYS' WARNING". [VE] [RS] [Q]
> And this storm did not sneak up on anybody. Three days before it hit, the weather service in Buffalo wrote that it was a once in a generation type of event.

*register: 8/10*

### H1-S4 — narration
**Picture:** a Guard soldier knocking on a snowed-in front door: NY National Guard photo, DVIDS 7576030 (welfare checks, Buffalo, 30 Dec 2022), public domain. Slow push in. No chip. [HUMAN] [Q] [loop E open]
> So I went looking for two things. Why were so many people out there in it, and why couldn't anybody get to them in time?

*register: 9/10*

## T1 · Hook tail

### T1-S1 — narration
**Picture:** Buffalo Niagara International Airport weather station readout (self-made ASOS log card, rows ticking past: 7:24, 8:06, 8:39). Source line: "Buffalo airport ASOS observations, IEM archive". Chip "FRIDAY · DEC 23". [VE] [Q] [loop L0 open]
> The forecast was right, and it was early. What went wrong that Friday morning came down to minutes, and the airport's own weather station logged every one of them.

*register: 8/10*

## I1 · Intro

### I1-S1 — narration
**Picture:** self-made map, Lake Erie to Buffalo, Erie County outlined, label "WESTERN NEW YORK". Then the ASOS card from T1 returns: "38°F · RAIN" at the pre-dawn rows, then "VIS 1/4 MI · 8:39 AM" lights up, then a red clock chip "DRIVING BAN · 9:30 AM". Source lines: "Buffalo airport ASOS, IEM archive"; "Erie County driving ban, WKBW". [VE] [RS] [PAY] [loop L0 closes]
> Buffalo sits at the eastern end of Lake Erie, in western New York. [verify: Buffalo at the eastern end of Lake Erie] Before dawn on Friday, December twenty-third, it was raining at the airport, at about thirty-eight degrees. [verify: 23 Dec 2022 was a Friday, the last workday before Christmas weekend] By eight thirty-nine that morning, snow and wind had cut the visibility there to a quarter of a mile. Erie County's driving ban took effect at nine thirty. [verify: Erie County ban effective 9:30 a.m. Fri 23 Dec, WKBW, secondary] That's fifty-one minutes after the whiteout reached the airport.

*register: 8/10*

### I1-S2 — narration
**Picture:** DVIDS 7572837 (827th Engineer Co clearing snow to recover an AMR ambulance, Buffalo, 26 Dec 2022), public domain, held wide. Three stat chips stack one by one: "37 STRAIGHT HOURS", "51.9 IN AT THE AIRPORT", "GUSTS 69 MPH". Source lines: "NYS DHSES, 4 Aug 2023"; "NWS Buffalo PNS, 28 Dec 2022"; "Buffalo airport ASOS, IEM archive". [VE] [RS]
> Fifty-one minutes doesn't sound like much. On the last workday before Christmas, it was enough to leave people on the road. Then the storm settled in. The state counted thirty-seven straight hours of blizzard conditions in Erie County. The airport measured fifty-one point nine inches of snow, and gusts there hit sixty-nine miles an hour.

*register: 8/10*

### I1-S3 — narration
**Picture:** DVIDS 7576030 sequence (Guard welfare checks, Buffalo), public domain, over a running tally graphic that builds by date: 27 Dec "17 of 31", 28 Dec "17 of 37", 30 Dec "17 of 39", final "18 of 46", the "outside" bar the longest at every step. Source line: "Erie County counts via NPR/KAXE, AP, WBFO, WIVB". [VE] [RS] [Q] [PAY]
> As the National Guard and the road crews dug the city out, they started finding people. Where they found them is the part that stopped me. I went through every county count that listed where people were found. [verify: outside was the largest category in every county count with a breakdown, 27 Dec to final, secondary] Outside, in the snow, was the largest group in every single one, more than anywhere else.

*register: 9/10*

### I1-S4 — narration
**Picture:** back to the NWS Buffalo forecast discussion card, now the earlier product: "very large and powerful storm system", 4:10 a.m. Sun 18 Dec 2022 (IEM archive, FXUS61 KBUF 180910). Chip "5 DAYS OUT". Slow fade toward the Act 1 blackout. [VE] [Q] [loop L1 open]
> And the forecasters saw it coming even earlier than that warning. The weather service in Buffalo flagged this storm on the Sunday before, five days out. What they saw on their screens that week is where this starts.

*register: 8/10*
