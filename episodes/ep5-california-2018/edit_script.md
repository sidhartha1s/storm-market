# edit_script.md — ep5 · "The Fire That Made Its Own Tornado" (California 2018 duology)

> **DESIGN GATE ARTIFACT.** Owner signs off this design BEFORE any paid spend or bulk sourcing.
> Inserts (audio-carrying clips) each get individual owner confirmation before entering a render.
> Script built on `references/script-scaling.md` (the retention lattice) — cadences are per-minute
> invariants; runtime scales by acts, never by stretching beats.

## Spec
- **Channel:** The Warning Hour. **Slug:** `ep5-california-2018`.
- **Working title:** *The Fire That Made Its Own Tornado — California, 2018*
  - alt: *The Day a Wildfire Grew a Tornado — California 2018* / *2018: The Year Fire Became Weather*
- **Runtime target:** ~34–35 min. **Word budget LOCKED by probe-TTS 2026-08-05:** measured
  158 wpm (long-sentence seg) / 139 wpm (punchy seg), blended ≈ 145 wpm delivered →
  4,600 words ≈ 34–35 min. Probes: `audio/probe-a.wav`, `audio/probe-b.wav`.
- **Voice:** pocket-TTS Pharaoh clone (config `external.*`). Narration below is readable-form;
  the TTS pass mechanically converts (numbers/dates spelled, <24-word sentences, no paired dashes).
- **Scope:** duology. Carr Fire (Jul 2018, the fire tornado) front half; Camp Fire (Nov 2018,
  Paradise) emotional climax. Bridge thesis: 2018 = the year fire became weather + industrial disaster.
- **Info:fluff ≈ 75:25.** Fluff = sensory dwell + foreshadow only where a beat needs air.

## Hook contract compliance (DESIGN.md + owner orders 2026-08-05)
- [x] **NO black start — frame one is mid-action** (owner order): the CAL FIRE vortex shot already
  rotating at 0:00, scanner audio already mid-transmission. High curiosity, high impact.
- [x] intelligible high-stakes **anchor line by ~2.5s** (INSERT-01 scanner/broadcast voice)
- [x] **date/place card inside the first second** — "REDDING, CALIFORNIA · JULY 26, 2018"
- [x] every cut lands **on an audio event**; sonic spine = fire-roar + rotor + wind, builds → dies
- [x] **2.5s VOID only at hook END** (the punctuation before the narrator — never the start)
- [x] stats slam ON audio events: 143 MPH · EF-3 · 2,700°F

## Insert-transcription rule (owner order 2026-08-05 — binding)
Every `insert` is **transcribed in full (faster-whisper) BEFORE cut selection**. Cut chosen at the
transcript's action/emotion peak; excerpt + transcript path logged here AND in provenance.csv.

## Sourcing & licensing rails (binding — from footage research)
- **Spine = federal PD**: NASA GOES-16 pyroCb + MODIS/VIIRS, NWS/NOAA (Lareau science), USGS
  burn-scar, DVIDS (Cal Guard air ops). Un-claimable.
- **Iconic Carr firenado clip = CAL FIRE helicopter footage** → **VERDICT (2026-08-05):
  USE-WITH-CREDIT** ("CAL FIRE", Helicopter Coordinator footage, Aug 2018 Green Sheet release).
  CA state-works PD doctrine (AB 2880 died 2016); fire.ca.gov terms = public domain with a
  third-party-photo caveat that does not cover agency-shot footage. Source the clean copy via
  Storyful's CAL FIRE-credited upload (youtube.com/watch?v=GUglSm1PwyQ) — NOT network versions
  (their added graphics/music are separately copyrighted). Backstop stands: NASA pyroCb +
  `g-vortex` + NWS radar.
- **Camp Fire evacuation bystander clips (Chatfield/Simmons/Andrews/Seawright) + sheriff bodycam =
  STRIKE RISK. NEVER direct-from-poster.** Only network-AIRED re-cuts, 3–4s, narrated-over,
  credited. Intimate fleeing beats → AI dramatization.
- News/broadcast: 3–4s max/use, graded, credited, never the same cut twice, vary sources/chapters.
- 911/dispatch audio = PD, claim-free — the emotional layer of choice.
- Every sourced file → provenance.csv row; re-read the row before wiring.
- **Real human portraits (owner order) — VERDICTS 2026-08-05:** Stoke = SAFE-WITH-CREDIT
  (Redding FD official photo, credit the department). Smith = PREFER-ALTERNATIVE (use the
  firehero.org National Fallen Firefighters memorial photo; no unsourced grabs). Bledsoe =
  SAFE-WITH-CREDIT (family-released-to-press; credit "photo via family/outlet"; brief +
  dignified). McKay = SAFE-WITH-CREDIT (news interview stills, Camp Fire act). All ≤4–5s once,
  then cut to symbolic. NO child-victim likeness, ever.

## Graphics to hand-author (compositions/g-*.html — GRAPHICS CONTRACT; 2–3 versions of the big two)
1. `g-vortex` ★ — pyrotornadogenesis mechanism (shear zone → updraft → vortex stretching → EF-3).
2. `g-carr-map` — ignition point → Whiskeytown → the river jump into Redding. Real map plate.
3. `g-pyrocb` — plume 4→8 mi in 15 min, ~39,000 ft anvil; 3-NEXRAD triangulation annotated.
4. `g-stat-carr` — Carr toll card (ep2 stat-panel anatomy).
5. `g-camp-map` — Paradise ridge + Skyway/Pearson/Pentz chokepoints + 2014 lane-narrowing.
6. `g-ember` — plume-coupled ember cast: embers ~10 km ahead, >30 spot fires by 8:30 a.m.
7. `g-hook` ★ — THE CORRECTIVE (verified, our DA-report tally): 71 of 84 found at/just outside
   home (58 inside) · 10 died fleeing (8 vehicle, 2 foot) · 15 mobility-limited.
8. `g-stat-camp` — Camp toll card.
9. `g-title` — channel title match-cut close.
- **Match-cuts (owner order):** scene-to-scene transitions cut on matched shape/motion where the
  beat allows (rotating vortex → rotating radar sweep; river bend → road curve; calendar page →
  falling ember). Title card match-cuts the closing line.

## AI-image / AI-b-roll gap list (owner-gated at design)
- Vortex dramatization intercuts (if CAL FIRE clip is licensing-held).
- Close human-scale burned-neighborhood aftermath (Redding + Paradise).
- Intimate sheltering/fleeing dramatizations (no real-person likeness).
- Night ridge-road gridlock mood plate; bus-in-smoke plate (no child likeness).

