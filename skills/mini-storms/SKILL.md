---
name: mini-storms
description: "Mini-storms — the fast lane of The Warning Hour (storm-market repo): 8–12 min seasonal / breaking / outlier videos — 8–12 min, stitched news + PD + social clips and Ken-Burns stills, narration, red emphasis text, BREAKING NEWS packaging, shipped in ≤3 h. Use the MOMENT the user asks for a quick / breaking / seasonal / outlier / news-style storm-market video (e.g. \"Krakatoa video\", \"Nepal floods quick one\", \"El Niño Texas warning\", \"seasonal video\", \"mini storm\", \"/mini-storms\"). NOT for the weekly documentary episodes — those are /storm-episode (same repo, same voice, different pace). Forked from storm-episode 2026-09-08; renamed from storm-breaking 2026-09-08 (owner)."
---

# mini-storms — the fast lane of The Warning Hour

Same channel, same repo, same voice, same claim-safe footage doctrine as `/storm-episode`.
This file is the tracked copy in `storm-market/skills/mini-storms/`; `~/.claude/skills/mini-storms` is a junction to it.
Different product: an **8–12 min information-passing video** on this week's disaster outlier,
cut like news (stitched clips + stills with motion, red stat pops, vignette, music bed), built
and shipped in **≤3 hours wall-clock including render**, with ONE owner gate.

**From 2026-09-15 the news lane ships Format C (rolling present-tense update) by default; read that section of
FORMAT.md first, then the ops slate in `ops/programme-14d.md` and the live cards in `ops/tracker.json`.**

Repo: `C:\Users\Sidhartha\Automation Projects\storm-market`
Format rulebook (measured from teardowns, lives in the repo): `references/mini-storms/FORMAT.md`
Teardowns + NexLev data: `references/mini-storms/teardowns/README.md`, `references/mini-storms/nexlev-*.md`

## Phase 0 — preflight (same as storm-episode, abbreviated)
1. `git -C <repo> fetch origin` → `git rev-list --count HEAD..origin/main`; non-zero = stale checkout.
2. Worktree BEFORE the first write: `git worktree add .worktrees/ms-<slug> -b ms-<slug> origin/main` (slug prefix `ms-`; the first two videos shipped as `br-*`).
   Absolute paths in every message to the owner.
3. Read FROM THE WORKTREE, in this order: `references/mini-storms/FORMAT.md` (this format's
   rules), then repo `CLAUDE.md` "Footage rules" + "Voice" + HARD RULEs, `config.yaml`. Skip
   DESIGN.md's documentary editing architecture except: CTA contract, Content ID protocol. Every MG rule
   (on-screen text, popfig, glass card, the presenter circle): `references/mg-quickref.md`.
4. Pin current before the first render: `python3 scripts/pin_ritual.py --check-only`; exit 3 (stale) ⇒ run `python3 scripts/pin_ritual.py` (hidden schtasks) and PR the bump now, never mid-video; exit 4 (npm unreachable) ⇒ proceed on the current pin and note it in the kickoff summary.
5. Generator tripwire still applies: no script may WRITE episode HTML. The breaking template
   compositions in `library/mini-storms/` are copied and hand-retuned per cut.

## Time budget (3 h; the clock is a spec, not a wish)

| Step | Budget | Output |
|---|---|---|
| 1. Topic + packaging | 25 min | `packaging.md`: 3 titles, thumbnail text (top-of-frame, ≤4 words, BREAKING-style kicker), the 3–5 s hook sentence, intro outline, chapter list with the per-section word/time table |
| 2. OWNER GATE | — | Owner picks title/hook in chat. The ONLY gate. Never infer approval. |
| 3. Script | 25 min | `edit_script.md` (storm-episode segment format so `tts_episode.py` works unchanged), then the humanise pass (3b) |
| 4. TTS + words | 10 min | `python3 scripts/tts_episode.py episodes/ms-<slug>`: TTS, lane tempo, words.json in one pass |
| 5. Sourcing | 35 min | `media/` + `provenance.csv`; pool reused from `library/mini-storms/<topic>/` first |
| 6. Compose | 40 min | `index.html` from the breaking template set; red popfigs on every number/place/date, every overlay start resolved from `audio/*.words.json` cues (never estimated seconds; build fails on an unmatched cue) |
| 7. Static QC | 15 min | `python3 scripts/run_gates.py episodes/ms-<slug>` + `node scripts/freeze_scan.mjs episodes/ms-<slug>`, then the settle-frame pass in `references/mg-quickref.md` "Verify" (new/changed comps only, one subagent reader, two fix rounds max) |
| 8. Render | 25 min | `scripts\render.cmd ms-<slug> draft` hidden via run_hidden.vbs → owner preview → `full` |
| 9. Deliverables | 10 min | `master_deliverables.py --hevc`, metadata.md, thumbnail still candidates, private upload |

