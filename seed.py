"""Seed fake data for the Kingdom Plumbing prototype."""

import os
import random
from datetime import datetime, timedelta

from app.database import SessionLocal, engine, Base
from app import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

FAKE_CUSTOMERS = [
    {"name": "Margaret Henderson", "phone": "503-555-0101", "email": "mhenderson@gmail.com", "address": "124 SE Oak St, Portland, OR 97214", "city": "Portland", "notes": "Repeat customer. Prefers morning appointments. Has two rental properties."},
    {"name": "Robert & Linda Crawford", "phone": "503-555-0102", "email": "crawford.family@yahoo.com", "address": "456 NW Maple Ave, Portland, OR 97209", "city": "Portland", "notes": "Older home (1920s). Frequent pipe issues. Wants full repipe estimate."},
    {"name": "Steve Nakamura", "phone": "503-555-0103", "email": "snakamura@outlook.com", "address": "789 SW Pine Ln, Beaverton, OR 97005", "city": "Beaverton", "notes": "Commercial client. Sushi restaurant on Canyon Rd. Grease trap maintenance."},
    {"name": "Diana Lopez", "phone": "503-555-0104", "email": "dlopez@hotmail.com", "address": "321 NE Cedar Rd, Portland, OR 97211", "city": "Portland", "notes": "New homeowner. Just bought fixer-upper in Alberta Arts District."},
    {"name": "Anand Patel", "phone": "503-555-0105", "email": "apatel@gmail.com", "address": "654 SE Birch Blvd, Hillsboro, OR 97123", "city": "Hillsboro", "notes": "Property manager for 12-unit apartment complex. Needs reliable ongoing service."},
    {"name": "Jennifer O'Brien", "phone": "503-555-0106", "email": "jobrien@gmail.com", "address": "987 NW Willow Way, Portland, OR 97210", "city": "Portland", "notes": "Referral from Margaret Henderson. Kitchen remodel starting next month."},
    {"name": "Marcus Johnson", "phone": "503-555-0107", "email": "mjohnson@outlook.com", "address": "147 SW Elm St, Beaverton, OR 97006", "city": "Beaverton", "notes": "HOA president for condo building. Needs bids for repipe project."},
    {"name": "Karen Whitfield", "phone": "503-555-0108", "email": "kwhitfield@gmail.com", "address": "258 NE Spruce Dr, Portland, OR 97212", "city": "Portland", "notes": "Emergency-only customer. Called at 2 AM last time. Very price-sensitive."},
]

FAKE_EMPLOYEES = [
    {"name": "Mike Torres", "role": "Senior Field Technician", "phone": "503-555-0201", "email": "mtorres@kingdomplumbing.local", "hourly_rate": 38.0},
    {"name": "Sarah Kim", "role": "Field Technician", "phone": "503-555-0202", "email": "skim@kingdomplumbing.local", "hourly_rate": 35.0},
    {"name": "James Wilson", "role": "Office Manager", "phone": "503-555-0203", "email": "jwilson@kingdomplumbing.local", "hourly_rate": 28.0},
    {"name": "Angela Brown", "role": "Dispatcher / Scheduler", "phone": "503-555-0204", "email": "abrown@kingdomplumbing.local", "hourly_rate": 26.0},
]

SERVICE_TYPES = [
    "Emergency Leak Repair",
    "Water Heater Replacement",
    "Drain Cleaning",
    "Whole-House Repipe",
    "Annual Inspection",
    "Bathroom Remodel",
    "Sewer Line Replacement",
    "Garbage Disposal Install",
]

JOB_TITLES = [
    "Kitchen sink leak under cabinet",
    "Water heater replacement (50 gal)",
    "Main drain line hydro-jet cleaning",
    "Bathroom repipe — galvanized to PEX",
    "Annual plumbing inspection & safety check",
    "Shower valve cartridge replacement",
    "Toilet replacement & flange repair",
    "Garbage disposal install (Badger 5)",
    "Sewer line camera inspection",
    "Dishwasher water line hookup",
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


LEAD_NAMES = [
    ("Tom Bradley", "tbradley@gmail.com", "503-555-3101", "NE Portland"),
    ("Rachel Green", "rgreen@outlook.com", "503-555-3102", "Beaverton"),
    ("David Chen", "dchen@gmail.com", "503-555-3103", "Hillsboro"),
    ("Amanda Foster", "afoster@yahoo.com", "503-555-3104", "Lake Oswego"),
    ("Greg Murphy", "gmurphy@gmail.com", "503-555-3105", "Tigard"),
    ("Nina Patel", "npatel@hotmail.com", "503-555-3106", "Portland"),
    ("Chris Barnes", "cbarnes@outlook.com", "503-555-3107", "Gresham"),
    ("Lisa Monroe", "lmonroe@gmail.com", "503-555-3108", "Milwaukie"),
    ("Kevin Hartley", "khartley@yahoo.com", "503-555-3109", "West Linn"),
    ("Sandra Ellis", "sellis@gmail.com", "503-555-3110", "Portland"),
    ("Paul Nguyen", "pnguyen@outlook.com", "503-555-3111", "Beaverton"),
    ("Heather Walsh", "hwalsh@gmail.com", "503-555-3112", "Oregon City"),
]

LEAD_DESCRIPTIONS = [
    "No hot water since yesterday. Need ASAP — family of 5.",
    "Basement flooding when washer drains. Suspect main line blockage.",
    "Old galvanized pipes. Low pressure everywhere. Want estimate for repipe.",
    "Remodeling master bath. Need plumber for rough-in and fixtures.",
    "Water bill doubled last month. Think we have a leak somewhere.",
    "Garbage disposal jammed and leaking under sink. Need replacement.",
    "Toilet runs constantly and wobbles. May need flange repair.",
    "Installing tankless water heater. Need gas line run and venting.",
    "Sewer smell in backyard. Camera inspection requested.",
    "Dishwasher not draining properly. Possible clogged drain line.",
    "Shower barely drips. No pressure in master bath only.",
    "Kitchen faucet leaking from handle base. Moen fixture.",
]

def create_leads():
    leads = []
    sources = ["website", "google", "referral", "facebook", "thumbtack", "yelp"]
    statuses = ["new", "new", "new", "contacted", "contacted", "converted"]  # weighted toward new
    for i in range(12):
        name, email, phone, city = LEAD_NAMES[i]
        l = models.Lead(
            source=random.choice(sources),
            name=name,
            phone=phone,
            email=email,
            address=f"{city}, OR",
            service_type=random.choice(SERVICE_TYPES),
            preferred_time=random.choice(["Morning (8-12)", "Afternoon (12-5)", "Evening (5-8)"]),
            description=LEAD_DESCRIPTIONS[i],
            status=random.choice(statuses),
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
