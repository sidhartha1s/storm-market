"""Download an account's best (and optionally worst) reels of the last 45 days.
Usage: python3 pull.py <dir> <handle> <top_n> <bottom_n> [latest]   ('latest' = newest top_n, ignoring views)
Reads <dir>/ig_<handle>.json (from ig_list.py); writes <dir>/media/<handle>/<code>.mp4 + .info.json and picks.json."""
import json, subprocess, sys, time, os, statistics, shutil, glob

d, h, top, bottom = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
latest = len(sys.argv) > 5
acc = json.load(open(f"{d}/ig_{h}.json", encoding="utf-8"))
recent = [r for r in acc["reels"] if r["age_days"] <= 45 and r["views"]]
if latest:
    picks = sorted(recent, key=lambda r: r["age_days"])[:top]
else:
    # reels under 3 days old have not finished collecting views; keep them out of the worst list
    ranked = sorted(recent, key=lambda r: -r["views"])
    settled = [r for r in ranked if r["age_days"] >= 3]
    picks = ranked[:top] + [r for r in settled[::-1][:bottom] if r not in ranked[:top]]
med = statistics.median([r["views"] for r in recent]) if recent else 0
out = f"{d}/media/{h}"
os.makedirs(out, exist_ok=True)
for r in picks:
    r["x_median"] = round(r["views"] / med, 2) if med else None
    if not os.path.exists(f"{out}/{r['code']}.mp4"):
        subprocess.run(["yt-dlp", "-q", "--no-warnings", "--write-info-json", "-o", f"{out}/%(id)s.%(ext)s",
                        f"https://www.instagram.com/reel/{r['code']}/"], timeout=300, stderr=subprocess.DEVNULL)
        time.sleep(3)
    if not os.path.exists(f"{out}/{r['code']}.mp4"):
        # fallback: the no-login route is refused for some reels; fetch through the logged-in browser tab
        print("[FALLBACK] browser download", r["code"], flush=True)
        subprocess.run([shutil.which("opencli"), "instagram", "download", f"https://www.instagram.com/reel/{r['code']}/",
                        "--path", out, "--window", "background"], capture_output=True, timeout=300)
        got = glob.glob(f"{out}/{r['code']}/*.mp4")
        if got:
            shutil.move(got[0], f"{out}/{r['code']}.mp4")
        time.sleep(4)
    r["ok"] = os.path.exists(f"{out}/{r['code']}.mp4")
json.dump({"handle": h, "header": acc["header"], "recent_n": len(recent), "median_views": med, "picks": picks},
          open(f"{out}/picks.json", "w", encoding="utf-8"), indent=1)
print(h, "| recent", len(recent), "| median", med, "| picked", len(picks), "| downloaded", sum(r["ok"] for r in picks), flush=True)
