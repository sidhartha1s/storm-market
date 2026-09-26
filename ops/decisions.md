# Decisions log

One line per decision, newest first: date, what was decided, who decided, why. Content-lane decisions in force are
summarised in `ops/ROADMAP.md`; this file is the dated record for everything else. A reversed decision gets a new
line that names the one it replaces.

| date | decision | by | why |
|---|---|---|---|
| 26 Sep 26 | Presenter circle (Paul) keeps its corner keep-out while shown; he is not shown in motion-graphics-only scenes | owner | "That's just a distraction at that point. at least for now." (`references/mg-quickref.md` "Frame and safe zones") |
| 26 Sep 26 | Text over footage: the glass card is the one treatment; beige cite card only for quoted sources over dark maps; no dark chip | owner | one surface for text over footage (`references/mg-quickref.md` "Palette and surfaces") |
| 26 Sep 26 | All text at least 5 % inside the frame: 96 px left/right, 54 px top/bottom; gate to follow (task 16) | owner | text-safe margin (`references/mg-quickref.md` "Frame and safe zones") |
| 26 Sep 26 | One stillness number: 4 s with nothing moving fails; graphics_qc idle thresholds (3.0/2.5 s) move to 4.0 s (task 17) | owner | two numbers for one rule (beat_density 4 s, graphics_qc 3.0/2.5 s) |
| 26 Sep 26 | Popfig red is #d0121f; an eyebrow only when it names the thing, never decoration or a pre-reveal number | owner | `references/mg-quickref.md` "Palette and surfaces", "Text doctrine" |
| 26 Sep 26 | Exits: panels and cards slide out; a full-frame MG scene ends on a camera move, fade-through or cut, never a hard vanish of one element mid-frame | owner | `references/mg-quickref.md` "Motion and exits" |
| 26 Sep 26 | Text doctrine: diagrams label (a line and the name, a figure reference, an equation); the narration explains; no paragraphs | owner | "they will just draw a line and mention the name of it" (`references/mg-quickref.md` "Text doctrine") |
| 26 Sep 26 | Docs plan: `references/mg-quickref.md` is the single home of MG rules; `LEARNINGS.md` split into `learnings/` by job | owner | one fact, one home; reading rules was the biggest phase of the MG trial (task 12: 38.4 % / 41.6 %) |
| 26 Sep 26 | Hyperframes pin: keep the lock, drop the currency block, bump at kickoff | owner | owner call; done in #104 (CLAUDE.md pin rule, `render_preflight.py` drift-only, kickoff `pin_ritual.py --check-only`) |
| 24 Sep 26 | Fresh hand-built MGs: Opus, not Sonnet (proposed) | trial, owner to confirm | one-brief trial: Opus faster (14.19 vs 22.29 min) and blind-judged 43/50 vs 26/50; Sonnet passed all 4 gates with a broken font path and stat spray |
| 24 Sep 26 | Full 0.25 s layout sweep not built (0 of 30 extra flags real on ep-1974); font-fidelity staging proposed instead (task 14) | eval, owner to confirm | the gates measure text in system Arial while renders use Montserrat/Inter, which hid two shipped collisions |
| 24 Sep 26 | Fixes 1-6 and the era gate merged (#94-#100) after green e2e and Opus review | owner go | bugs found by the Opus re-review of #85-#91 |
| 24 Sep 26 | Every PR: branch, code, `/simplify`, tests + E2E, PR, `code-reviewer` on Opus, merge after owner OK | owner | Sonnet reviews approved 7 bugs that an Opus re-review caught |
| 24 Sep 26 | Speed changes must not regress quality (owner scores current output ~90 %); each change lists its tradeoff and waits for the owner's merge go | owner | quality landed after many rounds |
| 24 Sep 26 | Tag `v1-stable` is the rollback point before the simplify pass; small revertable PRs, no V2 repo | owner | rollback without maintaining two repos |
| 24 Sep 26 | verify_render allows black/freeze only in declared blackouts and CTA dips; holds and the CTA body may be silent but not black or frozen | Opus review, owner go | a black CTA or frozen hold must fail |
| 24 Sep 26 | Era check: loud `[WARN]` when nothing on screen is archival, exit 0 (warn, not fail) | owner | a silent PASS hid that nothing was checked |
| 24 Sep 26 | Only the v5-sep6 CTA stays in `assets/cta/`; old versions live in git history | owner | keep only the latest CTA |
| 24 Sep 26 | Frame QC is 3 settle frames per changed composition, strict FAIL list, 2 fix rounds max | owner | v5/v11/v14/v19 churn came from wrong frames and no stop rule |
| 24 Sep 26 | Code reviewers run on Opus; Haiku never unless the owner asks | owner | review quality |
