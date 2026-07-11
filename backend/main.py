from fastapi import FastAPI
from sqlalchemy import text

from database.connectivity import Base, engine
from routes.auth_rountes import auth_route
from routes.role_routes import role_router
from models.user import User
from models.Role import Role
from models.module import Module
from models.BoardType import Board
from models.board_patterns import BoardPattern
from models.subject import Subject
from models.Class import Class


app = FastAPI(title="School Management API")
Base.metadata.create_all(bind=engine)
# Include Routes
app.include_router(auth_route)
app.include_router(role_router)

# @app.get("/")
# def root():
#     return {"message": "API is running"}

# Database Connection Check
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database Connected Successfully!")
except Exception as e:
    print(" Connection Failed")
    print(e)