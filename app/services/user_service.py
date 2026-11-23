from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserUpdate


def update_user(
    db: Session,
    user: User,
    data: UserUpdate
) -> User:
    update_data = data.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(user, field, value)
    
    db.commit()
    db.refresh()
    
    return user

