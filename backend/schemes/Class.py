from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class ClassBase(BaseModel):
    board_id: int
    name: str
    code: Optional[str] = None
    is_active: bool = True


class ClassCreate(ClassBase):
    pass


class ClassUpdate(BaseModel):
    board_id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    is_active: Optional[bool] = None


class ClassResponse(ClassBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)