from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class BoardBase(BaseModel):
    name: str
    code: str
    official_website: Optional[str] = None
    is_active: bool = True


class BoardCreate(BoardBase):
    pass


class BoardUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    official_website: Optional[str] = None
    is_active: Optional[bool] = None


class BoardResponse(BoardBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)