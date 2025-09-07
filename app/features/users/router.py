from fastapi import APIRouter, Depends
from app.features.users.deps import get_current_user
from app.features.users.schemas import UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user
