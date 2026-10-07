# Landing page — The Storm-Ready Home

Static site, no framework, no server logic. Since the 2026-09-06 Binder redesign every page is **generated**: `python3 landing/tools/build_home.py && python3 landing/tools/build_pages.py && python3 landing/tools/gen_states.py`, then `python3 landing/tools/gate_migration.py`. Money and email both live on Gumroad — the paid manual at
`/l/ebook`, the free state packets at `/l/packet`. Deploys to Cloudflare Pages as-is.

**Live at https://paulraymond.online** (Cloudflare Pages project `paulraymond`; `paulraymond.pages.dev` is the same build). Redeploy with
`npx wrangler pages deploy <this dir> --project-name paulraymond --branch main`.
**`--branch main` is required** — without it wrangler publishes to a preview alias named after your
git branch and production silently keeps serving the old build.

| File | What |
|---|---|
| `index.html` | **Generated** by `tools/build_home.py` (Binder design, 2026-09-06). Edit the content strings in that script, never the HTML. Inline CSS from `tools/chrome.py`; Google Fonts is the only CDN dependency. |
| `tools/chrome.py` | The one shared chrome for every page: CSS, urgency band (viewer count, rolling 2h45-3h countdown, CTA), pinned index-tab nav, dock, toast, legal footer, JS. Change it here, then rebuild all three generators. |
| `tools/build_pages.py` | Generates the 16 hand pages (about, privacy, terms, 404, yt, field-notes, resources) from the pre-Binder copies in `tools/_orig/`. Tab labels live in its `TAB_LABELS` dict. |
| `tools/gate_migration.py` | **Gate.** Every page vs `main`: old visible text present, JSON-LD equal, no lorem / em dash / #000, buy path present. Run before any deploy. |
| `privacy.html`, `terms.html` | Generic text-only legal pages, linked in the footer, noindexed. |
| `og-src.html` | Source for `assets/og.png` (1200×630 social card). Regenerate: `node shot.mjs og-src.html ./out 1200`, crop to 630. |
| `assets/` | Cover + headshot (compressed JPEGs; the PNG originals remain as source), OG card, four real page shots, five Paul photos (selfie, plywood, binder, field kit, stage). |
| `gumroad/` | The two Gumroad surfaces (custom product page + storefront profile) and their checkers. |
| `buycheck.mjs` | **Gate.** Reads the buy button's *resolved* href in a real browser and confirms it reaches a live checkout. |
| `widthcheck.mjs` | **Gate.** Fails if the page scrolls sideways at any width. |
| `shot.mjs` | Full-page screenshots at true device widths. |
| `field-notes/` | Blog ("Field Notes"): one dispatch per published episode + evergreen field guides. Each dispatch embeds the live YouTube video at the top. |
| `resources/` | Seven checklist pages + hub — free to read on the page (SEO layer). The printable pack (`/l/checklists`) and the state packets (`/l/packet`) are email-gated via free Gumroad products; every page carries the $9.99 book as the primary CTA. |
| `states/` | 51 state guides + menu, **generated** by `tools/gen_states.py` from `tools/state_data.csv`. Edit the CSV or the template in the script, re-run `python3 tools/gen_states.py`, commit the output. Never hand-edit a state page. |
| `yt/` | Landing page for video viewers (QR code, description link): the video's promise, price, refund and buy button on one screen. Noindexed, not in the sitemap or `llms.txt`. Source `tools/_orig/yt/index.html`, a one-sheet page in `build_pages.py`. |
| `about/` | Author page. Method-led, pen-name framing — no falsifiable credentials, ever (owner-approved 2026-08-26). |
| `llms.txt`, `sitemap.xml` | Page map for crawlers/LLMs. Regenerate the sitemap whenever a page is added (it lists every `*/index.html` except the noindexed `yt/`). |

## Sale tracking: which video sold the book

Gumroad records a sale's source only when the buy link carries all three of `utm_source`, `utm_medium` and
`utm_campaign`; it then shows them in the sales CSV export and the sales API. The shared script in `tools/chrome.py`
(`SRC_JS`) copies the visitor's tag onto every Gumroad link on every page and keeps it for the browser session.
A visit with no tag leaves the links untouched. Two ways to tag a link into the site:

- **The three utm fields.** This is what the `/yt/<slug>` lines in `_redirects` send (`youtube / video /
  <slug>`), so a description link that uses `/yt/<slug>` is traced. A bare
  `https://paulraymond.online` link carries no tag and stays untraced: that is what `config.yaml` `first_link` and
  the published descriptions use today.
- **The short form `?src=<how>`**, for a URL that must stay short: `qr` for the QR in the book ad, `desc` for a
  description link. It becomes `youtube / <how> / evergreen`. There is no per-episode part (owner 6 Oct 26): the
  tag says how the buyer arrived, not which video. Both should point at `https://www.paulraymond.online/yt/?src=<how>`.

