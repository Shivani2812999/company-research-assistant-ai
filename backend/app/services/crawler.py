import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Pages we are interested in crawling
IMPORTANT_PAGES = [
    "about",
    "product",
    "products",
    "service",
    "services",
    "pricing",
    "contact",
    "solution",
    "solutions"
]


def crawl_homepage(url: str) -> dict:
    """
    Download a webpage and extract its title and text.
    """

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        # Remove unwanted tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        title = soup.title.string.strip() if soup.title else "No Title"

        text = soup.get_text(separator=" ", strip=True)

        return {
            "title": title,
            "content": text[:5000]
        }

    except Exception as e:
        import traceback
        traceback.print_exc()

        return {
            "title": "",
            "content": ""
        }


def find_links(url: str):
    """
    Find all links on a webpage.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    soup = BeautifulSoup(response.text, "lxml")

    links = []

    for a in soup.find_all("a", href=True):

        absolute = urljoin(url, a["href"])

        if absolute not in links:
            links.append(absolute)

    return links


def filter_links(links):
    """
    Keep only important pages.
    """

    filtered = []

    for link in links:

        lower = link.lower()

        if any(word in lower for word in IMPORTANT_PAGES):
            filtered.append(link)

    return filtered

def crawl_important_pages(url: str):
    """
    Crawl important pages and combine their content.
    """

    # Homepage content
    homepage = crawl_homepage(url)

    # Find all links
    links = find_links(url)

    # Keep only important links
    links = filter_links(links)

    pages = []

    combined_text = homepage["content"]

    # Crawl only first 5 pages
    for link in links[:5]:

        print(f"Crawling: {link}")

        page = crawl_homepage(link)

        pages.append({
            "url": link,
            "title": page["title"]
        })

        combined_text += "\n\n" + page["content"]

    return {
        "title": homepage["title"],
        "pages": pages,
        "content": combined_text
    }