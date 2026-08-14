# edit_script.md — ep6 · "Hurricane Katrina 2005" (The Warning Hour)

> **DESIGN GATE ARTIFACT.** Owner signs off this design BEFORE any paid spend or bulk sourcing.
> Inserts (audio-carrying clips) each get individual owner confirmation before entering a render.
> Script built on `references/script-scaling.md` (the retention lattice) — cadences are per-minute
> invariants; runtime scales by acts, never by stretching beats.
> Research corpus: `references/ep6-katrina/` (facts-met-timeline.md, facts-engineering-aftermath.md,
> teardown-darkhorizon.md, comment-insights-darkhorizon.md, storymine-60minutes.md, footage-inventory.md).

## Spec
- **Channel:** The Warning Hour. **Slug:** `ep6-katrina-2005`.
- **Working title:** *The Flood They Rehearsed — New Orleans 2005*
  - alt A: *The Worst Engineering Disaster in American History — Katrina 2005* (ASCE-backed superlative)
  - alt B: *The Hurricane That Missed New Orleans — Katrina 2005*
- **Thumbnail concept:** real aerial of flooded New Orleans grid (NOAA NGS/FEMA PD), rooftop in
  frame, bold "KATRINA 2005" — NO AI thumbnail (competitor audience actively polices AI; top-comment backlash documented).
- **Runtime target: 30 min (owner order).** Word budget planning figure: 30 × 0.9 × 158 ≈ **4,270
  words**; **probe-TTS 2 segments before locking** (ep5 measured blend 145 → likely ~3,900; adjust
  after probe). Current draft ≈ 4,100 words.
- **Voice:** pocket-TTS Pharaoh clone (config `external.*`; verify voice-ref md5 before produce).
  Narration below is readable-form; TTS pass mechanically converts (numbers/dates spelled out,
  <24-word sentences, no paired dashes).
