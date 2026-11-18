from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


def get_categories(db: Session) -> list[Category]:
    statement = select(Category).order_by(Category.name)
    return list(db.scalars(statement).all())


def get_category(db: Session, category_id: int) -> Category | None:
    return db.get(Category, category_id)


def create_category(db: Session, data: CategoryCreate) -> Category:
    category = Category(**data.model_dump())

    try:
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    except IntegrityError:
        db.rollback()
        raise


def update_category(
    db: Session,
    category: Category,
    data: CategoryUpdate,
) -> Category:
    update_data = data.model_dump(exclude_unset=True)

    try:
        for field, value in update_data.items():
            setattr(category, field, value)

        db.commit()
        db.refresh(category)
        return category
    except IntegrityError:
        db.rollback()
        raise


def delete_category(db: Session, category: Category) -> bool:
    # A category cannot be deleted while products still reference it.
    if category.products:
        return False

    try:
        db.delete(category)
        db.commit()
        return True
    except IntegrityError:
        db.rollback()
        raise