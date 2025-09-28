import praw, os, json

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

subreddits = ["worldnews", "Indonesia", "politics"]
posts = []

for sub in subreddits:
    for post in reddit.subreddit(sub).search("corruption", limit=10):
        posts.append({
            "subreddit": sub,
            "title": post.title,
            "url": post.url,
            "score": post.score,
        })

os.makedirs("data", exist_ok=True)
with open("data/reddit.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=2, ensure_ascii=False)

print(f"✅ {len(posts)} postingan disimpan ke data/reddit.json")
