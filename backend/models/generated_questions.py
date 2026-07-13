from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connectivity import Base


class GeneratedQuestion(Base):
    __tablename__ = "generated_questions"

    id = Column(Integer, primary_key=True, index=True)

    generated_paper_id = Column(
        Integer,
        ForeignKey("generated_question_papers.id"),
        nullable=False
    )

    syllabus_topic_id = Column(
        Integer,
        ForeignKey("syllabus_topics.id"),
        nullable=False
    )

    question_no = Column(Integer, nullable=False)

    question_type = Column(String(50), nullable=False)
    # MCQ, Short Answer, Long Answer, Case Study, Assertion-Reason

    difficulty_level = Column(String(20), nullable=True)
    # Easy, Medium, Hard

    question_text = Column(Text, nullable=False)

    marks = Column(Integer, nullable=False)

    answer = Column(Text, nullable=True)

    explanation = Column(Text, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    generated_paper = relationship(
        "GeneratedQuestionPaper",
        backref="questions"
    )

    syllabus_topic = relationship(
        "SyllabusTopic",
        backref="generated_questions"
    )