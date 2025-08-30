from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
import time


class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: int = Field(default_factory=lambda: int(time.time()))
    title: str
    slug: str = Field(index=True, unique=True)
    content: str
    cover_image: str  # Path to image file, .etc '/hamster_neutral.jpg'


class BlogPostCreate(BaseModel):
    title: str
    content: str
    cover_image: str


class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    cover_image: Optional[str] = None