Check: `node landing/buycheck.mjs "https://www.paulraymond.online/?src=test"` prints `FAIL ... lost the src tag`
for the band or dock CTA if the tag did not reach it. Its exit code is no use yet: buycheck also fails on the live
site for an older reason (it looks for a `#buy` element the Binder design does not have, and for checkout markers
Gumroad no longer serves). Use the throwaway tag `test` for checks (it becomes `youtube / test / evergreen`); `qr` or `desc` would be counted with real visits.
Not yet proven with a real sale: that Gumroad attributes a purchase made through a `?wanted=true` link.

## Content pages (added 2026-08-26) — the rules

- **Shared design language.** Every content page copies the landing tokens (paper/storm-sky
  palette, Fraunces / Source Serif 4 / IBM Plex Mono, mono kickers) and the shared nav:
  Field Notes · Free Checklists · State Guides · YouTube · red **Get the Book — $9.99** button
  (sticky nav, the only solid-red control; ≤540px shows brand + book button only). Inline CSS
  per page, no build step — same as `index.html`.
- **Book first, candy second (owner 2026-08-26).** The $9.99 book is the product; free pages are
  the sample. Every content page carries the book in the sticky nav, a sample strip, a book CTA
  card with the real cover (`assets/cover-mini.webp`, never a CSS fake) and the footer book
  row. The printable pack and state packets are email-gated through free Gumroad products
  (`/l/checklists` — owner creates it, copy in `gumroad/checklists.md`; `/l/packet?variant=`).
- **Blog metadata comes from YouTube, never from `episodes/<slug>/metadata.md`.** The owner
  may retitle or re-describe a video after upload; the dispatch mirrors the LIVE title,
  chapters and FAQ block. Channel: https://www.youtube.com/@PaulRaymond-s9v.
- **Keyword targets were validated against Google Autosuggest (US), not guessed.** Notably:
  "safe room checklist" barely exists — the page targets "tornado safe room in house / cost /
  storm shelter vs safe room"; "emergency binder checklist/template/printables" is the
  strongest commercial cluster; state pages lead with "<state> storm shelter rebate/grant".
- **No fabricated facts, testimonials, or urgency widgets on content pages.** Figures keep
  their citation; state pages omit any section whose CSV field is empty rather than inventing.
- **Schema:** dispatches carry Article + VideoObject + FAQPage + BreadcrumbList; checklists
  carry FAQPage (+ HowTo where stepwise); state pages FAQPage; about carries Person with
  `sameAs` → the channel. Direct-answer paragraph under every H1 (AI-overview bait).
- **Search Console** is verified for `sc-domain:paulraymond.online`; API access via the
  service account documented in the owner's memory (never the Simplotel gws stack).
- **Adding an episode dispatch:** copy `field-notes/joplin-tornado-2011/index.html`, swap the
  video id + live metadata, add the card to `field-notes/index.html`, add a `/yt/<slug>` line
  to `_redirects`, regenerate `sitemap.xml`, add the URL to `llms.txt`.

## Verify

```bash
node widthcheck.mjs index.html            # must exit 0 — checks 390 / 768 / 1280
node shot.mjs index.html ./out 390 1280   # full-page PNGs to eyeball
```

Current state: **widthcheck PASS at 390, 768, 1280.**

### Two traps that cost time here, documented so they don't again

1. **`chrome --headless --screenshot --window-size=390,1500` does not give you a 390px layout.**
   Desktop Chrome enforces a minimum window width, renders wider, and crops the screenshot. The
   result looks *exactly* like a horizontal-overflow bug and is not one. Use `shot.mjs`, which
   drives CDP `Emulation.setDeviceMetricsOverride` — the only way to see what a phone sees.
2. **The cover art is 1024×1536 and must be height-capped in the hero.** Unconstrained, it pushed
   the headline and the buy button below the fold at 1280×900. Capped to 340px in the first build;
   widened to 430px in the 2026-08-13 redesign at the owner's request — CTA still lands in the
   first fold at 1280×900 (verified in `.qc-shots/redesign3+`).
3. **Scroll-reveal animation blanked the whole page in full-page captures** (and would blank it
   for no-JS readers). Removed in the redesign — content is visible by default; motion is limited
   to the hero sky, the live dot, and hovers.

## Page structure, and why it is in this order

Modelled on the two reference funnels in `../ebook/build/art/ref-yoder-cover.png` and the teardown
in the design spec, redesigned 2026-08-13 ("field-manual editorial": storm-sky hero/close
bookending an archival-paper body, Fraunces/Source Serif 4/IBM Plex Mono). The money section sits
**immediately below the first CTA and the manual description**, which is the owner's rule: the
higher the credible savings delta right below the pricing, the higher the conversion.

