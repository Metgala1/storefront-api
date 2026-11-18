from datetime import datetime

from sqlalchemy import DateTime, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class WebhookEvent(Base):
    __tablename__ = "WebhookEvent"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    eventId: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )

    eventType: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    processedAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )