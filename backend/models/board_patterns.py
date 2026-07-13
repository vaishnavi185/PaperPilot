from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connectivity import Base


class BoardPattern(Base):
    __tablename__ = "board_patterns"

    id = Column(Integer, primary_key=True, index=True)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    exam_type_id = Column(Integer, ForeignKey("exam_types.id"), nullable=False)

    academic_year = Column(String(20), nullable=False)

    pattern_json = Column(JSON, nullable=False)

    source_url = Column(String(255), nullable=True)
    medium = Column(String(50), nullable=True)   # English, Hindi, etc.

    status = Column(String(20), default="Pending")
    # Pending, Approved, Rejected

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

    board = relationship("Board", backref="patterns")
    class_ = relationship("Class", backref="patterns")
    subject = relationship("Subject", backref="patterns")
    exam_type = relationship("ExamType", backref="patterns")