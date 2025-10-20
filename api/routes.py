from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agent.faq_agent import answer_with_agent
from typing import Optional

router = APIRouter()

class AgentQuery(BaseModel):
    query: str
    style: Optional[str] = "default"

    class Config:
        json_schema_extra = {
            "example": {
                "query": "How do I reset my password?",
                "style": "friendly"
            }
        }

from fastapi import APIRouter, HTTPException, Body

@router.post("/agent-ask", tags=["Agentic QA"])
def ask_with_agent(
    request: AgentQuery = Body(
        example={
            "query": "How do I reset my password?",
            "style": "friendly"
        }
    )
):
    try:
        result = answer_with_agent(request.query, request.style)
        return {
            "query": result.get("query", request.query),
            "answer": result.get("answer", ""),
            "sources": result.get("sources", [])
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))