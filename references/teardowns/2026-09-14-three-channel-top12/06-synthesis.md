# The Warning Hour — Krakatau Post-Mortem & Next-Episode Brief
*Showrunner review, 2026-09-14. Sources: `channel-review/deep/{earthdesk,szone}-manifest.json`, `earthdesk/{1kbtGbtc6qA,NbOTGnETto4}.txt/.comments.txt`, `szone/Sk2Y8IQ3p7E.txt/.comments.txt`, `earthdesk-thumbs.png`, `thumbs/grid.png`, our `ms-krakatau-sirens/edit_script.md` and `ms-krakatoa-1883/edit_script.md`.*

## 1. Why EarthDesk blew up in four days
Same channel, same voice, same title/thumbnail template, same closing device, on both flops and winners — the 200x gap (153-224 views on 7 videos → 47k-196k on the next 3) is not craft. It's topic. Sinabung (a volcano, zero name recognition) got 153 views; Campi Flegrei (zero confirmed deaths) got 47,044; Anak Krakatau twice got 173,143 and 195,871. "Krakatoa = 1883, loudest sound ever recorded" is pre-existing cultural weight no amount of scripting manufactures for Sinabung or storm "Lowell." Pace is a soft correlate, not the driver: the 3 winners cluster tightly at 143-148 wpm vs flops' 142-164 wpm, but flop `4gI3cwww9Sw` ran 25:22 near-winner pace and still got 224 views, and flop `xeLk4NWx7XQ` opens with as strong a hook as any winner and got 23 views. Length, structure, thumbnail template, and publish-lag-to-event are all controlled-for identical between winners and flops (Campi Flegrei published 5+ weeks after its underlying quake and still won). The sharpest measurable signal is comments: all 7 flops have 0-1 comments, four literally 0-byte files; the 3 winners have 22-60 comments with real geology debate and AI-slop callouts. Flops didn't get a muted reception — they got no reception, which is an impressions/reach signal upstream of the video, not a "viewers watched and shrugged" signal.

## 2. Krakatau head-to-head: what cost us the test (ranked)
1. **Surfacing, not packaging, is the primary failure.** 55-60 impressions total means the algorithm barely showed our thumbnail to anyone. A title/thumbnail fix changes CTR on impressions already granted — it cannot manufacture impressions that were never served. EarthDesk's own channel median is 188 views; these two wins are 918x-1039x outliers even for them, so the platform's per-video surfacing decision isn't gated by subscriber base or channel authority, which we also lack.
2. **Keyword-literal packaging is the biggest controllable gap.** Every competitor thumbnail puts "Anak Krakatau"/"Krakatoa"/"erupts" as dominant on-frame text. Both our thumbnails omit the volcano name entirely ("THE IMPOSSIBLE TSUNAMI," "6+ ERUPTIONS IN A WEEK") — nothing for a "Krakatoa" search/suggested-panel match to grab.
3. **Format mismatch.** Competitors ran rolling breaking-news updates (no chapters, no CTA, present-tense cold open) matching "Krakatoa eruption" search intent exactly. We ran retention-engineered mini-docs (siren mechanics, 1883 history-first, Alaska analog) — a different genre answering a different intent, under the same keyword.
4. **Zero-history channel** (4 subs, first-ever Krakatau upload) has no watch-history signal to match against — compounds #1 but doesn't fully explain it, since EarthDesk's own low-median channel still broke out from a similar starting position on this topic.
5. **Length/CTA interruption** (40-60% shorter than competitors, mid-roll ebook pitch) plausibly hurts session/AVD post-click, but with single-digit clicks it had no chance to matter yet. Lowest-ranked cause.

