# ep2 — 2011 Super Outbreak — edit_script.md (DESIGN DRAFT v1, awaiting owner sign-off)

**Status: DESIGN REVIEW — no paid spend, no bulk sourcing, no TTS until owner approves.**

## Targets
- Runtime: **30 min** (owner-specified; above the channel's usual 13–23 band — deliberate).
- Narration budget: **30 × 0.9 × 137 ≈ 3,700 words** (measured pocket-TTS formula; probe-TTS 2 segments before full write).
- Structure: sub-composition per act (native per-act re-renders, per CLAUDE.md).
- Formula: cold-open ≤15s → thesis 60–90s → location-by-location march → stats mid, **emotion banked at the END** → warm Warning Hour footnote. Micro-loops every 30–45s. No recap.

## Positioning (from coverage-matrix.md — 4 independent competitor treatments)
- **Table stakes we must cover:** Hackleburg–Phil Campbell EF5 centerpiece, Tuscaloosa–Birmingham EF4, four-EF5s-in-one-day record, Smithville EF5, EF-scale explainer, on-air meteorologist through-line, aggregate close.
- **Our wedge (gaps NO competitor touches):**
  1. Real synoptic meteorology (CAPE/shear/jet stream/dryline — every competitor stays at "read the bulletin aloud").
  2. **NWS Service Assessment findings** — zero sources cite it. Key planned beat: the pre-dawn squall line knocked out power + sirens + NOAA weather radio transmitters ACROSS north Alabama hours before the violent afternoon wave — people never heard the warnings that were issued on time. (VERIFY in SA.)
  3. 911 audio (genre staple, absent in all 5 videos; PD, claim-free).
  4. True 4-day / multi-state scope (Apr 25–28; competitors are functionally AL-only).
  5. How engineers estimate wind speed from damage (answers Dark Horizon's dangled "beyond EF5" question).
  6. Reconciled, cited official numbers — competitors circulate 5 different death tolls (252/238/316/324/348), one contradicts itself in-video. We cite NWS/NOAA on-screen.
  7. **Dual-pol radar reform arc (owner-approved 2026-07-26):** April 2011 pre-dated the national dual-polarization rollout — debris-ball detection improved dramatically right after. Concrete "here's what changed."
  8. **24-min lead time contextualized (owner-approved):** national average ~13 min (V) — warnings ran ~2× better than normal and people still died. Sharpens the thesis.
  9. Browns Ferry nuclear plant: Hackleburg tornado cut its transmission lines, all 3 reactors scrammed to emergency diesel (V vs NRC report). Editor's-choice include.
  10. Hackleburg's Wrangler plant never reopened — **CONDITIONAL: include ONLY if verification confirms** (owner rule); else drop entirely.
- **Anti-patterns:** SkyWhisper spreads emotion across segments — we bank it at the end (proven formula). Spark/Wonder = same TV doc twice; its named-character material (Stevens/Downs/Brown story) is that production's interview content — we use only publicly documented facts/quotes with attribution, never re-narrate their interviews as ours.

## FACT-VERIFICATION LEDGER (hard gate before scripting prose)
All numbers below marked (V) must be verified against the **NWS Service Assessment (April 25–28 2011 outbreak)**, NOAA/NCEI Storm Events, and SPC records before TTS. Competitor numbers are hypotheses, not facts. Known conflicts: outbreak deaths 316/324/348 · AL deaths 238/252 · Hackleburg path 102/130 mi · winds 200/210 mph · Smithville deaths 16/23 · damage $10.2B/$15B.

---

## Act structure (sub-compositions)

### A0 — COLD OPEN + THESIS (0:00–1:30 · ~165 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a0-s1 | insert | **Ground-POV flash-forward montage (~20–25s, owner-upgraded from audio-only):** 6–8 micro-clips, 1.5–3s each, real people AS the tornado hits — inside a house (survivor smartphone POV), through a windshield, storefront camera, sheltering audio ("get down, get DOWN"), with the **911/dispatch audio as one scene** in the chain. Every clip enters **MID-ACTION** (no wind-up, no aftermath — the hit itself), and **cuts land ON the audio** (scream / crash / dispatch line drives each cut point, not a fixed grid). No date/place context — pure flash-forward (clips recur later in full context = bookend callback). Sourcing: original survivor uploads / news-archive compilations / FEMA-collected footage via yt-dlp + archive.org — **NOT re-ripped from the 5 reference videos** (their edit carries their production's Content ID fingerprint + VO bleed; refs are a SHOT LIST, we trace each clip to its original source). Per-clip provenance + license check; chaser footage excluded. Each clip OWNER-CONFIRMED (frames + source + license, one message). All audio loudnorm to narration level, first sound ≤1s in. | Raw ground POV, grain layer unifies, no titles |
| a0-s2 | narration (~90w) | Present-tense drop-in: mid-afternoon April 27, a tornado wider than a mile is on the ground and has been for over an hour. Warnings went out 24 minutes ahead (V). People are dying anyway. | Real NEXRAD re-plot (our render), town-name chyrons |
| a0-s3 | narration (~75w) | **Thesis @ ~60–75s:** by midnight, four EF5s in one day — never recorded before or since (V) — 300+ dead across 21 states (V). Foreshadow: "The forecast was nearly perfect. That is what makes this day so hard to forget — and it is why what went wrong matters more than what went right." | Title card: THE 2011 SUPER OUTBREAK, match-cut on "four" |

### A1 — THE SETUP: Apr 25–26 + the science (1:30–6:00 · ~555 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a1-s1 | narration | Apr 25: Vilonia AR devastated, first deaths (V); PDS watch; 42 tornadoes day one (V). Apr 26: 55 more (V). The outbreak is already national news — and the worst is 24h away. | Archive news stills, map march (our graphic) |
| a1-s2 | graphic+VO | **NET-INFO-GAIN meteorology block:** the actual ingredients — Gulf moisture surge, jet stream position, wind shear/helicity, CAPE "fuel gauge" translated to human scale. Why this alignment is a once-in-decades loading of the dice. Textbook-case framing. | Animated ingredient diagram, layered build, info beat every 2–3s |
| a1-s3 | narration | The forecasting drama: SPC 5/5 HIGH RISK at 7:55am (V); 45% tornado probability ring (V). **The 2006 "bust" caveat** (Swegle's best beat, deepened): why forecasters sweat squall-line-vs-supercell — too much instability can SAVE lives by clogging the storm mode. Apr 27 would not bust. | Real SPC outlook graphics (PD), probability map re-plot |
| a1-s4 | hold (3–6s) | Breath before the day begins. | Calm dawn sky, ambience up |

### A2 — MORNING TRAP: Apr 27 pre-dawn (6:00–9:00 · ~370 words)
| # | Type | Content | Visual intent |
|---|---|---|---|
| a2-s1 | narration | 3:41am Gordo EF3 (V); ~36 tornadoes before 8am (V); Spann on air from 5:40am ("a lot of you are just waking up to sirens"). | Dark radar loops, siren-lit streets |
| a2-s2 | narration | **THE SERVICE ASSESSMENT BEAT (nobody covers this):** the morning wave knocked out power to hundreds of thousands + destroyed NOAA weather radio transmitters + disabled sirens (V, SA) — north Alabama walked into the afternoon deaf. Warnings would be issued on time; many never arrived. | Doc-style: SA report pages, transmitter map graphic |
| a2-s3 | insert | Short broadcast clip of morning coverage (OWNER CONFIRMS). | — |

### A3 — PHILADELPHIA, MS EF5 (9:00–11:00 · ~245 words)
"The forgotten EF5" — 2:30pm, first of four; ~205mph, 3 dead (V); trenches dug 2 ft into earth. Any other year, a career-defining storm; today, a footnote by sunset. Establishes the march + stat-card cadence (duration → path → deaths → damage; SkyWhisper's ritual, adopted).

### A4 — HACKLEBURG → PHIL CAMPBELL EF5 · CENTERPIECE (11:00–16:00 · ~615 words)
| Beat | Content |
|---|---|
| march | 3:05pm touchdown; EF1→EF5; 75% of Hackleburg gone; Wrangler factory destroyed, jeans found 40 mi away; high school leveled; 18 dead (V) |
| object-horror | 25-ft slab of road pavement torn out, found ⅓ mi away; pace with 2–4s stingers |
| shelter beat | Phil Campbell concrete shelter loses its ROOF over 21 people — all 21 live (V). The margin between shelter and no shelter, made visible |
| march cont. | Mount Hope, Tanner, Harvest; 102-mi path (V), ~1h45m on ground (V); deadliest single tornado of the outbreak, ~71 dead (V) |
| radar graphic | Our NEXRAD Level-II re-plot of the supercell's full run (GCP mirror; honest burned-in-time labeling) |
| stat card | Duration / path / deaths / damage ($1.29B V) |

### A5 — SMITHVILLE, MS EF5 (16:00–18:30 · ~305 words)
3:42pm; EF5 within ~3 minutes (V); 205mph. Object horror: SUV hurled into the water tower; tombstones rotated backward; ground scoured a foot deep; 117 structures incl. city hall, police station, 4 churches (V). Deaths: **16 vs 23 conflict — VERIFY**. First MS tornado this violent since 1966 (V).

### A6 — TUSCALOOSA → BIRMINGHAM EF4 (18:30–24:00 · ~675 words)
| Beat | Content |
|---|---|
| formation | 4:43pm, Greene Co.; Oldshue livestream = first ground confirmation, ~30 min lead credited with saving lives |
| emergency | Tornado emergency; Spann: "This will be a day that will go down in state history… all you can do is pray for those people" |
| the hit | 5:13pm crosses the city; 12% of Tuscaloosa destroyed in ~6 minutes; 7,000 jobs gone in that window; EMA office itself destroyed |
| science beat | **NET-INFO-GAIN:** why this is rated EF4 not EF5 — how damage-survey engineers actually estimate winds, and why the scale caps out. Answers the "functionally an EF5" argument competitors wave at |
| object-horror | 34-ton railroad truss thrown 100 ft uphill; 35-ton railcar thrown 400 ft at a coal yard |
| Birmingham | Regains EF4 strength; Concord/Pleasant Grove/McDonald Chapel, 20 dead; swerve spares downtown |
| stat card | 64 dead (V) · 1,500+ injured · $2.4B (V) · costliest ever — for 25 more days, until Joplin |

### A7 — THE FOURTH EF5 + THE LONG NIGHT (24:00–26:30 · ~305 words)
Rainsville/DeKalb EF5 6:19pm: school bus stripped to bare chassis; 800-lb safe carried 600 ft, door torn off; 25 dead (V). Ringgold GA EF4 (20 dead V); Lake Martin cabins EF4. "No tornado warnings in Alabama for the first time in I don't know when." Apr 28 pre-dawn coda in Georgia — 3 more lives (V) — the rest beat before the reckoning.

### A8 — THE RECKONING (emotion banked here) (26:30–29:30 · ~370 words)
| Beat | Content |
|---|---|
| numbers, reconciled | On-screen-cited official totals (NWS/NOAA): ~360 tornadoes, 4 days, 21 states, 324 dead (V) — with a one-line "sources disagree; these are the government's own figures" credibility beat |
| why they died | SA findings woven together: morning-crippled warning infrastructure + ~80% historical false-alarm rate + this outbreak's atypical permanent-home fatality pattern (V). The warnings worked; the last mile failed |
| survivor vignettes | 2–3 publicly documented, attributed human stories held for HERE (per formula): candidates — the Phil Campbell shelter's 21; Ashley Harrison (UA senior, days from graduation) (V, respectful-framing rules, memorial-portrait ≤5s if real photo exists); Tuscaloosa memorial inscription read in full |
| close | Unresolved-quote energy, no tidy bow — then footnote |

### A9 — WARNING HOUR FOOTNOTE (29:30–30:00 · ~60 words)
Canonical warm preparedness cadence → "…This was The Warning Hour." Match-cut title card, no dwell, no recap.

---

## Inserts requiring owner confirmation (sourced AFTER design lock, each gated individually)
1. Cold-open 911/dispatch audio (a0-s1)
2. Morning broadcast clip (a2-s3)
3. Spann "pray for those people" moment (A6) — short, narrated-over, claims-survivable
4. Oldshue livestream excerpt (A6) — license check first; treat as chaser-adjacent, DO NOT use without clearance

## Footage plan (claim-proof stack)
NEXRAD re-plots (2 min. set: Hackleburg supercell, Tuscaloosa hook echo) · SPC/NWS PD graphics · FEMA/NG aftermath footage · archive.org day-after news · Pexels/Pixabay neutral b-roll · AI b-roll only for dramatization gaps · SFX from library per editorial choice. NO storm-chaser footage without license. Subject-family ledger maintained from first sourcing pass.

## Word budget check
165+555+370+245+615+305+675+305+370+60 = **3,665 words ≈ 26.8 min narration ≈ 30 min runtime** with holds/inserts. ✔
