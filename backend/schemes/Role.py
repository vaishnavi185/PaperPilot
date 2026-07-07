from pydantic import BaseModel

from datetime import datetime
class RoleCreate(BaseModel):
    name: str
    #description: str | None = None
class RoleUpdate(BaseModel):
    name: str
    description: str | None = None    

class RoleResponse(BaseModel):
    id: int
    name: str
    #description: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True    