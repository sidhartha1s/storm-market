# Design: Storm-Market Flagship Ebook + Gumroad Funnel

Date: 2026-07-25 · Status: awaiting owner review · Owner decisions locked in-session

## Context

The storm-market channel (US weather/disaster documentary retrospectives) shipped episode 1
(Joplin 2011) on 2026-07-22. The channel monetizes on YouTube RPM alone today (~$5.60–6.70 RPM
in the validated competitor set). The bottleneck: paid image API spend is currently unavailable,
so the owner is going offline for 1–2 weeks to build 15–20 episodes plus a **product funnel** that
converts channel traffic into direct revenue at a much higher per-viewer rate than ad RPM.

This spec defines that product: **one flagship ebook**, sold at $47 through Gumroad behind a
static landing page, packaged on the proven pattern of two reference funnels the owner supplied
(`eliasyoder.com`, `fixyourlawnin30days.com` — same operator, both AI-persona-fronted; Yoder
reportedly $150K+ in ebook sales in June 2026 alone).

Goal: a single high-value SKU that a viewer who just watched a 15-minute disaster documentary
buys without leaving the moment, and does not refund.

## Market findings (researched 2026-07-25)

- **The category is generic bushcraft, not weather.** Amazon's Survival & Emergency Preparedness
  bestsellers are SAS Survival Handbook, McRaven, *Meals in a Jar*. The prepper "Bibles"
  (Connelly, Marsh, Cobb) all run the same spine: mindset → water → food → body temperature →
  fire → first aid → sanitation → security → off-grid power. **Nobody owns "US weather/natural
  disaster, family, event-forensic."** That is our gap and only a disaster-documentary channel
  can credibly fill it.
- **Our real free competitor is FEMA `Are You Ready?` (IS-22, ~200pp, public domain).** The book
  cannot be a FEMA rewrite. It must beat FEMA on readable prose, real-event forensics, and
  fillable tools — the three things FEMA is bad at.
- **The adjacent digital money is in binders.** "Family Emergency Binder" fillable PDFs (60–107pp)
  sell steadily at $8–35. Prose is the reason to buy; printables are the reason not to refund.
- **Pricing:** the $30–49 band converts ~28% better than sub-$10 on Gumroad; tracked Gumroad
  ebook average is $50.91 across 1049 books. $47 is correctly placed.

### Reference-funnel teardown (the packaging pattern to follow)

| Element | eliasyoder.com | fixyourlawnin30days.com |
|---|---|---|
| Countable unit | 93 numbered methods, 13 sections | 30-day sequence |
| Bulk claim | "700+ page illustrated ebook, Second Edition" | PDF, page count not led with |
| Price | **$47**, slashed from $77, "Launch price — ends Sunday" | $32, countdown timer, "203 homeowners reading right now" |
| Value stack | 5 items priced individually → **$120 total value → pay $47** | single price, deliverables listed in FAQ |
| Money section | "The Math": typical household $6,160/yr → after Manual ~$2,025/yr → **net $4,000–6,000**, sourced to EIA + BLS | "The Money Chapter": 3-column service-vs-DIY table, $1,200 contract → $140–290 DIY, + "Example math for comparison only" disclaimer |
| Proof | 280K subs, 4.9★, 3 first-month buyer stories tied to specific chapters | reviews that name **the money chapter specifically** |
| Guarantee | 7-day, "no questions asked", refund same day | 7-day, case-by-case after |
| Regionalization | **none** — one FAQ line about climate | **two tracks** (warm/cool-season grass) + state-by-state extension directory |
| Trust | named persona + headshot + origin story | named persona + headshot + origin story |

**Corrected finding (owner challenged, reverified):** Yoder has **no 50-state section at all**.
The state-by-state element exists only on the lawn page and it is a **resource directory**
(land-grant extension offices, soil labs), listed as one bullet among the deliverables — not
content, not images. The "50 illustrated state pages" idea was ours, not theirs. Dropped.

## Owner decisions (locked this session)

1. **Spine:** numbered protections + 60-day sequence.
2. **Regionalization:** hazard-region overlay + state directory — implemented per the pivot below.
3. **Home-defense / firearms chapter: CUT.** Payment-processor risk; Gumroad prohibits what Stripe
   and PayPal flag, and they already forced the NSFW purge. Replaced by civil-unrest evacuation +
   home hardening, which is the useful 80% with none of the account risk.
