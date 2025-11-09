# app/crud/sample.py
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.sample import SampleItem

async def create_item(
    db: AsyncSession, 
    name: str, 
    description: str = None,
    language: str = None
):
    item = SampleItem(name=name, description=description, language=language)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(SampleItem).offset(skip).limit(limit))
    return result.scalars().all()

async def get_item_by_id(db: AsyncSession, item_id: int):
    result = await db.execute(select(SampleItem).where(SampleItem.id == item_id))
    return result.scalar_one_or_none()