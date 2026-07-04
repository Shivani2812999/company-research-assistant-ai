from pydantic import BaseModel


class ResearchRequest(BaseModel):
    query: str
    model: str = "openai/gpt-4o-mini"