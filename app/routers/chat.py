# app/routers/chat.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import uuid

from app.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse, ConversationHistory
from app.crud.conversation import create_conversation, get_conversation_history
from app.services.chatbot import generate_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Send a message to the Umoja AI chatbot.
    The bot will detect your language and respond accordingly.
    """
    # Generate session ID if not provided
    session_id = request.session_id or str(uuid.uuid4())
    
    # Generate response
    bot_response, detected_language = generate_response(request.message)
    
    # Save conversation to database
    conversation = await create_conversation(
        db=db,
        session_id=session_id,
        user_message=request.message,
        bot_response=bot_response,
        detected_language=detected_language
    )
    
    return ChatResponse(
        response=bot_response,
        detected_language=detected_language,
        session_id=session_id,
        timestamp=conversation.timestamp
    )

@router.get("/history/{session_id}", response_model=list[ConversationHistory])
async def get_history(
    session_id: str,
    limit: int = 50,
    db: AsyncSession = Depends(get_db)
):
    """Get conversation history for a session"""
    history = await get_conversation_history(db, session_id, limit)
    return history