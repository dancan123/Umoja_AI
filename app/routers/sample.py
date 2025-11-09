# app/routers/sample.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.crud import create_item, get_items, get_item_by_id
from app.schemas import SampleItemCreate, SampleItemResponse

router = APIRouter(prefix="/sample", tags=["Sample"])

@router.post("/", response_model=SampleItemResponse)
async def add_item(
    item: SampleItemCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new sample item"""
    return await create_item(
        db, 
        name=item.name, 
        description=item.description,
        language=item.language
    )

@router.get("/", response_model=list[SampleItemResponse])
async def list_items(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all sample items"""
    return await get_items(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=SampleItemResponse)
async def get_item(
    item_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific sample item by ID"""
    item = await get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item