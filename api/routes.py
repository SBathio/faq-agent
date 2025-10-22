from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from agent.faq_agent import run_agent

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    style: str = "default"

@router.post("/", tags=["FAQ Agent"])
async def ask_question(payload: QueryRequest):
    try:
        # Use asynchronous agent execution
        result = await run_agent.arun({"input": payload.query})
        return {
            "query": payload.query,
            "answer": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))