**The tracker moves with the work.** Every phase change (script, TTS, checks, preview launched/done, full render launched/done, master in the main checkout, upload) runs `python3 ops/build_tracker.py set <slug> <phase> <status> "note"` in the same turn (a new video first gets `python3 ops/build_tracker.py add <slug> <lane> "<DD Mon YY>" "<title>"`), then commit + push. A status reply naming a phase the tracker page does not show is wrong (owner 2026-09-15: three full renders and masters shipped while `ops/tracker.html` still showed 06:28 previews).

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
- **Title → hook carry (owner rule):** the hook (3–5 s, one sentence) pays off the title;
  the thumbnail phrase is said aloud inside the intro. Slightly dramatic, never false: every
  claim in title/hook must be in the script with a source.
- **Thumbnail:** owner makes it. You deliver 3 AI still candidates (nanobanana;
  `scripts/gen_ai_stills.py` is hardcoded to ep2) + the ≤4-word top-of-frame phrase + a red kicker word ("BREAKING NEWS",
  "WARNING", "IT'S HAPPENING"). Text lives in the TOP 25 % of the frame (TV impressions).
- **Instant ROI:** the 8–12 ideas are each a viewer-actionable or viewer-relevant fact
  ("if you live in…", "by Thursday…", "this number changed"). Open loops: name the biggest one in
  the hook, pay it off in the last third.

### 3. Script (`edit_script.md`)
- **Brief the writer with `references/script-quickref.md` + `references/flag-words.md` + the episode research
  pasted inline; the writer opens no other rule file.** The bullets below are that file's mini-storms-specific additions only.
- 8–12 min, sized with `scripts/word_budget.py` at the shipping tempo (repo CLAUDE.md "Voice"; the lane
  tempo lives in `config.yaml channel.tempo`). TTS-safe text rules from the same section. Mid-roll needs ≥8:00; author for 8:30+.
- Structure (owner 2026-09-08): **HOOK is 3–5 s** (owner 27 Sep 26), one present-tense sentence that pays off the
  title (spoken + red popfig) → **INTRO to ~1:10** (base the point: stakes numbers, open loops,
  promise of the payoff/checklist) → **CHAPTERS** (8–12 × 45–75 s, one red-stat pop minimum each,
  a "but/and/however" connective into the next, each opening on a 1–2 s caps card on black) →
  PAYOFF (open loop closed) → WARM CLOSE (preparedness, never fearmongering) → subscribe line.
- **Retention architecture is a hard rule from #4 on (FORMAT.md "Retention architecture", owner 2026-09-11):** the
  voice never narrates what the MG shows (dates, clock times, counts go on screen, the voice says the human line);
  stakes order not chronology; one open question at all times and every chapter ends by asking the next; no
  roadmap or structure announcements; hook confirms the click with a specific present-tense image, never a
  proper noun the audience does not know; one named person per tragedy; fact dumps become a clock / scorecard /
  equation card; "and you" by minute two; "not happening" is one line in the payoff; the ending lands the thesis
  before the END CTA spine; chain seams with but / because / which means. Score the draft script on stakes per
  90 s (1–10 per window) and map every loop's open and close time BEFORE TTS; two dips in a row = rewrite.
- **Size every section in words BEFORE TTS** with `scripts/word_budget.py` (probe two segments at the
  shipping tempo). Write the table (section, start–end, words, job) in `packaging.md`. A script that
  is short on words is short on runtime. CTA position per `config.yaml channel.cta`.
- **CTAs and interaction beats (FORMAT.md ledger, owner 2026-09-09):** hard cap 3 per video incl. the fixed END CTA,
  excl. Paul's; where-are-you-watching once (fresh wording); one mid-video question or think-it-yourself beat invented
  per episode; optional name-drop; breadcrumbs uncounted. Placed by judgment, never back to back.
- **Homographs are a TTS trap:** list, senses and the probe-before-respelling rule live in
  `references/homographs.md`, gated by `scripts/homograph_scan.py`. Owner's phrases are verbatim — never
  paraphrase a line he wrote.
- Every fact carries an inline `[src: …]` before TTS; zero open `[verify]` markers. Primary
  sources (USGS, NOAA, NHC, BNPB/BMKG, NWS, ReliefWeb) beat competitor videos.
- Segment IDs `A1-S1…` with `> ` blockquote narration, exactly the storm-episode format.

### 3b. Humanise pass (owner 2026-09-13)
Before TTS, run `references/humanise-rules.md` rules 2–14 line by line on the whole script; keep the diff in the episode folder.

