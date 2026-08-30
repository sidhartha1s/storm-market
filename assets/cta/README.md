# assets/cta — the channel's ebook CTA (must-keep in every episode)

Owner order 2026-08-30. Placement rules: `DESIGN.md` "CTA contract". Live values: `config.yaml channel.cta`.
Deterministic gate: `scripts/sweep_episode.py` ("CTA present + placed"). SRT cue: `scripts/build_srt.py`.

## Current file
| Field | Value |
|---|---|
| File | `paul-storm-ready-v4c.mp4` (1920×1080, h264/aac, **15.104 s**, 24 MB) |
| md5 | `34b6b40bdf772d75d4c7ebf11a0e2a80` |
| Transcript | `paul-storm-ready-v4c.txt` (4 sentences; whisper-verified against the audio) |
| Source | `C:\Users\Sidhartha\Videos\storm-insert-work\render\renders\insert-v4c-final.mp4`, rendered 2026-08-28 14:51 from `comp/v4c.html` ("HeyGen Paul, QR on chest") |
| Talking head | HeyGen v2 clip (`heygen/paul-full-v2.mp4`, 9:16) of the Paul Raymond portrait (`paul-portrait-v2.png`) |
| Voice | Cloned Pharaoh pocket-TTS VO (`vo/insert.wav`), decoupled from the video track |
| On-screen | QR + `paulraymond.online`, book cover, site card |
| First shipped | ep2 v2 (owner re-cut, spliced at 8:26–8:42 outside the pipeline); ep4 = first in-timeline use |

## Version history
- **v4c** (2026-08-28) — HeyGen talking head, QR on chest. CURRENT.
- v4b (2026-08-23) — DeAPI/LTX lipsync (clips A seed 7 + B seed 11 bridged), same composite; `archive/insert-v4b-final_deapi-paul.mp4`. Superseded.
- earlier (2026-08-16) — `Videos\storm-ready-insert.mp4`, 14.8 s, first cut.
- experiment (2026-08-29) — local Wav2Lip re-sync (`local-lipsync/paul60_wav2lip.mp4`, 60 s, 540×960). Not shipped, not a CTA.

## Swapping the clip
Never overwrite. Add `paul-storm-ready-v4d.mp4` (+ `.txt`, + row above with md5), bump `config.yaml channel.cta.file/duration/transcript`. The old file stays so shipped episodes reproduce from their tags.
