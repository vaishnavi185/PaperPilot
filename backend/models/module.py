from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from database.connectivity import Base


class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False, index=True)

    description = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True)
    is_system = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )