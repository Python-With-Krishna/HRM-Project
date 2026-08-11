from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

password_hash = PasswordHash.recommended()


def create_user(
    db: Session,
    user_data: UserCreate,
) -> User:

    hashed_password = password_hash.hash(
        user_data.password
    )

    user = User(
        username=user_data.username,
        hashed_password=hashed_password,
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_username(
    db: Session,
    username: str,
) -> User | None:

    statement = select(User).where(
        User.username == username
    )

    return db.scalar(statement)


def get_users(
    db: Session,
) -> list[User]:

    statement = select(User)

    return list(db.scalars(statement).all())