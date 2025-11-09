# app/crud/conversation.py
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.conversation import Conversation

async def create_conversation(
    db: AsyncSession,
    session_id: str,
    user_message: str,
    bot_response: str,
    detected_language: str
):
    conversation = Conversation(
        session_id=session_id,
        user_message=user_message,
        bot_response=bot_response,
        detected_language=detected_language
    )
    db.add(conversation)
    await db.commit()
    await db.refresh(conversation)
    return conversation

async def get_conversation_history(
    db: AsyncSession,
    session_id: str,
    limit: int = 50
):
    result = await db.execute(
        select(Conversation)
        .where(Conversation.session_id == session_id)
        .order_by(Conversation.timestamp.desc())
        .limit(limit)
    )
    return result.scalars().all()