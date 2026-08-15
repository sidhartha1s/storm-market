# Appendix B — State Authority Directory, and the 50 state packets

Status: **schema and generator built; every sourced column group has been attempted for all 51 rows, and
`build.py --check` passes.** Two groups (`em_phone`, `wind_deductible_note`) are fully filled from a
national directory. Four more (`mitigation_program`, `pharmacy_refill_law`, `winter_disconnect`,
`summer_disconnect`) are filled state-by-state where a citable source exists — correctly partial, not
incomplete, since most states genuinely have nothing to cite for several of these. One (`roof_acv_note`)
stayed empty: no citable source was found for any state. The remaining gaps and the dead ends behind them
are listed under Blockers so nobody re-walks them.

This directory holds two deliverables that share one dataset:

| Deliverable | Where it goes | Pages |
|---|---|---|
| **Appendix B** — compact state lookup | in the book, one row per state | ~18 |
| **The 50 state packets** — free lead magnet + buyer bonus | a $0 Gumroad product (`/l/packet`), all 51 zipped; also bundled with the paid product | ~4 each |

Same CSV, two renderers. That is the whole reason the 50-states problem became tractable: the owner's
objection was correct — *"suppose im from chicago, why the hell would i need to know 49 other states'
information on my book"* — so the book carries a compact one-row-per-state lookup, and the depth goes into a
per-state packet where the reader only ever sees their own.

---

## Hard rule on data

**Every field is either sourced to a primary agency page and dated, or it is empty.**

No inferred phone numbers. No guessed URLs. No "typically" values. A blank cell in a published directory is
an honest gap; a wrong phone number in an emergency directory is a genuine harm, and a wrong URL is the kind
of error that gets a paid product refunded.

`state_data.csv` therefore ships with headers and zero rows until collection is done, and `build.py` **fails
loudly** rather than rendering placeholder text.

---

## Schema — `state_data.csv`

One row per state, plus DC. Every value-bearing column has a paired `*_src` column holding the URL it came
from, and the row carries one `verified_on` date.

| Column | Content | Notes |
|---|---|---|
| `state` | Full name | |
| `abbr` | Two-letter | |
| `em_agency` | State emergency management agency, official name | |
| `em_url`, `em_url_src` | Its site | |
| `em_phone`, `em_phone_src` | Non-emergency main line | Never a 911 substitute |
| `alerts_note` | How residents enrol in state/county alerts | One sentence |
| `alerts_url`, `alerts_url_src` | Enrolment page | |
| `doi_agency` | Department of Insurance / equivalent | |
| `doi_url`, `doi_url_src` | Consumer complaints and lookup page | |
| `doi_phone`, `doi_phone_src` | Consumer helpline | |
| `mitigation_program` | Named grant or credit programme, if any | e.g. a fortified-roof grant |
| `mitigation_url`, `mitigation_url_src` | | Blank where none exists — most states |
| `wind_deductible_note` | Whether separate wind/hail or hurricane deductibles are common/regulated | Serves Protection 102 |
| `roof_acv_note` | Whether ACV roof schedules are permitted/common | Serves Playbook 7 |
| `pharmacy_refill_law` | Emergency prescription refill provision | Serves Protection 59 |
| `pharmacy_refill_src` | Statute or board page | |
| `winter_disconnect` | Winter disconnection moratorium, if any | Serves Playbook 11 |
| `summer_disconnect` | Summer/heat disconnection protection, if any | Serves Playbook 10 |
| `energy_assist_url`, `_src` | State low-income energy assistance page | |
| `energy_assist_phone`, `_src` | LIHEAP public-inquiry phone number | Added 2026-08-02 — in an outage a reader needs a number more than a URL |
| `well_test_contact` | Where private well owners get water tested | Serves Protections 9, 10 |
| `well_test_url`, `_src` | | |
| `hazard_1`, `hazard_2`, `hazard_3` | Top three hazards | Must match a Part Three playbook name exactly |
| `season_1`, `season_2`, `season_3` | Season window per hazard | e.g. "Apr–Jun" |
| `region_overlay` | Which of the five book regions apply | Pipe-separated |
| `verified_on` | ISO date the row was checked | **Required.** Row is rejected without it |

