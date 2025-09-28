import os
import json
from googleapiclient.discovery import build

# 🔑 Ambil API key dari environment variable
API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("❌ API Key tidak ditemukan. Set YOUTUBE_API_KEY di environment.")

# Setup client YouTube
youtube = build("youtube", "v3", developerKey=API_KEY)

# Query pencarian (bisa diubah sesuai kebutuhan)
query = "korupsi"

# Request ke YouTube API
request = youtube.search().list(
    q=query,
    part="snippet",
    maxResults=5,
    type="video"
)
response = request.execute()

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

# Simpan hasil ke file JSON
output_file = "data/youtube.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(response["items"], f, ensure_ascii=False, indent=2)

print(f"✅ {len(response['items'])} video disimpan ke {output_file}")

# Bonus: tampilkan judul video
for item in response["items"]:
    title = item["snippet"]["title"]
    vid = item["id"]["videoId"]
    print(f"- {title} → https://youtube.com/watch?v={vid}")
