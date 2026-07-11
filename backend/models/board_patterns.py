from sqlalchemy import Boolean

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connectivity import Base


class BoardPattern(Base):
    __tablename__ = "board_patterns"

    id = Column(Integer, primary_key=True, index=True)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    academic_year = Column(String(20), nullable=False)

    pattern_json = Column(JSON, nullable=False)

    source_url = Column(String(255), nullable=True)
    medium=Column(String(50), nullable=True)  # e.g. English, Hindi, etc.
    status = Column(String(20), default="Pending")  # Pending, Approved, Rejected
    is_active = Column(Boolean, default=True)

    last_updated = Column(DateTime(timezone=True), server_default=func.now())

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    board = relationship("Board", backref="patterns")
    subject = relationship("Subject", backref="patterns")
    class_ = relationship("Class", backref="patterns")