## 3. What all three do that we don't — do tomorrow
| # | Change | Evidence | Mark |
|---|---|---|---|
| 1 | Volcano name dominant in title + thumbnail, drop "Why" framing | 23/23 cards; H2H flags as our #1 gap | COMPATIBLE |
| 2 | Cold-open on scene/stat, zero rhetorical-question hook | 12/12 top12 + earthdesk structure note | COMPATIBLE (already a rule violation regardless) |
| 3 | Serial same-premise follow-up on a developing story | EarthDesk 3x Krakatau, spacedesk 2x Nepal | COMPATIBLE |
| 4 | Cut end CTA stack to ≤1 mid-roll line, no ebook pitch inside narration | 0/12 top12 close with a subscribe ask | COMPATIBLE with humanise rules; CONFLICT with monetization goal — business tradeoff, flag not fix |
| 5 | Name a real agency/scientist, spoken verbatim quote on-screen | 10/12 top12; our `[src:N]` tags are invisible to viewers | COMPATIBLE |
| 6 | Present/real-time tense hook over past-tense death toll | 6/12 top12 + both earthdesk Krakatau hooks | COMPATIBLE |
| 7 | Close on open/unresolved tracking line, not a CTA block | 8/12 top12 + both earthdesk winners quoted | COMPATIBLE |
| 8 | Tighten toward 143-148 wpm | earthdesk winners cluster there vs flops' 150-164 | COMPATIBLE, minor |
| 9 | Reveal-flip sentences ("but here's what made it worse") | 8+/12 winners use it | CONFLICT — banned, skip |
| 10 | Self-answered rhetorical-question transitions | heavy in winners | CONFLICT — banned, skip |
| 11 | Drama-stack triads | 6+/12 winners use it | CONFLICT — banned, skip |
| 12 | "Here's"-led transitions | winner + flop use it | CONFLICT — banned, find other phrasing |
| 13 | Stay em-dash-free | no conflict observed | COMPATIBLE, confirm every draft |
| 14 | Ellipsis two-beat title ("X Is Still Happening... And Now Y") | both earthdesk winners | COMPATIBLE |
| 15 | Track impressions/comments separately from CTR before blaming packaging | H2H ranked cause #1 | COMPATIBLE — measurement discipline |

## 4. Walt and Ray
**8 agreements:** (1) EarthDesk's calm pace is appealing in principle. (2) Neither would sit through the full 22-25 min if the story repeats itself once answered — Walt bails at 12-14 min, Ray quits at the 16-min mark when Ring-of-Fire filler restates an already-answered point. (3) Both would click EarthDesk's Sep-11 title/hook over ours. (4) Both flag "Will Krakatoa KILL Another 36,000 People?" as an oversell that the script's own ending ("nobody is forecasting an 1883") walks back. (5) Both name the thumbnail typo ("6+ ERRUPTIONS/ERRUPTIONS") as a trust-costing QC failure — noting EarthDesk has its own typo ("HGIH ALERT") but on a channel that already earned trust elsewhere. (6) Both cite the same named-source line — PVMBG's Rita Susilawati, "each volcano has its own magma system, its own kitchen" — as what trust actually looks like. (7) Both distrust manufactured-suspense phrasing (Walt: "here's the thing" dressed as insight; Ray: "the obvious question is the wrong one," "here's what made it even more terrifying"). (8) Both say they'd finish our video once clicked in, on the strength of concrete lines (Walt: "nobody is forecasting an 1883"; Ray: "Do the arithmetic... twenty-seven minutes") — i.e. craft isn't the failure, packaging is.

**3 disagreements:** (1) Tomorrow's topic — Walt wants to continue the live volcano story (three more Indonesian volcanoes, per EarthDesk's Sep-14 hook); Ray wants to skip volcanoes entirely ("you already ran two Krakatau pieces this month, I've had my fill") for a NOAA El Niño winter-forecast piece. (2) Priority of fixes — Ray puts the mid-story ebook pitch in his top three ("feels like a salesman interrupting... move it to the end or cut it"); Walt's top three is silent on the CTA, prioritizing the rhetorical-question opener instead. (3) Runtime — Walt sizes his (volcano) pick at 10-12 min; Ray sizes his (El Niño) pick at 8-9 min; both are prescriptions for "tomorrow's slot" that can't both govern the same episode.

