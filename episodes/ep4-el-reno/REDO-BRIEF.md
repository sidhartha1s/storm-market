# ep4 El Reno — REDO BRIEF (owner-approved 2026-08-02)

The first ep4 build (branch `ep4-el-reno`, worktree `.worktrees/ep4-el-reno`) was REJECTED:
its picture track was machine-injected (`build_picture.py` from `research/shot_ledger.md`) —
the forbidden generator pattern (see CLAUDE.md TRIPWIRE). Owner-identified failures: clip
CURATION (a volcano clip in a tornado doc; sunny calm-summer stock under menace narration)
and MOTION. **Script/TTS/timing/research were audited 2026-08-02 and are GOOD — salvage them.**
The redo = hand-authored picture track + compositions, ep2 method, per-cut judgment.

## Ground rules for the redo session
1. Run the `storm-episode` skill preflight FIRST (steps 1–6, incl. generator tripwire +
   hyperframes version check — `research/hyperframes-081-to-087.md` has the last bump notes).
2. New worktree from origin/main. NEVER build on the old `ep4-el-reno` branch.
3. Salvage by selective checkout from the old branch, assets only (list below).
4. Every salvaged media file gets a fresh frame-by-frame eyeball against its narration beat
   BEFORE wiring — the asset POOL is usable, the prior CURATION is not. Volcano/sunny-stock
   class errors came from wiring unwatched clips.

## SALVAGE (checkout from branch `ep4-el-reno`, paths relative to `episodes/ep4-el-reno/`)
```
edit_script.md                       # ~5000w narration, audited KEEP — documentary voice, open loops land
audio/                               # 33 segments + words.json, 31.3 min, maps 1:1 to script — do NOT re-TTS
research/facts.md
research/footage_sources.md
research/clip_hunt.md
research/clip_hunt_broadcast_stock.md
research/clip_hunt_cc_govt.md
research/insert_gate_packet.md       # owner-gated inserts
research/asset_inventory.txt
research/hyperframes-081-to-087.md
research/refs/                       # 6 competitor teardowns
media/_orig/  media/dvids/  media/ai/   # + rest of media pool as needed (3.5 GB, 504 files)
media/provenance.csv                 # candidate list, NOT gospel — re-verify rows before trusting
```
Caution: `media/broadcast/` (kfor/twc pulls) were gated preview-only — re-check provenance
era/backup-only notes before any reuse. `media/_trash/`, `*.reject` — leave behind.

## DO NOT COPY (contaminated / old-pipeline artifacts)
`index.html`, `compositions/` (wired against the injected pipeline — may be OPENED read-only
for design reference, never copied), `build_picture.py`, `inject_audio_hook.py`,
`research/shot_ledger.md`, `run_tts.cmd`, `renders/` (rejected draft), `grain.js`,
`gsap.min.js` (re-fetch clean), all `*.log`/`*.marker`/`timing.json`/`fferr.txt` run debris.

## Definition of done for the redo
Hand-authored `index.html` + `compositions/g-*.html` (Edit/Write per cut, GRAPHICS CONTRACT,
act-boundary blackouts hand-placed) → full static QC suite green → draft render → owner
review gate. Delete branch `ep4-el-reno` + its worktree only AFTER the redo ships.
