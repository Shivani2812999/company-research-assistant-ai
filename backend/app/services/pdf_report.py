from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(result: dict):

    reports_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "reports"
    )

    os.makedirs(reports_dir, exist_ok=True)

    filename = f"{result['query'].replace(' ', '_')}.pdf"
    file_path = os.path.join(reports_dir, filename)

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Company Research Report</b>", styles["Heading1"]))
    story.append(Paragraph(f"<b>Company:</b> {result['query']}", styles["Normal"]))
    story.append(Paragraph(f"<b>Website:</b> {result['website']}", styles["Normal"]))

    analysis = result["analysis"]

    story.append(Paragraph("<br/><b>Company Summary</b>", styles["Heading2"]))
    story.append(Paragraph(analysis["company_summary"], styles["Normal"]))

    story.append(Paragraph("<br/><b>Products / Services</b>", styles["Heading2"]))
    story.append(Paragraph(analysis["products_services"], styles["Normal"]))

    story.append(Paragraph("<br/><b>Phone Number</b>", styles["Heading2"]))
    story.append(Paragraph(analysis["phone_number"] or "Not Available", styles["Normal"]))

    story.append(Paragraph("<br/><b>Address</b>", styles["Heading2"]))
    story.append(Paragraph(analysis["address"] or "Not Available", styles["Normal"]))

    story.append(Paragraph("<br/><b>Pain Points</b>", styles["Heading2"]))
    for point in analysis["pain_points"]:
        story.append(Paragraph(f"• {point}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Competitors</b>", styles["Heading2"]))
    for competitor in analysis["competitors"]:
        story.append(Paragraph(f"• {competitor}", styles["Normal"]))

    doc.build(story)

    print("PDF saved at:", file_path)

    return filename