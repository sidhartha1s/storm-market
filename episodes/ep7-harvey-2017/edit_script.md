# edit_script.md — ep7 · "The Real Villains of Hurricane Harvey (It Wasn't the Storm)" (The Warning Hour)

> Design locked in-chat 2026-09-06 (owner). NO further design gate — next owner touchpoint is the
> draft render preview. Inserts still get ONE batched owner-approval message before wiring.
> Built on `references/script-framework.md` (hook doctrine, ROI-drip, one-product AV rule) +
> `references/script-scaling.md` (lattice) + DESIGN.md contracts.
> Research corpus: `references/ep7-harvey/` (facts-timeline.md, facts-villains.md,
> teardown-darkhorizon.md, teardown-stormforge.md, comment-insights.md, footage-inventory.md).

## Spec
- **Slug:** `ep7-harvey-2017` · **Channel:** The Warning Hour
- **Title (owner-locked):** *The Real Villains of Hurricane Harvey (It Wasn't the Storm)*
- **Thumbnail:** real PD flooded-Houston aerial + bold "HOUSTON 2017" / title text. NO AI thumbnail.
- **Runtime target:** ~21 min (owner band 20 ±2–3). Word budget ≈ **2,800** (21 × 0.9 × ~149 wpm,
  ep6 manifest prior; probe-TTS ×2 re-verifies before final trim).
- **Voice:** pocket-TTS Pharaoh clone (config `external.*`, verify md5). Narration below is
  readable-form; the TTS pass mechanically converts (numbers/dates spelled out, <24-word
  sentences, no paired dashes).
- **Positioning:** Dark Horizon (1.07M views) skips the dams almost entirely; StormForge (516K)
  covered the dam/court spine — we out-execute on specificity (exact court language, the 31.4-inch
  design-storm receipt, the Dec-2025 affirmance + Apr-2026 downstream reversal NO video has),
  humanity (documented survivor accounts as attributed quotes), and the untouched
  renter/aftermath angle. Title makes a defensible claim (no "almost ended Texas" hyperbole —
  that drew documented backlash).
- **Info:fluff ≈ 75:25.** Net-info-gain carried (no competitor has): ① 57% of HCFCD gauges set
  records; ② 90/69/46% river-gauge scorecard; ③ the 31.4-inch design storm vs the ~31 inches that
  fell (the 1940s trade-off, verbatim court record); ④ Dec 22 2025 Federal Circuit affirmance +
  Apr 22 2026 downstream ruling (post-dates every competitor video); ⑤ highest water reading was
  INLAND (Manchester, Ship Channel, 10.35 ft) — runoff, not surge.
- **Fact discipline:** every number below traces to references/ep7-harvey/facts-*.md. Remaining
  `[verify]` items are listed at the bottom; ZERO open markers before TTS (unresolved = cut).

## Hook contract compliance (DESIGN.md + framework; owner-ordered ep7 deviations logged)
- [x] Owner deviation: **narrator from second zero IS the hook** (no broadcast anchor line).
- [x] Owner deviation: **NO void after the hook** — flows into the intro on the next breath.
- [x] NO black start: frame one is mid-action VIDEO (helicopter flood flyover), rain bed live at 0s.
- [x] Title-popup inside the first second (HURRICANE HARVEY on the spoken words).
- [x] Match-cut text popups land ON the spoken word (owner order): HURRICANE HARVEY → HOUSTON
  (danger red #e74c3c) → THE UNITED STATES GOVERNMENT → AUGUST 2017 popfig.
- [x] Every cut lands on an audio event; riser peaks exactly on "government".
- [x] All hook slots VIDEO with native motion — stills banned in the hook (owner order).
- [x] BMW rule: hook continues the title's exact frame (villains → verdict language).
- [x] ROI-first: the verdict (the WHAT) is stated in the hook; the episode owes only the WHY.

## HOOK — AV table (~0:35, seg h1)
| t | VIDEO (all moving) | TEXT popup (on the word) | AUDIO |
|---|---|---|---|
| 0.0–5.5 | Helicopter flyover over flooded Houston (S-1 beat ①; primary candidate DVIDS 567965 wide pass, fallback 546792) | HURRICANE HARVEY (popfig, on the words) → HOUSTON (danger red, on the word) | Rain bed live at 0s under narrator: "Years after Hurricane Harvey, a federal court ruled on who flooded thousands of homes in Houston." |
| 5.5–10.5 | Boat wake down a flooded street (DVIDS 546960 Friendswood punt team) | — | "The verdict named no hurricane. It named no act of God." (hammer breaks; bed swells) |
| 10.5–16 | Addicks release aerial, water moving through the works (DVIDS 547295) | THE UNITED STATES GOVERNMENT (on the phrase) | "It named the United States government." Riser builds and PEAKS on "government" → hard cut |
| 16–24 | Rain-lashed night rescue chaos (DVIDS 546494 TX Nat'l Guard night rescues) | AUGUST 2017 (popfig) | "But to understand how a hurricane got framed for it, you have to go back to the very four days Houston stood still." |
| 24→ | NO VOID, NO BLACKOUT — hard cut into intro's first shot on the breath | | Rain bed carries across the seam |

## Loop table (script-scaling.md discipline)
| Loop | Planted | Paid |
|---|---|---|
| EPISODE LOOP: "the verdict named the government — how does a hurricane end up in court?" | hook | act 6 (the verdict, in full) |
| Roster loop: four suspects named | intro | one per act, acts 1–5 |
| L1: "the storm is the only innocent one" | intro | act 1 close (guilty of rain, innocent of the flood) |
| L2: "the water had to go somewhere — and that somewhere was chosen decades earlier" | act 1 close (cta-hinge tease) | act 2 open (cta-hinge payoff) + act 4 (the pools) |
| L3: "why didn't they just leave?" | act 2 close | act 3 (Rita receipt, the acquittal) |
| L4: "the phones would not stop" | act 3 open | act 3 close (Emmett line, Cajun Navy) |
| L5: "fourteen thousand homes were built inside the answer" | act 3 close | act 4 (the flood pools) |
| L6: "the dams got the exact storm they were designed around" | act 4 close | act 5 (31.4 vs ~31) |
| L7: "it stopped raining — why is the water rising?" | act 5 mid | act 5 close (the releases + upstream backup) |
| **cta-hinge (REQUIRED)**: tease = last line of a1-s6 → CTA → payoff = first line of a2-s1 | end act 1 (~6:50 ≈ 32%) | act 2 open |

## Act order (escalation rule: biggest reveal lands last)
HOOK 0:35 → INTRO 1:25 → ACT 1 The Storm That Would Not Move 3:30 → **CTA** (15.6s + dips) →
ACT 2 The City That Could Not Drink 2:50 → ACT 3 The Four Days 3:30 → ACT 4 The Maps Nobody
Showed 3:00 → ACT 5 The Decision 4:00 → ACT 6 The Verdict 2:00 → CLOSE 0:50 ≈ **21:10**.
Blackouts 0.6–0.9s at every act seam (NONE at hook→intro, owner order); 1.0s dips around CTA.

---

# SEGMENTS

## h1 — HOOK (narration, ~62 words, AV table above)
> Years after Hurricane Harvey, a federal court ruled on who flooded thousands of homes in
> Houston. The verdict named no hurricane. It named no act of God. It named the United States
> government. But to understand how a hurricane got framed for it, you have to go back to the
> very four days Houston stood still.

## INTRO (~1:25, ~205 words) — grounds the event, concedes the storm, states the ROI roster

**i1-s1 (narration, ~75 w)** — VIDEO: GOES-16 satellite loop of Harvey spinning onto the coast
(NOAA); popfig "AUGUST 25, 2017" on the date.
> August, twenty seventeen. Hurricane Harvey slams into the Texas coast as a Category Four,
> with winds of one hundred and thirty two miles per hour. Then it does something almost no
> hurricane has ever done. It stops. For four days it sits over the fourth largest city in
> America, and it rains harder than it has ever rained in this country's recorded history.

**i1-s2 (narration, ~60 w)** — VIDEO: flooded freeway aerial → submerged suburbs (PD); counter
popfig "1,000,000,000,000 GALLONS" rolling on the number.
> One trillion gallons fall on Harris County alone. More than a hundred people die. Whole
> neighborhoods drown. And when it is over, almost everyone on Earth files it away the same
> way. A monster storm. A natural disaster. Nobody's fault.

**i1-s3 (narration, ~70 w)** — GRAPHIC g-roster: four silhouette cards revealed ON each phrase
(the ROI list, stated in full — framework doctrine).
> But the flood that broke Houston had four authors. A storm that refused to move. A city that
> had paved over its own defenses. A set of maps that showed exactly which homes would drown,
> and were never shown to the people living in them. And a decision, made in a quiet room in
> the middle of the night, to open the gates on purpose.
*(seam: hard cut, 0.7s blackout, act 1 opens — "but" carried by the first act line)*

## ACT 1 — VILLAIN ONE: THE STORM THAT WOULD NOT MOVE (~3:30, ~505 w)
**Job:** deliver the full-blooded hurricane act (the title's "storm" gets its due), explain the
stall honestly, close with the acquittal twist that re-frames the episode. Rehooks: landfall
broadcast pull, g-stall map, g-rainfall record counter.

**a1-s1 (narration, ~85 w)** — VIDEO: Rockport landfall fury, Cat-4 wind footage (PD/short
broadcast pull); popfig "ROCKPORT · 10:00 PM".
> Start on the coast, because the storm deserves its due. Ten PM, August twenty fifth. Harvey
> comes ashore near Rockport, Texas as a Category Four. The gusts near the coast pass one
> hundred and forty miles per hour. Rockport is two hundred miles from Houston, and this is
> the only time Texas will see Harvey as a major hurricane on land. Because within twelve
> hours of landfall, Harvey is not really a hurricane anymore.
*(micro-loop: "so how does a dying storm drown a city it never reached?")*

**a1-s2 (insert candidate INS-01, ~8s)** — broadcast pull: landfall-night coverage, reporter in
the wind (CLAIM-CLASS, short, narrated context around it). Cut chosen from full transcript.

**a1-s3 (narration, ~120 w)** — GRAPHIC **g-stall** (map): Harvey's track stalling between TWO
ridge systems drawn and labeled ON the narration — "FOUR CORNERS HIGH" and "GULF HIGH" — the
corrected mechanism (NHC TCR), not the folk "Rockies/Bermuda" version.
> Here is the part most retellings get wrong. Harvey did not stall because of one blocking
> ridge over the Rockies. The government's own hurricane report names two. A dome of high
> pressure parked over the Four Corners, and a second dome over the northern Gulf of Mexico.
> Harvey drifted into the dead space between them, and the steering currents simply shut off.
> A storm with nowhere to go does not have to be strong to be deadly. It just has to sit. And
> for four days, over the wettest air in the hemisphere, Harvey sat.

**a1-s4 (narration, ~110 w)** — GRAPHIC **g-rainfall**: rain-gauge counter rolling fast then
slowing into 60.58; the map color-scale beat drawn as the NWS scale running out of colors
(designed card built from the real WPC rainfall graphic).
> The numbers stopped fitting the instruments. A rain gauge near Nederland, Texas measured
> sixty point five eight inches. The most rain ever recorded from one storm in United States
> history. Parts of Houston took thirty six to forty eight inches. The Weather Service's
> rainfall maps literally ran out of colors, and forecasters had to invent new shades of
> purple just to draw what was falling. NOAA later called it a flood with less than a one in
> one thousand chance in any given year. Not a five hundred year flood. A thousand year flood,
> or worse.

**a1-s5 (narration, ~95 w)** — VIDEO: bayous raging, gauge stations, water rising on
infrastructure (USGS/HCFCD PD); popfig "57% OF GAUGES · ALL-TIME RECORDS".
> Harris County keeps its own network of flood gauges, and during those four days nearly six
> out of every ten of them measured levels no one had ever seen before. Of the sixty seven
> river forecast points across southeast Texas, ninety percent hit flood stage. Nearly half
> set all time records. The storm did all of that. That much is true, and no honest telling
> of this story skips it.

**a1-s6 (narration, ~95 w — CTA-HINGE TEASE, ends the act)** — VIDEO: slow aerial push over an
endless drowned grid, bed thinning to near-quiet.
> But here is the verdict on suspect number one. The storm made the water. The storm does not
> decide where the water goes. When a trillion gallons landed on Houston, every drop was
> handed to a system that people designed, people built, and people chose not to fix. The
> storm was guilty of the rain, and only the rain. Where that rain was about to be sent had
> been decided decades before Harvey was born.
*(1.0s dip to black → CTA)*

## CTA (owner asset, must-keep) — ~7:00 in ≈ 32% of runtime (window 30–40% ✓)
`media/cta/paul-storm-ready-v5.mp4` · 15.633s · own audio (`data-volume="1"`) · 1.0s black dip
in and out · `data-srt-label` from config · sits INSIDE act 1's chapter (no chapter boundary) ·
hard cut out of the dip into a2-s1's REAL footage. Hinge pair logged in the loop table.

## ACT 2 — VILLAIN TWO: THE CITY THAT COULD NOT DRINK (~2:50, ~410 w)
**Job:** pay the hinge (where the water went), indict the pavement with numbers, plant the
"why didn't they leave" loop. Rehooks: g-watershed diagram, Allison archival beat.

**a2-s1 (narration, ~105 w — CTA-HINGE PAYOFF opens on the first sentence)** — VIDEO: hard cut
to real footage: water sheeting off concrete, drainage culverts overwhelmed (PD).
> That somewhere was concrete. Houston is the largest American city with no zoning code, and
> for decades it grew in the one way water cannot forgive. Between the mid nineties and two
> thousand eleven, the county's paved, sealed, water proof surface grew by a quarter. Nearly a
> third of its natural wetlands disappeared in under twenty years. West of the city, a prairie
> of six hundred thousand acres that once drank the rain like a sponge had been carved down to
> a fraction of itself. The sponge was gone. The rain was not.

**a2-s2 (narration, ~90 w)** — GRAPHIC **g-watershed**: split mechanism diagram — one acre of
prairie absorbing vs concrete shedding; runoff arrows grow scaleX on the words.
> The county's own flood control district had done the math. Restoring a single acre of
> prairie soaks up the extra runoff created by two acres of new houses. Its leadership
> publicly disputed that finding, and the building went on. Houston's big drainage projects
> were built to handle what engineers call a one hundred year storm. Harvey was a one
> thousand year storm. The city was not under designed by a little. It was under designed by
> an order of magnitude.

**a2-s3 (narration, ~100 w)** — VIDEO: 2001 Tropical Storm Allison archival (PD/news short pull);
popfig "ALLISON · 2001".
> And Houston had been warned, by name. In two thousand one, Tropical Storm Allison put
> twenty eight inches of rain on the city in twelve hours, flooded seventy three thousand
> homes, and became the costliest tropical storm in American history at the time. Almost half
> of the buildings Allison flooded were outside every flood zone on FEMA's maps. The warning
> could not have been clearer. The maps are wrong, and the city cannot drink. Sixteen years
> later, Harvey arrived to collect.

**a2-s4 (narration, ~85 w)** — VIDEO: pre-storm calm, Houston skyline, traffic (stock/PD);
tempo drops; plant L3.
> So when Harvey stalled, six and a half million people were sitting in a bowl of sealed
> concrete under the heaviest rain in American history. Which raises the question every
> outsider asked that week, sometimes kindly, sometimes not. Why on earth didn't Houston
> evacuate? The answer is a story about the last time Texas tried. And it is the one villain
> on tonight's list that turns out to be innocent.
*(0.8s blackout → act 3)*

## ACT 3 — THE FOUR DAYS (~3:30, ~505 w)
**Job:** the human core — stay-put acquittal, 911 collapse, the civilian navy. Emotion banked
here. Rehooks: Turner/Abbott pulls, Emmett quote card, rescue footage run, USCG numbers.

**a3-s1 (narration, ~120 w)** — VIDEO: Rita 2005 gridlock archival (PD/news short pull); popfig
"RITA · 2005".
> September, two thousand five. Hurricane Rita is bearing down on Texas weeks after Katrina
> drowned New Orleans, and nearly three million people flee the coast at once. The evacuation
> becomes a hundred mile parking lot in hundred degree heat. People die of heat stroke in
> their cars. A bus carrying nursing home residents catches fire near Dallas, and twenty
> three of them never get out. When the counting is done, the leaving kills far more Texans
> than the storm does. More than a hundred deaths, and the vast majority were the evacuation,
> not the wind. Houston learned that lesson in the cruelest possible classroom.

**a3-s2 (insert candidate INS-02, ~7s)** — Mayor Turner presser pull (AP/KHOU, CLAIM-CLASS,
short): the "You literally cannot put six point five million people on the road" line, verbatim,
his own audio. **a3-s3 (insert candidate INS-03, ~6s)** — Abbott briefing pull (C-SPAN):
"you need to strongly consider evacuating." Narration bridges the contradiction between them.

**a3-s4 (narration, ~85 w)** — VIDEO: empty pre-storm streets → first flooded streets at night.
> The mayor said stay. The governor, the same afternoon, said think about leaving. Both were
> reading the same history and drawing opposite lessons, on live television, one day before
> landfall. Verdict on this suspect: staying put likely saved lives. The math of two thousand
> five says a Houston evacuation kills hundreds on dry roads before the first drop falls.
> The stay put call was not the crime. But it did mean that when the water rose, everyone
> was home.

**a3-s5 (narration, ~110 w)** — VIDEO: night rescues, boats in streets, dispatch-center b-roll;
counter popfig "75,000 CALLS".
> And then the phones would not stop. From Friday night to Monday morning, Houston's
> emergency center took roughly seventy five thousand nine one one calls. A normal weekend is
> eight or nine thousand a day. Dispatchers began telling families the thing no dispatcher
> ever wants to say. Get to the roof. Help is coming, but there are hundreds ahead of you.
> The county judge went on television and said a sentence that tells you everything about
> where the government stood. If you have a boat, we need your help.

**a3-s6 (narration, ~95 w)** — VIDEO: Cajun Navy convoys, civilian boats launching from
freeways, USCG hoists (DVIDS run); popfig "17,000 RESCUES".
> They came. Shrimpers, bass fishermen, duck hunters, the volunteer fleet the Gulf Coast
> calls the Cajun Navy, hauling boats toward the flood while the rain was still falling.
> Government crews and volunteers together pulled off more than seventeen thousand water
> rescues. The Coast Guard alone lifted eleven thousand people and over a thousand pets to
> safety, its biggest rescue operation since Katrina. Sixty eight people still died in the
> water. Almost all of them drowned in fresh water, in their own city, miles from the sea.
*(hold 3s: single boat wake at dusk, bed up — the breath)*

**a3-s7 (narration, ~50 w — plant L5)** — VIDEO: rain easing, sky lightening.
> By Monday the rain was finally moving east, and Houston believed the worst had passed. It
> had not. Because fourteen thousand homes on the west side had been built inside an answer
> to a question their owners never heard anyone ask.
*(0.8s blackout → act 4)*

## ACT 4 — VILLAIN THREE: THE MAPS NOBODY SHOWED (~3:00, ~435 w)
**Job:** the flood pools + disclosure failure + insurance trap. Signature graphic. Rehooks:
g-floodpool, Corps official's own quotes as text cards.

**a4-s1 (narration, ~115 w)** — GRAPHIC **g-floodpool** (signature, 2–3 versions authored):
real map plate of west Houston; the Addicks & Barker "flood pool" boundaries draw themselves;
then subdivision footprints appear INSIDE the line, one by one, ON the narration.
> West of downtown sit two enormous earthen dams called Addicks and Barker. Most Houstonians
> had never heard of them. The dams hold back two reservoirs that are dry almost all the
> time. Dry enough for soccer fields and hiking trails. But on the government's own maps
> there is a line around each one called the flood pool. The land the water is designed to
> cover when the dams do their job in a great storm. By twenty seventeen, roughly fourteen
> thousand homes had been built inside those lines. Subdivisions, schools, cul de sacs.
> Inside the pool.

**a4-s2 (narration, ~110 w)** — VIDEO: suburban west-Houston streets, families, for-sale signs
(stock/PD); then quote card (glasscard) with the Corps official's words, attributed.
> The Army Corps of Engineers knew. The official who ran the dams day to day put it in plain
> English to investigative reporters a full year before Harvey. In an ideal world, he said,
> neighborhoods like these would not exist. We are between a rock and a hard place. The Corps
> says it had no power to stop the building. Harris County has no zoning. The developers kept
> building, and in most cases nothing in Texas law required anyone to tell a buyer that their
> new street sat inside a federal reservoir's designed flood zone.

**a4-s3 (narration, ~105 w)** — GRAPHIC: FEMA-map card — the "low risk" stamp vs where water
actually went (built from the county's post-storm analysis, honest label if the three-quarters
figure stays MED: use Allison's verified "almost half" as the anchor).
> The official flood maps made it worse, because they told these families they were safe.
> During Allison, almost half the flooded buildings were outside every mapped flood zone, and
> Harvey repeated the trick at scale. Families outside the lines had no reason to carry flood
> insurance, and most did not. Around eight in ten flooded Houston households had no flood
> coverage at all. In the five years before Harvey, flood policies in Harris County had
> actually gone down by twenty five thousand. The city was less insured against the flood
> than it had been five years earlier.

**a4-s4 (narration, ~70 w — plant L6)** — VIDEO: slow push on the Addicks dam structure, quiet.
> So hold the picture. Fourteen thousand homes inside a designed flood zone, most of them
> uninsured, told by the maps they were safe. All of it waiting on one question nobody wanted
> to ask out loud. What happens when the reservoirs finally get the storm they were built
> for? In August twenty seventeen, the reservoirs got almost exactly that storm.
*(0.8s blackout → act 5)*

## ACT 5 — VILLAIN FOUR: THE DECISION (~4:00, ~580 w)
**Job:** the dams' history, the 1940s trade-off receipt, the night of the releases, both floods.
The episode's peak. Rehooks: g-decision, Zetterstrom presser insert, sunny-day water-creep.

**a5-s1 (narration, ~115 w)** — VIDEO: archival dam construction era imagery → modern gate
structures (USACE PD); popfig "1940s".
> Addicks and Barker were born from a flood. After Houston drowned twice in the nineteen
> twenties and thirties, Congress ordered dams built west of town with one mission. Protect
> downtown Houston. The engineers of the nineteen forties planned around a monster they
> called the design storm. Thirty one point four inches of rain. And then they made a
> decision that sat quietly in the files for seventy years. Buying all the land the design
> storm would flood was expensive. So they bought only the low ground, and wrote down that
> saving the money was worth the risk.

**a5-s2 (narration, ~90 w)** — GRAPHIC **g-decision** part 1: the written trade-off as a
document card — the court-record language revealed line by line, attributed.
> Their own paperwork said the quiet part plainly. One day, in a severe enough storm, the
> government would have to flood the land it chose not to buy, with the accompanying damages,
> to protect the city downstream. That sentence sat in the record while the subdivisions of
> act four went up inside the pool. In two thousand nine, Corps engineers rated both dams
> among the most dangerous in America. Extremely high risk. Take immediate action to avoid
> failure. The gate repairs were still unfinished when Harvey stalled.

**a5-s3 (narration, ~110 w)** — GRAPHIC g-decision part 2: twin reservoir columns filling in
real time against dated tick marks; "HALF A FOOT PER HOUR" popfig.
> Now run the four days again from inside the dams. The rain that fell on the watersheds
> above Addicks and Barker averaged thirty one inches across those four days. The nineteen
> forties design storm, arrived at last, almost to the inch. The dry reservoirs
> became lakes rising more than half a foot every hour. Both pools passed every level ever
> recorded. And the engineers were staring at the oldest trade in flood control. Hold the
> water and gamble with the dams themselves, or open the gates and flood the people
> downstream on purpose.

**a5-s4 (insert INS-04, ~10s)** — Zetterstrom USACE presser pull (DVIDS 549709, PD-FED): the
commander explaining the release in his own voice. Cut at the transcript's peak (full
transcription first, per rule).

**a5-s5 (narration, ~115 w)** — VIDEO: gates releasing (DVIDS 547295) → night footage; popfig
"AUGUST 28 · BEFORE DAWN".
> In the middle of the night on August twenty eighth, hours ahead of their own announced
> schedule because the pools were rising too fast, the Corps opened the gates. Buffalo Bayou,
> already swollen, took the release on top of the storm. In neighborhoods that had survived
> four days of record rain, the water now rose while the sky cleared. Thousands of homes
> along the bayou flooded after the rain had all but stopped. At least two people died in
> those homes after the gates came open. Families stood in sunshine and watched water climb
> their driveways.

**a5-s6 (narration, ~95 w — pays L7, the sunny-day image)** — VIDEO: THE signature shot —
clear sky, water creeping up a dry street (S-1 class find; fallback: post-release Energy
Corridor footage).
> And upstream, behind the dams, the other half of the design came true. The pools kept
> spreading past the government's property line, exactly as the nineteen forties memo said
> they someday would, onto private land, into living rooms. Roughly ten thousand homes and
> businesses upstream took water from the reservoirs themselves. Not from rain. From the
> pool lines on the map. The ones nobody had shown them. It stopped raining yesterday,
> people asked. Why is the water still rising? Now you know the answer.
*(hold 3–4s: water on sunlit street, bed low — then 0.9s blackout → act 6)*

## ACT 6 — THE VERDICT (~2:00, ~290 w) — pays the hook in full
**Job:** return to the courtroom from second zero. The act-of-God line lands literally.
Rehooks: g-verdict cards, gavel-paced reveals.

**a6-s1 (narration, ~110 w)** — GRAPHIC **g-verdict** part 1: case card — *In re Upstream
Addicks & Barker*, court, year; ruling line revealed on the words.
> The families sued. Not for the hurricane. For the trade offs. In twenty nineteen, a federal
> judge ruled on the upstream flooding and found that when the government builds a reservoir,
> knows the land it will someday flood, and chooses not to buy that land, the flooding is not
> a disaster. It is a taking of private property, and the Fifth Amendment says the government
> must pay for what it takes. The government appealed. In December twenty twenty five, the
> appeals court affirmed it. The flooding of those homes, the court said, would inevitably
> happen again. It was permanent. It was designed.

**a6-s2 (narration, ~115 w)** — GRAPHIC g-verdict part 2: the downstream card — the 2020
"Act of God" line ON SCREEN, then struck through as the reversal lands.
> Downstream took longer, because in twenty twenty a different ruling threw those families
> out of court with a phrase you have heard before. The damage, the judge wrote, was an act
> of God. But the appeals court sent it back. And in April of twenty twenty six, the same
> judge reversed himself. The gates, he found, were opened before the dams were in true
> danger, and the extra flooding was the government's to answer for. That case is still
> moving, and the government may appeal again. But remember how this story opened. The
> verdict named no hurricane. It named no act of God.

**a6-s3 (narration, ~65 w)** — VIDEO: modern Buffalo Bayou, calm water, rebuilt streets.
> That is how a hurricane gets framed. The storm brought the rain, and everything else, the
> pavement, the silent maps, the unbought land, the midnight gates, was people. Which is
> exactly why this story is worth twenty minutes of your life. Because the villains that
> flooded Houston were not weather. And they have not gone anywhere.
*(0.9s blackout → close)*

## CLOSE — Warning Hour signature (~0:50, ~110 w)
**c1-s1 (narration)** — VIDEO: dusk over a Houston bayou → match-cut to channel title card on
the closing line.
> Here is the part you can use. Somewhere near you there is a map like Houston's. A flood
> line, a dam pool, a drainage plan, drawn long before you moved in. The people who drew it
> know your street better than you do. Find it. Your county keeps it, and it is free to see.
> Because disasters don't ask permission. But they do send warnings. Learn what yours looks
> like, so when it comes, you already know what to do. This was The Warning Hour.

---

## Word count: ~2,795 (budget 2,800 ✓ — re-verify after probe-TTS ×2, trim on the manifest)

## Insert slate (ONE batched owner-approval message before wiring — the only pre-preview gate)
| ID | Clip | Class | Use |
|---|---|---|---|
| INS-01 | Rockport landfall-night broadcast pull (~8s) | CLAIM-CLASS | act 1 texture |
| INS-02 | Turner "cannot put 6.5 million on the road" (AP/KHOU) | CLAIM-CLASS | act 3, verbatim |
| INS-03 | Abbott "strongly consider evacuating" (C-SPAN) | PD-adjacent | act 3, verbatim |
| INS-04 | Zetterstrom USACE presser pull (~10s, DVIDS 549709) | PD-FED | act 5, the decision in his voice |
All transcribed in full BEFORE cut selection; excerpts + provenance rows logged here + CSV.

## Graphics slots (library-first; scratch reasons logged per DESIGN.md)
g-roster (intro) · g-stall (map-route-fit pattern) · g-rainfall (ep2 stat-panel counter
anatomy) · g-watershed (mechanism diagram) · g-floodpool (SIGNATURE — map plate + pool lines +
subdivision reveals; 2–3 versions) · g-decision (document card + twin filling columns) ·
g-verdict (case cards ×2, strike-through reversal beat). All JS/WAAPI, ≥3 type tiers,
continuous element per long graphic, slide-out exits, beats word-synced to words.json.

## Remaining [verify] items (resolve before TTS; unresolved = line cut/softened)
1. "three-quarters of Harvey-flooded homes outside the 100-yr floodplain" — NOT used in
   narration (Allison's verified "almost half" used instead). g-floodpool FEMA card must also
   use only the verified figure. STATUS: avoided.
2. Cedar Bayou — NOT used. STATUS: avoided.
3. "1:40 AM" — NOT used ("middle of the night... hours ahead of their announced schedule",
   per the verified window). STATUS: resolved by wording.
4. Combined death toll — narration uses "more than a hundred" (i1-s2), inside the verified
   103–105 range; act 3 uses the HIGH-confidence "sixty eight" direct figure. STATUS: resolved.
5. Katy Prairie "fraction of itself" — REPORTING-sourced; wording kept vague (no acreage
   claim). STATUS: resolved by wording.
6. "17,000 rescues" = government + volunteers combined (NWS SA) — narration says "together",
   correct. STATUS: resolved.
