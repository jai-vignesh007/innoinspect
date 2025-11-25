from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base import Base

class Inspection(Base):
    __tablename__ = "inspections"

    id = Column(Integer, primary_key=True, index=True)

    inspector_name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    machine_id = Column(String(100), nullable=False)

    checklist = Column(JSONB)
    notes = Column(Text)

    detected_defects = Column(JSONB)
    risk_level = Column(String(20))
    ai_summary = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
