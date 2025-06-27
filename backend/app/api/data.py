from fastapi import APIRouter, File, UploadFile, Request, HTTPException

import datetime
import shutil
import time
import re

import json

from sqlmodel import Session, select, text

from app.models.blog_post import BlogPost, BlogPostCreate, BlogPostUpdate
from app.core.database import SessionDep
from typing import List

router = APIRouter()


def generate_unique_slug(title: str, db: Session) -> str:
    # Slugify title (basic version; you can improve with unidecode or slugify lib)
    base_slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    slug = base_slug
    counter = 1
    while db.exec(select(BlogPost).where(BlogPost.slug == slug)).first():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


@router.post("/posts/create_post", response_model=BlogPost)
def create_post(post: BlogPostCreate, db: SessionDep):
    created_post = BlogPost(
        title=post.title,
        content=post.content,
        slug=generate_unique_slug(post.title, db),
    )
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post


@router.get("/posts/", response_model=List[BlogPost])
def read_posts(db: SessionDep):
    return db.exec(select(BlogPost)).all()


@router.get("/posts/{post_id}", response_model=BlogPost)
def read_post(post_id: int, db: SessionDep):
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/posts/{post_id}", response_model=BlogPost)
def update_post(post_id: int, updated_post: BlogPostUpdate, db: SessionDep):
    db_post = db.get(BlogPost, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_post.title = updated_post.title
    db_post.slug = updated_post.title.lower().replace(" ", "-")
    db_post.content = updated_post.content
    db_post.timestamp = int(time.time())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: SessionDep):
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted"}
