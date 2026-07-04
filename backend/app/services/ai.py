import os
import requests
import json

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def analyze_company(content: str, model: str):

    prompt = f"""
You are an expert business analyst.

Analyze the following company website content.

Return ONLY valid JSON.

Format:

{{
    "company_summary":"",
    "products_services":"",
    "phone_number":"",
    "address":"",
    "pain_points":[
        "",
        "",
        ""
    ],
    "competitors":[
        "",
        "",
        ""
    ]
}}

Website Content:

{content[:15000]}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        timeout=120
    )

    response.raise_for_status()

    # result = response.json()

    # return result["choices"][0]["message"]["content"]


    result = response.json()
    content = result["choices"][0]["message"]["content"]
    content = content.strip()
    content = content.replace("```json", "").replace("```", "")

    try:
        return json.loads(content)  
    except Exception:
        return {
            "raw_response": content
            
        }
    