1. Sticky red band — live viewer count + looping launch-price countdown
2. Hero — headline, sub, no-price CTA (price is revealed at the offer), 430px cover
3. Proof strip — 486 pages, 130 protections, 23 hazards, 60 days, 7-day refund
4. Joplin story — dated narrative lead with the tornado-selfie polaroid
5. What it is — counts grid, then all 23 hazards as chips so the scope is undeniable
6. **The money chapter** — the $3,029 / $43,600 gap, sourced, with the "what this is not" box
7. Find your region — 5 cards, makes it personal before the ask
8. Field strip — three photos: plywood work, field kit, stage
9. Look inside — four real rendered pages, not a mockup
10. Reviews — **invented placeholder cards, owner-accepted for now (see below)**
11. Paul Raymond — persona block with the quote
12. What $9.99 is — price anchored against plywood/deductible/generator/hotel/unprovable loss
13. The offer — $9.99, itemised value stack to $87.99, guarantee seal
14. Free state packet — a link to the $0 Gumroad product, with the kitchen-table binder photo
15. FAQ — including "isn't this free from FEMA?", answered honestly
16. Last call
+ Sticky bottom CTA (appears after the hero, hides while the offer is on screen), a 30s
  free-packet popup, and an exit-intent / 3-minute checkout popup.

## Owner-ordered additions (2026-08-13) — and the honesty ledger that goes with them

The first build deliberately omitted reviews, per-line dollar values, the countdown, and the
viewer counter (see git history for the original reasoning). The owner has since explicitly
ordered all four, so they exist — with these standing caveats on the record:

- **Reviews are invented placeholders.** The owner reviewed them and ordered them kept as-is with
  the in-file warning marker removed (2026-08-14, "reviews are fine for now / no marker"). The
  standing recommendation on the record is unchanged: swap in real, verifiable buyer quotes once
  they exist — fabricated reviews presented as genuine are an FTC liability.
