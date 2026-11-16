# storm-market

The production repo behind **The Warning Hour**, a YouTube channel of narrated US weather and natural-disaster
documentaries presented by Paul, plus a fast news lane for breaking and seasonal storms.

- YouTube: [The Warning Hour](https://www.youtube.com/channel/UCBM-Hk07cy7IqU4cIH64_nw)
- Site: [paulraymond.online](https://paulraymond.online) (The Storm-Ready Home field manual)

Episodes so far: El Reno 2013, Palm Sunday 1965, Joplin 2011, Moore 1999, Camille 1969, Mayfield 2021, Buffalo 2022,
the Appalachian storm of 1950 and Galveston 1900 (`python3 scripts/episode.py` lists them).

## How an episode is made

Each documentary is an edit, not a voice-over laid on b-roll. The timeline is the master: narration blocks, holds
that let a moment breathe, archive inserts with their own audio, and motion graphics built from public data
(radar, tornado paths, maps).

1. **Angle and packaging**: the story angle, title and thumbnail are locked first.
2. **Script**: written in acts, fact-checked, and screened for words YouTube's transcript scan flags.
3. **Voice**: local TTS with a cloned narrator voice, word timestamps from faster-whisper.
4. **Sourcing**: public-domain, government and stock footage, with a provenance row for every clip.
5. **Compose**: each episode is an HTML composition rendered with [HyperFrames](https://www.npmjs.com/package/hyperframes).
6. **QC gates**: scripts check timing, audio levels, safe zones, clip reuse, frozen frames and blank frames before any render.
7. **Deliver**: a -14 LUFS 1080p master, English SRT and metadata.

A human owner signs off the angle, packaging, the opening hook and the draft cut. Nothing is uploaded automatically.

## Repo map

| Path | What |
|---|---|
| `episodes/<slug>/` | One folder per episode: script, edit script, composition, research, thumbnails, metadata |
| `scripts/` | Pipeline tools and QC gates (TTS, transcription, linting, render, deliverables) with tests |
| `skills/` | Claude Code skills that run the two lanes: `storm-episode` and `mini-storms` |
| `references/` | Script method, motion-graphics rules, packaging rules, news-lane format |
| `library/` | Reusable graphics, design tokens and clip pools |
| `assets/` | Presenter, CTA, music, SFX and brand files, each with its provenance |
| `learnings/` | Measured gotchas, newest first |
| `landing/` | Static site, deployed to Cloudflare Pages |
| `ebook/` | The Storm-Ready Home manual |
| `ops/` | Open tasks, decisions log, roadmap |

Start with `CLAUDE.md` (the flow and where each rule lives) and `DESIGN.md` (the editing architecture).

## Requirements

Python 3 (pyyaml, faster-whisper), Node 22+, ffmpeg, Chrome, yt-dlp, and HyperFrames via npx. Paths in `config.yaml`
point at the owner's machine; change them before running anything.

## License

Code and docs are [MIT](LICENSE). Not covered: third-party media (stock audio and footage, archive and news clips,
saved web pages), which stays under its original owners' terms listed in the provenance files beside it, and the
presenter's likeness and voice, the channel brand and the ebook manuscript (all rights reserved).
