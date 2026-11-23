from fastapi import APIRouter

from app.core.dependencies import Current_User, DatabaseSession
from app.schemas.user import UserResponse, UserUpdate
from app.services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user: Current_User
):
    return current_user

@router.patch("/me", response_model=UserUpdate)
def update_my_profile(
    data: UserUpdate,
    db: DatabaseSession,
    current_user: Current_User
):
    return user_service.update_user(
        db,
        current_user,
        data
    )