from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import engine
from app.core.logger import setup_logging
from app.features.users.models import Base
import logging
from app.features.users import router as users_router
from app.features.auth import router as auth_router
from app.features.slash import router as slash_router
from app.features.scores import router as scores_router
from app.core.config import settings

logger = setup_logging(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan, root_path=settings.ROOT_PATH, title="Sudoku API v1", version="1.0.0")

app.include_router(users_router.router)
app.include_router(auth_router.router)
app.include_router(slash_router.router)
app.include_router(scores_router.router)
