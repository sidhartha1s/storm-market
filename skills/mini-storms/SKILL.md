---
name: mini-storms
description: Mini-storms — the fast lane of The Warning Hour (storm-market repo): 8–12 min seasonal / breaking / outlier videos — 8–12 min, stitched news + PD + social clips and Ken-Burns stills, narration, red emphasis text, BREAKING NEWS packaging, shipped in ≤3 h. Use the MOMENT the user asks for a quick / breaking / seasonal / outlier / news-style storm-market video (e.g. "Krakatoa video", "Nepal floods quick one", "El Niño Texas warning", "seasonal video", "mini storm", "/mini-storms"). NOT for the weekly documentary episodes — those are /storm-episode (same repo, same voice, different pace). Forked from storm-episode 2026-09-08; renamed from storm-breaking 2026-09-08 (owner).
---

# mini-storms — the fast lane of The Warning Hour

Same channel, same repo, same voice, same claim-safe footage doctrine as `/storm-episode`.
This file is the tracked copy in `storm-market/skills/mini-storms/`; `~/.claude/skills/mini-storms` is a junction to it.
Different product: an **8–12 min information-passing video** on this week's disaster outlier,
cut like news (stitched clips + stills with motion, red stat pops, vignette, music bed), built
and shipped in **≤3 hours wall-clock including render**, with ONE owner gate.

Repo: `C:\Users\Sidhartha\Automation Projects\storm-market`
Format rulebook (measured from teardowns, lives in the repo): `references/mini-storms/FORMAT.md`
Teardowns + NexLev data: `references/mini-storms/teardowns/README.md`, `references/mini-storms/nexlev-*.md`

## Phase 0 — preflight (same as storm-episode, abbreviated)
1. `git -C <repo> fetch origin` → `git rev-list --count HEAD..origin/main`; non-zero = stale checkout.
2. Worktree BEFORE the first write: `git worktree add .worktrees/ms-<slug> -b ms-<slug> origin/main` (slug prefix `ms-`; the first two videos shipped as `br-*`).
   Absolute paths in every message to the owner.
3. Read FROM THE WORKTREE, in this order: `references/mini-storms/FORMAT.md` (this format's
   rules), then repo `CLAUDE.md` "Footage rules" + "Voice" + HARD RULEs, `config.yaml`. Skip
   DESIGN.md's documentary editing architecture except: on-screen text rules, popfig, CTA contract,
   Content ID protocol.
4. Pin check: `python3 scripts/render_preflight.py` must pass; stale pin ⇒ `scripts/pin_ritual.py`
   at kickoff, never mid-render.
5. Generator tripwire still applies: no script may WRITE episode HTML. The breaking template
   compositions in `library/mini-storms/` are copied and hand-retuned per cut.

## Time budget (3 h; the clock is a spec, not a wish)

| Step | Budget | Output |
|---|---|---|
| 1. Topic + packaging | 25 min | `packaging.md`: 3 titles, thumbnail text (top-of-frame, ≤4 words, BREAKING-style kicker), the 3–10 s hook sentence, intro outline, chapter list with the per-section word/time table |
| 2. OWNER GATE | — | Owner picks title/hook in chat. The ONLY gate. Never infer approval. |
| 3. Script | 25 min | `edit_script.md` (storm-episode segment format so `tts_episode.py` works unchanged) |
| 4. TTS + words | 10 min | `python3 scripts/tts_episode.py episodes/ms-<slug>` |
| 5. Sourcing | 35 min | `media/` + `provenance.csv`; pool reused from `library/mini-storms/<topic>/` first |
| 6. Compose | 40 min | `index.html` from the breaking template set; red popfigs on every number/place/date |
| 7. Static QC | 15 min | sweep_episode, blank_scan, overlap_check, audio_levels, media_budget, 1 frame / 20 s eyeball via subagent |
| 8. Render | 25 min | `scripts\render.cmd br-<slug> full` hidden via run_hidden.vbs; draft skipped unless QC flagged |
| 9. Deliverables | 10 min | `master_deliverables.py --hevc`, metadata.md, thumbnail still candidates, private upload |

Total ≈ 3 h 05. If any step overruns 2×, ship what exists and list what was cut; never widen scope.

## Step details

### 1. Topic + packaging (`episodes/ms-<slug>/packaging.md`)
- **Topic source:** owner gives one, or you propose 3 from this week's outliers (NexLev via the
  claude7 profile, ≤6 outlier calls/day: see memory `reference-nexlev-via-claude7`; plus
  `yt-dlp --flat-playlist` on the tracked breaking channels listed in FORMAT.md). Pick
  high-demand / low-supply: an event blowing up now with few 8–15 min explainers under a week old.
