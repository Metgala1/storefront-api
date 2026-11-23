from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import UserRole as UserRoleEnum


class LoginRequest(BaseModel):
    email: str = Field(min_length=3, max_length=320)
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRoleEnum = Field(validation_alias="UserRole")
    model_config = ConfigDict(from_attributes=True)