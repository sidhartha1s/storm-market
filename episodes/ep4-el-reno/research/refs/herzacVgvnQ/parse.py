import json, sys

path = r"C:\Users\Sidhartha\Automation Projects\storm-market\episodes\ep4-el-reno\research\refs\herzacVgvnQ\vid.info.json"
with open(path, encoding="utf-8") as f:
    d = json.load(f)

out = []
out.append("TITLE: " + str(d.get("title")))
out.append("CHANNEL: " + str(d.get("channel") or d.get("uploader")))
out.append("UPLOAD_DATE: " + str(d.get("upload_date")))
out.append("DURATION_SEC: " + str(d.get("duration")))
out.append("VIEW_COUNT: " + str(d.get("view_count")))
out.append("LIKE_COUNT: " + str(d.get("like_count")))
out.append("COMMENT_COUNT: " + str(d.get("comment_count")))
out.append("\nDESCRIPTION (first 1500 chars):\n" + str(d.get("description",""))[:1500])

chapters = d.get("chapters")
out.append("\nCHAPTERS: " + (json.dumps(chapters, indent=1) if chapters else "None"))

tags = d.get("tags")
out.append("\nTAGS: " + str(tags[:20] if tags else None))

comments = d.get("comments") or []
comments_sorted = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
out.append(f"\nTOTAL COMMENTS FETCHED: {len(comments)}")
out.append("\nTOP 30 COMMENTS BY LIKES:")
for c in comments_sorted[:30]:
    text = (c.get("text") or "").replace("\n"," ")[:300]
    out.append(f"[{c.get('like_count')} likes] {text}")

with open(r"C:\Users\Sidhartha\Automation Projects\storm-market\episodes\ep4-el-reno\research\refs\herzacVgvnQ\parsed_summary.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("done")