- **Positioning vs the Dark Horizon ref (1.74M views, 19 min):** they told the levee story thin and
  skipped Mississippi entirely (their #1 audience complaint, verbatim in comments). We go deeper on
  the engineering receipts (sheet-pile shortfall, IPET's 50-breach anatomy), give Mississippi a real
  act, bank Hurricane Pam for a final-act reveal instead of spending it early, and close warm.
- **Info:fluff ≈ 75:25.** Spice = clarifying footnotes only (football-field-class comparisons, the
  Ricks backstory, "before the storm / after the storm" local idiom).
- **Net-info-gain (facts no competitor video carries):** ① the 7-foot sheet-pile shortfall at 17th
  Street + the Corps misreading its own E-99 load test; ② Hurricane Pam's eerily exact rehearsal 13
  months early, never funded to completion; ③ Superdome myth vs record (200 rumored bodies → 6
  verified deaths); ④ barge ING 4727 myth-bust (drifted through an already-open breach); ⑤ the 2023
  NOAA reanalysis death toll (1,392, scoped) vs the folk "1,800+".

## Hook contract compliance (DESIGN.md + owner lock 2026-08-15: Option A "The Rescue")
- [x] **NO black start — frame one is mid-action**: USCG helicopter hoist over flooded rooftops,
  rotor audio already live. (PD-FED spine; see sourcing note S-1 below — hoist VIDEO is the one
  must-find asset; photo-set fallback exists.)
- [x] Intelligible high-stakes **anchor line by ~2.5s**: real 911 attic call (INS-01).
- [x] **Date/place card inside the first second**: "NEW ORLEANS · AUGUST 29, 2005" — doubles as the
  first date match-cut popup (device plants in second one).
- [x] Every cut lands **on an audio event**; inserts end on their complete statement.
- [x] **Sonic spine**: rotor + water-lap bed builds under the whole hook, ducks under the caller,
  swell mounts into the turn, riser peaks exactly WITH the loop line's last word, dies into the void.
- [x] **2.5s VOID at hook END only** (the punctuation before the narrator enters).
- [x] Misdirection beat uses the VERIFIED artifact: NPR "Day to Day" 30 Aug 2005, "New Orleans
  Spared the Worst, But Still Reeling" (verbatim, dated, self-contradicting in its own segment).
  The folk phrase "dodged the bullet" is UNVERIFIABLE same-day — never scripted as a quote.

## Insert-transcription rule (binding)
Every `insert` is transcribed in full (faster-whisper) BEFORE cut selection. Cut chosen at the
transcript's action/emotion peak; excerpt + transcript path logged here AND in provenance.csv.

## Sourcing & licensing rails (binding — from footage-inventory.md, 75 catalogued sources)
- **Spine = federal PD (37 sources):** USCG/DVIDS rescue ops, FEMA photo library (Booher/Bahamonde),
  National Guard/DoD, NOAA GOES loops + NGS post-storm aerials, USGS before/after pairs
  (Gulfport/Biloxi/Waveland), NHC advisories, White House archive pressers. Un-claimable.
- **S-1 (hook-critical must-find):** USCG hoist VIDEO for frame one. Inventory has the photo set
  (#5, PO2 Shawn Beaty HH-60 crew Aug 30) and Guard heli video (#6); bulk-sourcing runs a logged-in
  DVIDS sweep + archive.org pass for USCG rescue reels. Fallbacks: National Guard Blackhawk rescue
  footage (PD), then a claim-class network rescue pull (short, narrated-over).
- **WWL-TV continuous coverage, 307 raw files on archive.org (#38)** — the broadcast-rehook spine.
  Claim-class: short varied cuts, transcribed first, graded, credited, never the same cut twice.
- **911 audio:** CBS "Voices in the Storm" 2015 release (#46) incl. the Dubreuil St attic-trapped
  caller — the hook anchor candidate. Claim-class via CBS's release; verification pass checks
  whether the underlying NOPD recordings are obtainable as government records (structural
  immunity); else it runs claim-budgeted. Raw Broadcastify-class scanner rips stay HELD (#85).
- **C-SPAN-produced hearing coverage = claim-class-or-avoid** (#52–56); prefer the White House
  videoconference transcript/footage (#34, PD-FED) and Democracy Now's Dec 9 2005 hearing coverage
  (#59, verify reuse terms) for testimony beats.
- **Strike-class, DO NOT USE:** amateur archive.org captures with no license path (#83), y2mate
  rips (#84), scanner rips (#85). Independent/private footage never without license.
- **AI b-roll: effectively ZERO this episode** (owner gate item). The competitor's audience
  actively punishes AI Katrina footage; the real PD pool is the deepest of any US disaster. Only
  candidate gap: a dark non-identifiable attic interior for the 911 beat — proposal is to cover it
  with the real rooftop/axe-marks stills instead. If the owner wants the AI dramatization anyway,
  it's one DeAPI still, railguarded.
- Every sourced file → provenance.csv row (full URLs, never elided); re-read the row before wiring.
- **Real human portraits (verdicts before compose):** all memorial/vignette faces get per-person
  licensing verdicts at bulk sourcing; ≤4–5s dwell, once, then symbolic; NO child likenesses; no
  identifiable children in distress anywhere (Gretna/boat-rescue crowds framed wide or cropped).
- **Sensitive-thread rules:** Memorial Hospital (Dr. Pou) told as a CONTESTED legal question, both
  sides, grand-jury outcome stated only after independent verification; NO patient imagery. Gretna
  bridge told with both on-record perspectives, no adjudication. Nagin's suicide/jumper claims are
  single-source — not restated as fact. Superdome coverage leads with the verified record.

## Sourcing quota (owner-set 2026-08-15)
Catalogue 60–80 candidate sources ✅ (75 done, 27 assertion assets). Bulk-sourcing mounts ~45–55
distinct acquisitions; count SOURCES, not cuts; 2–3 candidates per key beat; assertion assets
(911 audio, radio, WWL pulls, pressers, front pages, testimony, before/after pairs) are their own
priority line. PySceneDetect splits the WWL reels; cuts spread across the episode, never bunched.

## Graphics to hand-author (compositions/g-*.html — GRAPHICS CONTRACT; 2–3 versions of the big two ★)
1. `g-iwall` ★★ — THE showpiece. I-wall failure mechanism: surge load → wall deflects → gap opens
   on the land side → water pressure drives to the base → weak marsh-clay layer shears → wall
   slides. Then the receipt: design drawing shows sheet piling to 17.5 ft below sea level; sonar
   found ~10 ft. Animated cross-section, ep2-g-met class, word-synced beats.
2. `g-bowl` ★ — why New Orleans floods: animated cross-section, river levee 25 ft, lake, canals
   reaching into the city like fingers, land sinking below sea level. Sets up everything.
3. `g-track` — Gulf track map Aug 23→29: category escalation stamps, the cone tightening on New
   Orleans, 56-hour lead-time counter. Real map plate (ep3-map-route-fit pattern).
4. `g-floodmap` — Aug 29–31 flood-spread: neighborhood-by-neighborhood fill, % counter rolling to
   80, depth callouts. Real city plate.
5. `g-surge-ms` — Mississippi wall-of-water map: 27.8 ft Pass Christian high-water mark against a
   3-story-house scale figure; 17–22 ft Gulfport→Pascagoula band.
6. `g-bulletin` — the Ricks bulletin types itself on screen (real verbatim text, teletype pacing,
   selective line reveals synced to narration).
7. `g-pam` — the reveal card: "HURRICANE PAM · JULY 2004" simulation vs reality side-by-side rows
   (predicted / happened), row-by-row word-synced.
8. `g-stat-toll` — scoped death-toll panel (1,392 · direct/indirect split · the elderly stat) —
   ep2 stat-panel anatomy, counter rolls fast then slows.
9. `g-stat-uscg` — the counter-story panel: 33,500 saved, 24,135 from rooftops and water.
10. `g-datepop` — **the date match-cut popup device (owner-requested):** one reusable style block
    (ep2 stamp anatomy: Arial Black on #8e2020, white, tracked; eyebrow month + big day numeral +
    optional time line, e.g. "AUG 29 · 6:10 AM"). Stamp-slam entry (fromTo scale 2.6→1, 0.35s,
    power4.in), dark backing chip, full slide/fade exit, holds ~2–3s. EVERY instance hand-placed on
    the words.json timestamp of the spoken date. ~14 instances (ledger below). A snippet, not a
    scene template.
11. `g-close` — signature closing card, match-cut to the channel name, episode number on card.

## Date match-cut popup ledger (instance ← spoken cue; timestamps filled from words.json at compose)
| # | Popup text | Cue (narration) | Act |
|---|---|---|---|
| D1 | AUG 29 · NEW ORLEANS | hook card (first second) | Hook |
| D2 | SEPT 1965 · HURRICANE BETSY | "nineteen sixty-five" | A1 |
| D3 | JUNE 2002 | "Washing Away" series | A1 |
| D4 | AUG 23 | depression forms | A2 |
| D5 | AUG 25 | Florida landfall | A2 |
| D6 | AUG 28 · 7:00 AM | Category 5 advisory | A2/A3 |
| D7 | AUG 28 · 10:11 AM | Ricks bulletin | A3 |
| D8 | AUG 28 · 11:00 AM | mandatory evacuation | A3 |
| D9 | AUG 28 · NOON | Superdome opens | A3 |
| D10 | AUG 29 · 6:10 AM | Buras landfall | A4 |
| D11 | AUG 29 · 8:54 AM | radar goes silent | A4 |
| D12 | AUG 30 | "spared the worst" / 80% | A4/A5 |
| D13 | AUG 31 | Convention Center crowds | A6 |
| D14 | SEPT 1 | Nagin radio outburst | A6 |
| D15 | SEPT 2 | "Brownie" / relief arrives | A6 |
| D16 | JULY 2004 (amber flashback variant) | Pam reveal | A7 |
| D17 | JUNE 2006 | Strock admission | A7 |
| D18 | MAY 2022 | new walls handed over | A7 |
Style note: one visual system; the day numeral advances like a stamp on a case file. Flashback
instances (D2, D3, D16) get the amber serif variant so past-tense reads instantly.

## Insert candidates (each owner-gated individually at sourcing; transcribe-before-cut)
| ID | What | Source | Class | Where |
|---|---|---|---|---|
| INS-01 | 911 attic call (Dubreuil St caller + operator Paula Massey) | CBS "Voices in the Storm" (#46) | claim-class (hunt NOPD original) | Hook anchor |
| INS-02 | NPR "Day to Day" pull: "New Orleans was spared the worst…" | npr.org 4823849 | claim-class (short) | Hook turn (alt: designed card + narration) |
| INS-03 | Nagin WWL radio outburst, Sept 1 | archive.org (#44) | claim-class | A6 |
| INS-04 | WWL-TV coverage moments (2–3 distinct cuts across acts) | archive.org #38 | claim-class | A3/A4/A5 rehooks |
| INS-05 | Bush "Again, Brownie, you're doing a heck of a job" | WH archive transcript + press-pool video (PD-FED) | PD-FED if WH feed | A6 |
| INS-06 | Survivor testimony line (Dec 2005 House hearing) | #59 Democracy Now (verify terms) / #34 WH VTC | verify | A7 |
| INS-07 | Honoré briefing beat | DVIDS sweep | PD-FED | A6 |

## LOOP TABLE (plant → pay; every act plants one and pays one)
| Loop | Line (plant) | Planted | Paid |
|---|---|---|---|
| L0 (episode) | "The hurricane missed. The city drowned anyway." | Hook | A7 (they rehearsed it and knew) |
| L1 | "The drawings said one thing. The ground held another." | A1 | A5 (sheet-pile sonar reveal) |
| L2 | "The forecast was nearly perfect. That is what makes this hard to hear." | A2 | A3/A4 (56 hours, used and wasted) |
| L3 | "They called it the refuge of last resort." | A3 | A6 (what the last resort became) |
| L4 | "At eight fifty-four, the radar near the city went silent." | A4 | A5 (what happened under the silence) |
| L5 | "Remember the water in the Lower Ninth. We will come back to who paid for it." | A5 | A7 (sovereign immunity: no one) |
| L6 | "Someone had rehearsed this exact disaster." | A6 | A7 (Hurricane Pam) |

## ACT BRIEFS (script-scaling format)

> **HOOK — The Rescue · ~70s · ~60 narration words + inserts**
> **Job:** unskippable cold open; plant L0; establish the date-popup device.
> **In / out:** frame one mid-hoist, rotor live → 2.5s VOID.
> **Loops:** plants L0.
> **Rehooks:** 911 call (~2s), breach-water hard cut (~8s), NPR "spared" pull (~14s), loop line (~26s).
> **Tempo + emotion:** fast attack, cuts on audio events; banks dread, not grief.

> **ACT 1 — A City Below the Sea · ~3.5 min · ~480 words**
> **Job:** the bowl + the walls + forty years of warnings. Viewer must be able to SEE why this city
> floods before the storm exists. Betsy 1965 parallel (competitor gap).
> **In / out:** narrator enters over the bowl graphic → blackout.
> **Loops:** plants L1 · pays hook's implicit "how does a city drown" question.
> **Rehooks:** g-bowl reveal, Betsy archival beat (D2), "Washing Away" pull-quote card (D3).
> **Tempo:** medium, explainer pace with two spikes; banks little emotion (info act).

> **ACT 2 — The Storm · ~3.5 min · ~480 words**
> **Job:** Aug 23–28 chronology; the engine of the thing (warm Gulf); Cat 5 902 mb peak; the
> forecast that was nearly perfect. March of date popups begins (D4–D6).
> **In / out:** satellite loop mid-spin → blackout.
> **Loops:** plants L2 · pays none (early build act — the exception the lattice allows once).
> **Rehooks:** GOES loop escalation, FL landfall broadcast beat, Cat-5 advisory text slam.
> **Tempo:** accelerating wave; cuts tighten as the storm grows.

> **ACT 3 — The Warning · ~4 min · ~560 words**
> **Job:** Aug 27–28. The Ricks bulletin typed on screen (verbatim, PD). Mandatory evac at 11 AM,
> contraflow, who could not leave, Superdome opens at noon. 56 hours of lead time made concrete.
> **In / out:** quiet Sunday-morning city b-roll → bulletin teletype → blackout on "refuge of last resort."
> **Loops:** plants L3 · pays L2 (the warning WAS delivered).
> **Rehooks:** g-bulletin typing (the act's spine), WWL evac-coverage pull, D7–D9 popups.
> **Tempo:** slow dread build; the bulletin lines land one at a time.

> **ACT 4 — Landfall · ~4.5 min · ~620 words**
> **Job:** Aug 29, hour by hour. Buras 6:10 AM. Then MISSISSIPPI GETS ITS DUE: Pass Christian 27.8
> ft, Waveland/Bay St. Louis ground zero, 172 dead in Mississippi (the competitor's loudest gap —
> our differentiator). Radar goes silent 8:54. Evening: the country hears "spared the worst" while
> the bowl is already filling.
> **In / out:** landfall wind/rain mid-action → CNN-homepage/NPR irony beat → blackout.
> **Loops:** plants L4 · pays L2 (forecast verified almost to the mile).
> **Rehooks:** D10/D11 popups, g-surge-ms wall-of-water, WWL landfall pull, USGS before/after pair.
> **Tempo:** fastest act; pacing wave peaks; MS segment gets its own mini-arc (hook-in → erase → toll).

> **ACT 5 — The Breaches · ~4.5 min · ~620 words**
> **Job:** the engineering act. Morning-of timeline (London Ave, Industrial Canal 7:45 "explosive
> sound", 17th St), g-iwall mechanism, the sheet-pile receipt (17.5 designed vs ~10 found), IPET's
> 50-breach anatomy (4 below design load), barge myth-bust, 80% flooded by Aug 31.
> **In / out:** black water through a wall mid-flow → g-floodmap fill to 80% → blackout.
> **Loops:** pays L1 and L4 · plants L5.
> **Rehooks:** g-iwall reveals, sonar-depth stamp, ING 4727 myth-bust beat, D12.
> **Tempo:** methodical, forensic; counters and diagrams; the act where info density IS the drama.

> **ACT 6 — The Week After · ~4.5 min · ~620 words**
> **Job:** Superdome (10–12k at landfall → 23k peak; then the myth: 200 rumored bodies, 6 verified
> deaths), Convention Center (crowds Aug 31, officials "learn" Sept 1–2, relief Sept 2), comms
> collapse (3M lines, 1,477 towers, NOPD dark), Nagin outburst, USCG counter-story (33,500),
> "Brownie" beat, Gretna bridge (both perspectives, 60-Minutes-sourced, verified subset only).
> **In / out:** Superdome aerial mid-orbit → USCG hoist echo (different cut than hook) → blackout.
> **Loops:** pays L3 · plants L6.
> **Rehooks:** INS-03 Nagin audio, g-stat-uscg counter, D13–D15 popups, front-page stills.
> **Tempo:** alternating chaos (fast) and institutional stillness (slow); banks anger.

> **ACT 7 — The Reckoning + The People · ~4.5 min · ~630 words**
> **Job:** Pam reveal (g-pam: July 2004, 300 officials, predicted 60,000+ dead — 13 months early,
> follow-up never funded). Strock's June 2006 admission (first such in Corps history). ASCE: worst
> engineering catastrophe in US history. Sovereign immunity: no one ever paid (pays L5). The
> people: elderly stat (nearly half of Louisiana's dead were 75 or older), scoped 1,392 toll,
> Charity rooftop vignette + one hearing-testimony voice. $14.5B new walls, 2022. Warm signature
> close on the channel card.
> **In / out:** amber flashback popup (D16) mid-reveal → toll panel → close card. No recap.
> **Loops:** pays L6, L5, L0.
> **Tempo + emotion:** descending stakes into stillness; THE emotion bank of the episode; ends warm,
> preparedness-forward, never fearmongering.

---

# SCRIPT (typed segments; prose = readable-form, TTS pass converts; [verify] markers must be ZERO before TTS)

Legend: `narration` = own TTS wav · `hold` = no voice, ambience only · `insert` = clip's own audio
(owner-gated) · `graphic` = g-* composition, VO optional. Visual intent names candidate sources by
inventory # (footage-inventory.md). Every hold >8s carries its reason.

## HOOK — The Rescue (~0:00–1:10)

**h1-s1 · insert (INS-01 anchor under hoist video)** — FRAME ONE: USCG hoist over flooded rooftops,
already mid-lift, rotor audio live (S-1 must-find video; fallback #6 Guard Blackhawk). Date/place
card D1 "NEW ORLEANS · AUGUST 29, 2005" inside first second. At ~2.0s the 911 call cuts through
(Dubreuil St attic caller, #46; exact excerpt chosen from transcript at the emotion peak; ends on
her complete statement). Sonic spine: rotor + water-lap bed under everything.

**h1-s2 · hold (~3s)** — hard cut ON the caller's line ending → black floodwater pouring through a
breached wall (WWL #38 or PD aerial of 17th St gap; graded). Bed swells. Reason: the image IS the
sentence; no voice competes with it.

**h1-s3 · insert (INS-02, ~5s)** — radio-static bridge, then the NPR pull, aired the next morning:
*"New Orleans was spared the worst of Hurricane Katrina…"* (alt if pull unusable: designed
headline card, narrator silent). Riser starts under it.

**h1-s4 · narration (~48 words)**
That report aired the morning after landfall. It was wrong before it was broadcast. By the time
the country heard it, the water was already inside the city, and it was still rising.
The hurricane missed New Orleans. The city drowned anyway. *(riser peaks and ends WITH "anyway")*

**h1-s5 · hold — THE VOID (2.5s)** — hard cut to black. Spine dies. Silence. *(the hook's punctuation)*

## ACT 1 — A City Below the Sea (~1:10–4:40, ~470 words)

**a1-s1 · graphic g-bowl + VO (~95 words)**
New Orleans is shaped like a bowl. The Mississippi River runs along one rim. Lake Pontchartrain
sits on the other. And most of the city lies between them, below the level of both. Whole
neighborhoods sit below the level of the sea. Rain cannot drain out of this city. Every
drop has to be pumped up and over the rim. People here do not live beside the water. They live
inside it, behind walls, the way a ship's crew lives behind a hull.
*(g-bowl beats: rim labels → below-sea shading → pump arrows → hull line. New info every 2-3s.)*

**a1-s2 · narration over levee/canal aerials (#16, #25) (~75 words)**
The hull is real. Earthen levees and concrete floodwalls wrap the city, hundreds of miles of them.
And cut through that shield run drainage canals. Open channels of water reaching from the lake
deep into the city's neighborhoods, each lined with its own thin concrete wall. The strength of
the whole city comes down to the weakest wall on the weakest canal. So. Who checks the walls?
*(micro-loop: "who checks the walls")*

**a1-s3 · narration, Betsy archival stills (#16 era-verified) + D2 popup (~85 words)**
New Orleans already knew what failure felt like. In September of 1965, Hurricane Betsy pushed the
lake into these same streets. People drowned in their attics in the Lower Ninth Ward. Congress
moved within weeks. It ordered the Army Corps of Engineers to build a shield around the city,
strong enough for the worst storm the region was ever likely to see. The plan was supposed to
take about thirteen years to finish. [verify: 13-year original estimate — GAO-06-244T]

**a1-s4 · graphic (timeline bar 1965→2005) + VO (~70 words)**
Forty years later, the shield was still not finished. Government auditors put it at roughly
sixty-five percent complete. And the finished parts had a problem of their own. The ground under
New Orleans sinks a little every year. Walls built to a safe height in one decade quietly dropped
below it in the next. The fence was unfinished, and parts of it were shrinking.

**a1-s5 · narration, "Washing Away" front-page card + D3 popup (~95 words)**
None of this was secret. In June of 2002, the city's own newspaper ran a front-page warning series
called Washing Away. Its first sentence: "It's only a matter of time before South Louisiana takes
a direct hit from a major hurricane." The reporters printed a likely death toll. Somewhere between
twenty-five thousand and one hundred thousand people. That landed on driveways and kitchen tables
across New Orleans, three years before Katrina had a name. The warning was not missing. It was
delivered to the door.
*(pull-quote card: real T-P front page #61/#62, quote line highlighted on its spoken word)*

**a1-s6 · narration (~50 words) — L1 plant**
And buried in the engineering files sat one more detail. The canal floodwalls stood on sheets of
steel, driven down to anchor them in the soft ground. How deep that steel actually went, and how
deep the drawings said it went, would turn out to be two different numbers. Hold that thought.

**a1-s7 · hold (~2.5s)** — slow aerial of the city at dusk, bed low. Reason: let L1 land before the
act turn. → **BLACKOUT (2.5s)**

## ACT 2 — The Storm (~4:40–8:10, ~480 words)

**a2-s1 · graphic g-track opens mid-motion + VO + D4 popup (~80 words)**
Far to the east, over the warm shallows of the Bahamas, satellites were watching a
cluster of thunderstorms trying to become something. On August 23rd, 2005, it became the twelfth
tropical depression of the season. A day later it had a name. Katrina. Nobody in Louisiana looked
up. Storms are born out there every August. Almost all of them die as names on a list.

**a2-s2 · narration, FL landfall WWL/network beat (#42, short) + D5 popup (~70 words)**
This one did not. On August 25th, Katrina crossed South Florida as a Category 1, with winds near
eighty miles per hour. Six people died there. Then the storm slid off the coast, into the Gulf of
Mexico. And the Gulf, that week, was exactly what a hurricane wants. Hot water, running deep.

**a2-s3 · graphic (engine diagram inside g-track) + VO (~85 words)**
A hurricane is an engine. Warm seawater is its fuel. Most storms churn up cold water from below
and starve themselves. But Katrina crossed a current where the warmth runs deep, so the engine
never starved. [verify: Loop Current crossing — NHC TCR discussion] Over two days it went from a
Category 1 to a Category 3, then a Category 4. And on the morning of August 28th, in less than
twelve hours, it became a Category 5.
*(GOES loop #17/#20 escalating behind the diagram; D6 popup on "August 28th")*

**a2-s4 · graphic stat slam + satellite loop (~90 words)**
At that point the numbers stop sounding like weather. Sustained winds of one hundred seventy-three
miles per hour. A central pressure of nine hundred two millibars, among the lowest ever measured
in an Atlantic hurricane. Tropical-storm winds reached more than two hundred miles out from the eye. Put
that circle over a map and it swallows the whole northern Gulf Coast at once. This was no longer a
question of whether someone would be hit. Everyone in the circle already was.
*(stats slam ON their spoken words, ep2-style; no pre-reveal)*

**a2-s5 · narration over track-cone tightening (~105 words) — L2 plant**
And here is the part of this story nobody expects. The forecast was nearly perfect. Two and a half
days before landfall, the Hurricane Center drew its line to the Louisiana coast. Katrina followed
that line almost exactly. In the final two days, every new forecast lined up almost directly on
top of the storm's actual path. Emergency managers had fifty-six hours of clear, correct
warning. More than two full days. Most disasters begin with a surprise. This one began with a
bullseye. The forecast was nearly perfect. Remember that. It is what makes everything that follows
hard to hear.
*(g-track: 56-hour counter ticks up as cone tightens)*

**a2-s6 · hold (~2.5s)** — satellite eye filling the frame, bed drops to a low pulse. Reason: scale
lands in silence. → **BLACKOUT (2.5s)**

## ACT 3 — The Warning (~8:10–12:10, ~560 words)

**a3-s1 · narration, quiet Sunday-morning New Orleans b-roll (#38 pre-storm WWL, graded) (~65 words)**
Sunday, August 28th. A hot, still morning in New Orleans. Church bells, coffee, a normal weekend
sky. Out in the Gulf, more than four hundred miles of hurricane were turning toward the city.
Everything that needed to happen now had about twenty-four hours to happen in.

**a3-s2 · graphic (NHC advisory text #31) + VO + D6 continuity (~55 words)**
At seven that morning, the Hurricane Center's advisory used a phrase forecasters almost never
type. "Potentially catastrophic Category 5 hurricane." Not strong. Not dangerous. Catastrophic,
in the official forecast, in capital letters. In the forecast office across the lake in Slidell,
one man read the data and decided plain language was not enough.

**a3-s3 · graphic g-bulletin (teletype) + VO + D7 popup (~120 words)**
His name was Robert Ricks. He grew up in the Ninth Ward. His family had lived through Betsy. At
eleven minutes past ten, he sent a bulletin that veterans of the Weather Service still talk about.
It said, in plain block letters: devastating damage expected. A most powerful hurricane with
unprecedented strength. Most of the area will be uninhabitable for weeks, perhaps longer. Water
shortages will make human suffering incredible by modern standards. Persons exposed to the winds
will face certain death if struck. He was not exaggerating. He said later he had been editing
himself down, trying to find things to take out. Every line you just heard is real, and every line
came true.
*(g-bulletin: real verbatim lines type on their spoken words; the rest of the product scrolls faint)*

**a3-s4 · insert INS-04a (WWL evac coverage, short) + narration + D8 popup (~90 words)**
One hour later, at eleven in the morning, Mayor Ray Nagin stood at a podium and did something no
New Orleans mayor had ever done. He ordered a mandatory evacuation of the entire city. Nineteen
hours before landfall. On the highways, every lane was already running one direction. Out. About
one point two million people left south Louisiana in a day and a half, roughly ninety percent of
the people at risk. It was, by the numbers, one of the most successful evacuations in
American history.

**a3-s5 · narration, evacuee/traffic stills (#14 FEMA) (~90 words)**
By the numbers. But a number was missing from it. Tens of thousands of people were still in the
bowl. Some had no car. Some had no money, at the end of the month, for gas or a motel. Some were
too old or too sick to move, or caring for someone who was. And some had ridden out Betsy and
Camille and simply did not believe the water would come for them this time. The city knew these
people existed. The plan for them fit in one word. Superdome.

**a3-s6 · narration + Superdome exterior lines (#2, #14) + D9 popup (~85 words) — L3 plant**
At noon on Sunday, the city opened the Superdome as what officials called a refuge of last
resort. Not a shelter. A refuge of last resort, a place to survive the wind and nothing more. By the
time the storm arrived, more than ten thousand people were inside. They had waited in lines that
wrapped around the building,
carrying garbage bags of clothes. National Guard soldiers searched them at the doors. Remember
that phrase. Refuge of last resort. We are going to find out exactly what it meant.

**a3-s7 · hold (~3s)** — dusk shot of the Dome, city lights, bed to low drone. Reason: the act's
dread must settle before landfall. → **BLACKOUT (2.5s)**

## ACT 4 — Landfall (~12:10–16:40, ~620 words)

**a4-s1 · insert INS-04b (WWL landfall-morning coverage, short) then narration + D10 popup (~85 words)**
Six ten AM. Monday, August 29th. Katrina came ashore at Buras, Louisiana, a fishing town at the
mouth of the Mississippi. The storm had weakened overnight, from a Category 5 to a Category 3.
Winds near one hundred twenty-seven miles per hour. In Buras, the water simply removed the town.
And then, for the next three hours, the eye of the storm did New Orleans a favor. It turned
slightly east. The city would not take the direct hit. Mississippi would.

**a4-s2 · narration + radar frames (KLIX, timestamps honest) + D11 popup (~80 words) — L4 plant**
The radar station at Slidell tracked the eyewall as it came on. At eight forty-two, forecasters
warned of gusts over one hundred miles per hour crossing the lake. Then, at eight fifty-four in
the morning, the radar near the city went silent. [verify: KLIX last transmitted scan 1354 UTC —
AMS/NCDC, MED] The eyewall was passing directly over the antenna. From that moment, through the
worst hours of the storm, the picture went dark. Remember the silence. Things happened inside it.

**a4-s3 · graphic g-surge-ms + VO (~110 words)**
At nine forty-five the center crossed the coast again, at the Louisiana-Mississippi line. And here
the Gulf of Mexico stood up and walked onto the land. At Pass Christian, Mississippi, the storm
surge reached twenty-seven point eight feet. That is seawater the height of a three-story
building, moving with the weight of an ocean behind it. Waveland. Bay St. Louis. Pass Christian.
Long Beach. Gulfport. Biloxi. Along miles of coast, the first three or four blocks of town were
not damaged. They were removed. Slabs stayed. Addresses stayed. Everything above the slab went
inland or out to sea.
*(g-surge-ms: surge bar grows against house silhouette; town names stamp along the coast map)*

**a4-s4 · narration, USGS before/after pairs (#28, #29) (~85 words)**
One hundred seventy-two people died in Mississippi that morning. Whole retirement communities,
gone between breakfast and noon. If you lived on that coast, you will already know something
strange about this story. The country barely remembers your part of it. Katrina made landfall on
Mississippi. Mississippi took the storm. New Orleans, thirty-five miles from the center, [verify: 35-mi margin, NHC Adv 27 primary pull]
took something else. Something slower, and in its own way, worse. Because while the Gulf was erasing
Waveland, the phones inside New Orleans had already started ringing.
*(before/after wipes ON the town names; micro-loop close)*

**a4-s5 · narration, WWL/CNN evening irony + D12 popup (~130 words)**
By Monday evening, the storm was inland and dying, and a story was forming on the news wires. New
Orleans had been spared the worst. The morning after landfall, national radio said exactly that.
Spared the worst. And measured in wind, it was even true. But the same newscast, in the same
breath, reported two levee breaches already pouring lake water into the city. Nobody put the two
sentences together. On screens across America, the relief headline and the drowning city ran side
by side, and the relief headline won the evening. Inside the bowl there was no electricity, no
radar, and almost no working phones. The one thing rising faster than the water was the distance
between what the country believed and what was true.
*(visual: real Wayback CNN homepage capture, 5:55 PM Aug 29, screenshot honest; then black water at night)*

**a4-s6 · hold (~3s)** — black water sliding through a residential street at night, bed = water +
distant alarms. Reason: the irony must curdle before the forensic act. → **BLACKOUT (2.5s)**

## ACT 5 — The Breaches (~16:40–21:10, ~620 words)

**a5-s1 · narration, breach aerials (#25 NOAA NGS) (~90 words)**
Here is what was happening inside the radar silence. Katrina's surge did not just press on the
lakefront. It pushed up the drainage canals, those open channels reaching into the city's heart,
and it pressed on the thin walls beside them. Before seven that morning, a floodwall on the London
Avenue Canal gave way. [verify: London Ave east breach ~6-7 AM timing — MED source] Around seven
forty-five, people near the Industrial Canal heard something like an explosion. A wall section
collapsed, and a gap nearly a thousand feet wide opened into the Lower Ninth Ward.

**a5-s2 · narration, Lower Ninth imagery + barge beat (~85 words)**
The Lower Ninth went under in minutes. Houses floated off their slabs with families inside. A
massive steel barge washed through the gap and came to rest on top of a
neighborhood. For years people said the barge caused the breach. Engineers later proved it did
not. The wall failed first, on its own, and the barge simply drifted through the wound. Keep that
distinction. This episode keeps coming back to it. Walls that failed on their own.

**a5-s3 · graphic g-iwall ★ + VO (~150 words)**
And at the 17th Street Canal, the biggest drainage canal in the city, the wall did something the
engineering textbooks said it must never do. The water that morning reached about ten and a half
feet up a wall built to hold fourteen. It never got near the top. But the pressure leaned the
concrete outward, just slightly, and that lean opened a thin gap between the wall and the soil
holding it. Water poured down into the gap, and now the pressure was not pushing on the wall
anymore. It was pushing on the ground under it. Beneath that levee lay a soft layer of old swamp
clay. The clay sheared, the way mud slides off a shovel, and the wall rode the ground sideways
into the neighborhood behind it. It did not overflow. It moved. A floodwall has no halfway.
It holds, or it is gone.
*(g-iwall v1-v3 to be authored; beats word-synced: load → lean → gap → clay shear → slide)*

**a5-s4 · graphic g-iwall part 2 (the receipt) + VO (~105 words) — L1 pay**
Months later, engineers ran sonar along the wreckage, looking for the steel sheets that were
supposed to anchor that wall deep in the ground. The design drawings called for steel driven
seventeen and a half feet below sea level. The sonar found it stopped at about ten. Seven feet of
promised steel that was never there. And the trail led back to a load test the Corps of Engineers
had run on its own wall design in the nineteen eighties, a test whose results, read correctly,
said the steel needed to go far deeper in soil this soft. [verify: E-99 depth-implication figures
before quoting numbers] The drawings said one thing. The ground held another.

**a5-s5 · graphic g-floodmap + VO + stat beats (~110 words)**
By the end of Monday the city had not one broken wall but dozens of failure points. The official
investigation would eventually count fifty breaches across the region's defenses. Forty-six of
them were overwhelmed the way you would expect, water pouring over the top and chewing the levee
apart from behind. Four were not. Four walls, including the 17th Street and London Avenue canals,
failed below the level they were designed to hold. The system did not lose to a storm bigger than
its design. Parts of it lost to a storm smaller than its promise. Water kept flowing for two more
days. By Wednesday, eighty percent of New Orleans was under water. [verify: 80%-by-Aug-31 timing
to a primary cite]
*(g-floodmap: neighborhoods fill hour by hour; counter rolls to 80; depth callouts to 15 ft)*

**a5-s6 · narration (~55 words) — L5 plant**
Stand in the flooded Lower Ninth for one more second before we move on. Every ruined block you are
looking at now traces back to engineering decisions with names and dates attached. Hold one
question until the end of this story. For all of this, who paid? The answer is coming, and you
will not like it.

**a5-s7 · hold (~2.5s)** — still water over rooftops at dawn, bed thins. → **BLACKOUT (2.5s)**

## ACT 6 — The Week After (~21:10–25:40, ~620 words)

**a6-s1 · narration, Superdome aerial mid-orbit (#2, #14) (~85 words) — L3 pay begins**
Remember the phrase. Refuge of last resort. By midweek, the building held around twenty-three
thousand people. The storm had peeled sheets of the roof away over their heads. Then the power
died, and the plumbing died, and the air conditioning died, in a domed building in Louisiana in
August. No working toilets for a crowd the size of a small city. Food and water ran to rations.
The refuge of last resort was now the largest stranded population in America.

**a6-s2 · narration, front pages + crowd stills (wide, no identifiable children) (~95 words)**
And then the stories started. Rumors moved through the crowd and onto the airwaves. Murders in
the dark. Bodies stacked in the freezers, as many as two hundred. Officials repeated the rumors on
national television, and for a week, America believed the Superdome had become a war zone. Months
later, investigators counted what actually happened there. Six people died in that building. Four
from illness. One overdose. One suicide. No murders. The truth was bad enough. Twenty-three
thousand people abandoned in the heat for nearly a week. The myth just pointed the shame at the
wrong people.

**a6-s3 · narration + Convention Center beat + D13 popup (~90 words)**
A mile away, the story the country should have been told was assembling itself. On Wednesday,
police began directing people to the Convention Center, telling them buses would come. As many as
twenty-five thousand gathered there. There was no food. No water. No guards. No buses. And for two
days, the officials running the federal response said, on camera, that they were only just
learning those people existed. Reporters were broadcasting live from the building. The government
said it did not know. Both of those sentences were true at the same time.

**a6-s4 · narration, comms-collapse beat (~75 words)**
How does a government lose twenty-five thousand people in its own city? Like this. The storm took
out three million phone lines and nearly fifteen hundred cell towers. Police radios in New Orleans
went dark. City Hall was an island. For days, the people running
the rescue could not reliably talk to each other, and information moved at the speed of rumor.
The country watched it live. The responders could not.

**a6-s5 · insert INS-03 (Nagin WWL outburst, transcript-cut) + D14 popup + narration (~55 words)**
On Thursday night, the mayor went on the radio and stopped being polite. *(insert: the cut lands on
his complete sentence; excerpt + transcript path logged at sourcing)* Whatever else history says
about Ray Nagin, that night he said what the whole bowl was thinking.

**a6-s6 · graphic g-stat-uscg + rescue footage (S-1 pool, different cuts than hook) (~95 words)**
And yet, in the same city, in the same week, one part of the response worked like a machine. The
Coast Guard started flying before the wind stopped. Helicopter crews hoisted people off rooftops
one at a time, hour after hour, day and night, for a week. Count what they did. Thirty-three
thousand five hundred people saved. Twenty-four thousand of them lifted straight out of the water
and off the roofs. The system did not fail because everyone failed. It failed at the top, while
the people at the bottom of it kept working.

**a6-s7 · narration, Gretna bridge beat (wide framing) (~70 words)**
The week's ugliest hour came on a bridge. Thousands tried to walk out of the drowned city, over
the river to the dry suburb of Gretna. Police from that suburb met the crowd at the crest and
fired shotguns over their heads. Gretna says it had no power, no shelter, and no choice. The
people on the bridge, most of them Black, heard something else in it. That argument has never
ended.

**a6-s8 · insert INS-05 (Bush "Brownie" — WH pool) + D15 popup + narration (~55 words) — L6 plant**
On Friday, the president stood beside his FEMA director and praised him. *(insert lands on the
sentence)* Ten days later, that director resigned. And in the files of his own agency sat a
document that turns this whole story from a tragedy into something harder to forgive. Because
someone had rehearsed this exact disaster.

**a6-s9 · hold (~2.5s)** — helicopter silhouette against sunset over water. → **BLACKOUT (2.5s)**

## ACT 7 — The Reckoning + The People (~25:40–30:00, ~630 words)

**a7-s1 · graphic g-pam + D16 amber popup + VO (~135 words) — L6 pay**
Thirteen months before Katrina, in July of 2004, about three hundred emergency officials from
every level of government met in Baton Rouge for a week-long exercise. FEMA paid for it. On their
screens was a fictional hurricane aimed at New Orleans. They named it Pam. Pam was a Category 3.
Its simulated surge topped the levees and put the city under water. The planners' projections:
more than a million people evacuated. Half a million buildings destroyed. And a death toll over
sixty thousand. The exercise predicted the overwhelmed shelters. It predicted evacuees stranded on
the highways. It predicted hospitals losing power with patients inside. The plan to fix all of it
was supposed to come next, in follow-up sessions. The follow-up was never finished. The money ran
out. Thirteen months later, the real storm arrived.
*(g-pam rows: PREDICTED / HAPPENED, revealed pair by pair on the spoken words)*

**a7-s2 · narration + Strock presser still + D17 popup (~90 words) — L0 pay begins**
So no one gets to call this a surprise. In June of 2006, the commander of the Army Corps of
Engineers stood in front of cameras and said something no one in his position had ever said. This
was the first time the Corps had to stand up and admit a catastrophic failure of one of its own
projects. The engineers' professional association went further. It called the flooding of New
Orleans the worst engineering catastrophe in the history of the United States. Not the worst
storm. The worst engineering failure.

**a7-s3 · narration (~85 words) — L5 pay**
Now the question from the Lower Ninth. Who paid? Here is the answer. A law from 1928 makes the
federal government immune from lawsuits over flood-control works, no matter what. The courts
looked at walls that fell below their own design load, at admissions from the builders themselves,
and ruled that not one dollar of damages could be collected. One judge found a way through, on one
channel, for four families. A higher court took even that away. For the drowning of a major
American city, the legal price paid was zero.

**a7-s4 · graphic g-stat-toll + VO (~90 words)**
The human price was not zero. The official count, after years of study, stands at one thousand
three hundred ninety-two lives, taking the storm and its aftermath together, across the Gulf
states. Louisiana buried the most. And Louisiana's own records show exactly who the water took.
Four out of ten of its dead drowned. Nearly half were seventy-five or older. The people who could not
climb to an attic. The people who stayed because leaving was harder for them than for anyone
else. The flood found the oldest people in the bowl, and it kept them.
*(counter rolls fast, slows into 1,392; secondary rows appear after the landing)*

**a7-s5 · narration, vignette (Charity rooftop) (~85 words)**
One of them died on a hospital roof. At Charity Hospital, doctors moved the whole emergency room
upstairs by flashlight and hand-pumped air into patients for days. One elderly woman lay on the
helipad, waiting for a helicopter, her husband beside her, fanning her in the heat. She died on
the roof, waiting. The doctor who told her story afterward said he did not know where her husband
had gone. He did not know if the man even knew she was dead.
*(visual: Charity exterior + helipad aerial, symbolic; no patient imagery; attribution chip
"account: Charity Hospital physician, CBS interview, Sept 2005")* [verify: physician name from
original CBS credits before any name is shown]

**a7-s6 · narration + city-return imagery (~70 words)**
New Orleans lost more than half its people in the year after the storm, and many never came
back. [verify: 484,674 to 230,172, Data Center compilation of Census data] The ones who did divide their lives with a phrase you will hear in every neighborhood.
Before the storm. After the storm. The city has new walls now. Fourteen and a half billion
dollars of them, finished in 2022. *(D18 popup)* They are stronger, deeper, and honestly built.
And they are rated for a storm smaller than Katrina.
[verify: HSDRRS 100-year design vs Katrina recurrence — phrase precisely or cut final sentence]

**a7-s7 · graphic g-close + VO (~75 words) — signature close**
Disasters do not ask permission. But they do send warnings. New Orleans got its warnings in
writing, three years early, on the front page. It got a full-dress rehearsal, one year early,
with the death toll attached. The warnings were all there. What was missing was anyone required
to act on them. Learn what your warnings sound like, and decide, now, what you will do when one
arrives. This was The Warning Hour. Episode six.
*(match-cut channel card on "The Warning Hour"; card does not sit; episode number on card)*

---

## Word count & pacing check (draft)
Hook ~48 · A1 ~470 · A2 ~485 · A3 ~565 · A4 ~620 · A5 ~595 · A6 ~620 · A7 ~630 → **~4,035 words**
≈ 27.8 min narration at 145 wpm + inserts/holds/blackouts ≈ **30 min runtime.** Probe-TTS 2
segments (one long-sentence, one punchy) before locking; adjust ±10% by trimming A2/A6 first.

## Open [verify] ledger (must be ZERO before TTS — verification agents close these)
1. a1-s3: original 13-year completion estimate for LP&V project (GAO doc).
2. a2-s3: Loop Current crossing as the rapid-intensification driver (NHC TCR discussion section).
3. a4-s2: KLIX last transmitted scan 8:54 AM CDT (AMS/NCDC — MED; either confirm or soften to
   "the radar picture from Slidell went dark").
4. a5-s1: London Avenue east-breach timing "before seven" (MED source; soften if unconfirmed).
5. a5-s4: E-99 load-test implication figures (31–46 ft) — currently NOT quoted in prose (kept
   qualitative); confirm before adding numbers, else prose stands as-is.
6. a7-s5: Charity physician name from original CBS credits (only if a name is displayed).
7. a7-s6: HSDRRS "rated for a storm smaller than Katrina" precision — confirm 100-year design
   level vs Katrina's estimated recurrence interval, else cut the sentence.
8. Cross-check EVERY on-screen stat card against spoken script word-for-word at compose
   (the competitor shipped "+15,000 Deaths" against a spoken 1,400 — audience caught it).

