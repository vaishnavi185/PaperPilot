from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.Role import Role
from schemes.Role import RoleCreate,RoleUpdate


class RoleController:

    @staticmethod
    def create_role(role: RoleCreate, db: Session):

        db_role = db.query(Role).filter(Role.name == role.name).first()

        if db_role:
            return {"message": "Role already exists"}

        new_role = Role(
            name=role.name,
            #description=role.description
        )

        db.add(new_role)
        db.commit()
        db.refresh(new_role)

        return new_role
    
    def get_all_roles(db: Session):

        return db.query(Role).all()
    def update_role(role_id: int, role_data: RoleUpdate, db: Session):

        role = db.query(Role).filter(Role.id == role_id).first()

        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        role.name = role_data.name
        role.description = role_data.description

        db.commit()
        db.refresh(role)

        return role
    def delete_role(role_id: int, db: Session):

        role = db.query(Role).filter(Role.id == role_id).first()

        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        db.delete(role)
        db.commit()

        return {"message": "Role deleted successfully"}