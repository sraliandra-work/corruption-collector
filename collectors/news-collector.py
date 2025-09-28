import feedparser, json, os
from datetime import datetime

FEEDS = [
    "https://rss.kompas.com/",
    "https://rss.detik.com/",
    "https://www.cnnindonesia.com/nasional/rss",
]

items = []
for url in FEEDS:
    feed = feedparser.parse(url)
    for e in feed.entries:
        if any(kw in e.title.lower() for kw in ["korupsi", "suap", "gratifikasi", "kpk"]):
            items.append({
                "source": url,
                "title": e.title,
                "link": e.link,
                "published": e.published if "published" in e else "",
            })

os.makedirs("data", exist_ok=True)
with open("data/news.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"✅ {len(items)} berita disimpan ke data/news.json")
