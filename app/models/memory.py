from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Memory(Base):

    __tablename__ = "memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    memory_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    key: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    value: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    importance: Mapped[int] = mapped_column(
        Integer,
        default=5
    )

    confidence: Mapped[float] = mapped_column(
        Float,
        default=1.0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )