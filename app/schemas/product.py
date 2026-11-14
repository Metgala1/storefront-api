from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    category: str
    quantity: int
    description: str


class ProductUpdate(BaseModel):
    name: str
    price: float
    category: str
    quantity: int
    description: str


class ProductPatch(BaseModel):
    name: str | None = None
    price: float | None = None
    category: str | None = None
    quantity: int | None = None
    description: str | None = None