from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/leads", tags=["leads"])


@router.get("/", response_model=List[schemas.LeadOut])
def list_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_leads(db, skip=skip, limit=limit)


@router.get("/{lead_id}", response_model=schemas.LeadOut)
def get_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = crud.get_lead(db, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.post("/", response_model=schemas.LeadOut)
def create_lead(payload: schemas.LeadCreate, db: Session = Depends(get_db)):
    return crud.create_lead(db, payload.model_dump())


@router.patch("/{lead_id}/convert", response_model=schemas.LeadOut)
def convert_lead(lead_id: int, customer_id: int, db: Session = Depends(get_db)):
    lead = crud.update_lead_status(db, lead_id, "converted", customer_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead
