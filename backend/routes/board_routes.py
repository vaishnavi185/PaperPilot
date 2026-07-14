
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies.auth import get_current_user
from database.connectivity import get_db
from controller.BoardController import BoardController
from schemes.board import (
    BoardCreate,
    BoardUpdate,
    BoardResponse
)

board_router = APIRouter(
    prefix="/boards",
    tags=["Boards"]
)


@board_router.post("/add-board", response_model=BoardResponse)
def create_board(
    board: BoardCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BoardController.create_board(board, db)


@board_router.get("/get-board", response_model=list[BoardResponse])
def get_all_boards(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BoardController.get_all_boards(db)


@board_router.get("/get_by_id/{board_id}", response_model=BoardResponse)
def get_board(
    board_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BoardController.get_board_by_id(board_id, db)


@board_router.put("/update-board/{board_id}", response_model=BoardResponse)
def update_board(
    board_id: int,
    board: BoardUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BoardController.update_board(board_id, board, db)


@board_router.delete("/delete-board/{board_id}")
def delete_board(
    board_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BoardController.delete_board(board_id, db)
