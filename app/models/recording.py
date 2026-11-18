from datetime import datetime

from sqlalchemy import DateTime, Integer, LargeBinary, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Recording(Base):
    __tablename__ = "Recording"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )

    title: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    data: Mapped[bytes] = mapped_column(
        LargeBinary,
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
    )