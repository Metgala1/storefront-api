from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Example(Base):
    __tablename__ = "example"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )


print("Registered tables:")
print(list(Base.metadata.tables.keys()))