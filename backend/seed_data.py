"""Uitgebreide wereldwijde seed data voor InflationScanner.

Bevat producten, winkels en prijshistorie voor 40+ landen verspreid
over alle continenten, met realistische inflatie-trends.
"""

from datetime import datetime

from app.database import Base, SessionLocal, engine
from app.models import PriceEntry, Product, Store

# Maak tabellen aan (drop eerst bestaande)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ============================================================
# WINKELS - Wereldwijd (supermarkten, horeca, speciaalzaken)
# ============================================================
stores_data = [
    # --- Europa ---
    # Nederland
    {"name": "Albert Heijn", "chain": "Albert Heijn", "location": "Amsterdam", "cc": "NL"},
    {"name": "Jumbo", "chain": "Jumbo", "location": "Utrecht", "cc": "NL"},
    {"name": "Lidl NL", "chain": "Lidl", "location": "Rotterdam", "cc": "NL"},
    {"name": "McDonald's NL", "chain": "McDonald's", "location": "Den Haag", "cc": "NL"},
    # Belgie
    {"name": "Colruyt", "chain": "Colruyt", "location": "Brussel", "cc": "BE"},
    {"name": "Delhaize", "chain": "Delhaize", "location": "Antwerpen", "cc": "BE"},
    # Duitsland
    {"name": "Aldi DE", "chain": "Aldi", "location": "Berlijn", "cc": "DE"},
    {"name": "Edeka", "chain": "Edeka", "location": "Hamburg", "cc": "DE"},
    {"name": "Lidl DE", "chain": "Lidl", "location": "Munchen", "cc": "DE"},
    # Frankrijk
    {"name": "Carrefour FR", "chain": "Carrefour", "location": "Parijs", "cc": "FR"},
    {"name": "Leclerc", "chain": "E.Leclerc", "location": "Lyon", "cc": "FR"},
    # Spanje
    {"name": "Mercadona", "chain": "Mercadona", "location": "Madrid", "cc": "ES"},
    {"name": "Lidl ES", "chain": "Lidl", "location": "Barcelona", "cc": "ES"},
    # Italie
    {"name": "Coop IT", "chain": "Coop", "location": "Rome", "cc": "IT"},
    {"name": "Esselunga", "chain": "Esselunga", "location": "Milaan", "cc": "IT"},
    # Portugal
    {"name": "Pingo Doce", "chain": "Pingo Doce", "location": "Lissabon", "cc": "PT"},
    # Verenigd Koninkrijk
    {"name": "Tesco", "chain": "Tesco", "location": "Londen", "cc": "GB"},
    {"name": "Sainsbury's", "chain": "Sainsbury's", "location": "Manchester", "cc": "GB"},
    # Ierland
    {"name": "Tesco IE", "chain": "Tesco", "location": "Dublin", "cc": "IE"},
    # Zweden
    {"name": "ICA", "chain": "ICA", "location": "Stockholm", "cc": "SE"},
    # Noorwegen
    {"name": "Rema 1000", "chain": "Rema 1000", "location": "Oslo", "cc": "NO"},
    # Denemarken
    {"name": "Netto DK", "chain": "Netto", "location": "Kopenhagen", "cc": "DK"},
    # Finland
    {"name": "S-Market", "chain": "S-Group", "location": "Helsinki", "cc": "FI"},
    # Zwitserland
    {"name": "Migros", "chain": "Migros", "location": "Zurich", "cc": "CH"},
    {"name": "Coop CH", "chain": "Coop", "location": "Bern", "cc": "CH"},
    # Oostenrijk
    {"name": "Billa", "chain": "Billa", "location": "Wenen", "cc": "AT"},
    # Polen
    {"name": "Biedronka", "chain": "Biedronka", "location": "Warschau", "cc": "PL"},
    # Tsjechie
    {"name": "Albert CZ", "chain": "Albert", "location": "Praag", "cc": "CZ"},
    # Griekenland
    {"name": "Sklavenitis", "chain": "Sklavenitis", "location": "Athene", "cc": "GR"},
    # Turkije
    {"name": "Migros TR", "chain": "Migros", "location": "Istanbul", "cc": "TR"},
    {"name": "BIM", "chain": "BIM", "location": "Ankara", "cc": "TR"},
    # Rusland
    {"name": "Pyaterochka", "chain": "Pyaterochka", "location": "Moskou", "cc": "RU"},
    # Oekraine
    {"name": "ATB Market", "chain": "ATB", "location": "Kiev", "cc": "UA"},
    # Roemenie
    {"name": "Kaufland RO", "chain": "Kaufland", "location": "Boekarest", "cc": "RO"},
    # Hongarije
    {"name": "Spar HU", "chain": "Spar", "location": "Boedapest", "cc": "HU"},
    # Kroatie
    {"name": "Konzum", "chain": "Konzum", "location": "Zagreb", "cc": "HR"},

    # --- Noord-Amerika ---
    # VS
    {"name": "Walmart US", "chain": "Walmart", "location": "New York", "cc": "US"},
    {"name": "Kroger", "chain": "Kroger", "location": "Cincinnati", "cc": "US"},
    {"name": "McDonald's US", "chain": "McDonald's", "location": "Chicago", "cc": "US"},
    {"name": "ShopRite", "chain": "ShopRite", "location": "New Jersey", "cc": "US"},
    # Canada
    {"name": "Loblaws", "chain": "Loblaws", "location": "Toronto", "cc": "CA"},
    {"name": "Tim Hortons", "chain": "Tim Hortons", "location": "Vancouver", "cc": "CA"},
    {"name": "No Frills", "chain": "No Frills", "location": "Ottawa", "cc": "CA"},
    # Mexico
    {"name": "Walmart MX", "chain": "Walmart", "location": "Mexico-Stad", "cc": "MX"},
    {"name": "Soriana", "chain": "Soriana", "location": "Monterrey", "cc": "MX"},
    # El Salvador
    {"name": "Super Selectos", "chain": "Super Selectos", "location": "San Salvador", "cc": "SV"},
    # Panama
    {"name": "Super 99", "chain": "Super 99", "location": "Panama-Stad", "cc": "PA"},
    # Costa Rica
    {"name": "AutoMercado", "chain": "AutoMercado", "location": "San Jose", "cc": "CR"},
    # Guatemala
    {"name": "La Torre", "chain": "La Torre", "location": "Guatemala-Stad", "cc": "GT"},
    # Cuba
    {"name": "TRD Caribe", "chain": "TRD", "location": "Havana", "cc": "CU"},
    # Jamaica
    {"name": "Hi-Lo", "chain": "Hi-Lo", "location": "Kingston", "cc": "JM"},
    # Dominicaanse Rep.
    {"name": "Jumbo DO", "chain": "Jumbo", "location": "Santo Domingo", "cc": "DO"},

    # --- Zuid-Amerika ---
    # Brazilie
    {"name": "Carrefour BR", "chain": "Carrefour", "location": "Sao Paulo", "cc": "BR"},
    {"name": "Pao de Acucar", "chain": "GPA", "location": "Rio de Janeiro", "cc": "BR"},
    # Argentinie
    {"name": "Carrefour AR", "chain": "Carrefour", "location": "Buenos Aires", "cc": "AR"},
    # Colombia
    {"name": "Exito", "chain": "Grupo Exito", "location": "Bogota", "cc": "CO"},
    # Chili
    {"name": "Lider", "chain": "Walmart Chile", "location": "Santiago", "cc": "CL"},
    # Peru
    {"name": "Wong", "chain": "Cencosud", "location": "Lima", "cc": "PE"},
    # Suriname
    {"name": "Fernandes", "chain": "Fernandes", "location": "Paramaribo", "cc": "SR"},
    # Venezuela
    {"name": "Excelsior Gama", "chain": "Excelsior Gama", "location": "Caracas", "cc": "VE"},
    # Uruguay
    {"name": "Tienda Inglesa", "chain": "Tienda Inglesa", "location": "Montevideo", "cc": "UY"},
    # Ecuador
    {"name": "Supermaxi", "chain": "Supermaxi", "location": "Quito", "cc": "EC"},
    # Bolivia
    {"name": "Hipermaxi", "chain": "Hipermaxi", "location": "Santa Cruz", "cc": "BO"},
    # Paraguay
    {"name": "Superseis", "chain": "Superseis", "location": "Asuncion", "cc": "PY"},

    # --- Midden-Oosten ---
    # Saoedi-Arabie
    {"name": "Tamimi Markets", "chain": "Tamimi", "location": "Riyad", "cc": "SA"},
    # VAE
    {"name": "Carrefour AE", "chain": "Carrefour", "location": "Dubai", "cc": "AE"},
    {"name": "Lulu Hypermarket", "chain": "Lulu", "location": "Abu Dhabi", "cc": "AE"},
    # Israel
    {"name": "Shufersal", "chain": "Shufersal", "location": "Tel Aviv", "cc": "IL"},
    # Qatar
    {"name": "Al Meera", "chain": "Al Meera", "location": "Doha", "cc": "QA"},
    # Koeweit
    {"name": "The Sultan Center", "chain": "TSC", "location": "Koeweit-Stad", "cc": "KW"},
    # Jordanie
    {"name": "Carrefour JO", "chain": "Carrefour", "location": "Amman", "cc": "JO"},
    # Libanon
    {"name": "Spinneys LB", "chain": "Spinneys", "location": "Beiroet", "cc": "LB"},
    # Egypte
    {"name": "Carrefour EG", "chain": "Carrefour", "location": "Cairo", "cc": "EG"},
    # Irak
    {"name": "Majidi Mall", "chain": "Majidi", "location": "Bagdad", "cc": "IQ"},

    # --- Azie ---
    # India
    {"name": "Reliance Fresh", "chain": "Reliance", "location": "Mumbai", "cc": "IN"},
    {"name": "Big Bazaar", "chain": "Big Bazaar", "location": "Delhi", "cc": "IN"},
    # Japan
    {"name": "Aeon", "chain": "Aeon", "location": "Tokyo", "cc": "JP"},
    {"name": "7-Eleven JP", "chain": "7-Eleven", "location": "Osaka", "cc": "JP"},
    # China
    {"name": "Walmart CN", "chain": "Walmart", "location": "Shanghai", "cc": "CN"},
    {"name": "Hema", "chain": "Freshippo", "location": "Peking", "cc": "CN"},
    # Zuid-Korea
    {"name": "E-Mart", "chain": "E-Mart", "location": "Seoul", "cc": "KR"},
    # Thailand
    {"name": "Tesco Lotus", "chain": "Lotus's", "location": "Bangkok", "cc": "TH"},
    {"name": "7-Eleven TH", "chain": "7-Eleven", "location": "Chiang Mai", "cc": "TH"},
    # Indonesie
    {"name": "Indomaret", "chain": "Indomaret", "location": "Jakarta", "cc": "ID"},
    {"name": "Alfamart", "chain": "Alfamart", "location": "Surabaya", "cc": "ID"},
    # Filipijnen
    {"name": "SM Supermarket", "chain": "SM", "location": "Manila", "cc": "PH"},
    # Vietnam
    {"name": "VinMart", "chain": "VinMart", "location": "Hanoi", "cc": "VN"},
    # Singapore
    {"name": "FairPrice", "chain": "NTUC FairPrice", "location": "Singapore", "cc": "SG"},
    # Maleisie
    {"name": "Mydin", "chain": "Mydin", "location": "Kuala Lumpur", "cc": "MY"},
    # Pakistan
    {"name": "Imtiaz", "chain": "Imtiaz", "location": "Karachi", "cc": "PK"},
    # Bangladesh
    {"name": "Shwapno", "chain": "Shwapno", "location": "Dhaka", "cc": "BD"},

    # --- Afrika ---
    # Zuid-Afrika
    {"name": "Shoprite ZA", "chain": "Shoprite", "location": "Kaapstad", "cc": "ZA"},
    {"name": "Pick n Pay", "chain": "Pick n Pay", "location": "Johannesburg", "cc": "ZA"},
    # Nigeria
    {"name": "Shoprite NG", "chain": "Shoprite", "location": "Lagos", "cc": "NG"},
    # Kenia
    {"name": "Naivas", "chain": "Naivas", "location": "Nairobi", "cc": "KE"},
    # Ghana
    {"name": "Shoprite GH", "chain": "Shoprite", "location": "Accra", "cc": "GH"},
    # Marokko
    {"name": "Marjane", "chain": "Marjane", "location": "Casablanca", "cc": "MA"},
    # Ethiopie
    {"name": "Shoa Supermarket", "chain": "Shoa", "location": "Addis Abeba", "cc": "ET"},
    # Tanzania
    {"name": "Shoppers TZ", "chain": "Shoppers", "location": "Dar es Salaam", "cc": "TZ"},
    # Senegal
    {"name": "Auchan SN", "chain": "Auchan", "location": "Dakar", "cc": "SN"},
    # Ivoorkust
    {"name": "Carrefour CI", "chain": "Carrefour", "location": "Abidjan", "cc": "CI"},

    # --- Oceanie ---
    # Australie
    {"name": "Woolworths AU", "chain": "Woolworths", "location": "Sydney", "cc": "AU"},
    {"name": "Coles", "chain": "Coles", "location": "Melbourne", "cc": "AU"},
    # Nieuw-Zeeland
    {"name": "Countdown NZ", "chain": "Countdown", "location": "Auckland", "cc": "NZ"},

    # --- Fastfood ketens (wereldwijd) ---
    {"name": "McDonald's DE", "chain": "McDonald's", "location": "Berlijn", "cc": "DE"},
    {"name": "McDonald's FR", "chain": "McDonald's", "location": "Parijs", "cc": "FR"},
    {"name": "McDonald's JP", "chain": "McDonald's", "location": "Tokyo", "cc": "JP"},
    {"name": "McDonald's AU", "chain": "McDonald's", "location": "Sydney", "cc": "AU"},
    {"name": "McDonald's BR", "chain": "McDonald's", "location": "Sao Paulo", "cc": "BR"},
    {"name": "McDonald's IN", "chain": "McDonald's", "location": "Mumbai", "cc": "IN"},
    {"name": "McDonald's ZA", "chain": "McDonald's", "location": "Johannesburg", "cc": "ZA"},
    {"name": "McDonald's TR", "chain": "McDonald's", "location": "Istanbul", "cc": "TR"},
    {"name": "McDonald's MX", "chain": "McDonald's", "location": "Mexico-Stad", "cc": "MX"},
    {"name": "McDonald's SA", "chain": "McDonald's", "location": "Riyad", "cc": "SA"},
    {"name": "McDonald's EG", "chain": "McDonald's", "location": "Cairo", "cc": "EG"},
    {"name": "Burger King NL", "chain": "Burger King", "location": "Amsterdam", "cc": "NL"},
    {"name": "Burger King US", "chain": "Burger King", "location": "Miami", "cc": "US"},
    {"name": "Burger King DE", "chain": "Burger King", "location": "Frankfurt", "cc": "DE"},
    {"name": "KFC GB", "chain": "KFC", "location": "Londen", "cc": "GB"},
    {"name": "KFC ZA", "chain": "KFC", "location": "Kaapstad", "cc": "ZA"},
    {"name": "Starbucks US", "chain": "Starbucks", "location": "Seattle", "cc": "US"},
    {"name": "Starbucks GB", "chain": "Starbucks", "location": "Londen", "cc": "GB"},
    {"name": "Starbucks JP", "chain": "Starbucks", "location": "Tokyo", "cc": "JP"},
]

