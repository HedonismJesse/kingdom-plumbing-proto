# Kingdom Plumbing Prototype

FastAPI backend prototype for the Kingdom Plumbing unified business system.

## Quick Start

### 1. Environment

```bash
cp .env.example .env
# Edit .env with your database URL if needed
```

### 2. Database

This prototype uses PostgreSQL. If you have Docker:

```bash
docker run -d --name kingdom-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=kingdom_plumbing \
  -p 5432:5432 postgres:16
```

Or use a local PostgreSQL instance and update `DATABASE_URL` in `.env`.

### 3. Install & Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Seed fake data
python seed.py

# Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. API Documentation

Once running, open:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### 5. Docker (optional)

```bash
docker build -t kingdom-plumbing-api .
docker run -d -p 8000:8000 --env-file .env kingdom-plumbing-api
```

## API Overview

| Resource | Endpoints |
|----------|-----------|
| **Leads** | `GET /leads`, `POST /leads`, `GET /leads/{id}`, `PATCH /leads/{id}/convert` |
| **Customers** | `GET /customers`, `POST /customers`, `GET /customers/{id}` |
| **Jobs** | `GET /jobs`, `POST /jobs`, `GET /jobs/{id}`, `PATCH /jobs/{id}/status` |
| **Estimates** | `GET /estimates`, `POST /estimates`, `GET /estimates/{id}` |
| **Invoices** | `GET /invoices`, `POST /invoices`, `GET /invoices/{id}`, `POST /invoices/{id}/pay` |
| **Employees** | `GET /employees`, `POST /employees`, `GET /employees/{id}` |
| **Time Entries** | `GET /time-entries`, `POST /time-entries`, `POST /time-entries/{id}/clock-out` |

## Data Model

```
Lead → Customer → Job → Invoice
         ↓         ↓
      Estimate  TimeEntry
         ↓         ↓
      Employee ←──┘
```

## Next Steps

1. Add a simple Next.js or React dashboard
2. Connect the WordPress Elementor form to `POST /leads`
3. Add authentication (OAuth2 or simple API keys)
4. Deploy to a VPS for live demo
