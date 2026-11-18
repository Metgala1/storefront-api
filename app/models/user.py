from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, Text, func
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.enums import UserRole as UserRoleEnum

if TYPE_CHECKING:
    from app.models.message import Message
    from app.models.room import Room
    from app.models.room_member import RoomMember
    from app.models.session import Session


class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )

    passwordHash: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    UserRole: Mapped[UserRoleEnum] = mapped_column(
        SQLAlchemyEnum(
            UserRoleEnum,
            name="UserRole",
            values_callable=lambda enum_cls: [
                member.value for member in enum_cls
            ],
        ),
        default=UserRoleEnum.CUSTOMER,
        nullable=False,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    updatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships

    sessions: Mapped[list["Session"]] = relationship(
        back_populates="user",
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="sender",
    )

    rooms: Mapped[list["RoomMember"]] = relationship(
        back_populates="user",
    )

    ownedRooms: Mapped[list["Room"]] = relationship(
        back_populates="owner",
    )