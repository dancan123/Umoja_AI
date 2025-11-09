# app/schemas/chat.py
from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None

class ChatResponse(BaseModel):
    response: str
    detected_language: str
    session_id: str
    timestamp: datetime

    class Config:
        from_attributes = True

class ConversationHistory(BaseModel):
    id: int
    session_id: str
    user_message: str
    bot_response: str
    detected_language: str
    timestamp: datetime

    class Config:
        from_attributes = True