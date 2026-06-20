from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/", response_model=List[schemas.DocumentOut])
def list_documents(
    skip: int = 0,
    limit: int = 100,
    employee_id: Optional[int] = None,
    type: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return crud.get_documents(db, skip=skip, limit=limit, employee_id=employee_id, type=type)


@router.get("/{document_id}", response_model=schemas.DocumentOut)
def get_document(document_id: int, db: Session = Depends(get_db)):
    doc = crud.get_document(db, document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc


@router.post("/", response_model=schemas.DocumentOut)
def create_document(payload: schemas.DocumentCreate, db: Session = Depends(get_db)):
    return crud.create_document(db, payload.model_dump())
