from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.configs.env import Settings
from src.configs.database import create_db_and_tables
from src.apis import api as routers
from src.utils.logger import logger_config

logger = logger_config(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    logger.info("Startup: triggered")

    yield

    logger.info("Shutdown: triggered")


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        lifespan=lifespan,
    )

    app.include_router(routers, prefix='/api')

    return app
