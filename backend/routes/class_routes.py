from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.class_controller import ClassController
from database.connectivity import get_db
from dependencies.auth import get_current_user
from schemes.Class import (
    ClassCreate,
    ClassUpdate,
    ClassResponse,
)

class_router = APIRouter(
    prefix="/classes",
    tags=["Classes"]
)


@class_router.post("/add-class", response_model=ClassResponse)
def create_class(
    class_data: ClassCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ClassController.create_class(class_data, db)


@class_router.get("/get-class", response_model=list[ClassResponse])
def get_all_classes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ClassController.get_all_classes(db)


@class_router.get("/get_by_id/{class_id}", response_model=ClassResponse)
def get_class(
    class_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ClassController.get_class_by_id(class_id, db)


@class_router.put("/update-class/{class_id}", response_model=ClassResponse)
def update_class(
    class_id: int,
    class_data: ClassUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ClassController.update_class(class_id, class_data, db)


@class_router.delete("/delete-class/{class_id}")
def delete_class(
    class_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ClassController.delete_class(class_id, db)