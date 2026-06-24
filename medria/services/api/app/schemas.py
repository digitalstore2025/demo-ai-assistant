from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: str = "patient"
    language: str = "ar"


class UserLogin(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    email: Optional[str] = None
    phone: Optional[str] = None
    role: str
    language: str
    created_at: datetime

    class Config:
        from_attributes = True


class DoctorProfileCreate(BaseModel):
    user_id: str
    specialty: str = "internal_medicine"
    license_status: str = "pending"
    verified: str = "false"


class DoctorProfileResponse(BaseModel):
    id: str
    user_id: str
    specialty: str
    license_status: str
    verified: str

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


class ChatSessionCreate(BaseModel):
    appointment_id: Optional[str] = None


class ChatSessionResponse(BaseModel):
    id: str
    appointment_id: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class MessageCreate(BaseModel):
    session_id: str
    sender_role: str
    content: str


class MessageResponse(BaseModel):
    id: str
    session_id: str
    sender_role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class AiSummaryRequest(BaseModel):
    summary: str
