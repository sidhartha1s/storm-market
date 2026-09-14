# The Warning Hour: showrunner decision, 2026-09-14

Sources: two senior interviews (Walt, Dayton; Ray, Abilene) + synthesis, phrase corpus (23,305 competitor words vs 5,929 ours, `count.py`/`c2.py`), skeptic audit + refutation, packaging plan, shorts plan. Humanise rule numbers verified against `.worktrees/ep8-krakatau-seabed/references/humanise-rules.md` lines 9-45 (rules 1-17). No files edited.

## 1. What the audience actually wants
1. A checkable fact in the title (number + category + date). Ray: "states a fact I can check." Only "Four EF5 Tornadoes in One Day" passed both seniors.
2. No fake news chyron. Ray: "A lie. I know what a chyron looks like." Walt: "reads as a lie before the video even plays."
3. Spelling. Ray: "I'd not trust a man who can't spell eruption to tell me about one." Grid bottom-middle: "ERRUPTIONS".
4. Place names on the thumb, no arrows/circles/slogans. Walt: "A place name I know beats a slogan every time." Only thumb Walt would click: "the mountain that says SEATTLE."
5. Systems-failure explainers. Ray on the six dead transmitters: "Nobody ever told me that." "My radio's on the counter right now. That's the one I'd tell my son-in-law."
6. Two sentences and a picture for physics, no helicity/joules. Ray: "Say 'the air was like gasoline' and move on."
7. No quiz, no comment-begging, one CTA at the end. Walt: "I'm not at a carnival." Krakatau #4 line 53 at ~1:10: "Comment down where you are watching this from."
8. American ground inside 30 s or a reason to care. Ray on Krakatau: "Would've left at minute two if he'd said so up front." US stake arrived at 5:31.
9. Feet, miles, Fahrenheit, dollars. Ray: "Lituya is the one time you gave me feet, and that's the one part I remember."
10. Sourced uncertainty. Walt: "'these numbers disagree' followed by which one you chose and why." Competitor "nobody knows" class 1.0/1000, ours 0.2.
11. Steady NWS-radio pace, 150 wpm, longer sentences allowed. Synthesis: "Let sentences run; the 24-word cap chops." Ep2 143 wpm, 32 sentences >24 w, 41% AVD.
12. One vivid object per segment, not stacked. Ray: "I'd cut the Ford Explorer by the third throw." Walt: "You'd rewind it."

## 2. What we are doing wrong (survived refutation)
| # | Sev | Finding | Evidence |
|---|---|---|---|
| 1 | S5 | Non-US topics with no place/year in title or thumb get no browse cohort | Krakatau #3/#4: ~50 impressions each, almost all Search, 4 + 2 views; title lacks "Anak Krakatau"/"2026"; thumb has no place, map, or arrow (review L34) |
| 2 | S5 | Production spend downstream of the impression gate | Krakatau #4: retention pass, 11 rules, popfigs, MG cards, 12 sources, 2 views |
| 3 | S4 | Distribution plumbing unshipped | metadata.md L32 "[EP1 LINK — OWNER TO FILL]" live in ep2 description; no playlist; end-screen execution unverified; ep2 viewers at 11.5 min AVD had nowhere to go |
| 4 | S4 | House rules ban the proven hook and force the flop's shape | humanise L32 bans "this is the story of" (ep2 uses it, 1,529 views); FORMAT chapter-exit questions + 24-word cap gave Krakatau #4 9 question marks, 0.6% sentences ≥25 w, flattest rhythm of eight files |
| 5 | S4 | US stake too late on foreign stories | FORMAT rule 8 says second minute; Krakatau #4 C5 "ALASKA, 1958" at 5:31; 8 Indonesian toponyms before it |
| 6 | S4 | Early engagement tic | "Comment down where you are watching… I reed all the comments" inside 75 s; competitors' only early address is a promise |
| 7 | S3 | Zero forward window, no named scientist | "next week/coming days" 1.4/1000 theirs vs 0.0 ours; scientists 2.2 vs 0.3; no debunk block (5/6 outliers have one at 60-75%) |
| 8 | S3 | Metric and no comparator on foreign figures; "still/already" as glue (5.2 vs 2.1) | "heard four thousand eight hundred kilometres away" with no US comparator |
| 9 | S3 | Publish hygiene | Typo thumb shipped, placeholders shipped; no pre-publish checklist |
| 10 | S3 | Three formats in 20 days, two off-audience | 7 uploads: doc, El Nino mini, Krakatau mini; El Nino minis 47/150 vs Krakatau 4/2 |
Dropped after refutation: publish-slot advice, "5k subs" thresholds, "cut docs to 20 min" (ep2 spec was 30 min at 137 wpm, retained 41%), CTA move (no retention curve; median viewer passed 8:26), "seniors never click urgency" (Texas caps title got the best mini CTR).

