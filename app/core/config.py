from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "sudoku_app_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str | None = None
    ROOT_PATH: str = ""
    SECRET_KEY: str = "change-me-in-prod"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
if not settings.DATABASE_URL:
    settings.DATABASE_URL = (
        f"postgresql+asyncpg://{settings.POSTGRES_USER}:"
        f"{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:"
        f"{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    )
