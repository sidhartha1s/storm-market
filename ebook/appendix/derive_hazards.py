#!/usr/bin/env python3
"""Derive hazard_1..3, season_1..3 and region_overlay for every state from NCEI Storm Events.

Why this exists rather than a judgement call per state: the obvious source for
"what are this state's top three hazards" is NOAA's billion-dollar disaster list, and
it is the wrong source. That list ranks property loss, it folds tornado, hail and
straight-line wind into one "severe storm" category, and it has no heat category at all
(heat is folded into drought). Ranking a household directory that way would bury the
hazard that kills the most Americans in most states.

So this ranks by direct deaths, per state, from the NCEI Storm Events database — the
same records the National Weather Service compiles Storm Data from. 2010-2025 inclusive;
the current year is excluded because it is partial.

Every NWS event type that recorded a direct death is either mapped to one of the book's
sixteen Part Three playbooks or explicitly excluded, and the script fails if a new event
type appears unmapped, so a NOAA schema change cannot silently drop deaths.

Usage:
    python3 derive_hazards.py --fetch      # download the yearly gzipped CSVs (~180 MB)
    python3 derive_hazards.py              # compute from the cache, write hazards.csv
"""

import argparse
import collections
import csv
import gzip
import os
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / ".storm-events-cache"
OUT = HERE / "hazards.csv"

BASE = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
FIRST_YEAR, LAST_YEAR = 2010, 2025

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126 Safari/537.36"}

# NWS event type -> Part Three playbook name. These names must match build.py's
# PLAYBOOKS dict exactly, so the packet can say "see Playbook 7" and be right.
PLAYBOOK = {
    "Excessive Heat": "Extreme heat",
    "Heat": "Extreme heat",
    "Tornado": "Tornado",
    "Funnel Cloud": "Tornado",
    "Flash Flood": "Extreme rainfall and flash flood",
    "Debris Flow": "Extreme rainfall and flash flood",
    "Heavy Rain": "Extreme rainfall and flash flood",
    "Flood": "Riverine and coastal flooding",
    "Coastal Flood": "Riverine and coastal flooding",
    "Lakeshore Flood": "Riverine and coastal flooding",
    "Thunderstorm Wind": "Hail and derecho",
    "Hail": "Hail and derecho",
    "High Wind": "Hail and derecho",
    "Strong Wind": "Hail and derecho",
    "Marine Thunderstorm Wind": "Hail and derecho",
    "Marine Strong Wind": "Hail and derecho",
    "Marine High Wind": "Hail and derecho",
    "Wildfire": "Wildfire",
    "Dense Smoke": "Wildfire smoke",
    "Cold/Wind Chill": "Extreme cold",
    "Extreme Cold/Wind Chill": "Extreme cold",
    "Frost/Freeze": "Extreme cold",
    "Lightning": "Lightning",
    "Hurricane": "Hurricane and storm surge",
    "Hurricane (Typhoon)": "Hurricane and storm surge",
    "Tropical Storm": "Hurricane and storm surge",
    "Tropical Depression": "Hurricane and storm surge",
    "Storm Surge/Tide": "Hurricane and storm surge",
    "Winter Weather": "Blizzard and ice storm",
    "Winter Storm": "Blizzard and ice storm",
    "Blizzard": "Blizzard and ice storm",
    "Ice Storm": "Blizzard and ice storm",
    "Heavy Snow": "Blizzard and ice storm",
    "Sleet": "Blizzard and ice storm",
    "Lake-Effect Snow": "Blizzard and ice storm",
    "Tsunami": "Tsunami",
    "Volcanic Ash": "Volcanic ashfall",
    "Volcanic Ashfall": "Volcanic ashfall",
    "Dust Storm": "Drought and dust",
    "Dust Devil": "Drought and dust",
    "Drought": "Drought and dust",
}

