from fastapi import APIRouter, Depends

from src.apis.ping import routers as health_check
from src.apis.tasks import routers as tasks
from src.apis.users import routers as users

api = APIRouter()

api.include_router(
    health_check.router,
    tags=["Health Check"],
)
api.include_router(
    tasks.router,
    tags=["Task"],
)

api.include_router(
    users.router,
    tags=["User"],
)

