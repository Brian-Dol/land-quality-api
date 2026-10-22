<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:064e3b,100:10b981&height=170&section=header&text=Land%20Quality%20API&fontColor=ffffff&fontSize=48&fontAlignY=38&desc=JWT-secured%20REST%20API%20for%20land%20records%20and%20soil%20assessments&descAlignY=60&descSize=16" alt="Land Quality API" />

![Python](https://img.shields.io/badge/Python-3.12-3776ab?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.1-092e20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST-a30000?style=flat-square)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169e1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ed?style=flat-square&logo=docker&logoColor=white)

</div>

A backend API for managing **land owners, land parcels and soil quality assessments**. Every endpoint requires a JSON Web Token, so records are only readable and writable by authenticated clients.

## ✨ Features

- 🔐 **JWT authentication** with access and refresh tokens (`djangorestframework-simplejwt`)
- 🧑‍🌾 **Owners**, 🌍 **Lands** and 🧪 **Quality assessments** exposed as full CRUD resources
- 📐 Assessments record **pH level, moisture content, nutrient levels and a quality score** per parcel
- 🔗 Relational model: an owner has many lands, and a land has many assessments
- 🐘 PostgreSQL storage with environment-based configuration (no secrets in the code)
- 🐳 Docker Compose setup for the API and its database

## 🏗️ Architecture

```mermaid
flowchart LR
    C[Client] -->|POST credentials| T["/api/auth/token/"]
    T -->|access + refresh JWT| C
    C -->|Bearer token| R["DRF router<br/>/api/owners, /api/lands, /api/assessments"]
    R --> P{IsAuthenticated}
    P -->|valid| V[ModelViewSets + Serializers]
    V --> DB[(PostgreSQL)]
    P -->|invalid| X[401 Unauthorized]
```

### Data model

```mermaid
erDiagram
    OWNER ||--o{ LAND : owns
    LAND ||--o{ LANDQUALITYASSESSMENT : "is assessed by"
    OWNER {
        string name
        string email UK
        string phone
    }
    LAND {
        string location
        decimal size_in_acres
        string soil_type
    }
    LANDQUALITYASSESSMENT {
        date date_assessed
        decimal ph_level
        decimal moisture_content
        string nutrient_levels
        int quality_score
    }
```

## 🔌 API reference

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/auth/token/` | Obtain access and refresh tokens |
| `POST` | `/api/auth/token/refresh/` | Refresh an access token |
| `GET, POST` | `/api/owners/` | List or create owners |
| `GET, PUT, PATCH, DELETE` | `/api/owners/{id}/` | Retrieve, update or delete an owner |
| `GET, POST` | `/api/lands/` | List or create land parcels |
| `GET, PUT, PATCH, DELETE` | `/api/lands/{id}/` | Retrieve, update or delete a parcel |
| `GET, POST` | `/api/assessments/` | List or create quality assessments |
| `GET, PUT, PATCH, DELETE` | `/api/assessments/{id}/` | Retrieve, update or delete an assessment |

All resource endpoints need the header `Authorization: Bearer <access token>`.

## 🚀 Getting started

### With Docker

```bash
git clone https://github.com/Brian-Dol/land-quality-api.git
cd land-quality-api
cp .env.example .env        # then edit the secrets
docker compose up --build
```

### Locally

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # point DB_HOST at your PostgreSQL instance
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API is served at `http://localhost:8000/api/`.

### Try it

```bash
# 1. Get a token
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "your-password"}'

# 2. Create a land parcel with the returned access token
curl -X POST http://localhost:8000/api/lands/ \
  -H "Authorization: Bearer <access>" -H "Content-Type: application/json" \
  -d '{"owner": 1, "location": "Nakuru", "size_in_acres": "12.50", "soil_type": "loam"}'
```

## 🧰 Tech stack

| Layer | Technology |
|---|---|
| Language | Python |
| Framework | Django, Django REST Framework |
| Auth | SimpleJWT |
| Database | PostgreSQL |
| Config | django-environ |
| Packaging | Docker, Docker Compose |

## 🗺️ Roadmap

This is a focused learning and portfolio project. Known gaps and next steps:

- [ ] Automated tests for the serializers and permissions
- [ ] Per-owner permissions, so users only see their own parcels
- [ ] Pagination, filtering and OpenAPI documentation
- [ ] Coordinate-based analysis (PostGIS and external geospatial data sources)
- [ ] CI pipeline with GitHub Actions

## 👤 Author

**Brian Dol**, Senior Full Stack Engineer · [Portfolio](https://portfolio.dol-brian23.workers.dev/) · [LinkedIn](https://linkedin.com/in/brian-dol-31a06115a/)
