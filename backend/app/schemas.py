from pydantic import BaseModel, EmailStr

from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    identification: str
    phone: str
    role: str
    medical_license: Optional[str] = None
    specialty: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    identification: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True
