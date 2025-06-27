from sqlmodel import Field, SQLModel
from datetime import datetime
import time
from typing import Optional
from pydantic import BaseModel


class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: Optional[int] = Field(default_factory=lambda: int(time.time()))
    title: str
    slug: str = Field(index=True, unique=True)
    content: str


class BlogPostCreate(BaseModel):
    title: str
    content: str


class BlogPostUpdate(BaseModel):
    title: str
    content: str
