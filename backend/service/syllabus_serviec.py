from datetime import datetime
import tempfile

from sqlalchemy.orm import Session

from models.Syllabus import Syllabus
from schemes.Syllabus import SyllabusUpdate
from exceptions.httpexception import not_found
from utils.pdf_extractor import extract_text_from_pdf

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
        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.file.read())
            temp_path = temp_file.name

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(temp_path)

        # Check extracted text
        print(extracted_text)

        # Reset file pointer before uploading to Cloudinary
        file.file.seek(0)

        # Upload to Cloudinary
        upload_result = cloudinary.uploader.upload(
            file.file,
            folder="syllabus",
            resource_type="raw",
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
            raise not_found("Syllabus not found")

        return syllabus

    @staticmethod
    def update_syllabus(
        syllabus_id: int,
        syllabus_data: SyllabusUpdate,
        db: Session,
    ):
        syllabus = db.query(Syllabus).filter(Syllabus.id == syllabus_id).first()

        if not syllabus:
            raise not_found("Syllabus not found")

        for key, value in syllabus_data.model_dump(exclude_unset=True).items():
            setattr(syllabus, key, value)

        db.commit()
        db.refresh(syllabus)

        return syllabus

    @staticmethod
    def delete_syllabus(syllabus_id: int, db: Session):
        syllabus = db.query(Syllabus).filter(Syllabus.id == syllabus_id).first()

        if not syllabus:
            raise not_found("Syllabus not found")

        syllabus.deleted_at = datetime.utcnow()
        syllabus.is_active = False

        db.commit()
        db.refresh(syllabus)

        return {"message": "Syllabus deleted successfully"}