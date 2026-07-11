from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
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