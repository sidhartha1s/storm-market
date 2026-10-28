# Senior survival + landing review, 27 Oct 2026

Owner ask: senior readers read the book and try to survive a disaster; an investigator says whether they lived and
what was missing; fold that into the book with more diagrams and pictures. Then three senior buyers (63, 75, 80)
walk the landing page; fix what stopped them.

## The book test

| Reader | Disaster modeled on | Outcome | What decided it |
|---|---|---|---|
| Dorothy, 78, Fort Myers Beach, insulin, walker, no car | Hurricane Ian 2022 | survived, injured | her only driver wanted to "wait for the order"; registry form never confirmed |
| Harold, 74 (COPD, home oxygen) and Marge, 72 (dementia), Paradise | Camp Fire 2018 | near-death (Harold) | no alert reached a flip phone at night; Marge refused the car; 2 h in smoke on oxygen |
| Earl, 82, alone, Austin, CPAP, warfarin | Winter Storm Uri 2021 | near-death | fell fixing an old generator at night on a blood thinner; nobody nearby checked |
| Bev, 67, Moore single-wide, husband with cane, grandkids | Moore EF5 2013 | survived, injured, by luck | one shelter, locked; no backup |

Files: `book/<name>-prep.md` (what each reader did), `book/INVESTIGATION.md` (timelines, missing items, ranked fixes),
`book/xref-audit.md` (wrong protection numbers).

What went into the book (commit "Book: what four senior readers needed..."):
- "Start here if you are over 65" page and a $50 / $150 / $500 buying ladder (P0).
- Older-reader paragraphs: flip phone / landline / hearing-aid alerts (85, 87, 47), no-car drivers and the county
  registry questions (111), oxygen, CPAP, insulin and blood thinners (59-61), a 64 F "leave" number and the
  generator-at-night rule (P3-11, 40), mobile-home three-shelter plan (P4-C2), dementia car tips (P4-C1),
  CAL FIRE trapped-in-car steps (P3-05). 18 new sources, 0 open citations, still 130 protections.
- 11 new diagrams and 4 ChatGPT illustrations (Figures 14-28), disclosed on the Credits page.
- 11 wrong cross-references fixed; British spelling to US throughout.
- Book is 517 pages (was 486). `fitcheck` PASS on all 517.

## The landing test

| Buyer | Device | Verdict | Moment |
|---|---|---|---|
| Jenny, 63 | iPhone | would not buy yet | fake-looking countdown, viewer count and "just got it" toast; "$9.99+" at checkout |
| Janet, 75 | iPad, large text | would call her grandson first | pen-name About page; unknown Gumroad; "Name a fair price" error |
| Jacob, 80 | 1366 desktop, 125% zoom | left | first screen: countdown, viewer count, toast over the buy button |

Fixed (commit "Landing: answer what seniors could not find..."): plain "PDF by email, nothing is mailed, print what
you need" under the hero button and in the FAQ; new FAQs "Is it safe to pay?" and "Can I buy it for my mother or
father?"; bottom pill no longer covers the hero button; 41 forms on 61 pages made consistent; state pages' LIHEAP
link text; every page count now 517.

Kept by owner decision (ops/decisions.md, 27 Oct 26): countdown, viewer count, purchase toast, $87.99 value stack,
five-star line and testimonials, Gumroad pay-what-you-want "$9.99+".

Shipped 27-28 Oct: site deployed to Cloudflare; Gumroad ebook carries the 517-page book and rebuilt Binder, and its
description and page say 517; the free packet product's page and all 51 state packets say 517 (the rehook page had 486).

Not done: the About page pen-name framing (owner-approved 26 Aug), the North Carolina page has no hurricane/Helene
(state data is derived from NOAA Storm Events; needs a sourced data pass).
