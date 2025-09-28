import os, json
from googleapiclient.discovery import build

API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)

query = "korupsi"
request = youtube.search().list(q=query, part="snippet", maxResults=5, type="video")
response = request.execute()

videos = []
for item in response["items"]:
    vid = item["id"]["videoId"]
    videos.append({
        "title": item["snippet"]["title"],
        "videoId": vid,
        "url": f"https://youtube.com/watch?v={vid}",
    })

os.makedirs("data", exist_ok=True)
with open("data/youtube.json", "w", encoding="utf-8") as f:
    json.dump(videos, f, indent=2, ensure_ascii=False)

print(f"✅ {len(videos)} video disimpan ke data/youtube.json")
