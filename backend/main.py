from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend.sources.google import search_google
from backend.sources.youtube import search_youtube
from backend.sources.wikipedia import search_wikipedia

app = FastAPI()

@app.get("/search", response_class=HTMLResponse)
def search_all(q: str):

    results = []
    results.extend(search_google(q))
    results.extend(search_youtube(q))
    results.extend(search_wikipedia(q))

    html = f"""
    <html>
    <head>
        <title>Results for {q}</title>
    </head>
    <body>
        <h1>Results for: {q}</h1>
    """

    for result in results:
        html += f"""
        <div style="margin-bottom:20px;">
            <a href="{result['url']}">
                <h3>{result['title']}</h3>
            </a>
            <p>{result.get('snippet','')}</p>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return html
