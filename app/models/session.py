from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class Session(Base):
    __tablename__ = "Session"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )

    userId: Mapped[int] = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE"),
        nullable=False,
    )

    expiresAt: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        back_populates="sessions",
    )