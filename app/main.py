import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.database import engine, Base
from app.api import leads, customers, jobs, estimates, invoices, employees, time, photos, documents

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kingdom Plumbing API",
    description="Prototype backend for lead-to-invoice workflow.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads.router)
app.include_router(customers.router)
app.include_router(jobs.router)
app.include_router(estimates.router)
app.include_router(invoices.router)
app.include_router(employees.router)
app.include_router(time.router)
app.include_router(photos.router)
app.include_router(documents.router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "kingdom-plumbing-api"}

app.mount("/", StaticFiles(directory="dashboard", html=True), name="static")
