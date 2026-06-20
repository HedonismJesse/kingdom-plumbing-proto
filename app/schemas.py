from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class LeadBase(BaseModel):
    source: str = "website"
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    service_type: Optional[str] = None
    preferred_time: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class LeadOut(LeadBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class CustomerBase(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    notes: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerOut(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class EmployeeBase(BaseModel):
    name: str
    role: str
    phone: Optional[str] = None
    email: Optional[str] = None
    hourly_rate: Optional[float] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int
    is_active: str
    created_at: datetime

    class Config:
        from_attributes = True


class JobBase(BaseModel):
    job_number: str
    title: str
    description: Optional[str] = None
    status: str = "scheduled"
    customer_id: int
    technician_id: Optional[int] = None
    address: Optional[str] = None
    scheduled_date: Optional[datetime] = None
    estimated_hours: Optional[float] = None
    flat_rate: Optional[float] = None
    materials_cost: Optional[float] = None
    total_amount: Optional[float] = None
    notes: Optional[str] = None


class JobCreate(JobBase):
    pass


class JobOut(JobBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class EstimateBase(BaseModel):
    estimate_number: str
    title: str
    description: Optional[str] = None
    status: str = "draft"
    customer_id: int
    line_items: Optional[str] = None
    subtotal: Optional[float] = None
    tax: Optional[float] = None
    total: Optional[float] = None
    notes: Optional[str] = None


class EstimateCreate(EstimateBase):
    pass


class EstimateOut(EstimateBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class InvoiceBase(BaseModel):
    invoice_number: str
    status: str = "draft"
    customer_id: int
    job_id: Optional[int] = None
    line_items: Optional[str] = None
    subtotal: Optional[float] = None
    tax: Optional[float] = None
    total: Optional[float] = None
    amount_paid: float = 0.0
    due_date: Optional[datetime] = None
    notes: Optional[str] = None


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceOut(InvoiceBase):
    id: int
    paid_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TimeEntryBase(BaseModel):
    employee_id: int
    job_id: Optional[int] = None
    clock_in: datetime
    clock_out: Optional[datetime] = None
    hours_worked: Optional[float] = None
    notes: Optional[str] = None


class TimeEntryCreate(TimeEntryBase):
    pass


class TimeEntryOut(TimeEntryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
