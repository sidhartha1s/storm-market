# Jacob Feldman (80, retired claims adjuster, Asheville NC) - landing page review, 2026-10-27

## 1. Path taken
Real Chromium via playwright-cli at 1366x768, then 1093x614 (125% approx). All URLs with ?src=test.
1. `/` hero (~20 s before I would have closed the tab; kept going as a tester). Read the whole page text, looked at the sample pages and the price comparison.
2. `/about/` (~1 min), `/states/` (skimmed), `/states/north-carolina/` (~2 min, every line).
3. `/field-notes/`, then `/field-notes/joplin-tornado-2011/` (~2 min), `/resources/` (free checklists).
4. Buy button -> `paulraymond.gumroad.com/l/ebook` loaded fine. Stopped at the product page, typed nothing. The browser session died once on the way to Gumroad; reopened, same result.
5. A guessed URL `/resources/Family-Emergency-Plan/` returned "Page not found" (my guess, not a link on the site).

## 2. Verdict: LEFT (would not buy on first visit)
Exact moment: first screen. A blue bar reads "21 viewing now - Launch price ends in 02:46:47", and a toast "Earl G. from Peoria, IL just got The Storm-Ready Home, 11m ago" slides over the hero. Countdown + live-viewer count + purchase toast = the pressure tactics Jacob hates. The viewer count changes per page (17, 19, 21, 22, 26) and the countdown reads about 2h46m on every page I loaded, so it looks fake. An ex-adjuster spots that in seconds and files the whole page under fraud indicators.
He might return for the content (the sample pages are genuinely good), but the trust damage lands before he sees them.

## 3. Bugs
- Fake-urgency widgets (jacob-01-hero-1366.png): countdown, "N viewing now", "just got" toast. The toast overlaps the hero button ("Get the book, $9.99" half hidden) at 1366.
- Sticky bottom dock ("The Storm-Ready Home - $9.99 / Get the book") covers the hero CTA and book cover at 1366, worse at zoom (jacob-02-hero-zoom125.png). It repeats on every page and covers reading text (jacob-03-mid-zoom125.png, jacob-04-north-carolina.png).
- Right-hand section rail (01 Start here ... 08) sits against the page edge and crowds the paper at 1093 (jacob-02). A small floating round dot at the left edge (jacob-03, jacob-04) has no clear purpose.
- No horizontal overflow at either size (scrollWidth = clientWidth, checked).
- NC page: tag says "HURRICANE COAST" but the hazard list has no hurricane. "Energy bill assistance (LIHEAP)" heading is duplicated and the entry shows no phone or link text.
- Gumroad price showed in rupees for this tester (geo-IP; Jacob would see USD). The box says "Name a fair price" with a "+", so pay-what-you-want wording may confuse a buyer who expects a fixed $9.99. Flagged only; checkout is fixed per brief.
- The only 404 was my guessed URL. Not every link was clicked.

## 4. Copy
Hype / pressure:
- "Launch price ends in 02:46:47" (countdown that does not move between visits).
- "21 viewing now" and "Earl G. from Peoria, IL just got..." (fake-looking social proof).
- "$87.99 of value, once" for $9.99: a stack of "$14.99 manual / $19 binder / $15 sequence / $20 lifetime updates". Never sold separately, so it reads as invented. A claims adjuster calls that an inflated valuation.
- "The storm doesn't warn twice." Alarmist, and the Joplin article itself says the sirens sounded twice.
Unbacked / suspicious:
- "Rated five stars by early readers." Where, by whom? Nine testimonials, all five stars, first name + state, no date, no way to verify.
- "Paul Raymond is the authorial name this work is published under" (About). A pseudonym, no bio, no credentials, no photo. Biggest trust gap for a skeptic.
- "Written by hands that have done every protection in it": no evidence.
- Inconsistent numbers: "61 fillable forms" (home) vs "41 forms, 61 pages" (checklists). Cover says "5 REGIONS".
- "Built from National Weather Service & FEMA post-storm reports": no list of which reports on the sales page.
Vague / wrong for Jacob:
- NC guide: hazards = flash flood (Sep), hail/derecho, tornado. No hurricane, no Helene, no mountain flooding or landslides, nothing about western NC. For a man who lost a car in Helene this reads as templated data.
- Joplin timeline does not reconcile: lede says warning with 24 min lead and sirens at 5:11; FAQ says warning at 5:17, sirens at 5:11 and 5:38, "24 minutes before impact". Sources are listed as plain text, no links.
- Field Notes has two articles; "Next dispatch... Episode 2" signals a thin archive.
- Sales table says "Loss you can't prove, no photos: Unrecoverable". Overstated; adjusters pay claims without photos.
What he would want instead: chapter list with page numbers, the exact report titles (NWS service assessment names, NIST NCSTAR numbers, FEMA publication IDs) as links, one full free chapter (claims/money), author identity and background, an up-front "not insurance advice", and an NC page covering Helene, the NFIP 30-day wait and mountain debris flow.

## 5. Trust
Raised trust:
- Real photographed sample pages with citations beside claims and a "WHAT THIS DOES NOT DO" box (jacob-03). Exactly the adjuster tone. Best asset on the site.
- Seven free printable checklists, plain refund terms, "not insurance advice" disclaimer, no claimed agency affiliation.
- NC page lists real agency phone numbers and links (NC DPS, NC DOI) with a "data verified 2026-08-02" stamp. Joplin dispatch has a source list and timestamped YouTube chapters.
- Clean Gumroad page with a visible 7-day refund.
Lowered trust:
- Countdown, viewer count and purchase toast.
- Pseudonymous, faceless author; AI-looking cover model (jacob-07-gumroad.png).
- Anonymous five-star testimonials; the "$87.99 value" stack.
- NC guide missing Helene/hurricane; Joplin timeline mismatch.
- Small text and a sticky dock that eats the screen at 1366 and 125%.

## 6. Top 5 changes (ranked)
1. Delete the countdown, "N viewing now" and "just got it" toast everywhere; drop the sticky dock on content pages. This alone changes leave into keep reading.
2. Show who Paul is: real name or an honest pen-name explanation, photo, credentials or a named expert reviewer, a contact email.
3. Make sources clickable: list the actual NWS/NIST/FEMA reports on the sales page, link them in field notes, add a downloadable table of contents and one full free chapter (claims/money).
4. Fix the NC guide: hurricane and Helene lessons, western NC flood/landslide, NFIP waiting period; fix the "Hurricane coast" mismatch and the duplicate LIHEAP entry; sweep the other states for the same gap.
5. Remove the "$87.99 value" stack and unattributed "five stars" (use real, dated, full-name reviews or none). Reconcile 61 vs 41 forms and the Joplin timeline.

Screenshots in this folder: jacob-01-hero-1366.png, jacob-02-hero-zoom125.png, jacob-03-mid-zoom125.png, jacob-04-north-carolina.png, jacob-05-fieldnote.png, jacob-06-about.png, jacob-07-gumroad.png.
Not checked: Gumroad payment form (stopped before it), the free packet PDF, 49 other state pages, mobile.
