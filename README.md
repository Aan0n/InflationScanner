# InflationScanner

Scan producten of kassabonnetjes om te zien hoe duur producten werkelijk zijn geworden.

## Wat doet InflationScanner?

InflationScanner is een webapp waarmee je de prijsontwikkeling van alledaagse producten kunt bekijken. Gebruikers dragen bij aan een groeiende database door:

- **Barcode scannen** - Scan een product in de winkel om de prijs toe te voegen
- **Prijzen handmatig invoeren** - Voeg prijzen toe met datum en winkel
- **Prijsgeschiedenis bekijken** - Zie grafieken van hoe prijzen veranderen over tijd
- **Top inflatie** - Bekijk welke producten het meest in prijs zijn gestegen

## Technologie

- **Backend**: Python met FastAPI
- **Database**: SQLite (later uitbreidbaar naar PostgreSQL)
- **Frontend**: HTML/CSS/JavaScript als Progressive Web App
- **Barcode scanner**: QuaggaJS (camera-gebaseerd)
- **Grafieken**: Chart.js

## Snel starten

### 1. Vereisten

- Python 3.11 of nieuwer

### 2. Installatie

```bash
cd backend
pip install -r requirements.txt
```

### 3. Voorbeelddata laden (optioneel)

```bash
cd backend
python seed_data.py
```

### 4. Server starten

```bash
cd backend
uvicorn app.main:app --reload
```

Open daarna http://localhost:8000 in je browser.

## Projectstructuur

```
InflationScanner/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py      # Database configuratie
│   │   ├── main.py           # FastAPI applicatie & API endpoints
│   │   ├── models.py         # Database modellen
│   │   └── schemas.py        # Request/response schemas
│   ├── tests/
│   ├── requirements.txt
│   └── seed_data.py          # Voorbeelddata script
├── frontend/
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/app.js
│   └── templates/
│       └── index.html
├── LICENSE
└── README.md
```

## API Endpoints

| Methode | Pad | Beschrijving |
|---------|-----|-------------|
| GET | `/api/products` | Zoek producten |
| GET | `/api/products/{id}` | Product details |
| GET | `/api/products/barcode/{barcode}` | Zoek op barcode |
| POST | `/api/products` | Nieuw product |
| GET | `/api/stores` | Lijst winkels |
| POST | `/api/stores` | Nieuwe winkel |
| POST | `/api/prices` | Prijs toevoegen |
| GET | `/api/prices/{product_id}/history` | Prijsgeschiedenis |
| GET | `/api/stats/top-inflation` | Grootste prijsstijgingen |

## Toekomstplannen

- [ ] Kassabon scannen met OCR (foto van je bon)
- [ ] Gebruikersaccounts en privacy-instellingen
- [ ] Native iPhone app
- [ ] Prijsalerts (melding als een product goedkoper wordt)
- [ ] Vergelijk prijzen tussen winkels
- [ ] CBS inflatie-data integratie
