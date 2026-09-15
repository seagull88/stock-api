from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class Stock(Base):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    company: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
