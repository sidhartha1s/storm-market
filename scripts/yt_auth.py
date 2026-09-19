#!/usr/bin/env python3
"""One-time YouTube Analytics consent for The Warning Hour (sidclashes2much@gmail.com).
Prints a consent link, waits on localhost:8977 with no timeout, saves the refresh token to
~/.claude/google-credentials/tokens/youtube-warning-hour.json. Reuse: scripts/yt_stats.py."""
import json, os, secrets, sys, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

CRED = os.path.expanduser("~/.claude/google-credentials")
client = json.load(open(f"{CRED}/client_secret.json"))["installed"]
OUT = f"{CRED}/tokens/youtube-warning-hour.json"
SCOPES = "https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/youtube.readonly"
PORT = 8977
state = secrets.token_urlsafe(16)
url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
    "client_id": client["client_id"], "redirect_uri": f"http://localhost:{PORT}/", "response_type": "code",
    "scope": SCOPES, "access_type": "offline", "prompt": "consent", "state": state})
print("CONSENT URL:", url, flush=True)

got = {}
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        ok = q.get("state", [""])[0] == state and "code" in q
        self.send_response(200); self.end_headers()
        self.wfile.write(b"Done, you can close this tab." if ok else b"Bad state or no code; tell Claude.")
        if ok: got["code"] = q["code"][0]
    def log_message(self, *a): pass

srv = HTTPServer(("localhost", PORT), H)
while "code" not in got: srv.handle_request()
body = urllib.parse.urlencode({"code": got["code"], "client_id": client["client_id"], "client_secret": client["client_secret"],
                               "redirect_uri": f"http://localhost:{PORT}/", "grant_type": "authorization_code"}).encode()
tok = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", body)))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({"client_id": client["client_id"], "client_secret": client["client_secret"], "refresh_token": tok["refresh_token"]}, open(OUT, "w"))
print("SAVED", OUT, flush=True)
