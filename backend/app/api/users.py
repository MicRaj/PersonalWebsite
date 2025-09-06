import datetime
import json
import os
import re
import shutil
import time
from pathlib import Path
from typing import List, Optional

import bcrypt
from dotenv import load_dotenv
from fastapi import (APIRouter, Cookie, Depends, File, HTTPException, Request,
                     Response, UploadFile, status)
from itsdangerous import TimestampSigner
from sqlmodel import Session, select, text

from app.core.database import SessionDep, get_session
from app.models.blog_post import BlogPost, BlogPostCreate, BlogPostUpdate
from app.models.session import SessionModel
from app.models.user import User, UserCreate, UserLogin

secret_file = Path("/run/secrets/backend_secret_key")
SECRET_KEY = secret_file.read_text().strip()
signer = TimestampSigner(SECRET_KEY)

router = APIRouter()


def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()
    return hashed


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def get_current_user(db: Session, session_id: str):
    print(f"session_id: {session_id}, type: {type(session_id)}")
    if not session_id:
        raise HTTPException(status_code=401, detail="Not logged in")

    try:
        unsigned_id = signer.unsign(session_id, max_age=86400).decode()
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=f"Invalid or expired session {session_id}, {e}",
        )

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
def create_user(user: UserCreate, db: SessionDep, session_id: str = Cookie(None)):
    user = get_current_user(db, session_id)
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to create users")
    existing_user = db.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
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
    user = db.exec(select(User).where(User.username == login.username)).first()
    if not user or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Check for existing session
    existing_session = db.exec(
        select(SessionModel).where(SessionModel.user_id == user.id)
    ).first()

    if existing_session:
        db.delete(existing_session)
        db.commit()

    session = SessionModel(user_id=user.id)
    db.add(session)
    db.commit()
    db.refresh(session)

    # Sign the session ID and set as HttpOnly cookie
    signed_session_id = signer.sign(session.id).decode()
    response.set_cookie(
        "session_id",
        signed_session_id,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=86400,  # 1 day
        path="/",
    )

    return {"message": "Login successful"}


@router.get("/me")
def read_me(db: SessionDep, session_id: str = Cookie(None)):
    user = get_current_user(db, session_id)
    return {"id": user.id, "username": user.username, "is_admin": user.is_admin}
