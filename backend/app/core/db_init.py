import os
from pathlib import Path

import bcrypt
from sqlmodel import select

from app.core.database import get_session
from app.models.user import User

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
secret_file = Path("/run/secrets/admin_password")
ADMIN_PASSWORD = secret_file.read_text().strip()
print(f"ADMIN_USERNAME: {ADMIN_USERNAME}, ADMIN_PASSWORD: {ADMIN_PASSWORD}")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def create_initial_admin():
    db = next(get_session())
    existing_admin = db.exec(
        select(User).where(User.username == ADMIN_USERNAME)
    ).first()
    if not existing_admin:
        admin_user = User(
            username=ADMIN_USERNAME,
            hashed_password=hash_password(ADMIN_PASSWORD),
            is_admin=True,
        )
        db.add(admin_user)
        db.commit()
        print(f"Admin user '{ADMIN_USERNAME}' created.")
    else:
        print(f"Admin user '{ADMIN_USERNAME}' already exists.")


if __name__ == "__main__":
    create_initial_admin()
