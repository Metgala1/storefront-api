from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundException
from app.core.permissions import require_admin
from app.database.session import get_db
from app.models.user import User
from app.schemas.product import (
    ProductCreate,
    ProductPage,
    ProductResponse,
    ProductUpdate,
)
from app.services import product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=ProductPage)
def list_products(
    db: DatabaseSession,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    search: str | None = Query(default=None, min_length=1, max_length=100),
    category_id: int | None = Query(default=None, gt=0),
    sort_by: str = Query(
        default="id",
        pattern="^(id|name|price|rating|createdAt)$",
    ),
    sort_order: str = Query(
        default="desc",
        pattern="^(asc|desc)$",
    ),
):
    products, total = product_service.get_products(
        db,
        skip=skip,
        limit=limit,
        search=search,
        category_id=category_id,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    return {
        "items": products,
        "total": total,
        "skip": skip,
        "limit": limit,
        "has_more": skip + len(products) < total,
    }


@router.get("/{product_id}", response_model=ProductResponse)
def retrieve_product(product_id: int, db: DatabaseSession):
    product = product_service.get_product(db, product_id)

    if product is None:
        raise NotFoundException("Product")

    return product


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    data: ProductCreate,
    db: DatabaseSession,
    current_user: Annotated[User, Depends(require_admin)]
    ):
    return product_service.create_product(db, data)


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: DatabaseSession,
    current_user: Annotated[User, Depends(require_admin)]
):
    product = product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product_service.update_product(db, product, data)


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product(
    product_id: int,
    db: DatabaseSession,
    current_user: Annotated[User, Depends(require_admin)]
    ):
    product = product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    product_service.delete_product(db, product)
    return Response(status_code=status.HTTP_204_NO_CONTENT)