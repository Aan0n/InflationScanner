"""InflationScanner API - Hoofdapplicatie."""

from datetime import datetime
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import func
from sqlalchemy.orm import Session
from starlette.requests import Request

from .database import Base, engine, get_db
from .models import PriceEntry, Product, Store
from .schemas import (
    PriceEntryCreate,
    PriceEntryResponse,
    PriceHistoryPoint,
    PriceHistoryResponse,
    ProductCreate,
    ProductResponse,
    StoreCreate,
    StoreResponse,
)

# Maak database tabellen aan
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InflationScanner API",
    description="Bekijk hoe productprijzen veranderen over tijd",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend bestanden serveren
frontend_dir = Path(__file__).parent.parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir / "static"), name="static")
templates = Jinja2Templates(directory=frontend_dir / "templates")


# --- Frontend routes ---


@app.get("/")
async def home(request: Request):
    """Hoofdpagina."""
    return templates.TemplateResponse("index.html", {"request": request})


# --- Product endpoints ---


@app.post("/api/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Maak een nieuw product aan."""
    if product.barcode:
        existing = db.query(Product).filter(Product.barcode == product.barcode).first()
        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Product met barcode {product.barcode} bestaat al (id={existing.id})",
            )
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get("/api/products", response_model=list[ProductResponse])
def list_products(
    search: str | None = Query(None, description="Zoek op naam of barcode"),
    category: str | None = None,
    country: str | None = Query(None, description="Filter op land van herkomst (ISO 3166-1 alpha-2)"),
    db: Session = Depends(get_db),
):
    """Zoek producten."""
    query = db.query(Product)
    if search:
        query = query.filter(
            Product.name.ilike(f"%{search}%") | Product.barcode.ilike(f"%{search}%")
        )
    if category:
        query = query.filter(Product.category == category)
    if country:
        query = query.filter(Product.origin_country == country.upper())
    return query.order_by(Product.name).limit(50).all()


@app.get("/api/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Haal een specifiek product op."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product niet gevonden")
    return product


@app.get("/api/products/barcode/{barcode}", response_model=ProductResponse)
def get_product_by_barcode(barcode: str, db: Session = Depends(get_db)):
    """Zoek een product op barcode."""
    product = db.query(Product).filter(Product.barcode == barcode).first()
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Geen product gevonden met barcode {barcode}"
        )
    return product


# --- Store endpoints ---


@app.post("/api/stores", response_model=StoreResponse)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    """Maak een nieuwe winkel aan."""
    db_store = Store(**store.model_dump())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store


@app.get("/api/stores", response_model=list[StoreResponse])
def list_stores(
    country: str | None = Query(None, description="Filter op land (ISO 3166-1 alpha-2)"),
    db: Session = Depends(get_db),
):
    """Lijst van alle winkels."""
    query = db.query(Store)
    if country:
        query = query.filter(Store.country_code == country.upper())
    return query.order_by(Store.name).all()


# --- PriceEntry endpoints ---


@app.post("/api/prices", response_model=PriceEntryResponse)
def add_price(entry: PriceEntryCreate, db: Session = Depends(get_db)):
    """Voeg een nieuwe prijsregistratie toe."""
    product = db.query(Product).filter(Product.id == entry.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product niet gevonden")

    data = entry.model_dump()
    if data["recorded_at"] is None:
        data["recorded_at"] = datetime.utcnow()

    db_entry = PriceEntry(**data)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


@app.get("/api/prices/{product_id}/history", response_model=PriceHistoryResponse)
def get_price_history(
    product_id: int,
    currency: str | None = Query(None, description="Filter op valuta (bijv. EUR, USD, CAD)"),
    db: Session = Depends(get_db),
):
    """Bekijk de volledige prijsgeschiedenis van een product."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product niet gevonden")

    query = (
        db.query(PriceEntry)
        .filter(PriceEntry.product_id == product_id)
    )
    if currency:
        query = query.filter(PriceEntry.currency == currency.upper())
    entries = query.order_by(PriceEntry.recorded_at.asc()).all()

    # Bepaal de meest voorkomende valuta in de resultaten
    result_currency = "EUR"
    if entries:
        currencies = {}
        for e in entries:
            currencies[e.currency] = currencies.get(e.currency, 0) + 1
        result_currency = max(currencies, key=currencies.get)

    history = []
    for entry in entries:
        store_name = None
        country_code = None
        if entry.store_id:
            store = db.query(Store).filter(Store.id == entry.store_id).first()
            if store:
                store_name = store.name
                country_code = store.country_code
        history.append(
            PriceHistoryPoint(
                price=entry.price,
                currency=entry.currency,
                recorded_at=entry.recorded_at,
                store_name=store_name,
                country_code=country_code,
                source=entry.source,
            )
        )

    current_price = entries[-1].price if entries else None
    oldest_price = entries[0].price if entries else None
    price_change = None
    if current_price and oldest_price and oldest_price != 0:
        price_change = round(((current_price - oldest_price) / oldest_price) * 100, 2)

    return PriceHistoryResponse(
        product=product,
        currency=result_currency,
        current_price=current_price,
        oldest_price=oldest_price,
        price_change_percent=price_change,
        history=history,
    )


@app.get("/api/stats/top-inflation", response_model=list[dict])
def top_inflation_products(
    limit: int = 10,
    country: str | None = Query(None, description="Filter op winkelland"),
    currency: str | None = Query(None, description="Filter op valuta"),
    db: Session = Depends(get_db),
):
    """Producten met de grootste prijsstijging."""
    products = db.query(Product).all()
    results = []

    for product in products:
        query = db.query(PriceEntry).filter(PriceEntry.product_id == product.id)
        if currency:
            query = query.filter(PriceEntry.currency == currency.upper())
        if country:
            query = query.join(Store).filter(Store.country_code == country.upper())
        entries = query.order_by(PriceEntry.recorded_at.asc()).all()

        if len(entries) >= 2:
            oldest = entries[0].price
            newest = entries[-1].price
            entry_currency = entries[-1].currency
            if oldest > 0:
                change = round(((newest - oldest) / oldest) * 100, 2)
                results.append(
                    {
                        "product_id": product.id,
                        "product_name": product.name,
                        "oldest_price": oldest,
                        "current_price": newest,
                        "currency": entry_currency,
                        "change_percent": change,
                        "country": product.origin_country,
                    }
                )

    results.sort(key=lambda x: x["change_percent"], reverse=True)
    return results[:limit]
