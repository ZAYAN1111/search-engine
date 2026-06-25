import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(query):
try:
response = requests.get(
"https://www.googleapis.com/youtube/v3/search",
params={
"key": YOUTUBE_API_KEY,
"part": "snippet",
"q": query,
"maxResults": 10,
"type": "video"
},
timeout=10
)

```
    response.raise_for_status()

    data = response.json()

    results = []

    for item in data.get("items", []):

        video_id = item["id"]["videoId"]

        results.append({
            "source": "YouTube",
            "title": item["snippet"]["title"],
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
            "snippet": item["snippet"].get("description", "")
        })

    print(f"YouTube returned {len(results)} results for '{query}'")

    return results

except Exception as e:
    print(f"YouTube search error: {e}")
    return []
```
