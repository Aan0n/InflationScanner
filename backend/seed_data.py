"""Voorbeelddata om de database te vullen met testproducten en prijzen."""

from datetime import datetime

from app.database import Base, SessionLocal, engine
from app.models import PriceEntry, Product, Store

# Maak tabellen aan
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# --- Winkels (internationaal) ---
stores = [
    Store(name="Albert Heijn", chain="Albert Heijn", location="Amsterdam", country_code="NL"),
    Store(name="Jumbo", chain="Jumbo", location="Utrecht", country_code="NL"),
    Store(name="Lidl", chain="Lidl", location="Rotterdam", country_code="NL"),
    Store(name="McDonald's NL", chain="McDonald's", location="Den Haag", country_code="NL"),
    Store(name="Walmart", chain="Walmart", location="New York", country_code="US"),
    Store(name="McDonald's US", chain="McDonald's", location="Chicago", country_code="US"),
    Store(name="Loblaws", chain="Loblaws", location="Toronto", country_code="CA"),
    Store(name="Tim Hortons", chain="Tim Hortons", location="Vancouver", country_code="CA"),
    Store(name="Reliance Fresh", chain="Reliance", location="Mumbai", country_code="IN"),
    Store(name="Tesco", chain="Tesco", location="London", country_code="GB"),
]
db.add_all(stores)
db.commit()