- **One event, many angles, one asset pool.** Krakatoa ⇒ "what just happened", "who is at risk",
  "the 1883 precedent", "state X should watch this". Each angle = a new script + TTS over the
  SAME clip pool, re-ordered and re-trimmed. Never the same clip in the same order twice.
- **Title → hook carry (owner rule):** the hook (3–10 s, one sentence) pays off the title;
  the thumbnail phrase is said aloud inside the intro. Slightly dramatic, never false: every
  claim in title/hook must be in the script with a source.
- **Thumbnail:** owner makes it. You deliver 3 AI still candidates (`scripts/gen_ai_stills.py`
  or nanobanana) + the ≤4-word top-of-frame phrase + a red kicker word ("BREAKING NEWS",
  "WARNING", "IT'S HAPPENING"). Text lives in the TOP 25 % of the frame (TV impressions).
- **Instant ROI:** the 8–12 ideas are each a viewer-actionable or viewer-relevant fact
  ("if you live in…", "by Thursday…", "this number changed"). Open loops: name the biggest one in
  the hook, pay it off in the last third.

### 3. Script (`edit_script.md`)
- 8–12 min ⇒ **1,300–1,850 delivered words** at 150–160 wpm (measured niche pace is 160–200;
  pocket-TTS Pharaoh lands ~129, so this lane applies `atempo 1.15–1.2`, documentary lane stays
  native). TTS-safe text rules from repo CLAUDE.md "Voice". Mid-roll needs ≥8:00; author for 8:30+.
- Structure (owner 2026-09-08): **HOOK is 3–10 s**, one present-tense sentence that pays off the
  title (spoken + red popfig) → **INTRO to ~1:10** (base the point: stakes numbers, open loops,
  promise of the payoff/checklist) → **CHAPTERS** (8–12 × 45–75 s, one red-stat pop minimum each,
  a "but/and/however" connective into the next, each opening on a 1–2 s caps card on black) →
  PAYOFF (open loop closed) → WARM CLOSE (preparedness, never fearmongering) → subscribe line.
- **Size every section in words BEFORE TTS** at the delivered pace. Measure it: Pharaoh landed
  **158 wpm native** on br-elnino-california's short news sentences (2026-09-08), so no atempo;
  atempo 1.1–1.15 only if a script measures <140 wpm after TTS (long documentary sentences do).
  Plan at ~150 wpm ≈ 2.5 words/s. Write the table (section, start–end, words, job) in
  `packaging.md`; 9:30 ≈ 1,410 words, 8:30 floor ≈ 1,260, 12:00 ceiling ≈ 1,780. A script that
  is short on words is short on runtime; check `words ÷ 2.47` per segment. CTA per `config.yaml channel.cta` unless the owner says
  otherwise for this format (decision pending — see Open items).
- **CTAs and interaction beats (FORMAT.md ledger, owner 2026-09-09):** hard cap 3 per video incl. the fixed END CTA,
  excl. Paul's; where-are-you-watching once (fresh wording); one mid-video question or think-it-yourself beat invented
  per episode; optional name-drop; breadcrumbs uncounted. Placed by judgment, never back to back.
- **Homographs are a TTS trap (owner 2026-09-09, "AI-slop radar"):** pocket-TTS read "I read all the comments" as
  "I red" (past tense). Before TTS, scan every interaction line for read / lead / live / wind / tear / bass /
  close / present / record and respell the narration copy phonetically ("reed") while the script keeps the
  owner's exact wording. Listen to every interaction beat once after TTS; a wrong-tense homograph reads as AI
  slop to the audience. Owner's phrases are verbatim — never paraphrase a line he wrote.
- Every fact carries an inline `[src: …]` before TTS; zero open `[verify]` markers. Primary
  sources (USGS, NOAA, NHC, BNPB/BMKG, NWS, ReliefWeb) beat competitor videos.
- Segment IDs `A1-S1…` with `> ` blockquote narration, exactly the storm-episode format.

### 5. Sourcing (generous, multi-source, credited)
Priority order, per clip:
1. Pool reuse: `library/mini-storms/<topic>/` (provenance.csv rows travel with the file).
2. Public domain / govt: USGS, NOAA, NASA, FEMA, Coast Guard, national agencies of the event
   country, Wikimedia Commons (check licence per file).
