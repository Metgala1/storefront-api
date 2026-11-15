from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: str = Field(
        min_length=1,
        max_length=100,
        description="Product's name",
        examples=["MacBook Air"],
    )
    category: str = Field(
        min_length=1,
        max_length=100,
        description="Product's category",
        examples=["computers"],
    )
    price: float = Field(
        gt=0,
        description="Product's price",
        examples=[1200],
    )
    quantity: int = Field(
        default=0,
        ge=0,
        description="Units in stock",
        examples=[10],
    )
    description: str = Field(
        default="",
        max_length=500,
        description="Product's description",
        examples=["Best student laptop"],
    )


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    """PUT: full replacement."""


class ProductPatch(BaseModel):
    """PATCH: every field optional."""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=1, max_length=100)
    category: str | None = Field(default=None, min_length=1, max_length=100)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)
    description: str | None = Field(default=None, max_length=500)


class Product(ProductBase):
    id: int
    
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: str

class ProductListResponse(BaseModel):
    count: int
    total: int
    skip: int
    limit: int
    products: list[ProductResponse]

class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str

class ProductWithCategoryResponse(BaseModel):
    id: int
    name: str
    price: float
    category: CategoryResponse


class ProductNotFoundException(Exception):
    pass