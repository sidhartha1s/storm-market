#!/usr/bin/env python3
"""Derive energy_assist_url and its public inquiry line for every state from one federal page.

The Administration for Children and Families publishes a single LIHEAP state and
territory contact listing covering all 50 states and DC. That is one primary federal
source instead of 51 state lookups, and it carries the field the reader actually needs:
the *public inquiry* number, not the program officer's desk line.

Two rules from the appendix README are enforced here rather than trusted:

  - Appendix B only publishes https:// URLs, and the ACF listing carries bare domains and
    http:// links. Each one is normalised to https:// and then checked through
    verify_urls.check. A URL the host merely refuses us is still published, because the
    citation is the federal listing; only a 404 or an unresolvable hostname is dropped, since
    that means the listing has gone stale for that state.
  - A phone number is only published if it parses as a complete US number. The upstream
    page has at least one truncated entry, and a truncated phone number in an emergency
    directory is worse than an empty cell.

Usage:
    python3 derive_energy.py            # writes energy.csv, verifying every URL
    python3 derive_energy.py --no-verify   # skip the network check (offline iteration)
"""

import argparse
import csv
import re
import sys
from pathlib import Path

import verify_urls
from verify_urls import BLOCKED, DEAD

HERE = Path(__file__).parent
OUT = HERE / "energy.csv"

SOURCE = ("https://www.acf.hhs.gov/ocs/map/"
          "liheap-map-state-and-territory-contact-listing")

STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
    "Wyoming",
]

# Three forms are complete enough to publish, in priority order:
#   1-800-464-HELP (4357)   vanity number WITH its digit expansion — printed as published,
#                           because that is how the state answers the phone
#   1-800-392-8098          plain ten- or eleven-digit number
#   2-1-1                   the state routes energy assistance through the 211 line
# Deliberately NOT matched: "1-877-411-WARM" with no digits after it, which is how the
# upstream page truncates some entries. An incomplete number in an emergency directory is
# worse than an empty cell, so it is dropped and reported rather than guessed at.
PHONE_RE = re.compile(
    r"(?:1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?[A-Z]{4}\s*\(\d{4}\)"
    r"|(?:1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    r"|\b2-1-1\b"
)


def page_text():
    raw = verify_urls.fetch(SOURCE, timeout=120).decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = raw.replace("&amp;", "&").replace("&nbsp;", " ").replace("&#39;", "'")
    return re.sub(r"[ \t]+", " ", raw)


def blocks(text):
    """Split the contact listing into one block per state, in page order."""
    start = text.find("State Data")
    if start < 0:
        sys.exit("FAIL: 'State Data' heading not found — the ACF page layout changed.")
    text = text[start:]
    found = []
    for state in STATES:
        at = text.find("\n " + state + " \n")
        if at < 0:
            at = text.find(state)
        if at >= 0:
            found.append((state, at))
    if len(found) < len(STATES):
        missing = sorted(set(STATES) - {s for s, _ in found})
        sys.exit(f"FAIL: no block found for {missing} — the ACF page layout changed.")
    found.sort(key=lambda pair: pair[1])
    out = {}
    for i, (state, at) in enumerate(found):
        end = found[i + 1][1] if i + 1 < len(found) else len(text)
        out[state] = text[at:end]
    return out


def normalise(url):
    url = url.strip().rstrip(">").rstrip(".,;")
    if not url:
        return ""
    url = re.sub(r"^http://", "https://", url)
    if not url.startswith("https://"):
        url = "https://" + url.lstrip("/")
    return url


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-verify", action="store_true",
                        help="skip the live URL check (offline iteration only)")
    args = parser.parse_args()

    per_state = blocks(page_text())

    rows, dropped_urls, dropped_phones, blocked_urls, checks = [], [], [], [], []
    for state in STATES:
        block = per_state[state]

        url = ""
        match = re.search(r"WEB SITE:\s*(\S+)", block)
        if match:
            url = normalise(match.group(1))
            if url and not args.no_verify:
                verdict, _, why = verify_urls.check(url)
                checks.append(verdict)
                if verdict == DEAD:
                    dropped_urls.append((state, url, why))
                    url = ""
                elif verdict == BLOCKED:
                    blocked_urls.append((state, url, why))

        phone = ""
        match = re.search(r"PUBLIC INQUIRIES:\s*([^\n]{0,40})", block)
        if match:
            found = PHONE_RE.search(match.group(1))
            if found:
                phone = found.group(0).strip()
            else:
                dropped_phones.append((state, match.group(1).strip()[:24]))

        rows.append({
            "state": state,
            "energy_assist_url": url,
            "energy_assist_url_src": SOURCE if url else "",
            "energy_assist_phone": phone,
            "energy_assist_phone_src": SOURCE if phone else "",
        })

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    filled = sum(1 for r in rows if r["energy_assist_url"])
    print(f"wrote {OUT}  ({filled}/{len(rows)} rows carry an https URL)")
    if checks:
        print(f"  checks: {verify_urls.summarise(checks)}")
    if blocked_urls:
        print(f"\n{len(blocked_urls)} URL(s) published on the federal listing's word "
              "(the host refused us, but never said the page is gone):")
        for state, url, why in blocked_urls:
            print(f"  {state}: {url}  [{why}]")
    if dropped_urls:
        print(f"\n{len(dropped_urls)} URL(s) dropped as gone:")
        for state, url, why in dropped_urls:
            print(f"  {state}: {url}  [{why}]")
    if dropped_phones:
        print(f"\n{len(dropped_phones)} phone number(s) left blank as incomplete upstream:")
        for state, text in dropped_phones:
            print(f"  {state}: {text!r}")
    print(f"\nSource: {SOURCE}")


if __name__ == "__main__":
    main()