## 3. Scripting changes (paste into script-os.md)
1. **Pace.** 150 wpm delivered, docs and minis alike. Slow only for numbers, never for drama; pause after death counts, not before reveals. No atempo above 1.0. COMPATIBLE.
2. **Rhythm.** Median sentence 12-18 words; 10-15% of sentences 25-35 words as fact-chains joined by and/then/which; one kicker ≤4 words per 150 words, never a flip. The 24-word cap is deleted; TTS stumbles are fixed per sentence, not by rule. COMPATIBLE with rule 13 (it asks for variety, the cap killed it).
3. **Opening promise.** Sentence one is a number or a date. Inside 45 s one direct-address fact promise ("Inside twenty minutes you will know what a very strong El Niño did to your state the last two times"). "This is the story of…" is allowed once, before 0:60, in documentaries. CONFLICT with rule 7 (thesis opener banned). Resolution: amend rule 7 to ban the thesis opener only after 0:60 and only when it restates a beat already shown; the proven hit uses it.
4. **Address.** "You" = promise or stake only, max 3 per 1,000 words after minute 1; "we" = Americans/the country 2-3× per script; replace half of "people" with the named group (retirees in mobile homes, night-shift nurses); "I" never; no comment ask before the closing CTA. COMPATIBLE (rule 2 stays: no "picture yourself").
5. **Authority.** One named researcher + institution + venue per mechanism chapter, form "X said, and this is a direct quote". Agencies named on screen (CPC, NWS, USGS, EIA). "Nobody knows" always in a source's mouth ("The USGS bulletin uses the word 'cannot'"). Fear only as sourced fact ("Georgia Tech modelled it: 12,800 deaths"), never narrator adjectives (terrible, cruel, mercifully). COMPATIBLE (rules 1, 6, 16).
6. **Certainty split.** Flat declaratives for record and mechanism; the future in the three-path form: "If A, X. If B, Y. If C, Z. [Source] has not said which." Hedge words only on numbers. COMPATIBLE (rule 10 stays).
7. **Time anchoring.** Live videos: "as of this morning", day-of-week stamps, and a dated watch-for close ("The next CPC update lands Thursday; the number to look for is Niño-3.4"). "Still/already" capped at 1.5/1000; replace with a clock. COMPATIBLE with rule 14 if the close is a fact, not a recap.
8. **Place anchoring.** US state or region named in the first 60 s of every script; every foreign distance/height restated in a US landmark and in feet/miles/°F/dollars; max 3 unfamiliar foreign place names per script. Supersedes FORMAT rule 8's "second minute". COMPATIBLE.
9. **Transitions.** Seams are time-stamps or place-stamps ("At half past two that afternoon, in Mississippi"), never questions and never "to understand X you have to understand Y". Chapter-exit questions allowed only when the answer is an open fact, max 3 per doc, 2 per mini. CONFLICT between script-os "question → information → payoff" loop and rule 8. Resolution: keep rule 8 for mid-paragraph questions; rewrite script-os to say the loop's "question" is usually implied by a stamp or an unresolved fact, spoken at most 3×.
10. **Debunk block.** Live-hazard videos carry a 60-90 s sourced debunk at 60-75% ("The problem with that story is…", then the measurement). No "let us set the theories aside". COMPATIBLE (rule 4).
11. **Vocabulary.** Keep the term, define in ≤12 words, reuse it 3+ times ("a flank collapse, the side of the cone sliding into the sea"). One "in plain terms" translation per number-dense minute. Superlative always with comparator and unit ("1,720 feet, higher than the Empire State Building with its antenna"); "one of the most X in the United States" 2-3× per script with the count. COMPATIBLE (rules 3, 5, 11).
12. **One object per segment.** One vivid object (water tower, safe, tombstones) per chapter, never stacked; one named victim with age, job and a sourced quote per tragedy. COMPATIBLE (rules 11, 16).
13. **Close.** Fact + dated forward window, then the CTA spine once. No aphorism, no mirrored callback, no "This was The Warning Hour." COMPATIBLE (rules 7, 14).

