from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    nickname: str
    password: str


class UserOut(BaseModel):
    id: int
    nickname: str
    is_active: bool
    is_superuser: bool
    score: int

    model_config = ConfigDict(from_attributes=True)
