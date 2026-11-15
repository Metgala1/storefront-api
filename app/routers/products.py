from fastapi import APIRouter, status

from app.dependencies.auth import AdminUser
from app.dependencies.pagination import Pagination
from app.schemas.product import (
    ProductCreate,
    ProductListResponse,
    ProductNotFoundException,
    ProductPatch,
    ProductResponse,
    ProductUpdate,
)

router = APIRouter(tags=["Products"])

products: list[dict] = [
    {
        "id": 1,
        "name": "MacBook Air",
        "category": "computers",
        "price": 1200,
        "quantity": 10,
        "description": "Lightweight laptop with all-day battery life, ideal for everyday work and travel.",
    },
    {
        "id": 2,
        "name": "iPhone 17",
        "category": "phones",
        "price": 900,
        "quantity": 25,
        "description": "Apple's latest smartphone with a sharp display and a powerful camera system.",
    },
    {
        "id": 3,
        "name": "MacBook Pro",
        "category": "computers",
        "price": 2000,
        "quantity": 5,
        "description": "High-performance laptop built for developers, designers, and video editing.",
    },
    {
        "id": 4,
        "name": "Samsung Galaxy",
        "category": "phones",
        "price": 850,
        "quantity": 15,
        "description": "Android flagship with a bright AMOLED screen and versatile camera setup.",
    },
    {
        "id": 5,
        "name": "iPad Air",
        "category": "tablets",
        "price": 600,
        "quantity": 8,
        "description": "Slim, powerful tablet for drawing, note-taking, and entertainment.",
    },
]


def find_index(product_id: int) -> int:
    for index, product in enumerate(products):
        if product["id"] == product_id:
            return index
    raise ProductNotFoundException()


@router.get("", response_model=ProductListResponse)
def get_products(
    pagination: Pagination,
    category: str | None = None,
    search: str | None = None,
):
    result = products

    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]
    if search:
        result = [p for p in result if search.lower() in p["name"].lower()]

    skip, limit = pagination["skip"], pagination["limit"]
    page = result[skip : skip + limit]

    return {
        "count": len(page),
        "total": len(result),
        "skip": skip,
        "limit": limit,
        "products": page,
    }


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(product_id: int):
    return products[find_index(product_id)]


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate, admin: AdminUser):
    new_id = max((p["id"] for p in products), default=0) + 1
    new_product = {"id": new_id, **data.model_dump()}
    products.append(new_product)
    return new_product


@router.put("/{product_id}", response_model=ProductResponse)
def replace_product(product_id: int, data: ProductUpdate, admin: AdminUser):
    index = find_index(product_id)
    products[index] = {"id": product_id, **data.model_dump()}
    return products[index]


@router.patch("/{product_id}", response_model=ProductResponse)
def edit_product(product_id: int, data: ProductPatch, admin: AdminUser):
    index = find_index(product_id)
    products[index].update(data.model_dump(exclude_unset=True))
    return products[index]


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, admin: AdminUser):
    products.pop(find_index(product_id))