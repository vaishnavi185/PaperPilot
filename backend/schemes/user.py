from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime
from typing import Optional


from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain an uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain a lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain a digit")
        if not re.search(r"[@$!%*?&]", value):
            raise ValueError("Password must contain a special character")

        return value
   # role_id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
   # role_id: Optional[int] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    #role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserInfo(BaseModel):
    id: int
    name: str
    email: EmailStr
    #role: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserInfo