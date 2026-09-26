# Director's notes on the wave-2 drafts (read 15 Sep 26, 00:40 IST) — for the 06:00 pass

## ms-sakurajima-ash (16 Sep slot A) — usable spine, needs the same pass slot A/B got
- Facts: 20, all JMA/Tokyo VAAC/Kagoshima City, dated 13–14 Sep. Zero named quotes; the agency bulletin line ("volcanic gas discharge
  remains generally abundant, magma continues accumulating beneath the Aira Caldera, eruptive activity is expected to continue") is the
  on-screen quote, attributed to JMA's 14 Sep 16:00 bulletin. That satisfies Format C (agency named, verbatim, on screen).
- Cut: every meta line ("this desk", "this channel will fold", "that is not a gap in reporting", "take what follows as", "Picture the
  ground under this", "Here is the mechanism the daily headlines skip", advisory numbers read aloud as "two-oh-two-six slash").
- Cut the unsourced colour in Beat 3 (ferries under the plume, residents checking wind like tide, streets swept, schools open): not in
  the sheet. Replace with sourced geography (Yoshino district, Asagiri Town, Akune) and the 13 vs 14 Sep wind swing, which IS sourced.
- Beat 7 is 350 words about what the desk could not fetch. The viewer's unknowns are three: alert level unchanged?, ashfall depth?,
  flights? Keep those, drop the rest.
- Re-pull at 06:00: JMA activity page for any 15 Sep eruption, VAAC list, Kagoshima ashfall forecast. Title stays number-first.

## ms-0916-usf-b (16 Sep slot B) — Missouri/Kansas City flash floods: LIVE but minor
- 18 facts, NWS Pleasant Hill/Des Moines, 4–7 inches, 14-county Flood Watch to 16 Sep, Des Moines 7.61 in for the month. No deaths,
  no rescues, no named local official. Two verbatim quotes (NHC's Beven on the Bermuda disturbance; the NWS office).
- Kill-rule check: "state-level flood/tornado stories under 20k every time" (four-channel data). Run it only if 06:00 shows deaths,
  rescues or a river crest; otherwise slot B goes to ms-0917-haw-b (Kauai recovery day 2: KIUC nearing 90 %, Green's $400M ask,
  23 facts) or ms-elnino-cpc-today (CPC >90 %, WMO near 100 %, 22 facts).

## ms-0917-krak-a, ms-0918-jpn-a, ms-elnino-cpc-today — drafts exist (2,550–2,700 words each, too long by ~35 %); pass them the
  day before their slot with a fresh fact re-pull. JMA raised Tokachidake to Level 3 and Typhoon 25 formed near Truk (18 Sep sheet):
  both are stronger proper-noun stories than a generic "what JMA is watching".

## Process lessons from day 1 (both slots), to fold into FORMAT.md / learnings/
1. Whisper transcript is the pronunciation gate: run TTS, read the words.json for every proper noun, respell phonetically in the
   blockquote only, re-synthesise. Cost today: ~40 min and a full retime. Do it BEFORE the timeline is written next time
   (probe-TTS the name list first).
2. Transcribe only after atempo; a words.json older than its wav (words end > wav length) is the tell. Check it before cueing.
3. The frame reviewers (Sonnet) misjudge "touches the frame edge" and "pin in the water" often; settle geometry with a pixel check
   (PIL on the snapshot or on the source map) before moving anything a second time.
4. shot_comp.mjs leaves `_shot_*.html` staging copies in compositions/; delete them before graphics_qc or it grades them too.
5. Draft render at 2 workers takes the box to 0.8 GB free with Firefox open; nothing else launches during a render.

## 15 Sep 26, 23:50 IST — decision for the 16 Sep slots
- **Sakurajima re-pull (done):** nothing dated 15 Sep on JMA, Tokyo VAAC, tenki.jp, Kagoshima City, 373news, KTS. Latest fact is the
  14 Sep 16:00 bulletin; next routine bulletin 18 Sep. Kill rule ("same-story follow-up only when the number/level moved") says
  Sakurajima does NOT ship 16 Sep unless it erupts overnight. v2 script saved (`script-ms-sakurajima-ash-v2.md`), usable in 20 min
  if it does: strip the "as of this check / no update found" meta lines, the beat-1 self-narration, and read numbers only on screen.
- **16 Sep slot A → El Niño (CPC advisory, "what the agency said this week")**: the owner's core series, CPC numbers move weekly,
  100 % US audience on the two shipped minis. Slot B → Kauai day 2 IF KIUC's number moved (wave-3 desk reports story_moved).
- Wave-3 workflow launched 23:52 IST with the day-1 rules baked in (names on screen, numerals on screen, no meta lines).


## 16 Sep 26, late (director)
- 16 Sep shipped to preview: A ms-elnino-cpc-today (draft #2 with CPC's 14 Sep weekly Niño values; the 10 Sep advisory numbers were stale by the time the first draft rendered; lesson: the weekly PDF is a Monday product and the radar must read it before every El Niño script), B ms-kauai-lowell-day2 (7:09, short because the script came in at 1,115 words; next Kauai update targets 1,350+).
- El Niño pool rebuilt after the worktree loss: 45 rows re-fetched + 35 Sept files + 49 cutters. Mudslide stock clip is an Italian coastal town; do not use.
- 17 Sep slot A (Indonesia) v1 script is on disk (1,371 words). Radar verdict: marginal (Ibu 400 -> 600 m, Semeru 1,000 m again, Lewotolok ongoing, search silent since day 6, Krakatau unchanged). KILL RULE: ships only if the 06:00 check adds a real mover (search extended/closed/found, Krakatau eruption, Ibu at or above 1,000 m, an airport). Otherwise 17 Sep A falls to the next mover.
- 17 Sep slot B: Kauai/Sakurajima/El Niño all flat at 16 Sep late. Candidates for the morning: Kauai first North Shore neighborhood back (KIUC), the Bermuda system getting a name (NHC), Sakurajima >= 3,000 m (JMA).
