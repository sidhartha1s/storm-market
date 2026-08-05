# edit_script.md — ep5 · "The Fire That Made Its Own Tornado" (California 2018 duology)

> **DESIGN GATE ARTIFACT.** Owner signs off this design BEFORE any paid spend or bulk sourcing.
> Nothing below is rendered or generated yet. Inserts (audio-carrying clips) each get individual
> owner confirmation before they enter a render (DESIGN.md hard rule).

## Spec
- **Channel:** The Warning Hour. **Slug:** `ep5-california-2018`.
- **Working title:** *The Fire That Made Its Own Tornado — California, 2018*
  - alt: *The Day a Wildfire Grew a Tornado — California 2018* / *2018: The Year Fire Became Weather*
- **Runtime target:** 33 min (band-exceeding, owner-approved wide scope — cf. ep2's 30 min).
- **Word budget:** ~4,700 narration words (33 × 0.9 × 158). **NOT LOCKED** — probe-TTS 2 segments
  first (CLAUDE.md: the 158 figure must be re-confirmed per episode). Draft below runs ~4,650.
- **Voice:** pocket-TTS Pharaoh clone (config `external.*`). Narration shown **readable** here for
  review; the per-segment TTS text spells out every number/date/time and obeys the <24-word / no-
  paired-dash rules before TTS (mechanical transform at the TTS step).
- **Scope:** duology. Carr Fire (Jul 2018, the fire tornado) = front half + cold-open pinpoint;
  Camp Fire (Nov 2018, Paradise) = emotional climax. Bridge thesis ties them into one 2018 story.

## Hook contract compliance (DESIGN.md cold-open contract — mapped)
- [x] intelligible high-stakes **anchor line by ~2.5s** — real Carr-Fire scanner/broadcast voice (INSERT-01, to source + owner-confirm)
- [x] **date/place card in first second** — "REDDING, CALIFORNIA · JULY 26, 2018"
- [x] **firenado on screen in the hook** (owner order) — CAL FIRE helicopter vortex shot (INSERT-02, STATE-VERIFY)
- [x] every cut lands **on an audio event**; **sonic spine** = fire-roar/wind build under the anchor
- [x] **2–3s black VOID** before the narrator enters
- Few clips, each earning its slot. No undifferentiated montage.

## Sourcing & licensing rails (from footage agent — binding)
- **Spine = federal PD**: NASA GOES-16 pyroCb + MODIS/VIIRS, NWS/NOAA (Lareau vortex science),
  USGS burn-scar (Landsat/LCMAP), DVIDS (Cal Guard air ops). Un-claimable.
- **The iconic Carr firenado clip = CAL FIRE helicopter footage** (institutional, NOT chaser) →
  **STATE-VERIFY**: CA state/local works lean public-domain, but this clip rode a fatality
  "Green Sheet" release, not an explicit reuse grant. **Confirm CAL FIRE reuse terms + no
  restrictive statement BEFORE it locks into the cut.** Backstop if it fails: NASA pyroCb
  satellite + self-made vortex graphic + NWS radar.
- **Camp Fire evacuation footage = private bystander phone video / sheriff bodycam = STRIKE RISK
  (chaser-class).** MUST-NOT-USE-DIRECT: Chatfield, Simmons, Andrews, Seawright raw clips. Usable
  only re-cut from a **network's aired broadcast** (3–4s, narrated-over, courtesy credit). Intimate
  "family fleeing" beats → AI-dramatized inserts, never social reposts.
- News/broadcast: 3–4s max, narrated over, graded to the unified film look, credited (credit ≠
  license ≠ claim-immunity). Never reuse a broadcast cut twice; vary source/chapter.
- Every sourced file → a `media/provenance.csv` row; re-read the row BEFORE wiring (era/backup notes disqualify).

## Graphics to hand-author (compositions/g-*.html — GRAPHICS CONTRACT, motion mandatory)
1. `g-vortex` — **pyrotornadogenesis mechanism** (the centerpiece). Wind-shear zone → fire plume
   updraft → vortex-tube stretching → EF3 vortex. Build the mechanism, animate it, label names it
   (NOT a cone captioned "tornado"). Continuous updraft motion + word-synced reveals.
2. `g-carr-map` — Carr ignition (Hwy 299 / Carr Powerhouse Rd) → jump across the Sacramento River
   into Redding. Real map plate, route fits measurable landmarks.
3. `g-pyrocb` — the fire's own storm: plume 4→8 miles in 15 min, top ~39,000 ft, glaciated anvil;
   3-NEXRAD triangulation (Beale / Eureka / Medford) annotated. Continuous plume-growth motion.
4. `g-stat-carr` — Carr toll stat card (ep2 g-stat anatomy: acreage / structures / 8 lives / cost).
5. `g-camp-map` — Paradise on the ridge; the evacuation chokepoints (Skyway, Pearson, Pentz);
   the 2014 lane-narrowing annotated. Self-made — no claim-safe traffic-jam footage exists.
6. `g-ember` — plume-coupled ember cast: embers lofted up to ~10 km ahead, >30 spot fires by
   8:30 a.m. merging into lobes. Continuous ember-drift motion.
7. `g-hook` (the fatal geometry) — **70 of 84 died at/near their own homes, only 8 fleeing** — the
   stat that flips the "stuck in traffic" story. Reveal as a corrective beat, not a poster.
8. `g-stat-camp` — Camp toll (85 lives / 18,804 structures / $16.65 B / 84 manslaughter counts).
9. `g-title` — channel title match-cut for the outro.
> Each big-concept graphic (`g-vortex`, `g-hook`) gets **2–3 versions** for owner pick (DESIGN.md).

## AI-image / AI-b-roll gap list (for owner — no claim-safe real footage)
- Fire-tornado vortex dramatization to intercut with the CAL FIRE shot + `g-vortex` (if CAL FIRE clip is licensing-held).
- Close, human-scale burned-neighborhood aftermath (Redding & Paradise) — Getty has it paid; free is thin.
- Intimate "family sheltering / fleeing" beats (Bledsoe home; Paradise porches) — dramatized, never real-victim likeness, never social reposts.
- Night ridge-road gridlock mood plate for Act 5 (generic, not a real identifiable clip).

## Open verification items to CLOSE before script locks (from UNVERIFIED flags)
- Pull readable **Lareau et al. 2018 GRL** full text (satellite figures/EF language) — press-release-sourced now.
- "**Second-ever** fire vortex after 2003 Canberra" — confirm against primary before on-air.
- Bledsoe "wet blanket" quote — secondhand via news aggregation; trace or attribute as reported.
- **85 vs 86** Camp toll (double-count correction) — state 85, caveat.
- "football field per second" — **peak ~90-min rate**, not 24-hr average; qualify on screen.
- Camp ember "10 km" — Lareau 2026 abstract-only; attribute as the study's finding.
- Rose Farrell / "Feather Canyon facility" — UNVERIFIED; do not use unless confirmed.

---

# THE EDIT (typed segments — narration / hold / insert / graphic; blackouts at act turns)

## COLD OPEN — the firenado (0:00–0:30)
- **INSERT-01** (owner-confirm): real Carr-Fire scanner/broadcast anchor voice from the evening of
  Jul 26 — a dispatcher or live news line naming Redding under fire. Anchor lands by ~2.5s. Date/
  place card "REDDING, CALIFORNIA · JULY 26, 2018" in the first second. *[to source: Broadcastify
  archive / network air-check; if no claim-safe line clears, fall back to a 911/dispatch line.]*
- **INSERT-02** (owner-confirm): CAL FIRE helicopter shot of the rotating fire column (STATE-VERIFY).
  Sonic spine = fire-roar + wind swell building under INSERT-01. Cut on the roar peak.
- **narration** (whisper-low, over the dying roar): "For one hour, on one July evening, a wildfire
  did something fire is not supposed to do. It reached into the sky, and it built a tornado."
- **hold / VOID** (2.5s black, spine fading) → narrator enters.

> **BLACKOUT** → Act 1.

## ACT 1 — an ordinary fire (≈0:30–5:30)
- **graphic `g-carr-map`** under narration: ignition point, the river, Redding.
- **narration:** It began the way a thousand California fires begin. On the afternoon of July
  twenty-third, two thousand eighteen, a man was towing a trailer on Highway two ninety-nine, west
  of Redding. A tire went flat. The bare steel rim dragged on the pavement, and it threw sparks
  into dry roadside grass. // In a drought year, that is all it takes. The Carr Fire was born from
  a wheel. // For three days it burned through the hills around Whiskeytown, the way these fires
  do. Crews drew their lines. The city of Redding, ninety thousand people, watched the smoke and
  believed the river would hold it. // The Sacramento River is two hundred feet of moving water. It
  is the kind of natural barrier a city trusts. // On the evening of July twenty-sixth, the fire
  reached the far bank. And then it did not stop.
- **INSERT-03** (owner-confirm): short broadcast clip — Redding under threat, Jul 26 (3–4s, credited).
- **narration:** What crossed the river that night was not the fire anyone had been fighting. The
  air itself had changed. // To understand what happened next, you have to understand that a fire
  this large stops being a fire. It becomes weather.
- **hold** (3s): federal-PD wide plume shot (NASA/DVIDS), spine up.

> **BLACKOUT** → Act 2.

## ACT 2 — pyrotornadogenesis: how a fire grows a tornado (≈5:30–12:00)  *[meteorology wedge]*
- **graphic `g-pyrocb`:** the fire's own storm. **narration:** A fire that burns hot enough sends
  up a column of rising air. On the twenty-sixth, the Carr Fire's column exploded upward, from four
  miles high to eight miles high, in fifteen minutes. // At the top, so high the air was freezing,
  the column grew an anvil of ice. The fire had made its own thundercloud. Scientists call it a
  pyrocumulonimbus. A fire, wearing the sky like a hat.
- **graphic `g-vortex`** (centerpiece; animate the mechanism): **narration:** Under that rising
  column, the wind was already turning along the fire's edge, where cool air met the superheated
  air of the burn. On its own, that spin means nothing. // But a rising column does to spinning air
  what a spinning skater does when she pulls in her arms. It stretches it. It concentrates it. It
  makes it faster. // This is exactly how an ordinary tornado forms under a thunderstorm. The only
  difference here was the storm. The storm was the fire. // But heat alone could never have done
  it. The sky above Redding had to be primed for spin, the same unstable air an ordinary tornado
  needs. The fire did not break the rules of weather. It met them, and it became the trigger the
  sky was waiting for. *[most-loved audience concept: "the fire is just the trigger the atmosphere
  needed" — state it plainly, the competitor only implies it.]*
- **graphic `g-vortex` (payoff beat):** **narration:** At around seven thirty in the evening, the
  spin reached the ground. A vortex roughly one thousand feet wide. Winds the National Weather
  Service later estimated near one hundred forty-three miles an hour. Strong enough to rate an EF
  three, the same scale we use for the tornadoes of the Great Plains. // Inside it, temperatures may
  have reached twenty-seven hundred degrees. It tore two steel transmission towers out of the
  ground. It stripped the bark from oak trees. It threw a shipping container.
- **INSERT-02 reprise** (different crop/grade, callback — the CAL FIRE vortex, held ~4s).
- **narration (the correction — net-info-gain):** You will hear this called the Carr Fire tornado.
  The scientists who studied it were more careful. The Weather Service logged it as a fire whirl,
  because our rules had no box for what they were seeing. // No tornado warning was ever issued for
  it. There was no procedure to issue one. The first tornado warning in history for a fire-made
  vortex would not come for another two years. // In two thousand eighteen, the science was standing
  in the burn, watching something it did not yet have the words for.
- **graphic `g-pyrocb` (radar beat):** **narration:** They pieced the vortex together afterward
  from three separate radars, at Beale, at Eureka, and across the border in Oregon. Only the second
  fire vortex ever formally documented to reach true tornado strength. *[verify "second-ever."]*
- **hold** (3s): the ice-topped plume from space (NASA), spine low.

> **BLACKOUT** → Act 3.

## ACT 3 — the eight (≈12:00–16:30)  *[Carr emotion banked]*
- **narration:** The vortex was on the ground for about thirty minutes. In that half hour, and the
  hours around it, the Carr Fire took eight lives.
- **narration (Don Smith):** Don Ray Smith was eighty-one, a contract bulldozer operator, cutting
  fire line ahead of the flames when the front overran him. Other dozer operators nearby got out,
  barely.
- **INSERT-04a** (owner-confirm; 911 audio = PD, claim-safe): the surviving dozer crew's call to
  dispatch — windows blown from the cab, a voice saying he cannot last much longer. This is the
  reference video's single most-reacted beat (785-like comment: "made me tear up"). **Trace to the
  original dispatch/news release — do NOT re-rip from the competitor.** Trim to end on the complete line.
- **memorial dwell** (≤4–5s): Don Ray Smith portrait (verify usage) → cut to a dozer line in the hills.
- **narration (Stoke):** Jeremy Stoke was thirty-seven, a fire inspector for the city of Redding.
  At seven forty that evening he was driving toward the fire, going to help people evacuate, when
  the vortex found the road. // His last radio call asked for a helicopter to drop water on his own
  position. There was no helicopter that could fly into that. He did not get out.
- **INSERT-04b** (owner-confirm; OPTIONAL, if claim-safe): a few seconds of Stoke's mayday radio
  traffic, or a memorial line read on-air. *[to source; else render as attributed on-screen text.]*
- **memorial dwell** (≤4–5s): Jeremy Stoke portrait (verify usage rights) → cut to symbolic (a
  Redding street), never linger on the face.
- **narration (Bledsoe):** A few miles away, in a home in Redding, seventy-year-old Melody Bledsoe
  was watching her two great-grandchildren, James, who was five, and Emily, who was four. // Their
  great-grandfather, Ed, had left the house earlier that day and was trying to get back to them.
  The fire moved faster than anyone believed it could. *[FAIRNESS: competitor's telling was
  publicly corrected (399 likes) for implying Ed was callous — he was not; he tried and could not
  reach them. Verify exact whereabouts, see open items.]*
  // The boy reached him by phone. The words are in the record: "Grandpa, come
  and get me. The fire's coming in the back door." // He tried. The roads were already gone.
- **memorial dwell** (≤4–5s): symbolic imagery only (three candles / a wet blanket motif —
  dramatized, NO real-child likeness). **narration:** When they were found, Melody was covering both
  children with a wet blanket. She had done everything she could, to the very end. *[attribute "wet
  blanket" as reported.]*
- **graphic `g-stat-carr`:** two hundred twenty-nine thousand acres. Sixteen hundred buildings.
  Eight lives. Over one and a half billion dollars. // **narration:** By the end of August, the Carr
  Fire was contained. California exhaled. // It should have been the worst fire of the year. It was
  not close.
- **hold / VOID** (3s black) — the exhale before the turn.

> **BLACKOUT (long, ~3s)** → Bridge.

## BRIDGE — 2018 was not done (≈16:30–17:30)
- **graphic (CA state plate, calendar motion Jul→Nov):** **narration:** The Carr Fire was the fire
  that broke the laws of fire. What came next broke something else. // One hundred and six days
  later, and one hundred miles to the south, a hundred-year-old wire was about to fail on a ridge
  above a town called Paradise. // Twenty-seven thousand people lived there. Most of them had never
  heard the phrase "wildland urban interface." They were about to become the deadliest example of it
  in American history.

> **BLACKOUT** → Act 4.

## ACT 4 — the morning of November 8th (≈17:30–23:30)
- **graphic `g-camp-map`:** Paradise on its ridge; the few roads down. **narration:** Paradise sat
  on a ridge in the Sierra foothills. Beautiful, and trapped. To leave, everyone had to funnel onto
  a handful of narrow roads, and the main one, the Skyway, ran downhill into the smoke. // This was
  not a secret. In two thousand eight, a county grand jury warned that the town could not be
  evacuated in time. The roads could clear maybe a quarter of the people in two hours. // Six years
  later, the town narrowed the Skyway by two lanes. For safer everyday traffic.
- **narration (ignition):** At six fifteen on the morning of November eighth, a control room logged
  a fault on the Caribou-Palermo line, a set of transmission towers strung across the canyon in
  nineteen twenty-one. // On one tower, a hook holding a live wire had worn, over ninety-seven
  years, from the width of your finger down to a few millimeters. That morning it finally broke. //
  By six thirty-three, the canyon below was on fire. There was a red-flag wind that day, gusting
  past forty miles an hour, and the humidity was under twenty percent. The fire had everything it
  needed.
- **INSERT-05** (owner-confirm): 3–4s network broadcast, Nov 8 morning (credited, graded).
- **graphic `g-ember`:** **narration:** Then the Camp Fire did what the Carr Fire had taught us to
  fear. Its own plume began throwing fire ahead of itself. // Embers rode the column and came down
  miles in front of the flames, some nearly six miles ahead, starting dozens of new fires inside
  Paradise before the main fire ever arrived. // By half past eight in the morning, the town was
  burning from the inside out. People woke to a normal Thursday and had minutes.
- **hold** (3s): NASA SWIR fire-line from space, spine building.

> **BLACKOUT** → Act 5.

## ACT 5 — eighty-five (≈23:30–29:30)  *[Camp emotion banked + the corrective]*
- **narration (the race):** The sheriff would later say the fire was outrunning them before they
  understood there was a race. // They tried to send a countywide emergency alert. It failed, and no
  one realized it had failed until the next day. So they went zone by zone, street by street, with
  the fire moving a football field every second at its worst.
- **INSERT-06** (owner-confirm): a network-aired evacuation clip, 3–4s ONLY, credited. *[NEVER the
  raw bystander/sheriff-bodycam originals — strike risk.]*
- **narration (McKay — the hero beat):** On the Skyway, a school bus driver named Kevin McKay had
  twenty-two children whose parents could not reach them, and two teachers, and five hours of
  gridlock through fire on both sides. // When the smoke came into the bus, he tore off his own
  shirt, soaked it, cut it into strips, and passed them back so the children could breathe. // Every
  one of those twenty-two children lived.
- **memorial/quiet dwell** (≤4s): dramatized bus-in-smoke plate (AI, no real-child likeness).
- **graphic `g-hook` (the corrective — the episode's sharpest net-info-gain):** **narration:** And
  here is the thing almost every telling of this fire gets wrong. // We picture the dead in their
  cars, trapped in the traffic on the Skyway. But when investigators counted, of the eighty-four
  deaths in their report, only eight died while trying to flee. // Seventy died at home, or just
  outside their own front doors. The people who could not move fast enough. The old. The disabled.
  The ones who never got the warning that failed. // The traffic did not kill Paradise. Not
  leaving, killed Paradise.
- **narration (the toll):** Eighty-five people died. The count is not even simple. It rose to
  eighty-six, then fell back to eighty-five, when they realized one victim had been counted twice.
  Each number is a person someone is still counting. *[caveat 85/86.]*
- **graphic `g-stat-camp`:** eighty-five lives. Eighteen thousand, eight hundred and four buildings.
  A town, gone in a morning. // **narration:** Paradise, California, population twenty-seven
  thousand, effectively ceased to exist between breakfast and lunch.
- **hold / VOID** (3s).

> **BLACKOUT** → Act 6.

## ACT 6 — the reckoning + the close (≈29:30–33:00)
- **narration (PG&E):** The wire that started it belonged to Pacific Gas and Electric. Two years
  later the company pleaded guilty to eighty-four counts of involuntary manslaughter. // Not eighty-
  five. Prosecutors could not be certain that one of the dead had not chosen the fire over waiting
  for it. // The utility paid the largest fine the law allowed, and filed for bankruptcy owing tens
  of billions to the people it had burned.
- **narration (what changed / the thesis):** Two fires, one hundred miles and four months apart. One
  reached into the sky and grew a tornado. The other reached into a town and erased it. // For a
  century we called these brush fires. In two thousand eighteen they stopped behaving like brush,
  and started behaving like weather, and like the failure of the machines we built. // Both of them
  had been predicted. A grand jury saw Paradise coming. The science was already watching the sky. //
  The warnings were there. What was missing was the hour to act on them.
- **graphic `g-title` (match-cut to channel title, does not sit):** **narration (warm close):**
  Disasters don't ask permission. But they do send warnings. The Carr Fire and the Camp Fire were
  California's, written in one terrible year. // Learn what yours sounds like. Know your roads
  before you need them. Know that the fire can arrive before the alert. // So that when it comes,
  you already know what to do. // This was The Warning Hour.
- **hold** (2s) on the title card → hard out. No recap. No outro summary.

---

## Shot ledger (filename → subject-family → uses) — filled during sourcing
| filename | subject-family | license-class | uses |
|---|---|---|---|
| _(populated at Phase 5 sourcing; one exact filename per asset, cited by filename always)_ | | | |

## Segment/type summary
- narration segments: ~26 · holds/voids: ~8 · inserts (owner-confirm): 6 (INSERT-01…06) · graphics: 9
- chapter blackouts: 7 (every act turn + long bridge) — hand-placed `.blackout` sections, 2.4–3.0s.

## Next steps after design sign-off (owner gate)
1. Probe-TTS 2 segments → confirm wpm → adjust word budget/length.
2. TTS per narration segment → wavs + words.json.
3. Source clips (2–3 candidates/beat, provenance rows, frame-verify) — INSERTs to owner individually.
4. Resolve the open verification items above.
5. Hand-author index.html + compositions/g-*.html (GRAPHICS CONTRACT).
6. Static QC suite green → draft render → owner preview → full.