### 5. Sourcing (generous, multi-source, credited)
Priority order, per clip:
1. Pool reuse: `library/mini-storms/<topic>/` (provenance.csv rows travel with the file).
2. Public domain / govt: USGS, NOAA, NASA, FEMA, Coast Guard, national agencies of the event
   country, Wikimedia Commons (check licence per file).
3. Stock: Pexels / Pixabay (owner rule: ≤10 picks ⇒ thumbs on localhost, owner picks fast).
4. **Eyeball every pool cutter before wiring it:** one labelled contact grid (mid-frame per clip, PIL tile) read by a
   Sonnet subagent, classified ERUPTION / AIRPORT / OFFICIALS / OTHER. provenance.csv carries the source, not the
   picture; five "2026 plume" picks by file name were departure boards (Krakatau #4, 2026-09-11).
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

### 6b. Presenter circle (phase 2, standard from Texas on)
Mount Paul's 240 px circle per FORMAT.md "Presenter circle": two loops cut from the CTA master, talk gated on the
narration speech spans, hidden in the hook / CTA / close. Deliverables: `master_deliverables.py` → the 1080p
`-master.mp4` IS the upload file + SRT; no upscale step, the owner upscales by hand (2026-09-09).

### Dujuan U1 review rules (owner 17 Sep 26, hard)
- **Comps are mounted inside index.html's DOM.** Every class in a composition carries the comp's prefix (`tm-`, `sw-`, …); `scripts/css_collision.py` (inside sweep) fails any shared name. The browser gates stage comps WITH the host `<style>` blocks; a comp that passes standalone proves nothing.
- **Approved index-level layouts never move for a comp.** Popfigs and chips keep the approved classes and positions; where a card comp is the driver of the beat and the approved spot is not clear of its text, skip that popfig (list the skips in the handback). No custom zones.
- **Cards mount with their first fact**, rows land on the beat, tracks draw progressively; no comp window shows only background for >2 s (`blank_scan` counts text/media only, ids are not content).
- **Seams ≤0.8 s** between voice segments (`lint_timeline` fails otherwise); the only hole is the CTA.
- **CTA inside `config.yaml channel.cta.window_ms`**, immediately before the closing tracking segment, entered by a spoken bridge half-line ("Just a second before the last numbers…") with no blackout, dip or gap; keep the dip out.
- **A visible content change every <=8 s in every comp** (a tween on a content element's opacity/position/text/colour, not ambient drift), each element landing on its narration word; the draft must show zero `freezedetect=n=0.003:d=6` holds outside the CTA and the close. Green beat_density with a 21 s static card is what draft 1 of alert-levels shipped (17 Sep 26).
- **No edits under an episode while its render is alive** (a worker reloading mid-render captures a mixed state; JMA draft 2 thrown away 17 Sep 26). Composers wait for the lead's "render done".
- **Never write `textContent` on an element that has children** (it deletes them at runtime; the sweeping rule span vanished after the first caption in 7 alert-levels comps while every gate passed, 17 Sep 26). Swap text on a dedicated text span.
- **The freeze scan runs before the render, not after it.** `node scripts/freeze_scan.mjs episodes/<slug> [--comp a,b]` stages each comp with the host styles, steps its timeline every 0.5 s and runs the render check's own `freezedetect` on the screenshots (about 50 s per comp, against 13 to 24 min per draft). Composers iterate on it until PASS and read its `sheets-pre/` contact sheets; a render is confirmation, never the detector. It is the one browser gate allowed beside a live render (`render_busy.py --light`, needs 2 GB free, one scan at a time). `scripts/comp_lint.py` (inside sweep) fails text written on an element with children and text set in `onStart`/`onComplete`.
- **Every draft gets the settle-frame pass in `references/mg-quickref.md` "Verify" (new/changed comps only, one subagent reader, two fix rounds max)** before the owner sees it; green gates alone never clear a draft.

### 7–9. QC, render, ship
Same scripts and hidden-window rules as storm-episode. Static gates → 3–5 slice renders (40 s windows at 10 fps
around every new card, the CTA and the close; strip read by a subagent) → ONE draft → owner preview → full.
**One heavy job at a time:** `scripts/render_busy.py` refuses gates and ffmpeg batches while a render is alive.
Frames: the settle-frame pass in `references/mg-quickref.md` "Verify" (new/changed comps only, one subagent reader, two fix rounds max). `metadata.md`: first URL = `channel.cta.first_link`,
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
- An owner correction lands in its single home the same session: `references/mg-quickref.md`, a gate, or the right `learnings/` file (newest first).

## Open items (ask in the ship summary, not before)
- Instagram cookie login on this box has not been tested yet; first run verifies with one reel.
