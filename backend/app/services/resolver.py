from app.services.search import find_official_website
from app.services.crawler import crawl_important_pages
from app.services.ai import analyze_company
from app.services.pdf_report import generate_pdf


def research_company(query: str, model: str):

    website = find_official_website(query)

    page = crawl_important_pages(website)

    ai_result = analyze_company(
        page["content"],
        model
    )

    pdf_file = generate_pdf({
    "query": query,
    "website": website,
    "analysis": ai_result
})

    return {
        "query": query,
        "website": website,
        "title": page["title"],
        "pages": page["pages"],
        "analysis": ai_result,
        "pdf": pdf_file
    }