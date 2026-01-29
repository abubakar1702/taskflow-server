from typing import Optional
from pydantic import BaseModel, EmailStr, computed_field
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str


class UserRead(UserBase):
    id: Optional[UUID] = None
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class UserInDB(UserRead):
    password_hash: str