stores = []
for sd in stores_data:
    s = Store(name=sd["name"], chain=sd["chain"], location=sd["location"], country_code=sd["cc"])
    stores.append(s)
db.add_all(stores)
db.commit()

# Maak lookup per naam
store_map = {s.name: s.id for s in stores}


def S(name):
    """Helper: store id opzoeken op naam."""
    return store_map[name]


# ============================================================
# PRODUCTEN MET HISTORISCHE PRIJZEN
# Formaat: (prijs, datum, winkel_naam, valuta)
# ============================================================

products_data = [
    # ============================================================
    #  EUROPA
    # ============================================================

    # === NEDERLAND (EUR) ===
    {
        "product": Product(name="Big Mac", category="horeca", brand="McDonald's", origin_country="NL"),
        "prices": [
            (3.50, "2020-01-15", "McDonald's NL", "EUR"),
            (3.75, "2021-03-10", "McDonald's NL", "EUR"),
            (3.95, "2022-06-20", "McDonald's NL", "EUR"),
            (4.49, "2023-09-01", "McDonald's NL", "EUR"),
            (4.95, "2024-06-15", "McDonald's NL", "EUR"),
            (5.29, "2025-01-10", "McDonald's NL", "EUR"),
        ],
    },
    {
        "product": Product(name="Melk halfvol (1L)", barcode="8710400010012", category="zuivel", brand="Campina", origin_country="NL"),
        "prices": [
            (0.89, "2020-02-01", "Albert Heijn", "EUR"),
            (0.95, "2021-04-15", "Albert Heijn", "EUR"),
            (1.09, "2022-07-20", "Albert Heijn", "EUR"),
            (1.19, "2023-03-10", "Jumbo", "EUR"),
            (1.29, "2024-01-05", "Albert Heijn", "EUR"),
            (1.35, "2025-02-18", "Jumbo", "EUR"),
        ],
    },
    {
        "product": Product(name="Wit brood", barcode="8710400020011", category="brood", brand="Bolletje", origin_country="NL"),
        "prices": [
            (1.29, "2020-03-01", "Albert Heijn", "EUR"),
            (1.39, "2021-06-10", "Jumbo", "EUR"),
            (1.59, "2022-09-15", "Albert Heijn", "EUR"),
            (1.79, "2023-05-20", "Lidl NL", "EUR"),
            (1.89, "2024-08-12", "Albert Heijn", "EUR"),
            (2.09, "2025-01-25", "Jumbo", "EUR"),
        ],
    },
    {
        "product": Product(name="Heineken Pils (6-pack)", barcode="8712000900014", category="dranken", brand="Heineken", origin_country="NL"),
        "prices": [
            (5.49, "2020-01-20", "Albert Heijn", "EUR"),
            (5.69, "2021-05-15", "Jumbo", "EUR"),
            (5.99, "2022-03-10", "Albert Heijn", "EUR"),
            (6.49, "2023-07-22", "Lidl NL", "EUR"),
            (6.79, "2024-04-18", "Albert Heijn", "EUR"),
            (7.19, "2025-02-01", "Jumbo", "EUR"),
        ],
    },
    {
        "product": Product(name="Pindakaas (350g)", barcode="8710400030020", category="voeding", brand="Calvé", origin_country="NL"),
        "prices": [
            (2.19, "2020-04-10", "Albert Heijn", "EUR"),
            (2.29, "2021-08-05", "Jumbo", "EUR"),
            (2.59, "2022-11-20", "Albert Heijn", "EUR"),
            (2.89, "2023-06-15", "Lidl NL", "EUR"),
            (3.09, "2024-09-01", "Jumbo", "EUR"),
            (3.29, "2025-03-01", "Albert Heijn", "EUR"),
        ],
    },
    {
        "product": Product(name="Bananen (1kg)", category="groente", origin_country="NL"),
        "prices": [
            (1.49, "2020-02-15", "Albert Heijn", "EUR"),
            (1.49, "2021-03-20", "Jumbo", "EUR"),
            (1.59, "2022-05-10", "Lidl NL", "EUR"),
            (1.79, "2023-08-25", "Albert Heijn", "EUR"),
            (1.89, "2024-07-12", "Jumbo", "EUR"),
            (1.99, "2025-01-30", "Albert Heijn", "EUR"),
        ],
    },
    {
        "product": Product(name="Kipfilet (per kg)", category="vlees", origin_country="NL"),
        "prices": [
            (7.99, "2020-01-10", "Albert Heijn", "EUR"),
            (8.49, "2021-04-22", "Jumbo", "EUR"),
            (9.49, "2022-08-30", "Albert Heijn", "EUR"),
            (10.99, "2023-05-15", "Lidl NL", "EUR"),
            (11.49, "2024-10-01", "Jumbo", "EUR"),
            (12.49, "2025-02-20", "Albert Heijn", "EUR"),
        ],
    },
    {
        "product": Product(name="Toiletpapier (8 rollen)", barcode="8710400040029", category="huishouden", brand="Page", origin_country="NL"),
        "prices": [
            (3.99, "2020-03-20", "Albert Heijn", "EUR"),
            (4.29, "2021-07-15", "Jumbo", "EUR"),
            (4.99, "2022-10-10", "Lidl NL", "EUR"),
            (5.29, "2023-04-05", "Albert Heijn", "EUR"),
            (5.49, "2024-06-18", "Jumbo", "EUR"),
            (5.79, "2025-01-15", "Albert Heijn", "EUR"),
        ],
    },
    {
        "product": Product(name="Whopper", category="horeca", brand="Burger King", origin_country="NL"),
        "prices": [
            (4.50, "2020-02-10", "Burger King NL", "EUR"),
            (4.75, "2021-05-20", "Burger King NL", "EUR"),
            (5.10, "2022-08-15", "Burger King NL", "EUR"),
            (5.50, "2023-11-01", "Burger King NL", "EUR"),
            (5.90, "2024-07-20", "Burger King NL", "EUR"),
            (6.25, "2025-02-15", "Burger King NL", "EUR"),
        ],
    },

    # === BELGIE (EUR) ===
    {
        "product": Product(name="Melk halfvol (1L)", category="zuivel", brand="Inex", origin_country="BE"),
        "prices": [
            (0.85, "2020-01-10", "Colruyt", "EUR"),
            (0.92, "2021-03-15", "Delhaize", "EUR"),
            (1.05, "2022-06-20", "Colruyt", "EUR"),
            (1.15, "2023-09-10", "Delhaize", "EUR"),
            (1.25, "2024-04-05", "Colruyt", "EUR"),
            (1.32, "2025-01-20", "Delhaize", "EUR"),
        ],
    },
    {
        "product": Product(name="Belgische Frieten (1kg)", category="voeding", origin_country="BE"),
        "prices": [
            (1.69, "2020-02-20", "Colruyt", "EUR"),
            (1.79, "2021-05-10", "Delhaize", "EUR"),
            (1.99, "2022-08-15", "Colruyt", "EUR"),
            (2.29, "2023-03-25", "Delhaize", "EUR"),
            (2.49, "2024-07-12", "Colruyt", "EUR"),
            (2.69, "2025-02-01", "Delhaize", "EUR"),
        ],
    },

    # === DUITSLAND (EUR) ===
    {
        "product": Product(name="Big Mac", category="horeca", brand="McDonald's", origin_country="DE"),
        "prices": [
            (3.69, "2020-01-15", "McDonald's DE", "EUR"),
            (3.89, "2021-04-10", "McDonald's DE", "EUR"),
            (4.09, "2022-07-20", "McDonald's DE", "EUR"),
            (4.59, "2023-10-01", "McDonald's DE", "EUR"),
            (5.09, "2024-06-15", "McDonald's DE", "EUR"),
            (5.49, "2025-01-10", "McDonald's DE", "EUR"),
        ],
    },
    {
        "product": Product(name="Vollmilch (1L)", category="zuivel", brand="Weihenstephan", origin_country="DE"),
        "prices": [
            (0.69, "2020-02-01", "Aldi DE", "EUR"),
            (0.75, "2021-05-15", "Edeka", "EUR"),
            (0.95, "2022-08-20", "Lidl DE", "EUR"),
            (1.09, "2023-03-10", "Aldi DE", "EUR"),
            (1.15, "2024-01-05", "Edeka", "EUR"),
            (1.19, "2025-02-18", "Aldi DE", "EUR"),
        ],
    },
    {
        "product": Product(name="Mischbrot (500g)", category="brood", origin_country="DE"),
        "prices": [
            (1.29, "2020-03-01", "Aldi DE", "EUR"),
            (1.39, "2021-06-10", "Edeka", "EUR"),
            (1.69, "2022-09-15", "Lidl DE", "EUR"),
            (1.89, "2023-05-20", "Aldi DE", "EUR"),
            (1.99, "2024-08-12", "Edeka", "EUR"),
            (2.19, "2025-01-25", "Lidl DE", "EUR"),
        ],
    },
    {
        "product": Product(name="Whopper (DE)", category="horeca", brand="Burger King", origin_country="DE"),
        "prices": [
            (4.49, "2020-02-15", "Burger King DE", "EUR"),
            (4.69, "2021-06-20", "Burger King DE", "EUR"),
            (4.99, "2022-09-10", "Burger King DE", "EUR"),
            (5.49, "2023-12-01", "Burger King DE", "EUR"),
            (5.89, "2024-08-15", "Burger King DE", "EUR"),
            (6.29, "2025-02-20", "Burger King DE", "EUR"),
        ],
    },

    # === FRANKRIJK (EUR) ===
    {
        "product": Product(name="Big Mac", category="horeca", brand="McDonald's", origin_country="FR"),
        "prices": [
            (4.05, "2020-01-15", "McDonald's FR", "EUR"),
            (4.25, "2021-04-10", "McDonald's FR", "EUR"),
            (4.50, "2022-07-20", "McDonald's FR", "EUR"),
            (4.95, "2023-10-01", "McDonald's FR", "EUR"),
            (5.30, "2024-06-15", "McDonald's FR", "EUR"),
            (5.60, "2025-01-10", "McDonald's FR", "EUR"),
        ],
    },
    {
        "product": Product(name="Baguette tradition", category="brood", origin_country="FR"),
        "prices": [
            (0.85, "2020-02-10", "Carrefour FR", "EUR"),
            (0.90, "2021-05-15", "Leclerc", "EUR"),
            (1.00, "2022-08-20", "Carrefour FR", "EUR"),
            (1.10, "2023-03-10", "Leclerc", "EUR"),
            (1.15, "2024-06-05", "Carrefour FR", "EUR"),
            (1.25, "2025-01-20", "Leclerc", "EUR"),
        ],
    },
    {
        "product": Product(name="Camembert (250g)", category="zuivel", brand="Président", origin_country="FR"),
        "prices": [
            (1.89, "2020-03-01", "Carrefour FR", "EUR"),
            (1.99, "2021-06-10", "Leclerc", "EUR"),
            (2.19, "2022-09-15", "Carrefour FR", "EUR"),
            (2.49, "2023-05-20", "Leclerc", "EUR"),
            (2.69, "2024-08-12", "Carrefour FR", "EUR"),
            (2.89, "2025-02-01", "Leclerc", "EUR"),
        ],
    },

    # === SPANJE (EUR) ===
    {
        "product": Product(name="Aceite de oliva (1L)", category="voeding", origin_country="ES"),
        "prices": [
            (3.49, "2020-01-20", "Mercadona", "EUR"),
            (3.69, "2021-04-15", "Lidl ES", "EUR"),
            (4.99, "2022-07-10", "Mercadona", "EUR"),
            (7.49, "2023-10-05", "Lidl ES", "EUR"),
            (8.99, "2024-05-18", "Mercadona", "EUR"),
            (9.49, "2025-01-15", "Lidl ES", "EUR"),
        ],
    },
    {
        "product": Product(name="Pan blanco (barra)", category="brood", origin_country="ES"),
        "prices": [
            (0.65, "2020-02-15", "Mercadona", "EUR"),
            (0.70, "2021-05-20", "Lidl ES", "EUR"),
            (0.80, "2022-08-25", "Mercadona", "EUR"),
            (0.90, "2023-03-10", "Lidl ES", "EUR"),
            (0.95, "2024-06-15", "Mercadona", "EUR"),
            (1.05, "2025-01-20", "Lidl ES", "EUR"),
        ],
    },

    # === ITALIE (EUR) ===
    {
        "product": Product(name="Pasta Barilla (500g)", category="voeding", brand="Barilla", origin_country="IT"),
        "prices": [
            (0.69, "2020-01-10", "Coop IT", "EUR"),
            (0.75, "2021-04-22", "Esselunga", "EUR"),
            (0.99, "2022-08-30", "Coop IT", "EUR"),
            (1.19, "2023-05-15", "Esselunga", "EUR"),
            (1.29, "2024-10-01", "Coop IT", "EUR"),
            (1.35, "2025-02-20", "Esselunga", "EUR"),
        ],
    },
    {
        "product": Product(name="Parmigiano Reggiano (per kg)", category="zuivel", origin_country="IT"),
        "prices": [
            (15.90, "2020-02-15", "Esselunga", "EUR"),
            (16.50, "2021-05-20", "Coop IT", "EUR"),
            (17.90, "2022-08-25", "Esselunga", "EUR"),
            (19.50, "2023-03-10", "Coop IT", "EUR"),
            (20.90, "2024-06-15", "Esselunga", "EUR"),
            (22.50, "2025-01-20", "Coop IT", "EUR"),
        ],
    },

    # === PORTUGAL (EUR) ===
    {
        "product": Product(name="Bacalhau seco (per kg)", category="vlees", origin_country="PT"),
        "prices": [
            (9.99, "2020-01-15", "Pingo Doce", "EUR"),
            (10.99, "2021-04-10", "Pingo Doce", "EUR"),
            (12.49, "2022-07-20", "Pingo Doce", "EUR"),
            (13.99, "2023-10-01", "Pingo Doce", "EUR"),
            (14.99, "2024-06-15", "Pingo Doce", "EUR"),
            (15.99, "2025-01-10", "Pingo Doce", "EUR"),
        ],
    },

    # === VERENIGD KONINKRIJK (GBP) ===
    {
        "product": Product(name="Baked Beans (420g)", barcode="5000157000012", category="voeding", brand="Heinz", origin_country="GB"),
        "prices": [
            (0.65, "2020-03-20", "Tesco", "GBP"),
            (0.75, "2021-07-15", "Sainsbury's", "GBP"),
            (0.95, "2022-10-10", "Tesco", "GBP"),
            (1.10, "2023-04-05", "Sainsbury's", "GBP"),
            (1.20, "2024-06-18", "Tesco", "GBP"),
            (1.35, "2025-01-15", "Sainsbury's", "GBP"),
        ],
    },
    {
        "product": Product(name="Whole Milk (2 pints)", category="zuivel", origin_country="GB"),
        "prices": [
            (1.10, "2020-01-10", "Tesco", "GBP"),
            (1.15, "2021-04-22", "Sainsbury's", "GBP"),
            (1.35, "2022-08-30", "Tesco", "GBP"),
            (1.55, "2023-05-15", "Sainsbury's", "GBP"),
            (1.65, "2024-10-01", "Tesco", "GBP"),
            (1.75, "2025-02-20", "Sainsbury's", "GBP"),
        ],
    },
    {
        "product": Product(name="Fish and Chips (portie)", category="horeca", origin_country="GB"),
        "prices": [
            (6.50, "2020-02-15", "Tesco", "GBP"),
            (7.00, "2021-05-20", "Tesco", "GBP"),
            (7.99, "2022-08-25", "Tesco", "GBP"),
            (8.99, "2023-03-10", "Tesco", "GBP"),
            (9.50, "2024-06-15", "Tesco", "GBP"),
            (10.50, "2025-01-20", "Tesco", "GBP"),
        ],
    },
    {
        "product": Product(name="KFC Bucket (8 st.)", category="horeca", brand="KFC", origin_country="GB"),
        "prices": [
            (11.99, "2020-02-10", "KFC GB", "GBP"),
            (12.49, "2021-05-20", "KFC GB", "GBP"),
            (13.49, "2022-08-15", "KFC GB", "GBP"),
            (14.49, "2023-11-01", "KFC GB", "GBP"),
            (15.49, "2024-07-20", "KFC GB", "GBP"),
            (15.99, "2025-02-15", "KFC GB", "GBP"),
        ],
    },
    {
        "product": Product(name="Starbucks Caffe Latte (Grande)", category="dranken", brand="Starbucks", origin_country="GB"),
        "prices": [
            (3.25, "2020-01-15", "Starbucks GB", "GBP"),
            (3.45, "2021-04-10", "Starbucks GB", "GBP"),
            (3.65, "2022-07-20", "Starbucks GB", "GBP"),
            (3.95, "2023-10-01", "Starbucks GB", "GBP"),
            (4.25, "2024-06-15", "Starbucks GB", "GBP"),
            (4.55, "2025-01-10", "Starbucks GB", "GBP"),
        ],
    },

    # === IERLAND (EUR) ===
    {
        "product": Product(name="Kerrygold Butter (250g)", category="zuivel", brand="Kerrygold", origin_country="IE"),
        "prices": [
            (2.49, "2020-01-10", "Tesco IE", "EUR"),
            (2.69, "2021-04-22", "Tesco IE", "EUR"),
            (2.99, "2022-08-30", "Tesco IE", "EUR"),
            (3.29, "2023-05-15", "Tesco IE", "EUR"),
            (3.49, "2024-10-01", "Tesco IE", "EUR"),
            (3.69, "2025-02-20", "Tesco IE", "EUR"),
        ],
    },

    # === ZWEDEN (SEK) ===
    {
        "product": Product(name="Mjölk (1L)", category="zuivel", brand="Arla", origin_country="SE"),
        "prices": [
            (11.90, "2020-01-15", "ICA", "SEK"),
            (12.50, "2021-04-10", "ICA", "SEK"),
            (13.90, "2022-07-20", "ICA", "SEK"),
            (15.90, "2023-10-01", "ICA", "SEK"),
            (16.90, "2024-06-15", "ICA", "SEK"),
            (17.50, "2025-01-10", "ICA", "SEK"),
        ],
    },

    # === NOORWEGEN (NOK) ===
    {
        "product": Product(name="Melk (1L)", category="zuivel", brand="Tine", origin_country="NO"),
        "prices": [
            (17.90, "2020-01-20", "Rema 1000", "NOK"),
            (18.50, "2021-05-15", "Rema 1000", "NOK"),
            (19.90, "2022-08-10", "Rema 1000", "NOK"),
            (21.50, "2023-03-05", "Rema 1000", "NOK"),
            (22.90, "2024-07-12", "Rema 1000", "NOK"),
            (23.90, "2025-01-30", "Rema 1000", "NOK"),
        ],
    },

    # === ZWITSERLAND (CHF) ===
    {
        "product": Product(name="Milch (1L)", category="zuivel", origin_country="CH"),
        "prices": [
            (1.60, "2020-01-15", "Migros", "CHF"),
            (1.65, "2021-04-10", "Coop CH", "CHF"),
            (1.75, "2022-07-20", "Migros", "CHF"),
            (1.85, "2023-10-01", "Coop CH", "CHF"),
            (1.90, "2024-06-15", "Migros", "CHF"),
            (1.95, "2025-01-10", "Coop CH", "CHF"),
        ],
    },

    # === POLEN (PLN) ===
    {
        "product": Product(name="Chleb (brood, 500g)", category="brood", origin_country="PL"),
        "prices": [
            (2.99, "2020-01-10", "Biedronka", "PLN"),
            (3.29, "2021-04-22", "Biedronka", "PLN"),
            (3.99, "2022-08-30", "Biedronka", "PLN"),
            (4.99, "2023-05-15", "Biedronka", "PLN"),
            (5.49, "2024-10-01", "Biedronka", "PLN"),
            (5.99, "2025-02-20", "Biedronka", "PLN"),
        ],
    },

    # === TSJECHIE (CZK) ===
    {
        "product": Product(name="Rohlík (broodje, 10 st.)", category="brood", origin_country="CZ"),
        "prices": [
            (15.90, "2020-02-01", "Albert CZ", "CZK"),
            (17.90, "2021-05-15", "Albert CZ", "CZK"),
            (21.90, "2022-08-20", "Albert CZ", "CZK"),
            (24.90, "2023-03-10", "Albert CZ", "CZK"),
            (27.90, "2024-06-05", "Albert CZ", "CZK"),
            (29.90, "2025-01-20", "Albert CZ", "CZK"),
        ],
    },

    # === GRIEKENLAND (EUR) ===
    {
        "product": Product(name="Feta kaas (per kg)", category="zuivel", origin_country="GR"),
        "prices": [
            (7.99, "2020-01-15", "Sklavenitis", "EUR"),
            (8.49, "2021-04-10", "Sklavenitis", "EUR"),
            (9.49, "2022-07-20", "Sklavenitis", "EUR"),
            (10.49, "2023-10-01", "Sklavenitis", "EUR"),
            (11.49, "2024-06-15", "Sklavenitis", "EUR"),
            (12.49, "2025-01-10", "Sklavenitis", "EUR"),
        ],
    },

    # === TURKIJE (TRY) - Hoge inflatie! ===
    {
        "product": Product(name="Big Mac", category="horeca", brand="McDonald's", origin_country="TR"),
        "prices": [
            (14.99, "2020-01-15", "McDonald's TR", "TRY"),
            (19.99, "2021-04-10", "McDonald's TR", "TRY"),
            (34.99, "2022-07-20", "McDonald's TR", "TRY"),
            (69.99, "2023-10-01", "McDonald's TR", "TRY"),
            (109.99, "2024-06-15", "McDonald's TR", "TRY"),
            (149.99, "2025-01-10", "McDonald's TR", "TRY"),
        ],
    },
    {
        "product": Product(name="Süt (1L melk)", category="zuivel", origin_country="TR"),
        "prices": [
            (4.50, "2020-02-01", "Migros TR", "TRY"),
            (6.50, "2021-05-15", "BIM", "TRY"),
            (12.90, "2022-08-20", "Migros TR", "TRY"),
            (22.90, "2023-03-10", "BIM", "TRY"),
            (34.90, "2024-06-05", "Migros TR", "TRY"),
            (42.90, "2025-01-20", "Migros TR", "TRY"),
        ],
    },
    {
        "product": Product(name="Ekmek (brood)", category="brood", origin_country="TR"),
        "prices": [
            (1.50, "2020-01-20", "BIM", "TRY"),
            (2.00, "2021-05-15", "Migros TR", "TRY"),
            (3.50, "2022-08-10", "BIM", "TRY"),
            (7.00, "2023-03-05", "Migros TR", "TRY"),
            (10.00, "2024-07-12", "BIM", "TRY"),
            (13.00, "2025-01-30", "Migros TR", "TRY"),
        ],
    },

    # === RUSLAND (RUB) ===
    {
        "product": Product(name="Moloko (melk, 1L)", category="zuivel", origin_country="RU"),
        "prices": [
            (59.0, "2020-01-15", "Pyaterochka", "RUB"),
            (65.0, "2021-04-10", "Pyaterochka", "RUB"),
            (79.0, "2022-07-20", "Pyaterochka", "RUB"),
            (89.0, "2023-10-01", "Pyaterochka", "RUB"),
            (99.0, "2024-06-15", "Pyaterochka", "RUB"),
            (109.0, "2025-01-10", "Pyaterochka", "RUB"),
        ],
    },

    # === OEKRAINE (UAH) ===
    {
        "product": Product(name="Khlib (brood)", category="brood", origin_country="UA"),
        "prices": [
            (12.0, "2020-01-10", "ATB Market", "UAH"),
            (14.0, "2021-04-22", "ATB Market", "UAH"),
            (18.0, "2022-08-30", "ATB Market", "UAH"),
            (25.0, "2023-05-15", "ATB Market", "UAH"),
            (30.0, "2024-10-01", "ATB Market", "UAH"),
            (35.0, "2025-02-20", "ATB Market", "UAH"),
        ],
    },

    # === ROEMENIE (RON) ===
    {
        "product": Product(name="Pâine albă (wit brood)", category="brood", origin_country="RO"),
        "prices": [
            (2.50, "2020-01-15", "Kaufland RO", "RON"),
            (2.80, "2021-04-10", "Kaufland RO", "RON"),
            (3.50, "2022-07-20", "Kaufland RO", "RON"),
            (4.20, "2023-10-01", "Kaufland RO", "RON"),
            (4.80, "2024-06-15", "Kaufland RO", "RON"),
            (5.20, "2025-01-10", "Kaufland RO", "RON"),
        ],
    },

    # === HONGARIJE (HUF) ===
    {
        "product": Product(name="Tej (melk, 1L)", category="zuivel", origin_country="HU"),
        "prices": [
            (279.0, "2020-01-10", "Spar HU", "HUF"),
            (299.0, "2021-04-22", "Spar HU", "HUF"),
            (399.0, "2022-08-30", "Spar HU", "HUF"),
            (479.0, "2023-05-15", "Spar HU", "HUF"),
            (519.0, "2024-10-01", "Spar HU", "HUF"),
            (549.0, "2025-02-20", "Spar HU", "HUF"),
        ],
    },

    # === KROATIE (EUR, sinds 2023) ===
    {
        "product": Product(name="Mlijeko (melk, 1L)", category="zuivel", origin_country="HR"),
        "prices": [
            (5.99, "2020-01-15", "Konzum", "HRK"),
            (6.49, "2021-04-10", "Konzum", "HRK"),
            (7.49, "2022-07-20", "Konzum", "HRK"),
            (1.10, "2023-10-01", "Konzum", "EUR"),
            (1.19, "2024-06-15", "Konzum", "EUR"),
            (1.25, "2025-01-10", "Konzum", "EUR"),
        ],
    },

    # ============================================================
    #  NOORD-AMERIKA
    # ============================================================

    # === VERENIGDE STATEN (USD) ===
    {
        "product": Product(name="Big Mac (US)", category="horeca", brand="McDonald's", origin_country="US"),
        "prices": [
            (3.99, "2020-01-15", "McDonald's US", "USD"),
            (4.29, "2021-03-10", "McDonald's US", "USD"),
            (4.69, "2022-06-20", "McDonald's US", "USD"),
            (5.15, "2023-09-01", "McDonald's US", "USD"),
            (5.49, "2024-06-15", "McDonald's US", "USD"),
            (5.89, "2025-01-10", "McDonald's US", "USD"),
        ],
    },
    {
        "product": Product(name="Gallon Milk (US)", barcode="0041130001234", category="zuivel", brand="Great Value", origin_country="US"),
        "prices": [
            (2.78, "2020-02-01", "Walmart US", "USD"),
            (3.09, "2021-04-15", "Kroger", "USD"),
            (3.59, "2022-07-20", "ShopRite", "USD"),
            (3.89, "2023-03-10", "Walmart US", "USD"),
            (4.09, "2024-01-05", "Kroger", "USD"),
            (4.29, "2025-02-18", "ShopRite", "USD"),
        ],
    },
    {
        "product": Product(name="Dozen Eggs (US)", barcode="0041130005678", category="voeding", origin_country="US"),
        "prices": [
            (1.47, "2020-01-20", "Walmart US", "USD"),
            (1.79, "2021-05-15", "Kroger", "USD"),
            (2.87, "2022-03-10", "ShopRite", "USD"),
            (4.82, "2023-01-10", "Walmart US", "USD"),
            (3.59, "2024-04-18", "Kroger", "USD"),
            (4.15, "2025-02-01", "ShopRite", "USD"),
        ],
    },
    {
        "product": Product(name="Whopper (US)", category="horeca", brand="Burger King", origin_country="US"),
        "prices": [
            (4.19, "2020-02-10", "Burger King US", "USD"),
            (4.49, "2021-05-20", "Burger King US", "USD"),
            (4.99, "2022-08-15", "Burger King US", "USD"),
            (5.49, "2023-11-01", "Burger King US", "USD"),
            (5.99, "2024-07-20", "Burger King US", "USD"),
            (6.49, "2025-02-15", "Burger King US", "USD"),
        ],
    },
    {
        "product": Product(name="Starbucks Caffe Latte (Grande, US)", category="dranken", brand="Starbucks", origin_country="US"),
        "prices": [
            (3.95, "2020-01-15", "Starbucks US", "USD"),
            (4.15, "2021-04-10", "Starbucks US", "USD"),
            (4.45, "2022-07-20", "Starbucks US", "USD"),
            (4.95, "2023-10-01", "Starbucks US", "USD"),
            (5.45, "2024-06-15", "Starbucks US", "USD"),
            (5.95, "2025-01-10", "Starbucks US", "USD"),
        ],
    },

    # === CANADA (CAD) ===
    {
        "product": Product(name="Brood wit (CA)", barcode="0062150012345", category="brood", brand="Wonder", origin_country="CA"),
        "prices": [
            (2.49, "2020-03-01", "Loblaws", "CAD"),
            (2.69, "2021-06-10", "No Frills", "CAD"),
            (2.99, "2022-09-15", "Loblaws", "CAD"),
            (3.29, "2023-05-20", "No Frills", "CAD"),
            (3.49, "2024-08-12", "Loblaws", "CAD"),
            (3.79, "2025-01-25", "No Frills", "CAD"),
        ],
    },
    {
        "product": Product(name="Double Double Coffee", category="dranken", brand="Tim Hortons", origin_country="CA"),
        "prices": [
            (1.62, "2020-01-10", "Tim Hortons", "CAD"),
            (1.72, "2021-04-22", "Tim Hortons", "CAD"),
            (1.82, "2022-08-30", "Tim Hortons", "CAD"),
            (1.92, "2023-05-15", "Tim Hortons", "CAD"),
            (2.02, "2024-10-01", "Tim Hortons", "CAD"),
            (2.17, "2025-02-20", "Tim Hortons", "CAD"),
        ],
    },

    # === MEXICO (MXN) ===
    {
        "product": Product(name="Big Mac (MX)", category="horeca", brand="McDonald's", origin_country="MX"),
        "prices": [
            (49.0, "2020-01-15", "McDonald's MX", "MXN"),
            (55.0, "2021-04-10", "McDonald's MX", "MXN"),
            (62.0, "2022-07-20", "McDonald's MX", "MXN"),
            (72.0, "2023-10-01", "McDonald's MX", "MXN"),
            (82.0, "2024-06-15", "McDonald's MX", "MXN"),
            (89.0, "2025-01-10", "McDonald's MX", "MXN"),
        ],
    },
    {
        "product": Product(name="Tortillas de maíz (1kg)", category="voeding", origin_country="MX"),
        "prices": [
            (13.0, "2020-02-01", "Walmart MX", "MXN"),
            (14.0, "2021-05-15", "Soriana", "MXN"),
            (16.0, "2022-08-20", "Walmart MX", "MXN"),
            (18.0, "2023-03-10", "Soriana", "MXN"),
            (20.0, "2024-06-05", "Walmart MX", "MXN"),
            (22.0, "2025-01-20", "Soriana", "MXN"),
        ],
    },
    {
        "product": Product(name="Frijoles (1kg)", category="voeding", origin_country="MX"),
        "prices": [
            (22.0, "2020-01-20", "Walmart MX", "MXN"),
            (25.0, "2021-05-15", "Soriana", "MXN"),
            (29.0, "2022-08-10", "Walmart MX", "MXN"),
            (35.0, "2023-03-05", "Soriana", "MXN"),
            (39.0, "2024-07-12", "Walmart MX", "MXN"),
            (42.0, "2025-01-30", "Soriana", "MXN"),
        ],
    },

    # === EL SALVADOR (USD) ===
    {
        "product": Product(name="Pupusas (3 stuks)", category="voeding", origin_country="SV"),
        "prices": [
            (0.75, "2020-01-15", "Super Selectos", "USD"),
            (0.85, "2021-04-10", "Super Selectos", "USD"),
            (1.00, "2022-07-20", "Super Selectos", "USD"),
            (1.15, "2023-10-01", "Super Selectos", "USD"),
            (1.25, "2024-06-15", "Super Selectos", "USD"),
            (1.50, "2025-01-10", "Super Selectos", "USD"),
        ],
    },
    {
        "product": Product(name="Arroz (rijst, 5 lbs)", category="voeding", origin_country="SV"),
        "prices": [
            (2.25, "2020-02-01", "Super Selectos", "USD"),
            (2.50, "2021-05-15", "Super Selectos", "USD"),
            (2.85, "2022-08-20", "Super Selectos", "USD"),
            (3.25, "2023-03-10", "Super Selectos", "USD"),
            (3.50, "2024-06-05", "Super Selectos", "USD"),
            (3.75, "2025-01-20", "Super Selectos", "USD"),
        ],
    },

    # === PANAMA (USD/PAB) ===
    {
        "product": Product(name="Arroz (rijst, 5 lbs)", category="voeding", origin_country="PA"),
        "prices": [
            (2.99, "2020-01-20", "Super 99", "USD"),
            (3.25, "2021-05-15", "Super 99", "USD"),
            (3.59, "2022-08-10", "Super 99", "USD"),
            (3.99, "2023-03-05", "Super 99", "USD"),
            (4.25, "2024-07-12", "Super 99", "USD"),
            (4.49, "2025-01-30", "Super 99", "USD"),
        ],
    },
    {
        "product": Product(name="Leche (melk, 1L)", category="zuivel", origin_country="PA"),
        "prices": [
            (1.15, "2020-02-15", "Super 99", "USD"),
            (1.25, "2021-05-20", "Super 99", "USD"),
            (1.39, "2022-08-25", "Super 99", "USD"),
            (1.49, "2023-03-10", "Super 99", "USD"),
            (1.59, "2024-06-15", "Super 99", "USD"),
            (1.69, "2025-01-20", "Super 99", "USD"),
        ],
    },

    # === COSTA RICA (CRC) ===
    {
        "product": Product(name="Gallo Pinto (portie)", category="voeding", origin_country="CR"),
        "prices": [
            (1500.0, "2020-01-10", "AutoMercado", "CRC"),
            (1650.0, "2021-04-22", "AutoMercado", "CRC"),
            (1850.0, "2022-08-30", "AutoMercado", "CRC"),
            (2100.0, "2023-05-15", "AutoMercado", "CRC"),
            (2350.0, "2024-10-01", "AutoMercado", "CRC"),
            (2500.0, "2025-02-20", "AutoMercado", "CRC"),
        ],
    },

    # === GUATEMALA (GTQ) ===
    {
        "product": Product(name="Frijoles (1 lb)", category="voeding", origin_country="GT"),
        "prices": [
            (5.50, "2020-01-15", "La Torre", "GTQ"),
            (6.00, "2021-04-10", "La Torre", "GTQ"),
            (7.00, "2022-07-20", "La Torre", "GTQ"),
            (8.00, "2023-10-01", "La Torre", "GTQ"),
            (8.50, "2024-06-15", "La Torre", "GTQ"),
            (9.00, "2025-01-10", "La Torre", "GTQ"),
        ],
    },

    # === JAMAICA (JMD) ===
    {
        "product": Product(name="Ackee & Saltfish (blik)", category="voeding", origin_country="JM"),
        "prices": [
            (450.0, "2020-02-01", "Hi-Lo", "JMD"),
            (520.0, "2021-05-15", "Hi-Lo", "JMD"),
            (620.0, "2022-08-20", "Hi-Lo", "JMD"),
            (750.0, "2023-03-10", "Hi-Lo", "JMD"),
            (850.0, "2024-06-05", "Hi-Lo", "JMD"),
            (950.0, "2025-01-20", "Hi-Lo", "JMD"),
        ],
    },

    # === DOMINICAANSE REPUBLIEK (DOP) ===
    {
        "product": Product(name="Arroz (rijst, 5 lbs)", category="voeding", origin_country="DO"),
        "prices": [
            (135.0, "2020-01-20", "Jumbo DO", "DOP"),
            (145.0, "2021-05-15", "Jumbo DO", "DOP"),
            (175.0, "2022-08-10", "Jumbo DO", "DOP"),
            (195.0, "2023-03-05", "Jumbo DO", "DOP"),
            (210.0, "2024-07-12", "Jumbo DO", "DOP"),
            (225.0, "2025-01-30", "Jumbo DO", "DOP"),
        ],
    },

    # ============================================================
    #  ZUID-AMERIKA
    # ============================================================

    # === BRAZILIE (BRL) ===
    {
        "product": Product(name="Big Mac (BR)", category="horeca", brand="McDonald's", origin_country="BR"),
        "prices": [
            (16.90, "2020-01-15", "McDonald's BR", "BRL"),
            (18.90, "2021-04-10", "McDonald's BR", "BRL"),
            (22.90, "2022-07-20", "McDonald's BR", "BRL"),
            (27.90, "2023-10-01", "McDonald's BR", "BRL"),
            (30.90, "2024-06-15", "McDonald's BR", "BRL"),
            (33.90, "2025-01-10", "McDonald's BR", "BRL"),
        ],
    },
    {
        "product": Product(name="Arroz (5kg)", category="voeding", origin_country="BR"),
        "prices": [
            (12.99, "2020-02-01", "Carrefour BR", "BRL"),
            (14.99, "2021-05-15", "Pao de Acucar", "BRL"),
            (22.99, "2022-08-20", "Carrefour BR", "BRL"),
            (25.99, "2023-03-10", "Pao de Acucar", "BRL"),
            (27.99, "2024-06-05", "Carrefour BR", "BRL"),
            (29.99, "2025-01-20", "Pao de Acucar", "BRL"),
        ],
    },
    {
        "product": Product(name="Feijão preto (1kg)", category="voeding", origin_country="BR"),
        "prices": [
            (4.99, "2020-01-20", "Carrefour BR", "BRL"),
            (5.99, "2021-05-15", "Pao de Acucar", "BRL"),
            (7.99, "2022-08-10", "Carrefour BR", "BRL"),
            (8.99, "2023-03-05", "Pao de Acucar", "BRL"),
            (9.49, "2024-07-12", "Carrefour BR", "BRL"),
            (10.49, "2025-01-30", "Carrefour BR", "BRL"),
        ],
    },

    # === ARGENTINIE (ARS) - Extreme inflatie! ===
    {
        "product": Product(name="Leche (melk, 1L)", category="zuivel", origin_country="AR"),
        "prices": [
            (55.0, "2020-01-15", "Carrefour AR", "ARS"),
            (89.0, "2021-04-10", "Carrefour AR", "ARS"),
            (159.0, "2022-07-20", "Carrefour AR", "ARS"),
            (349.0, "2023-10-01", "Carrefour AR", "ARS"),
            (890.0, "2024-06-15", "Carrefour AR", "ARS"),
            (1450.0, "2025-01-10", "Carrefour AR", "ARS"),
        ],
    },
    {
        "product": Product(name="Pan francés (stokbrood)", category="brood", origin_country="AR"),
        "prices": [
            (80.0, "2020-02-01", "Carrefour AR", "ARS"),
            (130.0, "2021-05-15", "Carrefour AR", "ARS"),
            (250.0, "2022-08-20", "Carrefour AR", "ARS"),
            (550.0, "2023-03-10", "Carrefour AR", "ARS"),
            (1200.0, "2024-06-05", "Carrefour AR", "ARS"),
            (1900.0, "2025-01-20", "Carrefour AR", "ARS"),
        ],
    },

    # === COLOMBIA (COP) ===
    {
        "product": Product(name="Arroz (5 lbs)", category="voeding", origin_country="CO"),
        "prices": [
            (6500.0, "2020-01-20", "Exito", "COP"),
            (7200.0, "2021-05-15", "Exito", "COP"),
            (8500.0, "2022-08-10", "Exito", "COP"),
            (9800.0, "2023-03-05", "Exito", "COP"),
            (10500.0, "2024-07-12", "Exito", "COP"),
            (11200.0, "2025-01-30", "Exito", "COP"),
        ],
    },

    # === CHILI (CLP) ===
    {
        "product": Product(name="Pan (brood, 1kg)", category="brood", origin_country="CL"),
        "prices": [
            (990.0, "2020-01-15", "Lider", "CLP"),
            (1090.0, "2021-04-10", "Lider", "CLP"),
            (1290.0, "2022-07-20", "Lider", "CLP"),
            (1490.0, "2023-10-01", "Lider", "CLP"),
            (1590.0, "2024-06-15", "Lider", "CLP"),
            (1690.0, "2025-01-10", "Lider", "CLP"),
        ],
    },

    # === PERU (PEN) ===
    {
        "product": Product(name="Arroz (5kg)", category="voeding", origin_country="PE"),
        "prices": [
            (14.50, "2020-01-10", "Wong", "PEN"),
            (15.90, "2021-04-22", "Wong", "PEN"),
            (18.50, "2022-08-30", "Wong", "PEN"),
            (20.90, "2023-05-15", "Wong", "PEN"),
            (22.50, "2024-10-01", "Wong", "PEN"),
            (24.90, "2025-02-20", "Wong", "PEN"),
        ],
    },

    # === SURINAME (SRD/USD) ===
    {
        "product": Product(name="Rijst (5kg)", category="voeding", origin_country="SR"),
        "prices": [
            (4.50, "2020-01-15", "Fernandes", "USD"),
            (5.00, "2021-04-10", "Fernandes", "USD"),
            (5.99, "2022-07-20", "Fernandes", "USD"),
            (6.99, "2023-10-01", "Fernandes", "USD"),
            (7.50, "2024-06-15", "Fernandes", "USD"),
            (8.25, "2025-01-10", "Fernandes", "USD"),
        ],
    },

    # === VENEZUELA (VES) - Hyperinflatie ===
    {
        "product": Product(name="Harina P.A.N. (1kg)", category="voeding", brand="P.A.N.", origin_country="VE"),
        "prices": [
            (1.20, "2020-01-20", "Excelsior Gama", "USD"),
            (1.50, "2021-05-15", "Excelsior Gama", "USD"),
            (1.80, "2022-08-10", "Excelsior Gama", "USD"),
            (2.20, "2023-03-05", "Excelsior Gama", "USD"),
            (2.80, "2024-07-12", "Excelsior Gama", "USD"),
            (3.50, "2025-01-30", "Excelsior Gama", "USD"),
        ],
    },

    # === URUGUAY (UYU) ===
    {
        "product": Product(name="Leche (melk, 1L)", category="zuivel", brand="Conaprole", origin_country="UY"),
        "prices": [
            (32.0, "2020-01-15", "Tienda Inglesa", "UYU"),
            (35.0, "2021-04-10", "Tienda Inglesa", "UYU"),
            (42.0, "2022-07-20", "Tienda Inglesa", "UYU"),
            (49.0, "2023-10-01", "Tienda Inglesa", "UYU"),
            (55.0, "2024-06-15", "Tienda Inglesa", "UYU"),
            (62.0, "2025-01-10", "Tienda Inglesa", "UYU"),
        ],
    },

    # === ECUADOR (USD) ===
    {
        "product": Product(name="Arroz (5 lbs)", category="voeding", origin_country="EC"),
        "prices": [
            (2.85, "2020-02-01", "Supermaxi", "USD"),
            (3.10, "2021-05-15", "Supermaxi", "USD"),
            (3.45, "2022-08-20", "Supermaxi", "USD"),
            (3.80, "2023-03-10", "Supermaxi", "USD"),
            (4.10, "2024-06-05", "Supermaxi", "USD"),
            (4.35, "2025-01-20", "Supermaxi", "USD"),
        ],
    },

    # === BOLIVIA (BOB) ===
    {
        "product": Product(name="Pan de batalla (brood)", category="brood", origin_country="BO"),
        "prices": [
            (0.50, "2020-01-20", "Hipermaxi", "BOB"),
            (0.50, "2021-05-15", "Hipermaxi", "BOB"),
            (0.60, "2022-08-10", "Hipermaxi", "BOB"),
            (0.70, "2023-03-05", "Hipermaxi", "BOB"),
            (0.80, "2024-07-12", "Hipermaxi", "BOB"),
            (0.90, "2025-01-30", "Hipermaxi", "BOB"),
        ],
    },

    # === PARAGUAY (PYG) ===
    {
        "product": Product(name="Leche (melk, 1L)", category="zuivel", origin_country="PY"),
        "prices": [
            (5500.0, "2020-01-15", "Superseis", "PYG"),
            (5900.0, "2021-04-10", "Superseis", "PYG"),
            (6800.0, "2022-07-20", "Superseis", "PYG"),
            (7500.0, "2023-10-01", "Superseis", "PYG"),
            (8200.0, "2024-06-15", "Superseis", "PYG"),
            (8900.0, "2025-01-10", "Superseis", "PYG"),
        ],
    },

    # ============================================================
    #  MIDDEN-OOSTEN
    # ============================================================

    # === SAOEDI-ARABIE (SAR) ===
    {
        "product": Product(name="Big Mac (SA)", category="horeca", brand="McDonald's", origin_country="SA"),
        "prices": [
            (14.0, "2020-01-15", "McDonald's SA", "SAR"),
            (15.0, "2021-04-10", "McDonald's SA", "SAR"),
            (16.0, "2022-07-20", "McDonald's SA", "SAR"),
            (17.0, "2023-10-01", "McDonald's SA", "SAR"),
            (18.0, "2024-06-15", "McDonald's SA", "SAR"),
            (19.0, "2025-01-10", "McDonald's SA", "SAR"),
        ],
    },
    {
        "product": Product(name="Rijst Basmati (5kg)", category="voeding", origin_country="SA"),
        "prices": [
            (22.0, "2020-02-01", "Tamimi Markets", "SAR"),
            (24.0, "2021-05-15", "Tamimi Markets", "SAR"),
            (27.0, "2022-08-20", "Tamimi Markets", "SAR"),
            (30.0, "2023-03-10", "Tamimi Markets", "SAR"),
            (32.0, "2024-06-05", "Tamimi Markets", "SAR"),
            (34.0, "2025-01-20", "Tamimi Markets", "SAR"),
        ],
    },

    # === VAE (AED) ===
    {
        "product": Product(name="Laban (yoghurt, 1L)", category="zuivel", brand="Al Ain", origin_country="AE"),
        "prices": [
            (4.50, "2020-01-20", "Carrefour AE", "AED"),
            (4.75, "2021-05-15", "Lulu Hypermarket", "AED"),
            (5.25, "2022-08-10", "Carrefour AE", "AED"),
            (5.75, "2023-03-05", "Lulu Hypermarket", "AED"),
            (6.00, "2024-07-12", "Carrefour AE", "AED"),
            (6.50, "2025-01-30", "Lulu Hypermarket", "AED"),
        ],
    },
    {
        "product": Product(name="Shawarma (portie)", category="horeca", origin_country="AE"),
        "prices": [
            (10.0, "2020-01-15", "Carrefour AE", "AED"),
            (11.0, "2021-04-10", "Carrefour AE", "AED"),
            (12.0, "2022-07-20", "Carrefour AE", "AED"),
            (14.0, "2023-10-01", "Carrefour AE", "AED"),
            (15.0, "2024-06-15", "Carrefour AE", "AED"),
            (16.0, "2025-01-10", "Carrefour AE", "AED"),
        ],
    },

    # === ISRAEL (ILS) ===
    {
        "product": Product(name="Chalav (melk, 1L)", category="zuivel", brand="Tnuva", origin_country="IL"),
        "prices": [
            (5.90, "2020-01-10", "Shufersal", "ILS"),
            (6.30, "2021-04-22", "Shufersal", "ILS"),
            (6.90, "2022-08-30", "Shufersal", "ILS"),
            (7.50, "2023-05-15", "Shufersal", "ILS"),
            (7.90, "2024-10-01", "Shufersal", "ILS"),
            (8.50, "2025-02-20", "Shufersal", "ILS"),
        ],
    },
    {
        "product": Product(name="Hummus (400g)", category="voeding", origin_country="IL"),
        "prices": [
            (8.90, "2020-02-15", "Shufersal", "ILS"),
            (9.50, "2021-05-20", "Shufersal", "ILS"),
            (10.90, "2022-08-25", "Shufersal", "ILS"),
            (12.50, "2023-03-10", "Shufersal", "ILS"),
            (13.90, "2024-06-15", "Shufersal", "ILS"),
            (14.90, "2025-01-20", "Shufersal", "ILS"),
        ],
    },

    # === QATAR (QAR) ===
    {
        "product": Product(name="Rijst Basmati (5kg)", category="voeding", origin_country="QA"),
        "prices": [
            (18.0, "2020-01-15", "Al Meera", "QAR"),
            (19.5, "2021-04-10", "Al Meera", "QAR"),
            (21.0, "2022-07-20", "Al Meera", "QAR"),
            (23.0, "2023-10-01", "Al Meera", "QAR"),
            (24.5, "2024-06-15", "Al Meera", "QAR"),
            (26.0, "2025-01-10", "Al Meera", "QAR"),
        ],
    },

    # === KOEWEIT (KWD) ===
    {
        "product": Product(name="Melk (1L)", category="zuivel", origin_country="KW"),
        "prices": [
            (0.35, "2020-02-01", "The Sultan Center", "KWD"),
            (0.38, "2021-05-15", "The Sultan Center", "KWD"),
            (0.42, "2022-08-20", "The Sultan Center", "KWD"),
            (0.45, "2023-03-10", "The Sultan Center", "KWD"),
            (0.48, "2024-06-05", "The Sultan Center", "KWD"),
            (0.50, "2025-01-20", "The Sultan Center", "KWD"),
        ],
    },

    # === JORDANIE (JOD) ===
    {
        "product": Product(name="Khubz (brood)", category="brood", origin_country="JO"),
        "prices": [
            (0.25, "2020-01-20", "Carrefour JO", "JOD"),
            (0.25, "2021-05-15", "Carrefour JO", "JOD"),
            (0.30, "2022-08-10", "Carrefour JO", "JOD"),
            (0.35, "2023-03-05", "Carrefour JO", "JOD"),
            (0.35, "2024-07-12", "Carrefour JO", "JOD"),
            (0.40, "2025-01-30", "Carrefour JO", "JOD"),
        ],
    },

    # === EGYPTE (EGP) - Hoge inflatie ===
    {
        "product": Product(name="Big Mac (EG)", category="horeca", brand="McDonald's", origin_country="EG"),
        "prices": [
            (40.0, "2020-01-15", "McDonald's EG", "EGP"),
            (45.0, "2021-04-10", "McDonald's EG", "EGP"),
            (55.0, "2022-07-20", "McDonald's EG", "EGP"),
            (85.0, "2023-10-01", "McDonald's EG", "EGP"),
            (130.0, "2024-06-15", "McDonald's EG", "EGP"),
            (165.0, "2025-01-10", "McDonald's EG", "EGP"),
        ],
    },
    {
        "product": Product(name="Eish (brood, 10 st.)", category="brood", origin_country="EG"),
        "prices": [
            (5.0, "2020-02-01", "Carrefour EG", "EGP"),
            (5.0, "2021-05-15", "Carrefour EG", "EGP"),
            (10.0, "2022-08-20", "Carrefour EG", "EGP"),
            (15.0, "2023-03-10", "Carrefour EG", "EGP"),
            (20.0, "2024-06-05", "Carrefour EG", "EGP"),
            (25.0, "2025-01-20", "Carrefour EG", "EGP"),
        ],
    },

    # === LIBANON (LBP/USD) ===
    {
        "product": Product(name="Brood (rabta)", category="brood", origin_country="LB"),
        "prices": [
            (1.00, "2020-01-20", "Spinneys LB", "USD"),
            (1.00, "2021-05-15", "Spinneys LB", "USD"),
            (1.50, "2022-08-10", "Spinneys LB", "USD"),
            (2.00, "2023-03-05", "Spinneys LB", "USD"),
            (2.50, "2024-07-12", "Spinneys LB", "USD"),
            (2.50, "2025-01-30", "Spinneys LB", "USD"),
        ],
    },

    # ============================================================
    #  AZIE
    # ============================================================

    # === INDIA (INR) ===
    {
        "product": Product(name="Atta Wheat Flour (5kg)", barcode="8901058000012", category="voeding", brand="Aashirvaad", origin_country="IN"),
        "prices": [
            (225.0, "2020-02-15", "Reliance Fresh", "INR"),
            (240.0, "2021-03-20", "Big Bazaar", "INR"),
            (270.0, "2022-05-10", "Reliance Fresh", "INR"),
            (299.0, "2023-08-25", "Big Bazaar", "INR"),
            (315.0, "2024-07-12", "Reliance Fresh", "INR"),
            (335.0, "2025-01-30", "Big Bazaar", "INR"),
        ],
    },
    {
        "product": Product(name="Amul Butter (500g)", barcode="8901058001234", category="zuivel", brand="Amul", origin_country="IN"),
        "prices": [
            (210.0, "2020-01-10", "Reliance Fresh", "INR"),
            (220.0, "2021-04-22", "Big Bazaar", "INR"),
            (240.0, "2022-08-30", "Reliance Fresh", "INR"),
            (260.0, "2023-05-15", "Big Bazaar", "INR"),
            (275.0, "2024-10-01", "Reliance Fresh", "INR"),
            (295.0, "2025-02-20", "Big Bazaar", "INR"),
        ],
    },
    {
        "product": Product(name="Big Mac (IN) - Maharaja Mac", category="horeca", brand="McDonald's", origin_country="IN"),
        "prices": [
            (179.0, "2020-01-15", "McDonald's IN", "INR"),
            (189.0, "2021-04-10", "McDonald's IN", "INR"),
            (209.0, "2022-07-20", "McDonald's IN", "INR"),
            (229.0, "2023-10-01", "McDonald's IN", "INR"),
            (249.0, "2024-06-15", "McDonald's IN", "INR"),
            (269.0, "2025-01-10", "McDonald's IN", "INR"),
        ],
    },
    {
        "product": Product(name="Toor Dal (1kg)", category="voeding", origin_country="IN"),
        "prices": [
            (89.0, "2020-02-01", "Reliance Fresh", "INR"),
            (99.0, "2021-05-15", "Big Bazaar", "INR"),
            (119.0, "2022-08-20", "Reliance Fresh", "INR"),
            (145.0, "2023-03-10", "Big Bazaar", "INR"),
            (165.0, "2024-06-05", "Reliance Fresh", "INR"),
            (179.0, "2025-01-20", "Big Bazaar", "INR"),
        ],
    },

    # === JAPAN (JPY) ===
    {
        "product": Product(name="Big Mac (JP)", category="horeca", brand="McDonald's", origin_country="JP"),
        "prices": [
            (390.0, "2020-01-15", "McDonald's JP", "JPY"),
            (390.0, "2021-04-10", "McDonald's JP", "JPY"),
            (410.0, "2022-07-20", "McDonald's JP", "JPY"),
            (450.0, "2023-10-01", "McDonald's JP", "JPY"),
            (480.0, "2024-06-15", "McDonald's JP", "JPY"),
            (500.0, "2025-01-10", "McDonald's JP", "JPY"),
        ],
    },
    {
        "product": Product(name="Gohan (rijst, 5kg)", category="voeding", origin_country="JP"),
        "prices": [
            (1780.0, "2020-02-01", "Aeon", "JPY"),
            (1850.0, "2021-05-15", "7-Eleven JP", "JPY"),
            (1980.0, "2022-08-20", "Aeon", "JPY"),
            (2180.0, "2023-03-10", "Aeon", "JPY"),
            (2380.0, "2024-06-05", "7-Eleven JP", "JPY"),
            (2580.0, "2025-01-20", "Aeon", "JPY"),
        ],
    },
    {
        "product": Product(name="Gyunyu (melk, 1L)", category="zuivel", origin_country="JP"),
        "prices": [
            (178.0, "2020-01-10", "Aeon", "JPY"),
            (185.0, "2021-04-22", "7-Eleven JP", "JPY"),
            (198.0, "2022-08-30", "Aeon", "JPY"),
            (218.0, "2023-05-15", "7-Eleven JP", "JPY"),
            (238.0, "2024-10-01", "Aeon", "JPY"),
            (258.0, "2025-02-20", "7-Eleven JP", "JPY"),
        ],
    },
    {
        "product": Product(name="Starbucks Caffe Latte (JP)", category="dranken", brand="Starbucks", origin_country="JP"),
        "prices": [
            (420.0, "2020-01-15", "Starbucks JP", "JPY"),
            (440.0, "2021-04-10", "Starbucks JP", "JPY"),
            (460.0, "2022-07-20", "Starbucks JP", "JPY"),
            (490.0, "2023-10-01", "Starbucks JP", "JPY"),
            (520.0, "2024-06-15", "Starbucks JP", "JPY"),
            (550.0, "2025-01-10", "Starbucks JP", "JPY"),
        ],
    },

    # === CHINA (CNY) ===
    {
        "product": Product(name="大米 (rijst, 5kg)", category="voeding", origin_country="CN"),
        "prices": [
            (29.90, "2020-01-20", "Walmart CN", "CNY"),
            (31.90, "2021-05-15", "Hema", "CNY"),
            (34.90, "2022-08-10", "Walmart CN", "CNY"),
            (36.90, "2023-03-05", "Hema", "CNY"),
            (38.90, "2024-07-12", "Walmart CN", "CNY"),
            (39.90, "2025-01-30", "Hema", "CNY"),
        ],
    },
    {
        "product": Product(name="牛奶 (melk, 1L)", category="zuivel", origin_country="CN"),
        "prices": [
            (6.50, "2020-02-15", "Walmart CN", "CNY"),
            (6.90, "2021-05-20", "Hema", "CNY"),
            (7.50, "2022-08-25", "Walmart CN", "CNY"),
            (7.90, "2023-03-10", "Hema", "CNY"),
            (8.50, "2024-06-15", "Walmart CN", "CNY"),
            (8.90, "2025-01-20", "Hema", "CNY"),
        ],
    },

    # === ZUID-KOREA (KRW) ===
    {
        "product": Product(name="쌀 (rijst, 10kg)", category="voeding", origin_country="KR"),
        "prices": [
            (22000.0, "2020-01-15", "E-Mart", "KRW"),
            (23500.0, "2021-04-10", "E-Mart", "KRW"),
            (26000.0, "2022-07-20", "E-Mart", "KRW"),
            (28000.0, "2023-10-01", "E-Mart", "KRW"),
            (30000.0, "2024-06-15", "E-Mart", "KRW"),
            (32000.0, "2025-01-10", "E-Mart", "KRW"),
        ],
    },

    # === THAILAND (THB) ===
    {
        "product": Product(name="ข้าว (rijst, 5kg)", category="voeding", origin_country="TH"),
        "prices": [
            (129.0, "2020-02-01", "Tesco Lotus", "THB"),
            (139.0, "2021-05-15", "7-Eleven TH", "THB"),
            (159.0, "2022-08-20", "Tesco Lotus", "THB"),
            (179.0, "2023-03-10", "7-Eleven TH", "THB"),
            (189.0, "2024-06-05", "Tesco Lotus", "THB"),
            (199.0, "2025-01-20", "7-Eleven TH", "THB"),
        ],
    },
    {
        "product": Product(name="Pad Thai (portie)", category="horeca", origin_country="TH"),
        "prices": [
            (50.0, "2020-01-20", "7-Eleven TH", "THB"),
            (55.0, "2021-05-15", "7-Eleven TH", "THB"),
            (60.0, "2022-08-10", "7-Eleven TH", "THB"),
            (70.0, "2023-03-05", "7-Eleven TH", "THB"),
            (75.0, "2024-07-12", "7-Eleven TH", "THB"),
            (80.0, "2025-01-30", "7-Eleven TH", "THB"),
        ],
    },

    # === INDONESIE (IDR) ===
    {
        "product": Product(name="Beras (rijst, 5kg)", category="voeding", origin_country="ID"),
        "prices": [
            (55000.0, "2020-01-15", "Indomaret", "IDR"),
            (58000.0, "2021-04-10", "Alfamart", "IDR"),
            (65000.0, "2022-07-20", "Indomaret", "IDR"),
            (72000.0, "2023-10-01", "Alfamart", "IDR"),
            (78000.0, "2024-06-15", "Indomaret", "IDR"),
            (85000.0, "2025-01-10", "Alfamart", "IDR"),
        ],
    },
    {
        "product": Product(name="Indomie (5-pack)", category="voeding", brand="Indomie", origin_country="ID"),
        "prices": [
            (10500.0, "2020-02-01", "Indomaret", "IDR"),
            (11500.0, "2021-05-15", "Alfamart", "IDR"),
            (12500.0, "2022-08-20", "Indomaret", "IDR"),
            (13500.0, "2023-03-10", "Alfamart", "IDR"),
            (14500.0, "2024-06-05", "Indomaret", "IDR"),
            (15500.0, "2025-01-20", "Alfamart", "IDR"),
        ],
    },

    # === FILIPIJNEN (PHP) ===
    {
        "product": Product(name="Bigas (rijst, 5kg)", category="voeding", origin_country="PH"),
        "prices": [
            (225.0, "2020-01-20", "SM Supermarket", "PHP"),
            (240.0, "2021-05-15", "SM Supermarket", "PHP"),
            (265.0, "2022-08-10", "SM Supermarket", "PHP"),
            (290.0, "2023-03-05", "SM Supermarket", "PHP"),
            (315.0, "2024-07-12", "SM Supermarket", "PHP"),
            (335.0, "2025-01-30", "SM Supermarket", "PHP"),
        ],
    },

    # === VIETNAM (VND) ===
    {
        "product": Product(name="Gạo (rijst, 5kg)", category="voeding", origin_country="VN"),
        "prices": [
            (75000.0, "2020-01-15", "VinMart", "VND"),
            (80000.0, "2021-04-10", "VinMart", "VND"),
            (90000.0, "2022-07-20", "VinMart", "VND"),
            (100000.0, "2023-10-01", "VinMart", "VND"),
            (110000.0, "2024-06-15", "VinMart", "VND"),
            (120000.0, "2025-01-10", "VinMart", "VND"),
        ],
    },
    {
        "product": Product(name="Phở (portie)", category="horeca", origin_country="VN"),
        "prices": [
            (35000.0, "2020-02-01", "VinMart", "VND"),
            (38000.0, "2021-05-15", "VinMart", "VND"),
            (42000.0, "2022-08-20", "VinMart", "VND"),
            (48000.0, "2023-03-10", "VinMart", "VND"),
            (52000.0, "2024-06-05", "VinMart", "VND"),
            (58000.0, "2025-01-20", "VinMart", "VND"),
        ],
    },

    # === SINGAPORE (SGD) ===
    {
        "product": Product(name="Rice (5kg)", category="voeding", origin_country="SG"),
        "prices": [
            (8.50, "2020-01-10", "FairPrice", "SGD"),
            (8.90, "2021-04-22", "FairPrice", "SGD"),
            (9.50, "2022-08-30", "FairPrice", "SGD"),
            (10.50, "2023-05-15", "FairPrice", "SGD"),
            (11.50, "2024-10-01", "FairPrice", "SGD"),
            (12.50, "2025-02-20", "FairPrice", "SGD"),
        ],
    },

    # === MALEISIE (MYR) ===
    {
        "product": Product(name="Beras (rijst, 5kg)", category="voeding", origin_country="MY"),
        "prices": [
            (12.90, "2020-02-15", "Mydin", "MYR"),
            (13.50, "2021-05-20", "Mydin", "MYR"),
            (14.90, "2022-08-25", "Mydin", "MYR"),
            (16.50, "2023-03-10", "Mydin", "MYR"),
            (17.90, "2024-06-15", "Mydin", "MYR"),
            (19.50, "2025-01-20", "Mydin", "MYR"),
        ],
    },

    # === PAKISTAN (PKR) ===
    {
        "product": Product(name="Atta (meel, 10kg)", category="voeding", origin_country="PK"),
        "prices": [
            (450.0, "2020-01-15", "Imtiaz", "PKR"),
            (550.0, "2021-04-10", "Imtiaz", "PKR"),
            (750.0, "2022-07-20", "Imtiaz", "PKR"),
            (1200.0, "2023-10-01", "Imtiaz", "PKR"),
            (1500.0, "2024-06-15", "Imtiaz", "PKR"),
            (1700.0, "2025-01-10", "Imtiaz", "PKR"),
        ],
    },

    # === BANGLADESH (BDT) ===
    {
        "product": Product(name="Chal (rijst, 5kg)", category="voeding", origin_country="BD"),
        "prices": [
            (250.0, "2020-02-01", "Shwapno", "BDT"),
            (275.0, "2021-05-15", "Shwapno", "BDT"),
            (320.0, "2022-08-20", "Shwapno", "BDT"),
            (380.0, "2023-03-10", "Shwapno", "BDT"),
            (420.0, "2024-06-05", "Shwapno", "BDT"),
            (460.0, "2025-01-20", "Shwapno", "BDT"),
        ],
    },

    # ============================================================
    #  AFRIKA
    # ============================================================

    # === ZUID-AFRIKA (ZAR) ===
    {
        "product": Product(name="Big Mac (ZA)", category="horeca", brand="McDonald's", origin_country="ZA"),
        "prices": [
            (33.90, "2020-01-15", "McDonald's ZA", "ZAR"),
            (36.90, "2021-04-10", "McDonald's ZA", "ZAR"),
            (42.90, "2022-07-20", "McDonald's ZA", "ZAR"),
            (49.90, "2023-10-01", "McDonald's ZA", "ZAR"),
            (54.90, "2024-06-15", "McDonald's ZA", "ZAR"),
            (59.90, "2025-01-10", "McDonald's ZA", "ZAR"),
        ],
    },
    {
        "product": Product(name="White Bread (brood)", category="brood", origin_country="ZA"),
        "prices": [
            (12.99, "2020-02-01", "Shoprite ZA", "ZAR"),
            (14.49, "2021-05-15", "Pick n Pay", "ZAR"),
            (16.99, "2022-08-20", "Shoprite ZA", "ZAR"),
            (18.99, "2023-03-10", "Pick n Pay", "ZAR"),
            (20.99, "2024-06-05", "Shoprite ZA", "ZAR"),
            (22.99, "2025-01-20", "Pick n Pay", "ZAR"),
        ],
    },
    {
        "product": Product(name="Melk (1L)", category="zuivel", origin_country="ZA"),
        "prices": [
            (13.99, "2020-01-20", "Shoprite ZA", "ZAR"),
            (15.49, "2021-05-15", "Pick n Pay", "ZAR"),
            (17.99, "2022-08-10", "Shoprite ZA", "ZAR"),
            (19.99, "2023-03-05", "Pick n Pay", "ZAR"),
            (21.99, "2024-07-12", "Shoprite ZA", "ZAR"),
            (23.99, "2025-01-30", "Pick n Pay", "ZAR"),
        ],
    },
    {
        "product": Product(name="KFC Streetwise 2", category="horeca", brand="KFC", origin_country="ZA"),
        "prices": [
            (29.90, "2020-02-10", "KFC ZA", "ZAR"),
            (32.90, "2021-05-20", "KFC ZA", "ZAR"),
            (36.90, "2022-08-15", "KFC ZA", "ZAR"),
            (41.90, "2023-11-01", "KFC ZA", "ZAR"),
            (45.90, "2024-07-20", "KFC ZA", "ZAR"),
            (49.90, "2025-02-15", "KFC ZA", "ZAR"),
        ],
    },

    # === NIGERIA (NGN) - Hoge inflatie ===
    {
        "product": Product(name="Rice (50kg bag)", category="voeding", origin_country="NG"),
        "prices": [
            (18000.0, "2020-01-15", "Shoprite NG", "NGN"),
            (22000.0, "2021-04-10", "Shoprite NG", "NGN"),
            (32000.0, "2022-07-20", "Shoprite NG", "NGN"),
            (45000.0, "2023-10-01", "Shoprite NG", "NGN"),
            (65000.0, "2024-06-15", "Shoprite NG", "NGN"),
            (82000.0, "2025-01-10", "Shoprite NG", "NGN"),
        ],
    },
    {
        "product": Product(name="Bread (brood)", category="brood", origin_country="NG"),
        "prices": [
            (350.0, "2020-02-01", "Shoprite NG", "NGN"),
            (450.0, "2021-05-15", "Shoprite NG", "NGN"),
            (600.0, "2022-08-20", "Shoprite NG", "NGN"),
            (800.0, "2023-03-10", "Shoprite NG", "NGN"),
            (1100.0, "2024-06-05", "Shoprite NG", "NGN"),
            (1500.0, "2025-01-20", "Shoprite NG", "NGN"),
        ],
    },

    # === KENIA (KES) ===
    {
        "product": Product(name="Unga (maismeel, 2kg)", category="voeding", origin_country="KE"),
        "prices": [
            (110.0, "2020-01-20", "Naivas", "KES"),
            (120.0, "2021-05-15", "Naivas", "KES"),
            (145.0, "2022-08-10", "Naivas", "KES"),
            (180.0, "2023-03-05", "Naivas", "KES"),
            (200.0, "2024-07-12", "Naivas", "KES"),
            (220.0, "2025-01-30", "Naivas", "KES"),
        ],
    },
    {
        "product": Product(name="Maziwa (melk, 500ml)", category="zuivel", origin_country="KE"),
        "prices": [
            (50.0, "2020-01-15", "Naivas", "KES"),
            (55.0, "2021-04-10", "Naivas", "KES"),
            (60.0, "2022-07-20", "Naivas", "KES"),
            (70.0, "2023-10-01", "Naivas", "KES"),
            (75.0, "2024-06-15", "Naivas", "KES"),
            (80.0, "2025-01-10", "Naivas", "KES"),
        ],
    },

    # === GHANA (GHS) ===
    {
        "product": Product(name="Rice (5kg)", category="voeding", origin_country="GH"),
        "prices": [
            (25.0, "2020-02-01", "Shoprite GH", "GHS"),
            (30.0, "2021-05-15", "Shoprite GH", "GHS"),
            (42.0, "2022-08-20", "Shoprite GH", "GHS"),
            (65.0, "2023-03-10", "Shoprite GH", "GHS"),
            (85.0, "2024-06-05", "Shoprite GH", "GHS"),
            (105.0, "2025-01-20", "Shoprite GH", "GHS"),
        ],
    },

    # === MAROKKO (MAD) ===
    {
        "product": Product(name="Khobz (brood)", category="brood", origin_country="MA"),
        "prices": [
            (1.20, "2020-01-20", "Marjane", "MAD"),
            (1.20, "2021-05-15", "Marjane", "MAD"),
            (1.50, "2022-08-10", "Marjane", "MAD"),
            (1.80, "2023-03-05", "Marjane", "MAD"),
            (2.00, "2024-07-12", "Marjane", "MAD"),
            (2.20, "2025-01-30", "Marjane", "MAD"),
        ],
    },
    {
        "product": Product(name="Huile d'olive (1L)", category="voeding", origin_country="MA"),
        "prices": [
            (35.0, "2020-01-15", "Marjane", "MAD"),
            (38.0, "2021-04-10", "Marjane", "MAD"),
            (45.0, "2022-07-20", "Marjane", "MAD"),
            (55.0, "2023-10-01", "Marjane", "MAD"),
            (65.0, "2024-06-15", "Marjane", "MAD"),
            (72.0, "2025-01-10", "Marjane", "MAD"),
        ],
    },

    # === ETHIOPIE (ETB) ===
    {
        "product": Product(name="Teff (1kg)", category="voeding", origin_country="ET"),
        "prices": [
            (35.0, "2020-02-01", "Shoa Supermarket", "ETB"),
            (42.0, "2021-05-15", "Shoa Supermarket", "ETB"),
            (55.0, "2022-08-20", "Shoa Supermarket", "ETB"),
            (75.0, "2023-03-10", "Shoa Supermarket", "ETB"),
            (95.0, "2024-06-05", "Shoa Supermarket", "ETB"),
            (110.0, "2025-01-20", "Shoa Supermarket", "ETB"),
        ],
    },

    # === TANZANIA (TZS) ===
    {
        "product": Product(name="Mchele (rijst, 5kg)", category="voeding", origin_country="TZ"),
        "prices": [
            (8000.0, "2020-01-20", "Shoppers TZ", "TZS"),
            (9000.0, "2021-05-15", "Shoppers TZ", "TZS"),
            (10500.0, "2022-08-10", "Shoppers TZ", "TZS"),
            (12000.0, "2023-03-05", "Shoppers TZ", "TZS"),
            (13500.0, "2024-07-12", "Shoppers TZ", "TZS"),
            (15000.0, "2025-01-30", "Shoppers TZ", "TZS"),
        ],
    },

    # === SENEGAL (XOF) ===
    {
        "product": Product(name="Riz brisé (rijst, 5kg)", category="voeding", origin_country="SN"),
        "prices": [
            (1800.0, "2020-01-15", "Auchan SN", "XOF"),
            (1950.0, "2021-04-10", "Auchan SN", "XOF"),
            (2200.0, "2022-07-20", "Auchan SN", "XOF"),
            (2500.0, "2023-10-01", "Auchan SN", "XOF"),
            (2750.0, "2024-06-15", "Auchan SN", "XOF"),
            (3000.0, "2025-01-10", "Auchan SN", "XOF"),
        ],
    },

    # === IVOORKUST (XOF) ===
    {
        "product": Product(name="Attiéké (1kg)", category="voeding", origin_country="CI"),
        "prices": [
            (300.0, "2020-02-01", "Carrefour CI", "XOF"),
            (350.0, "2021-05-15", "Carrefour CI", "XOF"),
            (400.0, "2022-08-20", "Carrefour CI", "XOF"),
            (500.0, "2023-03-10", "Carrefour CI", "XOF"),
            (600.0, "2024-06-05", "Carrefour CI", "XOF"),
            (700.0, "2025-01-20", "Carrefour CI", "XOF"),
        ],
    },

    # ============================================================
    #  OCEANIE
    # ============================================================

    # === AUSTRALIE (AUD) ===
    {
        "product": Product(name="Big Mac (AU)", category="horeca", brand="McDonald's", origin_country="AU"),
        "prices": [
            (6.40, "2020-01-15", "McDonald's AU", "AUD"),
            (6.70, "2021-04-10", "McDonald's AU", "AUD"),
            (7.10, "2022-07-20", "McDonald's AU", "AUD"),
            (7.60, "2023-10-01", "McDonald's AU", "AUD"),
            (8.10, "2024-06-15", "McDonald's AU", "AUD"),
            (8.55, "2025-01-10", "McDonald's AU", "AUD"),
        ],
    },
    {
        "product": Product(name="Milk (2L)", category="zuivel", origin_country="AU"),
        "prices": [
            (2.20, "2020-02-01", "Woolworths AU", "AUD"),
            (2.40, "2021-05-15", "Coles", "AUD"),
            (2.80, "2022-08-20", "Woolworths AU", "AUD"),
            (3.20, "2023-03-10", "Coles", "AUD"),
            (3.50, "2024-06-05", "Woolworths AU", "AUD"),
            (3.70, "2025-01-20", "Coles", "AUD"),
        ],
    },
    {
        "product": Product(name="White Bread (brood)", category="brood", origin_country="AU"),
        "prices": [
            (2.50, "2020-01-20", "Woolworths AU", "AUD"),
            (2.70, "2021-05-15", "Coles", "AUD"),
            (3.00, "2022-08-10", "Woolworths AU", "AUD"),
            (3.40, "2023-03-05", "Coles", "AUD"),
            (3.70, "2024-07-12", "Woolworths AU", "AUD"),
            (3.99, "2025-01-30", "Coles", "AUD"),
        ],
    },

    # === NIEUW-ZEELAND (NZD) ===
    {
        "product": Product(name="Milk (2L)", category="zuivel", origin_country="NZ"),
        "prices": [
            (3.49, "2020-01-10", "Countdown NZ", "NZD"),
            (3.69, "2021-04-22", "Countdown NZ", "NZD"),
            (4.09, "2022-08-30", "Countdown NZ", "NZD"),
            (4.59, "2023-05-15", "Countdown NZ", "NZD"),
            (4.99, "2024-10-01", "Countdown NZ", "NZD"),
            (5.29, "2025-02-20", "Countdown NZ", "NZD"),
        ],
    },
    {
        "product": Product(name="White Bread (brood)", category="brood", origin_country="NZ"),
        "prices": [
            (2.99, "2020-02-15", "Countdown NZ", "NZD"),
            (3.19, "2021-05-20", "Countdown NZ", "NZD"),
            (3.59, "2022-08-25", "Countdown NZ", "NZD"),
            (3.99, "2023-03-10", "Countdown NZ", "NZD"),
            (4.29, "2024-06-15", "Countdown NZ", "NZD"),
            (4.59, "2025-01-20", "Countdown NZ", "NZD"),
        ],
    },
]


# ============================================================
# DATA INVOEGEN
# ============================================================

for item in products_data:
    product = item["product"]
    db.add(product)
    db.commit()
    db.refresh(product)

    for price_val, date_str, store_name, currency in item["prices"]:
        entry = PriceEntry(
            product_id=product.id,
            store_id=store_map.get(store_name),
            price=price_val,
            currency=currency,
            recorded_at=datetime.strptime(date_str, "%Y-%m-%d"),
            source="manual",
        )
        db.add(entry)

db.commit()
db.close()

# Statistieken (gebruik constructor args i.p.v. ORM attributen na close)
num_prices = sum(len(p["prices"]) for p in products_data)
countries = set()
for sd in stores_data:
    countries.add(sd["cc"])

print("=" * 50)
print("Wereldwijde seed data succesvol geladen!")
print("=" * 50)
print(f"  Winkels:              {len(stores_data)}")
print(f"  Producten:            {len(products_data)}")
print(f"  Prijsregistraties:    {num_prices}")
print(f"  Landen:               {len(countries)} ({', '.join(sorted(countries))})")
print("=" * 50)
