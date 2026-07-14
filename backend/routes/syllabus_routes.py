
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from controller.syllabus_controller   import SyllabusController
from database.connectivity import get_db
from dependencies.auth import get_current_user
from schemes.Syllabus import (
    SyllabusCreate,
    SyllabusUpdate,
    SyllabusResponse,
)

syllabus_router = APIRouter(
    prefix="/syllabi",
    tags=["Syllabus"]
)


@syllabus_router.post("/add-syllabus", response_model=SyllabusResponse)
def create_syllabus(
    board_id: int = Form(...),
    class_id: int = Form(...),
    subject_id: int = Form(...),
    academic_year: str = Form(...),
    title: str = Form(...),
    version: str = Form("1.0"),
    status: str = Form("Active"),
    is_active: bool = Form(True),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SyllabusController.create_syllabus(
        board_id,
        class_id,
        subject_id,
        academic_year,
        title,
        version,
        status,
        is_active,
        file,
        db,
    )


@syllabus_router.get("/get-syllabus", response_model=list[SyllabusResponse])
def get_all_syllabi(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SyllabusController.get_all_syllabi(db)


@syllabus_router.get("/get_by_id/{syllabus_id}", response_model=SyllabusResponse)
def get_syllabus(
    syllabus_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SyllabusController.get_syllabus_by_id(syllabus_id, db)


@syllabus_router.put("/update-syllabus/{syllabus_id}", response_model=SyllabusResponse)
def update_syllabus(
    syllabus_id: int,
    syllabus: SyllabusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SyllabusController.update_syllabus(syllabus_id, syllabus, db)


@syllabus_router.delete("/delete-syllabus/{syllabus_id}")
def delete_syllabus(
    syllabus_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SyllabusController.delete_syllabus(syllabus_id, db)

