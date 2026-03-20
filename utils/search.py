import requests

import os
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")

def web_search(query):
    try:
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": SERPER_API_KEY},
            json={"q": query}
        )
        results = response.json().get("organic", [])[:3]
        return "\n".join(f"{x['title']}: {x['snippet']}" for x in results)
    except Exception as e:
        return f"Search error: {e}"