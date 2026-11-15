from typing import Annotated

from fastapi import Depends, Header, HTTPException, status


FAKE_USERS = {
    "admin-token": {"id": 1, "username": "admin", "role": "admin"},
    "user-token": {"id": 2, "username": "alice", "role": "user"},
}


def get_current_user(x_token: Annotated[str | None, Header()] = None) -> dict:
    user = FAKE_USERS.get(x_token) if x_token else None
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return user


CurrentUser = Annotated[dict, Depends(get_current_user)]


def get_current_admin(user: CurrentUser) -> dict:
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only an admin can perform this task",
        )
    return user


AdminUser = Annotated[dict, Depends(get_current_admin)]