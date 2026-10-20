# assets/cta — the channel's ebook CTA (must-keep in every episode)

Owner order 2026-08-30. Placement rules: `DESIGN.md` "CTA contract". Live values: `config.yaml channel.cta`.
Deterministic gate: `scripts/sweep_episode.py` ("CTA present + placed"). SRT cue: `scripts/build_srt.py`.

## Current file
| Field | Value |
|---|---|
| File | `paul-storm-ready-v9-oct20.mp4` (1920x1080 24 fps, h264/aac, **24.042 s** of picture (577 frames), audio stream 24.042 s, 9.4 MB) |
| md5 | `bba0b9f3289d0de3797dbfbd1017e3d8` |
| Transcript | `paul-storm-ready-v9-oct20.txt` (the words are v6-oct7's, unchanged; all of them read back from the asset with faster-whisper small) |
| Voice | the narrator voice: each take's audio converted with Chatterbox VC to `config.yaml external.voice_ref` (`voice_ref_md5` in config), timing kept. -15.4 LUFS, -3.5 dBFS peak |
| Picture | remade 20 Oct 26 (owner): Paul's on-camera shots 2 and 4 are new Omni takes made from `assets/paul/paul-sheet-c.png` and `assets/book/binder-sheet-v3.png`, downloaded at Flow's free 1080p upscale. No zoom (the old 15 % crop softened the face and read as AI); the channel logo `assets/brand/warning-hour-logo.png` covers the generator's watermark instead. Shot 3 is v8's take (Flow refused the remake twice) |
| Source | `C:\Users\Sidhartha\Videos\paul-v2-test\ad\hf-v4\renders\book-ad-v5-24fps.mp4` (hyperframes render of `ad/hf-v4/build_comp.py`, root `data-fps="24"`; transcoded at crf 22, loudnorm to -14.8 LUFS target, audio trimmed to the picture) |
| QR | opens `https://www.paulraymond.online/yt/?src=qr` (decoded from the asset at 20 s and 23.8 s) |

## Version history
- **v9-oct20** (2026-10-20): CURRENT. New Paul shots from the locked character and binder sheets, no zoom, logo over the watermark (owner: "go v5").
- v8-oct19 (2026-10-19): v7 re-voiced in the narrator voice; picture unchanged. Retired 2026-10-20. Restore with `git show fa1de4a9:assets/cta/paul-storm-ready-v8-oct19.mp4 > paul-storm-ready-v8-oct19.mp4`.
- v7-oct10 (2026-10-10): book ad v3 in the owner's own voice. Retired 2026-10-19. Restore with `git show f6e52149:assets/cta/paul-storm-ready-v7-oct10.mp4 > paul-storm-ready-v7-oct10.mp4`.
- v6-oct7 (2026-10-07): book ad v3 in the cloned Flow voice: opens on the book cover and pages, then Paul on camera with the QR card, then a silent QR end card. Retired; removed from the tree 2026-10-10 (owner: the ad in his voice). Restore with `git show c4829acd:assets/cta/paul-storm-ready-v6-oct7.mp4 > paul-storm-ready-v6-oct7.mp4`.
- v5-sep6 (2026-09-06): 15.139 s, QR to the bare home page. Retired; removed from the tree 2026-10-07 (owner). Restore with `git show 59dcbea5:assets/cta/paul-storm-ready-v5-sep6.mp4 > paul-storm-ready-v5-sep6.mp4`.
- v4c (2026-08-28): HeyGen talking head, QR on chest. Retired; removed from the tree 2026-09-24 (owner). Restore with `git show <sha>:assets/cta/paul-storm-ready-v4c.mp4`.
- v4b (2026-08-23): DeAPI/LTX lipsync. Superseded.

## Swapping the clip
Never overwrite. Add the new versioned file (e.g. `paul-storm-ready-v6-<date>.mp4`) (+ `.txt`, + row above with md5), bump `config.yaml channel.cta.file/duration/transcript`. Remove the old file in the same PR; shipped episodes keep their own `media/cta/` copy, and git history keeps the old version.
