from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str


class UserCreate(BaseModel):
    username: str
    password: str
