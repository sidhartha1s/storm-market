# storm-market

US weather/disaster documentary YouTube channel. Faceless, narrated, 13-23 min episodes.
Read CLAUDE.md for the contract; references/ for the niche research + script formula.

Per-episode flow: script.md (owner design gate) -> TTS (pocket-TTS, Pharaoh voice) ->
hyperframes composition (HTML/JS authored per episode) -> render (GPU + fast-capture) ->
frame QC -> preview (owner gate) -> final.mp4. No auto-upload.
