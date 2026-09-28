## What
1. **`scripts/sfx_peak.py`** — reporting tool only (SFX timing is hand-authored in `index.html`;
   no script may author episode HTML per CLAUDE.md's tripwire). `find_peak_time()` decodes a
   sound file mono via ffmpeg and takes `argmax(|signal|)`; `eligible_hits()` reads `index.html`
   for `<audio>` elements whose id starts with `sx-` (excludes `nx-`/`ins-` and riser ids). Real
   episodes carry `data-bed` on every SFX element, hit or bed alike (see `audio_levels.py:19-20`
   and `ep-enderlin-2025`'s markup), so it cannot distinguish a one-shot hit — filtering on it
   found 0 hits on real episodes; dropped. `<video>` is no longer matched (b-roll mp4s outnumbered
   real hits 806:7 on real episodes). Prints each hit's `data-start`/`data-media-start` and where
   its peak currently lands in the timeline — a stable report, not a `cue - peak` "corrected"
   value: the old formula re-derived its suggestion from the CURRENT `data-start`, so applying it
   and re-running shifted the suggestion again every time. One line added to `DESIGN.md` "Audio
   rules (hard)" telling the editor to run it. Risers keep the existing end-of-line rule
   untouched.
2. **`scripts/pop_scan.py`**, wired into `scripts/verify_render.sh`** — frame-diff spike detector:
   downscales to 180x180 gray at the render's own fps (CPU-light on the diff math; ffmpeg still
   decodes full-resolution frames before scaling — the docstring's earlier "no full-resolution
   decode" claim was wrong and is fixed), flags a frame whose diff to BOTH neighbours is >3x the
   neighbours' diff to each other and above an absolute floor. **This is the one REPORT-only
   check in `verify_render.sh`** — every other check in that script hard-FAILs (exit 4) on a
   defect; pop-scan deliberately does not, because a real intentional quick cut/flash-edit can
   trip the same "differs sharply from both neighbours" signature, so a human call is required
   (documented in the script's own header, no more dangling "see PR" pointer). `verify_render.sh`
   also no longer re-parses fps out of `index.html` a second time (reuses `$COMP_FPS`, already
   parsed off `#root`), and guards the ffmpeg exit status so a failed decode reports "not run, not
   clean" instead of the misleading "no spike frames found".
3. **`scripts/master_deliverables.py`** — added `-colorspace bt709 -color_primaries bt709
   -color_trc bt709 -color_range tv` to the master's ffmpeg command. The master step is `-c:v
   copy` (no re-encode), so no `format=yuv420p` filter applies — verified ffmpeg still writes
   these as the output container's color metadata under stream copy (confirmed manually before
   touching the script: source tagged `unknown/unknown`, copy+tags output `bt709/tv`). Loudness
   gain logic is untouched.

No springs added (owner rejected springs in the source review this PR implements).

## Evidence
- `python3 scripts/test_sfx_peak.py`, `test_pop_scan.py`, `test_master_deliverables.py` — all
  PASS (peak-location against a sample-exact synthetic impulse; `eligible_hits()` against markup
  copied VERBATIM from real episodes — `ep-enderlin-2025`'s real `sx-stamp-ef5`/`sx-stamp-ef3`
  with `data-bed` present, a real riser, a real bed, a real `nx-` line, a real `sx-` `data-media-start`
  element, and a `<video>` with an `sx-` id; isolated-spike/smooth-motion/hard-cut/floor cases for
  the pop detector; a real ffmpeg-injected single-frame flash found at its known timestamp;
  `verify_render.sh` still exits 0 on a clean synthetic render; ffprobe on a synthetic 3s master
  shows `color_space=bt709` and `color_range=tv`).
- `sfx_peak.py` against 3 real episodes (read-only, main checkout): `ep-enderlin-2025` 41 hits,
  `ep6-katrina-2005` 52 hits, `sh-hawaii-lowell-1` 7 hits (9 real `sx-` ids minus 2 risers,
  matches exactly). Before this fix it found 0 on every real episode.
- `python3 scripts/e2e.py episodes/ep-enderlin-2025`: all 11 `scripts/test_*.py` PASS, overall
  **E2E PASS**. `ep-enderlin-2025` itself reports `RUN_GATES FAIL - sweep_episode.py` on 33
  missing media files including the CTA (`media/cta/paul-storm-ready-v5-sep6.mp4`) — confirmed
  pre-existing and unrelated to this PR: it reproduces identically on an untouched `origin/main`
  worktree (the gitignored local media simply isn't staged in a fresh worktree checkout), and
  `e2e.py`'s own design treats a legitimate gate FAIL (verdict present, no crash) as passing its
  suite, which is why the run reports overall PASS.
- Confirmed free RAM (3.7-3.9 GB) and no other live render/e2e before running; a second session's
  live `hyperframes` render was detected mid-session (different worktree) and waited out before
  the final clean e2e run above.

Simplify: reused the repo's existing ffmpeg-subprocess + regex-on-HTML pattern (same shape as
`audio_levels.py`) for `sfx_peak.py` instead of adding a new parsing layer; `pop_scan.py`'s
frame-diff math is stdlib+numpy only (no new video-processing dependency); the BT.709 change is
three flags on an existing ffmpeg call, no new code path.

## Rollback
`git revert c2c88a8e^..ae534c0e` (all commits on this branch, including the review-fix commits).

## Review
Review: Opus BLOCK (data-bed filter, video match, unstable cue) fixed in ae534c0e.
