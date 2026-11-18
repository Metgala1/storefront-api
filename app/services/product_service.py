from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_products(
    db: Session,
    *,
    skip: int = 0,
    limit: int = 20,
    search: str | None = None,
    category_id: int | None = None,
    sort_by: str = "id",
    sort_order: str = "desc",
) -> tuple[list[Product], int]:

    statement = select(Product)

    if search:
        statement = statement.where(
            Product.name.ilike(f"%{search}%")
        )

    if category_id is not None:
        statement = statement.where(
            Product.categoryId == category_id
        )

    # Count all matching products before pagination.
    count_statement = select(func.count()).select_from(
        statement.subquery()
    )

    total = db.scalar(count_statement) or 0

    sort_columns = {
        "id": Product.id,
        "name": Product.name,
        "price": Product.price,
        "rating": Product.rating,
        "createdAt": Product.createdAt,
    }

    sort_column = sort_columns[sort_by]

    if sort_order == "desc":
        sort_column = sort_column.desc()
    else:
        sort_column = sort_column.asc()

    statement = (
        statement
        .order_by(sort_column, Product.id.desc())
        .offset(skip)
        .limit(limit)
    )

    products = list(db.scalars(statement).all())

    return products, total


def get_product(db: Session, product_id: int) -> Product | None:
    return db.get(Product, product_id)


def create_product(db: Session, product_data: ProductCreate) -> Product:
    product = Product(**product_data.model_dump())

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def update_product(
    db: Session,
    product: Product,
    product_data: ProductUpdate,
) -> Product:
    update_data = product_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product: Product) -> None:
    db.delete(product)
    db.commit()