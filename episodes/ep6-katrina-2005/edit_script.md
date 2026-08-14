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

*(segments follow in part 2 of this file)*
