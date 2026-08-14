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
    
    
    
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None



class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class loginResponse(BaseModel):
    message: str
    email: EmailStr

    model_config = {"from_attributes": True}
