from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.product import Product

router = APIRouter(tags=["Products"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("/")
def get_products(
    db: Annotated[Session, Depends(get_db)],
    category_id: int | None = None,
    min_price: float | None = None,
    sort_by: str = "id",
    direction: str = "asc",
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
):
    statement = select(Product)

    # Filtering
    if category_id is not None:
        statement = statement.where(
            Product.category_id == category_id
        )

    if min_price is not None:
        statement = statement.where(
            Product.price >= min_price
        )

    # Sorting
    sort_columns = {
        "id": Product.id,
        "name": Product.name,
        "price": Product.price,
        "rating": Product.rating
    }

    sort_column = sort_columns.get(sort_by, Product.id)

    if direction == "desc":
        sort_column = sort_column.desc()
    else:
        sort_column = sort_column.asc()

    statement = statement.order_by(sort_column, Product.id.asc())

    # Pagination
    skip = (page - 1) * limit

    statement = statement.offset(skip).limit(limit)

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