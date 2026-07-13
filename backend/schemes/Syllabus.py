from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class SyllabusBase(BaseModel):
    board_id: int
    class_id: int
    subject_id: int

    academic_year: str

    title: str
    version: str = "1.0"

    file_url: Optional[str] = None

    status: str = "Active"
    is_active: bool = True


class SyllabusCreate(SyllabusBase):
    pass


class SyllabusUpdate(BaseModel):
    board_id: Optional[int] = None
    class_id: Optional[int] = None
    subject_id: Optional[int] = None

    academic_year: Optional[str] = None

    title: Optional[str] = None
    version: Optional[str] = None

    file_url: Optional[str] = None

    status: Optional[str] = None
    is_active: Optional[bool] = None


class SyllabusResponse(SyllabusBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)