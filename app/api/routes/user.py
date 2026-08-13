from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.user import UserCreate
from app.services.user import create_user, get_user_by_email

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def create_user_endpoint(user_data: UserCreate, db: AsyncSession = Depends(get_db), ): # noqa: B008
    return await create_user(db, user_data)

@router.get("/{email}")
async def get_user_by_email_endpoint(email: str, db: AsyncSession = Depends(get_db)): # noqa: B008
    return await get_user_by_email(db, email)
