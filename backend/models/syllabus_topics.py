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


class SyllabusTopic(Base):
    __tablename__ = "syllabus_topics"

    id = Column(Integer, primary_key=True, index=True)

    syllabus_id = Column(Integer, ForeignKey("syllabi.id"), nullable=False)

    unit_no = Column(Integer, nullable=True)
    unit_name = Column(String(255), nullable=True)

    chapter_no = Column(Integer, nullable=True)
    chapter_name = Column(String(255), nullable=False)

    topic_name = Column(String(255), nullable=True)

    content = Column(Text, nullable=False)

    embedding_status = Column(Boolean, default=False)

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

    syllabus = relationship("Syllabus", backref="topics")