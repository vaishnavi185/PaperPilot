from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Dict, Any


class BoardPatternBase(BaseModel):
    board_id: int
    class_id: int
    subject_id: int
    exam_type_id: int

    academic_year: str

    pattern_json: Dict[str, Any]

    source_url: Optional[str] = None
    medium: Optional[str] = None

    status: str = "Pending"
    is_active: bool = True


class BoardPatternCreate(BoardPatternBase):
    pass


class BoardPatternUpdate(BaseModel):
    board_id: Optional[int] = None
    class_id: Optional[int] = None
    subject_id: Optional[int] = None
    exam_type_id: Optional[int] = None

    academic_year: Optional[str] = None

    pattern_json: Optional[Dict[str, Any]] = None

    source_url: Optional[str] = None
    medium: Optional[str] = None

    status: Optional[str] = None
    is_active: Optional[bool] = None


class BoardPatternResponse(BoardPatternBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)