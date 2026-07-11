from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connectivity import Base


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)

    name = Column(String(50), nullable=False)   # e.g. Class 10
    code = Column(String(20), nullable=True)    # e.g. X, 10

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted_at = Column(DateTime(timezone=True), nullable=True)

    board = relationship("Board", backref="classes")