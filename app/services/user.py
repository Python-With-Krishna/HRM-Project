from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import user as user_crud
from app.schemas.user import UserCreate


async def create_user(db: AsyncSession, user_data: UserCreate):
    existing_user = await user_crud.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")
    new_user = await user_crud.create_user(db, user_data)
    return new_user

async def get_user_by_email(db: AsyncSession, email: str):
    user = await user_crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user