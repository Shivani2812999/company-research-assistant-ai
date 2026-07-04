# 🚀 AI Company Research Assistant

An AI-powered web application that researches any company from its name, discovers its official website, crawls important business information, analyzes the content using LLMs, and generates a professional PDF research report.

---

## 📌 Features

- 🔍 Search any company by name
- 🌐 Automatically find the official website
- 🕸️ Crawl important pages (About, Services, Contact, etc.)
- 🤖 AI-generated company analysis
- 📊 Extract:
  - Company Summary
  - Products & Services
  - Contact Information
  - Address
  - Pain Points
  - Competitors
- 📄 Generate downloadable PDF reports
- 💬 Clean React-based user interface
- ⚡ FastAPI backend

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- Axios
- CSS

### Backend
- FastAPI
- Python
- BeautifulSoup
- Requests
- ReportLab

### AI
- OpenRouter API
- Large Language Models (GPT)

---

## 📂 Project Structure

```
company-research-assistant/
│
├── backend/
│   ├── app/
│   │   ├── services/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Shivani2812999/company-research-assistant-ai.git
cd company-research-assistant-ai
```

---

### 2. Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 🚀 Usage

1. Enter a company name.
2. Click **Research**.
3. The system:
   - Finds the official website
   - Crawls important pages
   - Performs AI analysis
   - Displays the research results
4. Download the generated PDF report.

---

## 📄 API Endpoints

### Research Company

```
POST /research
```

Request:

```json
{
  "query": "Google",
  "model": "openai/gpt-4o-mini"
}
```

---

### Download PDF

```
POST /research/pdf
```

---

### Download Generated Report

```
GET /reports/{filename}
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- AI Research Results
- PDF Download
- Generated PDF

Example:

```
README Images/
    home.png
    result.png
    pdf.png
```

Then:

```md
![Home](images/home.png)

![Research Result](images/result.png)

![PDF](images/pdf.png)
```

---

## 🎯 Future Improvements

- Multi-page website crawling
- Company logo detection
- Lead generation
- Financial information extraction
- Export to Word
- Email reports
- Authentication
- Research history
- Dashboard
- Docker deployment

---

## 👩‍💻 Author

**Shivani Hadapad**

- GitHub: https://github.com/Shivani2812999
- LinkedIn: https://www.linkedin.com/in/Shivani-hadapad-1a838717a/

---

## ⭐ If you found this project useful, please give it a star!
