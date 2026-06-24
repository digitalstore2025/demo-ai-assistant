from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: str = "patient"
    language: str = "ar"


class UserResponse(BaseModel):
    id: str
    email: Optional[str] = None
    phone: Optional[str] = None
    role: str
    language: str
    created_at: datetime

    class Config:
        from_attributes = True


class AppointmentCreate(BaseModel):
    patient_id: str
    doctor_id: str
    start_time: datetime
    end_time: datetime


class AppointmentResponse(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    start_time: datetime
    end_time: datetime
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class AiSummaryRequest(BaseModel):
    summary: str
