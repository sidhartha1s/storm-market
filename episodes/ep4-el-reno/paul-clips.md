# ep4-el-reno · Paul's six clips: what goes into Flow (9 Oct 26)

Status: inputs only. Nothing is generated. The lines are the owner's picks (`paul-lines.md`, review page 9 Oct 26); the hook is his line verbatim.
The prompt wording below is drafted from the saved clip rules (`references/mg-quickref.md` "Paul on screen"), not copied from an earlier prompt file: read it before spending.

## How the run goes (owner, 9 Oct 26)
"spend 1 call at a time, whisper and trasncribe if any speech defect is there. if fixable by a audio only narration run, dont rerun OMNI."

1. One clip per call, one take, 15 credits. The next call starts only after the last clip is checked.
2. Each downloaded clip is transcribed and compared word for word with its line.
3. A speech defect that a narrator take can cover (a wrong, missing or extra word while he is off screen or the mouth is not readable) is fixed with the narrator take of the same line, which the voice tool makes from `edit_script.md`. The clip is not made again.
4. A clip is made again only when the picture is the problem, or the defect sits on his mouth in full view.

## Same for every clip
- Mode: frames to video, start frame = the desk frame of @char1 already used for the book ad. One 10 second video, a single take, no variations.
- The character is called @char1 in the prompt, never by name.
- Prompt body: `@char1 sits at his desk and speaks straight to the camera. Medium shot, the camera does not move. Calm, deep, measured voice, natural small hand movement. He says exactly these words and nothing else: "<LINE>" He stops speaking and holds his look at the camera. No music, no captions, no text on screen.`

## The six lines
| Clip | Segment | Where | Words | Line (goes into the prompt as it stands) |
|---|---|---|---|---|
| ins-paul-1 | H1-S1 | frame one of the video | 17 | Twenty-one people lost their lives that night, and not one of them was inside a building. |
| ins-paul-2 | A1-S12 | end of Act 1 | 25 | Stick with me. What radar found inside that tornado is part of why twenty one lives were lost that night, and none inside a building. |
| ins-paul-3 | A2-S5 | middle of Act 2 | 26 | Their radar showed two things turning. I call the second one the tornado inside the tornado: a much smaller one, spinning hard inside the wide one. |
| ins-paul-4 | A3-S12 | Act 3, after both strikes | 24 | One crew met it moving at about fifty six miles an hour. The other met the same vortex nearly still, for about twenty seconds. |
| ins-paul-5 | A3-S15 | last line before the book ad | 19 | That night, home was the safe place. Twelve people went to hide somewhere else. How far did they go? |
| ins-paul-6 | A5-S13 | at the full 21-pin map | 24 | That is my reading of the table. No one on it was inside a sturdy building. By that count, the safest place was home. |

## Notes
- Clip 1 is cut when he stops speaking, never filled to 10 seconds.
- Clip 6 carries a lower third in the edit: "sturdy building, not a mobile home · National Weather Service".
- Clip 4 says "the same vortex". The radar paper supports it in three passages; the limit is written in `fact_check.md`.
- Six clips at 15 credits is 90. Free credits are 50 a day on one account, so six clips need two days on one account or the second account.

## Results, 9 Oct 26
All six clips are made in Flow (Omni 1.1 Flash, first frame only, one take each) and sit in `media/paul/ins-paul-<n>/raw-01.mp4` (git-ignored, 1280x720, 24 fps, 10 s). Each was transcribed and compared with its line before the next one was sent: every word is spoken, none added.

| Clip | Speech starts (s) | Speech ends (s) | Words | Tries |
|---|---|---|---|---|
| ins-paul-1 | 0.57 | 5.54 | word for word | 2 (first refused) |
| ins-paul-2 | 0.47 | 9.26 | word for word | 1 |
| ins-paul-3 | 0.40 | 9.59 | word for word | 1 |
| ins-paul-4 | 0.69 | 8.55 | word for word | 1 |
| ins-paul-5 | 0.46 | 8.23 | word for word | 1 |
| ins-paul-6 | 0.60 | 9.05 | word for word | 2 (first refused) |

- Eight approvals at 15 credits, two refused by Flow and refunded: 90 credits net. The balance read 905 after the last clip.
- Flow refused clip 1 and clip 6 once each: "Unable to generate videos that might cause reputational risk or misrepresent current events". Both passed when the prompt opened by saying this is a history documentary about the 2013 tornado and the voice note dropped "grave". The prompts that passed are in each `jobs.json`.
- The transcript check needs two passes (whole clip, then each phrase between silences): the whole-clip pass dropped ten spoken words on clip 2.
- Every clip carries Flow's grey four-point star, 48 px wide, centred near (1160, 600): "Visible watermarking is required in your region". The owner's rule (9 Oct 26): a Warning Hour logo bug sits over that spot on every Omni clip. Candidates: `assets/brand/candidates/`; his pick is on the Q page `elreno-logo.html`.

## Mount-ready clips, 9 Oct 26
The owner picked mark 2 (amber funnel on a dark badge) on the Q page. It is the channel logo: `assets/brand/warning-hour-logo.png` (512 px, transparent corners). Each `media/paul/ins-paul-<n>/ins-paul-<n>.mp4` is the raw clip scaled to 1920x1080 with the logo, 96 px wide, centred at (1740, 900), which is the star's spot at this size. The raw files are kept beside them.

| Clip | Length (s) | Pace of the raw clip (wpm) | Changes besides the logo |
|---|---|---|---|
| ins-paul-1 | 6.96 | 205 | cut 0.35 s after the last word (5.89 s), then slowed to 0.85, picture and sound together |
| ins-paul-2 | 10.01 | 171 | none |
| ins-paul-3 | 10.01 | 170 | none |
| ins-paul-4 | 10.01 | 183 | none |
| ins-paul-5 | 10.01 | 147 | none |
| ins-paul-6 | 10.01 | 170 | none |

Recipe, one clip (clips 2 to 6):
```
ffmpeg -i raw-01.mp4 -i assets/brand/warning-hour-logo.png -filter_complex "[0:v]scale=1920:1080:flags=lanczos[v];[1:v]scale=96:96:flags=lanczos[b];[v][b]overlay=1692:852[o]" -map "[o]" -map 0:a -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -r 24 -c:a copy ins-paul-<n>.mp4
```
Clip 1 adds `-t 5.89` before `-i`, `,setpts=PTS/0.85` after the overlay, and `[0:a]atempo=0.85` for the sound (re-encoded to AAC).

- Checked: one frame of every clip at 4 s, and the first and last moments of clip 4: the logo sits over the star in each. Clip 1 was transcribed again after the slow-down: every word, speech from 0.66 s to 6.50 s.
- Only clip 1 is slowed: it is the one clip well above the narrator's measured 179 words a minute.
- Still to do: mount each as `ins-paul-<n>` in the composition.
