from utils.logger import logger

from exceptions.httpexception import bad_request, unauthorized
from sqlalchemy.orm import Session

from models.user import User
from schemes.user import UserCreate, LoginRequest
from utils.security import hash_password, verify_password
from utils.jwt import create_access_token


class AuthService:

    @staticmethod
    def register_user(user: UserCreate, db: Session):
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            return bad_request("Email already exists")
        
        new_user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f"User created successfully: {new_user.email}")
        return new_user

    @staticmethod
    def login_user(user: LoginRequest, db: Session):
        db_user = db.query(User).filter(User.email == user.email).first()

        if not db_user:
            logger.warning(f"Login failed: {user.email} - User not found")
            return unauthorized("Invalid email or password")

        if not verify_password(user.password, db_user.password):
            logger.warning(f"Login failed: {user.email} - Invalid password")
            return unauthorized("Invalid email or password")

        access_token = create_access_token(
            data={
                "sub": str(db_user.id),
                "email": db_user.email
            }
        )
        logger.info(f"User logged in successfully: {db_user.email}")
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": db_user.id,
                "name": db_user.name,
                "email": db_user.email
            }
        }