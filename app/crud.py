from typing import Optional

from sqlalchemy.orm import Session

from app import models


# Leads

def get_lead(db: Session, lead_id: int):
    return db.query(models.Lead).filter(models.Lead.id == lead_id).first()


def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lead).order_by(models.Lead.created_at.desc()).offset(skip).limit(limit).all()


def create_lead(db: Session, lead: dict):
    db_lead = models.Lead(**lead)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


def update_lead_status(db: Session, lead_id: int, status: str, customer_id: Optional[int] = None):
    db_lead = get_lead(db, lead_id)
    if db_lead:
        db_lead.status = status
        if customer_id:
            db_lead.converted_to_customer_id = customer_id
        db.commit()
        db.refresh(db_lead)
    return db_lead


# Customers

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).order_by(models.Customer.name).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: dict):
    db_customer = models.Customer(**customer)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


# Jobs

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).order_by(models.Job.created_at.desc()).offset(skip).limit(limit).all()


def create_job(db: Session, job: dict):
    db_job = models.Job(**job)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def update_job_status(db: Session, job_id: int, status: str):
    db_job = get_job(db, job_id)
    if db_job:
        db_job.status = status
        db.commit()
        db.refresh(db_job)
    return db_job


# Estimates

def get_estimate(db: Session, estimate_id: int):
    return db.query(models.Estimate).filter(models.Estimate.id == estimate_id).first()


def get_estimates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Estimate).order_by(models.Estimate.created_at.desc()).offset(skip).limit(limit).all()


def create_estimate(db: Session, estimate: dict):
    db_estimate = models.Estimate(**estimate)
    db.add(db_estimate)
    db.commit()
    db.refresh(db_estimate)
    return db_estimate


# Invoices

def get_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()


def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).order_by(models.Invoice.created_at.desc()).offset(skip).limit(limit).all()


def create_invoice(db: Session, invoice: dict):
    db_invoice = models.Invoice(**invoice)
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def mark_invoice_paid(db: Session, invoice_id: int):
    from datetime import datetime
    db_invoice = get_invoice(db, invoice_id)
    if db_invoice:
        db_invoice.status = "paid"
        db_invoice.amount_paid = db_invoice.total
        db_invoice.paid_date = datetime.utcnow()
        db.commit()
        db.refresh(db_invoice)
    return db_invoice


# Employees

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).order_by(models.Employee.name).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: dict):
    db_employee = models.Employee(**employee)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


# Time Entries

def get_time_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TimeEntry).order_by(models.TimeEntry.clock_in.desc()).offset(skip).limit(limit).all()


def create_time_entry(db: Session, entry: dict):
    db_entry = models.TimeEntry(**entry)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def clock_out(db: Session, entry_id: int, hours: Optional[float] = None):
    from datetime import datetime
    db_entry = db.query(models.TimeEntry).filter(models.TimeEntry.id == entry_id).first()
    if db_entry:
        db_entry.clock_out = datetime.utcnow()
        if hours is not None:
            db_entry.hours_worked = hours
        elif db_entry.clock_in:
            delta = (db_entry.clock_out - db_entry.clock_in).total_seconds() / 3600
            db_entry.hours_worked = round(delta, 2)
        db.commit()
        db.refresh(db_entry)
    return db_entry
