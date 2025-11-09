# app/models/sample.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class SampleItem(Base):
    __tablename__ = "sample_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    language = Column(String(10), nullable=True)  # Language code
    created_at = Column(DateTime, default=datetime.utcnow)