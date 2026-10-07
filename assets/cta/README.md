# assets/cta — the channel's ebook CTA (must-keep in every episode)

Owner order 2026-08-30. Placement rules: `DESIGN.md` "CTA contract". Live values: `config.yaml channel.cta`.
Deterministic gate: `scripts/sweep_episode.py` ("CTA present + placed"). SRT cue: `scripts/build_srt.py`.

## Current file
| Field | Value |
|---|---|
| File | `paul-storm-ready-v6-oct7.mp4` (1920x1080 24 fps, h264/aac, **24.417 s** of picture, audio stream 24.5 s, 8.6 MB) |
| md5 | `047cd059bdc2a642f833995053aa94ac` |
| Transcript | `paul-storm-ready-v6-oct7.txt` |
| Source | `C:\Users\Sidhartha\Videos\paul-v2-test\ad\hf\renders\book-ad-v3-yt.mp4` (book ad v3, owner 7 Oct 26; hyperframes render at 24 fps, transcoded at crf 22, audio copied: -14.5 LUFS, -1.4 dBFS peak) |
| QR | opens `https://www.paulraymond.online/yt/?src=qr` (decoded from the asset at 20 s and 23.8 s) |

## Version history
- **v6-oct7** (2026-10-07): CURRENT. Book ad v3: opens on the book cover and pages, then Paul on camera with the QR card, then a silent QR end card.
- v5-sep6 (2026-09-06): 15.139 s, QR to the bare home page. Retired; removed from the tree 2026-10-07 (owner). Restore with `git show 59dcbea5:assets/cta/paul-storm-ready-v5-sep6.mp4 > paul-storm-ready-v5-sep6.mp4`.
- v4c (2026-08-28): HeyGen talking head, QR on chest. Retired; removed from the tree 2026-09-24 (owner). Restore with `git show <sha>:assets/cta/paul-storm-ready-v4c.mp4`.
- v4b (2026-08-23): DeAPI/LTX lipsync. Superseded.

## Swapping the clip
Never overwrite. Add the new versioned file (e.g. `paul-storm-ready-v6-<date>.mp4`) (+ `.txt`, + row above with md5), bump `config.yaml channel.cta.file/duration/transcript`. Remove the old file in the same PR; shipped episodes keep their own `media/cta/` copy, and git history keeps the old version.
