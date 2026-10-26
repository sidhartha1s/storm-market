# Janet Whitfield (75, Tulsa) landing-page test, 2026-10-27

Setup: Chromium via playwright-cli, 820x1180, URLs tagged ?src=test. Tester IP is in India, so Gumroad showed rupees; Janet would see dollars (flagged below). Text-size bump not emulated. Screenshots: janet-01-top, -02-scroll1, -03-mid, -04-bottom, -05-about, -06-oklahoma, -07-gumroad, -08-checkout (.png, same folder).

## 1. Path taken
1. `/` (about 4 min reading, top to bottom, 13,360 px tall). Headline, cover, five reasons, sample pages, price table, 9 testimonials, FAQ.
2. `/about/` (1 min). `/resources/` (1 min). `/states/` then `/states/oklahoma/` (2 min).
3. Back to `/`, clicked "Get the book, $9.99" -> `paulraymond.gumroad.com/l/ebook` (the session then died; reopened the same Gumroad URL).
4. Clicked "I want this!" once. Did not type anything. Stopped at the product page; never reached a card form.

## 2. Verdict: would call her grandson first
Decision moment: About page. She reads "Paul Raymond is the authorial name this work is published under." So Paul is a pen name, with no photo, phone or real person. She had liked the Oklahoma page and its real state phone numbers. Then Gumroad, a brand she has never heard of, asked her to "Name a fair price" and threw an error on the first click. Not bought.

## 3. Bugs
- **Buy button errors.** On the Gumroad page, "I want this!" gave "You must input an amount" (janet-08-checkout.png). The price is a "Name a fair price" box that starts empty, and the button shows "950.67+" with a plus sign. A 75-year-old reads that as broken, or "the price is not $9.99". Caveat: tested from an Indian IP in rupees; a US visitor in dollars may be prefilled. Unverified, and worth a check from a US IP.
- **Two sticky bars overlap content** all the way down: the top blue bar and a bottom pill "The Storm-Ready Home . $9.99 / Get the book". The bottom pill covers text and the sample page (janet-02, -03). Her large text means even less visible space.
- **Moving things:** a live countdown clock (02:56:33, ticks every second), a "19 viewing" counter that changes, and slide-in popups "Earl G. from Peoria just got..." and "Carol S. from Wichita, KS just got..." (janet-04). All of these draw the eye away from reading.
- **Top nav tabs are clipped** ("F..." cut off at the right edge, "Get the Boo" on the Oklahoma page). She will not know it scrolls sideways (janet-01, -06).
- Small text: captions, "viewing", tab labels, the popup timestamps and the price-table amounts are small and in a monospace font. Body copy is a readable size but grey-on-cream, so contrast is modest.
- Buy links carry `utm_source=youtube`, though she came from email. Harmless to her, but it makes analytics wrong.
- Gumroad page has a currency list of 30 currencies, and an email "Subscribe" box above the product. Confusing for her.

## 4. Copy
- "A 486-page manual... This binder is what it looks like" (hero): manual or binder? Cover shows a book. She cannot tell what she is buying.
- "One PDF of 486 pages, delivered to your inbox" (FAQ): she does not know what a PDF is, and the FAQ is at the very bottom. Never says "not mailed to you, no paper".
- "No app, no DRM": DRM means nothing to her. "print any page" is buried in a list, and the sample is "Read it for a week on me", unclear.
- "$9.99 $87.99" with five "included" items: reads as a fake discount. She asks why a $14.99 manual plus a $19 binder, and so on, now costs $9.99.
- "7-day REFUND, NO QUESTIONS" vs "reply to the delivery email": she cannot call anyone. Where is the email address or phone number?
- "Rated five stars by early readers" with no source; nine testimonials all five stars, all first name plus state. One is "Janet . Kentucky", so her own name feels odd.
- "The storm doesn't warn twice" / countdown clock / "just got" popups feel pushy to a woman scared of sirens. The clock implies a deadline that does not exist.
- "Carol S. ... 4m ago" on the homepage, then "Carol S. ... 50m ago" on About: she notices it looks canned.
- "It works for renters and 68-year-olds": a clumsy age label; she is 75, and does not appreciate being named an age group.
- "after-action reports", "NIST", "service assessments", "mitigation credits", "hazard playbooks": jargon.
- Plain words that would help: "Your download is a computer file (PDF). Nothing comes in the mail. You can print it at home or the library. Call us at ___."

## 5. Trust
Raises trust: the free pages and Oklahoma state guide with real agency numbers, 405-521-2481; the 7-day money-back promise; the honest "what this does not do" claim; the "not a prepper book" FAQ; the legal footer saying no government endorsement; the Oklahoma testimonial ("Linda . Oklahoma").
Lowers trust: the pseudonym admission on About, with no photo or phone, and the same cover model also appearing on the cover and the kitchen photo (looks staged / AI); the live countdown, viewer counter and purchase popups (stock "social proof"); the $87.99 fake-value stack; "Rated five stars" with no source; checkout leaving the site for an unfamiliar company.
Gumroad: she has never heard of it, the page looks nothing like Paul's site (white, plain, pink buttons), and "Name a fair price" and a currency menu feel like a stranger's shop. No lock logo or "safe payment" wording near the button, no "Visa / PayPal accepted" line. She would want reassurance before it.

## 6. Top 5 changes (ranked)
1. Fix the Gumroad price: fixed $9.99 (no "Name a fair price", no "+"), button must work first click. Test from a US IP.
2. Add a real human: phone number or named email on the homepage, a real photo and plain bio of the author, and drop or explain the pen-name line. Say who answers.
3. Add a plain-language "What you get" box at the top: "A computer file (PDF), sent by email in 2 minutes. Nothing mailed. Print it at home. Works on iPad." Replace "binder" mixed with "book".
4. Remove the countdown, viewer counter, purchase popups and one of the two sticky bars. Cut "$87.99 value".
5. Before checkout, add a "Paying is safe" line: "Payment handled by Gumroad, a well-known secure service. Visa, Mastercard, PayPal accepted. 7-day refund: email ___." Also let the top nav wrap instead of clipping, and make text larger.

Not checked: payment form itself, the confirmation email, whether a US IP sees a prefilled price, other state pages, Field Notes, iPad Safari specifics.
