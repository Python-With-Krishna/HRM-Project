from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyResponse


async def create_company(db: AsyncSession,company_data: CompanyCreate,) -> CompanyResponse:
    company = Company(
        name=company_data.name,
        email=company_data.email,
        phone=company_data.phone,
        address=company_data.address,
    )

    db.add(company)
    await db.commit()
    await db.refresh(company)

    return CompanyResponse.model_validate(company)

async def get_company_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(Company).where(Company.email == email))
    return result.scalar_one_or_none()