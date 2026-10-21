# ep-moore-1999 · edit_script.md (Bridge Creek-Moore tornado, Oklahoma, 3 May 1999)

Lane: documentary (`/storm-episode`). Angle: `angle.md` (owner lock 21 Oct 26, wording tightened by two fact passes).
Research: `research/fact-sheet.md` (primary sources, every line cited), `research/teardowns.md` (6 competitor videos +
viewer asks). Status: structure + act briefs by the orchestrator; hook, tail and intro written; acts 1 to 5 NOT
written yet (next round, one writer per act). Nothing here is locked (`references/script-scaling.md` "Section lock").

## Runtime and shape
- Target: about 20 min (proposal; the owner sets length per episode). 5 acts of 3 to 4.5 min plus hook/intro
  (~2 min) and close (~0.5 min) plus the CTA (24.0 s) and blackouts. `word_budget.py` sizes it once probe TTS exists.
- Architecture: Explanation-with-a-twist. Dominant question: **"The warning worked. So why did thirty-six people
  still lose their lives, and why did thirty-five people in one cellar all live?"**
- Script concept (Claim line, copied): The warning on May 3, 1999 worked, and the tornado still took 36 lives, so it
  came down to where people sheltered, not to the warning.
- Ruled out as the lead (every competitor leads with it): "strongest tornado ever / 300+ mph" (4 of 6 videos) and the
  overpass lesson (5 of 6). Both appear inside acts, never in the hook.
- Chapters in stakes order: the warning (why it was good) → the place it could not save (Bridge Creek) → the pivot
  (Tornado Emergency, and the TV advice not to copy) → the place it did save (Moore, 2,000+ in the path) → what changed.

## Hook sound (DESIGN.md "Cold-open hook contract": reasoned per episode)
This story IS a warning, so the civil-defence siren (`soundreality-civil-defense-siren-128262.mp3`) is earned here:
it fades up under Paul's line, ducks under the narrator, and stops dead on the cut to the cellar-door image. A NOAA
Weather Radio alert tone (1050 Hz, self-made with ffmpeg: zero claim risk) marks the 6:57 statement in act 3.

## Loop table
| id | planted | paid | line |
|---|---|---|---|
| E | H1 (hook) | A4 + A5 | warning worked, 36 still lost → where they were |
| L0 | T1 (tail) | A2 | the cellar door the tornado pulled open: did they live? (hook says yes; HOW is A2) |
| L1 | A1 end | A2 | the tornado formed at 6:26 near Amber, Bridge Creek next: what was standing there |
| L2 | A2 end | A3 | the warning everyone remembers had not been written yet when Bridge Creek was hit |
| L3 | A3 (TV station) | A3 end / A4 | "get out of its path": it worked that night, and why it was luck |
| cta-hinge | A3 last seg | A4 first seg | tease: Moore had more than two thousand people in the path → CTA → payoff "Five." |
| L4 | A4 (room left standing) | A5 | the one room that kept standing, and the room built to stand |

## Act briefs (orchestrator; one writer per act next round, each pasting the Angle block + its brief)

