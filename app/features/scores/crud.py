from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.features.users.models import User
from app.features.users import crud as users_crud


async def get_all_scores(db: AsyncSession):
    result = await db.execute(select(User).order_by(User.score.desc()))
    return result.scalars().all()


async def update_score(db: AsyncSession, user_id: int, score: int):
    user = await users_crud.get_user_by_id(db, user_id)
    user.score += score
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
