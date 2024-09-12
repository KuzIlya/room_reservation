from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from .reservation import Reservation


class MeetingRoom(Base):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(Text)
    reservations: Mapped[Reservation] = relationship(
        'Reservation',
        cascade='delete'
    )
