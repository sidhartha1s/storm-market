# Money Chapter — Research Pack

Date: 2026-07-26 · Status: **partial. Not publishable yet.** See the verification queue.
Design contract: `docs/superpowers/specs/2026-07-25-ebook-funnel-design.md`

**Rule from the spec, restated: no figure ships unsourced. A delta that cannot be sourced is cut,
not estimated.** This file exists so that rule is auditable.

## Source tiers

| Tier | Meaning | Publishable? |
|---|---|---|
| **A** | Government primary, statute, or the issuing body's own document | Yes |
| **B** | Industry research house, insurance trade press, dated retail listing | Yes, attributed and dated |
| **C** | Contractor, agency, or roofer marketing page quoting a number with no filing behind it | **No.** Lead-generation copy, not data |

Most premium-discount percentages on the open web are Tier C. That is the central problem with the
recurring-annual number, and it is called out below rather than papered over.

---

## Delta A — Kit markup (one-time)

The direct analog of the lawn page's service math: *you are not paying for supplies, you are paying
for someone else to know what goes in the bucket.*

| Figure | Value | Tier | Source |
|---|---|---|---|
| Ready America 4-Person 3-Day Deluxe kit | $154.99 | B | Home Depot listing, captured 2026-07-26 |
| Pre-made kit range, general | $150–400 (basic $50–200; premium $500+) | C | prepper review blogs — **replace with 5 dated retailer captures** |
| DIY equivalent | $100–300 claimed | C | same problem |

**Verdict: the delta is real but the numbers are not mine yet.** The honest version is built, not
cited: assemble the actual 4-person 72-hour list from the book, price every line at Walmart, Target
and a grocery chain on one dated day, and publish that table against three dated retail kit
listings. That makes it Tier B and unfalsifiable.

**A genuinely strong finding, already usable:** pre-made kits almost never include medication,
documents, cash, pet records, infant supplies, or personal hygiene. So the buyer of a $155 kit still
does not have a kit. That is a better argument than the price gap and it costs nothing to prove —
just enumerate what's in the box against what the book's list requires.

---

## Delta B — Recurring annual (insurance and mitigation credits)

This is the Yoder-equivalent number and the intended hero. **It is currently the weakest-sourced
part of the entire book.**

| Figure | Value | Tier | Source |
|---|---|---|---|
| Florida mandates wind-mitigation discounts | Fla. Stat. **§627.0629** | **A** | statute |
| Alabama minimum discount, coastal FORTIFIED roof | ~25–30% | C→ needs A | trade press summarizing filings |
| FORTIFIED roof discount, wind portion | 20–55% | C | roofer marketing pages |
| FORTIFIED, hurricane portion | 35–60%; other wind 20–35% | C | same |
| Louisiana retrofit tax deduction | up to $5,000 or 50% of cost, lesser | C→ verify statute | trade press |
| FL wind-mitigation inspection premium cut | 25–45% of the **wind portion**, which is itself 30–60% of the bill | C | agency marketing |
| Opening protection credit | 30–45% of wind premium, all openings required | C | window contractor |

**Honest read:** that a discount is legally mandated is Tier A and safe to state. Every *percentage*
above is Tier C — written by people selling roofs and windows. The primary sources exist and are
public but tedious: **state Department of Insurance rate filings and the mitigation credit tables
insurers must file.** Until those are pulled, the book can say a mandated discount exists and tell
the reader exactly how to obtain their own carrier's credit table — which is arguably more useful
than a national average anyway, since the credit is carrier- and county-specific.

**Recommendation: do not put a national percentage in the hero headline.** Frame the recurring
number as *"most readers have never asked for the credit their state requires their insurer to
offer"* and let the reader compute their own figure with a worksheet. That is honest, it is
Tier A-backed, and it converts the weakness into a personalization asset.

---

## Delta C — Claim and aid gap (event-conditional, the big number)

Strongest-sourced of the three.

