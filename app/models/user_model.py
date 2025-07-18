from fastapi import HTTPException, status
from typing import List, Optional
from ..database import get_supabase
from ..schemas.user_schema import UserCreate, UserUpdate, UserAddressCreate

supabase = get_supabase()

class UserModel:
    @staticmethod
    def get_users() -> List[dict]:
        res = supabase.table("users").select("*").execute()
        return res.data

    @staticmethod
    def get_user(user_id: int) -> Optional[dict]:
        res = supabase.table("users").select("*").eq("id", user_id).execute()
        return res.data[0] if res.data else None

    @staticmethod
    def create_user(user: UserCreate) -> dict:
        existing = supabase.table("users").select("*").eq("email", user.email).execute()
        if existing.data:
            raise HTTPException(status_code=400, detail="Email already registered")

        res = supabase.table("users").insert(user.dict()).execute()
        return res.data[0]

    @staticmethod
    def update_user(user_id: int, data: UserUpdate) -> Optional[dict]:
        update_data = data.dict(exclude_unset=True)
        res = supabase.table("users").update(update_data).eq("id", user_id).execute()
        return res.data[0] if res.data else None

    @staticmethod
    def delete_user(user_id: int) -> bool:
        supabase.table("users").delete().eq("id", user_id).execute()
        return True


class UserAddressModel:
    @staticmethod
    def create_address(user_id: int, address: UserAddressCreate) -> dict:
        data = address.dict()
        data["user_id"] = user_id
        res = supabase.table("user_addresses").insert(data).execute()
        return res.data[0]
