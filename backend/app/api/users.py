import datetime
import json
import re
import shutil
import time
from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    Request,
    UploadFile,
    Response,
    status,
    Cookie,
)
from sqlmodel import Session, select, text

from app.core.database import SessionDep
from app.models.blog_post import BlogPost, BlogPostCreate, BlogPostUpdate
from backend.app.models.user import User, UserCreate, UserLogin
from backend.app.models.session import SessionModel
from backend.app.core.database import get_session
from itsdangerous import TimestampSigner


SECRET_KEY = "super-secret"  # load from env in real app
signer = TimestampSigner(SECRET_KEY)

router = APIRouter()


def hash_password(password: str) -> str:
    return password  # Replace with actual hashing logic


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return plain_password == hashed_password  # Replace with actual verification logic


def get_current_user(
    session_id: str = Cookie(None), db: SessionDep = Depends(get_session)
):
    if not session_id:
        raise HTTPException(status_code=401, detail="Not logged in")

    try:
        unsigned_id = signer.unsign(session_id, max_age=86400).decode()
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    session_obj = db.get(SessionModel, unsigned_id)
    if not session_obj or session_obj.expires_at < time.time():
        raise HTTPException(status_code=401, detail="Session expired")

    user = db.get(User, session_obj.user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def cleanup_expired_sessions(db: Session):
    now = int(time.time())
    expired_sessions = db.exec(
        select(SessionModel).where(SessionModel.expires_at < now)
    ).all()

    for session in expired_sessions:
        db.delete(session)

    db.commit()

    return len(expired_sessions)


@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: SessionDep):
    existing_user = db.exec(select(User).where(User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login/")
def login_attempt(login: UserLogin, response: Response, db: SessionDep):
    user = db.exec(select(User).where(User.email == login.email)).first()
    if not user or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    session = SessionModel(user_id=user.id)
    db.add(session)
    db.commit()
    db.refresh(session)

    # Check for existing session
    existing_session = db.exec(
        select(SessionModel).where(SessionModel.user_id == user.id)
    ).first()

    if existing_session:
        db.delete(existing_session)
        db.commit()

    # Sign the session ID and set as HttpOnly cookie
    signed_session_id = signer.sign(session.id).decode()
    response.set_cookie(
        "session_id",
        signed_session_id,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=86400,  # 1 day
    )

    return {"message": "Login successful"}


@router.get("/me")
def read_me(user=Depends(get_current_user)):
    return {"id": user.id, "Username": user.username}
