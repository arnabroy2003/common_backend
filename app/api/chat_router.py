from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()

service = ChatService()


@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    reply = service.chat(
        db=db,
        request=request
    )

    return {
        "reply": reply
    }