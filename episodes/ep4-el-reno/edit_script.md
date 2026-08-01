# ep4 — El Reno 2013 — edit_script.md (DESIGN v2 — owner-approved 2026-08-01, sourcing authorized)

**Owner orders added at approval (2026-08-01):**
- **Clip breadth is a sourcing budget, not taste:** ep2 shipped 187 windows/28 min; ep3 audit proved the asset pool must FEED the cut rate. Target for 36 min: **~200+ picture windows → 120–150 distinct assets minimum.** Repeats allowed but never OBVIOUS (owner 2026-08-01): same asset/subject re-used only ≥3–4 min apart, different context/grade, never twice in one act stretch — the viewer must never feel "he threw this again." Subject-family dedup still applies within that window; a starved pool = the #1 boredom/leave signal.
- **Non-PD material stays hard-capped:** network/broadcast pulls 3–4s per cut, narrated over, credited, never the same cut twice. PD/stock/self-made = uncapped.
- **Key concept graphics get MULTIPLE VERSIONS:** for each big-concept graphic (width-scale, EF-vs-radar, the turn/trap geometry) author 2–3 visual approaches, snapshot all, pick the one that SHOWS the concept best (GRAPHICS CONTRACT §7: build the mechanism, never label a shape). Words carry little; the picture must land the idea alone.
- **Chaser footage stays BANNED unless licensed** (re-confirmed against the 2026-07-26 Oldshue ruling — strikes are channel-fatal; grading it down is disguise, prohibited). Emotional connect to the dead chasers = their publicly documented PHOTOS (memorial rules, ≤5s, attributed) + licensing option flagged to owner (see clip_hunt.md when ready).
- ep3's overall FEEL (graphics craft, archival texture) is the bar — keep its touch, restore the blackouts + panel exits per PR #8 contract.
- `render_radar.py` → parameterize (site/date/bbox/paths via args or config), reuse for KTLX/El Reno. De-hardcode, don't fork.

