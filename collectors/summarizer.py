import json, os
from datetime import datetime

DATA_DIR = "data"

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return []

# Load semua data
news = load_json("news.json")
twitter = load_json("twitter.json")
youtube = load_json("youtube.json")
reddit = load_json("reddit.json")

summary_lines = []
today = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

summary_lines.append(f"# 📰 Laporan Update Korupsi\n")
summary_lines.append(f"Terakhir diperbarui: **{today}**\n")

# Ringkas berita
summary_lines.append("## 📌 Berita")
if news:
    for item in news[:5]:
        summary_lines.append(f"- [{item['title']}]({item['link']}) ({item['source']})")
else:
    summary_lines.append("- Tidak ada data berita.")

# Ringkas Twitter
summary_lines.append("\n## 🐦 Twitter")
if twitter:
    for t in twitter[:5]:
        summary_lines.append(f"- @{t['user']}: {t['content'][:100]}... [Lihat]({t['url']})")
else:
    summary_lines.append("- Tidak ada data tweet.")

# Ringkas YouTube
summary_lines.append("\n## ▶️ YouTube")
if youtube:
    for v in youtube[:5]:
        summary_lines.append(f"- {v['title']} [Link]({v['url']})")
else:
    summary_lines.append("- Tidak ada data video.")

# Ringkas Reddit
summary_lines.append("\n## 👥 Reddit")
if reddit:
    for r in reddit[:5]:
        summary_lines.append(f"- ({r['subreddit']}) {r['title']} [Link]({r['url']})")
else:
    summary_lines.append("- Tidak ada data reddit.")

# Simpan ke file Markdown
os.makedirs(DATA_DIR, exist_ok=True)
with open(os.path.join(DATA_DIR, "summary.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines))

print("✅ Summary saved to data/summary.md")
