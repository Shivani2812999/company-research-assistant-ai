from fastapi import FastAPI
import os
from app.models import ResearchRequest
from app.services.search import find_official_website
from app.services.crawler import crawl_homepage
from app.services.resolver import research_company
from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException
from fastapi.responses import FileResponse

from app.services.pdf_report import generate_pdf

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel

class PDFRequest(BaseModel):
    query: str
    result: dict


# @app.post("/research/pdf")
# async def download_pdf(request: PDFRequest):
#     pdf_path = generate_pdf({
#         "query": request.query,
#         "website": request.result.get("website"),
#         "analysis": request.result.get("analysis")
#     })

#     return FileResponse(
#         path=pdf_path,
#         media_type="application/pdf",
#         filename="company-report.pdf"
#     )


REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")

@app.get("/reports/{filename}")
async def download_report(filename: str):
    filename = os.path.basename(filename)

    file_path = os.path.join(REPORTS_DIR, filename)

    print("REPORTS_DIR:", REPORTS_DIR)
    print("Looking for:", file_path)
    print("Exists:", os.path.exists(file_path))

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Report not found: {filename}")

    return FileResponse(file_path, media_type="application/pdf", filename=filename)


@app.get("/")
def home():
    return {
        "message": "Company Research Assistant API is running!"
    }

@app.post("/research")
def research(request: ResearchRequest):

    # result = research_company(request.query)
    result = research_company(
    request.query,
    request.model
)

    return result

from app.services.crawler import find_links, filter_links

@app.get("/test-links")
def test_links():

    links = find_links("https://github.com")

    important = filter_links(links)

    return {
        "total_links": len(links),
        "important_links": important
    }