from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/estimates", tags=["estimates"])


@router.get("/", response_model=List[schemas.EstimateOut])
def list_estimates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_estimates(db, skip=skip, limit=limit)


@router.get("/{estimate_id}", response_model=schemas.EstimateOut)
def get_estimate(estimate_id: int, db: Session = Depends(get_db)):
    estimate = crud.get_estimate(db, estimate_id)
    if not estimate:
        raise HTTPException(status_code=404, detail="Estimate not found")
    return estimate


@router.post("/", response_model=schemas.EstimateOut)
def create_estimate(payload: schemas.EstimateCreate, db: Session = Depends(get_db)):
    return crud.create_estimate(db, payload.model_dump())


@router.post("/{estimate_id}/approve", response_model=schemas.EstimateOut)
def approve_estimate(estimate_id: int, db: Session = Depends(get_db)):
    from datetime import datetime
    estimate = crud.get_estimate(db, estimate_id)
    if not estimate:
        raise HTTPException(status_code=404, detail="Estimate not found")
    if estimate.status != "approved":
        estimate.status = "approved"
        db.commit()
        db.refresh(estimate)
    return estimate
