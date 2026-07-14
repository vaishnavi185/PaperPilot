from sqlalchemy.orm import Session

from models.Syllabus import Syllabus
from schemes.Syllabus import SyllabusUpdate
from exceptions.httpexception import not_found
import cloudinary.uploader
import config.cloudinary


class SyllabusService:

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
    ):
        # TODO: Save uploaded file and replace this with the actual path
        upload_result = cloudinary.uploader.upload(
        file.file,
        folder="syllabus",
        resource_type="raw"
        )

        file_url = upload_result.get("secure_url")

        new_syllabus = Syllabus(
            board_id=board_id,
            class_id=class_id,
            subject_id=subject_id,
            academic_year=academic_year,
            title=title,
            version=version,
            file_url=file_url,
            status=status,
            is_active=is_active,
        )

        db.add(new_syllabus)
        db.commit()
        db.refresh(new_syllabus)

        return new_syllabus

    @staticmethod
    def get_all_syllabi(db: Session):
        return db.query(Syllabus).all()

    @staticmethod
    def get_syllabus_by_id(syllabus_id: int, db: Session):
        syllabus = db.query(Syllabus).filter(Syllabus.id == syllabus_id).first()

        if not syllabus:
            not_found("Syllabus not found")

        return syllabus

    @staticmethod
    def update_syllabus(
        syllabus_id: int,
        syllabus_data: SyllabusUpdate,
        db: Session,
    ):
        syllabus = db.query(Syllabus).filter(Syllabus.id == syllabus_id).first()

        if not syllabus:
            not_found("Syllabus not found")

        for key, value in syllabus_data.model_dump(exclude_unset=True).items():
            setattr(syllabus, key, value)

        db.commit()
        db.refresh(syllabus)

        return syllabus

    @staticmethod
    def delete_syllabus(syllabus_id: int, db: Session):
        syllabus = db.query(Syllabus).filter(Syllabus.id == syllabus_id).first()

        if not syllabus:
            not_found("Syllabus not found")

        db.delete(syllabus)
        db.commit()

        return {"message": "Syllabus deleted successfully"}