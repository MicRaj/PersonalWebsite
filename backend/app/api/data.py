from fastapi import APIRouter, File, UploadFile, Request, HTTPException

import datetime
import shutil

import json

from sqlmodel import Session, select, text

from app.models.blog_post import BlogPost
from app.core.database import SessionDep
from typing import List
router = APIRouter()

#Upload post
#Posts by ID
#Top 10 posts latest and their slugs
@router.post("/posts/", response_model=BlogPost)
def create_post(post: BlogPost, db: SessionDep):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.post("/posts/upload_markdown/", response_model=BlogPost)
def upload_markdown(
    title: str,
    slug: str,
    db: SessionDep,
    file: UploadFile = File(...),
    
):
    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only markdown files (.md) are supported.")

    content = file.file.read().decode("utf-8")

    post = BlogPost(
        title=title,
        slug=slug,
        content_markdown=content,
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post

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
def update_post(post_id: int, updated_post: BlogPost, db: SessionDep):
    db_post = db.get(BlogPost, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_post.title = updated_post.title
    db_post.slug = updated_post.slug
    db_post.content_markdown = updated_post.content_markdown
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
