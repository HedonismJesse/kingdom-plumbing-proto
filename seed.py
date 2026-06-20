"""Seed fake data for the Kingdom Plumbing prototype."""

import os
import random
from datetime import datetime, timedelta

from app.database import SessionLocal, engine, Base
from app import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

FAKE_CUSTOMERS = [
    {"name": "John Smith", "phone": "503-555-0101", "email": "jsmith@example.com", "address": "124 Oak St, Portland, OR 97201", "city": "Portland"},
    {"name": "Sarah Jones", "phone": "503-555-0102", "email": "sjones@example.com", "address": "456 Maple Ave, Portland, OR 97202", "city": "Portland"},
    {"name": "Mike Baker", "phone": "503-555-0103", "email": "mbaker@example.com", "address": "789 Pine Ln, Beaverton, OR 97005", "city": "Beaverton"},
    {"name": "Lisa Lee", "phone": "503-555-0104", "email": "llee@example.com", "address": "321 Cedar Rd, Portland, OR 97203", "city": "Portland"},
    {"name": "Raj Patel", "phone": "503-555-0105", "email": "rpatel@example.com", "address": "654 Birch Blvd, Hillsboro, OR 97123", "city": "Hillsboro"},
    {"name": "Emily Chen", "phone": "503-555-0106", "email": "echen@example.com", "address": "987 Willow Way, Portland, OR 97204", "city": "Portland"},
    {"name": "David Garcia", "phone": "503-555-0107", "email": "dgarcia@example.com", "address": "147 Elm St, Beaverton, OR 97006", "city": "Beaverton"},
    {"name": "Karen White", "phone": "503-555-0108", "email": "kwhite@example.com", "address": "258 Spruce Dr, Portland, OR 97205", "city": "Portland"},
]

FAKE_EMPLOYEES = [
    {"name": "Mike Torres", "role": "Field Technician", "phone": "503-555-0201", "email": "mtorres@kingdomplumbing.local", "hourly_rate": 35.0},
    {"name": "Sarah Kim", "role": "Field Technician", "phone": "503-555-0202", "email": "skim@kingdomplumbing.local", "hourly_rate": 38.0},
    {"name": "James Wilson", "role": "Office Manager", "phone": "503-555-0203", "email": "jwilson@kingdomplumbing.local", "hourly_rate": 28.0},
    {"name": "Angela Brown", "role": "Dispatcher", "phone": "503-555-0204", "email": "abrown@kingdomplumbing.local", "hourly_rate": 26.0},
]

SERVICE_TYPES = [
    "Emergency Repair",
    "Water Heater",
    "Drain Cleaning",
    "Pipe Replacement",
    "Inspection",
    "Remodel",
]

JOB_TITLES = [
    "Kitchen sink leak repair",
    "Water heater replacement",
    "Main drain cleaning",
    "Bathroom pipe replacement",
    "Annual plumbing inspection",
    "Shower valve installation",
    "Toilet replacement",
    "Garbage disposal repair",
]


def create_customers():
    customers = []
    for data in FAKE_CUSTOMERS:
        c = models.Customer(**data)
        db.add(c)
        customers.append(c)
    db.commit()
    for c in customers:
        db.refresh(c)
    print(f"Created {len(customers)} customers")
    return customers


def create_employees():
    employees = []
    for data in FAKE_EMPLOYEES:
        e = models.Employee(**data)
        db.add(e)
        employees.append(e)
    db.commit()
    for e in employees:
        db.refresh(e)
    print(f"Created {len(employees)} employees")
    return employees


def create_leads():
    leads = []
    for i in range(12):
        service = random.choice(SERVICE_TYPES)
        l = models.Lead(
            source="website",
            name=f"Lead Person {i+1}",
            phone=f"503-555-{3000+i:04d}",
            email=f"lead{i+1}@example.com",
            address="Portland, OR",
            service_type=service,
            preferred_time=random.choice(["Morning", "Afternoon", "Evening"]),
            description=f"Interested in {service.lower()}",
            status=random.choice(["new", "contacted", "converted"]),
        )
        db.add(l)
        leads.append(l)
    db.commit()
    print(f"Created {len(leads)} leads")
    return leads


