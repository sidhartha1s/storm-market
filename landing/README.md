# Landing page — The Storm-Ready Home

Static, zero dependencies, zero build step. One HTML file with inline CSS, assets alongside it.
Deploys to Cloudflare Pages as-is.

**NOT DEPLOYED. Not live anywhere.** See "Before it goes live" — three blockers, one of them is
Gumroad.

| File | What |
|---|---|
| `index.html` | The whole page. Inline CSS, no framework, no CDN, no external fonts. |
| `assets/` | Cover, OG image, four real page shots from the book. |
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
2. Proof strip — 488 pages, 130 protections, 23 hazards, 60 days, 7-day refund
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

## Before it goes live — three blockers

1. **Gumroad product does not exist.** The buy button at `#buy` has no URL. Create the product, then
   set `href` to the Gumroad URL and add their overlay script. Gumroad cannot show a struck-through
   price natively — put the $87 anchor in the product description and use a discount code for $47.
2. **The lead-magnet form is not wired.** It posts to `/api/subscribe`, which does not exist. The
   submit handler currently **fails loudly with an alert** rather than pretending to subscribe
   anyone. Needs either a Cloudflare Pages Function forwarding to a mail provider, or a hosted form
   endpoint. The 50 state packets must also exist before this can deliver anything.
3. **The book's prose is complete; its citations are not.** All **130 of 130** protections and all
   **23 of 23** hazard playbooks are drafted, plus front matter, people/places, the binder spec and the
   60-day sequence — 117,554 words. **All 130 citation markers are now closed**: every one carries a
   full citation and a retrieval date, and the handful of claims that could not be traced to a primary
   document were cut rather than softened. Sourcing is no longer the gating item; layout is.

   On the **488** figure: it is now a **floor and needs resetting.** Prose excluding the Binder measures
   114,637 words, and the rendered sample pages average **243 words per page** (measured, 11 body pages,
   including ones carrying diagrams and tables). That gives 472 prose pages, plus 80 binder pages and 18
   appendix pages — **about 570.** Closing the citations added ~23,600 words. The page currently
   understates the product, which is the safe direction, but it is still inaccurate. **Recount against
   the laid-out book and change every instance of 488 on the landing page before launch** — it appears
   in the meta description, the hero subhead, the proof strip, the deliverables list and the delivery
   section.

4. **The 50 state packets do not exist yet**, so the free-packet email gate has nothing to deliver
   — but the dataset behind them is now half collected and `build.py --check` passes on all 51 rows
   for the first time. Filled from national directories rather than 51 hand lookups: the three
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

## Deploy (when unblocked, and with the owner)

Cloudflare Pages, direct upload — no build:

```bash
npx wrangler pages project create storm-ready-home        # once
npx wrangler pages deploy landing --project-name storm-ready-home
```

Then point the domain at it in the Cloudflare dashboard. Check before shipping: OG image resolves at
an absolute URL, the buy button goes to a live Gumroad product, a real test purchase completes and
delivers, and the refund path works.
