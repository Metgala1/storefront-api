from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)
from app.services import product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[ProductResponse])
def list_products(db: DatabaseSession):
    return product_service.get_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def retrieve_product(product_id: int, db: DatabaseSession):
    product = product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(data: ProductCreate, db: DatabaseSession):
    return product_service.create_product(db, data)


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: DatabaseSession,
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
def delete_product(product_id: int, db: DatabaseSession):
    product = product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    product_service.delete_product(db, product)
    return Response(status_code=status.HTTP_204_NO_CONTENT)