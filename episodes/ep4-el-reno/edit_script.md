# ep4 — El Reno 2013 — edit_script.md (DESIGN v2 — owner-approved 2026-08-01, sourcing authorized)

**Owner orders added at approval (2026-08-01):**
- **Clip breadth is a sourcing budget, not taste:** ep2 shipped 187 windows/28 min; ep3 audit proved the asset pool must FEED the cut rate. Target for 36 min: **~200+ picture windows → 120–150 distinct assets minimum.** No repeats (subject-family dedup); a starved pool = the #1 boredom/leave signal.
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
175+560+800+800+800+650+650+580+65 = **5,080 words** ≈ 35.7 min at 158 wpm ÷ 0.9 pacing → on target for ~36 min. Probe-TTS 2 segments before full script write.
