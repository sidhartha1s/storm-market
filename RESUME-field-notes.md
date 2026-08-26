# RESUME breadcrumb — field-notes SEO build (paused 2026-08-26, owner hit 5h window)

Worktree: `.worktrees/field-notes` (branch `field-notes` off origin/main @ eb753b2). Nothing committed yet — everything below is on disk, auto-commit hook may have picked up some files; check `git status` first.

## Done (verify on disk, don't trust this list — global CLAUDE.md rule 12)
- Blog: `landing/field-notes/index.html`, `landing/field-notes/joplin-tornado-2011/index.html`
  (live video s--FjTUXU-w, YouTube-fetched metadata), `landing/field-notes/tornado-warning-vs-watch/index.html`
- About: `landing/about/index.html` (pen-name-safe, no falsifiable credentials — owner-approved framing)
- Edits: `landing/index.html` footer links block, `landing/_redirects` (+/yt/joplin), `landing/llms.txt` (full page map)
- States (agent, DONE, idle): `landing/states/` — 52 index.html (menu + 51), generator `landing/tools/gen_states.py`
  + `landing/tools/state_data.csv` (RESURRECTED from git commit 40fb265 — it is NOT on origin/main; note in PR body)
- Resources (agent, INCOMPLETE at pause): 5/8 done — MISSING: `landing/resources/index.html` (hub),
  check word counts of `tornado-safe-room` + later pages; agent name was `resources-author` (dead after session end — re-run remaining pages fresh)

## Keyword targets (Google-autosuggest validated — keep these, don't re-guess)
- emergency-binder: "emergency binder checklist/template/printables/free" (strongest commercial match)
- tornado-safe-room: "tornado safe room in house / cost / storm shelter vs safe room" (NOT "checklist")
- hurricane page: "+pdf +2026"; states: "<state> storm shelter rebate/grant" lead angle
- Blog next: ep2 dispatch when published; "why do tornado sirens go off twice" covered in warning-vs-watch

## Remaining (in order)
1. Finish resources: hub `landing/resources/index.html` + verify all 7 topic pages complete/quality
2. Spot-check 3 state pages (TX, FL, sparse row) for None/nan leaks — states agent's self-check unverified
3. Regenerate `landing/sitemap.xml` — all index.html dirs + home/privacy/terms
4. Gates: `node landing/widthcheck.mjs` on NEW pages (390/768/1280) + visual QC (shot.mjs) + `node landing/buycheck.mjs`
5. Commit → PR (small if possible; note CSV resurrection + generator rationale — tripwire does NOT apply, landing≠episode HTML)
   → auto code-review → fix findings
6. PREVIEW deploy for owner approval (NEVER production without his OK):
   `npx wrangler pages deploy landing --project-name paulraymond --branch field-notes`
   → https://field-notes.paulraymond.pages.dev — owner eyeballs, then production deploy is `--branch main`
7. After merge: GSC — submit sitemap + URL-inspect key pages (SA key: `~/.claude/google-credentials/gsc-paulraymond-sa.json`,
   property `sc-domain:paulraymond.online`; recipe in memory `reference-paulraymond-google-identity`)

## Standing constraints
- Identity wall: sidclashes2much@gmail.com stack for this site; never gws/simplotel creds here
- git/gh as sidhartha1s; rebase-merge; docs sweep (landing/README.md needs the new-pages section!) in same PR
- Owner may retitle YouTube videos — blog always fetches live YouTube metadata, never repo metadata.md
