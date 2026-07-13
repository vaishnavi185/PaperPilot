from fastapi import FastAPI
from sqlalchemy import text

from database.connectivity import Base, engine
from routes.index import api_router
from middleware.cors import setup_cors
# Import models
from models.user import User
from models.Role import Role
from models.module import Module
from models.BoardType import Board
from models.board_patterns import BoardPattern
from models.subject import Subject
from models.Class import Class
from models.Syllabus import Syllabus
from models.exam_types import ExamType
from models.generated_question_papers import GeneratedQuestionPaper
from models.syllabus_topics import SyllabusTopic

app = FastAPI(title="Exam_Pilot")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database Connected Successfully!")
except Exception as e:
    print("Connection Failed")
    print(e)

setup_cors(app)    