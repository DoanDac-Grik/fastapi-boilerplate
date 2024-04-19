from fastapi import APIRouter, status
router = APIRouter()

@router.get(
    "/ping",
    status_code=status.HTTP_200_OK,
)
def check_health():
    return "pong"


