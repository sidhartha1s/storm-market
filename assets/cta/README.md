# assets/cta — the channel's ebook CTA (must-keep in every episode)

Owner order 2026-08-30. Placement rules: `DESIGN.md` "CTA contract". Live values: `config.yaml channel.cta`.
Deterministic gate: `scripts/sweep_episode.py` ("CTA present + placed"). SRT cue: `scripts/build_srt.py`.

## Current file
| Field | Value |
|---|---|
| File | `paul-storm-ready-v8-oct19.mp4` (1920x1080 24 fps, h264/aac, **24.417 s** of picture, audio stream 24.401 s) |
| md5 | `66e1a8b2c8fc5ebe2c3675b599a8dada` |
| Transcript | `paul-storm-ready-v8-oct19.txt` (the words are v6-oct7's, unchanged) |
| Voice | the narrator voice (19 Oct 26): v7's audio converted with Chatterbox VC to `config.yaml external.voice_ref` (`voice_ref_md5` in config), timing kept, so the lips still match. The words read back match the transcript (faster-whisper small.en). -15.4 LUFS, -4.3 dBFS peak. The picture stream is v7's, copied without re-encoding (stream md5 `676c3204cb47a62c0ac09d058f46f722` on both). `sweep_episode.py` fails when the CTA's `voice_ref_md5` differs from the narrator's, so a voice change forces a re-voiced CTA |
| Source | `C:\Users\Sidhartha\Videos\paul-v2-test\ad\hf\renders\book-ad-v3-yt.mp4` (book ad v3, owner 7 Oct 26; hyperframes render at 24 fps, transcoded at crf 22; its own audio, the v6-oct7 voice, was -14.5 LUFS, -1.4 dBFS peak) |
| QR | opens `https://www.paulraymond.online/yt/?src=qr` (decoded from the asset at 20 s and 23.8 s) |

## Version history
- **v8-oct19** (2026-10-19): CURRENT. v7 re-voiced in the narrator voice (owner: the CTA was still the old voice); picture unchanged.
- v7-oct10 (2026-10-10): book ad v3 in the owner's own voice. Retired 2026-10-19. Restore with `git show f6e52149:assets/cta/paul-storm-ready-v7-oct10.mp4 > paul-storm-ready-v7-oct10.mp4`.
- v6-oct7 (2026-10-07): book ad v3 in the cloned Flow voice: opens on the book cover and pages, then Paul on camera with the QR card, then a silent QR end card. Retired; removed from the tree 2026-10-10 (owner: the ad in his voice). Restore with `git show c4829acd:assets/cta/paul-storm-ready-v6-oct7.mp4 > paul-storm-ready-v6-oct7.mp4`.
- v5-sep6 (2026-09-06): 15.139 s, QR to the bare home page. Retired; removed from the tree 2026-10-07 (owner). Restore with `git show 59dcbea5:assets/cta/paul-storm-ready-v5-sep6.mp4 > paul-storm-ready-v5-sep6.mp4`.
- v4c (2026-08-28): HeyGen talking head, QR on chest. Retired; removed from the tree 2026-09-24 (owner). Restore with `git show <sha>:assets/cta/paul-storm-ready-v4c.mp4`.
- v4b (2026-08-23): DeAPI/LTX lipsync. Superseded.

## Swapping the clip
Never overwrite. Add the new versioned file (e.g. `paul-storm-ready-v6-<date>.mp4`) (+ `.txt`, + row above with md5), bump `config.yaml channel.cta.file/duration/transcript`. Remove the old file in the same PR; shipped episodes keep their own `media/cta/` copy, and git history keeps the old version.
