from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.room import Room
    from app.models.user import User


class RoomMember(Base):
    __tablename__ = "RoomMember"

    __table_args__ = (
        UniqueConstraint(
            "userId",
            "roomId",
            name="RoomMember_userId_roomId_key",
        ),
    )

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )

    userId: Mapped[int] = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE"),
        nullable=False,
    )

    roomId: Mapped[str] = mapped_column(
        ForeignKey("Room.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        back_populates="rooms",
    )

    room: Mapped["Room"] = relationship(
        back_populates="members",
    )