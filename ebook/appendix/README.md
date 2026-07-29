# Appendix B — State Authority Directory, and the 50 state packets

Status: **schema and generator built; six of the fourteen sourced column groups collected for all 51
rows, and `build.py --check` passes.** The remaining groups are listed under Blockers with the aggregator
hunt to date, including the dead ends, so nobody re-walks them.

This directory holds two deliverables that share one dataset:

| Deliverable | Where it goes | Pages |
|---|---|---|
| **Appendix B** — compact state lookup | in the book, one row per state | ~18 |
| **The 50 state packets** — free lead magnet + buyer bonus | landing page email gate, one PDF per state | ~4 each |

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
| `merge.py` | Assembles the fragments into `state_data.csv`. Fails if two fragments disagree on the state set. |
| `hazards.csv`, `agencies.csv`, `energy.csv`, `water.csv` | The per-column fragments. Committed so a run is auditable. |
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

1. **Six column groups collected, six to go.** Filled for all 51 rows: hazards, seasons, regions,
   `doi_phone`, `well_test_contact`; and near-complete `em_url`, `doi_url`, `doi_agency`, `well_test_url`,
   `energy_assist_url`. **Still empty, with no working national source found yet:**

   | Column | Status of the hunt |
   |---|---|
   | `em_phone` | usa.gov's directory carries no phone. Scraping a number off each agency page is exactly the "inferred phone" the hard rule bans, so this needs a published list. |
   | `alerts_note`, `alerts_url` | County-level, so no national list exists. Best route: link discovery over the 51 agency pages already cached, publishing only a link whose own text names alerts. |
   | `mitigation_program`, `mitigation_url` | Blank for most states by design — only a handful run one. FL, CA and AL are already written up in Part Five from their own programme pages. |
   | `wind_deductible_note`, `roof_acv_note` | Regulatory facts, per state. NAIC publishes reports but no machine-readable table. |
   | `pharmacy_refill_law` | NCSL holds the table; **ncsl.org sits behind a Cloudflare bot check** that headless Chrome does not clear. |
   | `winter_disconnect`, `summer_disconnect` | The LIHEAP Clearinghouse held exactly this table; **`liheapch.acf.gov` and `liheapch.acf.hhs.gov` both time out entirely** — that site appears to be gone rather than blocked. Needs a replacement. |

   Dead ends already tried, so nobody repeats them: `content.naic.org` through the indexing tool returns 3.5 KB
   of site chrome (fetch it raw instead — 154 KB, with the per-state data), `ready.gov` and `fema.gov` state
   lists 403, the `iii.org` deductible article 404s, `nclc.org` shutoff protections 404s, `neada.org` state
   offices 404s.

2. **One schema gap to decide.** `energy.csv` carries a verified public-inquiry phone for 49 states and the
   schema has no column for it. `merge.py` reports the dropped column on every run rather than discarding it
   silently. Worth adding — in an outage a reader needs a number more than a URL — but it is a schema
   change, so it waits for a decision.
2. **The landing page's free-packet email gate cannot deliver anything until packets exist.** Currently the
   form fails loudly by design rather than pretending to subscribe.
3. **Re-verification cadence.** Agency URLs and phone numbers rot. The packets print `verified_on`, and the
   set needs a re-check before each launch push.
