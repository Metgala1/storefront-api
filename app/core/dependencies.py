from typing import Annotated
from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.services.auth_service import get_user_from_session

DatabaseSession = Annotated[Session, Depends(get_db)]

def get_current_user(
    request: Request,
    db: DatabaseSession
) -> User:
    session_token = request.cookies.get("session")
    
    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
    
    user = get_user_from_session(db, session_token)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session"
        )
    
    return user

Current_User = Annotated[User, Depends(get_current_user)]