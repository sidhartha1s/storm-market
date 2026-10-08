# Documentary slate: the tornado docs (owner order 20 Sep 26)

Owner, 20 Sep 26: replan El Reno and add Super Outbreak 1974 (all seven F5s), Lubbock 1970, Enderlin 2025,
Fargo 1957 with Ruskin Heights, Woodward 1947, and every Palm Sunday outbreak. 20 to 25 minute documentaries with
motion graphics. 1974 first. This file is the plan; `tracker.json` holds the live cards.

Read this as the plan written on 20 Sep 26, not as status: the E1 (1974) and E2 (Enderlin) cards below still show
their target dates and `[verify]` marks although both episodes have since been built. Where this file and
`tracker.json` or an episode folder disagree, they win.

## 1. What the Studio export says (lifetime to 20 Sep 26, `references/channel-audit-2026-09-19/studio/`)

| video | lane | length | impressions | CTR | views | AVD | watched |
|---|---|---|---|---|---|---|---|
| 2011 Super Outbreak | doc | 28:13 | 11,845 | 6.5 % | 1,589 | 11:32 | 40.9 % |
| Joplin 2011 | doc | 17:06 | 10,569 | 3.7 % | 534 | 4:21 | 25.0 % |
| 1925 Tri-State | doc | 34:53 | 4,372 | 1.8 % | 144 | 7:20 | 20.9 % |
| Carr Fire tornado (19 Sep) | doc | 32:32 | 280 | 5.7 % | 30 | 1:52 | 5.8 % |
| El Niño Texas | mini | 10:07 | 2,028 | 7.0 % | 250 | 3:09 | 30.5 % |
| CPC El Niño | mini | 7:24 | 467 | 5.1 % | 97 | 1:38 | 21.9 % |
| El Niño California | mini | 9:30 | 349 | 8.0 % | 61 | 3:15 | 34.3 % |
| Krakatau 8 missing | mini | 9:19 | 158 | 5.7 % | 18 | 3:17 | 34.8 % |
| Krakatau tsunami mechanism | mini | 11:53 | 159 | 3.8 % | 15 | 2:44 | 23.1 % |
| Dujuan Silver Week | mini | 9:30 | 118 | 10.2 % | 19 | 1:04 | 11.3 % |
| Krakatau 36,000 | mini | 9:07 | 95 | 2.1 % | 9 | 1:04 | 11.8 % |

Reading:
- **Distribution, not retention, is what collapsed.** The three tornado docs were shown 4,000 to 12,000 times each.
  No mini except Texas was shown more than 500 times. YouTube tests every upload with a small batch to the
  channel's known audience (US, 65+, tornado history); a Krakatau or Japan title fails that batch on the first
  200 impressions and never gets a second one.
- **The channel-level AVD drop (about 10 min a day on 7 to 12 Sep, about 3:20 a day from 13 Sep) is a mix effect.**
  Daily AVD is the average over whatever got watched that day; when 9 minute minis and 40 second shorts replace a
  28 minute doc in the mix, it falls whether or not any single video got worse. Per video, the minis hold 11 to
  35 % watched, the same band as Joplin and Tri-State. The owner's measurement is right; the cause is the mix.
- **Retention is a second, real problem on every video but one.** Only the 2011 Super Outbreak clears 40 %
  watched. Joplin, Tri-State and every mini sit at 11 to 35 %. Carr Fire at 5.8 % after one day means the first
  two minutes lose the room; check its hook before anything else is uploaded.
- **Packaging decided the two docs that had the same test.** Joplin and Super Outbreak got 10,000 plus impressions
  each; 6.5 % CTR turned into 1,589 views, 3.7 % into 534. Tri-State's black and white plate and a year nobody
  recognises got 1.8 %.
- **The sample is small** (31,494 impressions, 2,810 views, 4 subscribers) but the two signals above are not
  noise. Give the news lane more time only for US live events; do not give more time to foreign minis.

