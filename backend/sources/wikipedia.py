import requests

def search_wikipedia(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 5
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        results = []
        for item in data.get("query", {}).get("search", []):
            title = item["title"]
            snippet = item["snippet"].replace("<span class=\"searchmatch\">", "").replace("</span>", "")
            url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            results.append({
                "source": "Wikipedia",
                "title": title,
                "url": url,
                "snippet": snippet
            })
        return results
    except Exception as e:
        print(f"Wikipedia search error: {e}")
        return []
