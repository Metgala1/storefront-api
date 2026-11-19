from datetime import UTC, datetime, timedelta
import secrets

import bcrypt
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.session import Session as UserSession
from app.models.user import User


SESSION_DURATION = timedelta(days=7)


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    password_matches = bcrypt.checkpw(
        password.encode("utf-8"),
        user.passwordHash.encode("utf-8"),
    )

    if not password_matches:
        return None

    return user


def create_user_session(db: Session, user_id: int) -> str:
    session_token = secrets.token_hex(32)

    expires_at = (
        datetime.now(UTC) + SESSION_DURATION
    ).replace(tzinfo=None)

    user_session = UserSession(
        id=session_token,
        userId=user_id,
        expiresAt=expires_at,
    )

    db.add(user_session)
    db.commit()

    return session_token


def get_user_from_session(
    db: Session,
    session_token: str,
) -> User | None:
    user_session = db.get(UserSession, session_token)

    if user_session is None:
        return None

    now = datetime.now(UTC).replace(tzinfo=None)

    if user_session.expiresAt <= now:
        db.delete(user_session)
        db.commit()
        return None

    return db.get(User, user_session.userId)


def delete_user_session(
    db: Session,
    session_token: str,
) -> None:
    user_session = db.get(UserSession, session_token)

    if user_session is not None:
        db.delete(user_session)
        db.commit()