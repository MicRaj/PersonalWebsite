import time
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: int = Field(default_factory=lambda: int(time.time()))
    title: str
    slug: str = Field(index=True, unique=True)
    content: str
    cover_image: str  # Path to image file, .etc '/hamster_neutral.jpg'
    user_id: int = Field(foreign_key="user.id")


class BlogPostCreate(BaseModel):
    title: str
    content: str
    cover_image: str


class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    cover_image: Optional[str] = None
