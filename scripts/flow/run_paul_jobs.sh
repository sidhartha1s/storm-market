#!/bin/bash
# Run the Flow driver over a list of Paul job folders, one at a time (the driver refuses to run beside another).
# usage: bash scripts/flow/run_paul_jobs.sh <job dir> [<job dir> ...]   (each holds jobs.json; log lands beside it)
# Each job spends only what its jobs.json budget allows and only on Flow's exact credit quote (see ad_gen.py).
# A job the driver refuses for low free RAM (a render on the box) is retried every 60 s for up to 30 min, not skipped:
# on 23 Oct 26 nine jobs fell through in 15 s beside a render.
HERE="$(dirname "$(readlink -f "$0")")"
for d in "$@"; do
  for try in $(seq 1 31); do
    echo "== $(date +%H:%M:%S) start $d"
    PYTHONUNBUFFERED=1 python3 "$HERE/ad_gen.py" "$d/jobs.json" > "$d/drv.log" 2>&1
    last="$(tail -1 "$d/drv.log")"
    echo "== $(date +%H:%M:%S) exit $? $last"
    case "$last" in *"GB free, a Flow run needs"*) [ "$try" -lt 31 ] && sleep 60 && continue ;; esac
    break
  done
done