# Real deaths, deliberately outside the scope of this book. Rip currents alone killed
# 911 people over the window, which is more than wildfire — the book does not cover
# beach and open-water hazards, and a directory that silently reranked them into a
# household playbook would be lying about what the reader is being handed.
EXCLUDED = {
    "Rip Current", "High Surf", "Sneakerwave", "Seiche", "Astronomical Low Tide",
    "Avalanche", "Dense Fog", "Freezing Fog", "Marine Dense Fog",
    "Waterspout", "Marine Hail", "Marine Lightning",
}

STATES = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "District of Columbia": "DC",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
    "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI",
    "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
    "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND",
    "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
    "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN",
    "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
    "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}

# region_overlay is the one judgement column, so it is made by rule rather than by feel.
# A state gets a region if its death ranking earns it, or if it sits in the region's
# accepted geographic footprint — because a region in this book sets the *order* of the
# first ten protections, and under-assigning is the harmful direction.
QUAKE_WEST = {"CA", "WA", "OR", "AK", "NV", "UT", "ID", "MT", "WY", "HI"}
ICE_SNOW_NORTH = {"ME", "NH", "VT", "MA", "RI", "CT", "NY", "PA", "MI", "WI", "MN",
                  "IA", "ND", "SD", "NE", "MT", "WY", "CO", "ID", "AK", "OH", "IN", "IL",
                  "NJ", "WV", "MD", "DC", "UT", "KS", "MO"}
HURRICANE_COAST = {"TX", "LA", "MS", "AL", "FL", "GA", "SC", "NC", "VA", "MD", "DE",
                   "DC", "NJ", "NY", "CT", "RI", "MA", "NH", "ME", "HI"}
TORNADO_ALLEY = {"TX", "OK", "KS", "NE", "SD", "IA", "MO", "AR", "LA", "MS", "AL",
                 "TN", "KY", "IL", "IN", "OH", "GA", "MN", "CO", "WI", "MI"}
WILDFIRE_WEST = {"CA", "OR", "WA", "ID", "MT", "WY", "NV", "UT", "CO", "AZ", "NM",
                 "TX", "OK", "KS", "NE", "SD", "ND", "AK", "HI"}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def file_list():
    with urllib.request.urlopen(urllib.request.Request(BASE, headers=UA), timeout=120) as fh:
        index = fh.read().decode("utf-8", "replace")
    wanted = {}
    for name in re.findall(r"StormEvents_details-ftp_v1\.0_d(\d{4})_c\d+\.csv\.gz", index):
        pass
    for name in re.findall(r"StormEvents_details-ftp_v1\.0_d\d{4}_c\d+\.csv\.gz", index):
        year = int(re.search(r"_d(\d{4})_", name).group(1))
        if FIRST_YEAR <= year <= LAST_YEAR:
            wanted[year] = name          # last revision wins
    missing = sorted(set(range(FIRST_YEAR, LAST_YEAR + 1)) - set(wanted))
    if missing:
        sys.exit(f"FAIL: no details file published for {missing}")
    return [wanted[y] for y in sorted(wanted)]


def fetch():
    CACHE.mkdir(exist_ok=True)
    for name in file_list():
        target = CACHE / name
        if target.exists() and target.stat().st_size > 100_000:
            print(f"cached  {name}")
            continue
        with urllib.request.urlopen(urllib.request.Request(BASE + name, headers=UA), timeout=300) as fh:
            data = fh.read()
        target.write_bytes(data)
        print(f"fetched {name}  {len(data):,} bytes")