## 4. Packaging decision
- **Historical docs (banked four, Joplin, Tri-State):** archive photograph + heavy upright caps, place name in frame, human-scale fact as text ("158 DEAD IN 32 MINUTES"), year in title only. No AI storms, no BREAKING bar.
- **Forecast explainer (El Nino doc):** School B: official NOAA/CPC map or SST globe as the photograph, white first line, red payoff word, region + verdict. Map and arrow allowed; no chyron.
- **Live US minis:** School C with our own "THE WARNING HOUR" bug, never a network bar; map with 3-4 city labels, one red arrow, 2-4 word present-tense text. Texas template retained.
- **Title rule:** searchable Name+Year in the first 40 characters, total ≤52 characters (hypothesis cutoffs: TV ~40, mobile ~45-50, desktop ~55-60; verify in Studio). No superlative adjectives, no ALL CAPS in titles.
- **Series identity, 10-15 El Nino videos:** fixed type family, blue/amber palette, round "EL NINO 26-27" badge bottom-left; variable = state photograph + state name. Title spine `El Nino Winter 2026-27: <State/Region>: <verdict>`.
- **El Nino doc, chosen:** title `El Nino Winter 2026-27: What 1982 and 1997 Did to Your State` (60 chars, over the 52 cap; fallback `Super El Nino 2026: What Happened Last Time`, 43). Thumb: split, 1997-98 California mudslide photo (NOAA/USGS) left, CPC Dec-Feb outlook map right, text "YOUR STATE, THIS WINTER". Test & Compare against "STRONGEST SINCE 1997" over the SST globe.
- **Hurricane-peak mini, chosen:** title `Hurricane Season 2026 Peak: The Silence Before October` (52). Thumb: split, empty 2026 GOES-East frame left, 2005 GOES frame right, text "IT'S NOT OVER", our bug top-right, Florida/Carolinas labels.
- **Fix now:** respell "ERUPTIONS", add "ANAK KRAKATAU" line 1; replace Texas BREAKING bar with our bug and add Dallas/Houston labels.

## 5. Shorts pipeline
**Verdict: GO, capped at a 10-Short test, after the El Nino doc ships.** Ray watches "ten at a time" in the truck; Walt tolerates only real tape with a date. Audience-age check at Short 10: <40% aged 35+ = stop.
Recipe:
1. `shorts/<slug>/BRIEF.md`: source wav, word indices from `audio/aN-sM.words.json`, 5-6 clip paths, 6 text lines, one send-line.
2. `scripts/short_cut.py`: trim by word times (+250 ms tail), TTS send-line with `_voiceref_24k.wav`, loudnorm -14 LUFS, sentence-chunked `captions.srt`.
3. `shorts-9x16.html` template, 1080x1920, 30 fps: cover-crop clips at 1.03x slow scale, one 130 px text line per 10 s block, captions lower third, 3 s end-freeze on the long video's thumb.
4. 45-58 s, 2-3 cuts per 10 s, 150 wpm as-is, no music above a -24 LUFS drone, no trending audio.
5. Frame 1 = real footage + spoken number inside 1 s.
6. Render `hyperframes render --width 1080 --height 1920`, hevc 8-12 Mbps.
7. QC: downscale to 360x640 and read every line; trim starts and ends on a sentence; slice avoids the 8:26 CTA.
8. Upload: Related video = the exact long video; pinned comment with timestamp deep link; reply to first 5 comments within the hour.
9. One per day, 6-7 pm ET; alternate footage-first vs map-first openings, keep the winner.
10. Kill at Short 10 if <100 related-video taps or long-video weekly views not up ≥10%.
First five: S1 Smithville car and water tower (`a5-s1.wav`); S4 22 minutes / 83% false alarms (`a8-s2.wav`); S5 Joplin sirens that cried wolf (ep1 `a2-s1`+`a2-s2`, "Let that number sit" removed); S3 Browns Ferry three miles away (`a4-s3.wav`); S2 six transmitters dark (`a2-s2.wav`).

