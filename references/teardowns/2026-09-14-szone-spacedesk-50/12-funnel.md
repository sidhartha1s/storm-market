FUNNEL AUDIT — The Storm-Ready Home / Gumroad page

**Sources read:** landing-live.txt (rendered page), landing.html (source, incl. dev comments), cta-transcript.txt, sample.pdf pages 1–8, TX.pdf (4 pages).

Note: per standing project instruction, urgency widgets ("96 viewing now", countdown) are out of scope for this review — excluded below, not silently overlooked.

**1. Message match: 1/5 for hazard-specific traffic**
The entire page is a tornado/hurricane artifact. Hero image: Paul in front of a tornado. Opening story: Joplin tornado, 2011. First testimonials: tornado, then hurricane. Garage-door bracing and window protection dominate the "work" and "worth" sections. Nothing on the page names El Nino, winter, flooding-from-El Nino, or volcanic ash/Krakatau. A viewer arriving from an El Nino winter video lands on a tornado survivor story — zero continuity between what they just watched and what they're being sold. Matched offer per video type:
- El Nino/winter video → lead with the extreme-cold/blizzard chapter + free state packet (packets carry the state's actual winter hazard, e.g. TX packet lists "Extreme cold · Feb" as hazard #3).
- Krakatau/volcanic-ash video → lead with the "volcanic ashfall" or "systems dark" chapter, not a tornado story; that content exists in the book (chapter list confirms it) but is invisible anywhere on the page.
No hazard-matched variant exists; one static page serves all traffic.

**2. First screen, 65-year-old reading it cold**
Present: real name (Paul Raymond), a face (author photo + field photos), 7-day refund stated plainly, page count (486) up front, "who made it" answered at a headline level. Missing: any credential — no meteorologist, firefighter, engineer, or agency affiliation for Paul Raymond beyond "got tired of watching mistakes" and staged field photos; nothing verifies expertise. Also a direct self-contradiction baked into the HTML (line 356-358 comment): the curated 5-star testimonials sit right above where Gumroad's live rating field would render "no reviews yet" — the platform's own trust signal would visibly dispute the testimonials the moment it's turned on.

**3. CTA clip (verbatim, 15s, 30–40% mark):**
"Most people who watch these stories are already the careful one in the house, so I wrote down what the careful ones did before it mattered. Scan the QR code, or find the first link in the description. I would genuinely appreciate you taking a look."
Problems: never names the hazard just covered (generic "these stories"), never mentions the free state packet as an option, asks for "a look" not an action, no price/offer stated, single placement only (nothing at the end). Fix: name the specific hazard, lead with "your state's packet is free, first link" before the $14.99 ask, and repeat a shorter CTA at the video's close — the 30-40% mark is before most viewers have banked enough value to act, so a zero-cost first step converts better than a direct-to-$14.99 ask.

**4. Price and offer stack**
$14.99 vs $87.99 anchor: the $87.99 is built from four sub-items (binder $19, sequence $15, packets $19, updates $20) that are not sold separately anywhere — a skeptical buyer can't verify any of those prices, which weakens rather than strengthens the anchor. 7-day refund is stated twice, clearly, "reply to the delivery email" — workable but non-native to Gumroad's own refund flow, adds a manual step. Recommend dropping the itemized fake sub-prices in favor of a single comparison already used elsewhere on the page (the $2,670+ "cost of one bad afternoon" ledger is the stronger, verifiable anchor).

**5. Sample PDF (8 pages read: cover, legal front matter, TOC, "find your region," Protection 23, Protection 74, Tornado chapter opener, Tornado decision tree)**
Delivers a real "this is rigorous" moment by page 5 (Protection 23: cost/time/materials/regions fields, a diagram, a "what this does not do" box) — that's a genuine buy-signal for a tornado/hurricane reader. But every page sampled is tornado- or wind-hazard content; nothing from the Ice & Snow North, extreme cold, or volcanic ash chapters is in the sample, so a winter or Krakatau viewer gets no proof-of-relevance in the free sample either — same mismatch as the landing page, compounding it.

**6. Ranked fix list (highest expected effect first) + metrics**
1. Free-packet-first CTA rewrite (script #3 above) — biggest single lever; converts a hazard viewer to a zero-cost claim instead of asking for $14.99 cold.
2. Hazard-matched landing variant (or at minimum a swappable hero story per traffic source) — fixes the 1/5 message-match score directly.
3. Add Paul Raymond credentials/bio — closes the single biggest missing trust signal for a 65-year-old buyer.
4. Fix the testimonials-vs-live-rating contradiction before any rating widget goes live.
5. Replace the invented $19/$15/$19/$20 sub-stack with the verified $2,670+ cost comparison already on the page.
6. Confirm the free state-packet claim flow actually functions end-to-end — 0 claims against ~54 page views means either no one is offered it or the mechanism is broken; this is currently unverified, not just underused.
7. Add at least one non-tornado/hurricane sample page (extreme cold or volcanic ash) to the PDF sample.
8. Restate a short CTA at video's end, not only at 30-40%.
9. Instrument per-video UTM tracking in Cloudflare/Gumroad so the El Nino vs Krakatau mismatch can be measured, not assumed.
10. Re-test CTA placement earlier than 30-40% given the channel's low AVD (29% on the best video) — most viewers won't reach the current CTA at all.

**3 metrics to watch:** (a) Gumroad page-views → checkout-started rate (currently 54 views, 0 sales — need this split to know if the drop is pre- or post-click); (b) free state-packet claim count (currently 0 — first sign the offer/flow is even reachable); (c) Cloudflare referrer/UTM breakdown by source video, to attribute the ~54 views to El Nino vs Krakatau and quantify the message-mismatch cost per video type.