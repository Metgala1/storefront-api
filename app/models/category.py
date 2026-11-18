from typing import TYPE_CHECKING

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.product import Product


class Category(Base):
    __tablename__ = "Category"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )

    products: Mapped[list["Product"]] = relationship(
        back_populates="category",
    )