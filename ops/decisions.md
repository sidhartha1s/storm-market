# Decisions log

One line per decision, newest first: date, what was decided, who decided, why. Content-lane decisions in force are
summarised in `ops/ROADMAP.md`; this file is the dated record for everything else. A reversed decision gets a new
line that names the one it replaces.

| date | decision | by | why |
|---|---|---|---|
| 24 Sep 26 | Every PR: branch, code, `/simplify`, tests + E2E, PR, `code-reviewer` on Opus, merge after owner OK | owner | Sonnet reviews approved 7 bugs that an Opus re-review caught |
| 24 Sep 26 | Speed changes must not regress quality (owner scores current output ~90 %); each change lists its tradeoff and waits for the owner's merge go | owner | quality landed after many rounds |
| 24 Sep 26 | Tag `v1-stable` is the rollback point before the simplify pass; small revertable PRs, no V2 repo | owner | rollback without maintaining two repos |
| 24 Sep 26 | verify_render allows black/freeze only in declared blackouts and CTA dips; holds and the CTA body may be silent but not black or frozen | Opus review, owner go | a black CTA or frozen hold must fail |
| 24 Sep 26 | Era check: loud `[WARN]` when nothing on screen is archival, exit 0 (warn, not fail) | owner | a silent PASS hid that nothing was checked |
| 24 Sep 26 | Only the v5-sep6 CTA stays in `assets/cta/`; old versions live in git history | owner | keep only the latest CTA |
| 24 Sep 26 | Frame QC is 3 settle frames per changed composition, strict FAIL list, 2 fix rounds max | owner | v5/v11/v14/v19 churn came from wrong frames and no stop rule |
| 24 Sep 26 | Code reviewers run on Opus; Haiku never unless the owner asks | owner | review quality |
