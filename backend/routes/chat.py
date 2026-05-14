from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.drive_agent import agent

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    response = agent.invoke(
        {
            "input": request.message
        }
    )

    return {
        "response": response["output"]
    }