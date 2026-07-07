from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connectivity import get_db
from models.user import User
from schemes.user import UserCreate, UserResponse,LoginResponse,LoginRequest
from controller.auth_controller import AuthController

auth_route = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_route.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return AuthController.register_user(user, db)

@auth_route.post("/login", response_model=LoginResponse)
def login(user: LoginRequest, db: Session = Depends(get_db)):
    return AuthController.login_user(user, db)