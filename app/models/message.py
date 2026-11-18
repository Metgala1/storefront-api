from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.room import Room
    from app.models.user import User


class Message(Base):
    __tablename__ = "Message"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )

    roomId: Mapped[str] = mapped_column(
        ForeignKey("Room.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    senderId: Mapped[int] = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE"),
        nullable=False,
    )

    sender: Mapped["User"] = relationship(
        back_populates="messages",
    )

    room: Mapped["Room"] = relationship(
        back_populates="messages",
    )