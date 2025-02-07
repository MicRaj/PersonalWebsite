from fastapi import APIRouter, File, UploadFile, Request
import datetime
import shutil

import json

from sqlmodel import Session, select, text

from app.models.yesno import YesNo
from app.core.database import SessionDep

router = APIRouter()

@router.post("/upload")
async def upload_answer(request: Request, db: SessionDep):
    answer = await request.body() 
    answer = answer.decode("utf-8")
    db.add(YesNo(timestamp=datetime.datetime.now(), answer=answer))
    db.commit()

@router.get(("/get"))
def get_answer(db: SessionDep):
    all_answers = db.exec(select(YesNo)).all()
    return all_answers