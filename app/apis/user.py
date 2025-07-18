# fastapi-app/api/user.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.user_model import UserModel
from app.schemas.user_schema import User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return UserModel.create_user(user)

@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100):
    return UserModel.get_users(skip, limit)

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = UserModel.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    updated_user = UserModel.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    success = UserModel.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return
