from schemes.user import UserCreate, LoginRequest
from sqlalchemy.orm import Session
from service.auth_service import AuthService


class AuthController:

    @staticmethod
    def register_user(user: UserCreate, db: Session):
        return AuthService.register_user(user, db)

    @staticmethod
    def login_user(user: LoginRequest, db: Session):
        return AuthService.login_user(user, db)