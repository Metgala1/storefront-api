from fastapi import APIRouter
from app.schemas.users import UserResponse

router = APIRouter(tags=["Users"])

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Roger",
        "email": "roger@example.com",
        "role": "CUSTOMER",
        "password_hash": "secret_hash_value"
    }