> **ACT 1 — Four forty-seven · ~3.5 min · ~470 words**
> **Job:** prove the warning was good, with numbers no competitor gives (65/18/31/13 min, 32-min average; US average then 10 to 15 min).
> **In / out:** a 4:47 p.m. clock on screen → 6:26 p.m. touchdown near Amber, Bridge Creek next (L1 plant).
> **Loops:** plants L1 · pays nothing new (the hook's promise is restated, not paid).
> **Rehooks:** the SPC high-risk upgrade 3:49 p.m.; the drill that simulated a violent tornado at OKC days before; 32 spotter classes; the water-bill safety insert in Moore; first tornado warning 4:47.
> **Tempo + emotion:** fast, procedural, low emotion; one human: the forecaster drill. Named researcher: none needed; agency on screen (NWS Norman).

> **ACT 2 — Bridge Creek · ~4 min · ~530 words**
> **Job:** the place the warning could not save, and why: twelve lost at Bridge Creek, most in mobile homes (Storm Data 9, Brooks list 10, B&D 11: say "most"); the Turner cellar, 35 people, door pulled off, all lived (SA p22, NOAA Report). Mobile homes 20+ times deadlier per unit (Brooks and Doswell 2002), anchors pulled out (FEMA 342). DOW wind about 302 mph over Bridge Creek at 6:54 as the science beat (Wurman 2007; never "strongest ever").
> **In / out:** 6:47 p.m., Bridge Creek → "the warning people remember was written two minutes after this" (L2 plant).
> **Loops:** pays L0, L1 · plants L2. Answers the viewer ask "not Bridge Creek as a footnote" (1,800 likes).
> **Rehooks:** the cellar door; the DOW reading; a slab swept clean in Willow Lake Addition; a dozen cars carried a quarter mile.
> **Tempo + emotion:** slow, the first emotional peak. One named person: Darrell Turner (NOAA Report). Clay-soil/basement question answered (FEMA: slabs, basements rare).

> **ACT 3 — Tornado Emergency · ~4 min · ~520 words**
> **Job:** the pivot. 6:57 p.m., the first Tornado Emergency, aimed at Moore and south OKC 25 min ahead; tone-alerted on NOAA Weather Radio; "credited with adding the emphasis that prompted numerous residents to action" (SA p15). TV helicopters, the street-name box. Then the small arc: one station urged people to get out of the path (SA p11); it worked that night only because of the long lead time and the tornado's size; do not copy it. Overpasses: two lost their lives there (SA Finding 10), told as people who left shelter, one line, not a lesson block.
> **In / out:** 6:57 alert tone → cta-hinge tease.
> **Loops:** pays L2 · plants L3, pays L3 · plants cta-hinge.
> **Rehooks:** the statement text on screen; the alert tone; the station quote; the I-44 overpass.
> **Tempo + emotion:** builds fast to the hinge. One Paul full-frame turning-point line: the "do not copy this" line.

> **CTA** (`config.yaml channel.cta`, 24.0 s) between A3's last segment and A4-S1, inside the 0.40 to 0.60 window
> (about 9:30 to 10:30 of a 20 min cut). Paul full-frame clip speaks the tease right before it.

> **ACT 4 — Moore · ~4.5 min · ~600 words**
> **Job:** the place the warning did save. Payoff in its first word: "Five." (Moore EM: 2,000+ in the path, 5 lost, 3 in well-built structures: NWS Norman overpass talk). Westmoore High awards night, assistant principal moves everyone to interior halls and bathrooms, gym roof gone, nobody lost (SA p23, FEMA). Millhouse family in the centre hallway (NOAA Report). Then the hard half: 19 of the 36 were in houses, some in the bathtub or under the stairs (Brooks list); FEMA's rooms left standing (bathroom 81 %, closet 75 %, kitchen 16 %); at F4/F5 "survivability is a matter of luck" without a real shelter (Doswell and Brooks 2002). Safe rooms built to FEMA's guide: no casualties in them (one near Bridge Creek's F5 edge).
> **In / out:** "Five." → the one room built to stand (L4 plant).
> **Loops:** pays cta-hinge, E (first half) · plants L4.
> **Tempo + emotion:** strongest human moment in the last third lives here (Westmoore or the youngest losses: a three-week-old and a four-month-old; the editor picks one, sourced, no names unless a source names them).

> **ACT 5 — What changed · ~3 min · ~400 words**
> **Job:** pays E and L4. Zero deaths aged 5 to 23 (Brooks and Doswell 2002: under 1 in 3,000 by chance; children taught tornado safety). Estimated 540 to 700 deaths without the warnings and preparedness of the day (B&D 2002; H. Brooks 1999: say "estimated"). The Tornado Emergency went from a one-night phrase to standard NWS wording [verify: formal date, preprint says 2014 with impact-based warnings]. FEMA safe rooms after 1999 [verify: Oklahoma safe-room rebate program, years, counts]. Close: fact + dated forward window, then the signature line (DESIGN.md "Signature closing footnote").
> **Loops:** pays E, L4. No new loop.
> **Tempo + emotion:** slow, ends higher than it started.

## Packaging (candidates only; the owner picks at the packaging gate)
`scripts/title_fre.py` scores, 21 Oct 26:
- "Moore 1999: The Warning Worked. The Homes Did Not." (109.8, 50 ch)
- "Moore 1999: 35 in One Cellar. All Lived." (109.0, 40 ch)
- "Moore 1999: An Hour of Warning Was Not Enough" (94.3, 45 ch: under 100, rewrite or drop)
Thumbnail school A (Name + Year documentary card): the Bridge Creek mud swath (William Lerner, NWS, SA photo, PD) with "35 IN ONE CELLAR" or "THE WARNING WORKED".

---

## H1 · Hook

### H1-S1 — narration
**Picture:** **Paul on camera:** full frame at 0:00, the one hook sentence, nothing added. Civil-defence siren fades up under him. Popfig "OKLAHOMA · MAY 3, 1999" inside the first second. Cut on "lives" to the A9 photo near Bridge Creek (Erin Maxwell, NWS, NWS Norman event page). Chip "65 MIN WARNING · 36 LIVES". [HOOK] [VE] [loop E open]
> You'd think an hour's warning saves everyone. The first county in this tornado's path got sixty-five minutes, and thirty-six along that path still lost their lives.

*register: 8/10*

### H1-S2 — narration
**Picture:** Bridge Creek mud swath and wooden projectiles, ground view (William Lerner, NWS HQ, Service Assessment photo). Push into a self-made cellar-door graphic (no public-domain photo of the cellar is in the inventory); the siren stops dead on the cut to it. Chip "35 IN ONE CELLAR · ALL LIVED". [RS] [VE] [HUMAN]
> In that same county, in the same little community where twelve people didn't survive, thirty-five people crammed into one storm cellar. The F5 pulled the cellar door open. All thirty-five lived.

*register: 8/10*

### H1-S3 — narration
**Picture:** The Service Assessment cover (NWS, "Oklahoma/Southern Kansas Tornado Outbreak of May 3, 1999"), pages turning, then the aerial of the path through Newcastle, Moore and Oklahoma City (John Jarboe, NWS, NSSL May 3 page). [PAY] [Q]
> I've read the weather service's own report on that night, every page, and the warning did its job. What decided who lived was where each person was when the tornado got there.

*register: 9/10*

## T1 · Hook tail

### T1-S1 — narration
**Picture:** NWS Norman outbreak map, zoom to Grady County; the self-made cellar-door graphic returns, door held open, hold on it. [Q] [loop L0 open]
> That cellar sat in an area of mostly mobile homes in Grady County, Oklahoma, right in the path of the F5. What those thirty-five people did before the wind got there is how every one of them came out alive.

*register: 8/10*

## I1 · Intro

### I1-S1 — narration
**Picture:** Self-made map from the NWS Norman damage-path KML: the track draws from Amber to Midwest City as the towns are named, clock chip "6:26 PM" to "7:48 PM". Then the KTLX radar image at 7:18 p.m. (Service Assessment photo). [VE] [Q]
> May third, 1999, central Oklahoma. At six twenty-six in the evening, a tornado touched down about two miles from Amber, a small town in Grady County. It ran about thirty-seven miles through Bridge Creek, Moore, south Oklahoma City and Del City. It finally came apart in Midwest City at about seven forty-eight. At its widest it was a mile across, and the survey teams rated it an F5. The weather service had been warning about this storm long before it ever touched the ground.

*register: 8/10*

### I1-S2 — narration
**Picture:** Self-made lead-time bars by county from Service Assessment p9 (Grady 65, McClain 18, Cleveland 31, Oklahoma 13 min), then one bar "32 MIN AVERAGE" beside a grey band "US AVERAGE THEN 10 TO 15 MIN" (Wurman et al. 2007 on the source line). Source line: "NWS Service Assessment, Aug 1999". [RS] [VE] [PAY] [Q]
> The first county in its path, Grady, got sixty-five minutes of warning. McClain County got eighteen minutes, Cleveland County, where Moore is, got thirty-one, and Oklahoma County got thirteen. Averaged across all four, the first warning came thirty-two minutes ahead. That's more than double what most of the country got back then, which was ten to fifteen minutes. And still, thirty-six people along that path lost their lives. That was the most from a single American tornado in twenty years, since Wichita Falls in 1979.

*register: 8/10*

### I1-S3 — narration
**Picture:** NSSL May 3 page damage photos (damage1 to damage6.jpg, NSSL), Bridge Creek first, then Moore and Del City; chips "BRIDGE CREEK · 12" then "THE OTHER 24". Source line: "Brooks, NSSL death list; NWS Storm Data". End on a self-made clock face reading 4:47 PM, siren-free room tone. [PAY] [Q] [loop: question carried into A1]
> Twelve of them were at Bridge Creek, out in Grady County, and most of those were in mobile homes. The other twenty-four were spread along the rest of the path, most of them inside houses. The number I keep coming back to is this one. Grady County's first tornado warning went out an hour and thirty-nine minutes before this tornado even touched down. How forecasters got that far ahead of a tornado that didn't exist yet starts with one warning. Four forty-seven.

*register: 9/10*
