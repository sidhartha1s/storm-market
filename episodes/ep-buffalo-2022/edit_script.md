# ep-buffalo-2022 · edit_script.md (Buffalo blizzard, Erie County, New York, 23 to 27 December 2022)

Lane: documentary (`/storm-episode`). Angle: `angle.md` (owner delegated the pick 26 Oct 26 02:09:38, "angle is your call"; wording tightened by the research pass: "more ... than anywhere else", not "most").
Research: `research/deaths.md`, `research/nws.md`, `research/response.md` (every fact with a URL, PRIMARY or SECONDARY).
Status (26 Oct 26): structure + act briefs by the orchestrator; hook, tail and intro by a separate writer over six rounds; fact-check `fact_check.md` (0 open `[verify]`, 0 UNVERIFIED); fresh Opus grader each round, `grade_hook.md` then `grade_hook_r2.md` to `grade_hook_r6.md`: 6, 6.5, 6.5, 7.5, 7, 7 of 10. The lock bar is 8, so H1, T1 and I1 are NOT LOCKED (condition b fails, and condition c, the owner's explicit sign-off, is pending). No TTS, no clips, no renders this round.
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
| L0 | T1 (T1-S1) | I1-S1 | how fast Friday morning turned → rain at 38°F before dawn, the whiteout at the airport at 8:39 a.m., the county driving ban at 9:30 a.m., fifty-one minutes apart |
| L1 | I1 end (I1-S5) | A1 / A2 | "How does a forecast that early still end with so many people found outside, in the snow?" → A1 the forecast products, A2 Friday morning |
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
Hook shape: missing (2026-10-26)
PROVISIONAL (26 Oct 26): orchestrator's default pick from `hook_options.md`, owner pick pending; if he picks another shape only the hook and intro are redone.

### H1-S1 — Paul on camera
**Picture:** Paul full frame at 0:00 in a Santa hat; popfig "BUFFALO, NY · DEC 23, 2022" inside the first second; the sound under him: a phone line ringing on and on, low under the wind, with no pickup. [HOOK] [loop E open]
> The biggest group the storm took around Buffalo was found in the open, and some of the nine one one calls never got an answer.

Rows: `research/deaths.md` section 1 "final" and section 3 (18 outside, the largest single category, SECONDARY); `research/response.md` section 5 (NYU Wagner report via AP: "emergency calls that went unanswered due to a backlog", SECONDARY; "some" calls, never every call). The line sets the two facts side by side and does not claim the people outside were the ones who called.

### H1-S2 — narration (the hedge)
**Picture:** on the cut, DVIDS 7576030 (a Guard soldier knocking at a front door during welfare checks, Buffalo, 30 Dec 2022, courtesy photo), public domain, cropped to 16:9. Chip "18 IN THE OPEN". Source line: "Erie County Executive Mark Poloncarz, last reported count, via WIVB". [VE] [PAY]
> That was eighteen people, by the newest numbers the county gave out.

Rows: `research/deaths.md` section 1 "final" (18 outside of 46, three cases pending, so the hedge stays); `fact_check_r6_hook.md` rows 2 and 3.

### H1-S3 — narration
**Picture:** self-made dispatch queue card, a counter running up to "1,100 CALLS WAITING". Source line: "NYU Wagner review, via Firehouse, 5 Jun 2023". Wind holds low. [VE] [RS] [Q]
> By the morning after the first day, eleven hundred emergency calls were waiting in line, a review for the city found later.

Rows: `research/response.md` section 2 (backlog of 1,100 emergency calls "by the morning after the first day", Firehouse citing the NYU report, SECONDARY; report PDF itself not read).

### H1-S4 — narration (the second break)
**Picture:** self-made text card, "7 LIVES · CALLS UNANSWERED". Source line: "NYU Wagner review for the City of Buffalo, via AP, 2 Jun 2023". Wind drops to near silence. [VE] [RS] [Q]
> That same review tied seven of the lives lost in Erie County to calls that went unanswered in the backlog.

Rows: `research/response.md` section 2 and section 5 (seven Erie County deaths tied to unanswered calls due to a backlog, NYU report via AP, SECONDARY). This is the review's seven, never equated with the county's seven delayed-EMS category in `research/deaths.md`.

## T1 · Hook tail

### T1-S1 — narration
**Picture:** Buffalo Niagara International Airport weather station readout (self-made ASOS log card, rows ticking past: 7:24, 8:06, 8:39). Source line: "Buffalo airport ASOS observations, IEM archive". Chip "FRIDAY · DEC 23". [VE] [Q] [loop L0 open] (loop E stated aloud)
> I wanted to know why so many of them were out in it. Part of the answer is how fast Friday morning turned, the day before Christmas Eve, and the airport's weather log shows it.

*register: 9/10*

## I1 · Intro

### I1-S1 — narration
**Picture:** self-made map, Lake Erie to Buffalo, Erie County outlined, labels "LAKE ERIE" and "WESTERN NEW YORK" (the geography is on screen only). Then the ASOS card from T1 returns: "38°F · RAIN" at the pre-dawn rows, then "VIS 1/4 MI · 8:39 AM" lights up, then a red clock chip "DRIVING BAN · 9:30 AM". Source lines: "Buffalo airport ASOS, IEM archive"; "Erie County driving ban, WKBW". [VE] [RS] [PAY] [loop L0 closes]
> Before dawn that Friday, December twenty-third, if you were getting ready for work in Buffalo, it was raining, at about thirty-eight degrees. By eight thirty-nine in the morning, snow and wind had cut the visibility at the airport to a quarter of a mile. Erie County's driving ban took effect at nine thirty in the morning. That's fifty-one minutes after the visibility dropped to a quarter of a mile.

*register: 8/10*

### I1-S2 — narration
**Picture:** DVIDS 7572837 (827th Engineer Co clearing snow to recover an AMR ambulance, Buffalo, 26 Dec 2022, Eric Durr), public domain, held wide. Chips, one per sentence: "HUNDREDS STRANDED", then "GUSTS 69 MPH", then "37 STRAIGHT HOURS". Source lines: "Office of the Governor, 26 Dec 2022"; "NWS Buffalo Blizzard Warning, 22 Dec 2022"; "Buffalo airport ASOS, IEM archive"; "NYS DHSES, 4 Aug 2023". [VE] [RS] [Q]
> During the storm, hundreds of drivers ended up stranded, the governor's office said. The weather service's warning opened with the words blizzard conditions, before it gave any snow total. Out at the airport, the weather station logged gusts of sixty-nine miles an hour. And the state counted thirty-seven straight hours of blizzard-like conditions in Erie County. That's a day and a half with no letup if you were caught out in it. So who was out in that, and why couldn't help reach some of them?

*register: 8/10*

### I1-S3 — narration
**Picture:** a Guard soldier knocking at a front door during welfare checks: NY National Guard photo, DVIDS 7576030 (Buffalo, 30 Dec 2022, courtesy photo), public domain, portrait 1212x1804 cropped to 16:9. Then the self-made running tally graphic, full frame, building by date: 27 Dec "17 of 31", 28 Dec "17 of 37", 30 Dec "17 of 39", last reported "18 of 46" (no date, no "final"), the "outside" bar the longest at every step; Source line: "Erie County counts via NPR/KAXE, AP, WBFO, WIVB; last reported count, Poloncarz via WIVB". [VE] [RS] [PAY] [Q]
> As the National Guard and the road crews dug the city out, they started finding people. Outside, in the snow, was the biggest group in every county count I could find.

*register: 8/10*

### I1-S4 — narration
**Picture:** self-made name card, text only, "ANNDEL TAYLOR · 22", over a licensed night-snow street (Pexels or Pixabay, no car or person identifiable). No family photo unless licensed. Chip "~6 MIN FROM HOME". Source line: "Her family, via CBS News / CNN, 28 Dec 2022". [HUMAN] [VE] [Q]
> Anndel Taylor was twenty-two. Her family said she got stuck in her car that Friday, driving home from work, about six minutes from home. She called nine one one, but crews couldn't get to her car.

*register: 9/10*

### I1-S5 — narration
**Picture:** back to the NWS Buffalo forecast discussion card, now the earlier product: "very large and powerful storm system", 4:10 a.m. Sun 18 Dec 2022 (IEM archive, FXUS61 KBUF 180910). Chip "5 DAYS OUT". Slow fade toward the Act 1 blackout. [VE] [Q] [loop L1 open]
> And the forecasters were talking about it even earlier than that. By the Sunday before, five days out, the weather service in Buffalo was calling it a very large and powerful storm system. How does a forecast that early still end with so many people found outside, in the snow?

*register: 9/10*
