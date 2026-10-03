#!/usr/bin/env python3
"""
Generate music beds via DeAPI ACE-Step. HARD MAX = MAX_CALLS paid calls total (tracked in
call_budget.json). Usage:
    python3 gen_music.py <key> <prompt> <duration> <outfile.mp3> [model]
model defaults to AceStep_1_5_XL_Turbo_INT8; the free tier caps each model at 3 jobs/day.
"""
import os, subprocess, sys, json, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
BUDGET_FILE = os.path.join(ROOT, "call_budget.json")
MAX_CALLS = 19  # +2 owner 2026-07-22 (aftermath-somber takes 3/4); +4 owner 2026-10-02 (El Reno mood set, "go for music"); +3 2026-10-03 replacing calls 12-14 (403 suspended key, nothing billed, balance unchanged)

# .env is gitignored, so it exists only in the main checkout; worktrees find it via git's common dir.
_GIT_COMMON = subprocess.run(["git", "-C", ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                             capture_output=True, text=True, check=True).stdout.strip()
ENV_PATH = os.path.join(os.path.dirname(_GIT_COMMON), ".env")

def load_env():
    env = {}
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env

def load_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE) as f:
            return json.load(f)
    return {"calls_used": 0, "log": []}

def save_budget(b):
    with open(BUDGET_FILE, "w") as f:
        json.dump(b, f, indent=2)

def api_request(method, url, api_key, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "Mozilla/5.0")  # Cloudflare blocks default urllib UA (403/1010)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print("HTTP ERROR", e.code, e.read().decode())
        raise

def main():
    key_name, caption, duration, outfile = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    model = sys.argv[5] if len(sys.argv) > 5 else "AceStep_1_5_XL_Turbo_INT8"
    if os.path.exists(outfile):
        sys.exit(f"[SKIP] {outfile} exists; no API call made")
    env = load_env()
    api_key = env[key_name]

    budget = load_budget()
    if budget["calls_used"] >= MAX_CALLS:
        print(f"[BUDGET] HARD STOP: {budget['calls_used']}/{MAX_CALLS} calls used. Refusing to call API.")
        sys.exit(1)

    # Verified request schema (2026-07-22, via 422 field-validation errors + live test call):
    # required fields are caption, lyrics, duration, inference_steps, guidance_scale, seed, format
    # ("prompt"/"steps"/"guidance" from the provenance.txt shorthand are NOT the real field names).
    body = {
        "model": model,
        "caption": caption,
        "lyrics": "[Instrumental]",
        "duration": duration,
        "inference_steps": 8,
        "guidance_scale": 1,
        "seed": int(time.time()) % 100000,
        "format": "mp3",
    }

    # Reserve the call BEFORE the HTTP request: a POST that raises may still have billed.
    budget["calls_used"] += 1
    entry = {"outfile": os.path.basename(outfile), "caption": caption, "duration": duration, "model": model}
    budget["log"].append(entry)
    save_budget(budget)
    print(f"[CALL {budget['calls_used']}/{MAX_CALLS}] Submitting job for {outfile} ...")
    resp = api_request("POST", "https://api.deapi.ai/api/v2/audio/music", api_key, body)
    entry["submit_resp"] = resp
    save_budget(budget)

    # POST returns {"data": {"request_id": "uuid"}}; poll GET /api/v2/jobs/{request_id}
    # (verified live: /api/v2/audio/music/{id} 404s, /api/v2/jobs/{id} is the real poll endpoint)
    data = resp.get("data", resp)
    request_id = data.get("request_id") or data.get("id")
    if not request_id:
        print("Could not find request_id in response:", json.dumps(resp))
        sys.exit(1)
    print("request_id:", request_id)

    poll_url = f"https://api.deapi.ai/api/v2/jobs/{request_id}"
    result = None
    for attempt in range(120):
        time.sleep(5)
        try:
            r = api_request("GET", poll_url, api_key)
        except Exception as e:
            print(f"  poll {attempt}: error {e}")
            continue
        rdata = r.get("data", r)
        status = rdata.get("status")
        print(f"  poll {attempt}: status={status} progress={rdata.get('progress')}")
        if status in ("done", "completed", "success", "succeeded"):
            result = rdata
            break
        if status in ("failed", "error"):
            print("Job failed:", json.dumps(r))
            sys.exit(1)
    if not result:
        print("Timed out waiting for job completion")
        sys.exit(1)

    audio_url = result.get("result_url") or result.get("result")
    if not audio_url:
        print("Could not find audio URL in result:", json.dumps(result))
        sys.exit(1)
    print("audio_url:", audio_url)

    urllib.request.urlretrieve(audio_url, outfile)
    print("Saved:", outfile)
    print("REQUEST_ID:", request_id)

if __name__ == "__main__":
    main()
