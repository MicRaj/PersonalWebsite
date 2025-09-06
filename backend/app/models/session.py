import secrets
import time

from sqlmodel import Field, SQLModel


class SessionModel(SQLModel, table=True):
    id: str = Field(default_factory=lambda: secrets.token_hex(16), primary_key=True)
    user_id: int
    created_at: int = Field(default_factory=lambda: int(time.time()))
    expires_at: int = Field(
        default_factory=lambda: int(time.time()) + 60 * 60 * 24
    )  # 1 day
