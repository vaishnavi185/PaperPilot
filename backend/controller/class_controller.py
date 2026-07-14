from sqlalchemy.orm import Session

from schemes.Class import ClassCreate, ClassUpdate
from service.Class_service import ClassService


class ClassController:

    @staticmethod
    def create_class(class_data: ClassCreate, db: Session):
        return ClassService.create_class(class_data, db)

    @staticmethod
    def get_all_classes(db: Session):
        return ClassService.get_all_classes(db)

    @staticmethod
    def get_class_by_id(class_id: int, db: Session):
        return ClassService.get_class_by_id(class_id, db)

    @staticmethod
    def update_class(class_id: int, class_data: ClassUpdate, db: Session):
        return ClassService.update_class(class_id, class_data, db)

    @staticmethod
    def delete_class(class_id: int, db: Session):
        return ClassService.delete_class(class_id, db)