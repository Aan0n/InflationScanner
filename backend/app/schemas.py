"""Pydantic schemas voor API request/response validatie."""

from datetime import datetime

from pydantic import BaseModel


# --- Product schemas ---


class ProductCreate(BaseModel):
    name: str
    barcode: str | None = None
    category: str | None = None
    brand: str | None = None
    description: str | None = None
    origin_country: str | None = None  # ISO 3166-1 alpha-2, bijv. "NL", "US"


class ProductResponse(BaseModel):
    id: int
    name: str
    barcode: str | None
    category: str | None
    brand: str | None
    description: str | None
    origin_country: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


# --- Store schemas ---


class StoreCreate(BaseModel):
    name: str
    location: str | None = None
    chain: str | None = None
    country_code: str | None = None  # ISO 3166-1 alpha-2, bijv. "NL", "CA"


class StoreResponse(BaseModel):
    id: int
    name: str
    location: str | None
    chain: str | None
    country_code: str | None

    model_config = {"from_attributes": True}


# --- PriceEntry schemas ---


class PriceEntryCreate(BaseModel):
    product_id: int
    store_id: int | None = None
    price: float
    currency: str = "EUR"
    source: str = "manual"
    recorded_at: datetime | None = None


class PriceEntryResponse(BaseModel):
    id: int
    product_id: int
    store_id: int | None
    price: float
    currency: str
    recorded_at: datetime
    source: str

    model_config = {"from_attributes": True}


# --- Prijsgeschiedenis ---


class PriceHistoryPoint(BaseModel):
    price: float
    currency: str
    recorded_at: datetime
    store_name: str | None = None
    country_code: str | None = None
    source: str


class PriceHistoryResponse(BaseModel):
    product: ProductResponse
    currency: str
    current_price: float | None
    oldest_price: float | None
    price_change_percent: float | None
    history: list[PriceHistoryPoint]
