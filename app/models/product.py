from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.category import Category


class Product(Base):
    __tablename__ = "Product"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    rating: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    reviewsCount: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    specs: Mapped[list[str]] = mapped_column(
        ARRAY(Text),
        nullable=False,
    )

    image: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )

    updatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    categoryId: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "Category.id",
            name="Product_categoryId_fkey",
        ),
        nullable=False,
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products",
    )

    __table_args__ = (
        Index("Product_rating_idx", "rating"),
    )