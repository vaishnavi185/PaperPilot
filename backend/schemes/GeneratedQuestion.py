from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class GeneratedQuestionBase(BaseModel):
    generated_paper_id: int
    syllabus_topic_id: int

    question_no: int

    question_type: str
    difficulty_level: Optional[str] = None

    question_text: str

    marks: int

    answer: Optional[str] = None
    explanation: Optional[str] = None

    is_active: bool = True


class GeneratedQuestionCreate(GeneratedQuestionBase):
    pass


class GeneratedQuestionUpdate(BaseModel):
    generated_paper_id: Optional[int] = None
    syllabus_topic_id: Optional[int] = None

    question_no: Optional[int] = None

    question_type: Optional[str] = None
    difficulty_level: Optional[str] = None

    question_text: Optional[str] = None

    marks: Optional[int] = None

    answer: Optional[str] = None
    explanation: Optional[str] = None

    is_active: Optional[bool] = None


class GeneratedQuestionResponse(GeneratedQuestionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)