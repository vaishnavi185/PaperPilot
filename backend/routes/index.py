from fastapi import APIRouter

from routes.auth_rountes import auth_route
from routes.role_routes import role_router
from routes.board_routes import board_router
from routes.class_routes import class_router
from routes.subject_route import subject_router

api_router = APIRouter()

api_router.include_router(auth_route)
api_router.include_router(role_router)
api_router.include_router(board_router)
api_router.include_router(class_router)
api_router.include_router(subject_router)