from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.product import Product

router = APIRouter(tags=["Products"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("/")
def get_products(db: DbSession):
    statement = select(Product).order_by(Product.id)
    return db.scalars(statement).all()

@router.get("/{product_id}")
def get_product_by_id(db: DbSession, product_id: int):
    # statement = select(Product).where(Product.id == product_id)
    # product = db.scalars(statement).first()
    product = db.get(Product , product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product