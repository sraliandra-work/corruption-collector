import snscrape.modules.twitter as sntwitter
import json, os

KEYWORDS = ["korupsi", "suap", "gratifikasi", "KPK"]
MAX_TWEETS = 50

tweets = []
for kw in KEYWORDS:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{kw} since:2023-01-01').get_items()):
        if i >= MAX_TWEETS:
            break
        tweets.append({
            "date": tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
            "user": tweet.user.username,
            "content": tweet.content,
            "url": tweet.url,
        })

os.makedirs("data", exist_ok=True)
with open("data/twitter.json", "w", encoding="utf-8") as f:
    json.dump(tweets, f, indent=2, ensure_ascii=False)

print(f"✅ {len(tweets)} tweet disimpan ke data/twitter.json")