---

## Collection method

**One national directory beats fifty-one hand lookups, wherever one exists.** The original plan was to visit
each state's own site per column, which is ~1,000 lookups and starts rotting the moment it is finished. Where
a federal or national body already maintains the whole set, that body is the source: one citable URL per
column, maintained by someone else, and a re-run detects drift instead of hiding it. Each column group lives
in its own `derive_*.py`, writes its own CSV fragment, and `merge.py` assembles `state_data.csv`.

| Column group | Source | Script |
|---|---|---|
| `hazard_1..3`, `season_1..3`, `region_overlay` | NOAA NCEI Storm Events, direct deaths 2010–2025 | `derive_hazards.py` |
| `em_url`, `em_agency` | usa.gov state emergency management directory; agency name from each site's own `<title>` | `derive_agencies.py` |
| `doi_agency`, `doi_phone`, `doi_url` | NAIC state insurance department directory and its per-state detail pages | `derive_agencies.py` |
| `energy_assist_url` | ACF LIHEAP state and territory contact listing | `derive_energy.py` |
| `well_test_contact` | EPA list of state SDWA laboratory certification programs, 40 CFR 142.10(b)(3)(i) | `derive_water.py` |
| `well_test_url` | EPA "Private Drinking Water Well Programs in Your State" | `derive_water.py` |
| `em_phone` | EMAC (Emergency Management Assistance Compact) state contact directory | `derive_em_phone.py` |
| `wind_deductible_note` | NAIC "Hurricane Deductibles" topic page — the 19 states + DC it names, and an honest non-claim for the rest | `derive_deductibles.py` |
| `mitigation_program`, `mitigation_url` | Hand-verified against each programme's own government page — no national list exists | `derive_mitigation.py` |
| `pharmacy_refill_law` | Hand-verified against each state's own statute/rule (or licensing board's published guidance) — no working national table exists | `derive_pharmacy.py` |
| `winter_disconnect`, `summer_disconnect` | Hand-verified against each state utility commission's own page or rule — no working national table exists | `derive_disconnect.py` |

Nothing here is a scrape of a search result and nothing is a model guess. Where a source omits a state, the
cell stays empty and the run prints which state and why.

### Being blocked is not being dead

`verify_urls.py` checks every URL before it is published and returns one of three verdicts. The first version
of these scripts had only two, and it was wrong in a way worth recording:

- **live** — fetched directly, or rendered in headless Chrome. Publish.
- **blocked** — the host refused *us*: 403, a TLS or connection failure, a timeout, or a hostname this
  machine will not resolve. **Publish anyway.** The citation is the maintained national directory that lists
  the page, which is better evidence than our own refused request. Treating 403 as "gone" blanked nine
  emergency-management URLs that usa.gov actively maintains, and a resolution failure says nothing about the
  page at all — this machine cannot resolve `wi.gov` while `wisconsin.gov` resolves fine.
- **dead** — the target itself answered 404 or 410. Drop it: the directory has gone stale for that state.

Every run prints the split, so the output always says how much was confirmed live versus taken on the
directory's word. That number belongs in the launch checklist.

**A second pass still clicks every URL before launch**, because a dead link in a paid product is the most
common complaint in this category, and "blocked to us" is exactly the set a human should eyeball.

---

## Files

