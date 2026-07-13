from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class GeneratedQuestionPaperBase(BaseModel):
    board_id: int
    class_id: int
    subject_id: int

    syllabus_id: int
    board_pattern_id: int
    exam_type_id: int

    title: str

    total_marks: int
    duration: str

    file_url: Optional[str] = None

    status: str = "Generated"
    is_active: bool = True


class GeneratedQuestionPaperCreate(GeneratedQuestionPaperBase):
    pass


class GeneratedQuestionPaperUpdate(BaseModel):
    board_id: Optional[int] = None
    class_id: Optional[int] = None
    subject_id: Optional[int] = None

    syllabus_id: Optional[int] = None
    board_pattern_id: Optional[int] = None
    exam_type_id: Optional[int] = None

    title: Optional[str] = None

    total_marks: Optional[int] = None
    duration: Optional[str] = None

    file_url: Optional[str] = None

    status: Optional[str] = None
    is_active: Optional[bool] = None


class GeneratedQuestionPaperResponse(GeneratedQuestionPaperBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)