4. **Money math:** stacked — recurring annual + one-event loss avoidance.
5. **Prep calendar: 60 days max**, not 12 months.
6. **Persona:** "Weather Joe" — landing page only, never in videos. A few generated headshots plus
   one personal-comment section, matching how both reference pages do trust.
7. **Price:** $47, shown slashed from $87 on the landing page.
8. **Image budget: BLOCKED — pending DeAPI keys.** See Visual System.
9. **The book's subject is large-scale natural disaster — "nature's wrath" — not household accidents.**
   Owner correction 2026-07-26: home fire, CO, frozen pipes, and sewer backup are **sub-points
   inside the aftermath section of the disaster that causes them** (fire after the quake, sewer
   backup after the rain event, CO after the outage, pipes after the freeze), never peer chapters.
   An earlier draft led with home fire on probability grounds — wrong frame for this book.
10. **Extreme rainfall is its own chapter** (owner caught its total absence). It behaves nothing
   like riverine flooding: atmospheric rivers, rain bombs, urban flash flooding, rain-on-snow.
11. **Landslide: no standalone chapter** (owner: unpreventable, and survival is binary). Kept only
   where action exists — **post-wildfire burn-scar debris flow**, which USGS issues hazard
   assessments for after every major fire and which is evacuable with warning. Lives in the
   wildfire aftermath section.
12. **EMP: a short section only** (~2pp — what it is, what to do, how to act), inside the space
   weather chapter. Not a scenario chapter, not a doomsday frame.
