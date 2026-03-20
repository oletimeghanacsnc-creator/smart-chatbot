import requests

SERPER_API_KEY = "2dd8ef5924b3a758197d5fb4c2a7a88ef7c711e9"

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