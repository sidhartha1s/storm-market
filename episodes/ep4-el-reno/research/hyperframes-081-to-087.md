# hyperframes 0.7.81 → 0.7.87 diff (npm tarball comparison)

Method: `npm pack hyperframes@0.7.81` and `@0.7.87`, extracted both, diffed `dist/cli.js` (201,382 → 202,289 lines) and other changed files. package.json version bump is the only intermediate-version signal (no separate changelog published on npm for 82-86).

## Checked against known-burn history

- **ffprobe/ffmpeg deadlines** (`deadlineAtMs`, `3e4`, `12e4`): all constants byte-identical between versions (30s / 60s / 120s heartbeat ramp unchanged). Line numbers shifted (+79 to +1266) due to unrelated additions elsewhere in the file, but the actual timeout values did not change. No repeat of the 120s→30s regression.
- **PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS / PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS**: same env var names, same defaults (60s page-load default, 300000ms/5min protocol default), same help text. Unchanged.
- **HYPERFRAMES_FFPROBE_PATH / HYPERFRAMES_FFMPEG_PATH**: identical handling, same env var names, same preflight assignment logic.
- **`--workers` / worker distribution**: `distributeFrames`, `distributeFramesInterleaved`, `workerCount` logic unchanged.
- **Render encoder flags** (`crf`, `fps`, `libx264`/`libx265`, GPU-ban-in-distributed-mode message): unchanged, byte-identical.
- **StaticGuard**: no diff hits — appears untouched.

## Actual changes found

1. **New CLI flag `--capture-budget`** on the `capture` command (help text only found in 0.7.87): "Cooperative post-navigation budget in ms (default: 120000), separate from page-load `--timeout`; not a hard wall-clock timeout and cannot interrupt already-started native/core work." This is additive/opt-in — doesn't change default behavior of existing flags.
2. **Fast-capture "short band route" refinement**: new `deShortBandRoute` / `deShortBandMinFrames` logic feeding into `deInversionEffectiveMinFrames`, which narrows the frame-count threshold for choosing single-worker vs parallel drawElement streaming in certain cases. This is an internal capture-strategy heuristic tweak — same env var overrides (`HF_DE_SINGLE_MIN_FRAMES`, `HF_DE_PARALLEL_ROUTER`, `--workers`) still work to force a specific path if it ever picks wrong.
3. GIF palette filter (`palettegen`/`paletteuse`) gained a `${transparency}` parameter — unrelated to this repo's mp4 render path.
4. Bundled skill docs (`SKILL.md`, `references/routes/music-to-video.md`, `init-and-scaffold.md`, `lint-validate-inspect.md`) and the Studio web UI assets changed — cosmetic/doc updates, not CLI behavior.

## RECOMMENDATION: BUMP

No regressions found in any of the historically-dangerous areas (deadlines, navigation/protocol timeouts, ffprobe/ffmpeg paths, workers, encoder flags). Changes between 81→87 are additive (new opt-in flag, capture-strategy heuristic refinement with existing override knobs, doc/UI updates). Safe to bump.

If bumping, update together (must move as one set):
- `config.yaml` → `render.hyperframes_version` (repo pin)
- every `npx hyperframes@<pin>` occurrence in `scripts/` — grep `hyperframes@0.7.81` across the repo before merging the bump PR.
