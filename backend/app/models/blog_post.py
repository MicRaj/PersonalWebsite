from sqlmodel import Field, SQLModel
from datetime import datetime
import time
from typing import Optional

class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: int = Field(default_factory=lambda: int(time.time()))
    title: str
    slug: str
    content_markdown: str