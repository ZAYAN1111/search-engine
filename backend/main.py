from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.sources.google import search_google
from backend.sources.youtube import search_youtube
from backend.sources.wikipedia import search_wikipedia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_all(q: str):
    results = []
    results.extend(search_google(q))
    results.extend(search_youtube(q))
    results.extend(search_wikipedia(q))
    return {"query": q, "results": results}



