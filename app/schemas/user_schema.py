from pydantic import BaseModel
from typing import Optional  

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    full_name: Optional[str] = None

class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class User(UserBase):
    id: int
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

    class Config:
        from_attributes = True  