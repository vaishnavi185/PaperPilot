from fastapi import HTTPException, status


def not_found(message: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )


def bad_request(message: str):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )


def unauthorized(message: str = "Unauthorized"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message
    )
def conflict(message: str):
    raise HTTPException(status_code=409, detail=message)


def unprocessable_entity(message: str):
    raise HTTPException(status_code=422, detail=message)


def internal_server_error(message: str = "Internal Server Error"):
    raise HTTPException(status_code=500, detail=message)