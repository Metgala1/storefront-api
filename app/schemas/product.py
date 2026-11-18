from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    price: float = Field(ge=0)
    rating: float = Field(ge=1, le=5)
    reviewsCount: int = Field(ge=0)
    description: str
    specs: list[str]
    image: str
    quantity: int = Field(ge=0)
    categoryId: int = Field(gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    price: float | None = Field(default=None, ge=0)
    rating: float | None = Field(default=None, ge=1, le=5)
    reviewsCount: int | None = Field(default=None, ge=0)
    description: str | None = None
    specs: list[str] | None = None
    image: str | None = None
    quantity: int | None = Field(default=None, ge=0)
    categoryId: int | None = Field(default=None, gt=0)


class ProductResponse(ProductBase):
    id: int
    createdAt: datetime
    updatedAt: datetime

    model_config = ConfigDict(from_attributes=True)