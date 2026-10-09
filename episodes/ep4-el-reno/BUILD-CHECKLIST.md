# El Reno v4b build checklist (started 10 Oct 26)

Owner, 10 Oct 26: "clips are good. go ahead. move faster." Status is read from this file, not from memory.

## Done
- [x] Script voiced: 80 segments, `audio/` (9 Oct 26)
- [x] Paul's six clips made, logo on, 1080p: `media/paul/ins-paul-<n>/ins-paul-<n>.mp4`
- [x] Timeline from the audio: `timeline.json` (22 min 7 s, book ad at 56.7 %)
- [x] Composition skeleton: `index.html` (74 narration tags, 6 Paul clips, book ad with dips, 5 chapter blackouts, 67 graphic hosts)
- [x] Branch brought up to main (merge, 10 Oct 26)

## Sourcing (workers write `media/provenance-<lane>.csv`)
- [ ] News footage: `media/news/` (worker src-news). Round 1: 5 usable clips, highway jam and flooding only. Round 2 running (10 Oct 26): the TV crew's own sequence, station helicopter footage of the tornado, radar on air, a drainage channel, a listen pass.
- [ ] Government documents, page captures, photos, track data: `media/docs/`, `media/pd/`, `media/data/` (worker src-pd). Round 1: 57 files, ledger matches. Round 2 running: the tornado itself, a survey team, city flooding, a siren, a slab house, radar trucks.
- [x] Stock fills: `media/stock/`, 21 clips kept of 66 fetched (Pixabay 6 of 30, Pexels 15 of 36), every strip read by eye, ledger `media/provenance-stock.csv` (10 Oct 26). Open: no usable stock for need 4 (one-storey house) or need 7 (warning siren); cover from government photos or the drawings.
- [x] Lane ledgers merged into `media/provenance.csv` (the picture gate reads it) and the tracked copy `provenance.csv` at the episode root: 105 rows, every file on disk, no duplicate (10 Oct 26). Re-merge if a lane ledger changes.

## Graphics (Opus builders; mounts and windows in `mg_specs/mounts.json`)
- [x] map21, 12 comps: built, builder's gate clean (10 Oct 26). Flood footage needed under g-i1s3-pins, comp-local 2.0 to 6.9 s.
- [x] replot, 11 comps: built, builder's gate clean, measured road layout applied to the three comps that draw both roads (10 Oct 26).
- [ ] maps, 9 comps: 9 files on disk, builder's receipt not in yet.
- [x] drawings, 7 comps: built, builder's gate clean (10 Oct 26). Traffic aerial needed under g-a5s11-returns, episode 1250.90 to 1256.20 s.
- [x] roads, 6 comps: built, builder's gate clean (10 Oct 26).
- [ ] cards, 12 comps plus the closing channel card: builder started 10 Oct 26 (mg-cards).
- [ ] docs, 10 comps: builder started 10 Oct 26 (mg-docs).
- [ ] Meaning check of each family's "must be true" list (orchestrator, as the lists arrive). Done 10 Oct 26: all seven families (cards with one change: the University of Oklahoma tile is text only; docs unchanged).
- Road layout all families share, measured from OpenStreetMap road geometry (Overpass, 10 Oct 26): US-81 lon -97.9379; Alfadale Road 1.05 mi and Radio Road 2.04 mi east of it; Reuter Road lat 35.4790; Reno Road 1.00 mi south; Interstate 40 about 1.52 mi north at US-81; research car (530 m west of Radio Road) 1.71 mi east of US-81. Metro frame px: US-81 x 503.2, Radio Road x 572.7, car x 561.5, Reuter y 518.9, I-40 y 467.2.
- [ ] Settled-frame read of every comp over its footage (Opus verifier, then one frame each by the orchestrator). Verifier mg-verify-1 started 10 Oct 26 on map21, drawings, replot, roads (36 comps); report at `.qc-tmp/verify-1/REPORT.md`. Maps, docs, cards follow.

