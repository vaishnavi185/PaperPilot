from sqlalchemy.orm import Session

from schemes.Subject import SubjectCreate,SubjectResponse,SubjectUpdate
from service.subject_service import SubjectService


class SubjectController:

    @staticmethod
    def create_subject(subject_data: SubjectCreate, db: Session):
        return SubjectService.create_subject(subject_data, db)

    @staticmethod
    def get_all_subjects(db: Session):
        return SubjectService.get_all_subjects(db)

    @staticmethod
    def get_subject_by_id(subject_id: int, db: Session):
        return SubjectService.get_subject_by_id(subject_id, db)

    @staticmethod
    def update_subject(subject_id: int, subject_data: SubjectUpdate, db: Session):
        return SubjectService.update_subject(subject_id, subject_data, db)

    @staticmethod
    def delete_subject(subject_id: int, db: Session):
        return SubjectService.delete_subject(subject_id, db)