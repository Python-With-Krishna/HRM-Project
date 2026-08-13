from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


async def create_user(db: AsyncSession,user_data: UserCreate,) -> UserResponse:
    user = User(
        name=user_data.name,
        email=user_data.email,
        phone=user_data.phone,
        password=user_data.password,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return UserResponse.model_validate(user)

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()