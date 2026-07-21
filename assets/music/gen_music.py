#!/usr/bin/env python3
"""
Generate music beds via DeAPI ACE-Step. HARD MAX 10 paid calls total (tracked in
call_budget.json). Usage:
    python3 gen_music.py <key> <prompt> <duration> <outfile.mp3>
"""
import os, sys, json, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
BUDGET_FILE = os.path.join(ROOT, "call_budget.json")
MAX_CALLS = 10

ENV_PATH = os.path.join(ROOT, "..", "..", ".env")

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
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print("HTTP ERROR", e.code, e.read().decode())
        raise

def main():
    key_name, prompt, duration, outfile = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    env = load_env()
    api_key = env[key_name]

    budget = load_budget()
    if budget["calls_used"] >= MAX_CALLS:
        print(f"[BUDGET] HARD STOP: {budget['calls_used']}/{MAX_CALLS} calls used. Refusing to call API.")
        sys.exit(1)

    body = {
        "model": "AceStep_1_5_XL_Turbo_INT8",
        "prompt": prompt,
        "lyrics": "[Instrumental]",
        "duration": duration,
        "steps": 8,
        "guidance": 1,
    }

    print(f"[CALL {budget['calls_used']+1}/{MAX_CALLS}] Submitting job for {outfile} ...")
    resp = api_request("POST", "https://api.deapi.ai/api/v2/audio/music", api_key, body)
    budget["calls_used"] += 1
    budget["log"].append({"outfile": os.path.basename(outfile), "prompt": prompt, "duration": duration, "submit_resp": resp})
    save_budget(budget)

    job_id = resp.get("job_id") or resp.get("id") or resp.get("data", {}).get("job_id")
    if not job_id:
        print("Could not find job_id in response:", json.dumps(resp))
        sys.exit(1)
    print("job_id:", job_id)

    # Poll
    poll_url_candidates = [
        f"https://api.deapi.ai/api/v2/audio/music/{job_id}",
        f"https://api.deapi.ai/api/v2/jobs/{job_id}",
    ]
    result = None
    for attempt in range(120):
        time.sleep(5)
        for purl in poll_url_candidates:
            try:
                r = api_request("GET", purl, api_key)
            except Exception:
                continue
            status = r.get("status") or r.get("data", {}).get("status")
            if status:
                print(f"  poll {attempt}: status={status}")
                if status in ("completed", "success", "succeeded", "SUCCESS", "COMPLETED"):
                    result = r
                    break
        if result:
            break
    if not result:
        print("Timed out waiting for job completion")
        sys.exit(1)

    # find audio url
    def find_url(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str) and v.startswith("http") and (".mp3" in v or ".wav" in v):
                    return v
                found = find_url(v)
                if found:
                    return found
        elif isinstance(obj, list):
            for item in obj:
                found = find_url(item)
                if found:
                    return found
        return None

    audio_url = find_url(result)
    if not audio_url:
        print("Could not find audio URL in result:", json.dumps(result))
        sys.exit(1)
    print("audio_url:", audio_url)

    urllib.request.urlretrieve(audio_url, outfile)
    print("Saved:", outfile)

    # record request_id for provenance
    req_id = result.get("job_id") or result.get("id") or job_id
    print("REQUEST_ID:", req_id)

if __name__ == "__main__":
    main()
