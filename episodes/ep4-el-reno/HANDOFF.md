# ep4-el-reno — HANDOFF (v3 rewire, 2026-08-30, static QC green, draft render pending)

Worktree: `C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep4-el-reno-v3` (branch `ep4-el-reno-v3`).
Design: `edit_script.md` (DESIGN v3, owner-approved 2026-08-30). Timeline master: `audio/timeline_v3.json`
(27 kept segments, 1568.08 s = 26:08; owner accepted ~1 min over "around 25").

## State
- `index.html` hand-authored on the ep6 pattern; every cut placed on a spoken word
  (`audio/*.words.json` lookup — owner order "matchcut everything to the transcript").
- CTA hinge per DESIGN.md "CTA contract": a2-s3b tease → 1.2 s dip → `media/cta/paul-storm-ready-v4c.mp4`
  at 554.96 (35.4 %) with own audio → 1.0 s dip → a3-s1 payoff at 571.06. Pattern banked at
  `references/editing-patterns/ep4-cta-hinge.html`.
- Comps: `g-width-v1` (371.24, 47.5 s; v2 ring variant parked in `compositions/_alt/`), `g-turn` (578.06,
  41.0 s), `g-dimethod` (1255.60, 81.6 s). 33 snapshot frames reviewed by subagents; all flags fixed.
- Static suite (all run on the final index, 2026-08-30 evening): lint_timeline PASS (313 tags) ·
  sweep_episode PASS 15/15 incl. CTA gate, luma gate, motion gate · overlap_check v2 PASS · graphics_qc
  PASS (3 comps) · beat_density 0/3 · blank_scan PASS · audio_levels PASS (68 elements).
- Media mix (measured): video 60 % · stills 28 % (85, none > 6 s, all Ken Burns) · comps 11 %.
  Stills are over the 15 % target because 12 KTLX radar PNG plates + maps + survey docs; the KTLX
  loops from the src-radar agent (not delivered at handoff) are the swap that moves ~60 s to video.

## Inserts needing the owner's YES (audio-carrying; frames in `media/_gate/`)
1. `ins-kfor-hook` 0.00–3.50 — KFOR, "please do not ride this out in any interior closet or bathroom"
   (file `graded/hook-anchor-voice-g5.mp4`, +5 dB derived; the `__0000.00-0004.01` graded cut is silent).
2. `ins-twc-hook` 3.50–7.00 — TWC Bettes, "...and is heading right at Bettes and his team" (+3.5 dB derived).
All other broadcast pulls are muted (28 pulls, ≤ 8 s, narrated over, `.bc` grade class).

## Draft (2026-08-30 23:53) — PARKED for owner review
`C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep4-el-reno-v3\episodes\ep4-el-reno\renders\ep4-el-reno-draft.mp4`
(1568.13 s = 26:08, 1080p15 draft, 451 MB, marker 0, zero extraction failures; `verify_render.sh`:
no silence, no 6 s+ freeze; the CTA plays 554.96-570.06 with only the two designed dips detected).
Media: 118 clips re-encoded at crf 35 from `media/_orig/` (120 MB total, budget 150) — see LEARNINGS
item 14 for why (444 MB starved 14 ffprobe deadlines; the 150 MB line is real on 0.7.109).
Blackdetect spans beyond the designed dips, for the owner's eye (dark-background comps/footage, not
DOM-empty per blank_scan): 1:15 (3.5 s dark after the hook void), 6:11 (g-width open, 2.3 s),
20:06 (1.3 s), 20:55 (g-dimethod open, 6.5 s), 26:04 outro card.

## Next steps (in order)
1. Owner reviews the draft. Gates needing YES: `ins-kfor-hook`, `ins-twc-hook` (audio inserts);
   the five dark spans above; source quality at crf 35 (b-roll ~1.5 Mbps) — for the FULL render
   the trade is fewer clips vs crisper sources, owner's call.
2. Full render needs `RENDER_PIN_STALE_OK=1` (pin 0.7.109, owner: "hf 0.7.109 is fine"); launch
   hidden with a far-future `//ST` + `//Run` (never `//ST now+1` — it double-fires).
3. `python3 scripts/master_deliverables.py episodes/ep4-el-reno <basename>` (−14 LUFS master, SRT with
   the CTA cue from `data-srt-label`, 1440p HEVC upload file). `metadata.md` is drafted (first URL =
   paulraymond.online, "📘 The book mentioned at 9:15", no chapter at the CTA) — fill credits from
   `media/provenance.csv` (Wikimedia CC BY authors verbatim).
4. If src-radar delivers `media/radar/*.mp4` KTLX loops: swap the radar PNG stills (ids `kb-ref*`,
   `kb-vel*`) for loops, re-run lint + sweep, re-render.
5. PR: docs sweep already in the branch (LEARNINGS 2026-08-30 entry items 1-18, editing-patterns
   README row). Scratch for the owner to delete before merge (recursive deletes are policy-denied
   for agents): `episodes/ep4-el-reno/tmp_scenedetect/`, `_compshots*/`, and `media/_orig/` if disk
   is tight (3.8 GB).

## Known/accepted at handoff
- `nwsnorman-elreno-radar-loop-c.mp4` is MISLABELED (April 9, 2013 frames) — pulled from the wire,
  flagged in provenance; do not wire.
- DVIDS 883792 clips carry burned-in captions (`CAUTION-captioned-DO-NOT-USE-*`) — not wired.
- `wxgov-storm-photo-*` / `supercell-photo-magnuson` / `raxpol png` are licence-FLAGGED
  (`research/licence_audit.md`) — none wired.
