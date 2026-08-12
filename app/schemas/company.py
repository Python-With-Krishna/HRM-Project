from pydantic import BaseModel, EmailStr


class CompanyCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None
    is_active: bool

    model_config = {"from_attributes": True}