def create_jobs(customers, employees):
    jobs = []
    techs = [e for e in employees if e.role == "Field Technician"]
    for i, customer in enumerate(customers[:6]):
        tech = random.choice(techs) if techs else None
        scheduled = datetime.utcnow() + timedelta(days=random.randint(-5, 10))
        j = models.Job(
            job_number=f"J-{2024}{i+1:04d}",
            title=random.choice(JOB_TITLES),
            description="Standard residential service call.",
            status=random.choice(["scheduled", "in_progress", "complete"]),
            customer_id=customer.id,
            technician_id=tech.id if tech else None,
            address=customer.address,
            scheduled_date=scheduled,
            estimated_hours=random.choice([1.0, 1.5, 2.0, 3.0, 4.0]),
            flat_rate=random.choice([150.0, 250.0, 350.0, 450.0, 550.0]),
            materials_cost=random.choice([25.0, 50.0, 75.0, 100.0]),
            total_amount=random.choice([175.0, 300.0, 425.0, 550.0]),
            notes="Customer prefers morning appointments.",
        )
        db.add(j)
        jobs.append(j)
    db.commit()
    for j in jobs:
        db.refresh(j)
    print(f"Created {len(jobs)} jobs")
    return jobs


def create_estimates(customers):
    estimates = []
    for i, customer in enumerate(customers[6:]):
        subtotal = random.choice([200.0, 350.0, 500.0, 750.0])
        tax = round(subtotal * 0.08, 2)
        e = models.Estimate(
            estimate_number=f"E-{2024}{i+1:04d}",
            title=random.choice(JOB_TITLES),
            description="Estimate for upcoming work.",
            status=random.choice(["draft", "sent", "approved"]),
            customer_id=customer.id,
            line_items="Labor, Materials, Tax",
            subtotal=subtotal,
            tax=tax,
            total=round(subtotal + tax, 2),
            notes="Awaiting customer approval.",
        )
        db.add(e)
        estimates.append(e)
    db.commit()
    print(f"Created {len(estimates)} estimates")
    return estimates


def create_invoices(customers, jobs):
    invoices = []
    for i, job in enumerate(jobs):
        if job.status != "complete":
            continue
        subtotal = job.total_amount or random.choice([200.0, 350.0, 500.0])
        tax = round(subtotal * 0.08, 2)
        total = round(subtotal + tax, 2)
        inv = models.Invoice(
            invoice_number=f"INV-{2024}{i+1:04d}",
            status=random.choice(["sent", "paid"]),
            customer_id=job.customer_id,
            job_id=job.id,
            line_items="Labor, Materials, Tax",
            subtotal=subtotal,
            tax=tax,
            total=total,
            amount_paid=total if random.random() > 0.3 else 0.0,
            due_date=datetime.utcnow() + timedelta(days=14),
            notes="Net 14 terms.",
        )
        if inv.amount_paid >= total:
            inv.status = "paid"
            inv.paid_date = datetime.utcnow() - timedelta(days=random.randint(1, 7))
        db.add(inv)
        invoices.append(inv)
    db.commit()
    print(f"Created {len(invoices)} invoices")
    return invoices


def create_time_entries(employees, jobs):
    entries = []
    techs = [e for e in employees if e.role == "Field Technician"]
    for i in range(8):
        tech = random.choice(techs) if techs else random.choice(employees)
        job = random.choice(jobs) if jobs else None
        start = datetime.utcnow() - timedelta(days=random.randint(0, 5), hours=random.randint(6, 14))
        end = start + timedelta(hours=random.choice([1.0, 1.5, 2.0, 3.0]))
        e = models.TimeEntry(
            employee_id=tech.id,
            job_id=job.id if job else None,
            clock_in=start,
            clock_out=end,
            hours_worked=round((end - start).total_seconds() / 3600, 2),
            notes="Routine service call.",
        )
        db.add(e)
        entries.append(e)
    db.commit()
    print(f"Created {len(entries)} time entries")
    return entries


def main():
    print("Seeding Kingdom Plumbing prototype data...")
    customers = create_customers()
    employees = create_employees()
    create_leads()
    jobs = create_jobs(customers, employees)
    create_estimates(customers)
    create_invoices(customers, jobs)
    create_time_entries(employees, jobs)
    print("Done.")
    db.close()


if __name__ == "__main__":
    main()
