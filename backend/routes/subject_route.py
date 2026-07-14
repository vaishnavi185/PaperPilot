from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.subject_controller import SubjectController
from database.connectivity import get_db
from dependencies.auth import get_current_user
from schemes.Subject import (
    SubjectCreate,
    SubjectUpdate,
    SubjectResponse,
)

subject_router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@subject_router.post("/add-subject", response_model=SubjectResponse)
def create_subject(
    subject: SubjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SubjectController.create_subject(subject, db)


@subject_router.get("/get-subject", response_model=list[SubjectResponse])
def get_all_subjects(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SubjectController.get_all_subjects(db)


@subject_router.get("/get_by_id/{subject_id}", response_model=SubjectResponse)
def get_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SubjectController.get_subject_by_id(subject_id, db)


@subject_router.put("/update-subject/{subject_id}", response_model=SubjectResponse)
def update_subject(
    subject_id: int,
    subject: SubjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SubjectController.update_subject(subject_id, subject, db)


@subject_router.delete("/delete-subject/{subject_id}")
def delete_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return SubjectController.delete_subject(subject_id, db)