## 6. El Nino documentary brief (20-22 min, ~3,300 words at 150 wpm, public inside 7 days)
**Opening 60 s:** 5-8 s of archive tape with burned-in date (1998 California mudslide or 1983 Malibu surf), silent. Then: "On [day], the Climate Prediction Center put the odds of a very strong El Niño this winter above ninety percent. The last two times it did that, the winters were 1982-83 and 1997-98." Lower-48 map. Promise: "Inside twenty minutes you will know what those two winters did to your state, and what the same agency says to watch for by November." No teaser, no "will history repeat", no comment ask.
**Chapter order:** 1 CPC advisory, the Niño-3.4 number, named forecaster quote (90 s). 2 What a very strong El Niño is, one mechanism in two sentences and a picture (jet stream shifts south). 3 California: 1982-83 and 1997-98 floods, mudslides, dollars. 4 Texas and the Gulf: rain, tornado outbreaks, hay and cattle. 5 Florida: 22-23 Feb 1998 tornadoes, 42 dead, named victim. 6 Pacific NW and Upper Midwest: warm dry winter, snowpack, ski and heating. 7 Northeast: snow drought, gas bill (EIA). 8 The silent Atlantic peak folded in (El Niño suppressing hurricanes, 3 min). 9 Debunk block: HAARP / "faked records", sourced. 10 What the 1982-83 forecasters got wrong, sourced. 11 Watch-for list by date, checklist, CTA spine once.
**US-stake lines by region:** West: "If you live between Sacramento and San Diego, both of those winters put water in living rooms; 1997-98 was the wettest February on record in Los Angeles." Gulf/Texas: "Ray's ground: wetter, cooler, more February tornadoes; USDA pasture moisture in 1998 was the highest of the decade." Florida: "The night of February 22, 1998, seven tornadoes killed 42 people in Central Florida, the deadliest outbreak in the state's history." Northwest/Upper Midwest: "Seattle and Minneapolis ran warm and dry; 1997-98 snowpack in the Cascades finished below half of normal." Northeast: "Boston to Philadelphia saw the least snow of the decade; EIA heating-gas demand fell, and the bill with it." Nationally: "An El Niño winter is the only winter forecast the CPC issues with better than nine-in-ten confidence; everything else here is what happened, not what will."
**Three risks:** (1) Timing: 400k-sub channels publish this week; miss 7 days and the cluster forms around them. (2) The "fear-mongering / you were wrong" wall in two months: every forward claim sourced to CPC/NOAA by name in narration, history in flat declaratives. (3) Splitting the week into the mini lane: the hurricane-peak mini is untested and diverts effort; fold it into chapter 8 unless the owner overrides (Q3).

## 7. Open questions for the owner
1. Studio traffic-source, impressions and CTR tables for all 8 uploads, plus ep2's last-7-day vs first-7-day CTR: the whole doc-vs-mini thesis rests on one video without them.
2. Current subscriber count and returning-viewer share; and Krakatau #3 vs #4 impressions (free A/B on the same topic).
3. Hurricane-peak mini: fold into the El Nino doc (recommended) or build as a separate 10-min mini with the School C thumb?
4. Approve amending humanise rule 7 (thesis opener allowed before 0:60) and rule 8 (max 3 chapter-exit questions), or keep both rules and accept ep2's hook is banned?
5. Which thumb actually shipped on ep2 (AI tornado or the Tuscaloosa live frame)? The "no AI storms" rule is unproven until we know.