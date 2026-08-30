import json, sys

with open("vid.info.json", "r", encoding="utf-8") as f:
    d = json.load(f)

out = {}
out["title"] = d.get("title")
out["channel"] = d.get("channel") or d.get("uploader")
out["upload_date"] = d.get("upload_date")
out["duration"] = d.get("duration")
out["duration_string"] = d.get("duration_string")
out["view_count"] = d.get("view_count")
out["like_count"] = d.get("like_count")
out["comment_count"] = d.get("comment_count")
out["description"] = (d.get("description") or "")[:1500]
out["chapters"] = d.get("chapters")

comments = d.get("comments") or []
comments_sorted = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
top = []
for c in comments_sorted[:30]:
    top.append({"text": c.get("text"), "likes": c.get("like_count")})
out["top_comments"] = top

with open("info_summary.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("done")
print("title:", out["title"])
print("channel:", out["channel"])
print("duration:", out["duration_string"], out["duration"])
print("views:", out["view_count"], "likes:", out["like_count"], "comments:", out["comment_count"])
