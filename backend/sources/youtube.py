import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(query):
"""
Search YouTube videos using the YouTube Data API.
Returns a list of search results compatible with Voyager.
"""

if not YOUTUBE_API_KEY:
    print("YouTube API key not found.")
    return []

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

    response.raise_for_status()

    data = response.json()

    results = []

    for item in data.get("items", []):

        video_id = (
            item.get("id", {})
            .get("videoId")
        )

        if not video_id:
            continue

        snippet = item.get("snippet", {})

        results.append({
            "source": "YouTube",
            "title": snippet.get("title", "Untitled Video"),
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
            "snippet": snippet.get("description", "")
        })

    print(
        f"YouTube returned {len(results)} results for '{query}'"
    )

    return results

except requests.exceptions.Timeout:
    print("YouTube API request timed out.")
    return []

except requests.exceptions.RequestException as e:
    print(f"YouTube API request failed: {e}")
    return []

except Exception as e:
    print(f"YouTube search error: {e}")
    return []
