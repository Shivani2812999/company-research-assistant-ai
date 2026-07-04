import requests
from app.config import SERPER_API_KEY

SERPER_URL = "https://google.serper.dev/search"


def find_official_website(query: str) -> str:
    """
    Finds the official website of a company using Serper.dev.
    If the user already enters a URL, return it directly.
    """

    query = query.strip()

    # If it's already a website, return it
    if query.startswith("http://") or query.startswith("https://"):
        return query

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "q": f"{query} official website"
    }

    try:
        response = requests.post(
            SERPER_URL,
            headers=headers,
            json=payload,
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        organic = data.get("organic", [])

        if organic:
            return organic[0]["link"]

        return ""

    except Exception as e:
        print("Serper Error:", e)
        return ""