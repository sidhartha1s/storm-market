# ep4 BUILD_STATE — resume breadcrumb (update after every stage)

Worktree: `C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep4-el-reno` (branch ep4-el-reno). NEVER build in main checkout.

## Done (verified on disk)
- edit_script.md: design v2 owner-approved + full SCRIPT (33 segs, TTS-safe). Facts: research/facts.md (+ Bettes section verified).
- TTS + transcribe: audio/*.wav + *.words.json 35/35 (33 segs + 2 probes). 31.3 min narration.
- timing.json: master timeline 1965.09s (32.75 min). 8 blackout dips. GAP=0.7 between narration segs.
- Sourcing COMPLETE, nothing paid: media/ 282 files + 21 gated broadcast candidates (media/broadcast/ + frames in media/_gate/). provenance.csv reconciled 0 orphans. Inventory: research/asset_inventory.txt.
- Radar: media/radar/ 26 ref + 4 vel KTLX self-rendered frames (22:23–00:18 UTC). render_radar.py now parameterized (C:/nexrad-t/).
- Insert gate packet: research/insert_gate_packet.md (9 shortlisted; verbatim-transcript upgrade in progress via gate-shortlist agent). OWNER MUST APPROVE inserts before any render.
- clip_hunt.md: full provider list (owner asked for it).
- hyperframes pin bumped 0.7.81→0.7.87 (config.yaml + scripts/render.cmd; diff review research/hyperframes-081-to-087.md).
- index.html: SKELETON only (audio track 0 + blackout dips track 1 + track comments). Picture windows/graphics hosts NOT yet authored.
- Graphics agents in flight: gfx-width (g-width-v1/v2), gfx-turn (g-turn-v1/v2), gfx-efscale (g-efscale-v1/v2), gfx-support (g-title, g-stat-elreno, g-quote-robinson, g-tweet-nws, g-evac, g-numbers, g-gearing, g-outro) → compositions/.

## Remaining (order)
1. Review graphics agent outputs: graphics_qc + staged snapshots (subagent reads frames), pick v1-vs-v2 per key graphic, polish.
2. Author picture windows act by act in index.html (cut on words.json; subject-family spacing ≥3-4 min for reuse; rehook = real PD/broadcast clip every 45-60s; stills 4-7s, video 8-12s; holds reasoned).
3. Cold-open hook (contract in DESIGN.md): EAS/NWR anchor audio ≤2.5s, date/place card 1st second, sonic spine, void end. Assets: radar bloom + AI wedge stills (DeAPI — TO GENERATE, sparingly: rain-wrapped wall ×2, multi-vortex, night underpass flood, empty rural road).
4. Music/SFX beds: check assets/music/ library first (library not per-episode); duck −14dB.
5. Owner insert gate: send packet (9 clips, one yes/no each) BEFORE render.
6. Static QC suite ALL green (sweep_episode, blank_scan, beat_density, graphics_qc, lint_timeline, render_preflight/media_budget) — render is the LAST step.
7. Draft render via scripts\render.cmd ep4-el-reno draft (detached, harness-tracked bg job, NOT foreground Start-Process — that killed the first TTS chain). verify_render.sh post-render. Post preview path + PARK.

## Owner orders this episode (beyond repo docs)
- PD + stock only, NOTHING paid. DeAPI for AI gap-fills, sparingly.
- Repeats OK only if non-obvious: ≥3-4 min spacing, different context/grade.
- Multi-version key graphics, pick best (visual-first: show the mechanism).
- Full absolute paths in every message. Episode target ~32-35 min (owner OK'd "whatever you're planning").
- Blackout dips restored (8 placed in timing.json). Minimal graphic text.
