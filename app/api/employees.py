from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=List[schemas.EmployeeOut])
def list_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip=skip, limit=limit)


@router.get("/{employee_id}", response_model=schemas.EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("/", response_model=schemas.EmployeeOut)
def create_employee(payload: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, payload.model_dump())


@router.post("/{employee_id}/login")
def employee_login(employee_id: int, pin: str, db: Session = Depends(get_db)):
    employee = crud.get_employee_by_pin(db, employee_id, pin)
    if not employee:
        raise HTTPException(status_code=401, detail="Invalid PIN")
    return {"success": True, "employee_id": employee.id, "name": employee.name, "role": employee.role}
