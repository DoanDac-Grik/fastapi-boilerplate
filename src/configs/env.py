from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: Literal["development", "staging", "production"] = "development"
    PROJECT_NAME: str = "ToDo Apis"
    DATABASE_URI: str
    HOST: str = "localhost"
    PORT: int

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()


class TestSettings(Settings):
    class Config:
        case_sensitive = True


test_settings = TestSettings()
