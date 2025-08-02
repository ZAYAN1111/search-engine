import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": YOUTUBE_API_KEY,
        "part": "snippet",
        "q": query,
        "maxResults": 5,
        "type": "video"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return [
            {
                "source": "YouTube",
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "snippet": item["snippet"].get("description", "")
            }
            for item in data.get("items", [])
        ]
    except Exception as e:
        print(f"YouTube search error: {e}")
        return []
