from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.category import Category


class Product(TimestampMixin, Base):
    __tablename__ = "Product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    reviews_count: Mapped[int] = mapped_column("reviewsCount", Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    specs: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False)
    image: Mapped[str] = mapped_column(Text, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    category_id: Mapped[int] = mapped_column("categoryId", ForeignKey("Category.id"), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products")