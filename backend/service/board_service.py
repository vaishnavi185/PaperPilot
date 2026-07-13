from datetime import datetime
from sqlalchemy.orm import Session

from models.BoardType import Board
from schemes.board import BoardCreate, BoardUpdate


class BoardService:

    @staticmethod
    def create_board(board: BoardCreate, db: Session):
        new_board = Board(
            name=board.name,
            code=board.code,
            official_website=board.official_website,
            is_active=board.is_active
        )

        db.add(new_board)
        db.commit()
        db.refresh(new_board)

        return new_board

    @staticmethod
    def get_all_boards(db: Session):
        return (
            db.query(Board)
            .filter(Board.deleted_at == None)
            .all()
        )

    @staticmethod
    def get_board_by_id(board_id: int, db: Session):
        return (
            db.query(Board)
            .filter(
                Board.id == board_id,
                Board.deleted_at == None
            )
            .first()
        )

    @staticmethod
    def update_board(board_id: int, board: BoardUpdate, db: Session):
        db_board = (
            db.query(Board)
            .filter(
                Board.id == board_id,
                Board.deleted_at == None
            )
            .first()
        )

        if not db_board:
            return None

        update_data = board.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_board, key, value)

        db.commit()
        db.refresh(db_board)

        return db_board

    @staticmethod
    def delete_board(board_id: int, db: Session):
        db_board = (
            db.query(Board)
            .filter(
                Board.id == board_id,
                Board.deleted_at == None
            )
            .first()
        )

        if not db_board:
            return None

        db_board.deleted_at = datetime.utcnow()
        db_board.is_active = False

        db.commit()

        return {
            "message": "Board deleted successfully."
        }