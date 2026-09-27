"""Paste the shared basemap (basemap.json) into every g-master-map comp between its markers.
`<!--BASEMAP:<id>-->...<!--/BASEMAP-->` gets the local layers with ids prefixed by <id>;
`<!--REGIONAL-->...<!--/REGIONAL-->` gets the state outlines + 49th parallel. Re-runnable."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.join(HERE, "..", "..", "compositions")
bm = json.load(open(os.path.join(HERE, "basemap.json")))
for fn in sorted(os.listdir(COMP)):
    if not fn.startswith("g-master-map") or not fn.endswith(".html"):
        continue
    p = os.path.join(COMP, fn); s = open(p, encoding="utf-8").read()
    n0 = s
    s = re.sub(r"<!--BASEMAP:([\w-]+)-->.*?<!--/BASEMAP-->",
               lambda m: "<!--BASEMAP:%s-->%s<!--/BASEMAP-->" % (m.group(1), bm["svg"].replace("{P}", m.group(1))), s, flags=re.S)
    s = re.sub(r"<!--REGIONAL-->.*?<!--/REGIONAL-->", lambda m: "<!--REGIONAL-->%s<!--/REGIONAL-->" % bm["regional_svg"], s, flags=re.S)
    if s != n0:
        open(p, "w", encoding="utf-8", newline="\n").write(s); print("injected", fn)
