# ep6-katrina-2005 — RETIRED HANDOFF (episode shipped 2026-08-23)

This handoff is obsolete: the episode is rendered, mastered, and PR'd. Final state:

- **Final render:** `renders/ep6-katrina-2005-final.mp4` (28:34, 1080p30, crf16, 4.27 GB;
  hyperframes 0.7.109 under the owner's `RENDER_PIN_STALE_OK=1` override — see LEARNINGS
  "ep6 ship" for why 0.8.x is blocked on this box).
- **Deliverables:** `renders/ep6-katrina-2005-final-master.mp4` (−14.41 LUFS / TP −0.99),
  `renders/ep6-katrina-2005-final-master-hevc.mp4` (~1.62 GB, upload master),
  `renders/ep6-katrina-2005-final.srt` (575 cues). Publish copy: `metadata.md`.
- **Provenance:** merged `media/provenance.csv` (114 rows; shards kept alongside). CC-BY
  attribution block for the Wikimedia stills is in `metadata.md` — those credits are
  license-mandatory, not courtesy.
- **Known accepted nits at ship:** vx-four1 (21:54) is the collapsed Twin Span aerial, not the
  Gretna bridge (owner: "not a huge flag", reviewing the spot himself); g-mrgo base image keeps its edge-cropped
  USGS legend (owner: keep the base image); designed dark-card holds trip freezedetect/
  blackdetect (list in LEARNINGS "ep6 ship").
- **Patterns preserved** (episode folders get deleted after publish):
  `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`,
  `references/editing-patterns/ep6-glass-panel-camera-clamp.html`, overlap_check v2 note in that
  folder's README. Editorial rules live in DESIGN.md "On-screen text rules" + blackout table.

Post-publish: retention curve at 48h → map dips to beats → LEARNINGS (per metadata.md upload
protocol). Nothing else pending in this folder.
