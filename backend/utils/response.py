from fastapi import status
from fastapi.responses import JSONResponse


def success_response(
    message: str,
    data=None,
    status_code: int = status.HTTP_200_OK
):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data,
        },
    )