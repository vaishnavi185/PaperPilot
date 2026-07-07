from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database.connectivity import Base




class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)

    school_name = Column(String(255), nullable=False)
    board = Column(String(100), nullable=False)              # CBSE, ICSE, State Board
    medium = Column(String(100), nullable=False)             # English, Hindi, etc.
    academic_session = Column(String(20), nullable=False)    # 2026-27

    logo = Column(String(500), nullable=True)

    address = Column(String(500), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    pincode = Column(String(10), nullable=False)

    status = Column(String(20), default="active")            # active, inactive, suspended

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )