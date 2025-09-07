from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.features.users.models import User


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def get_user_by_nickname(db: AsyncSession, nickname: str):
    result = await db.execute(select(User).where(User.nickname == nickname))
    return result.scalars().first()


async def create_user(db: AsyncSession, nickname: str, password: str):
    user = User(nickname=nickname, hashed_password=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