## Targets
- Runtime: **~36 min** (owner asked 35–40; recommend 36 — verified material carries it without filler; can stretch to 38 if owner wants the flood act longer).
- Narration budget: **36 × 0.9 × 158 ≈ 5,100 words** (probe-TTS 2 segments and recompute before locking, per LEARNINGS 2026-07-26 #7).
- Structure: sub-composition per act (native per-act re-renders).
- Formula: cold-open ≤15s anchor → thesis by ~75s → march → stats mid, **emotion banked at the END** → warm Warning Hour footnote. Micro-loops every 30–45s. No recap.
- **Blackout transition dips RESTORED (owner order 2026-08-01):** short dedicated dip-to-black sections (~1.5–3s, audio shutting down with the picture) at chapter turns and after major dramatic beats — placement marked ◼ in the act tables below. Never after every sentence; ep2 is the reference execution.
- **Graphics: minimal text (owner order, ep3 rework):** one idea per beat on screen, line-by-line builds, no dense multi-stat panels.

## Positioning (7-reference teardown, research/refs/)
Market: SkyWhisper "The Tornado That Shouldn't Exist" (887K views, 18 min) and Dark Horizon "The Tornado That Broke Every Rule" (16 min, ~147 wpm) are the serious competitors; TornadoTRX (31 min, 167 wpm — too fast, don't copy); Nat Geo "Inside The Mega Twister" (TV doc, raw chaser audio hook, thesis at 23s); two smaller channels (one is a called-out footage thief — cautionary tale) + one fandom Short.

**Table stakes we must cover:** record 2.6-mile width, EF3-vs-radar-winds controversy, TWISTEX deaths, the left turn + acceleration, Moore EF5 11 days earlier as context, rain-wrapped invisibility, highway gridlock.

**Our wedge (comment-mined gaps + primary-source facts NO competitor has):**
1. **Richard Henderson** — the fourth chaser death; repeatedly demanded in Dark Horizon's comments (11 likes), covered by nobody. We tell his story (texted a photo of the tornado at 6:05 PM; ten minutes later his phone went dead).
2. **Actually RESOLVE the EF3-vs-EF5 controversy** — every competitor dangles it; none explains the Damage-Indicator method. We have the Marshall et al. survey paper: radar winds ran a quantified **10–30% higher** than damage-implied winds, and "the highest velocities occurred in areas notably absent of DIs." The scale rates damage, not wind, by design.
3. **"Chaser traffic was a non-factor"** — the federal Service Assessment quotes Dan Robinson (the chaser directly ahead of TWISTEX) refuting the chaser-gridlock-killed-them narrative most videos imply.
4. **TWISTEX was not on a NOAA-funded mission that day** (SA, Section 3.9) — materially under-reported.
5. **The Mike Morgan "drive south" story is bigger than one man:** NWS Norman's OWN 1:00 PM tweet said "if you choose to flee in your car…" hours before the tornado formed. Institutional messaging failure, not a lone bad call. Comments on TornadoTRX explicitly ask for this interrogation.
6. **The forgotten 13:** the overnight flash flood killed more people than the tornado — deadliest flood in OKC history; some victims died sheltering in drainage ditches FROM the tornado. No reference video covers it as an act.
7. **Peer-reviewed evacuation record:** 2022 AMS study — largest tornado evacuation of six US metros studied 2011–2018, driven partly by Moore trauma 11 days prior (the Rita-after-Katrina analogy).
8. Anticyclonic + satellite tornado structure (radar-documented, rare) for the meteorology-explainer beat.

**Anti-patterns (teardown-verified):**
- Dark Horizon banks the TWISTEX deaths at the ~55–60% mark — its own comments prove that's the most memorable beat. We keep emotion at the END (our locked formula) and it will land harder.
- herzacVgvnQ's "Worst in US History" title got fact-checked to death in comments — our superlative anchors to a checkable metric: **widest** (Marshall et al.: "a new record for tornado width").
- Audio-authenticity scandal (Dark Horizon comments dispute whether the TWISTEX "final audio" is real) — we never use unverifiable "final moments" audio; anything recreated gets an on-screen label.
- Every competitor's visual spine is unlicensed chaser footage — structurally impossible for them to avoid claims. Our claim-proof stack is the differentiator, not a handicap.

## FACT LEDGER (verified — citations in research/facts.md; UNVERIFIED items never ship)
- Formed ~6:03 PM CDT, ~10 km west of El Reno. Warning 6:08 PM (+6:28, 6:57 follow-ons).
- Early motion SE at 20–25 mph, EF0/EF1 rural damage. ~6:09 PM: sharp LEFT turn + acceleration "from approximately 35 mph to more than 50 mph" (SA direct quote) — the trap.
- **Peak width 2.6 mi (4.2 km)** ~6:19 PM CDT south of El Reno — record, surpassing Hallam NE 2004 (Marshall et al., RaXPol 30 m/s isodop). Path 16.3 mi.
- **Rating EF3.** RaXPol instantaneous winds >130 m/s (~291 mph) near ground, >120 m/s (~268 mph) in subvortices; "surveyors could not find damage that would support a rating higher than EF3." Radar 10–30% above EF-implied winds. **"296 mph" exact figure = UNVERIFIED — say "roughly two hundred ninety" / "well over two hundred fifty," cite RaXPol.**
- Multi-vortex; satellite tornado into NW flank; genuine anticyclonic tornado ESE of main (Marshall et al. Fig. 28).
- **8 tornado deaths, ALL in vehicles**, 4 storm chasing: Tim Samaras 55 (found belted in the Cobalt), Paul Samaras 24, Carl Young 45 (both ejected; one found ~½ mi away), Richard Henderson (age "35" UNVERIFIED — don't state). Also F26 + 17-day-old infant parked along I-40 (mother and child).
- SA: "None of the individuals were functioning under a NOAA-sponsored research project at the time." SA: "It does not appear that traffic was a factor in the deaths of the TWISTEX storm chasers" + Dan Robinson verbatim: "chaser traffic was a non-factor at our location."
- **13 flash-flood deaths** overnight (12 in OKC) — deadliest flood event ever for OKC; deadliest in WFO Norman area since 1934 Hammon (17). Some victims in drainage ditches.
- NWS Norman 1:00 PM tweet: "If you choose to flee in your car, plan for and anticipate traffic jams and blocked roads, hail, heavy rain and flooding." Harold Brooks (NOAA) called blanket get-underground messaging "irresponsible at best." SA Finding 6: media focused on tornadoes, not flooding.
- 2022 AMS WCAS study: largest evacuation of six metros studied 2011–18; Moore EF5 (May 20, 11 days prior) primed the panic; SA draws the Rita-after-Katrina analogy.
- DI density peaked 69/sq mi at a manufactured-home cluster just south of I-40 vs <10/sq mi elsewhere.
- **DROPPED/FLAGGED:** "296 mph" exact; "~175 mph subvortex translation"; Henderson age 35; Guatemalan-family attribution to any named victim; ANY fact appearing only in competitor videos (they plagiarize each other — LEARNINGS ep3 #1).

---

## Act structure (sub-compositions; ◼ = blackout transition dip)

### A0 — COLD OPEN + THESIS (0:00–1:40 · ~175 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a0-s1 | insert/graphic hybrid | **Hook contract applied.** Black. NOAA Weather Radio / EAS tornado-warning audio (PD, claim-free) is the sonic anchor — intelligible warning voice by ~2.5s. Date/place card "EL RENO, OKLAHOMA — MAY 31, 2013" inside first second. Our KTLX radar re-plot blooms on beat 2 — the purple debris core swelling. Cut ON audio events. | Radar re-plot + title card; siren/NWR spine builds |
| a0-s2 | narration (~85w) | Present tense: the widest tornado ever measured is on the ground — and almost nobody in its path can see it. It is wrapped in rain. It looks like a wall of water. Inside it, winds near three hundred miles per hour. | AI wedge still (rain-wrapped wall, owner-gen) + NWS storm photos (PD) |
| a0-s3 | narration (~90w) | **Thesis @ ~70s:** it will hold the record for size. It will be rated EF3. And it will do something no tornado had ever done — kill the most careful storm chasers in the world. Foreshadow: "the men who understood this storm best were the ones it caught." | Title card: THE WIDEST TORNADO EVER RECORDED, match-cut on "record" |
| ◼ | blackout dip | ~2.5s void, audio dies with picture (hook punctuation per contract) | — |

### A1 — ELEVEN DAYS EARLIER: MOORE (1:40–5:30 · ~560 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a1-s1 | narration | May 20: Moore EF5 — Plaza Towers, Briarwood, 24 dead. The state is an open wound. This is WHY May 31 unfolds the way it does. | DVIDS National Guard Moore footage (PD, labeled MOORE — MAY 20 on-screen), FEMA stills |
| a1-s2 | narration | Eleven days of dread; forecasters watching Friday May 31 with a loaded atmosphere. SPC outlook build. | Real SPC outlook graphics (PD), calm-before b-roll (stock) |
| a1-s3 | graphic+VO | **Meteorology explainer #1 (minimal text):** the setup — moisture, shear, a dryline west of OKC; why late-May Oklahoma is the world's tornado engine. One label per beat. | Animated ingredient map, line-by-line reveals |
| a1-s4 | hold 3–5s | Breath: darkening Friday-evening sky. | Stock timelapse, ambience up |
| ◼ | blackout dip | act turn (~2s) | — |

### A2 — THE STORM (5:30–11:00 · ~800 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a2-s1 | narration | 6:03 PM: touchdown west of El Reno. Warning at 6:08 — five minutes. Rural EF0/EF1 first; slow, southeast, "well-behaved." Hundreds of chasers on the road grid (it's the most-observed tornado in history AND the most lethal to its observers — tension planted). | Our KTLX re-plot march (timestamps mapped to narration — UTC/local rule), NWS supercell photos (PD) |
| a2-s2 | graphic+VO | **The growth:** width counter — half a mile… one mile… 2.6 miles at 6:19 PM. Counter rolls fast, slows dramatically into 2.6 (numbers rule). Hallam 2004 comparison AFTER landing. Scale translation: wider than Manhattan; you could stand at one edge and not see the other even in clear air. | Width-scale graphic over map, single figure on screen at a time |
| a2-s3 | narration | Rain-wrap: why nobody could see it. Multi-vortex: the monster carries smaller, faster monsters inside it — and a satellite tornado, and a rare anticyclonic twin. | AI stills (owner-gen: rain-wrapped wall, subvortex fingers), NOAA Tech Memo radar figures (PD) |
| a2-s4 | insert | Short verified broadcast pull IF official-channel source clears (see BLOCKED note) — else NWSNorman video pull (PD). OWNER GATE. | — |
| ◼ | blackout dip | after the 2.6-mile landing beat (~2s) | — |

### A3 — THE TURN (11:00–16:30 · ~800 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a3-s1 | narration | 6:09 PM: the left turn. SA quote: forward speed 35 → 50+ mph, sharp left, intense inflow — "made driving away from the tornado difficult." Every escape calculation on Highway 81 is suddenly wrong. | Map graphic: path elbow drawn ON the spoken word; chaser-position schematic (our graphic, minimal labels) |
| a3-s2 | narration | Introduce TWISTEX properly (mid-video hero intro — teardown-validated): who Tim Samaras was — the engineer who built probes to survive tornado cores, National Geographic grants, the man famous for NOT taking risks. Paul behind the camera. Carl driving. NOT NOAA-funded that day (net-info-gain, stated plainly). | Public/archival photos of Samaras (real, memorial-dwell ≤5s rule), probe diagrams |
| a3-s3 | narration | The geometry of the trap: a storm wider than their escape margin, moving faster than their road, invisible in rain. Dan Robinson directly ahead of them (his SA account as ON-SCREEN QUOTED TEXT with attribution — his footage stays out). "Chaser traffic was a non-factor." | Map schematic of Reuter Rd/Hwy 81; SA page pull (PD document) |
| a3-s4 | hold 4–8s | The Cobalt beat lands — restraint, no dramatization. We state the record: found belted in, doing everything right. | NWS crash-scene photo (PD, static historical document, brief) → cut to open sky |
| ◼ | blackout dip | ~3s full shutdown after the deaths beat — the episode's heaviest dip | — |

### A4 — THE EXODUS (16:30–22:00 · ~800 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a4-s1 | narration | Meanwhile in OKC: Friday rush hour, 11 days after Moore. "Drive south" goes out on air. Tens of thousands get in cars. I-35/I-40/I-44 lock solid — under a tornado-warned sky. | Broadcast pull IF cleared (OWNER GATE) / stock gridlock + our map graphic of interstates clogging (animated, minimal text) |
| a4-s2 | narration | **Net-info-gain:** the fairness beat — NWS Norman's own 1:00 PM tweet said "if you choose to flee in your car…". Harold Brooks quote. The system, not one man, told Oklahoma to run. SA Finding 6. | Real tweet rendered as document graphic, quote cards (one line at a time) |
| a4-s3 | graphic+VO | 2022 AMS study: largest tornado evacuation of six metros studied 2011–2018. The Rita-after-Katrina analogy: trauma drives flight. | Single-stat card, then map pulse |
| a4-s4 | narration | The near-miss: the EF3-strength core crossed I-40 — DI density 69/sq mi at a manufactured-home cluster by the interstate vs under 10 elsewhere. A mother and her 17-day-old baby, parked along I-40, were among the eight. If the tornado had held EF-peak strength into the jam… (restraint: state, don't dramatize). | Aerial survey imagery (NOAA PD), map |
| ◼ | blackout dip | act turn (~2s) | — |

### A5 — THE SECOND DISASTER (22:00–26:30 · ~650 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a5-s1 | narration | The storm's second act nobody remembers: training rain over OKC that night. People sheltering from tornadoes in ditches and underpasses — the lowest ground in the city — as flash flood water rises. | Night rain/flood stock + AI stills (owner-gen: underpass at night, rising water — no people) |
| a5-s2 | narration | 13 dead — more than the tornado itself. Deadliest flood in OKC history; deadliest in the region since 1934. The media covered tornadoes; the flood warning got lost (SA Finding 6 callback). | Rainfall map (NWS PD), counter graphic (13 vs 8 — one comparison, minimal) |
| a5-s3 | hold 3–6s | Rain on empty street, ambience only. | Stock |
| ◼ | blackout dip | act turn (~2s) | — |

### A6 — WHY EF3? (26:30–31:00 · ~650 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a6-s1 | narration | The rating fight the comments always demand — resolved, not dangled. RaXPol measured ~291 mph near the ground. Official rating: EF3. Both are true. | RaXPol/NOAA radar figures (PD) |
| a6-s2 | graphic+VO | **Meteorology explainer #2:** the EF scale rates DAMAGE, not wind. Marshall et al.: "the highest velocities occurred in areas notably absent of DIs" — the violent core crossed open farmland; nothing there to break. Radar ran 10–30% above damage-implied winds. One concept per screen. | DI method diagram built line-by-line; survey-map overlay |
| a6-s3 | narration | What changed after: chase-community reckoning, mobile-radar respect, the NWSNorman "Lessons" retrospective. (Pull from NWSNorman video — PD insert candidate, OWNER GATE.) | NWSNorman video pull |
| ◼ | blackout dip | before the reckoning (~2.5s) | — |

### A7 — THE RECKONING (emotion banked HERE) (31:00–35:00 · ~580 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a7-s1 | narration | Richard Henderson — the story nobody tells. A truck driver who drove out from his home to watch. 6:05 PM: texts a friend a photo of the tornado. Ten minutes later: debris hitting the truck, then the line goes dead. Two sons. | His publicly documented photo if available (memorial rules, ≤5s); else symbolic: empty rural road, phone-photo framing (AI/stock) |
| a7-s2 | narration | TWISTEX legacy: Tim's probes and what his data still teaches; the community he built. The bitter symmetry — the man who preached distance, caught by the one storm whose size erased distance. Verified quotes only, attributed on screen. | Real photos (memorial-dwell rule), probe-data visual |
| a7-s3 | narration | The eight, named categories, all in vehicles — and the thirteen. What El Reno actually proved: you cannot outdrive what you cannot see. Shelter beats speed. | Slow survey-photo sequence (PD), names/figures one at a time |
| ◼ | blackout dip | ~3s before signature | — |

### A8 — WARNING HOUR FOOTNOTE (35:00–35:40 · ~65 words)
Canonical warm preparedness cadence, tuned to this episode: know your shelter BEFORE you're in a car → "…This was The Warning Hour." Episode number on card ("Episode 4 — El Reno 2013"). Match-cut, no dwell, no recap.

---

## Transition plan (restored channel signature)
7 blackout dips total (marked ◼): hook void, A1→A2, post-2.6-mile beat, post-TWISTEX (heaviest, ~3s), A4→A5, A5→A6 (pre-reckoning ~2.5s), pre-signature. Each: picture to #000 AND audio bed/SFX fade to silence together; narration never talks over a dip. ~1.5–3s each — never longer. Hard cuts everywhere else (teardowns confirm competitors are hard-cut-only; the dips are OUR signature, used sparingly = meaning-bearing).

## Inserts requiring owner confirmation (each gated individually, frames + transcript + source)
1. Broadcast pulls (A2-s4, A4-s1) — **currently BLOCKED**: all found KFOR/KWTV uploads are third-party re-uploads (provenance-laundering risk); usable only if station-official uploads are found and frame-matched. Fallback: NWSNorman video + graphics carry those beats.
2. NWSNorman "Lessons" video pulls (A6-s3, optionally A2-s4) — PD, but owner previews cuts.
3. NWR/EAS warning audio for the cold open — sourced from NOAA (PD), owner ear-checks the hook.

## Footage plan (claim-proof stack)
- **Spine (PD):** NWS Norman event page (damage survey photos, storm photos, path/warning/rainfall maps, KMZ tracks); NOAA Tech Memos (aerial survey + multi-vortex figures); SPC outlooks; NWSNorman YouTube video; DVIDS/FEMA Moore material (labeled MOORE on-screen); FEMA DR-4117 photo library (Andrea Booher El Reno set — pull from fema.gov, not Alamy).
- **Self-made:** KTLX NEXRAD re-plots — all three hourly tars confirmed on the GCS mirror (22:00–00:59 UTC). **`C:/nexrad-t/render_radar.py` is ep1/KSGF-hardcoded — needs an El Reno/KTLX adaptation before sourcing week.** Radar is unusually load-bearing this episode: the record width was radar-measured, so our re-plots ARE the story, not filler.
- **Stock:** Pexels/Pixabay for connective tissue only (rehook cadence: a REAL clip every 45–60s; this episode's "real" = PD govt footage/photos + radar).
- **BANNED, zero exceptions:** Dan Robinson dashcam, TWISTEX tapes (incl. the archive.org "Tim Samaras" uploads SkyWhisper leans on — hosting ≠ license), Reed Timmer, Basehunters, Piotrowski, RaXPol/DOW raw video (university-owned, not PD — their DATA via NOAA figures is fine), all third-party "KFOR" re-uploads, anything from the reference videos themselves.

## AI images for OWNER to generate (the gap list — flagged at script time, per new rule)
No claim-safe footage exists of the tornado itself on the ground (all chaser-owned). Needed:
1. **Rain-wrapped wedge wall** — a 2.6-mile black-green wall of rain across flat Oklahoma farmland, evening light (hook + A2). 2–3 variants.
2. **Multi-vortex fingers** — subvortices snaking under a vast low cloud base (A2-s3).
3. **Night underpass / drainage ditch, rising black water, heavy rain, headlights** — no people (A5).
4. **Empty rural road, storm light, telephone poles** — Henderson beat, symbolic (A7).
5. Optional: day-after newspaper front-page MOCKUP (or owner buys a newspapers.com day-pass for the real June 1 Oklahoman). Owner call.
6. Optional: white sedan on a wet section-line road, storm on horizon, distant/rear view, no people, no likeness (A3 restraint beat) — owner judgment on taste; the NWS crash photo (PD) may carry the beat alone.
No real-person likenesses in ANY generated image (DESIGN.md rule).

## Packaging (draft — final at publish)
- Title: **"The Widest Tornado Ever Recorded — El Reno 2013"** (superlative anchored to a checkable metric; herzacVgvnQ's comments prove unanchored superlatives get torched). Alt: "The Tornado That Killed the Experts — El Reno 2013".
- Thumbnail: cinematic AI rain-wrapped wedge + bold "EL RENO 2013" (beats all 7 refs — none ships a designed thumbnail).
- Description: no-spoiler, courtesy credits (NOAA/NWS/FEMA/DVIDS), Education metadata per CLAUDE.md.

## Word budget check
**Probe-TTS measured 2026-08-01 (probe-a0: 170.7 wpm, probe-a3: 161.8 wpm → plan at ~166 delivered).**
Budget: 36 × 0.9 × 166 ≈ **5,375 words**. Act split: A0 185 · A1 590 · A2 845 · A3 845 · A4 845 · A5 690 · A6 690 · A7 615 · A8 70 ≈ 5,375.
Sourcing: PD + stock ONLY, nothing paid (owner 2026-08-01). AI gap-fills self-generated via DeAPI keys, used sparingly — real clips carry the episode.

---

# SCRIPT (TTS-safe prose — resolved fact ledger only; segments parsed by scripts/tts_episode.py)

### A0-S2 — narration
> The widest tornado ever measured on this planet is on the ground right now, and almost nobody in its path can see it. It is wrapped in curtains of rain, and from the highway it looks like nothing more than a gray wall of water sliding across the fields. But inside that wall, instruments are recording winds close to three hundred miles per hour. It is growing faster than anyone has ever seen a tornado grow, and it is about to change direction without warning.

### A0-S3 — narration
> By the time the sun sets on the thirty first of May, twenty thirteen, this storm will hold a record no tornado has ever held. Two point six miles wide, edge to edge. And yet the official rating in the record books says EF three, a number that still starts arguments today. Because this tornado did something no tornado had ever done before. It killed the most careful storm chasers in the world. The men who understood this storm best were the ones it caught. This is the story of El Reno.

### A1-S1 — narration
> To understand what happened on that Friday evening, you have to go back eleven days. On the twentieth of May, an EF five tornado carved through the suburbs of Moore, Oklahoma, on the south side of Oklahoma City. It stayed on the ground for seventeen miles, and its winds passed two hundred miles per hour. It struck two elementary schools with children inside. Twenty four people died, including seven third graders at Plaza Towers Elementary. The state had barely finished counting its dead when the forecasts began pointing at the very same metro area again. So when Oklahomans looked at the sky on May thirty first, they were not looking with ordinary caution. They were looking with fresh grief, and that grief was about to shape every decision of the evening. Remember that, because it explains what a million people did next.

### A1-S1b — narration
> And Moore was not even the whole story of that May. The twentieth was the second major severe weather outbreak of the month, and the thirty first would be the third. For nearly two weeks, Oklahomans had lived inside a loop of watches, warnings, sirens, and funerals. Schools had drilled. Families had rehearsed. Hardware stores had sold out of shelter supplies. By that last Friday of the month, central Oklahoma was not a population that needed convincing that tornadoes kill. It was a population primed to act, instantly, on the next warning it heard. In most disasters, that kind of readiness saves lives. On this particular evening, it was about to do something stranger. Because what a frightened city does with a warning depends entirely on what it has been told to do. And the instructions Oklahoma City had absorbed that month pointed in a direction no textbook recommends.

### A1-S2 — narration
> Friday morning, the Storm Prediction Center in Norman drew a risk area over central Oklahoma and did not hedge. Moisture was streaming north from the Gulf, thick and unstable, the kind of air that feels like a wet blanket by mid afternoon. A dryline, the sharp boundary where desert air from the west meets that Gulf moisture, was set up just west of the metro. And overhead, the winds turned and strengthened with height, ready to spin anything that grew tall enough. Forecasters in Norman had watched this same loading of the dice eleven days earlier. Every ingredient said the same thing. If a storm formed on that dryline in the early evening, it would rotate, and it would be violent. By late afternoon, towers of cloud were already boiling up west of El Reno, and hundreds of storm chasers were already parked on the section roads, waiting.

### A1-S3 — graphic with VO
> Here is why this corner of the country builds monsters. Warm, moist air near the ground is fuel. Dry, hot air sliding over it from the southwest acts like a lid on a pot, letting the fuel build instead of burning off in small showers. When the lid finally breaks, everything goes up at once, one violent updraft instead of twenty harmless ones. And if the winds above turn with height, the whole rising column begins to rotate. A rotating thunderstorm is called a supercell. And a supercell over open Oklahoma farmland, in late May, at six in the evening, is the single most dangerous storm structure on Earth.

### A2-S1 — narration
> At three minutes past six in the evening, a funnel touched down in the fields west of El Reno. Five minutes later, at six oh eight, the tornado warning went out. At first, the storm behaved exactly the way the textbooks said it would. It moved southeast at twenty to twenty five miles per hour, chewing through empty farmland, damaging a few rural homes at EF zero and EF one strength. Slow, visible from a distance, and predictable. Which is why, within minutes, it became one of the most observed tornadoes in history. Research radars, television helicopters, and hundreds of chase vehicles were all watching the same storm at the same time. No tornado had ever been studied this closely while it happened. And no tornado has ever punished its observers the way this one was about to.

### A2-S1b — narration
> Among the watchers were two machines that make this story possible. Parked on the road grid were mobile research radars, radar dishes mounted on trucks. They are built to drive up close to a storm and scan it every few seconds instead of every few minutes. One of them, a rapid scan unit from the University of Oklahoma called RaXPol, rolled into position east of the developing tornado and locked on. The Doppler on Wheels trucks were out there too. Fixed radars, the big domes that feed the warnings on your television, sit tens of miles away and see a storm in slices, high above the ground. A truck parked two miles out sees the storm's actual ground floor, where people live and die, and it sees it almost continuously. Everything you are about to hear about this tornado's true size and true winds exists because those trucks were pointed at it at the right moment. Hold onto that thought, because at the end of this story, the radar and the record books are going to tell two different truths about the same storm.

### A2-S2 — graphic with VO
> Watch what happens in the sixteen minutes after touchdown. At six oh three, the tornado is a few hundred yards across. Ordinary. Then the storm begins pulling in air faster than anyone watching has ever seen. Half a mile wide. Then a full mile. Then two. At six nineteen in the evening, south of El Reno, the circulation reaches two point six miles across. Edge to edge, that is wider than the island of Manhattan. If you stood at one edge, the far side would be beyond the horizon of most people's eyesight, even in clear air. The old record, set in Nebraska nine years earlier, was gone. No tornado in recorded history had ever been this wide. And here is the part that mattered most to the people underneath it. A tornado that wide does not look like a tornado at all.

### A2-S3 — narration
> It looked like rain. The circulation was buried inside what chasers call a rain wrapped core, sheets of water pulled around the vortex like a curtain. From the roads south and east, there was no funnel to see, just a dark gray wall a few miles wide, and walls of water do not look dangerous. Inside that curtain, the radar could see what eyes could not. This was not one vortex. It was a family of them, smaller tornadoes inside the main circulation, orbiting it like moons, each one packing winds far stronger than the parent storm. The radar even caught a separate satellite tornado circling into its northwest flank, and, on the far side, something genuinely rare. A second tornado spinning the opposite direction, clockwise, born from the same storm. The atmosphere was doing things that evening that scientists are still writing papers about. And then, at nine minutes past six, everything the people watching it knew stopped being true.

### A2-S3c — graphic with VO
> One of those radar discoveries deserves thirty seconds of your attention, because it may be the strangest thing this storm did. Nearly every tornado in the northern hemisphere spins the same way, counterclockwise, for the same reason hurricanes do. The rotation of the Earth itself loads the dice. On this evening, the radar watched the great counterclockwise circulation south of El Reno, and then found, on its far side, a second tornado turning the opposite way. Clockwise. An anticyclonic tornado, one of the rarest events in severe weather, spinning mirror backwards a few miles from the widest tornado ever measured. The same storm was running both directions at once. Scientists explain it as a kind of atmospheric gearing. Spin one enormous wheel hard enough, and the air along its flank can be rolled backwards, like a small gear driven by a large one. It had almost never been documented this clearly. On any other day, that clockwise tornado would have been the headline. On this day, it was a footnote.

### A2-S3b — narration
> The warning system, to its credit, kept pace on paper. The first tornado warning at six oh eight was followed by stronger ones at six twenty eight and six fifty seven. The radar was showing the circulation multiply into that family of vortices. The information existed, and it was moving. But a warning describes a storm as it is, and this storm was rewriting itself faster than any bulletin could travel. A driver who heard the six oh eight warning pictured a tornado a few hundred yards wide, moving southeast, away from them, at highway speed minus half. Ten minutes later that picture was wrong in every detail that mattered. Wrong size, wrong direction, wrong speed. Out on the wet section roads west of Highway Eighty One, the gap between the storm people had pictured and the storm that actually existed was about to close on some of the most experienced observers alive.

### A3-S1 — narration
> At nine minutes past six, the tornado did something that rewrote every escape plan on Highway Eighty One. It turned hard to the left, and as it turned, it accelerated. The federal report is precise about this moment. Forward speed climbed from roughly thirty five miles per hour to more than fifty, and the inflow winds made driving away from it difficult. Every chaser on that road grid had built their position around a storm moving southeast at twenty five miles per hour. That storm no longer existed. In its place was something wider than their escape margin, faster than their vehicles on wet section roads, and completely hidden in rain. The mathematics of every escape route on that grid had just been rewritten, and nobody's map had updated yet. For most of the chasers, the mistake cost them a story they would tell for the rest of their lives. For four of them, it cost everything.

### A3-S1b — narration
> To understand why a faster, wider storm was a death sentence rather than an inconvenience, you have to picture the roads. Western Canadian County is a grid of section roads, gravel and dirt lines drawn a mile apart across the farmland, and by evening the rain had turned the dirt ones to grease. The paved escape routes were few, and Highway Eighty One, running north to south through the storm's new path, was the spine most of them fed into. A chase position that assumed a slow storm left you with options, turn south, drop east, wait it out. A storm suddenly two and a half miles wide, moving fifty miles per hour, swallowed those options whole. The math is brutal and simple. If the edge of the circulation is a mile away and expanding toward you faster than your car can safely move on a wet gravel road, the road you are on has already decided your next few minutes. Dozens of chasers that evening escaped by margins they still talk about. Vehicles were damaged, windows blown out, cars shoved off roads. The evening produced more close calls among experienced chasers than any storm before or since.

### A3-S2 — narration
> Tim Samaras was not a thrill seeker. He was an engineer, and in the storm chasing world he was famous for the opposite of recklessness. He built instrument probes designed to survive a direct hit from a tornado core, placed them in the storm's path, and got out. His pressure measurements inside a tornado still stand among the most valuable ever taken. National Geographic had funded his field work for years. Colleagues described him as the careful one, the man who preached margins and turned back when the margins closed. That evening his team, called TWISTEX, was three people. Tim, fifty five years old. His son Paul, twenty four, behind the camera. And meteorologist Carl Young, forty five, driving. Here is a detail almost nobody mentions. The federal review of that day records that none of the people chasing were operating under a government research project at that moment. The safety structure of an official mission was not there. It was three men, a small white Chevrolet Cobalt, and a storm about to break every rule they had built their careers on.

### A3-S3 — narration
> Just ahead of them on the same road was another veteran chaser, Dan Robinson. His account, quoted in the federal report, matters, because it kills a myth. People assume the chasers died because of chaser traffic, hundreds of cars clogging the escape roads. Robinson is explicit. At his position, other than the TWISTEX car behind him and one parked pickup, the road was empty. Chaser traffic was a non factor, his words. The report reaches the same conclusion. What caught them was the storm itself. The circulation widened so fast, and turned so sharply, that a road which had been outside the tornado became inside it in under a minute. Robinson's car took the edge and survived. The Cobalt, seconds behind, took a sub vortex, one of those embedded cores the radar had been tracking, with winds measured at more than two hundred and fifty miles per hour. Tim Samaras was found still in the car, his seat belt fastened. He had done everything right, the way he always did. Paul and Carl were carried from the vehicle by the wind. The careful one, and the storm that finally out ran care.

### A3-S3b — narration
> The Cobalt was not the only vehicle the storm caught. Minutes earlier, a Weather Channel chase vehicle carrying meteorologist Mike Bettes and his crew was snatched off the road by the circulation's edge and thrown, rolling across a field before landing crushed in the grass. Everyone inside survived, the driver with serious injuries, and the crew's own cameras recorded the vehicle's tumbling view of the sky. That footage went around the world within days, because it captured something no viewer had seen before. Professionals, in a reinforced chase vehicle, on live assignment, completely overpowered. Between the Bettes crash, the TWISTEX deaths, and the dozens of battered vehicles limping off the grid that evening, the message of El Reno was already written before the sun went down. This storm had hunted the people who knew storms best, and it had caught them.

### A4-S1 — narration
> While that was happening in the fields, something very different was going wrong twenty five miles east, in Oklahoma City. It was a little after six on a Friday evening. Rush hour. And the city was eleven days removed from watching an EF five bury schoolchildren in Moore. As the warnings spread, television coverage told people in the storm's path to get south, to get out of its way. And this time, people did not shelter. They ran. Tens of thousands of them got into cars, all at once, onto Interstate thirty five, Interstate forty, Interstate forty four. Within the hour, the highways south of the city had locked into a standstill, bumper to bumper for miles, under a sky with a tornado warned supercell bearing down on it. A parking lot of families, sitting in the open, in the path of a storm that had just killed four professional storm chasers. It is remembered as one of the most dangerous traffic jams in American history.

### A4-S2 — narration
> The television advice that evening has a name attached to it, a local chief meteorologist who twice told viewers without underground shelter to drive south. He was blamed for the gridlock for years afterward. But the record tells a messier story. At one o'clock that afternoon, hours before the tornado formed, the National Weather Service's own Norman office posted safety guidance that began, if you choose to flee in your car, plan for traffic jams, hail, heavy rain and flooding. The government's own messaging that day allowed for fleeing by car. Meanwhile a senior government scientist argued the opposite, that telling people they would not survive above ground was dangerous. Read that again. In the same city, on the same afternoon, the official guidance pointed in two directions at once. The federal review of the event does not pin the exodus on one broadcaster. It finds that the message system itself, government and media together, had never agreed on what a terrified city should actually do. A million people filled that silence with the Moore tornado, and chose their cars.

### A4-S3 — graphic with VO
> Years later, researchers studied vehicle movement across six American metro areas hit by tornado warnings, and they found nothing anywhere that compared to this evening. It stands as the largest tornado evacuation ever measured in an American city. Their conclusion echoes an older disaster. After Hurricane Katrina drowned New Orleans, the next storm sent Houston fleeing, and the evacuation itself killed dozens. Fear from the last disaster drives behavior in the next one. Moore was eleven days old. Oklahoma City ran.

### A4-S4 — narration
> Now put the two halves of this evening together, because they nearly met. The tornado, still enormous, was tracking east toward the exact interstates those families were parked on. It crossed Interstate forty near Banner Road as it weakened. Even then, it found the one cluster of buildings on its path, a group of manufactured homes just south of the interstate, and the damage survey there recorded the densest destruction of the entire track. Among the eight people killed by this tornado, every single one was in a vehicle. A father driving home. A young woman and her infant daughter, seventeen days old, parked along Interstate forty. The storm chasers on the section roads. Eight lives, all of them on wheels. And the terrible truth of the evening is this. If the tornado had held its record size and strength for another twenty minutes, it would have arrived on a jammed interstate holding thousands of stationary cars. Oklahoma came within a margin of minutes of the deadliest tornado disaster in its history. What actually happened next killed more people than the tornado did, and almost nobody outside Oklahoma remembers it.

### A5-S1 — narration
> The supercell that built the widest tornado ever measured did not stop working when the funnel lifted. Storms kept forming and passing over the same ground, hour after hour into the night, a pattern meteorologists call training, like railcars rolling over one crossing, and it wrung the Gulf's moisture out over the city at rates the drains were never built for. And here the evening's tragedies began to feed each other. All over Oklahoma City, people had taken shelter from the tornado the only way they could. Some had climbed into storm drains and drainage ditches, the lowest ground available, exactly where you hide from wind, and exactly where you die in water. Others were still out on the flooded roads, in the cars they had fled in. As the tornado threat faded from the news coverage, the water was already rising in the dark.

### A5-S2 — narration
> Thirteen people drowned that night, twelve of them in Oklahoma City. More than the tornado killed. It remains the deadliest flood event in the city's history, and the deadliest flash flood anywhere in that forecast region since nineteen thirty four. The federal review afterward made a finding that should sting every newsroom. The public said the broadcast coverage that evening was about tornadoes, almost entirely. The flood warnings were issued, and they were drowned out by the louder story. A city that had just run from the wind walked into the water. When people tell the story of El Reno, they count eight dead. The full number for that night is twenty one, and the larger half of it fell on the disaster nobody was watching.

### A5-S2b — narration
> Think about what the water asked of people that the wind never does. A tornado warning has one instruction, get low, get underground if you can. A flash flood inverts it completely. The safe place from one hazard is the deadly place for the other, and on this night the two hazards arrived in sequence, from the same storm, a few hours apart. The federal reviewers found people had been told to get out of the tornado's way, and some of them ended their evening in drainage ditches and low water crossings, in cars on flooded frontage roads, in the exact places the first warning had pushed them toward. There is no villain in that sentence. There is a warning system built to handle one disaster at a time, meeting a storm that refused to be one disaster. The review's recommendation afterward was almost humble. Teach the media, and the public, how to hold two hazards in mind at once. It took twenty one deaths in one night to put that sentence in a federal report.

### A6-S1 — narration
> Months later, the record books closed on a number that still makes people angry. EF three. A tornado two point six miles wide, with radar measured winds near three hundred miles per hour, sits in the official database two full steps below the top of the scale. Comment sections have been fighting about it ever since. The engineers who rated it were not confused, and they were not covering anything up. The answer is stranger than the controversy. Officially, the most violent winds of the widest tornado ever recorded never happened, because they never hit anything.

### A6-S2 — graphic with VO
> The Enhanced Fujita scale does not measure wind. It measures what wind does. Survey teams walk the path after the storm, find damaged structures, and work backward. A well built house swept from its foundation implies one wind speed. A snapped power pole implies another. No damage, no evidence, no rating. Now look at this tornado's path. Sixteen miles, almost all of it open farmland. The survey teams catalogued hundreds of damage points, and the worst of them, a handful of rural homes, supported EF three. But the mobile research radar sitting on that storm measured winds above two hundred ninety miles per hour near the ground, in sub vortices that spun across empty fields. Where the radar saw the most violent winds, the surveyors found nothing to inspect. Grass does not testify. Across the whole path, the radar's numbers ran ten to thirty percent above what the damage implied. The scale worked exactly as designed. It is just designed to measure a tornado by what it destroys, and this one spent its fury on emptiness. The record width stands, measured by radar. The violence stays officially invisible.

### A6-S2b — narration
> Sit with what that ten to thirty percent gap implies, because it reaches far beyond one storm. Every tornado in the historical record that crossed open country got the same treatment this one did, rated by whatever it happened to hit. Which means the record books are not a catalog of how strong tornadoes are. They are a catalog of how strong tornadoes were where they met something built by humans. Nobody knows how many storms filed away as weak spent their worst minutes over empty fields. El Reno became the case that forced that conversation into the open, because for once, a research radar was standing there taking the measurement the damage could not. The scientists who surveyed it published the radar numbers and the damage numbers side by side, and the gap between them is now part of how engineers argue about the scale itself. One tornado, two truths, both correct. The width record was accepted, because width can be measured by radar. The wind record officially does not exist. It blew across grass, and grass does not testify.

### A6-S3 — narration
> El Reno changed storm chasing the way a funeral changes a family. The community had spent two decades getting closer and closer to tornadoes, and the cost had somehow stayed at zero. Then the storm that killed the careful one proved that the margins everyone trusted could vanish in sixty seconds. The National Weather Service office in Norman built an entire retrospective around the lessons, and the lessons were blunt. A tornado can be wider than your escape plan. It can be invisible inside rain. It can turn and accelerate faster than a car on a wet section road. In the years since, the culture has shifted, more distance, more respect for rain wrapped storms, more reliance on radar over eyesight. The storm rewrote the rules by demonstrating, on the community's own cameras, that the old rules were wishes.

### A7-S1 — narration
> There is a fourth name among the chasers who died that evening, and it almost never gets told. Richard Henderson was not famous. He was a truck driver from the El Reno area who loved storms, a hobbyist who decided, that Friday, to drive out from his own home and watch this one. At five minutes past six, right after the funnel came down, he sent a friend a photo of it from his phone. A gray column over green fields, taken through a windshield. About ten minutes later, on the phone with that same friend, he said he could hear debris hitting his pickup. Then the line went dead. His family believes the tornado pulled him from the truck. He left two young sons. The famous storm that evening took the world's most careful chaser, and it also took a man who just wanted to see it, from the roads he had driven his whole life. The storm did not distinguish.

### A7-S2 — narration
> What survives of the TWISTEX team is not the crash site photographs. It is data. Tim Samaras's probes recorded pressure drops inside tornado cores that had never been captured before, numbers that are still cited, still teaching. His measurements are in the textbooks that today's forecasters learned from. Paul's cameras documented storms with an artist's eye. Carl Young's forecasting put the team where the science needed them, hundreds of times, safely, until the one storm that redefined what safely meant. The chasing community still marks the anniversary every May. And when researchers argue for keeping instruments and radars on tornadoes, so that warnings keep getting better, the case they cite is the work of a careful engineer from Colorado who believed the inside of a tornado was worth knowing.

### A7-S2b — narration
> The evening left marks on the warning system too, and they are quieter than a memorial but just as permanent. The federal review of that night runs to findings and recommendations that read like a confession. Coordinate what broadcasters tell a city that cannot shelter underground. Never let a flood warning drown under tornado coverage. Study how a traumatized population actually behaves, instead of how a pamphlet assumes it will. And years later, when researchers went looking through six American cities for anything resembling Oklahoma City's evening on the highways, they found nothing close. That study exists because this evening demanded an explanation. Every one of those changes was paid for on the thirty first of May, and the currency was twenty one lives, three of them belonging to the people who had spent their careers trying to make warnings better.

### A7-S3 — narration
> Eight names in the tornado's column. Thirteen in the flood's. Every one of the tornado's dead was in a vehicle, and that is the sentence this storm wrote into history. A car feels like safety because it moves, and this tornado was the proof that moving is not the same as escaping. You cannot outdrive what you cannot see, and you cannot out guess a storm that changes the rules mid game. The people who survived that evening in Oklahoma City were, overwhelmingly, the ones who stayed low, stayed home, and stayed out of the water. The widest tornado ever recorded killed no one in a house.

### A8-S1 — narration
> Disasters don't ask permission. But they do send warnings. Know where you would shelter before the sky ever asks the question, and let the car be your last answer, never your first. Learn what your warning sounds like, so when it comes, you already know what to do. This was The Warning Hour.
