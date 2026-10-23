#!/bin/bash
# Run the Flow driver over a list of Paul job folders, one at a time (the driver refuses to run beside another).
# usage: bash scripts/flow/run_paul_jobs.sh <job dir> [<job dir> ...]   (each holds jobs.json; log lands beside it)
# Each job spends only what its jobs.json budget allows and only on Flow's exact credit quote (see ad_gen.py).
HERE="$(dirname "$(readlink -f "$0")")"
for d in "$@"; do
  echo "== $(date +%H:%M:%S) start $d"
  PYTHONUNBUFFERED=1 python3 "$HERE/ad_gen.py" "$d/jobs.json" > "$d/drv.log" 2>&1
  echo "== $(date +%H:%M:%S) exit $? $(tail -1 "$d/drv.log")"
done
