import uvicorn

from src.app import create_app
from src.configs.env import settings

api = create_app(settings)

if __name__ == "__main__":
    uvicorn.run("asgi:api", host=settings.HOST, port=settings.PORT, reload=True)
