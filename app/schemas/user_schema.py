from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str
    phone_no: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone_no: Optional[str]


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Address
class UserAddressBase(BaseModel):
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: str


class UserAddressCreate(UserAddressBase):
    pass


class UserAddress(UserAddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