- **The value stack** itemises $14.99/$19/$15/$19/$20 (the manual's line is its value, not the $9.99 price) → "$87.99 total value". Owner-approved anchoring;
  nothing has sold separately at those prices.
- **The countdown is evergreen** (a deadline 2h45 to 3h away, kept in localStorage, rolls over on expiry) and
  **the viewer counter is decorative** (15 to 30, drifting by at most 2 every 6 to 10 s; owner 6 Oct 26). Both are aesthetic
  urgency, ordered by the owner, not measurements.

## Status

1. **Gumroad is wired and carries the files.** `GUMROAD_URL` at the top of the page script points
   at `/l/ebook`; the offer button and the exit-intent popup rewrite themselves to `?wanted=true`
   direct checkout. The product carries the 486-page manual, the 61-page binder and the state-packet
   zip, and an explicit 7-day refund policy. Contact email: owner decided 2026-08-14 there is none —
   footer + legal pages say "reply to your purchase receipt", and all support runs through Gumroad.

   The Cloudflare Web Analytics beacon block was removed from the page; enable analytics via the
   dashboard toggle on the Pages project if wanted (it injects its own beacon).
2. **The free state packets ship from Gumroad too** (`/l/packet`, $0, all 51 in one zip). This
   replaced a Cloudflare Pages Function that forwarded signups to Kit: it needed a `KIT_API_KEY`
   that never existed, so it 500'd on every real submit while the page promised a packet. Gumroad
   already does the email capture and the delivery, so the function and its Kit dependency were
   deleted rather than configured. **There is no server logic in this project any more.**
3. **The book is written, sourced, laid out and counted.** All **130 of 130** protections and all
   **23 of 23** hazard playbooks, plus front matter, people/places, the 60-day sequence, 61 pages of
   fillable binder forms, 13 original diagrams, a credits page, Sources and the 51-state directory.
   Every claim carries a full citation and a retrieval date; claims that could not be traced to a
   primary document were cut rather than softened.

   **The page figure is settled at 486** and every instance on this page has been reset — meta
   description, hero subhead, proof strip, deliverables list, delivery section. It is a count, not a
   projection: `ebook/build/paginate.mjs` measures every block in headless Chrome and fills fixed 6x9
   pages, `ebook/build/frontmatter.mjs` prepends the cover, title page, copyright page and contents,
   and `ebook/build/fitcheck.mjs` passes on all 486.

   Two other claims on this page were corrected at the same time, because they described a product
   that did not exist yet rather than the one in the repo:

   - "The Binder — 80 pages" is now **61 pages**. 41 forms, all present, every explicit multiplier
     honoured; the 80 was a per-section estimate written before anything was laid out. The binder
     also ships as its own file now: `ebook/binder/out/The-Storm-Ready-Home-Binder.pdf` (61 pages,
     661 KB, rendered 2026-08-13) — so the "printable, fillable forms" offer bullet matches the
     delivery instead of pointing into the middle of the 486-page book.
   - "All 50 State Packets" is now **51 — 50 states and DC**, which is what actually ships.

   The "illustrated PDF" claim and the named floor-plan diagram for Protection 23 were **false when
   written** — there were no figures in the book at all. They are true now: 13 code-drawn diagrams,
   credited in Part Eight. The lesson worth keeping is that the copy was written from the plan and
   nobody had checked it against the artifact.

4. **The 51 state packets (50 states + DC) now exist as HTML** at `ebook/appendix/out/packets/
   <ABBR>.html`, and `build.py` can render any of them to PDF — only 4 (CA, FL, IL, TX) have been
   rendered so far as spot checks, not all 51. Filled from national directories rather than 51 hand lookups: the three
   hazards, their seasons and the region overlay (NCEI Storm Events deaths), the emergency
   management agency and its URL (usa.gov), the insurance regulator, its phone and its complaint
   page (NAIC), the energy-assistance page (ACF LIHEAP), and both private-well testing fields
   (two EPA sources). **Outstanding:** the deductible and roof-settlement notes, the emergency
   prescription-refill provision, the utility disconnection moratoria, `em_phone`, and the
   mitigation programme where a state runs one — all per-state legal and regulatory facts with no
   national machine-readable table, which is why they are last. `ebook/appendix/README.md` lists
   every source found and every dead end tried.

**Both now done.** The **dedicated headshot** exists at `landing/assets/headshot.png` (500×600,
5:6), cropped from the approved cover art by `ebook/build/art/make_derived_art.py`, so it stays in
sync if the cover ever changes (that script still reads the old-face `cover-v3-raymond.png`: point it at
the Paul v2 cover before re-running, or it puts the old face back); the author-block portrait points at it directly instead of faking
a crop of the full cover with `background-position`. The **16:9 cover render** exists at
`ebook/build/art/cover-16x9.png` (1920×1080), composed from the same plate with the headline and
proof line typeset into the left half so it stays legible at Gumroad's thumbnail size — it's the
storefront image on the Gumroad product (`/l/ebook`, published, $9.99).

**Byline changed to Paul Raymond on 2026-07-29** at the owner's request, replacing Paul Reynolds
across this page, the sample, the cover art and the art notes. The cover byline was baked into the
generated pixels, so `ebook/build/art/rename_byline.py` repaints that strip in place rather than
regenerating owner-approved art; `landing/assets/cover.png` is the repainted file.
**Collision warning on the record:** unlike Reynolds, Paul Raymond collides with a real FEMA
Executive Public Information Officer (Paul D. Raymond, Jr.) and with Paul Raymond Publications, the
British adult-magazine brand. Details in `ebook/build/art/COVER-PROMPTS.md`.

## No mail provider, deliberately

There was one: a Cloudflare Pages Function posting free-packet signups to Kit's v4 API, with a
same-IP throttle and a `[FALLBACK]` line on the in-memory path. It was deleted on 2026-08-15, and
the reason is worth keeping.

It needed a `KIT_API_KEY` that was never created, so on the live site every submit returned
`HTTP 500 {"error":"Sign-ups aren't working right now."}` while the button above it said "Send my
state packet". It also only ever recorded a subscriber — the automation that would actually email
the right packet lived in a Kit dashboard that did not exist either. Two unbuilt pieces standing
between a promise on the page and anything reaching a reader.

Gumroad already does email capture, delivery and unsubscribe, and it was already carrying the paid
product. So the packets became a $0 Gumroad product (`/l/packet`) and the function, the Kit
dependency, the state `<select>` and its 51-entry JS array all came out. Nothing on this site
posts anywhere now.

## Deploy

Cloudflare Pages, direct upload — no build:

```bash
npx wrangler pages deploy landing --project-name paulraymond --branch main
```

**`--branch main` is not optional.** Wrangler names the deployment target after your git branch, so
from a feature branch it publishes to a preview alias (`<branch>.paulraymond.pages.dev`) and
production keeps serving the previous build with no error anywhere. This was hit for real on
2026-08-15 while shipping a factual correction — the fix went live only on the alias.

No environment variables. No bindings. Nothing to configure — the project is static files.

Check after shipping: `node buycheck.mjs` (the buy button resolves to a live checkout),
`node gumroad/pagecheck.mjs https://paulraymond.gumroad.com/l/ebook product`, and the free-packet
button reaching `/l/packet`.

**Live since 2026-08-14 at https://paulraymond.pages.dev.**
