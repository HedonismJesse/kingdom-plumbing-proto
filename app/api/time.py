from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/time-entries", tags=["time-entries"])


@router.get("/", response_model=List[schemas.TimeEntryOut])
def list_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_time_entries(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.TimeEntryOut)
def clock_in(payload: schemas.TimeEntryCreate, db: Session = Depends(get_db)):
    return crud.create_time_entry(db, payload.model_dump())


@router.post("/{entry_id}/clock-out", response_model=schemas.TimeEntryOut)
def clock_out(entry_id: int, db: Session = Depends(get_db)):
    entry = crud.clock_out(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Time entry not found")
    return entry
