from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connectivity import get_db
from controller.role_controller import RoleController
from schemes.Role import RoleCreate, RoleResponse,RoleUpdate

role_router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@role_router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return RoleController.create_role(role, db)

@role_router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return RoleController.get_all_roles(db)


# @router.get("/{role_id}", response_model=RoleResponse)
# def get_role(role_id: int, db: Session = Depends(get_db)):
#     return RoleController.get_role(role_id, db)


@role_router.put("/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    return RoleController.update_role(role_id, role, db)


@role_router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    return RoleController.delete_role(role_id, db)