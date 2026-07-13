from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database.connectivity import get_db
from utils.jwt import verify_access_token
from models.user import User
from exceptions.httpexception import unauthorized

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    token = credentials.credentials

    payload = verify_access_token(token)

    if not payload:
        unauthorized("Invalid or expired token")

    user = db.query(User).filter(User.id == int(payload["sub"])).first()

    if not user:
        unauthorized("User not found")

    return user