from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    password: str
    


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    is_active: bool
    updated_at: datetime

    model_config = {"from_attributes": True}
