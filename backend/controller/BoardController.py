from sqlalchemy.orm import Session

from schemes.board import BoardCreate, BoardUpdate
from service.board_service import BoardService


class BoardController:

    @staticmethod
    def create_board(board: BoardCreate, db: Session):
        return BoardService.create_board(board, db)

    @staticmethod
    def get_all_boards(db: Session):
        return BoardService.get_all_boards(db)

    @staticmethod
    def get_board_by_id(board_id: int, db: Session):
        return BoardService.get_board_by_id(board_id, db)

    @staticmethod
    def update_board(board_id: int, board: BoardUpdate, db: Session):
        return BoardService.update_board(board_id, board, db)

    @staticmethod
    def delete_board(board_id: int, db: Session):
        return BoardService.delete_board(board_id, db)