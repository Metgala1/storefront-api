from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundException
from app.core.permissions import require_admin
from app.database.session import get_db
from app.models.user import User
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from app.services import category_service

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: DatabaseSession):
    return category_service.get_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def retrieve_category(category_id: int, db: DatabaseSession):
    category = category_service.get_category(db, category_id)

    if category is None:
        raise NotFoundException("Category")

    return category


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    data: CategoryCreate,
    db: DatabaseSession,
    current_user: Annotated[User, Depends(require_admin)]
    ):
    try:
        return category_service.create_category(db, data)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A category with that name or slug already exists.",
        )


@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: DatabaseSession,
    current_user: Annotated[User, Depends(require_admin)]
):
    category = category_service.get_category(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    try:
        return category_service.update_category(db, category, data)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A category with that name or slug already exists.",
        )


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int, 
    db: DatabaseSession,
    current_user: Annotated[User, Depends(require_admin)]
    ):
    category = category_service.get_category(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    try:
        deleted = category_service.delete_category(db, category)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cannot delete a category that has associated products.",
        )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cannot delete a category that has associated products.",
        )