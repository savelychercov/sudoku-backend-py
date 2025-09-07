from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.features.users.deps import get_current_user
from app.features.scores.schemas import AddScore, ScoresOut
from app.features.scores import crud
from app.core.db import get_session
from app.features.users.schemas import UserOut
from typing import List

router = APIRouter(prefix="/scores", tags=["score"])


@router.post("/add", response_model=UserOut)
async def add_score(
        payload: AddScore,
        db: AsyncSession = Depends(get_session),
        current_user=Depends(get_current_user)):
    return await crud.update_score(db, current_user.id, payload.score)


@router.get("/all", response_model=List[ScoresOut])
async def get_all_scores(db: AsyncSession = Depends(get_session)):
    return await crud.get_all_scores(db)