## LOOP TABLE (the lattice spine — plant/pay tracked per act)
| # | Loop | Planted | Paid |
|---|---|---|---|
| L0 | "fire is not supposed to do this" (episode loop) | Cold open | Act 6 (the warnings were there) |
| L1 | "the river will hold it" | A1 | A1 end (it didn't) |
| L2 | "not the fire anyone had been fighting" | A1 end | A2 (it became weather) |
| L3 | "no box for what they were seeing / no warning existed" | A2 | A2 end (Loyalton 2020 closes it — competitor drops this thread) |
| L4 | "the vortex was not done" (Stoke on the road) | A3 open | A3 (the eight) |
| L5 | "it should have been the worst fire of the year" | A3 end | Bridge → A4 |
| L6 | "a hook the width of a finger" | A4 | A6 (84 counts) |
| L7 | "the fire was already ahead of them" (ember cast) | A4 | A5 (burning inside-out) |
| L8 | "you picture them in their cars — that is not what happened" | A5 | A5 (g-hook corrective) |
| L9 | "both had been predicted" | A4 (grand jury) | A6 (thesis + close) |

## Verification status (updated 2026-08-05 — fact-QC passes 1+2 applied)

**CLOSED (verdicts applied in script):** Lareau paper hedge (title poses the question; "may have
been" language in Act 2) · "second-ever after Canberra 2003" (study author's own claim) · Ed
Bledsoe whereabouts (doctor's appointment; drove back, ran, helped a burned man, stopped by
officers — competitor framing corrected) · ignition driver's fate (never named/charged; suits
targeted road agencies) · Loyalton 2020 ("believed to be the first" hedge) · manzanita (confirmed,
in Act 1) · orange night sky (general form only) · McKay bus (fully confirmed) · victim locations
(OUR name-by-name tally of the DA report's 84 narratives: 71 at/just outside home, 58 inside,
10 fleeing — 8 vehicle 2 foot, 15 mobility-limited; report states no aggregate) · sister-hook
wear (DA report §IV.b keyholing) · 113°F Redding · ~90 mi / 105 days · CAL FIRE clip + portraits
+ dozer-911 licensing (see rails).

**STILL OPEN (each gates only its own line; resolve at sourcing):**
- "Three miles in four hours" spread rate (competitor-sourced) — confirm vs CAL FIRE/NWS timeline.
- "Roughly two hundred days" without meaningful rain in Paradise — confirm vs NWS Sacramento
  climate data (agent verdict: ~200 supported, exact count unpinned).
- Bledsoe "wet blanket" line — airs AS ATTRIBUTED ("when crews reached the house, they found...")
  — keep the as-reported framing, never harden to an eyewitness claim.
- Camp ember distances — attributed to the Lareau 2026 radar study in-script (abstract-sourced).
- "football field a second" — peak-rate qualifier stays on screen.
- EXCLUDED (stay out): Rose Farrell porch detail, "Feather Canyon facility", ember-holes-in-trees,
  "210 days", "sunrise at ten PM at the hospital" specific form.

---

# THE EDIT — full script (typed segments; ~4,600 narration words)

Pacing-wave key: ⚡ fast (2–4s cuts) · 🌊 slow (holds/dwell) · blackouts hard-cut in AND out.

## COLD OPEN — mid-action (0:00–0:40) ⚡
- **0:00 frame one:** INSERT-02 — CAL FIRE helicopter shot, the vortex ALREADY rotating mid-frame.
  No fade-in. Rotor + fire-roar already running.
- **0:00.5:** title chip: "REDDING, CALIFORNIA · JULY 26, 2018".
- **INSERT-01** (owner-confirm; transcribe-first): the Shasta County 911 dozer call, cut in
  MID-TRANSMISSION, intelligible by ~2.5s — **a DIFFERENT excerpt than the competitor's pull**
  (their cut: "windows blown out"; our peak candidate: "don't risk anybody's life for mine").
  **License: CLEAR-TO-USE** (Shasta County govt record, CPRA-released via Record Searchlight —
  pull from the original at redding.com, NEVER a competitor re-rip). Teased here, paid in full
  at Act 3 INSERT-04a — same source, different cuts, `data-callback="hook-tease-payoff"`.
  *[Raw Broadcastify scanner audio = HELD (no license path) — do not use. Fallback anchor:
  audio from CAL FIRE's own three Green-Sheet-released videos, or a network air-check 3–4s.]*
- Stat chips slam ON audio events: **143 MPH** (on a roar peak) · **EF-3** (on a radio squelch) ·
  **2,700°F** (on the cut).
- **narration** (low, over the dying roar): This is not a tornado. This is a wildfire. And on one
  July evening in two thousand eighteen, above a city of ninety thousand people, it did something
  fire is almost never able to do. It reached into the sky. And it built one. **[L0 planted]**
- **hold / VOID** (2.5s black, spine dying) — the hook's punctuation. Narrator enters out of it.

> **BLACKOUT → ACT 1**

## ACT 1 — AN ORDINARY FIRE (0:40–6:10) · ~560 words · 🌊→⚡
*Job: banal cause → creeping dread. Plants L1, pays at own end. Rehooks: ignition animation,
broadcast clip, river map.*

- **narration:** Every disaster has an ordinary beginning. This one began with a flat tire. // On
  the afternoon of July twenty-third, two thousand eighteen, a travel trailer was rolling up
  Highway two ninety-nine through the dry hills west of Redding, California. Somewhere on that
  road, one of its tires failed. The drivers didn't notice. // The wheel kept turning on its bare
  steel rim, grinding the asphalt, mile after mile, scratching out a thin trail of sparks. // The
  grass beside that highway had been drying out all summer. California was coming out of its driest years on record, and a July heat wave had just pushed
  Redding to one hundred thirteen degrees. The hills were not landscape anymore. They
  were fuel. Much of that brush was manzanita, and it was so dry that summer that the living
  bushes burned like dead wood.
- **graphic `g-carr-map` (build 1):** ignition point pulses at Hwy 299 / Carr Powerhouse Rd.
- **narration:** By the time anyone saw smoke, the fire had a name — the Carr Fire, after the road
  where it was born — and a direction. East. Toward the city. // For three days, it behaved like
  the fires California knows. It burned through the Whiskeytown hills. Crews cut their lines.
  Aircraft flew their water runs, back and forth. Redding watched the smoke on the ridgeline the way you watch
  weather that belongs to someone else. // Between the fire and the city ran the Sacramento River.
  Two hundred feet of moving water. The kind of barrier a city trusts. **[L1 planted]**
- **INSERT-03** (owner-confirm; transcribed): 3–4s network clip, Jul 26 daytime — Redding under
  smoke, credited, graded.
- **narration:** On the morning of July twenty-sixth, the Carr Fire was still out in the hills,
  and the morning news called it a threat to the edges of town. By afternoon, in that
  record heat, it began to run. Three miles in four hours, straight at the water. *[verify 3mi/4hr — competitor-sourced]* // Evacuation
  orders started going out, block by block, then neighborhood by neighborhood, until thirty-eight
  thousand people were moving at once. ⚡ *[quick-cut montage: PD/DVIDS air ops, broadcast 3s,
  stock traffic — cuts on siren/radio events]*
- **narration:** That evening, the fire reached the far bank of the Sacramento River. The barrier
  the city trusted. // It did not stop. It did not even slow down. // Whole burning branches were
  falling out of the sky a mile ahead of the flames. The river was two hundred feet wide, and the
  fire stepped over it like a crack in the pavement. // Across Redding, people watched the
  night sky over the river turn orange. A sunrise, hours after sunset, on the wrong side of
  town. **[L1 paid]** // Because what crossed the
  river that night was not the fire the crews had been fighting for three days. By then, the Carr
  Fire wasn't just burning the hills. It was changing the sky above them. **[L2 planted]**
- **hold** 🌊 (3s): federal-PD wide plume (NASA/DVIDS), roar low, spine rising.

> **BLACKOUT → ACT 2**

## ACT 2 — THE FIRE THAT BECAME WEATHER (6:10–12:10) · ~800 words · 🌊 build → ⚡ reveal
*Job: the science wedge — the audience's most-loved concept, stated plainly. Pays L2, plants and
pays L3. Rehooks: pyroCb satellite loop, vortex reprise, radar graphic.*

- **graphic `g-pyrocb` (satellite loop + altitude column):** **narration:** To understand what
  happened over Redding, start with what a great fire does to the air above it. // Fire heats air.
  Hot air rises. A fire the size of a city block sends up a column you can see for miles. But the
  Carr Fire was now burning tens of thousands of acres at once, in hundred-and-ten-degree heat,
  and its column stopped behaving like smoke. It started behaving like a storm. // On the evening
  of July twenty-sixth, weather radar watched that column explode upward — from four miles high to
  eight miles high in fifteen minutes. **[info spike — counter rolls on `g-pyrocb`]** // At the
  top, eight miles up, the air is far below freezing. The smoke plume grew a cap of ice. An anvil,
  like a thunderhead. Meteorologists have a name for this: a pyrocumulonimbus. A fire cloud. // The
  Carr Fire had built its own thunderstorm. And that storm behaved like thunderstorms do. It made
  its own wind. It made its own lightning. It answered to nothing on the ground. **[L2 paid]**
- **narration (the honest nuance — the most-liked idea in the niche, stated plainly):** Now, heat
  alone cannot build a tornado. If it could, every big burn would spin. That evening, the
  air over Shasta County was already loaded — unstable, restless, with winds that changed
  direction as you went higher. The same ingredients the Great Plains feeds its tornadoes. // The fire did not break the
  rules of weather. The fire was the trigger the sky was waiting for.
- **graphic `g-vortex` (the mechanism, animated):** **narration:** Here is the mechanism. Along the
  fire's western edge, cool river air met superheated air off the burn, and the boundary between
  them began to turn — a lazy, invisible spin, close to the ground. Harmless, on any other day. //
  Above it, the fire cloud was inhaling. A column of rising air, accelerating upward, right over
  that spin. // A rising column does to spinning air what a skater does when she pulls in her arms.
  It stretches it. Tightens it. Speeds it up. // This is exactly how ordinary tornadoes are born
  under thunderstorms. There was only one difference here. The storm was the fire.
- **narration** ⚡: At about seven thirty PM, the spin touched ground on the west side of Redding.
  // A vortex a thousand feet wide at its base. Winds the National Weather Service would later put
  near one hundred forty-three miles per hour — and CAL FIRE's own investigators allowed up to one
  hundred sixty-five. On the scale we use for tornadoes, that is an EF-three. Not "like" a
  tornado. Tornado-strength, by the same measure we rate them in Oklahoma. **[stat beats land
  word-synced on `g-vortex` payoff]**
- **INSERT-02 reprise** (different crop/grade, `data-callback` — the CAL FIRE vortex, ~4s):
  **narration:** It stayed on the ground, feeding, for close to half an hour. Temperatures inside are
  estimated to have reached twenty-seven hundred degrees Fahrenheit. It pulled two steel
  high-voltage towers out of the ground and folded them. It stripped the bark off oak trees. It
  picked up a steel shipping container and threw it. 🌊
- **narration (the correction — net-info-gain):** You will hear this event called the first fire
  tornado ever recorded. The truth is stranger. The National Weather Service had no box for what
  it was seeing — officially, it logged the thing as a "fire whirl," language written for spinning
  embers the size of a dust devil. // The scientists who studied it were careful too. Their own
  paper asks, right in its title, whether this was a true tornado born of fire. Their honest
  answer: it may have been. Nothing like it had ever been measured over an American fire.
  **[L3 planted]** // No tornado warning was issued that evening.
  There was no procedure on Earth for issuing one. The forecasters were watching a tornado being
  born on radar, inside a fire, and the rulebook had no page for it. // It took two more years.
  In August of twenty twenty, over the Loyalton Fire north of Lake Tahoe, the Weather Service
  issued what is believed to be the first tornado warning for a fire-made vortex in American
  history. That page exists
  now. It was written because of Redding. **[L3 paid — the thread the other videos drop]**
- **graphic `g-pyrocb` (radar beat, 3 stations):** **narration:** Scientists reconstructed the
  Carr vortex afterward from three separate radar sites — Beale, Eureka, Medford — three radars, watching
  the same column of spinning smoke from three directions at once. In the published record, it
  stands as only the second fire-generated vortex ever documented at true tornado strength,
  after Australia's Canberra firestorm of two thousand three. **[CONFIRMED — study author's own claim]**
- **hold** 🌊 (3s): the ice-topped plume from space. Spine low. **narration (turn):** The science
  would take years. The vortex took minutes. And it was not spinning in an empty field. **[L4 planted]**

> **BLACKOUT → ACT 3**

## ACT 3 — THE EIGHT (12:10–17:20) · ~700 words · 🌊 heavy, ⚡ only inside the 911 beat
*Job: Carr's emotional bank. Pays L4. Plants L5 at exit. Portraits: Smith, Stoke, Bledsoe.*

- **narration:** The Carr Fire took eight lives. Five of them on that single evening. These are their stories.
- **narration (Don Smith):** Don Ray Smith was eighty-one years old, a bulldozer operator out of
  Pollock Pines, hired to cut fire line. He had been doing this work for decades. That evening he
  was alone on a dozer line northwest of the city when the fire front overran his position. //
  Nearby, another dozer crew was caught in the same run.
- **INSERT-04a** (owner-confirm; 911/dispatch = PD; TRANSCRIBE FIRST, cut at the peak): the
  surviving dozer operator's call — windows blown out of the cab, a voice saying he can't last
  much longer. Trim to the complete statement, nothing after. *[the single most-reacted beat in
  the reference video's comments — trace to the ORIGINAL dispatch release, never re-rip.]*
- **memorial dwell** (≤4–5s): Don Ray Smith portrait → cut to a dozer line at dusk. **narration:**
  The men in that recording survived. Don Smith did not. He was the Carr Fire's first victim.
- **narration (Stoke):** Jeremy Stoke was thirty-seven. A fire inspector for the City of Redding,
  A husband and a father. When the fire crossed the river he did what Redding firefighters
  did that night — he drove toward it, to get people out. // At seven thirty-nine PM he was on
  Buenaventura Boulevard when the vortex crossed the road. **[L4 paid]** // His last transmission
  was a mayday. He gave his position. He asked for a water drop on his own location. // There was
  no aircraft on Earth that could fly into that column. He died on the road, in the storm the
  fire had made.
- **memorial dwell** (≤4–5s): Jeremy Stoke portrait → cut to a Redding fire station, flag half-mast
  (or symbolic). *[If his actual radio traffic clears as claim-safe + tasteful: INSERT-04b, a few
  seconds, owner-gated. Else: his last call rendered as attributed on-screen text.]*
- **narration (Bledsoe):** And on Quartz Hill Road, in a house on the edge of the city, Melody
  Bledsoe was home with her two great-grandchildren. James was five. Emily was four. // Her
  husband Ed had gone to a doctor's appointment that day — before there was any sign of danger.
  Then Melody called. The fire was at the house. // Ed dropped everything and drove. Traffic
  blocked his road home, so he left the car and ran. On the way he stopped to help a burned man
  he found on the road. He tried a second route by car. Officers stopped him. The fire was
  already there. **[VERIFIED account — ABC7/WaPo interviews; the competitor's framing was
  publicly corrected by its own audience]** // James reached him by phone. The words are in the
  public record, and they are the hardest thing in this story. "Grandpa. Come and get me. The
  fire's coming in the back door." // Ed stayed on the phone with the boy until the line went
  dead. He spent the rest of that night trying to reach a house that could not be reached.
- **memorial dwell** (≤4–5s): Melody Bledsoe portrait ONLY (no child likeness) → cut to symbolic:
  a porch light in smoke, three candles. **narration:** When crews reached the house, they found
  that Melody had gathered the children under a wet blanket, covering them with her body. She was
  seventy years old. She did everything a human being could do, to the very end. *[attribute
  "wet blanket" as reported by family.]*
- **hold / VOID** 🌊 (3s black, low ambience — the breath after the heaviest beat so far).
- **graphic `g-stat-carr`:** **narration:** The Carr Fire burned for thirty-eight days. Two
  hundred twenty-nine thousand acres. Sixteen hundred buildings. More than a billion and a half
  dollars. Eight people. // By the end of August it was contained, and California exhaled, and
  the newspapers called it the disaster of the year. // It should have been. It was not even
  close. **[L5 planted — the whole room goes cold]**

> **BLACKOUT (long, 3s) → BRIDGE**

## BRIDGE — 2018 WAS NOT DONE (17:20–18:20) · ~150 words · ⚡ calendar motion
- **graphic (CA plate; calendar sheds Jul→Nov; match-cut: the vortex's rotation → the calendar
  page's turn):** **narration:** One hundred and five days after the vortex died over Redding, and about ninety miles to the
  south, something very different was about to go wrong. //
  The Carr Fire was nature moving faster than our science. What came next was our own machines,
  our own roads, our own warnings — everything people built to keep people safe, failing at once. // On a ridge in the Sierra
  foothills sat a town of twenty-seven thousand people. Many of them retirees. Pine trees over every
  street. One main road down the hill. // The town was called Paradise. **[L5 paid → A4]**

> **BLACKOUT → ACT 4**

## ACT 4 — THE MORNING OF NOVEMBER 8 (18:20–24:20) · ~800 words · ⚡ dominant, 🌊 at the map
*Job: mechanism of the massacre — wire, wind, embers, geometry. Plants L6, L7, L9.*

- **graphic `g-camp-map` (the ridge, the roads):** **narration:** Paradise sits on a ridge between
  two canyons, like a ship's deck between two furnaces. Beautiful. And cornered. // To leave
  town, nearly everyone funnels onto a handful of roads, and the main one — the Skyway — runs
  four lanes downhill toward Chico. // None of this was a secret. In two thousand eight, a Butte
  County grand jury studied the town and wrote it down in plain English: in a major fire, these
  roads cannot empty Paradise in time. They could clear maybe a quarter of the population in two
  hours. **[L9 planted]** // Six years after that warning, the town narrowed the Skyway. Two
  lanes taken away, for calmer everyday traffic. The road out of Paradise got smaller.
- **narration (the wire):** Forty miles northeast, across the Feather River canyon, ran a line of
  steel towers built in nineteen twenty-one — the Caribou-Palermo line, carrying hydroelectric
  power down from the Sierra for Pacific Gas and Electric. // On one of those towers hung a
  C-shaped steel hook, holding a live high-voltage line. It had hung there for ninety-seven
  years, swinging in the canyon wind, wearing away by fractions of a millimeter, year after year,
  from the width of your finger down to almost nothing. **[L6 planted]** // At six fifteen on the
  morning of November eighth, two thousand eighteen, in a fifty-mile-an-hour wind, it broke.
- **narration** ⚡: The live wire dropped, arced against the tower, and sprayed molten metal into
  the brush of the canyon below. At six thirty-three, CAL FIRE logged a new start near Camp Creek
  Road. The Camp Fire. // The county was under a red-flag warning that morning. Humidity under
  twenty percent. Gusts near fifty. It had barely rained in Paradise in roughly two
  hundred days. The canyon acted as a chimney, and the fire that came out of
  it was moving too fast for anyone to even talk about stopping it.
- **INSERT-05** (owner-confirm; transcribed): 3–4s network morning broadcast, Nov 8 — credited, graded.
- **graphic `g-ember` (plume-coupled spotting):** **narration:** And here the Camp Fire did what
  the Carr Fire had taught scientists to fear: its plume joined the attack. // The convection
  column lofted burning embers thousands of feet up and threw them ahead of the front — some,
  radar analysis later showed, landing miles in advance of the flames. The fire was raining
  fire. **[L7 planted; attribute radar finding to the Lareau study]** // At its worst, the fire
  was consuming the equivalent of a football field every second. Not per hour. Per second — at
  its peak, in its most explosive ninety minutes. *[peak-rate qualifier ON SCREEN]*
- **narration:** By eight thirty in the morning — two hours after the hook broke — investigators
  would count more than thirty separate fires already burning INSIDE Paradise, seeded by the
  ember rain, miles ahead of the main front. **[L7 paid]** // The town did not have a fire
  coming toward it. The town was already on fire, from the inside out, before most people had
  finished breakfast. // Twenty-seven thousand people. A quarter could get out in two hours.
  They were about to get minutes.
- **hold** 🌊 (3s): NASA Landsat SWIR fire-line from space — the ridge outlined in heat.

> **BLACKOUT → ACT 5**

## ACT 5 — EIGHTY-FIVE (24:20–30:20) · ~850 words · wave: ⚡ evacuation → 🌊 corrective → 🌊 toll
*Job: Camp's emotional bank + the episode's sharpest correction. Pays L8. Portraits: McKay.*

- **narration:** The sheriff of Butte County said it afterward in one sentence: the fire was
  outrunning our ability to warn people before we even understood we were in a race. // The
  county tried to push a mass alert to every phone. The system failed — and no one realized it
  had failed until the next day. So deputies and officers went street by street, door by door,
  with sirens and loudspeakers, while the sky went black at nine in the morning.
- **INSERT-06** (owner-confirm; transcribed; NETWORK-AIRED ONLY — never the raw bystander clips):
  3–4s of an aired evacuation report, credited, graded. ⚡
- **narration (the drive down):** What the evacuation actually looked like was this: the entire
  town, on the Skyway at once, in the dark, engines crawling, embers hitting the windshields,
  both shoulders of the road on fire. People abandoned cars and ran. People gave strangers their
  seats. The line of taillights went down the hill into the smoke, and nobody in it knew if the
  road ahead was open. *[visuals: AI gridlock mood plate + aired-broadcast micro-cuts; NO raw
  social video]*
- **narration (McKay — the hero beat):** In the middle of it was a school bus. // Kevin McKay drove a school
  bus for the Paradise school district. That morning, at Ponderosa
  Elementary, there were twenty-two children whose parents could not reach them. McKay took them,
  plus two teachers, and pointed the bus downhill into a five-hour crawl through the burning
  town. // When the smoke started filling the bus and the little ones started going quiet, he
  pulled off his own shirt, had the teachers tear it into strips and soak them in water, and
  passed the wet cloth back so the children could breathe through it. // Five hours. Fire on
  both sides of the road. Twenty-two children. // Every single one of them lived.
- **portrait dwell** (≤4s — hero, not memorial): Kevin McKay → dramatized bus-in-smoke plate (AI,
  no child likeness). 🌊
- **graphic `g-hook` (THE CORRECTIVE — build it as a reveal):** **narration:** Now. Hold the
  picture you have in your head — the cars, the gridlock, the people trapped on the road. Because
  here is the thing almost every telling of this fire gets wrong. **[L8 planted]** // When
  the district attorney wrote the report, it described where every single victim was found.
  We went through it, name by name. **[VERIFIED — our own tally of the DA report's 84
  narratives; the report states no aggregate]** // Of the eighty-four deaths in the criminal
  case, ten died trying to flee. Eight in their vehicles. Two on foot. // Seventy-one were found
  in their own homes, or just outside their own front doors. Fifty-eight of them never made it
  out of the house. **[the graphic flips: the road empties, the houses light up]** // And
  fifteen of the dead, the report says plainly, used wheelchairs, or walkers, or oxygen tanks,
  or could not drive. People who could not leave without help. No help could reach them. // The traffic did not kill Paradise. Staying killed Paradise — and most of the people
  who stayed never chose to. **[L8 paid]**
- **narration (survival footnote — info beat, brief):** And in the middle of the impossible,
  shelter worked where flight could not: more than a hundred people lived through the fire's
  worst hours standing in a parking lot in the center of town, ringed by engines, while
  everything around the asphalt burned. Firefighters kept them alive by holding one island of
  nothing-to-burn. // Know your roads. And know where the asphalt is. *[quiet Warning-Hour seed —
  pays into the close]*
- **narration (the toll):** Eighty-five people died in the Camp Fire. // Even that number had to
  fight to exist — it rose to eighty-six when survivors died of their injuries, then fell back
  when investigators found one victim had been counted twice. Eighty-five. Each revision was a
  person, with a name someone was still saying. 🌊
- **graphic `g-stat-camp`:** **narration:** In one morning: eighteen thousand, eight hundred and
  four buildings. One hundred fifty-three thousand acres. Sixteen and a half billion dollars.
  And a town of twenty-seven thousand people that effectively ceased to exist between breakfast
  and lunch.
- **hold / VOID** (3s).

> **BLACKOUT → ACT 6**

## ACT 6 — THE RECKONING + THE CLOSE (30:20–33:40) · ~550 words · 🌊 descending stakes into warm close
*Job: pay L6, L9, L0. No recap. Match-cut title close.*

- **narration (PG&E):** The hook that broke belonged to Pacific Gas and Electric. Investigators
  found hooks from the same line worn the same way: a century of metal, ground down to a few
  millimeters. **[CONFIRMED — DA report §IV.b: the same tower's right-phase C-hook had a matching
  worn channel; original hanger holes showed extensive "keyholing" wear under bolted-on
  replacement plates]** Inspections that should have caught it had been done from the
  ground, or from a helicopter window, for decades. **[L6 paid]** // Two years later, PG&E stood
  in a Butte County courtroom and pleaded guilty to eighty-four counts of involuntary
  manslaughter. Not eighty-five — prosecutors left out one victim they could not prove had died
  of the fire itself. // The maximum fine the law allowed came to about three and a half million
  dollars. Roughly forty-one thousand dollars per count. The company moved through bankruptcy,
  and a thirteen-and-a-half-billion-dollar fund for the survivors of its fires — paid, in the
  end, at seventy cents on the dollar.
- **narration (the driver — VERIFIED, airs):** And what about the couple whose trailer started
  the Carr Fire? The flat tire on Highway two ninety-nine? // Investigators never released their
  names. They were never charged. Never fined. Never sued. It was an accident, and the law
  treated it like one. The lawsuits that followed went after the agencies that managed the road,
  for the dry brush growing along it. // Hold those two endings side by side. One fire began
  with bad luck that could happen to anyone. The other began with a worn part that a company had
  a century to replace. That difference is the whole story of blame.
- **narration (thesis):** Two fires. Ninety miles and one hundred five days apart. // One
  reached eight miles into the sky and built a tornado out of its own heat — nature, moving
  faster than our science. The other started with a worn piece of steel no bigger than your
  hand, and erased a town through roads and warnings we had been told, in writing, would fail —
  our systems, moving slower than the fire. **[L9 paid]** // For a hundred years California
  called these things brush fires. In two thousand eighteen they stopped behaving like brush,
  and started behaving like weather on one end, and like industrial disaster on the other. //
  The record heat that set up Redding. The bone-dry November that set up Paradise. The science
  is blunt about the direction this is moving. The next Carr, the next Camp — those are not
  ifs. **[L0 payoff begins]**
- **graphic `g-title` (match-cut: the closing line's cadence lands AS the title card assembles —
  card does not sit):** **narration (warm close, The Warning Hour signature):** But here is what
  else was true in two thousand eighteen. The grand jury report existed. The evacuation plan
  existed. The radar was watching. The warnings were there — what was missing was the hour to
  act on them. **[L0 paid]** // Disasters don't ask permission. But they do send warnings. //
  Learn what yours sounds like. Know your roads before you need them. Know where you'd go if
  the alert never came. // So that when it comes, you already know what to do. // This was The
  Warning Hour.
- **hold** (2s) on the title card → hard out. No recap.

---

## Shot ledger (filename → subject-family → license → uses) — filled at sourcing
| filename | subject-family | license-class | uses |
|---|---|---|---|
| _(one exact filename per asset, cited by filename always)_ | | | |

## Segment/type summary
- narration ~30 · holds/voids ~9 · inserts (owner-confirm, transcribe-first) 7 (INSERT-01…06 + 04a/04b) · graphics 9 + bridge plate
- chapter blackouts: 7 hand-placed `.blackout` sections (2.4–3.0s), hard cut in/out
- rehook check: real beat every 45–60s ✓ (inserts, PD air ops, portraits, stat slams, graphic reveals)
- pacing wave: no stretch >90s at one tempo ✓ (marked ⚡/🌊 per segment)

## Next steps after design sign-off (owner gate)
1. Probe-TTS 2 segments → confirm wpm → lock word budget (trim/expand ±10%).
2. TTS per narration segment → wavs + words.json (faster-whisper).
3. Source clips (2–3 candidates/beat, provenance rows, per-cut frame verification); transcribe
   every insert BEFORE cut selection; INSERTs to owner individually; portraits usage-verified.
4. Close every verification item above (items marked [verify]/[DRIVER] gate their lines).
5. Hand-author index.html + compositions/g-*.html (GRAPHICS CONTRACT; JS/WAAPI only; match-cuts
   scene-to-scene; 2–3 versions of g-vortex + g-hook).
6. Static QC all green → verify code + timing once against words.json → draft render →
   owner preview (park) → full render → master_deliverables --hevc.
