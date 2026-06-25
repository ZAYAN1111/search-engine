import requests


def search_wikipedia(query):
    try:
        response = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": 10
            },
            headers={
                "User-Agent": "ProjectVoyager/1.0"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        results = []

        for item in data.get("query", {}).get("search", []):

            title = item.get("title", "")

            snippet = (
                item.get("snippet", "")
                .replace('<span class="searchmatch">', '')
                .replace('</span>', '')
            )

            results.append({
                "source": "Wikipedia",
                "title": title,
                "url": f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
                "snippet": snippet
            })

        print(f"Wikipedia returned {len(results)} results for '{query}'")

        return results

    except Exception as e:
        print("Wikipedia Error:", e)

        return []
