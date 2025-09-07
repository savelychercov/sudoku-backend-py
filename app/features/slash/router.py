from fastapi import APIRouter, Depends
from typing import Literal

router = APIRouter(tags=["slash"])


@router.get("/", response_model=Literal["API is running"])
async def get_slash():
    return "API is running"
