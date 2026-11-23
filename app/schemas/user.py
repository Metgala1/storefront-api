from pydantic import BaseModel, ConfigDict, Field


class UserUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=255,
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str = Field(validation_alias="UserRole")

    model_config = ConfigDict(from_attributes=True)