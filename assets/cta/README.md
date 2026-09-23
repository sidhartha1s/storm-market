# assets/cta — the channel's ebook CTA (must-keep in every episode)

Owner order 2026-08-30. Placement rules: `DESIGN.md` "CTA contract". Live values: `config.yaml channel.cta`.
Deterministic gate: `scripts/sweep_episode.py` ("CTA present + placed"). SRT cue: `scripts/build_srt.py`.

## Current file
| Field | Value |
|---|---|
| File | `paul-storm-ready-v5-sep6.mp4` (1920x1080 30 fps, h264/aac, **15.139 s**, 13.3 MB) |
| md5 | `541db438ad6e948e41286ee9fb6245fb` |
| Transcript | `paul-storm-ready-v5-sep6.txt` |
| Source | `C:\Users\Sidhartha\Automation Projects\newest paul CTA sep 6.mp4` (owner 2026-09-08 "newest paul CTA sep 6", 2560x1440, transcoded to 1080p30) |

## Version history
- **v5-sep6** (2026-09-06): CURRENT.
- v4c (2026-08-28): HeyGen talking head, QR on chest. Retired; removed from the tree 2026-09-24 (owner). Restore with `git show <sha>:assets/cta/paul-storm-ready-v4c.mp4`.
- v4b (2026-08-23): DeAPI/LTX lipsync. Superseded.

## Swapping the clip
Never overwrite. Add the new versioned file (e.g. `paul-storm-ready-v6-<date>.mp4`) (+ `.txt`, + row above with md5), bump `config.yaml channel.cta.file/duration/transcript`. Remove the old file in the same PR; shipped episodes keep their own `media/cta/` copy, and git history keeps the old version.
