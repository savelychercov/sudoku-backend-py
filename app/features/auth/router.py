from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.core.security import verify_password, create_access_token
from app.features.users import crud, schemas as user_schemas
from app.features.auth.schemas import Token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=user_schemas.UserOut)
async def signup(payload: user_schemas.UserCreate, db: AsyncSession = Depends(get_session)):
    existing = await crud.get_user_by_nickname(db, payload.nickname)
    if existing:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    return await crud.create_user(db, payload.nickname, payload.password)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: AsyncSession = Depends(get_session)):
    user = await crud.get_user_by_nickname(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    token = create_access_token(subject=user.nickname)
    return {"access_token": token, "token_type": "bearer"}
