# ep4-el-reno v3 — post-mortem (source: `.worktrees/ep4-el-reno-v3`, read-only)

Owner verdict: "a lot of audio for the stock footages, it's messed up as is; scrap it, find
the mistakes first, adapt for the next one, footage may be reused, do not copy the edit."

Method: mechanical parse of `index.html` (164 `<video>`, 72 `<audio>` tags) with a small
Python pass (regex-parsed every element's attributes, cross-joined against `media/provenance.csv`
by filename), plus a read of `edit_script.md`, `HANDOFF.md`, `compositions/*.html`, and the
`script-os.md` / `DESIGN.md` doctrine. No video/audio was rendered or played back.

## 1. Audio audit

DESIGN.md, "Audio rules (hard)": *"Every sourced clip is muted by default. Exactly one
exception: `insert` segments, where the clip's audio IS the content."* v3 does not implement
this rule at all.

**Every single `<video>` tag in the file — all 164 — has no `muted` attribute.** Per
hyperframes-core (`data-attributes.md`): `data-volume` defaults to `1` (0 dB) when absent, and
video is only silent if explicitly `muted`. So every clip without `muted` plays its native
track at full gain.

- 6 clips are the intentional sync-sound inserts (hook testimony + CTA) — correctly labeled
  with `data-srt-label`, explicit `data-volume="1"`. These are supposed to be audible.
- **158 clips have no `data-srt-label` and no `muted` — i.e. b-roll/stock/PD/broadcast clips
  playing native audio when the design called for them silent.**

| provenance class | unintentionally-audible clips | total screen time |
|---|---|---|
| stock (Pexels/Pixabay) | 93 | 544.2 s |
| PD/govt (NWS Norman, DVIDS, weather.gov) | 37 | 225.0 s |
| broadcast-news (KFOR/KOCO/CNN/ABC/TWC graded cuts) | 27 | 143.4 s |
| other | 1 | 3.0 s |
| **total** | **158** | **915.7 s of ~1554 s runtime (59%)** |

**All 158 overlap active narration for their full duration** (checked against all 30 `nx-*`
narration windows) — every one of the 27 broadcast-news clips is a real news pull with its own
reporter/anchor dialogue, so for 143 s of the episode two people (TTS narrator + a KFOR/CNN/ABC
voice) are talking at once. This is very likely the specific thing the owner heard as "messed
up." HANDOFF.md's own claim — *"All other broadcast pulls are muted (28 pulls, ≤ 8 s, narrated
over)"* and *"audio_levels PASS (68 elements)"* — is **false against the shipped file**: zero
`muted` attributes exist anywhere in it. Either the QC gate that produced that PASS line never
checks for `muted` on `<video>`, or a later hand-edit stripped the attribute after the gate ran.

Selected list (id / start / duration / class / source) — full 158-row list available by
re-running the audit; representative early spread:

```
vx-rainwall2      9.98s   2.52s  stock            stock/rainwall-pavement-02.mp4
vx-radarloopa    23.66s   4.18s  PD/govt          nwsnorman/nwsnorman-elreno-radar-loop-a.mp4
vx-cnn-samaras   27.84s   4.22s  broadcast-news   cnn-ethics-of-chasing__hook-samaras-broll.mp4
vx-kfor-closecall 57.62s  3.74s  broadcast-news   kfor-sutton-very-close-call-a7.mp4
vx-josefy       274.24s   6.00s  broadcast-news   kfor-sutton-josefy-up-close__3-9.mp4
vx-cnn-family  1466.24s   6.50s  broadcast-news   cnn-samaras-family-interview-a7.mp4
```

**Second, independent stacking problem in the sfx/score layer:** 42 non-narration `<audio>`
elements (beds, sirens, scores) exist alongside the 30 narration tracks. **65 pairs of
sfx/score beds overlap each other AND active narration simultaneously** (e.g. `sx-bed-1` +
`sx-score-1` + `sx-siren-a1` all stacked under `nx-a1s1b`). Combined with the 158 unmuted video
clips, large stretches of the episode carry narration + 2 SFX/score layers + native clip audio
at once — a four-way audio pile-up, not a mix.

## 2. Structure audit vs `script-os.md`

