# Landing page — The Storm-Ready Home

Static page, zero build step: one HTML file with inline CSS, assets alongside it, no framework, no
CDN. The one piece of server logic is `functions/api/subscribe.js`, a single Cloudflare Pages
Function for the lead-magnet form — no bundler, no other backend. Deploys to Cloudflare Pages as-is.

**NOT DEPLOYED. Not live anywhere.** See "Before it goes live" — four blockers, one of them is
Gumroad.

| File | What |
|---|---|
| `index.html` | The whole page. Inline CSS, no framework. One CDN dependency: Google Fonts (Fraunces / Source Serif 4 / IBM Plex Mono), added in the 2026-08-13 redesign. |
| `privacy.html`, `terms.html` | Generic text-only legal pages, linked in the footer, noindexed. |
| `og-src.html` | Source for `assets/og.png` (1200×630 social card). Regenerate: `node shot.mjs og-src.html ./out 1200`, crop to 630. |
| `assets/` | Cover + headshot (compressed JPEGs; the PNG originals remain as source), OG card, four real page shots, five Paul photos (selfie, plywood, binder, field kit, stage). |
| `functions/api/subscribe.js` | Pages Function behind the lead-magnet form. See "Mail provider". |
| `widthcheck.mjs` | **Gate.** Fails if the page scrolls sideways at any width. |
| `shot.mjs` | Full-page screenshots at true device widths. |

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
   the headline and the buy button below the fold at 1280×900. Capped to 340px wide.

## Page structure, and why it is in this order

Modelled on the two reference funnels in `../ebook/build/art/ref-yoder-cover.png` and the teardown
in the design spec. The money section sits **immediately below the first CTA and the manual
description**, which is the owner's rule: the higher the credible savings delta right below the
pricing, the higher the conversion.

1. Hero — headline, sub, price CTA, cover
2. Proof strip — 486 pages, 130 protections, 23 hazards, 60 days, 7-day refund
3. What it is — counts grid, then all 23 hazards as chips so the scope is undeniable
4. **The money chapter** — the $3,029 / $43,600 gap, sourced, with the "what this is not" box
5. Find your region — 5 cards, makes it personal before the ask
6. Look inside — four real rendered pages, not a mockup
7. Paul Raymond — persona block with the quote
8. The offer — $47 struck from $87, everything included
9. Free state packet — the email gate
10. FAQ — including "isn't this free from FEMA?", answered honestly
11. Last call

## Deliberate omissions

**No testimonials or reviews.** Both reference funnels use them heavily and they convert — but there
are no buyers yet, and **fabricating reviews is not something I will write.** The section is simply
absent rather than filled with invented names. Add it after real buyers exist; the design has room
for it between the offer and the FAQ.

**No per-line dollar values in the value stack.** Yoder itemises five deliverables at $47/$19/$19/$14/$21
to a "$120 total value" and collapses it to $47. That is price anchoring, and it is standard — but
those numbers are claims the seller owns, and nothing here has ever sold separately at those prices.
The stack lists what is included and shows $87 → $47 instead. If you want the itemised version, set
the numbers yourself.

**No countdown timer or "203 people viewing".** The lawn page uses both. They are fabricated urgency;
your call, not mine to add silently. A real launch-price end date is honest and easy to add.

## Before it goes live — four blockers

1. **Gumroad product does not exist.** The buy button at `#buy` has no URL. Create the product, then
   set `href` to the Gumroad URL and add their overlay script. Gumroad cannot show a struck-through
   price natively — put the $87 anchor in the product description and use a discount code for $47.
2. **The lead-magnet form is now wired, but delivery is not finished.** `functions/api/subscribe.js`
   is a Cloudflare Pages Function that validates the email + two-letter state code and forwards the
   subscriber to Kit (see "Mail provider" below) — no more alert-only placeholder. What it does
   **not** do: send the packet itself. It adds the subscriber with their state recorded as a custom
   field; a Kit automation keyed on that field (built in the Kit dashboard, not in this repo) has to
   actually email the right `<ABBR>.html`/PDF. That automation does not exist yet, and neither does
   the Kit account — `KIT_API_KEY` must be set before this stops 500ing (see Deploy). The state
   packets themselves are covered in blocker 4.
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
     honoured; the 80 was a per-section estimate written before anything was laid out.
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
sync if the cover ever changes; the author-block portrait points at it directly instead of faking
a crop of the full cover with `background-position`. The **16:9 cover render** exists at
`ebook/build/art/cover-16x9.png` (1920×1080), composed from the same plate with the headline and
proof line typeset into the left half so it stays legible at Gumroad's thumbnail size — it's the
storefront image, waiting on the Gumroad product being created (blocker 1).

