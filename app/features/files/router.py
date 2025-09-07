import shutil

from fastapi import APIRouter, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/files", tags=["files"])

game_file = "./SudokuGame.exe"
upload_password = "upload"


@router.get("/game")
async def return_game_file():
    if not os.path.exists(game_file):
        raise HTTPException(status_code=404, detail="Game file not found")
    return FileResponse(path=game_file, filename="SudokuGame.exe", media_type="application/octet-stream")


@router.post("/upload")
async def upload_game_file(
        password: str = Form(...),
        file: UploadFile = File(...),
):
    if password != upload_password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    try:
        with open(game_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    return {"status": "success", "saved_as": game_file}
