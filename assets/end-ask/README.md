# assets/end-ask — Paul's sign-off ask (every ep- documentary from Joplin on)

Owner 19 Oct 26 (Joplin, the words his, verbatim): "I genuinely appreciate you watching the video till the end. Please like
and subscribe and share your suggestions via comments. I read them all. And if you want the checklist, it's the first link
in the description." After the preview: "CTA is looking amazing. wire them to the videos for future, save assets
accordingly and correctly, dont lose." Placement rule: `DESIGN.md` "End ask". Live values: `config.yaml channel.end_ask`.
Gate: `scripts/sweep_episode.py` ("End ask present + placed").

## Current files (mounted back to back, a then b)
| File | Length | md5 | Words |
|---|---|---|---|
| `paul-end-ask-v1-oct19-a.mp4` | 9.083 s | `632818e077b958f22c719d580af0b41e` | `paul-end-ask-v1-oct19-a.txt` |
| `paul-end-ask-v1-oct19-b.mp4` | 6.417 s | `7cd5caf06614e5c8fe1b2418f0e8e772` | `paul-end-ask-v1-oct19-b.txt` |

1920x1080, 24 fps, h264/aac. How they were made (19 Oct 26):
- Omni Flash, one take each, from the desk frame of the Joplin Paul clips (`episodes/ep-joplin-2011/media/paul/inputs/paul-desk-frame.jpg`); 15 credits each.
- Voice converted Algenib to the narrator with Chatterbox VC (`config.yaml external.voice_ref`, md5 `ff03c38fefe26dc0b7adb08ea165f167`), timing kept, levelled to the narration median (-18.6 dB mean).
- Channel logo over Flow's mark per `references/mg-quickref.md` "Logo on every full-frame clip".
- Cut 0.70 s after the last word; b starts 0.40 s in, past a blip the conversion added.
- Whisper reads back the words above exactly.

## Swapping
Never overwrite. Add new versioned files (`paul-end-ask-v2-<date>-a.mp4`, ...) with their `.txt` and a row above, bump
`config.yaml channel.end_ask.files`, remove the old files in the same PR. Shipped episodes keep their own `media/end-ask/` copy.
