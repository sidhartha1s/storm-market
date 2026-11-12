"""List an Instagram account's reels (shortcode, views, date) by reading the Reels tab in the
logged-in browser session through opencli. Usage: python3 ig_list.py <out_dir> <handle> [handle...]
Date comes from the shortcode itself (media id >> 23 + Instagram epoch), so no per-reel request."""
import os, json, subprocess, sys, time, datetime, shutil

S = "igstudy"
OPENCLI = shutil.which("opencli") or "opencli"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
CUTOFF_DAYS = 45
SHOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ig_tmp.png")
JS = ("JSON.stringify({head:(document.querySelector('header')||{innerText:''}).innerText.slice(0,400),"
      "rows:[...document.querySelectorAll('main a[href]')].map(a=>[a.getAttribute('href'),a.innerText.replace(/\\n/g,' ')])"
      ".filter(x=>/\\/reel\\//.test(x[0]))})")


def oc(*args):
    r = subprocess.run([OPENCLI, "browser", "--session", S, *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=120, shell=False)
    line = next((l for l in r.stdout.splitlines() if l.startswith("{")), "{}")
    return json.loads(line)


def code_date(code):
    n = 0
    for c in code[:11]:
        n = n * 64 + ALPHA.index(c)
    return datetime.datetime.fromtimestamp(((n >> 23) + 1314220021721) / 1000, datetime.timezone.utc)


def num(s):
    s = s.strip().replace(",", "")
    if not s:
        return None
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(s[-1].upper())
    try:
        return int(float(s[:-1]) * mult) if mult else int(float(s))
    except ValueError:
        return None


def list_account(handle):
    oc("--window", "background", "open", f"https://www.instagram.com/{handle}/reels/")
    time.sleep(5)
    oc("screenshot", SHOT)  # a hidden tab does not load the grid; a screenshot forces a render
    time.sleep(2)
    seen, head, stale = {}, "", 0
    now = datetime.datetime.now(datetime.timezone.utc)
    for _ in range(45):
        d = oc("eval", JS)
        if not d.get("ok"):
            break
        data = json.loads(d["data"])
        head = head or data["head"]
        before = len(seen)
        for href, txt in data["rows"]:
            code = href.rstrip("/").split("/")[-1]
            seen.setdefault(code, txt)
        stale = stale + 1 if len(seen) == before else 0
        dates = [code_date(c) for c in seen]
        # pinned reels sit first and can be old, so stop only once several are past the cutoff
        if sum((now - x).days > CUTOFF_DAYS for x in dates) >= 6 or stale >= 4:
            break
        oc("eval", "window.scrollTo(0, document.body.scrollHeight); 1")
        oc("screenshot", SHOT)
        time.sleep(2)
    rows = [{"code": c, "views": num(t), "date": code_date(c).strftime("%Y-%m-%d"),
             "age_days": (now - code_date(c)).days} for c, t in seen.items()]
    return {"handle": handle, "header": head, "reels": rows}


if __name__ == "__main__":
    # self-check: a known shortcode decodes to a sane year
    assert 2010 < code_date("DZU1D_8OI62").year < 2030
    out = sys.argv[1]
    for h in sys.argv[2:]:
        res = list_account(h)
        json.dump(res, open(f"{out}/ig_{h}.json", "w", encoding="utf-8"), indent=1)
        recent = [r for r in res["reels"] if r["age_days"] <= CUTOFF_DAYS]
        print(h, "| reels seen", len(res["reels"]), "| last 45d", len(recent), "|",
              res["header"].replace("\n", " ")[:90], flush=True)
        time.sleep(4)
