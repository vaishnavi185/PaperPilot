from sqlalchemy.orm import Session

from schemes.Syllabus import SyllabusCreate, SyllabusUpdate
from service.syllabus_serviec import SyllabusService


class SyllabusController:

    
    @staticmethod
    def create_syllabus(
    board_id: int,
    class_id: int,
    subject_id: int,
    academic_year: str,
    title: str,
    version: str,
    status: str,
    is_active: bool,
    file,
    db: Session,
    ):return SyllabusService.create_syllabus(
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

    @staticmethod
    def get_all_syllabi(db: Session):
        return SyllabusService.get_all_syllabi(db)

    @staticmethod
    def get_syllabus_by_id(syllabus_id: int, db: Session):
        return SyllabusService.get_syllabus_by_id(syllabus_id, db)

    @staticmethod
    def update_syllabus(syllabus_id: int, syllabus_data: SyllabusUpdate, db: Session):
        return SyllabusService.update_syllabus(syllabus_id, syllabus_data, db)

    @staticmethod
    def delete_syllabus(syllabus_id: int, db: Session):
        return SyllabusService.delete_syllabus(syllabus_id, db)