# Jenny Alvarez (63, Tampa, iPhone 390x844) - landing page test, 2026-10-27

Screenshots (this folder): jenny-1-yt.png, jenny-2-home-top.png, jenny-s3600.png, jenny-s9000.png, jenny-s11500.png, jenny-3-about.png, jenny-4-checkout.png, jenny-5-checkout-scroll.png. Nothing typed, nothing submitted.

## 1. Path taken
1. /yt/?src=test (about 40 s). "The checklist Paul mentioned in the video." Cover, $9.99 with $87.99 struck through, refund line, orange button. Top bar shows "19  02:55:07" with no label. 486 pages / 130 protections stats. Clean, fast.
2. / home ?src=test (about 90 s of scrolling; page is 14,151 px, about 17 screens). Headline "The storm doesn't warn twice." Skimmed value stack, page photos, 9 testimonials, FAQ.
3. /about/ (20 s) looking for who Paul is. Found no photo or bio, only a method statement and "authorial name".
4. /resources/ (15 s). Seven free printable pages: good.
5. Back to /yt/, tapped "Get the book, $9.99" -> paulraymond.gumroad.com/l/ebook (loaded in about 3 s).

## 2. Verdict
Would NOT buy yet; left at checkout. Decision moments: (a) on the home page when the viewer count changed 19 -> 18 -> 30 and a toast said "Betty J. from Jackson, MS just got..." (fake, trust gone); (b) at Gumroad when the price showed as "950.67+" with a "Name a fair price" box, not $9.99. I would have bought for $9.99 if neither had happened. The free checklists nearly saved it.

## 3. Bugs
- Checkout price mismatch (jenny-4, -5): Gumroad displayed a rupee amount with "+" and a "Name a fair price" field. Caveat: my tester IP was detected as India (currency list says "Rupees - detected"), so Jenny in Tampa would likely see USD. But the "+" and the fair-price box exist for her too unless the product minimum is fixed. Needs a check from a US IP. The "+" means "or more": reads as pay-what-you-want, confusing.
- Top bar on phone (jenny-1, jenny-2): "19  02:55:07" with no labels. The CSS hides "viewing now" and "Launch price ends in" on mobile, so it is two unexplained numbers. Meaningless to her.
- Three layers stacked on phone: top bar, bottom "The Storm-Ready Home - $9.99 / Get the book" bar, plus the popup toast (jenny-s9000). Together they cover roughly 25 percent of the screen. The toast sits on a testimonial I was reading.
- Two different buttons for one action: "Get the book, $9.99", "Get my copy, $9.99", "Get the book", "Get my copy". Inconsistent.
- Tab strip at top (Start here / Why this book / Inside...) is cut off at the right edge and scrolls sideways; "Why" tab is partly clipped. Easy to miss it scrolls (jenny-2).
- The tiny monospace stats ("486 PAGES  130 PROTECTIONS", jenny-1) are small, about 13 px, grey. Hard for 63-year-old eyes.
- Page is 17 screens long. Too much scrolling on a phone.
- Home hero shows no price near its button; it appears only after scrolling.

## 4. Copy
Confusing / felt fake:
- "Launch price ends in 02:54:59": the timer is a per-visitor localStorage deadline (key srh-binder-deadline) and the page says nothing real is launching. Fake urgency.
- "30 viewing now": number changes randomly on each load (19, 18, 30, 24). Fake.
- "Betty J. from Jackson, MS just got The Storm-Ready Home, 30m ago": fake social proof.
- "$87.99 of value" / "$14.99, $19, $15, $19, $20": invented anchor prices for a PDF. Feels like a late-night infomercial. "Lifetime updates ($20)" has no basis.
- "Rated five stars by early readers": nine testimonials, all five stars, first names + state only, none verifiable.
- "authorial name" on /about/: "Paul Raymond is the authorial name this work is published under." So Paul is a pen name. I wondered who is real. The cover shows a model-like man; no real bio.
- "61 fillable forms" (home) vs "41 forms, 61 pages" (resources): inconsistent.
- "Yours in two minutes": fine, but I want to know it is a PDF I can read on an iPad and print.
Failed to answer:
- Can I read it on my iPhone/iPad? Do I need an app? (FAQ says "No app" only in Why section.)
- Is there a printed/spiral copy? A 486-page PDF is hard for someone like me to print.
- Can I buy a second copy for Mom? Can I gift it? Nothing said.
- Is this Hurricane/Florida specific? Margaret and Ray are Floridians (good), but no Florida hook above the fold.
- Who do I email for help? Footer says "reply to your purchase receipt", only.
Direct enough? Mostly yes in /yt/; the home page buries the answer under 17 screens. I would rather read: "486-page PDF. $9.99. Read on phone, print what you need. Refund in 7 days. Florida/Gulf hurricane chapters included. Written by [real name, photo, credentials]."

## 5. Trust
Raised trust: plain "what this does not do" honesty, cited FEMA/NWS sources, disclaimers saying no government affiliation, free printable pages, 7-day refund repeated, Gumroad (I know it), the cover and real page photos, a Florida testimonial, privacy and terms links.
Lowered trust: the three fake-looking mechanics above (my rule: leave), pen-name admission with no face or bio, the invented $87.99 anchor, identical five-star reviews, rupee/pay-what-you-want checkout.

## 6. Top 5 changes (ranked)
1. Delete the fake countdown, fake viewer count, and fake "just bought" toast. Biggest single trust killer for this buyer.
2. Verify Gumroad from a US IP shows plain "$9.99" and no "Name a fair price" box; fix the "+" if it is shown.
3. Put a real Paul (photo, real story, credentials or an honest "pen name because..." line) on /about and /yt.
4. Drop the $87.99 / lifetime-updates value stack; say "$9.99, one PDF, everything included."
5. Cut to one sticky button on phone; one button wording; add "Read on phone, print what you need" and "Buy a copy for family" lines near the price; label the tabs and make them wrap.