| Figure | Value | Tier | Source |
|---|---|---|---|
| Average IHP award, post-DRRA | **$3,029** | **A** | CRS, congress.gov (R48310 / IF13127) |
| Average IHP award, pre-DRRA | $3,859 | **A** | CRS |
| Avg award 2016–18, homeowners / renters | ~$4,200 / ~$1,700 | **A** | CRS |
| IHP statutory maximum | **$43,600** housing + $43,600 other needs | **A** | Federal Register, 2024-10-24 notice |
| Share receiving the maximum | 10.8% of housing-assistance recipients | **A** | CRS |
| Majority of recipients earn | ≤ $30,000/yr (53.6%) | **A** | CRS |
| Average NFIP flood claim | ~$68,000–69,000 | B | insurance trade press — **promote via FEMA primary** |
| NFIP paid, 2024 | $8B; >$10B expected incl. Helene/Milton | B | Insurance Journal |
| Helene | >57,400 claims, >$4.5B paid as of 2025-02-06 | B | Insurance Journal |
| Sewer backup claim, typical | $10,000–20,000 (some $5–10K; severe to $50K) | C | restoration-company blogs |
| Backwater valve, retrofit | $2,000–5,000 retrofit; ~$500 at new construction | C | plumber price guides |
| Hail: average claim | "upwards of $10,000 in some regions" | C | vague — unusable |
| Hail: 2"+ hail hit | >600,000 single-family homes, 2025 | B | LexisNexis Home Trends |
| Hail loss cost | −38.4% in 2025 vs 2023 peak; severity flat vs 2024 | B | LexisNexis Home Trends |
| Home fires, direct property damage | ~$11B/yr (2022) | B | NFPA via III |
| Average loss per home structure fire | **not obtained** | — | NFPA PDF indexed as binary; no text extraction |

**The single best pairing available right now, both Tier A:**
average FEMA IHP award **$3,029** against a statutory maximum of **$43,600**. That gap is the entire
argument for documentation discipline, and it is government-sourced on both sides. It needs no
embellishment.

---

## Verification queue — what must be fetched before any figure is written

| # | Target | Promotes |
|---|---|---|
| 1 | FEMA NFIP primary claims statistics (Watermark financial statements / NFIP claims data) | avg flood claim B→A |
| 2 | State DOI rate filings + carrier mitigation credit tables, 3 states (FL, AL, LA) | every discount % C→A |
| 3 | Alabama DOI bulletin establishing the FORTIFIED minimum discount | 25–30% C→A |
| 4 | Louisiana statute for the retrofit tax deduction | $5,000 C→A |
| 5 | NFPA "Fire Loss in the United States" — text version or III fact page | avg loss per fire, currently missing |
| 6 | III Facts + Statistics: Fire | fire figures B, free |
| 7 | Own dated retail basket: 4-person 72-hour list priced at 3 retailers + 3 kit listings | Delta A → B, self-built |
| 8 | Municipal sewer-backup claim data or an insurer's published range | sewer C→B |

---

## What the hero headline can honestly claim today

**Can say now:**
- The average FEMA award is $3,029 against a $43,600 maximum — documentation is what moves you up
  that scale. *(Tier A both sides.)*
- Your state may legally require your insurer to discount a mitigated home — most readers have never
  asked. *(Tier A: Fla. Stat. §627.0629 and equivalents.)*
- A $155 pre-made kit does not contain your medication, documents, cash, or pet records. *(Provable
  by enumeration.)*

**Cannot say yet:** any national percentage discount, any "save $X per year" figure, any average
hail or sewer or fire loss number.

**Consequence for the sales page, stated plainly:** a Yoder-style *"save $4,000–6,000 a year"*
headline is **not currently supportable** for this book, because household disaster spend is not a
recurring utility bill and the recurring credits are carrier-specific. The defensible equivalent is
the gap headline — *the difference between the average payout and the maximum is roughly $40,000, and
documentation is what decides where you land* — plus a worksheet that computes the reader's own
number. Owner decision required if a single national dollar figure is wanted instead; that would
require the queue above to be completed first, and it may still not yield one honest number.
