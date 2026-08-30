import json, sys

with open("vid.info.json", encoding="utf-8") as f:
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
out["description_first1500"] = (d.get("description") or "")[:1500]
out["chapters"] = d.get("chapters")
out["tags"] = d.get("tags")
out["categories"] = d.get("categories")

comments = d.get("comments") or []
comments_sorted = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
top30 = [{"text": c.get("text"), "likes": c.get("like_count")} for c in comments_sorted[:30]]
out["top_comments"] = top30
out["total_comments_downloaded"] = len(comments)

with open("parsed_meta.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("done")