**Dominant question:** never written as the required single sentence (*"the viewer keeps
watching to find out ___"*). The closest thing is the thesis in `a0-s3`/`a0-s8`: *"the men who
understood this storm best were the ones it caught"* + the EF3-vs-record-width paradox. This is
a strong thesis and it does function as an implicit dual question ("how did it kill the
experts" / "why does the record book say EF3 for the biggest tornado ever"), but it was never
converged into the one required sentence — a documentation gap against Layer 1 rule 1, not
necessarily a viewer-facing one.

**Acts and exit hooks** (from `edit_script.md` "Runtime" + "Act briefs"):

| act | window | exit hook |
|---|---|---|
| A0 hook+thesis | 0:00–1:14 | thesis reveal → 1.5 s void (time shift into flashback) |
| A1 Moore (11 days earlier) | 1:16–4:07 | location/time shift into A2 (darkening sky) |
| A2 the storm | 4:08–9:09 | **consequence** — "that gap...was about to close on some of the most experienced observers alive" → CTA |
| CTA | 9:10–9:25 | dip → payoff sentence |
| A3 the turn | 9:26–14:11 | consequence/reveal (Cobalt) → 2.5 s deliberate dead-air |
| A4 exodus+flood | 14:13–20:06 | escalation ("thirteen," "almost nobody remembers it") |
| A5 why EF3 | 20:07–23:02 | reveal (DI-method payoff) — informational, not forward-pulling |
| A6 reckoning | 23:03–25:32 | emotional close, deliberately no hook ("no recap") |
| A7 footnote | 25:32–25:53 | CTA sign-off, no hook (by design) |

**Chronology vs. stakes order:** mostly chronological with one flashback (A1, "eleven days
earlier") and one out-of-time explainer (A5, "why EF3" — a rating dispute resolved months
later, placed as an act). Structurally defensible (A4 disturbing/enormous → A5 cools into
analysis → A6 personal/emotional close matches the doctrine's escalation ladder), but putting
a pure-explainer beat immediately before the emotional peak (A6) is a real risk: A5 has only
one visual device (`g-dimethod`) carrying ~2:55 of screen time on a single concept, the
weakest "something materially changes every 60–90s" act in the cut.

**Minutes where nothing materially changes:** the v3 author's own cut list already removed 6
redundant segments before wiring (`a1-s3`, `a2-s3c`, `a3-s3b`, `a5-s2b`, `a6-s2b`, `a7-s2b` —
each logged as restating an adjacent beat). Of the 27 kept segments, two were flagged in
HANDOFF as a borderline keep-vs-cut call ("owner decision: keep `a4-s4` AND `a1-s1b`"):
- `a1-s1b` (60.48 s) — restates A1's "grief drives decisions" point without a new number,
  place, or mechanism; the weakest kept segment by this measure.
- `a4-s4` (75.96 s) — genuinely new (I-40/Banner Road convergence, "eight killed, every one in
  a vehicle") — correctly kept.
`a1-s1b` is the one real candidate for a v4 cut/rewrite on pacing grounds.

## 3. Graphics audit (from `compositions/*.html`)

Three comps, matching the "Graphics" table in `edit_script.md`:

- **`g-width-v1`** (a2-s2, 361.4s, 47.5s) — counter + map plate, labels `CIRCULATION WIDTH`,
  `DAMAGE PATH WIDTH`, `THE ISLAND OF MANHATTAN`, `MEASURED BY RAPID-SCAN RADAR`. This is a
  designed comparison device (bars/ranks/rail elements), not a stat card — matches the
  "any spatial claim gets a MAP" rule. Voice narrates the same number the card reveals in
  lockstep (0.5→1→2→2.6 mi), which is correct for a `graphic with VO` segment type.
- **`g-turn`** (568.2s, 41.0s) — road-map labels (`I-40`, `US-81`, `REUTER ROAD`), `ESCAPE
  MARGIN`, `FORWARD SPEED`, a verdict line. Matches the map-for-spatial-claim rule for the
  35→50 mph turn.
- **`g-dimethod`** (1245.8s, 81.6s) — two-column device: `WHAT THE RADAR MEASURED` vs `WHAT THE
  DAMAGE IMPLIES`, gauges, a `grass` element for "grass does not testify." This is the
  strongest of the three: it visualizes the actual mechanism (DI-method blind spot) rather than
  asserting the EF3 number over b-roll.

No stat-over-b-roll graphics found in the code — the three comps that exist are legitimate
designed devices. This part of v3 is not what triggered the rejection and should carry forward
largely as-is into v4 (same visual concepts, retimed to whatever v4's cut needs).

## 4. Footage worth keeping (clean provenance, grouped by act)

Everything below is currently wired in v3 with a clean provenance.csv row (PD/govt or licensed
stock) or a short (<12 s) graded broadcast cut with a matching row, **except the two flagged
items**, which need re-verification before reuse. One line per shot; full grouped dump (182
lines) was generated and is reproducible via the same parse against `media/provenance.csv`.

- **A0 (hook/thesis, 0:00–1:14):** `hook-anchor-voice-g5` (KFOR "do not ride this out," insert,
  owner-gated) · `twc-bettes-suv-toss-hookcut` (insert) · `nwsnorman-elreno-radar-loop-a`
  (real NWS radar bloom) · `stormsky-timelapse-01/supercell-timelapse-03` (stock sky).
- **A1 (Moore backstory, 1:16–4:07):** `nwsnorman-moore-may20-office-broll`, spotter-training
  a/b (PD), `docmine/cape-map` + `shear-map` + `jetstream-unstable-map` (self-made/NWS diagram
  plates), `dashboard-pov-rain-01` (stock).
- **A2 (the storm, 4:08–9:09):** `nwsnorman-elreno-radar-loop-b`, `docmine/dow-subvortex-path`,
  `docmine/storm-relative-velocity`, `wxgov-satellite-loop-elreno` (all PD/govt, mechanism
  clips), `kfor-sutton-josefy-up-close__3-9` (6 s broadcast, storm on air).
- **A3 (the turn, 9:26–14:11):** `cnn-ethics-of-chasing__0007.15-0014.55` (7.4 s, TWISTEX
  ethics context), `abc-3-storm-chasers-killed-a7` (4.9 s), `kfor-sutton-very-close-call-a7`
  (3.7 s, chaos beat) — **all three have no provenance.csv row (see §5, mistake 2)**, re-log
  before reuse.
- **A4 (exodus+flood, 14:13–20:06):** `abc-families-fleeing-highways` × 2 cuts (rows present,
  clean, ABC-verified channel), `kfor-chopper4-flooding-aerials` (silent aerial, clean row),
  `koco-one-year-ago` × 3 cuts (**no provenance row**, re-log).
- **A5 (why EF3, 20:07–23:02):** `docmine/ef0-contour-map`, `docmine/inflow-winds-callout` (PD
  diagrams, callback-eligible), **`nwsnorman/lessons-most-dangerous-tornado.mp4` is the STALE
  8.5 s video-only stub per provenance's own CAUTION note — the corrected replacement file is
  `nwsnorman-lessons-most-dangerous-tornado-full.mp4`; v3 wired the wrong one (see §5, mistake
  3).**
- **A6 (reckoning, 23:03–25:32):** `wikimedia-samaras-car-PDgov` (PD, ≤5 s), `cnn-samaras-family-interview-a7`
  (**no provenance row**), `nwsdoc-henderson-overtaken` (**no provenance row**).

## 5. Top ten mistakes, ranked

1. **Every `<video>` element ships without `muted`, breaking DESIGN.md's "muted by default"
   rule wholesale.** 158 non-insert clips (59% of runtime) play native audio under narration;
   27 of them are real news dialogue colliding with the TTS voice. This is almost certainly
   the specific defect the owner heard. **Fix for v4:** author every non-insert `<video>` with
   `muted` explicitly (don't rely on a default that isn't enforced); add a mechanical
   pre-render check — grep every `<video>` lacking `data-srt-label` for a missing `muted`
   attribute — to the static gate suite (`lint_timeline.py` or a new one-purpose check), since
   this is exactly the "mechanical, repeated, must never be forgotten" case CLAUDE.md carves
   out for code.
2. **HANDOFF.md certified a QC state ("audio_levels PASS," "28 pulls muted") that the shipped
   `index.html` does not have.** The gate that produced that PASS line does not check for
   `muted` on video, or the attribute was stripped after the gate ran and never re-verified.
   **Fix:** re-run the actual gate against the actual file before writing any HANDOFF claim;
   never let a doc assert a QC result the artifact doesn't currently hold.
3. **20 of ~27 wired broadcast/graded clips have no `media/provenance.csv` row at all**
   (`kfor-sutton-very-close-call-a7`, `kfor-sutton-josefy-up-close`, `cnn-ethics-of-chasing`
   ×3 numbered cuts, `koco-one-year-ago` ×3, `kfor-retrospective-2026` ×3,
   `koco-reshaped-8s`, `nwsdoc-henderson-overtaken`, `cnn-samaras-family-interview-a7`,
   `kfor-sutton-studio-interview` ×2, `abc-3-storm-chasers-killed-a7`, `twc-bettes-returns-a7`,
   `koco-10yr-anniversary`). `edit_script.md`'s own sourcing plan calls for a "deterministic
   diff of wired `src=` vs `provenance.csv` before the static suite" — it was never run, or its
   findings were ignored. **Fix:** run that diff for real before any render; every wired
   broadcast filename must resolve to a provenance row before it's usable evidence.
4. **A known-stale asset was wired anyway:** `nwsnorman/lessons-most-dangerous-tornado.mp4` is
   flagged in its own provenance row as an 8.5 s video-only stub, explicitly superseded by
   `nwsnorman-lessons-most-dangerous-tornado-full.mp4`. v3's A5 wired the stale stub.
   **Fix:** grep provenance notes for CAUTION/STALE/mislabel before wiring any asset, not just
   at initial sourcing time — re-check at wire time too, since the correction postdated the
   first pull.
5. **65 sfx/score-bed pairs stack simultaneously with active narration**, on top of the video
   audio bleed above — a four-layer pile in places (narration + 2 beds + clip audio).
   **Fix:** treat SFX as the "library, not mandate" it's meant to be — one bed + one swell at a
   time per doctrine, not a rumble + a score + a siren concurrently; run an ebur128/volumedetect
   pass per 15 s window before render, per storm-market CLAUDE.md's own audio-mixdown gate.
6. **A1-s1b (60.5 s) is a marginal keep** — restates A1's "grief shapes decisions" point without
   a new number, place, or mechanism, and was already flagged as borderline in HANDOFF. **Fix:**
   default to cutting it in v4 unless it earns its runtime with something new.
7. **The dominant question was never written as the single required sentence** (script-os.md
   Layer 1, rule 1). The thesis works but is a paired assertion, not a single "viewer keeps
   watching to find out ___" line. **Fix:** write that sentence explicitly in v4's edit_script.md
   before drafting acts — it disciplines every downstream cut decision.
8. **A5 ("why EF3," ~2:55) sits directly before the emotional peak (A6)** with only one visual
   device carrying the whole act — the weakest "something changes every 60–90s" stretch in the
   cut. **Fix:** either split the DI-method explainer earlier (e.g., planted in A2 where the
   radar-vs-eyes theme is introduced) or compress it and let A4's flood revelation flow more
   directly into A6's emotional close.
9. **Reuse of the same source video across widely separated numbered cuts** —
   `cnn-ethics-of-chasing` appears as four different timecode excerpts (`hook-samaras-broll`,
   `0062.14-0069.88`, `0007.15-0014.55`, `0026.51-0030.12`, `0045.23-0049.70`) across the hook,
   A2, A3, and A5. Doctrine says "vary sources, cuts, and chapters" — four pulls from one
   17-minute source, however differently cut, reads as thin sourcing under scrutiny.
   **Fix:** cap any single source video at 2 non-adjacent uses episode-wide, same as the
   broadcast-cut reuse rule, and source wider for the remaining beats.
10. **CTA asset (`cta/paul-storm-ready-v4c.mp4`) has no provenance row either** — low severity
    since it's owned content, not third-party, but it breaks the "every wired file has a row"
    discipline uniformly. **Fix:** log owned/CTA assets in provenance.csv too (license: "own,"
    no claims risk) so the deterministic diff in mistake #3 has zero exceptions to reason about.