13. **Single consolidated volume**, not separate books. Combined value is the selling point.
14. **Pandemic/biological: excluded as a chapter** (agent's call, owner delegated). Draws hostile
   reviews regardless of content, is not nature's wrath in the sense the rest of the book is, and
   dilutes a book whose credibility rests on NOAA/USGS-sourced physical hazards. The apolitical
   parts — isolation, hygiene, water safety — stay inside Water & Sanitation Failure.

## Product definition

**Working title:** *The Storm-Ready Home* (final title TBD from A/B list)
**Countable units for the sales page:** N protections · 23 hazard playbooks · 60-day sequence ·
5 regions · 50-state packets
**Protection count:** set by enumeration in build phase 1, target 110–130. The sales page uses the
**true counted number**, never a rounded one — Yoder's "93 methods" reads as counted, and that is
the credibility mechanism. Do not pre-commit to 101.
**Price:** $47 (landing page shows $87 struck through)

### Regionalization — the pivot (differs from a literal clone; deliberate)

Lenny's Track W / Track C works because a lawn has exactly one grass type. **Hazards are not
exclusive** — Chicago needs tornado, blizzard, extreme heat, and grid failure. A clone would
break the book. So:

- **Regions are a priority overlay, not a gate.** Chapter 1 identifies the reader's region
  (Tornado Alley · Hurricane Coast · Wildfire West · Ice-Snow North · Quake West) and hands them
  an ordered first-ten protection list. Every hazard playbook stays in the book for every reader.
- **State data ships as a per-state packet, not as book bulk.** 3–4 pages per state: NWS forecast
  office, state emergency management agency, county alert signup, state insurance department
  mitigation-credit program, top three hazards with season windows. Used twice:
  - **free lead magnet** — "Get your state's storm packet, free" (personalized opt-in, far
    stronger than a generic one-pager for a geographically scattered audience);
  - **buyer bonus** — their state, plus all 50 "in case you move."
- Generated by script from a reviewed CSV of public-agency data, not hand-written. Date-stamped
  "verified <month year>", which also justifies the "lifetime updates" line in the value stack.

### The 23 hazard playbooks

**16 primary hazards** (nature's wrath — the book's identity):

| # | Chapter | pp | Notes |
|---|---|---|---|
| 1 | Tornado | 10 | |
| 2 | Hurricane & storm surge | 10 | |
| 3 | **Extreme rainfall & flash flood** | 10 | atmospheric rivers, rain bombs, urban flooding, rain-on-snow; sewer backup as aftermath sub-point |
| 4 | Riverine & coastal flooding | 10 | slow-onset, levee, dam failure |
| 5 | Wildfire | 10 | Santa Ana/Chinook wind-driven behavior; burn-scar debris flow as aftermath sub-point |
| 6 | Wildfire smoke & air quality | 8 | long-range smoke, filtration, DIY filter box |
| 7 | Hail & derecho / straight-line wind | 10 | #1 US property-claim driver — heavy money-chapter fuel |
| 8 | Lightning | 8 | |
| 9 | Blizzard & ice storm | 10 | |
| 10 | Extreme heat | 10 | compounds with grid failure |
| 11 | Extreme cold & deep freeze | 10 | frozen pipes as aftermath sub-point |
| 12 | Drought, water scarcity & dust | 10 | well failure; dust storms/haboobs folded in here |
| 13 | Earthquake | 10 | post-quake fire as aftermath sub-point |
| 14 | Tsunami | 8 | |
| 15 | Space weather & geomagnetic storms | 10 | Quebec 1989, Carrington; **EMP as a ~2pp section**; Faraday build |
| 16 | Volcanic ashfall | 4 | PNW/AK/HI; filtration, vehicles, roof load; USGS-sourced |
| | | **148** | |

**7 cross-cutting chapters** (apply across every hazard above):

| # | Chapter | pp |
|---|---|---|
| 17 | Grid failure & long outage | 8 |
| 18 | Systems dark — cash, comms, payment, paper records | 8 |
| 19 | Electronics & records protection — surge, backup, device power | 8 |
| 20 | Water & sanitation failure — boil-water, hygiene, isolation basics | 8 |
| 21 | Hazmat released *by* a disaster — rail, refinery, chemical | 8 |
| 22 | Radiological proximity — NRC 10-mile EPZ, what KI does and doesn't do | 6 |
| 23 | Medical care when EMS cannot reach you | 10 |
| | | **56** |

### Page architecture — target 480–500pp (6×9 trim)

The 500pp the owner originally asked for, reached by function rather than filler. Padding to a page
target is what produces refunds and one-star "AI slop" reviews; every block below does a job.

| Part | Pages | Contents |
|---|---|---|
| P0 Front | 12 | How to use · the 15-minute start · find your region · disclaimer |
| P1 Why people die | 26 | 6 kill mechanisms + the timeline of a disaster; the forensic spine |
| P2 The Core Six | 62 | water · food · body temperature · power · air+sanitation · medical |
| P3 Hazard playbooks | 204 | the 23 chapters above |
| P4 People & places | 34 | kids · elderly · disability · pets/livestock · apartment vs house vs mobile home · car · work/school |
| P5 Warning literacy | 30 | reading NWS products, radar, alerts, sirens, evacuation orders → then insurance claims + FEMA aid after |
| P6 The Binder | 80 | fillable plans, checklists, logs, wallet cards, home inventory, document vault |
| P7 The 60 Days | 22 | day-by-day sequence, drill scripts, sources |
| Appendix | 18 | state authority directory (compact lookup) |
| **Total** | **488** | |

**Per-protection template** (Yoder's, adapted): number · one-line what-it-prevents · cost · time ·
materials · steps · **what it does NOT do** (the honesty line that builds trust) · which regions
prioritize it.

**Chapter openers** carry the forensics: each hazard playbook opens with a real cited event from
channel research (NWS Service Assessments, NIST reports, day-after archives) and converts it to
action. This is the differentiation and it recycles research already paid for per episode.

## Flag avoidance (four distinct risks)

1. **Copyright — researched 2026-07-26 at owner's request. Not legal advice; see the review note.**

   **The rule:** 17 U.S.C. § 105 places all works of the US Government in the public domain,
   published or unpublished. A "work of the US Government" is one prepared by an **officer or
   employee as part of official duties**. Public domain permits commercial use with no permission
   and no fee. NOAA states it directly: images in their library are public domain and may be used
   without express permission.

   **Five traps, all confirmed:**
   1. **Contractor work is not automatically PD.** The statute deliberately declined to bar
      copyright in works produced under government contract or grant; contractors may retain it.
   2. **"Unless otherwise noted in the credit or caption"** — NOAA's own carve-out. Federal sites
      host contributed and licensed material. **Every asset's caption is read before use**, not
      spot-checked. Same trap as the storm-chaser rule in repo CLAUDE.md.
   3. **Federal *video* is guilty until proven innocent.** NOAA warns their videos often contain
      third-party footage and the provider must be contacted. Federal *stills* are innocent until
      the caption says otherwise.
   4. **Logos and endorsement are a separate body of law from copyright.** The NOAA emblem needs
      written consent; the "National Weather Service" name and visual identifier are
      trademark-protected. Material may not be used to imply endorsement or affiliation with the
      US government, and commercial use especially must not imply NOAA endorsement. **Therefore:
      sources cited on a credits page; no federal seal or agency logo on the cover, the landing
      page, or any ad.**
   5. **Two categories § 105 does not reach:** state and local agency works (state EMA, county
      offices — states can and do hold copyright) and foreign government works (Environment Canada
      is *not* US public domain). Separately, a FEMA photo is copyright-free but a recognizable
      person in it may retain publicity/privacy rights, which weighs more in a sales context than
      an editorial one — prefer wide shots and non-identifiable subjects.

   **Protocol:** per-asset provenance log with source URL, agency, verbatim caption, capture date,
   and PD determination. Reuse the existing pattern at `episodes/ep1-joplin/media/provenance.csv`
   rather than inventing a new one.

   **⚠ Recommended spend:** one paid IP-attorney review of the provenance protocol and the
   credits/disclaimer page — not of every asset. Cheap insurance on a commercial product. Owner's
   call; the review document can be prepared on request.

   Zero stock imagery. Survivor quotes come from NWS service assessments (PD) or attributed news
   archives — **never fabricated**, per repo CLAUDE.md.
2. **Liability.** Prominent disclaimer; not medical or legal advice. No medication dosing, no DIY
   gas or electrical work instructions. Every instruction traceable to a citable authority
   (NWS/CDC/Red Cross/IBHS) — defensible, not opinion. Money-chapter figures carry the lawn
   page's "example math for comparison only, your situation differs" line verbatim in spirit.
3. **Payment processor.** No firearms/ammo/tactical content (decision 3). No financial-advice
   framing — Gumroad explicitly prohibits unlicensed financial advice. No supplements. Tone is
   FEMA family-safety, never doomsday-political.
4. **Platform AI disclosure.** Gumroad requires none. If this is ever mirrored to Amazon KDP, KDP
   requires AI-use disclosure — decide at that point, do not pre-commit.

## Visual system

**Two tiers, and tier 1 must stand alone.**

- **Tier 1 — code-drawn, $0, built first.** All data figures: radar plots, timelines, comparison
  tables, floor plans, the money-chapter tables, checklists, binder forms. HTML/CSS/SVG rendered
  to PDF through headless Chrome (the box already runs chrome-devtools + Node ≥22 for hyperframes).
  Infinitely revisable, no API dependency.
- **Tier 2 — generated illustration, BLOCKED on DeAPI keys.** Concept sketches and section plates
  that make abstract ideas land fast. Image slots are defined in the layout now and filled later;
  **the book must lay out complete and shippable with tier 1 only.**
- When keys land: standard cost railguards per global CLAUDE.md (hard call cap, dry-run 2 first,
  pre-increment reservation, `.done` resume) plus the JP image-QC sweep on every asset — hands and
  fingers, faces, eyeglasses, garbled burned-in text.

**⚠ OPEN — OWNER ACTION: DeAPI API keys not yet available. Image count cannot be budgeted until
they are. Surface this before any image work begins.**

## The Money Chapter

Stacked structure, three deltas, ordered small → large:

| Delta | Type | Mechanism |
|---|---|---|
| A · Kit markup | one-time | Pre-built 72-hour kits vs the same contents assembled from a grocery list. "You are not paying for supplies. You are paying for someone else to know what goes in the bucket." — the direct analog of Lenny's service math. |
| B · Insurance + mitigation credits | **recurring annual** | Wind/hail mitigation credits, IBHS FORTIFIED, deductible structure, coverage gaps found before the event. This is the Yoder-equivalent recurring number and the honest headline. |
| C · Claim recovery | event-conditional | Documented vs undocumented contents claim; knowing the FEMA IHP and appeal path. The big number, and the one needing the heaviest disclaimer. |

**Every figure must be sourced before it is written.** Named source targets, to be verified during
build, none of them assumed: NFIP claim averages (FEMA), FEMA IHP average award data, IBHS
FORTIFIED and state insurance-department wind-mitigation credit filings, BLS/EIA consumer data,
USDA food-loss guidance, retail kit pricing captured with dated screenshots.
**No number ships unsourced.** If a delta cannot be sourced, it is cut, not estimated.

## Landing page

Static, Cloudflare Pages. Gumroad overlay checkout (no custom payment code — Gumroad is the
backend, matching the JP-market setup). Section order, adapted from the reference pages:

1. Hero — outcome + the stacked dollar delta + page count + "earns the $47 back before the season"
2. Proof strip — subscriber count · rating · 7-day refund
3. What it is — 101 protections · 12 playbooks · 60 days · 5 regions
4. **The Money Chapter** (directly below pricing, per owner's note — the highest-leverage section)
5. Find your region — the 5-region selector, makes it personal before the ask
6. Look inside — 12-page sample spread, real pages
7. The Binder — screenshots of fillable pages
8. Weather Joe — persona origin story + personal comment block + headshot
9. Value stack — itemized to a total, collapsing to $47 (Yoder's exact mechanic)
10. Reviews — at least one naming the money chapter specifically
11. FAQ — format, refund, "does this work in my state", "I rent", "I'm not handy"
12. Last call — $87 struck to $47, urgency, guarantee restated

**Lead magnet vs buyer bonus — priced, then given away** (Yoder's mechanic; owner-confirmed):

| Stage | What | Shown as |
|---|---|---|
| Pre-purchase, email-gated | the reader's ONE state packet | "$19 value — free, on me" |
| Buyer bonus | all 50 states + fillable version + season-window calendar | "$29 value — included" |

The free packet proves the book is real; the buyer version is strictly bigger, so nothing is
double-sold. Lead magnet pinned in every video description.

Gumroad cannot show a struck-through price natively — put the $87 anchor on the landing page and
in the Gumroad product description, and use a discount code for the launch price.

## Build sequence

| Phase | Output | Gate |
|---|---|---|
| 1 | Full outline: all 101 protections named + assigned to parts, 60-day sequence mapped, region priority lists | Owner sign-off on the outline before any prose |
| 2 | Money Chapter research pack — every figure with its source URL and capture date | No unsourced number survives |
| 3 | Tier-1 visual system + PDF pipeline; 12-page sample spread rendered | Owner eyeballs the actual rendered PDF, not a description |
| 4 | Prose, part by part, P1 → P7 | Per-part read-through; refund-risk check on padding |
| 5 | Binder (P6) + state-packet generator | Generated packets spot-checked against live agency pages |
| 6 | Tier-2 images (unblocked by keys) + QC sweep | Every image eyeballed; railguards on |
| 7 | Landing page + Gumroad product + lead-magnet delivery | End-to-end test purchase with a real card |

## Verification

- **Book:** render the full PDF and read the actual artifact — page count, every figure, every
  cross-reference, the binder forms printed on paper. Never certify from the outline.
- **Money chapter:** each figure re-checked against its cited source on the day of ship.
- **State packets:** random sample of 8 states, every URL and phone number resolved live.
- **Funnel:** real test purchase end to end — payment → Gumroad delivery email → file opens on
  phone and desktop → refund path works. Lead-magnet opt-in tested with a real inbox.
- **Flag check:** full-text sweep for firearms/ammo/financial-advice language; figure-by-figure
  provenance audit against the copyright rule before publish.

## Deliberately excluded

- Home defense / firearms (decision 3)
- 50 illustrated state pages (owner-rejected; reader-value argument is correct)
- 12-month calendar (owner: 60 days max)
- A second SKU or subscription — one book, sold properly (decision 13)
- Any custom payment/backend code — Gumroad owns checkout
- Household-accident content as peer chapters (decision 9 — sub-points only)
- Standalone landslide chapter (decision 11 — burn-scar debris flow only)
- Pandemic/biological chapter (decision 14)
- Nuclear-EMP scenario chapter (decision 12 — ~2pp section only)
- Doomsday framing of any kind: grid-down-for-a-year, EMP collapse, societal breakdown. Reframes
  the book onto the prepper shelf and puts the Gumroad account in the risk zone.
- Avalanche (recreational, not household), airplane crash (no household mitigation — good video
  topic, not a book chapter), meteor/EMP-war speculation
