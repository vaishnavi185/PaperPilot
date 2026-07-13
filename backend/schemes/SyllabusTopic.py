from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class SyllabusTopicBase(BaseModel):
    syllabus_id: int

    unit_no: Optional[int] = None
    unit_name: Optional[str] = None

    chapter_no: Optional[int] = None
    chapter_name: str

    topic_name: Optional[str] = None

    content: str

    embedding_status: bool = False

    is_active: bool = True


class SyllabusTopicCreate(SyllabusTopicBase):
    pass


class SyllabusTopicUpdate(BaseModel):
    syllabus_id: Optional[int] = None

    unit_no: Optional[int] = None
    unit_name: Optional[str] = None

    chapter_no: Optional[int] = None
    chapter_name: Optional[str] = None

    topic_name: Optional[str] = None

    content: Optional[str] = None

    embedding_status: Optional[bool] = None

    is_active: Optional[bool] = None


class SyllabusTopicResponse(SyllabusTopicBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)