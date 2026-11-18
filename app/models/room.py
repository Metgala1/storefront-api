from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.message import Message
    from app.models.room_member import RoomMember
    from app.models.user import User


class Room(Base):
    __tablename__ = "Room"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    ownerId: Mapped[int] = mapped_column(
        ForeignKey("User.id"),
        nullable=False,
        index=True,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    owner: Mapped["User"] = relationship(
        back_populates="ownedRooms",
    )

    members: Mapped[list["RoomMember"]] = relationship(
        back_populates="room",
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="room",
    )