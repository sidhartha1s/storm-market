# Appendix B — State Authority Directory, and the 50 state packets

Status: **schema and generator built, data NOT collected.** No row of real agency data exists yet.

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

Not a scrape and not a model guess. Per state, in this order:

1. The state emergency management agency's own site — agency name, phone, alert enrolment page.
2. The state Department of Insurance site — consumer helpline, complaint page, and any published bulletin on
   wind/hail deductibles or roof settlement.
3. The state board of pharmacy or the statute itself for the emergency refill provision.
4. The state public utility commission for disconnection moratoria.
5. The state health department or extension service for well testing.
6. Top three hazards from NOAA/state hazard mitigation plan, not from impression.

**Then a second pass by a different reviewer** clicking every URL, because a dead link in a paid product is
the most common complaint in this category.

---

## Files

| File | What |
|---|---|
| `state_data.csv` | Headers only until collection is done. One row per state. |
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

1. **No data collected.** ~51 rows × ~20 sourced fields. This is the largest remaining unit of work in the
   whole product and it is entirely research rather than writing.
2. **The landing page's free-packet email gate cannot deliver anything until packets exist.** Currently the
   form fails loudly by design rather than pretending to subscribe.
3. **Re-verification cadence.** Agency URLs and phone numbers rot. The packets print `verified_on`, and the
   set needs a re-check before each launch push.