## Voice (owner, 10 Oct 26: "my own voice will and must be the way ... clone can do good")
- [x] Owner sent his recording; cleaned to `assets/voice/owner-sid-clone-ref.wav` (untracked until he picks his voice), cloned on its own (10 Oct 26)
- [x] Owner's picks saved 10 Oct 26 02:54: Route A (tone conversion) for Paul's clips; El Reno ships in his voice once his reference is better. He likes Route A's American delivery and calls the direct clone of his voice off.
- [x] Narration through Route A proven on two segments (10 Oct 26): same words (50 of 50, 54 of 54), same length, 3.7 to 7.5 s per 17.7 s segment on the GTX 1650. No second TTS, no retime.
- [x] Tone check (10 Oct 26): his recording is boxy against the studio voice; a half-strength corrected copy is on card 5 of the page.
- [x] Owner's second recording (`20261010_034112.mp3`, 10 Oct 26 03:41) cleaned into `assets/voice/owner-sid-clone-ref-v2.wav` (studio tone) and `assets/voice/_sid-variants/ref-v2-clean-noeq.wav` (no tone fix), both untracked. Demo on Paul's clips 1 and 3 at the top of the voice page; every word kept (16 of 16, 26 of 26).
- [ ] Owner: tick `v2_go` on the voice page (studio tone, no tone fix, or not yet). That tick is the go to mount his voice.
- [ ] Staged, not mounted (10 Oct 26, 04:17): both variants of every narration wav and Paul's six clips in `.qc-tmp/voice-sid/full/<studio|plain>/`, word check in `.qc-tmp/voice-sid/full/report.json`. Script `.qc-tmp/voice-sid/v2_full.py` is scratch; the conversion tool moves into `scripts/` by its own PR once he picks.
- [ ] Convert the 80 narration wavs, Paul's six clips and the ad clip to his voice with the new reference; listen-proof by transcript; set insert file gains (audio_levels fails all six Paul clips at -8 to -11 dB against narration today).

## Edit
- [x] Footage placed by hand under every segment that is not a full-frame graphic; full-frame graphics on track 2; outro mounted; no picture gap. `lint_timeline`, `sweep_episode`, `media_budget` pass (10 Oct 26, 03:12).
- [x] Fix round done by five Opus builders (map21, drawings, replot, roads, cards) from verifier 1's 29 rows; all five report `graphics_qc` PASS 68 compositions and sweep check 7 PASS (10 Oct 26, 03:25). Committed and pushed.
- [x] Verifier 1 re-check (10 Oct 26): of its 29 rows, 27 fixed, 2 partly, 6 new. Verifier 2's first read of maps, docs and cards: 20 rows (7 maps, 8 docs, 5 cards). Findings filed in `learnings/mg.md` 2026-10-10, `references/mg-brief-template.md` 7a, `references/mg-quickref.md` "Verify", `ops/tasks.md`.
- [x] Fix round 2 (the last allowed) done for replot, drawings, roads; receipts in.
- [ ] Fix round 2 for map21 (comp edits committed 04:01, receipt not seen) and cards (running); fix round 1 for maps and docs (running). Then the verifier re-reads the maps and docs fixes.
- [x] News clips, first, middle and last frame of all eight mounts read (10 Oct 26, 04:14): the ABC aerial showed the anchor's face before 2.6 s and after 12.6 s of the file, and the KFOR creek clip opened on the station's wipe. Mounts moved inside the clean spans (`v-t1s1-jam`, `v-a1s4-jam` 9.5 s, `v-a1s4-road` from 208.41, `v-a4s4-creek` in-point 3.7). Lint and sweep pass after.
- [x] Every footage mount read (10 Oct 26, 04:20): five frames across each of the 18 stock mounts and one frame of each of the 10 stills (sheets in `.qc-tmp/cuts/`). No watermark, burned-in text or end-of-file flash. Two Moore survey photos (9286 and 9355) are 800 px wide and will look soft at full frame for their 4.05 s and 3.45 s; a larger original is worth one search.
- [ ] Graphics over their real footage: orchestrator's one frame each, after the builders' last receipts.
- [ ] The Weather Channel crew sequence (A3-S3, A3-S4): owner confirms the insert before any render
- [x] Sound layer mounted (10 Oct 26, 03:26): two baked ambience stems (`bake_beds.py`: score, rain, two sirens, every drop-out from the script), 22 swells ending on a line, 6 hits on named cues. `audio_levels` passes every bed; its only failures are Paul's six clips (file gain, fixed with the voice conversion).
- [ ] Sound still open: the TV crew clip's own sound for about six seconds after "kept recording" (the timeline leaves no gap for it and the clip is muted); mixdown with ebur128 per 15 s window; owner's ear on the bed.
- [ ] Outro card (Z1-S3)
- [ ] Gates: `python3 scripts/run_gates.py episodes/ep4-el-reno` all green
- [ ] Pin check, then draft render; absolute path posted; park for the owner
