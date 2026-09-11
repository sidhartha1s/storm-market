# script-framework.md — how an episode's script is BUILT (owner-ordered 2026-09-06, ep7 kickoff)

> READ ORDER for any script/design work: this file → `references/script-scaling.md` (the
> retention lattice: cadences, acts, loop table, fact-QC) → DESIGN.md (hook contract, CTA
> contract, on-screen text rules). This file is the doctrine layer — WHY beats are shaped;
> script-scaling.md is the cadence math; DESIGN.md is the binding AV contract.

## 1. The script is ONE product: narration + visual + audio, never three
A beat is flagged "good" only when all three lanes land together. A great narration line over a
mute weak clip is a dead beat — the video is already lost. Every beat in edit_script.md is
authored as an AV UNIT: what is said, what is moving on screen, what the sound is doing — one
row, one judgment. Motion graphics get dedicated slots for information delivery; they are part
of the same product, not decoration.

- **Movement is mandatory in the hook** (and everywhere): every hook shot moves — footage with
  real motion, or a push/pan on anything static.
- **Match-cut text popups on named entities:** when the narration names the thing, the text of
  that thing lands ON the word ("Hurricane Harvey" → popup HURRICANE HARVEY; "Houston" → HOUSTON
  in the danger red; "the United States government" → that phrase as text). Reveal on the spoken
  word, narration order, narration wording (DESIGN.md on-screen text rules).

## 2. Hook doctrine (the "BMW rule" + ROI-first)
The clicker just read the title and thumbnail. Second zero must CONTINUE that exact frame — a
villains title opens in villain-language; opening the video by speaking the title is allowed.
Any first beat outside the title's frame reads as "not the video I clicked" → bounce.

- **Give the ROI in the hook, withhold only the explanation.** State the information (the
  verdict, the answer, the list) up front; the viewer stays for WHY, not WHAT. A hook that hides
  the list ("four things did this... stay to find out") is weak. Owner's apple example: name
  a-b-c-d in the hook/intro; the video explains why each matters.
- **No fluff or vocabulary risk** ("alibi" flagged) — short factual hammer lines; facts carry
  the rage-bait, not adjectives.
- **Hook may flow into the intro with no blackout** when the design says so (ep7); the 1.5s void
  remains the default punctuation (DESIGN.md hook contract) unless the episode's design overrides.
- Narrator-from-zero MAY be the hook (ep7 deviation, owner-ordered) — the broadcast-anchor-by-
  2.5s contract stays the default for episodes that don't explicitly override it.

## 3. ROI drip — how the promise is paced across the runtime (AVD is the target)
The payoff is never dumped early and never hoarded to the end. Structure:

- **Hook = the endpoint, flashed forward.** State the conclusion (ep7: the court named the
  government). The episode then EARNS it; the final act returns to the hook's scene and pays it
  in full detail. The hook is a promissory note the last act redeems.
- **Intro = the full WHAT** (the roster, the list, the claim) — the viewer's ROI is delivered as
  information within the first ~2 minutes. Everything after is WHY/HOW — that's what they stay for.
- **Each act closes one item (a mini-payoff) and plants the next** — small ROI every act, on the
  loop-table discipline (script-scaling.md). An act that only teases is a dead end; an act that
  closes everything kills the remaining runtime.
- **Escalation order:** items are sequenced so the LARGEST reveal (the one the hook flashed
  forward to) completes only in the final act. If the biggest payoff lands at minute 7, the last
  13 minutes are unwatched — re-order until the strongest material is load-bearing at the end.
- **Continuity devices:** but / therefore / however chain every seam — never "and then". Micro-
  loops every 30-45s per the lattice.
- **CTA anchor (editorial):** after the FIRST title-payoff seam, never before — the viewer must
  have received proof the video delivers before being sold to. Mechanically this lands inside
  the config 30-40% window (ep7: ~28-35%, first villain-reveal seam; config window is the gate).

## 3b. MG composition doctrine (owner, ep7 draft-v1 review 2026-09-06 — supersedes any "exit everything" reading)
- **Story elements STAY while relevant.** If the apple landed at :02 and the orange lands at :15,
  the apple stays on screen — the viewer sees the story accumulate. Remove an element only when it
  is no longer relevant to what is being said (e.g. a comparison bar whose beat has fully passed and
  whose zone is needed). Never a one-element-per-segment slideshow — that reads awkward and empty.
- **Only narration-matched words.** On-screen text carries what the voice is actually saying, in its
  wording, nothing more. No observer notes, no attribution eyebrows, no clever asides. "This is an
  apple named Bob" on the voice ≠ "an apple from the Australian countryside named Bobby" on screen.
- **Position with space.** Elements that persist get placed with breathing room — never stacked into
  one band. Check where every persistent element sits at every later beat, including against SHAPES
  (bars, lines), not just other text — the text-only overlap gate cannot see a bar under a headline.
- **Minimalism is the register.** It is a documentary; nobody pauses to read. If a line requires a
  pause to parse, it is cut or shortened.

## 4. Working agreement per episode
- edit_script.md carries the hook AS AN AV TABLE (t / picture / text-popup / audio / narration),
  not narration-only prose.
- Every hook line that carries a factual claim gets a `[verify]` leash until the research corpus
  confirms it; structure survives fact-adjustment, wording bends.
- The acts/topics list is a MENU at design time; order is finalized only after hook + intro are
  locked, applying §3's escalation order.
