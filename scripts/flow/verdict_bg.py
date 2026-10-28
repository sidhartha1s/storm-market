# Check one saved clip after the driver has exited and append the verdict line to the job's drv.log.
# usage: verdict_bg.py <jobs.json> <clip.mp4> <drv.log>
# Why: on a loaded ASUS (about 4 GB free) the verdict took 7 min on Galveston clip 1 (29 Oct 26) and the runner could
# not send the next clip until it ended. The verdict needs no browser, so ad_gen starts this and exits.
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jobcheck import clip_verdict

jobs, clip, drv = sys.argv[1:4]
try:
    line = clip_verdict(clip, json.load(open(jobs, encoding="utf8")), jobs)
except Exception as e:  # a crashed check is reported as unchecked, never as a pass
    line = ("UNVERIFIED", clip, "verdict crashed: " + repr(e)[:300])
with open(drv, "a", encoding="utf8") as f:
    f.write(" ".join(str(x) for x in line) + "\n")
