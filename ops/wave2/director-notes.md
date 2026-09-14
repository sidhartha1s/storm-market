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

## Process lessons from day 1 (both slots), to fold into FORMAT.md / LEARNINGS.md
1. Whisper transcript is the pronunciation gate: run TTS, read the words.json for every proper noun, respell phonetically in the
   blockquote only, re-synthesise. Cost today: ~40 min and a full retime. Do it BEFORE the timeline is written next time
   (probe-TTS the name list first).
2. Transcribe only after atempo; a words.json older than its wav (words end > wav length) is the tell. Check it before cueing.
3. The frame reviewers (Sonnet) misjudge "touches the frame edge" and "pin in the water" often; settle geometry with a pixel check
   (PIL on the snapshot or on the source map) before moving anything a second time.
4. shot_comp.mjs leaves `_shot_*.html` staging copies in compositions/; delete them before graphics_qc or it grades them too.
5. Draft render at 2 workers takes the box to 0.8 GB free with Firefox open; nothing else launches during a render.
