from typing import List
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas, models

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=List[schemas.JobOut])
def list_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip=skip, limit=limit)


@router.get("/{job_id}", response_model=schemas.JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.post("/", response_model=schemas.JobOut)
def create_job(payload: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, payload.model_dump())


@router.patch("/{job_id}/status", response_model=schemas.JobOut)
def update_job_status(job_id: int, status: str, db: Session = Depends(get_db)):
    job = crud.update_job_status(db, job_id, status)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.put("/{job_id}", response_model=schemas.JobOut)
def update_job(job_id: int, payload: schemas.JobCreate, db: Session = Depends(get_db)):
    from sqlalchemy import update
    db.execute(update(models.Job).where(models.Job.id == job_id).values(**payload.model_dump()))
    db.commit()
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.post("/{job_id}/invoice", response_model=schemas.InvoiceOut)
def invoice_from_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    total = job.total_amount or job.flat_rate or 450
    invoice = crud.create_invoice(db, {
        "invoice_number": "INV-" + str(job_id) + "-" + datetime.utcnow().strftime("%Y%m%d%H%M%S"),
        "customer_id": job.customer_id,
        "job_id": job.id,
        "total": total,
        "status": "sent",
        "line_items": job.title
    })
    return invoice
