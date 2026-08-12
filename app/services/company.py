from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import company as company_crud
from app.schemas.company import CompanyCreate


async def create_company(db: AsyncSession, company_data: CompanyCreate):
    existing_company = await company_crud.get_company_by_email(db, company_data.email)
    if existing_company:
        raise HTTPException(status_code=400, detail="Company with this email already exists.")

    company=await company_crud.create_company(db, company_data)
    return company