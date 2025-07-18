from typing import List, Optional
from fastapi import HTTPException, status
from ..database import get_supabase
from ..schemas.user_schema import User, UserCreate, UserUpdate

supabase = get_supabase()


class UserModel:

    @staticmethod
    def get_users(skip: int = 0, limit: int = 100) -> List[User]:
        users = supabase.table("users").select("*").range(skip, skip +
                                                          limit).execute()
        return users.data

    @staticmethod
    def get_user(user_id: int) -> Optional[User]:
        user = supabase.table("users").select("*").eq("id", user_id).execute()
        return user.data[0] if user.data else None

    @staticmethod
    def create_user(user: UserCreate) -> User:
        existing_user = supabase.table("users").select("*").eq(
            "email", user.email).execute()
        if existing_user.data:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Email already registered")

        try:
            user_data = user.model_dump()
        except AttributeError:
            user_data = user.dict()

        new_user = supabase.table("users").insert(user_data).execute()
        return new_user.data[0]

    @staticmethod
    def update_user(user_id: int, user: UserUpdate) -> Optional[User]:
        existing_user = supabase.table("users").select("*").eq(
            "id", user_id).execute()
        if not existing_user.data:
            return None

        try:
            update_data = user.model_dump(exclude_unset=True)
        except AttributeError:
            update_data = user.dict(exclude_unset=True)

        updated_user = supabase.table("users").update(update_data).eq(
            "id", user_id).execute()
        return updated_user.data[0]

    @staticmethod
    def delete_user(user_id: int) -> bool:
        existing_user = supabase.table("users").select("*").eq(
            "id", user_id).execute()
        if not existing_user.data:
            return False

        supabase.table("users").delete().eq("id", user_id).execute()
        return True
