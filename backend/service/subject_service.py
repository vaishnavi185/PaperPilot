from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.subject import Subject
from exceptions.httpexception import bad_request,not_found
from schemes.Subject import SubjectCreate, SubjectUpdate


class SubjectService:

    @staticmethod
    def create_subject(subject_data: SubjectCreate, db: Session):
        existing = db.query(Subject).filter(Subject.code == subject_data.code).first()
        if existing:
            bad_request("Subject with this code already exists")

        new_subject = Subject(**subject_data.model_dump())
        db.add(new_subject)
        db.commit()
        db.refresh(new_subject)
        return new_subject

    @staticmethod
    def get_all_subjects(db: Session):
        return db.query(Subject).all()

    @staticmethod
    def get_subject_by_id(subject_id: int, db: Session):
        subject = db.query(Subject).filter(Subject.id == subject_id).first()
        if not subject:
            not_found("Subject not found")
        return subject

    @staticmethod
    def update_subject(subject_id: int, subject_data: SubjectUpdate, db: Session):
        subject = db.query(Subject).filter(Subject.id == subject_id).first()
        if not subject:
            not_found("Subject not found")

        for key, value in subject_data.model_dump(exclude_unset=True).items():
            setattr(subject, key, value)

        db.commit()
        db.refresh(subject)
        return subject

    @staticmethod
    def delete_subject(subject_id: int, db: Session):
        subject = db.query(Subject).filter(Subject.id == subject_id).first()
        if not subject:
           not_found("subject not found")

        db.delete(subject)
        db.commit()
        return {"message": "Subject deleted successfully"}