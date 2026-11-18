from datetime import datetime

from sqlalchemy import DateTime, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Video(Base):
    __tablename__ = "Video"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )

    title: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    bucket: Mapped[str] = mapped_column(
        Text,
        default="videos",
        server_default="videos",
        nullable=False,
    )

    storagePath: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )

    mimeType: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    sizeBytes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    durationMs: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
        index=True,
    )

    updatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )