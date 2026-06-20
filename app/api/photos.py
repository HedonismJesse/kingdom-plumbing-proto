from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/photos", tags=["photos"])


@router.get("/", response_model=List[schemas.PhotoOut])
def list_photos(
    skip: int = 0,
    limit: int = 100,
    job_id: Optional[int] = None,
    employee_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return crud.get_photos(db, skip=skip, limit=limit, job_id=job_id, employee_id=employee_id)


@router.get("/{photo_id}", response_model=schemas.PhotoOut)
def get_photo(photo_id: int, db: Session = Depends(get_db)):
    photo = crud.get_photo(db, photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return photo


@router.post("/", response_model=schemas.PhotoOut)
def create_photo(payload: schemas.PhotoCreate, db: Session = Depends(get_db)):
    return crud.create_photo(db, payload.model_dump())
