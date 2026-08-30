import json

with open("vid.info.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print("TITLE:", d.get("title"))
print("CHANNEL:", d.get("channel") or d.get("uploader"))
print("UPLOAD_DATE:", d.get("upload_date"))
print("DURATION:", d.get("duration"), d.get("duration_string"))
print("VIEWS:", d.get("view_count"))
print("LIKES:", d.get("like_count"))
print()
print("DESCRIPTION (first 1500):")
print((d.get("description") or "")[:1500])
print()
chapters = d.get("chapters")
print("CHAPTERS:", chapters if chapters else "None")
print()

comments = d.get("comments") or []
comments_sorted = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
print("TOP 30 COMMENTS BY LIKES:")
for c in comments_sorted[:30]:
    text = (c.get("text") or "").replace("\n", " ")
    print(f"[{c.get('like_count')}] {text}")