# --- Producten met historische prijzen ---
products_data = [
    # === NEDERLAND (EUR) ===
    {
        "product": Product(
            name="Big Mac", barcode=None, category="horeca",
            brand="McDonald's", origin_country="NL",
        ),
        "prices": [
            (3.50, "2020-01-15", 4, "EUR"),
            (3.75, "2021-03-10", 4, "EUR"),
            (3.95, "2022-06-20", 4, "EUR"),
            (4.49, "2023-09-01", 4, "EUR"),
            (4.95, "2024-06-15", 4, "EUR"),
            (5.29, "2025-01-10", 4, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Melk halfvol (1L)", barcode="8710400010012",
            category="zuivel", brand="Campina", origin_country="NL",
        ),
        "prices": [
            (0.89, "2020-02-01", 1, "EUR"),
            (0.95, "2021-04-15", 1, "EUR"),
            (1.09, "2022-07-20", 1, "EUR"),
            (1.19, "2023-03-10", 2, "EUR"),
            (1.29, "2024-01-05", 1, "EUR"),
            (1.35, "2025-02-18", 2, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Wit brood", barcode="8710400020011",
            category="brood", brand="Bolletje", origin_country="NL",
        ),
        "prices": [
            (1.29, "2020-03-01", 1, "EUR"),
            (1.39, "2021-06-10", 2, "EUR"),
            (1.59, "2022-09-15", 1, "EUR"),
            (1.79, "2023-05-20", 3, "EUR"),
            (1.89, "2024-08-12", 1, "EUR"),
            (2.09, "2025-01-25", 2, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Heineken Pils (6-pack)", barcode="8712000900014",
            category="dranken", brand="Heineken", origin_country="NL",
        ),
        "prices": [
            (5.49, "2020-01-20", 1, "EUR"),
            (5.69, "2021-05-15", 2, "EUR"),
            (5.99, "2022-03-10", 1, "EUR"),
            (6.49, "2023-07-22", 3, "EUR"),
            (6.79, "2024-04-18", 1, "EUR"),
            (7.19, "2025-02-01", 2, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Pindakaas (350g)", barcode="8710400030020",
            category="voeding", brand="Calvé", origin_country="NL",
        ),
        "prices": [
            (2.19, "2020-04-10", 1, "EUR"),
            (2.29, "2021-08-05", 2, "EUR"),
            (2.59, "2022-11-20", 1, "EUR"),
            (2.89, "2023-06-15", 3, "EUR"),
            (3.09, "2024-09-01", 2, "EUR"),
            (3.29, "2025-03-01", 1, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Bananen (1kg)", barcode=None,
            category="groente", brand=None, origin_country="NL",
        ),
        "prices": [
            (1.49, "2020-02-15", 1, "EUR"),
            (1.49, "2021-03-20", 2, "EUR"),
            (1.59, "2022-05-10", 3, "EUR"),
            (1.79, "2023-08-25", 1, "EUR"),
            (1.89, "2024-07-12", 2, "EUR"),
            (1.99, "2025-01-30", 1, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Kipfilet (per kg)", barcode=None,
            category="vlees", brand=None, origin_country="NL",
        ),
        "prices": [
            (7.99, "2020-01-10", 1, "EUR"),
            (8.49, "2021-04-22", 2, "EUR"),
            (9.49, "2022-08-30", 1, "EUR"),
            (10.99, "2023-05-15", 3, "EUR"),
            (11.49, "2024-10-01", 2, "EUR"),
            (12.49, "2025-02-20", 1, "EUR"),
        ],
    },
    {
        "product": Product(
            name="Toiletpapier (8 rollen)", barcode="8710400040029",
            category="huishouden", brand="Page", origin_country="NL",
        ),
        "prices": [
            (3.99, "2020-03-20", 1, "EUR"),
            (4.29, "2021-07-15", 2, "EUR"),
            (4.99, "2022-10-10", 3, "EUR"),
            (5.29, "2023-04-05", 1, "EUR"),
            (5.49, "2024-06-18", 2, "EUR"),
            (5.79, "2025-01-15", 1, "EUR"),
        ],
    },
    # === VERENIGDE STATEN (USD) ===
    {
        "product": Product(
            name="Big Mac (US)", barcode=None, category="horeca",
            brand="McDonald's", origin_country="US",
        ),
        "prices": [
            (3.99, "2020-01-15", 6, "USD"),
            (4.29, "2021-03-10", 6, "USD"),
            (4.69, "2022-06-20", 6, "USD"),
            (5.15, "2023-09-01", 6, "USD"),
            (5.49, "2024-06-15", 6, "USD"),
            (5.89, "2025-01-10", 6, "USD"),
        ],
    },
    {
        "product": Product(
            name="Gallon Milk (US)", barcode="0041130001234",
            category="zuivel", brand="Great Value", origin_country="US",
        ),
        "prices": [
            (2.78, "2020-02-01", 5, "USD"),
            (3.09, "2021-04-15", 5, "USD"),
            (3.59, "2022-07-20", 5, "USD"),
            (3.89, "2023-03-10", 5, "USD"),
            (4.09, "2024-01-05", 5, "USD"),
            (4.29, "2025-02-18", 5, "USD"),
        ],
    },
    {
        "product": Product(
            name="Dozen Eggs (US)", barcode="0041130005678",
            category="voeding", brand=None, origin_country="US",
        ),
        "prices": [
            (1.47, "2020-01-20", 5, "USD"),
            (1.79, "2021-05-15", 5, "USD"),
            (2.87, "2022-03-10", 5, "USD"),
            (4.82, "2023-01-10", 5, "USD"),
            (3.59, "2024-04-18", 5, "USD"),
            (4.15, "2025-02-01", 5, "USD"),
        ],
    },
    # === CANADA (CAD) ===
    {
        "product": Product(
            name="Brood wit (CA)", barcode="0062150012345",
            category="brood", brand="Wonder", origin_country="CA",
        ),
        "prices": [
            (2.49, "2020-03-01", 7, "CAD"),
            (2.69, "2021-06-10", 7, "CAD"),
            (2.99, "2022-09-15", 7, "CAD"),
            (3.29, "2023-05-20", 7, "CAD"),
            (3.49, "2024-08-12", 7, "CAD"),
            (3.79, "2025-01-25", 7, "CAD"),
        ],
    },
    {
        "product": Product(
            name="Double Double Coffee", barcode=None,
            category="dranken", brand="Tim Hortons", origin_country="CA",
        ),
        "prices": [
            (1.62, "2020-01-10", 8, "CAD"),
            (1.72, "2021-04-22", 8, "CAD"),
            (1.82, "2022-08-30", 8, "CAD"),
            (1.92, "2023-05-15", 8, "CAD"),
            (2.02, "2024-10-01", 8, "CAD"),
            (2.17, "2025-02-20", 8, "CAD"),
        ],
    },
    # === INDIA (INR) ===
    {
        "product": Product(
            name="Atta Wheat Flour (5kg)", barcode="8901058000012",
            category="voeding", brand="Aashirvaad", origin_country="IN",
        ),
        "prices": [
            (225.0, "2020-02-15", 9, "INR"),
            (240.0, "2021-03-20", 9, "INR"),
            (270.0, "2022-05-10", 9, "INR"),
            (299.0, "2023-08-25", 9, "INR"),
            (315.0, "2024-07-12", 9, "INR"),
            (335.0, "2025-01-30", 9, "INR"),
        ],
    },
    {
        "product": Product(
            name="Amul Butter (500g)", barcode="8901058001234",
            category="zuivel", brand="Amul", origin_country="IN",
        ),
        "prices": [
            (210.0, "2020-01-10", 9, "INR"),
            (220.0, "2021-04-22", 9, "INR"),
            (240.0, "2022-08-30", 9, "INR"),
            (260.0, "2023-05-15", 9, "INR"),
            (275.0, "2024-10-01", 9, "INR"),
            (295.0, "2025-02-20", 9, "INR"),
        ],
    },
    # === VERENIGD KONINKRIJK (GBP) ===
    {
        "product": Product(
            name="Baked Beans (420g)", barcode="5000157000012",
            category="voeding", brand="Heinz", origin_country="GB",
        ),
        "prices": [
            (0.65, "2020-03-20", 10, "GBP"),
            (0.75, "2021-07-15", 10, "GBP"),
            (0.95, "2022-10-10", 10, "GBP"),
            (1.10, "2023-04-05", 10, "GBP"),
            (1.20, "2024-06-18", 10, "GBP"),
            (1.35, "2025-01-15", 10, "GBP"),
        ],
    },
]

for item in products_data:
    product = item["product"]
    db.add(product)
    db.commit()
    db.refresh(product)

    for price_val, date_str, store_idx, currency in item["prices"]:
        entry = PriceEntry(
            product_id=product.id,
            store_id=stores[store_idx - 1].id,
            price=price_val,
            currency=currency,
            recorded_at=datetime.strptime(date_str, "%Y-%m-%d"),
            source="manual",
        )
        db.add(entry)

db.commit()
db.close()

num_prices = sum(len(p["prices"]) for p in products_data)

print("Voorbeelddata succesvol geladen!")
print(f"  - {len(stores)} winkels (NL, US, CA, IN, GB)")
print(f"  - {len(products_data)} producten")
print(f"  - {num_prices} prijsregistraties")
print(f"  - Valuta's: CAD, EUR, GBP, INR, USD")
