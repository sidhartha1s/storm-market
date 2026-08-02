#!/usr/bin/env python3
"""Derive wind_deductible_note for all 51 rows from NAIC's Hurricane Deductibles topic page.

This is the one column in the "regulatory facts, per state" group that has a real national
source: the NAIC — the regulators' own standard-setting body, not an aggregator — maintains a
dated background page naming exactly which states have a separate hurricane or named-storm
deductible. Its own words, as of the page's last update:

    "As of June 2025, nineteen states and the District of Columbia have some form of hurricane
    or named storm deductible in place. These states include Alabama, Connecticut, Delaware,
    Florida, Georgia, Hawaii, Louisiana, Maine, Maryland, Massachusetts, Mississippi, New
    Jersey, New York, North Carolina, Pennsylvania, Rhode Island, South Carolina, Texas, and
    Virginia."

That is 19 named states; DC makes the twentieth jurisdiction the page counts. Two things the note
does NOT claim, so this script doesn't either:

  - it is a list of *hurricane/named-storm* deductibles specifically. The same page separately
    describes wind/hail deductibles as something "some policies" carry in any state, with no
    state list — so the note for a state outside the 19+DC says what NAIC does and doesn't say,
    rather than asserting the state has no wind deductible of any kind at all.
  - NAIC says "other states may allow insurers to include hurricane deductibles in property
    insurance products" — so absence from the list is NAIC not naming the state, not NAIC
    affirmatively ruling it out. The note is worded to match that.

wind_deductible_note has no paired *_src column in the schema (see README.md), so the citation is
carried inline in the note text itself rather than in a separate field — the same way the
manuscript's «SRC: ...» lines cite inline.

Usage:
    python3 derive_deductibles.py                # fetch (or reuse cache), verify, write deductibles.csv
    python3 derive_deductibles.py --refresh       # re-fetch the NAIC page
"""

import argparse
import csv
import html
import re
from pathlib import Path

import verify_urls
from verify_urls import DEAD

HERE = Path(__file__).parent
CACHE = HERE / ".agency-cache"
OUT = HERE / "deductibles.csv"

SOURCE = "https://content.naic.org/insurance-topics/hurricane-deductibles"

STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
    "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
    "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
    "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
    "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
}

# The sentence naming the 19 states is stable enough to parse directly, but it is re-parsed from
# the cached page rather than hardcoded, so a re-run catches NAIC updating the list or the date.
LIST_RE = re.compile(
    r"As of ([^,]+, \d{4}), (?:nineteen|\d+) states? and the District of Columbia have some form "
    r"of hurricane or named storm deductible in place\. These states include ([^.]+)\.")


def cached(refresh=False):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / "naic_hurricane_deductibles.html"
    if not path.exists() or refresh:
        data = verify_urls.fetch(SOURCE, timeout=60)
        path.write_bytes(data)
    return path.read_text(encoding="utf-8", errors="replace")


def parse(page):
    # All tags stripped to plain text first — the sentence is broken across several inline tags
    # in the raw markup, so matching against tag-free text is far more robust than trying to
    # thread the regex through however many <strong>/<a> wrappers happen to be present.
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", page)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    match = LIST_RE.search(html.unescape(re.sub(r"\s+", " ", text)))
    if not match:
        raise SystemExit("FAIL: the 'nineteen states' sentence was not found — NAIC's page changed. "
                         "Update LIST_RE in derive_deductibles.py.")
    as_of, names = match.groups()
    states = [html.unescape(n.strip().rstrip(".")) for n in re.split(r",| and ", names) if n.strip()]
    states.append("District of Columbia")  # the sentence structure names it separately, not in the list
    unknown = [s for s in states if s not in STATES.values()]
    if unknown:
        raise SystemExit(f"FAIL: NAIC named states this script doesn't recognise: {unknown}")
    return as_of.strip(), set(states)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="re-fetch the NAIC page")
    args = parser.parse_args()

    page = cached(args.refresh)
    as_of, listed = parse(page)

    verdict, _, why = verify_urls.check(SOURCE)
    print(f"source check: {verdict} ({why})")
    if verdict == DEAD:
        raise SystemExit("FAIL: the NAIC page itself now answers dead — find a replacement source.")

    rows = []
    for abbr, state in STATES.items():
        if state in listed:
            note = (f"NAIC lists {state} among the 19 states plus DC with a separate hurricane or "
                     f"named-storm deductible in homeowner policies as of {as_of} "
                     f"(content.naic.org/insurance-topics/hurricane-deductibles).")
        else:
            note = (f"NAIC's {as_of} hurricane-deductible list does not name {state}; NAIC notes "
                     "other states may still allow insurers to include one, and a separate "
                     "wind/hail deductible can appear in any state's policy regardless "
                     "(content.naic.org/insurance-topics/hurricane-deductibles).")
        rows.append({"state": state, "abbr": abbr, "wind_deductible_note": note})

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {OUT}  ({len(rows)} rows, {len(listed)} on NAIC's named-deductible list)")


if __name__ == "__main__":
    main()
