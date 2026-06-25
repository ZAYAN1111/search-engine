from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.sources.wikipedia import search_wikipedia

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

    results = search_wikipedia(q)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }
