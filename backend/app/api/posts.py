import datetime
import json
import re
import shutil
import time
from typing import List, Optional

from fastapi import APIRouter, File, HTTPException, Request, UploadFile
from sqlmodel import Session, select, text

from app.core.database import SessionDep
from app.models.blog_post import BlogPost, BlogPostCreate, BlogPostUpdate

router = APIRouter()


def sanitise_html(html: str) -> str:
    return html


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
        content=sanitise_html(post.content),
        slug=generate_unique_slug(post.title, db),
        cover_image=post.cover_image,
    )
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post


@router.get("/posts/", response_model=List[BlogPost])
def read_posts(db: SessionDep):
    return db.exec(select(BlogPost)).all()


@router.get("/posts/id/{post_id}", response_model=BlogPost)
def read_post(post_id: int, db: SessionDep):
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/posts/{post_slug}", response_model=BlogPost)
def read_post(post_slug: str, db: SessionDep):
    post = db.exec(select(BlogPost).where(BlogPost.slug == post_slug)).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/posts/{post_id}", response_model=BlogPost)
def update_post(
    post_id: int,
    updated_post: BlogPostUpdate,
    db: SessionDep,
):
    db_post = db.get(BlogPost, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    if updated_post.title is not None:
        db_post.title = updated_post.title
        db_post.slug = generate_unique_slug(updated_post.title, db)

    if updated_post.content is not None:
        db_post.content = sanitise_html(updated_post.content)

    if updated_post.cover_image is not None:
        db_post.cover_image = updated_post.cover_image

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
