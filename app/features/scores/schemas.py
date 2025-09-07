from pydantic import BaseModel, ConfigDict


class AddScore(BaseModel):
    score: int


class ScoresOut(BaseModel):
    nickname: str
    score: int

    model_config = ConfigDict(from_attributes=True)
