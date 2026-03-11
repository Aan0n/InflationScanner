"""Database modellen voor InflationScanner."""

from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Product(Base):
    """Een product dat gescand of ingevoerd is."""

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    barcode: Mapped[str | None] = mapped_column(String(50), unique=True, index=True)
    category: Mapped[str | None] = mapped_column(String(100), index=True)
    brand: Mapped[str | None] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text)
    origin_country: Mapped[str | None] = mapped_column(
        String(2), index=True
    )  # ISO 3166-1 alpha-2, bijv. "NL", "US", "IN"
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    prices: Mapped[list["PriceEntry"]] = relationship(back_populates="product")


class Store(Base):
    """Een winkel waar producten worden verkocht."""

    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    location: Mapped[str | None] = mapped_column(String(255))
    chain: Mapped[str | None] = mapped_column(String(100), index=True)
    country_code: Mapped[str | None] = mapped_column(
        String(2), index=True
    )  # ISO 3166-1 alpha-2, bijv. "NL", "US", "CA"

    prices: Mapped[list["PriceEntry"]] = relationship(back_populates="store")


class PriceEntry(Base):
    """Een prijsregistratie van een product op een bepaald moment."""

    __tablename__ = "price_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.id"), nullable=False, index=True
    )
    store_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("stores.id"), index=True
    )
    price: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="EUR")
    recorded_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, index=True
    )
    source: Mapped[str] = mapped_column(
        String(50), default="manual"
    )  # "manual", "scan", "receipt"

    product: Mapped["Product"] = relationship(back_populates="prices")
    store: Mapped["Store"] = relationship(back_populates="prices")