**Byline changed to Paul Raymond on 2026-07-29** at the owner's request, replacing Paul Reynolds
across this page, the sample, the cover art and the art notes. The cover byline was baked into the
generated pixels, so `ebook/build/art/rename_byline.py` repaints that strip in place rather than
regenerating owner-approved art; `landing/assets/cover.png` is the repainted file.
**Collision warning on the record:** unlike Reynolds, Paul Raymond collides with a real FEMA
Executive Public Information Officer (Paul D. Raymond, Jr.) and with Paul Raymond Publications, the
British adult-magazine brand. Details in `ebook/build/art/COVER-PROMPTS.md`.

## Mail provider

`functions/api/subscribe.js` forwards the free-packet signup to **Kit** (`api.kit.com`, formerly
ConvertKit), chosen over Mailchimp and Buttondown for one reason: free-tier headroom for a list
that doesn't exist yet. Mailchimp's free tier was cut to 250 contacts / 500 sends a month in
January 2026; Buttondown's free tier caps at 100 subscribers. Kit's free tier holds 10,000
subscribers with full API access, and its v4 REST API is one POST with one header that upserts a
subscriber and accepts arbitrary custom fields — no provider-side abstraction layer needed for a
single provider.

What the function does: `POST https://api.kit.com/v4/subscribers` with an `X-Kit-Api-Key` header,
body `{ email_address, fields: { state } }`. That's it — it records the subscriber and their
two-letter state. It does not tag, does not trigger a send, and does not know what a packet is.

What it deliberately does **not** do, and who has to do it before this delivers anything real:

1. **Create the Kit account and API key.** Account settings → Developer → API keys → generate a
   v4 key (not the legacy v3 key). Set it as `KIT_API_KEY` in the Cloudflare Pages project (see
   Deploy below). Nothing is stored in this repo.
2. **Add a custom field with the key `state`** in Kit (Subscribers → Custom fields) before the
   first real signup. Kit silently drops unknown field keys with a warning rather than erroring —
   that's Kit's behavior, documented here so a missing field doesn't get mistaken for a bug in this
   function later.
3. **Build the actual delivery automation** in the Kit dashboard: a visual automation triggered on
   subscribe, split on the `state` field, that emails the matching `ebook/appendix/out/packets/
   <ABBR>.html` (or its PDF once rendered). Fifty-one branches, or one templated send pointing at a
   hosted per-state URL — that design choice belongs to the owner, not hardcoded here.

**Rate limiting:** same-IP throttle, 5 requests / 10 minutes, real and tested (see Deploy). It's a
fixed-window counter kept in the Function's module scope, so it's enforced per isolate, not
globally across Cloudflare's edge — a real throttle against one abusive client hitting one edge
location, not a distributed guarantee. The code checks for an optional `SUBSCRIBE_RATE_LIMIT`
binding (Cloudflare's declarative Rate Limiting binding, GA since 2025-09) and uses it instead if
present; the in-memory path logs a `[FALLBACK]` line on every request so the gap stays visible. No
binding is configured today — nothing to set up for this to work, it's just the softer of the two
options.

## Deploy (when unblocked, and with the owner)

**Confirmed ready, without deploying anything:**
- `wrangler` 4.118.0 is installed and already authenticated in this environment (`npx wrangler
  whoami` resolves to an existing Cloudflare account) — no credentials were created, requested, or
  stored as part of this check.
- `functions/api/subscribe.js` was validated locally with `npx wrangler pages dev .`: malformed
  email → 400, malformed state → 400, GET → 405, `KIT_API_KEY` unset → loud 500 (never a fake
  success), 6th request within 10 minutes from the same IP → 429, and — with a temporary local-only
  fake key in `.dev.vars` (never committed; deleted immediately after the test) — a real network
  round-trip to Kit's live API that correctly surfaced Kit's 401 as this function's 502. The dev
  server was killed after testing; nothing was published.

Cloudflare Pages, direct upload — no build:

```bash
npx wrangler pages project create storm-ready-home        # once
npx wrangler pages deploy landing --project-name storm-ready-home
```

**Environment variables that must be set before the first deploy** (Pages project → Settings →
Environment variables, both Production and Preview):

| Variable | Required | Notes |
|---|---|---|
| `KIT_API_KEY` | Yes | Kit v4 API key (see "Mail provider" above). Unset → every submission 500s loudly instead of silently succeeding. |

`SUBSCRIBE_RATE_LIMIT` is an optional future binding, not a variable to set — see "Rate limiting"
above.

Then point the domain at it in the Cloudflare dashboard. Check before shipping: OG image resolves at
an absolute URL, the buy button goes to a live Gumroad product, a real test purchase completes and
delivers, the refund path works, and a real Kit sign-up lands in the account with `state` populated.

**Standing instruction: do not run either command above until Gumroad payments exist (blocker 1).
This site is deploy-ready. It is not launch-ready.**