**Their pick of tomorrow's video:** Walt → continue the Indonesia volcano story short (10-12 min, map + five numbers). Ray → drop volcanoes, run the El Niño/winter-outlook piece (8-9 min, NOAA-sourced).

## 5. Pace verdict
The owner's atempo-1.10 clone (~174 wpm from a 158-wpm base) moves in the opposite direction from the nearest comparable winner: EarthDesk's long-form documentary format wins at 143-148 wpm, 15-20% slower than 174, not faster. But the evidence for pace as the lever is weak on its own terms — it's explicitly ranked the lowest-priority cause in the H2H (#5 of 5) and flagged everywhere as a "soft correlate, not sole cause" (flop `4gI3cwww9Sw` ran near-winner pace and still got 224 views). SpaceDesk's ~190-wpm faceless format also wins, at median 26k — a different genre (breaking-news bulletin, closer to szone's 184-wpm Krakatau video) than our documentary format, so it doesn't validate 174 wpm for us either; it shows two different paces work for two different formats, neither of which is ours-at-174. **Verdict: the evidence does not prove atempo 1.10 is wrong, because our one measured test (Krakatau) failed on impressions/packaging before pace ever had a chance to matter.** What to test: run the next 2-3 same-format episodes at native 158 wpm and at a 145-wpm-target slowdown, holding title/thumbnail packaging fixed to the do-tomorrow list, and read impressions (not just CTR/AVD) before drawing a pace conclusion — per do-tomorrow item 15, pace can't be judged until impressions clear the floor.

## 6. Packaging for tomorrow's video
Showrunner call: continue the live Indonesia-volcano story (Walt's pick) — it's the one that lets us test the actual do-tomorrow fixes on a like-for-like serial follow-up (item 3) rather than a topic change; Ray's El Niño pitch is logged as the deferred alternative in §7.

**3 titles (≤52 chars):**
1. "Anak Krakatau Erupts Again... And Now Three More" (49)
2. "Krakatoa Is Still Erupting, Right Now" (38)
3. "Three Volcanoes Wake Up Right After Krakatau" (44)

**Thumb spec:** photoreal night eruption render (matches EarthDesk/szone visual grammar); "KRAKATOA" or "ANAK KRAKATAU" as the dominant bold on-frame word, 2-4 word declarative caption underneath (no question mark, no "why"); proofread against the "ERRUPTIONS"/"HGIH" typo class before export — this is the one fix both Walt and Ray named independently.

**First ~45s, humanise-compliant (no rhetorical question, no reveal-flip, no drama stack, no em dash, no "here's"):**
> Lava is still glowing over Anak Krakatau tonight. Three days after a twenty five hour eruption sent ash nine miles into the sky, three more volcanoes across Indonesia started shaking within hours of each other. Sinabung. Ile Lewotobi. Marapi. PVMBG, the country's volcano monitoring agency, says the three eruptions are not connected to Krakatau or to each other. Officer Rita Susilawati put it plainly: each volcano has its own magma system, its own kitchen. Indonesia sits on more active volcanoes than any country on Earth, and right now, four of them are speaking at once.
(95 words ≈ 38-40s at the 143-148 wpm test pace from §5; pad slightly to fit the 45s mark at final read speed.)

## 7. Open questions
1. Which pace do we actually ship tomorrow — native 158, or a deliberate 145 test — given §5 says the evidence doesn't settle it either way?
2. Does the owner want the CTA/ebook cut to zero mid-roll lines for this episode specifically, to isolate the packaging test from the CTA variable Ray flagged?
3. Ray's El Niño pitch is a genuinely different topic with no brand-name lever (per §1's core finding) — worth scheduling as its own test, or shelved?
4. Do we get on-screen spoken source attribution (name + verbatim quote) into the next script now, or hold it for a second iteration after this one tests packaging alone?