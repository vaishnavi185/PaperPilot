from sqlalchemy.orm import Session

from models.user import User
from schemes.user import UserCreate,LoginRequest
from utils.security import hash_password,verify_password
from utils.jwt import create_access_token


class AuthController:

    @staticmethod
    def register_user(user: UserCreate, db: Session):
        new_user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password) , # We'll hash this now
            #role_id=user.role_id
        )
        print(hash_password(user.password))      
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    def login_user(user: LoginRequest, db: Session):

        db_user = db.query(User).filter(User.email == user.email).first()

        if not db_user:
            return {
                "message": "Invalid email or password"
            }

        if not verify_password(user.password, db_user.password):
            return {
                "message": "Invalid email or password"
            }

        access_token = create_access_token(
        data={
        "sub": str(db_user.id),
        "email": db_user.email,
        #"role": db_user.role.name
        }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": db_user.id,
                "name": db_user.name,
                "email": db_user.email,
                #"role": db_user.role.name
            }
        }