Carried forward unknowingly: `ops/ROADMAP.md` already recorded on 14 Sep that "US topics get a 2 to 11k
impression test, non-US topics got no test", and the programme still scheduled Krakatau and Japan twice a day.
Seven of the last nine uploads were foreign minis. That is the mistake.

## 2. Decisions this plan makes
1. **Documentary lane leads.** Two docs a week (Wednesday and Saturday, US evening), all US tornado history, all
   20 to 25 minutes, all on `references/script-os.md` (dominant question, chapter cards, retention scorecard).
2. **News lane only for US live hazards** (SPC moderate or high risk days, landfalling hurricanes, a US EF4 plus).
   Foreign buckets (krakatau, japan) are parked; pools kept. The dated placeholder cards stay in the tracker
   until the owner deletes them.
3. **Packaging is locked before scripting**, three titles and a thumb brief per episode, owner picks. Thumb
   grammar copied from the one winner: colour tornado plate, year and event name in two lines, nothing else.
4. **One named person per act, one master map per episode, one clock device per episode.** These are the three
   things the 2011 doc had that Tri-State did not.

## 3. The 20 to 25 minute format (motion graphics contract)
Per episode, 12 to 16 designed graphics, library first (`library/catalog-index.json`), each with continuous motion:
- **g-master-map**: the outbreak or track on a real map plate, drawn in as the day unfolds, returned to at every
  act seam (the 2011 doc's location march, the thing viewers stayed for).
- **g-clock**: one countdown or timeline card per episode (first report to first death to last siren).
- **g-scale**: F or EF scale bar, this tornado against the rest of the slate (width, path, dead).
- **g-radar**: NEXRAD or WSR-57 re-plot, or a designed hook echo where no radar existed (say so on the card).
- **g-then-now**: what was fixed after this event and what still is not (the scorecard device).
- **g-person**: name card for each act's human (survivor, forecaster, photographer, child).
- Citation cards (source, date, one line) replace screenshots. Stills 3 to 6 s with motion, real clip every
  45 to 60 s, chapter blackouts 0.6 to 0.9 s, CTA inside the config window via a spoken hinge, END CTA spine.
- Word budget: 22:00 target, narration = 22 × 0.9 × 152 wpm ≈ 3,000 words, probe-TTS two segments first.

## 4. Episode cards (order = ship order; every number below is `[verify]` until the fact sheet clears it)

### E1 · 1974 Super Outbreak (3 to 4 April 1974) · target 27 Sep 26
- **Dominant question:** how did one afternoon produce seven F5s, and why could nobody see it coming until the
  sky was already full of them?
- **Architecture:** Countdown 60 % (the 18 hour clock, state by state) + Detective 40 % (Fujita's aerial survey
  turning 148 tracks into the map that changed forecasting).
- **Spikes:** 148 tornadoes in 13 states and Ontario; seven F5s in one day; Xenia's high school stage emptied
  moments before a bus landed on it; Tanner, Alabama hit by two F5s inside an hour; Brandenburg, Kentucky 31
  dead; Guin, Alabama erased; about 319 dead, 5,000 plus injured; Fujita's 10,000 mile survey and the word
  "super outbreak" itself.
- **US stake / present day:** the same corridor, the same April; what a 1974 day would do to today's warning
  system (lead times then vs now on g-then-now).
- **MGs:** g-master-map (13 states, tracks drawn in by hour), g-clock (Xenia 4:40 pm etc.), g-scale (seven F5 bars),
  g-radar (Cincinnati WSR-57 hook), g-person (Xenia drama students, Brandenburg family, Fujita), g-then-now.
- **Net-info sources:** NWS Wilmington OH / Louisville / Huntsville anniversary pages, NOAA Storm Data April
  1974, Fujita's 1974 survey paper and track map, Ohio Historical Society Xenia oral histories, NIST-era damage
  photos (PD), Kentucky Educational Television footage (licence check).
- **Packaging:** "The Day America Had 7 F5 Tornadoes" / "148 Tornadoes in 18 Hours: The 1974 Super Outbreak" /
  "Seven F5s. One Afternoon. Nobody Was Ready." Thumb: colour Xenia plate, "1974 / SUPER OUTBREAK".

### E2 · Enderlin, North Dakota (20 June 2025) · target 1 Oct 26
- **Dominant question:** why did the United States go twelve years without an EF5, and what did this one do to
  end the drought?
- **Architecture:** Explanation with a twist 60 % (the scale, not the storms, was the reason for the drought) +
  Countdown 40 % (the night of 20 June).
- **Spikes:** first EF5 since Moore 2013; rail cars lofted off a train (the evidence that earned the rating);
  three dead; the rating came months after the storm; how EF5 is proven when nothing is left to measure.
- **US stake:** the "no EF5s any more" belief, and what the scale change means for every warning the viewer
  hears.
- **MGs:** g-scale (the EF5 drought timeline 2013 to 2025), g-radar (Grand Forks NEXRAD velocity), g-master-map,
  g-mechanism (how a rail car's mass becomes a wind speed), g-then-now.
- **Sources:** NWS Grand Forks damage survey and DAT, SPC event page, NDSU / ND DOT rail imagery, local
  broadcaster clips (licence), NOAA drone survey (PD).
- **Packaging:** "The First EF5 in 12 Years" / "This Tornado Threw a Train" / "America's EF5 Drought Just Ended".

### E3 · Woodward, Oklahoma (9 April 1947) · target 4 Oct 26
- **Dominant question:** what happens to a town when a two mile wide tornado arrives and forecasting the word
  "tornado" is still forbidden?
- **Architecture:** Detective 60 % (Joan Gay Croft, the four year old who vanished from the hospital that night
  and was never found) + Countdown 40 % (Glazier, Higgins, Woodward, one storm, three towns).
- **Spikes:** 1.8 miles wide, about 100 mile track; 181 dead across Texas and Oklahoma, 100 plus in Woodward;
  eleven months later the first tornado forecast in history (Tinker AFB, 25 March 1948); the missing child.
- **US stake:** every warning the viewer gets exists because of what this storm made impossible to ignore.
- **MGs:** g-master-map (the track family across the Panhandle), g-clock, g-scale (width against a town plan),
  g-person (Joan Gay Croft), g-then-now (the 1948 forecast as the payoff card).
- **Sources:** NWS Norman anniversary page, Oklahoma Historical Society, Woodward News archive, NOAA Storm
  Data, Fawbush and Miller 1948 record.
- **Packaging:** "The Tornado Nobody Was Allowed to Forecast" / "1947: Two Miles Wide and No Warning Existed" /
  "The Girl Who Vanished in the Woodward Tornado".

### E4 · Lubbock, Texas (11 May 1970) · target 8 Oct 26
- **Dominant question:** how did one tornado through a downtown become the reason every tornado since has a
  number?
- **Architecture:** Explanation with a twist 70 % (Fujita's survey of Lubbock built the F scale) + human 30 %.
- **Spikes:** 26 dead; the 20 storey Great Plains Life Building twisted and still standing today; two funnels,
  one storm; Fujita's damage map; Texas Tech's wind institute born from the wreckage.
- **US stake:** the F scale and today's EF scale traced back to this street, and what the number on the warning
  actually measures.
- **MGs:** g-master-map (downtown Lubbock path), g-mechanism (why the tower twisted, the birth of the scale
  as one equation card), g-scale, g-person (Fujita, survivors), g-then-now (Metro Tower today).
- **Sources:** NWS Lubbock anniversary page, Fujita 1970 Lubbock report, Texas Tech National Wind Institute,
  Southwest Collection archive photos (PD check), Lubbock Avalanche-Journal archive.
- **Packaging:** "The Tornado That Invented the F Scale" / "A 20 Storey Tower Twisted and Never Fell" /
  "Lubbock 1970: Why Tornadoes Have Numbers".

### E5 · Palm Sunday 1965 (11 April 1965) · target 11 Oct 26
- **Dominant question:** the warnings were issued; why did 271 people still die, and what did the double funnel
  photograph change?
- **Architecture:** Countdown 60 % (Indiana, Michigan, Ohio, the evening in order) + Detective 40 % (Paul
  Huffman's Elkhart twin funnel photo, Fujita's first aerial survey).
- **Spikes:** 47 tornadoes in six states; 271 dead; Midway trailer park; the only known double funnel photo;
  warnings that never reached radios; the words "watch" and "warning" born from this day.
- **US stake:** the watch vs warning distinction the viewer still hears, and why it exists.
- **MGs:** g-master-map (six states, tracks by hour), g-clock, g-person (Huffman, Fujita, Dunlap family),
  g-radar (what 1965 radar could see), g-then-now (warning dissemination then vs now).
- **Sources:** NWS Northern Indiana and Grand Rapids anniversary pages, Fujita's Palm Sunday survey, Elkhart
  Truth archive (photo licence check), NOAA Storm Data, Weather Bureau survey report 1965.
- **Packaging:** "The Day Two Tornadoes Walked Side by Side" / "Palm Sunday 1965: 47 Tornadoes, 271 Dead" /
  "The Photo That Changed Tornado Warnings".

### E6 · Fargo 1957 and Ruskin Heights 1957 (20 May and 20 June 1957) · target 15 Oct 26
- **Dominant question:** two F5s one month apart hit the new postwar suburbs; what did the amateur photographers
  of Fargo teach science that the dead of Ruskin Heights could not?
- **Architecture:** Detective 70 % (Fujita's 150 photograph reconstruction of Fargo that named the wall cloud)
  + Countdown 30 % (Ruskin Heights, Kansas City, 44 dead).
- **Spikes:** 44 dead in a suburb that did not exist five years earlier; ten dead in Fargo; the first tornado
  ever reconstructed frame by frame from public photos; "wall cloud" and "collar cloud" enter the language.
- **US stake:** every storm chaser's vocabulary and every spotter's training comes from these two months.
- **MGs:** g-master-map (two cities, two dates), g-photo-reconstruction (Fujita's frames animated), g-person
  (photographers, Ruskin Heights family), g-scale, g-then-now.
- **Sources:** Fujita 1960 Fargo paper, NWS Grand Forks and Kansas City anniversary pages, Fargo Forum and
  Kansas City Star archives, NDSU archives (PD check).
- **Packaging:** "The Tornado Reconstructed From 150 Photographs" / "1957: The Year the Suburbs Met the F5" /
  "How Fargo Named the Wall Cloud".

### E7 · Palm Sunday 1994 (27 March 1994) · target 18 Oct 26
- **Dominant question:** a warning was out for Goshen United Methodist Church; why did twenty people die inside
  it, and what did the country do about it?
- **Architecture:** Countdown 70 % (the service, the warning, the minutes) + Explanation 30 % (why sirens and
  radios failed rural Alabama, the NOAA Weather Radio expansion that followed).
- **Spikes:** 20 dead in one church including the pastor's four year old daughter; 42 dead across the outbreak;
  no siren in Piedmont; the President at the church; the NWS service assessment.
- **US stake:** how warnings reach a room with no phone signal today.
- **MGs:** g-master-map (Alabama and Georgia tracks), g-clock (service start to impact), g-person (the Clem
  family), g-then-now (weather radio coverage map 1994 vs now).
- **Sources:** NWS Birmingham anniversary page and the 1994 service assessment, Anniston Star archive, FEMA
  photos (PD), C-SPAN presidential visit (PD).
- **Packaging:** "The Warning Was Issued. The Church Never Heard It." / "Palm Sunday 1994: 20 Dead in One
  Church" / "Why Piedmont Had No Siren".

### E8 · Palm Sunday 1920 (28 March 1920) · target 22 Oct 26
- **Dominant question:** the deadliest Palm Sunday of all had no radar, no radio and no word for what was
  coming; how do we know what happened at all?
- **Architecture:** Detective 80 % (reconstructing 37 tornadoes from newspapers and Grazulis) + human 20 %.
- **Spikes:** about 380 dead across the Midwest and Deep South; Illinois, Indiana, Ohio, Michigan, Georgia,
  Alabama in one afternoon; a country that would not officially say "tornado" for another 30 years.
- **US stake:** the same corridors as 1965 and 1974 (the three Palm Sundays on one map, the series payoff).
- **MGs:** g-master-map (the three Palm Sunday outbreaks overlaid), g-person (one family from the papers),
  g-scale, g-then-now.
- **Sources:** Grazulis "Significant Tornadoes", Monthly Weather Review April 1920, state newspaper archives
  (Chronicling America, PD), NWS Chicago and Northern Indiana pages.
- **Packaging:** "The Forgotten Palm Sunday: 380 Dead in 1920" / "Three Palm Sundays, One Corridor" /
  "America's Deadliest Palm Sunday Was Not 1965".

### E0 · El Reno, Oklahoma (31 May 2013) · replan
- **State:** v3 draft (26:08) rendered 30 Aug in worktree `ep4-el-reno-v3`, hook v2 preview 31 Aug, full static
  suite green, three weeks parked on owner review.
- **Recommendation:** do not rebuild. Run the script-os retention pass on the existing edit (scorecard per
  minute, cut filter, one dominant question stated: "the widest tornado ever measured killed the people best
  equipped to survive it; why?"), fix the weak minutes in place, then owner review of the draft, full render,
  ship. About two days. A from-scratch replan costs the three weeks already sunk and gains one thing the
  retention pass also gives.
- **If the owner wants the full replan anyway:** Detective 60 % (the 2.6 mile width, the Samaras data, the
  chase community's blind spot) + Countdown 40 %; MGs g-master-map (the 2.6 mile width over the city), g-clock,
  g-person (Samaras, the Oklahoma City commuters), g-then-now (chaser safety, the "do not flee in cars" lesson).
- **Target:** 24 Sep 26 on the retention pass path.

## 5. Pipeline per episode (tracker phases)
idea → **packaging** (3 titles + thumb brief, owner picks) → **script** (Sonnet research agent writes the fact
sheet with URLs and `[verify]` cleared; director writes chapter cards, then prose on the retention engine;
scorecard, cut filter, AVD pass, homograph scan) → **tts** (probe two segments, recompute words) → **sourcing**
(PD spine, one labelled grid read) → **assemble** (hand-authored index.html, MGs library first, comps mounted
inside the page) → **checks** (static suite + freeze scan + comp lint + frame read) → **preview** (draft render,
owner eyeballs) → **render** (one full render, one at a time) → **upload** (master, SRT, metadata, credits).
Two episodes run staggered: while one is in checks or render, the next is in script and sourcing.

## 6. Timeline (2 per week, Wed and Sat, US evening)
| ship | episode | build window |
|---|---|---|
| 24 Sep | El Reno (retention pass) | 21 to 23 Sep |
| 27 Sep | 1974 Super Outbreak | 21 to 26 Sep |
| 1 Oct | Enderlin 2025 | 25 to 30 Sep |
| 4 Oct | Woodward 1947 | 28 Sep to 3 Oct |
| 8 Oct | Lubbock 1970 | 2 to 7 Oct |
| 11 Oct | Palm Sunday 1965 | 5 to 10 Oct |
| 15 Oct | Fargo + Ruskin Heights 1957 | 9 to 14 Oct |
| 18 Oct | Palm Sunday 1994 | 12 to 17 Oct |
| 22 Oct | Palm Sunday 1920 | 16 to 21 Oct |

Kill rule for the docs: after three uploads, any episode under 4 % CTR on 2,000 plus impressions gets a
Studio Test and Compare on the thumb before the next one ships; under 30 % watched means the next script's
first two minutes are rewritten before TTS, no exceptions.
