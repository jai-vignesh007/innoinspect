from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class ChecklistItem(BaseModel):
    item: str
    status: str               # "OK", "ISSUE", "SKIPPED"
    note: Optional[str] = None


class InspectionCreate(BaseModel):
    inspector_name: str
    location: str
    machine_id: str
    checklist: Optional[List[ChecklistItem]] = None
    notes: Optional[str] = None


class InspectionOut(BaseModel):
    id: int
    inspector_name: str
    location: str
    machine_id: str
    checklist: Optional[List[ChecklistItem]] = None
    notes: Optional[str] = None

    detected_defects: Optional[List[str]] = None
    risk_level: Optional[str] = None
    ai_summary: Optional[str] = None

    created_at: datetime

    class Config:
        orm_mode = True
