from fastapi import HTTPException
from exceptions.httpexception import bad_request, not_found
from sqlalchemy.orm import Session

from models.Class import Class
from schemes.Class import ClassCreate, ClassUpdate



class ClassService:

    @staticmethod
    def create_class(class_data: ClassCreate, db: Session):
        existing = db.query(Class).filter(Class.code == class_data.code).first()
        if existing:
           bad_request("Class with this code already exists")

        new_class = Class(**class_data.model_dump())
        db.add(new_class)
        db.commit()
        db.refresh(new_class)
        return new_class

    @staticmethod
    def get_all_classes(db: Session):
        return db.query(Class).all()

    @staticmethod
    def get_class_by_id(class_id: int, db: Session):
        class_obj = db.query(Class).filter(Class.id == class_id).first()
        if not class_obj:
            not_found("Class not found")
        return class_obj

    @staticmethod
    def update_class(class_id: int, class_data: ClassUpdate, db: Session):
        class_obj = db.query(Class).filter(Class.id == class_id).first()
        if not class_obj:
            not_found("Class not found")

        for key, value in class_data.model_dump(exclude_unset=True).items():
            setattr(class_obj, key, value)

        db.commit()
        db.refresh(class_obj)
        return class_obj

    @staticmethod
    def delete_class(class_id: int, db: Session):
        class_obj = db.query(Class).filter(Class.id == class_id).first()
        if not class_obj:
            bad_request("Class not found")

        db.delete(class_obj)
        db.commit()
        return {"message": "Class deleted successfully"}