3. Stock: Pexels / Pixabay (owner rule: ≤10 picks ⇒ thumbs on localhost, owner picks fast).
4. News broadcast: `yt-dlp` pulls, 3–5 s each narrated-over, courtesy credit in description,
   never twice the same cut, expect claims not strikes.
5. Social (Instagram / TikTok / X): `yt-dlp --cookies-from-browser chrome <url>` (Instagram
   requires logged-in cookies; the `instagram:user` extractor is broken, single posts/reels work).
   9:16 clips are mounted centre in a blurred, darkened copy of themselves + vignette, with an
   on-screen `@handle` credit in the lower-left for the clip's whole duration (Stefan Burns
   convention: "TikTok @ghiefebri"). ALWAYS narrated over, never the source audio alone.
6. Stills with motion: slow pan / push (3–6 % over the hold) via WAAPI; never a static still >4 s.
- **Storm-chaser / independent videographer footage: still NEVER without a licence.** Credit ≠
  licence. Social clips of the actual event from bystanders are the target, not chasers' reels.
- Similar-looking is fine: rain, ash, floodwater from anywhere as b-roll; only the CLAIMED
  event footage must be real and credited. Never caption generic b-roll as the event.
- Transformative floor (why this is fair use and not a clip reel): our narration over every
  clip, our overlay layer, no clip >5 s unmodified, no single source >15 % of runtime.

### 6. Compose (fast, from templates, hand-retuned)
`library/mini-storms/` holds the template compositions (create on the first run, then reuse):
`clip-hold`, `still-kenburns`, `vertical-embed-credit`, `popfig-red`, `breaking-bug`
(lower-third kicker), `overlay-vignette-grain`, `stat-card`. Copy → retune per cut. Music: one
tense bed from `assets/sfx/` (score-act1.mp3 exists) at −24 LUFS under narration, duck 6 dB on
popfigs. Cut cadence from FORMAT.md: median shot 3.5–4.5 s, hook ≤4.2 s, plus one labelled
real data-feed hold (USGS/NOAA/NASA loop, 20–40 s) every 2–3 min as a credibility anchor.
JS/WAAPI only. Red popfig (Abril, text-shadow, ≤3 words) on every date / place / number /
affected count, plus a bottom-left running data chip and word-highlight captions on the same words.

### 7–9. QC, render, ship
Same scripts and hidden-window rules as storm-episode. One draft render only if static QC
flagged something; otherwise straight to full. Frame eyeball ≈ 1 per 20 s via a Sonnet subagent
(never Read frames into main context). `metadata.md`: first URL = `channel.cta.first_link`,
courtesy credits block listing every non-PD source with @handles, chapters at each idea block.

## Standing owner rules for this format (2026-09-08)
- **Narration always sits above every bed.** Owner 2026-09-08: "if narration ain't clear, or the bgm is
  disturbing, they skip." Measured recipe from #1: narration ≈ −16 dB; score beds 0.13, rain/ambience
  0.18–0.20, rumble 0.16 (data-volume). Measure the rendered mix with `ebur128` per 15 s window: the
  momentary loudness must stay flat where narration is constant (a rise = beds stacking). Never let a bed
  swell under speech; duck it under popfigs, not the other way round.
- **Eyebrow text under a red popfig gets a local radial scrim + 38 px Arial Black with a stroke** (v3 CSS in
  br-elnino-california index.html). Glass card stays reserved for quotes.
- **No chapter cards.** Chapters butt-cut with a 0.45 s narration gap; the script's last line of every
  chapter is the connective into the next.
- Minimum hand-holding: one gate (packaging). Everything else runs to a shipped private upload.
- Ship speed beats polish; the documentary lane owns taste. But: hook, open loops, instant ROI,
  and a proper script are non-negotiable here too (owner: "the script will be proper").
- ≥8:00 runtime for mid-rolls, always.
- Thumbnail text top-of-frame, owner authors the final thumbnail.
- Reuse the clip pool across angles; reorder, never replay the same sequence.
- LEARNINGS.md updated the same session as any owner correction, under a `## breaking` heading.

## Open items (ask in the ship summary, not before)
- CTA in the breaking lane: keep the 15 s Paul ebook CTA at 30–40 %, or a 5 s end-card version?
  Default until answered: keep the contract (sweep_episode enforces it on `ep*` slugs only; the
  `ms-`/`br-` prefixes are exempt, so mount it by hand).
- Instagram cookie login on this box has not been tested yet; first run verifies with one reel.