| File | What |
|---|---|
| `state_data.csv` | Generated by `merge.py`. One row per state, plus DC. Never hand-edited. |
| `verify_urls.py` | The shared three-verdict URL check. Every derive script uses it. |
| `derive_hazards.py` | Hazards, seasons, regions from NCEI Storm Events. Caches 178 MB under `.storm-events-cache/`. |
| `derive_agencies.py` | Emergency management and insurance regulator columns. Caches pages under `.agency-cache/`. |
| `derive_energy.py` | Energy-assistance column from the ACF LIHEAP listing. |
| `derive_water.py` | Private-well testing columns from two EPA sources. |
| `derive_em_phone.py` | `em_phone` from EMAC's state contact directory. Caches the page under `.agency-cache/`. |
| `derive_deductibles.py` | `wind_deductible_note` for all 51 rows, parsed from NAIC's Hurricane Deductibles page. |
| `derive_mitigation.py` | `mitigation_program`/`mitigation_url` — 7 hand-researched states, documented dead ends for the rest. |
| `derive_pharmacy.py` | `pharmacy_refill_law` — 15 hand-researched states, documented dead ends (Tennessee, Mississippi). |
| `derive_disconnect.py` | `winter_disconnect`/`summer_disconnect` — 12 + 3 hand-researched states. |
| `merge.py` | Assembles the fragments into `state_data.csv`. Fails if two fragments disagree on the state set. |
| `hazards.csv`, `agencies.csv`, `energy.csv`, `water.csv`, `em_phone.csv`, `deductibles.csv`, `mitigation.csv`, `pharmacy.csv`, `disconnect.csv` | The per-column fragments. Committed so a run is auditable. |
| `build.py` | Renders both outputs. Fails on missing `verified_on`, unknown hazard names, or a URL that is not `https://`. |
| `templates/appendix_row.html` | The compact in-book row |
| `templates/packet.html` | The 4-page per-state packet |
| `out/` | Generated — not committed |

## Running it

```bash
python3 build.py --check                 # validate the CSV only, exit 1 on any problem
python3 build.py --appendix              # writes out/appendix-b.html
python3 build.py --packets               # writes out/packets/<abbr>.html for every complete row
python3 build.py --packets --only IL,TX  # a subset while iterating
```

Then the HTML goes through the same `fitcheck.mjs` gate as the rest of the book, and the packets go through
Chrome `--print-to-pdf` with an **absolute** output path.

## Packet structure — 4 pages

1. **Your state, your three hazards** — with season windows, and your region's first-ten protection list.
2. **Who to call** — emergency management, insurance regulator, energy assistance, well testing, with the
   verified-on date printed on the page so the reader knows how fresh it is.
3. **Your money page** — the state's mitigation programme if it has one, the deductible and roof-settlement
   note, the emergency refill law, the disconnection protections.
4. **Your one-page plan** — a condensed version of the binder front sheet, pre-filled with the state's
   specifics.

## Blockers

1. **Twelve of the fourteen sourced column groups collected, two genuinely incomplete by design.**
   Filled for all 51 rows: hazards, seasons, regions, `doi_phone`, `well_test_contact`, `em_phone`,
   `wind_deductible_note`; and near-complete `em_url`, `doi_url`, `doi_agency`, `well_test_url`,
   `energy_assist_url`. Correctly *partial* (a citable source exists for only some states, and the
   rest were searched, not skipped): `mitigation_program`/`mitigation_url` (7/51),
   `pharmacy_refill_law` (15/51), `winter_disconnect` (12/51), `summer_disconnect` (3/51). **Still
   fully empty, with no working source found:**

   | Column | Status of the hunt |
   |---|---|
   | `alerts_note`, `alerts_url` | County-level, so no national list exists. Best route: link discovery over the 51 agency pages already cached, publishing only a link whose own text names alerts. |
   | `roof_acv_note` | No national or per-state source ever resolved to a *citable regulatory fact*. NAIC's own Hurricane Deductibles page (used for `wind_deductible_note`) covers named-storm deductibles, not roof ACV schedules, and has no equivalent page for this. A law firm's 50-state "matching regulations" chart (mwl-law.com) fetches as an unreadable compressed PDF. Cosmetic-damage-exclusion endorsement lists (ISO forms HO 06 43/44) turned up only through secondary aggregator blog posts with no primary regulatory filing behind the "which states approved this form" claim — not solid enough to cite in an emergency directory. Left empty rather than publish a plausible-sounding but unverified state list. |

   Dead ends already tried, so nobody repeats them: `content.naic.org` through the indexing tool returns 3.5 KB
   of site chrome (fetch it raw instead — 154 KB, with the per-state data), `ready.gov` and `fema.gov` state
   lists 403, the `iii.org` deductible article 404s, `nclc.org` shutoff protections 404s, `neada.org` state
   offices 404s, `liheapch.acf.gov`/`liheapch.acf.hhs.gov` time out entirely, `ncsl.org` sits behind a
   Cloudflare bot check headless Chrome does not clear, and the NGA's utility-affordability memo and its
   linked PDF describe only an aggregate count of states with a COVID-era moratorium, never which states or
   what the rule is.

   What broke those columns open instead, and what it cost:

   - **`em_phone`** — usa.gov's directory carries no phone, and scraping one off each of 51 agency
     sites is exactly the "inferred phone" the hard rule bans. EMAC (the Emergency Management
     Assistance Compact, administered under NEMA) publishes one phone per state for its own
     mutual-aid use, which is why it stays accurate: a wrong number there breaks EMAC's real
     deployments, not just this book. `derive_em_phone.py`, 51/51.
   - **`wind_deductible_note`** — NAIC's Hurricane Deductibles topic page states outright which 19
     states plus DC have a named-storm deductible "as of June 2025." `derive_deductibles.py`
     parses that sentence directly rather than hardcoding the list, so a re-run catches NAIC
     updating it. 51/51 (a sourced note either way, not just for the 20 that are listed).
   - **`mitigation_program`** — no national table exists; each of FL, CA, AL (already in Part
     Five), LA, OK, SC and KY was confirmed against the programme's own government page.
     Mississippi's "Strengthen Mississippi Homes" program was found and then dropped: its funding
     was suspended by the legislature in a 2025 special session, and neither URL a search turns up
     for it currently resolves (one is a live "Page not found" wrapper, the other 404s) — a
     programme that cannot be pointed at a live official page isn't citable yet. Georgia's and
     Mississippi's own FORTIFIED insurance-premium discounts run through state-created residual
     insurers (GUA, MWUA), which is a rate discount, not a grant/credit *programme* — left out
     rather than stretched to fit. `derive_mitigation.py`, 7/51.
   - **`pharmacy_refill_law`** — NCSL's table is unreachable (see dead ends above). Healthcare
     Ready's 2022 multi-state review was used only as a map of where to look, not as the citation:
     it groups states into buckets without a citable statute for most of them. Every row in
     `derive_pharmacy.py` traces to the state's own statute, admin rule, or (LA, GA) the licensing
     board's own published guidance. One specific trap worth flagging: a search repeatedly
     surfaced "Tennessee, TCA § 58-2-101, 20-day supply for displaced residents" as Tennessee's
     provision — that section is the Emergency Management Act's *definitions* clause and says
     nothing about pharmacy refills. Left blank rather than publish a citation that doesn't hold
     up on inspection. 15/51.
   - **`winter_disconnect`/`summer_disconnect`** — same shape as pharmacy: no working national
     table, so each row in `derive_disconnect.py` is sourced to the state utility commission's own
     page or rule (Minnesota, Kansas, New York, Massachusetts, Connecticut, Illinois, Michigan,
     Ohio, Pennsylvania, Wisconsin, Iowa, Idaho for winter; Arizona, California, Texas for summer).
     Most of these rules protect a narrower group than "everyone" — low income, a hardship
     declaration, a kept payment plan — so the note says who is protected, not just the date
     range. 12/51 and 3/51.

2. **Delivery is Gumroad's, not ours (2026-08-15).** The packets ship as a $0 Gumroad product at
   `/l/packet` — all 51 in one zip, built by zipping `out/packets/*.pdf`. The landing page links
   straight to it. The email-gate Pages Function that used to sit here was deleted: it needed a Kit
   API key that never existed and returned HTTP 500 on every real submit. Re-zip and re-upload the
   product's file whenever the packets are regenerated.
3. **Re-verification cadence.** Agency URLs and phone numbers rot. The packets print `verified_on`, and the
   set needs a re-check before each launch push.
