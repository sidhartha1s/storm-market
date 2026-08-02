#!/usr/bin/env python3
"""Merge the derived per-column CSVs into state_data.csv, the file build.py reads.

Each derive_*.py script owns one group of columns and writes its own CSV keyed by state. This
assembles them into the schema in README.md. It does not invent, infer or fill anything: a
column no derive script has produced yet stays empty, which is what makes an incomplete
appendix visible instead of plausible.

Deliberate design points:

  - **verified_on must be passed in.** It is the date the row's fields were actually checked
    against live sources, so stamping "today" automatically would quietly re-certify a merge
    of month-old CSVs. Pass the date you ran the derive scripts.
  - **A field arrives with its source or not at all.** Sources come from the derive scripts;
    this script never supplies one, so a value can never end up published unsourced.
  - **Unknown columns in a fragment are dropped loudly.** energy.csv carries a public-inquiry
    phone number that the schema has no column for; that is reported rather than silently
    discarded, so the schema gap is a decision and not an accident.

Usage:
    python3 merge.py --date 2026-07-29
    python3 merge.py --date 2026-07-29 --report    # also print per-column fill counts
"""

import argparse
import csv
import re
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "state_data.csv"

# The schema, in the order state_data.csv writes it. Must match README.md.
COLUMNS = [
    "state", "abbr",
    "em_agency", "em_url", "em_url_src", "em_phone", "em_phone_src",
    "alerts_note", "alerts_url", "alerts_url_src",
    "doi_agency", "doi_url", "doi_url_src", "doi_phone", "doi_phone_src",
    "mitigation_program", "mitigation_url", "mitigation_url_src",
    "wind_deductible_note", "roof_acv_note",
    "pharmacy_refill_law", "pharmacy_refill_law_src",
    "winter_disconnect", "summer_disconnect",
    "energy_assist_url", "energy_assist_url_src",
    "energy_assist_phone", "energy_assist_phone_src",
    "well_test_contact", "well_test_url", "well_test_url_src",
    "hazard_1", "hazard_2", "hazard_3",
    "season_1", "season_2", "season_3",
    "region_overlay", "verified_on",
]

# Fragments in merge order. Later fragments never overwrite a value an earlier one supplied.
FRAGMENTS = ["hazards.csv", "agencies.csv", "energy.csv", "water.csv",
             "em_phone.csv", "mitigation.csv", "deductibles.csv", "pharmacy.csv", "disconnect.csv"]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def read_fragment(path):
    if not path.exists():
        print(f"  {path.name}: absent, skipped")
        return {}, []
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    by_state = {row["state"].strip(): row for row in rows if row.get("state")}
    extra = [c for c in (rows[0] if rows else {}) if c not in COLUMNS]
    print(f"  {path.name}: {len(by_state)} rows"
          + (f", {len(extra)} column(s) not in the schema: {', '.join(extra)}" if extra else ""))
    return by_state, extra


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True,
                        help="ISO date the derive scripts were run against live sources")
    parser.add_argument("--report", action="store_true", help="print per-column fill counts")
    args = parser.parse_args()

    if not DATE_RE.fullmatch(args.date):
        raise SystemExit("FAIL: --date must be ISO yyyy-mm-dd.")

    print("reading fragments:")
    fragments = [read_fragment(HERE / name) for name in FRAGMENTS]

    present = [set(by_state) for by_state, _ in fragments if by_state]
    if not present:
        raise SystemExit("FAIL: no fragment produced any rows. Run the derive_*.py scripts first.")

    # A fragment that spells a state differently would silently add a row carrying half the
    # columns, which reads as a real state in the output. Refuse to merge instead.
    states = set.union(*present)
    for name, (by_state, _) in zip(FRAGMENTS, fragments):
        if by_state and set(by_state) != states:
            missing = sorted(states - set(by_state))
            raise SystemExit(
                f"FAIL: {name} does not cover the same states as the other fragments.\n"
                f"       missing from {name}: {missing}\n"
                "       Usually a spelling difference, not a real gap.")

    rows = []
    for state in sorted(states):
        merged = {column: "" for column in COLUMNS}
        merged["state"] = state
        for by_state, _ in fragments:
            source = by_state.get(state, {})
            for column in COLUMNS:
                value = (source.get(column) or "").strip()
                if value and not merged[column]:
                    merged[column] = value
        merged["verified_on"] = args.date
        rows.append(merged)

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nwrote {OUT}  ({len(rows)} rows, verified_on {args.date})")
    if args.report:
        print("\nper-column fill:")
        for column in COLUMNS:
            filled = sum(1 for row in rows if row[column])
            flag = "" if filled == len(rows) else "   <-- gap"
            print(f"  {column:<24} {filled:>2}/{len(rows)}{flag}")


if __name__ == "__main__":
    main()
