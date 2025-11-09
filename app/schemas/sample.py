# app/schemas/sample.py
from pydantic import BaseModel
from datetime import datetime

class SampleItemCreate(BaseModel):
    name: str
    description: str | None = None
    language: str | None = None

class SampleItemResponse(BaseModel):
    id: int
    name: str
    description: str | None
    language: str | None
    created_at: datetime

    class Config:
        from_attributes = True