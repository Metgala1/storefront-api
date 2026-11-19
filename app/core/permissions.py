from collections.abc import Callable

from fastapi import Depends, HTTPException, status

from app.core.dependencies import get_current_user
from app.models.enums import UserRole
from app.models.user import User


def require_role(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user)
    ) -> User:
        if current_user.UserRole not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't habe the persmission to perform this action"
            )
        
        return current_user
    
    return role_checker

require_admin = require_role(UserRole.ADMIN)
require_customer = require_role(UserRole.CUSTOMER)