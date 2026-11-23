from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.dependencies import Current_User
from app.database.session import get_db
from app.schemas.auth import LoginRequest, UserResponse
from app.services.auth_service import (
    authenticate_user,
    create_user_session,
    delete_user_session,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

DatabaseSession = Annotated[Session, Depends(get_db)]

SESSION_COOKIE = "session"
SESSION_MAX_AGE = 7 * 24 * 60 * 60


@router.post("/login", response_model=UserResponse)
def login(
    data: LoginRequest,
    response: Response,
    db: DatabaseSession,
):
    user = authenticate_user(
        db,
        data.email,
        data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    session_token = create_user_session(db, user.id)

    response.set_cookie(
        key=SESSION_COOKIE,
        value=session_token,
        max_age=SESSION_MAX_AGE,
        httponly=True,
        secure=settings.APP_ENV == "production",
        samesite="lax",
        path="/",
    )

    return user


@router.get("/me", response_model=UserResponse)
def get_me(user: Current_User):
    return user


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    request: Request,
    response: Response,
    db: DatabaseSession,
) -> None:
    session_token = request.cookies.get(SESSION_COOKIE)

    if session_token:
        delete_user_session(db, session_token)

    response.delete_cookie(
        key=SESSION_COOKIE,
        path="/",
        httponly=True,
        secure=settings.APP_ENV == "production",
        samesite="lax",
    )