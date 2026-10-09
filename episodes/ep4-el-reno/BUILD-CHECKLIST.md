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
- [ ] Merge the lane ledgers into `media/provenance.csv`

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
- [ ] Owner records the reference (only owner step)
- [ ] Probe two segments in his clone, he listens; measure pace, set the new tempo
- [ ] Re-voice the episode, retime every graphic to the new words, convert Paul's six clips to the same voice

## Edit
- [ ] Footage placed by hand under every segment that is not a full-frame graphic. Started 10 Oct 26: eight cuts in, full-frame graphics on track 2; timeline lint shows 20 picture gaps left (unbuilt documents and cards segments, A2-S10 and A3-S5 with no footage, four seam pads, the first 12 s of Z1-S3).
- [ ] The Weather Channel crew sequence (A3-S3, A3-S4): owner confirms the insert before any render
- [ ] Sound: bed, sirens, hits; mixdown listened to
- [ ] Outro card (Z1-S3)
- [ ] Gates: `python3 scripts/run_gates.py episodes/ep4-el-reno` all green
- [ ] Pin check, then draft render; absolute path posted; park for the owner
