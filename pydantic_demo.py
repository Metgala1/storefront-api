from pydantic import BaseModel, ValidationError, Field, ConfigDict

class ProductCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    name: str = Field(
        min_length=1,
        max_length=100,
        description="The product's display name",
        examples=["Macbook air"]
        )
    price: float = Field(
        gt=0,
        description="The product's selling price"
        )
    quantity: int = Field(ge=0)

dir()

try:
    product = ProductCreate(
    name="MacBook Air",
    price="1099.99",
    quantity="1"
    )
    print(product.name)
    print(product.price)
    print(type(product.model_dump()))
    print(type(product.model_dump_json()))
except ValidationError as error:
    print(error)

