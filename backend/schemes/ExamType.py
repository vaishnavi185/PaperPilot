from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class ExamTypeBase(BaseModel):
    name: str
    code: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True


class ExamTypeCreate(ExamTypeBase):
    pass


class ExamTypeUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class ExamTypeResponse(ExamTypeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)