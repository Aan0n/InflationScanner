"""Voorbeelddata om de database te vullen met testproducten en prijzen."""

from datetime import datetime

from app.database import Base, SessionLocal, engine
from app.models import PriceEntry, Product, Store

# Maak tabellen aan
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# --- Winkels ---
stores = [
    Store(name="Albert Heijn", chain="Albert Heijn", location="Amsterdam"),
    Store(name="Jumbo", chain="Jumbo", location="Utrecht"),
    Store(name="Lidl", chain="Lidl", location="Rotterdam"),
    Store(name="McDonald's", chain="McDonald's", location="Den Haag"),
]
db.add_all(stores)
db.commit()

# --- Producten met historische prijzen ---
products_data = [
    {
        "product": Product(
            name="Big Mac", barcode=None, category="horeca", brand="McDonald's"
        ),
        "prices": [
            (3.50, "2020-01-15", 4),
            (3.75, "2021-03-10", 4),
            (3.95, "2022-06-20", 4),
            (4.49, "2023-09-01", 4),
            (4.95, "2024-06-15", 4),
            (5.29, "2025-01-10", 4),
        ],
    },
    {
        "product": Product(
            name="Melk halfvol (1L)",
            barcode="8710400010012",
            category="zuivel",
            brand="Campina",
        ),
        "prices": [
            (0.89, "2020-02-01", 1),
            (0.95, "2021-04-15", 1),
            (1.09, "2022-07-20", 1),
            (1.19, "2023-03-10", 2),
            (1.29, "2024-01-05", 1),
            (1.35, "2025-02-18", 2),
        ],
    },
    {
        "product": Product(
            name="Wit brood",
            barcode="8710400020011",
            category="brood",
            brand="Bolletje",
        ),
        "prices": [
            (1.29, "2020-03-01", 1),
            (1.39, "2021-06-10", 2),
            (1.59, "2022-09-15", 1),
            (1.79, "2023-05-20", 3),
            (1.89, "2024-08-12", 1),
            (2.09, "2025-01-25", 2),
        ],
    },
    {
        "product": Product(
            name="Heineken Pils (6-pack)",
            barcode="8712000900014",
            category="dranken",
            brand="Heineken",
        ),
        "prices": [
            (5.49, "2020-01-20", 1),
            (5.69, "2021-05-15", 2),
            (5.99, "2022-03-10", 1),
            (6.49, "2023-07-22", 3),
            (6.79, "2024-04-18", 1),
            (7.19, "2025-02-01", 2),
        ],
    },
    {
        "product": Product(
            name="Pindakaas (350g)",
            barcode="8710400030020",
            category="voeding",
            brand="Calvé",
        ),
        "prices": [
            (2.19, "2020-04-10", 1),
            (2.29, "2021-08-05", 2),
            (2.59, "2022-11-20", 1),
            (2.89, "2023-06-15", 3),
            (3.09, "2024-09-01", 2),
            (3.29, "2025-03-01", 1),
        ],
    },
    {
        "product": Product(
            name="Bananen (1kg)",
            barcode=None,
            category="groente",
            brand=None,
        ),
        "prices": [
            (1.49, "2020-02-15", 1),
            (1.49, "2021-03-20", 2),
            (1.59, "2022-05-10", 3),
            (1.79, "2023-08-25", 1),
            (1.89, "2024-07-12", 2),
            (1.99, "2025-01-30", 1),
        ],
    },
    {
        "product": Product(
            name="Kipfilet (per kg)",
            barcode=None,
            category="vlees",
            brand=None,
        ),
        "prices": [
            (7.99, "2020-01-10", 1),
            (8.49, "2021-04-22", 2),
            (9.49, "2022-08-30", 1),
            (10.99, "2023-05-15", 3),
            (11.49, "2024-10-01", 2),
            (12.49, "2025-02-20", 1),
        ],
    },
    {
        "product": Product(
            name="Toiletpapier (8 rollen)",
            barcode="8710400040029",
            category="huishouden",
            brand="Page",
        ),
        "prices": [
            (3.99, "2020-03-20", 1),
            (4.29, "2021-07-15", 2),
            (4.99, "2022-10-10", 3),
            (5.29, "2023-04-05", 1),
            (5.49, "2024-06-18", 2),
            (5.79, "2025-01-15", 1),
        ],
    },
]

for item in products_data:
    product = item["product"]
    db.add(product)
    db.commit()
    db.refresh(product)

    for price_val, date_str, store_idx in item["prices"]:
        entry = PriceEntry(
            product_id=product.id,
            store_id=stores[store_idx - 1].id,
            price=price_val,
            recorded_at=datetime.strptime(date_str, "%Y-%m-%d"),
            source="manual",
        )
        db.add(entry)

db.commit()
db.close()

print("Voorbeelddata succesvol geladen!")
print(f"  - {len(stores)} winkels")
print(f"  - {len(products_data)} producten")
print(f"  - {sum(len(p['prices']) for p in products_data)} prijsregistraties")
