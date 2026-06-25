from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.sources.wikipedia import search_wikipedia
from backend.sources.youtube import search_youtube

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "status": "online",
        "service": "Project Voyager"
    }


@app.get("/search")
def search(q: str):

    wiki_results = search_wikipedia(q)
    youtube_results = search_youtube(q)

    results = []

    # Alternate Wikipedia and YouTube results
    max_len = max(len(wiki_results), len(youtube_results))

    for i in range(max_len):

        if i < len(wiki_results):
            results.append(wiki_results[i])

        if i < len(youtube_results):
            results.append(youtube_results[i])

    return {
        "query": q,
        "count": len(results),
        "results": results
    }
