import json, sys

with open("vid.info.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print("TITLE:", d.get("title"))
print("CHANNEL:", d.get("channel") or d.get("uploader"))
print("UPLOAD_DATE:", d.get("upload_date"))
print("DURATION_S:", d.get("duration"))
print("VIEW_COUNT:", d.get("view_count"))
print("LIKE_COUNT:", d.get("like_count"))
print("COMMENT_COUNT:", d.get("comment_count"))
print()
print("DESCRIPTION (first 1500 chars):")
print((d.get("description") or "")[:1500])
print()
chapters = d.get("chapters")
print("CHAPTERS:", chapters if chapters else "None")
print()

comments = d.get("comments") or []
comments_sorted = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
print(f"TOTAL COMMENTS FETCHED: {len(comments)}")
print("TOP 30 COMMENTS BY LIKES:")
for c in comments_sorted[:30]:
    text = (c.get("text") or "").replace("\n", " ")
    print(f"[{c.get('like_count')} likes] {text}")