def compute():
    files = sorted(CACHE.glob("StormEvents_details-ftp_v1.0_d*.csv.gz"))
    if not files:
        sys.exit("FAIL: no cached Storm Events files. Run with --fetch first.")

    deaths = collections.defaultdict(collections.Counter)
    months = collections.defaultdict(collections.Counter)
    unmapped = collections.Counter()

    for path in files:
        year = int(re.search(r"_d(\d{4})_", path.name).group(1))
        if not (FIRST_YEAR <= year <= LAST_YEAR):
            continue
        with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh):
                try:
                    dead = int(row.get("DEATHS_DIRECT") or 0)
                except ValueError:
                    dead = 0
                if dead <= 0:
                    continue
                # NCEI stores "DISTRICT OF COLUMBIA"; .title() would give "Of", which then
                # fails to join against every other fragment's "District of Columbia".
                state = (row.get("STATE") or "").strip().title().replace(" Of ", " of ")
                event = (row.get("EVENT_TYPE") or "").strip()
                if state not in STATES or not event:
                    continue          # marine zones and territories are out of scope
                if event in EXCLUDED:
                    continue
                playbook = PLAYBOOK.get(event)
                if playbook is None:
                    unmapped[event] += dead
                    continue
                deaths[state][playbook] += dead
                yearmonth = row.get("BEGIN_YEARMONTH") or ""
                if len(yearmonth) == 6:
                    months[(state, playbook)][int(yearmonth[4:6])] += dead

    if unmapped:
        sys.exit("FAIL: NWS event types recorded deaths but are neither mapped to a playbook "
                 "nor explicitly excluded. Add them to PLAYBOOK or EXCLUDED and say why:\n  "
                 + "\n  ".join(f"{v:6} {k}" for k, v in unmapped.most_common()))

    return deaths, months


def season(counter):
    """The tightest contiguous run of months holding at least 70% of the deaths."""
    if not counter:
        return ""
    total = sum(counter.values())
    by_month = [counter.get(m, 0) for m in range(1, 13)]
    best = None
    for length in range(1, 13):
        for start in range(12):
            window = sum(by_month[(start + k) % 12] for k in range(length))
            if window / total >= 0.70:
                if best is None or length < best[0]:
                    best = (length, start)
                break
        if best:
            break
    if not best:
        return "year round"
    length, start = best
    if length >= 11:
        return "year round"
    first = MONTHS[start]
    last = MONTHS[(start + length - 1) % 12]
    return first if length == 1 else f"{first}–{last}"


def regions(abbr, top):
    """Geographic footprint only.

    An earlier version also assigned a region when the death ranking named its
    signature hazard, which put Arizona in Ice & Snow North on the strength of its
    cold-exposure deaths. The five regions are geographic constructs that set the
    *order* of the first ten protections; the finer instrument is hazard_1..3, which
    is per state and points at the playbook directly. So the hazards do the hazard
    work and the regions stay geographic.
    """
    out = []
    if abbr in TORNADO_ALLEY:
        out.append("Tornado Alley")
    if abbr in HURRICANE_COAST:
        out.append("Hurricane Coast")
    if abbr in WILDFIRE_WEST:
        out.append("Wildfire West")
    if abbr in ICE_SNOW_NORTH:
        out.append("Ice & Snow North")
    if abbr in QUAKE_WEST:
        out.append("Quake West")
    return "|".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="download the yearly CSVs first")
    args = parser.parse_args()

    if args.fetch:
        fetch()

    deaths, months = compute()

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["state", "abbr", "hazard_1", "hazard_2", "hazard_3",
                         "season_1", "season_2", "season_3", "region_overlay",
                         "deaths_1", "deaths_2", "deaths_3", "deaths_total"])
        for state, abbr in sorted(STATES.items()):
            top = deaths[state].most_common(3)
            hazards = [h for h, _ in top] + [""] * (3 - len(top))
            counts = [str(n) for _, n in top] + [""] * (3 - len(top))
            seasons = [season(months.get((state, h), collections.Counter())) if h else ""
                       for h in hazards]
            writer.writerow([state, abbr, *hazards, *seasons, regions(abbr, top),
                             *counts, sum(deaths[state].values())])

    print(f"wrote {OUT}  ({len(STATES)} rows, direct deaths {FIRST_YEAR}–{LAST_YEAR})")
    print("Source: NOAA NCEI Storm Events Database, details files, "
          f"{BASE}")


if __name__ == "__main__":
    main()
