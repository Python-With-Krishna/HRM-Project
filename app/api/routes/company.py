from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.company import CompanyCreate
from app.services.company import create_company as create_company_service

router = APIRouter(prefix="/companies", tags=["companies"])

@router.post("/")
async def create_company_endpoint(
    company_data: CompanyCreate,
    db: AsyncSession = Depends(get_db),  # noqa: B008
):
    return await create_company_service(db, company_data)
