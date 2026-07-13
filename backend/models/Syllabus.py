from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connectivity import Base


class Syllabus(Base):
    __tablename__ = "syllabi"

    id = Column(Integer, primary_key=True, index=True)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)

    academic_year = Column(String(20), nullable=False)

    title = Column(String(255), nullable=False)

    version = Column(String(20), default="1.0")

    file_url = Column(String(500), nullable=True)

    # extracted_text = Column(Text, nullable=True)

    embedding_status = Column(Boolean, default=False)

    status = Column(String(20), default="Active")   # Active, Archived

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

    # Relationships
    board = relationship("Board", backref="syllabi")
    class_ = relationship("Class", backref="syllabi")
    subject = relationship("Subject", backref="syllabi")