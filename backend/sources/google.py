import os
import requests

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_google(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": 5
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return [
            {
                "source": "Google",
                "title": item["title"],
                "url": item["link"],
                "snippet": item.get("snippet", "")
            }
            for item in data.get("items", [])
        ]
    except Exception as e:
        print(f"Google search error: {e}")
        return []
