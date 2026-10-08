# Content operations roadmap · The Warning Hour · from 2026-09-14

Owner handed content operations to the director session on 2026-09-14 ("you are my director of content operations
and creative head; I am still the CEO"). This file is the director's plan; `ops/tracker.json` is the live state and
`ops/tracker.html` is the one-look page (`python3 ops/build_tracker.py`).

## What the data says (four channels, full upload lists, 2026-09-14)
| channel | videos | ≥100k | ≥1M | how they win |
|---|---|---|---|---|
| GlobalWeather-Network | 53 | 18 (34 %) | 4 | rolling "Latest Updates" on the deadliest live disaster, a new video every time the official number moves (Nepal flood: 11 videos, 682 → 920 → 1,000 → 1,200 → 1,400 → 1,700 → 2,400 → 3,000 dead), uploads land 00:00–07:00 UTC = US evening |
| TheSpaceDesk | 81 | 18 | 1 | space weather + any live hazard, 18–23 min, ~190 wpm |
| Szone-r2w | 187 | 13 | 0 | live hazard + one mechanism the news skipped, 18–23 min |
| TheEarthDesk | 10 | 2 | 0 | same template on every video; only the name-recognition topics (Krakatau, Campi Flegrei) surfaced |
Our own Studio export: US topics get a 2–11k impression test, CTR decides; non-US topics got no test until the
packaging carried the proper noun. Texas/California El Niño minis: ~100 % US 65+ audience.

## Decisions in force
- Two lanes. **News lane** (2/day): rolling present-tense update on a live event, 10–14 min, lane tempo from `config.yaml`, no chapter
  cards, popfigs, Paul in the corner circle, one named agency/scientist quote on screen, close on the unresolved
  tracking line then one soft comment + subscribe line. **Documentary lane** (weekends): the banked tornado docs,
  repackaged per `references/packaging-rules.md` before upload.
- Copy the proven shape (title formula, thumb grammar, structure). One more failure is acceptable, not a series.
- Topic buckets each own a clip pool under `library/mini-storms/<bucket>/`: elnino, krakatau-indonesia, hawaii-lowell,
  japan, nepal, us-flood, us-tornado (evergreen).
- **Serial recycling (owner 2026-09-14):** one live story = many videos from ONE pool. Each new video carries a new
  official number, alert level or angle (what happened → who is at risk → what the agency said today → the mechanism
  → the US stake), the clips re-ordered and re-trimmed, narration written fresh with analysis. That is GWN's Nepal
  playbook and it stays inside the reused-content policy because the narration and analysis are original each time.
- Renders run in the main chat and are announced to the owner first. One heavy job at a time.
- Humanise rules stay strict (`references/humanise-rules.md`).

## Org
| seat | who | owns |
|---|---|---|
| director | Fable, main chat | roadmap, packaging lock, edit assembly, gates, renders, QC, owner comms |
| radar | Sonnet, scheduled | 06:00 IST scan of USGS/GDACS/GVP-VAAC/NHC/SPC/CPC/Google News + the four channels' uploads; scores candidates into `tracker.json` (idea/todo) |
| scriptwriter A, B | Sonnet | one rolling-update script each on the 8-beat skeleton, humanise pass, source list with URLs |
| sourcer per bucket | Sonnet | clip pool: PD spine, agency, licensed; provenance rows with `shot` descriptions |
| packager | Sonnet | 3 titles + thumb brief per video, spell-check, Studio Test & Compare setup |
Workers never delete; the director diffs everything before commit. Renders are never delegated.

## Daily clock (IST)
06:00 radar scan → 06:30 director picks two slots, locks packaging → 07:00 scripts (A, B in parallel) + sourcing
(pools) → 09:00 TTS → lane tempo → re-transcribe → 09:30 assemble #1 → gates → announce → render → 12:00 assemble #2
→ gates → announce → render → publish both in the US-evening window (00:00–04:00 UTC) with the pre-publish checklist.

## Programme
See `ops/programme-14d.md` (generated 2026-09-14 from the four-channel data) and the live cards in `tracker.json`.

## Kill rules
- A bucket gets two videos; if neither clears 1,000 impressions in 48 h, the bucket is parked and the pool kept.
- A same-story follow-up ships only when the official number or alert level moved, or new footage exists.
- Any thumb with a spelling error, any description without the first URL, any video without the named quote does
  not publish.

## Open asks for the owner
- Google Trends or a search API for demand proof on the radar (REMIND).
- Studio access for impressions per video after each publish (CSV export is enough).
- Add `Agent` to the permissions allow list so subagents can run without the Workflow wrapper.
