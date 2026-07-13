from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connectivity import Base


class GeneratedQuestionPaper(Base):
    __tablename__ = "generated_question_papers"

    id = Column(Integer, primary_key=True, index=True)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)

    syllabus_id = Column(Integer, ForeignKey("syllabi.id"), nullable=False)
    board_pattern_id = Column(Integer, ForeignKey("board_patterns.id"), nullable=False)
    exam_type_id = Column(Integer, ForeignKey("exam_types.id"), nullable=False)

    title = Column(String(255), nullable=False)

    total_marks = Column(Integer, nullable=False)
    duration = Column(String(50), nullable=False)

    file_url = Column(String(500), nullable=True)

    status = Column(String(20), default="Generated")
    # Generated, Reviewed, Published

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

    deleted_at = Column(DateTime(timezone=True), nullable=True)

    board = relationship("Board", backref="generated_papers")
    class_ = relationship("Class", backref="generated_papers")
    subject = relationship("Subject", backref="generated_papers")
    syllabus = relationship("Syllabus", backref="generated_papers")
    board_pattern = relationship("BoardPattern", backref="generated_papers")
    exam_type = relationship("ExamType", backref="generated_papers")