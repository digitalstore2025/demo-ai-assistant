from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Appointment, User
from .schemas import AppointmentCreate, AppointmentResponse, AiSummaryRequest, UserCreate, UserResponse
from .ai_safety import evaluate_safety

router = APIRouter()

@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "medria-api"}

@router.get("/")
def root() -> dict[str, str]:
    return {"message": "Medria AI API is up"}

@router.post("/users", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    if payload.email:
        existing = db.query(User).filter(User.email == str(payload.email)).first()
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")
    user = User(email=str(payload.email) if payload.email else None, phone=payload.phone, role=payload.role, language=payload.language)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/appointments", response_model=AppointmentResponse)
def create_appointment(payload: AppointmentCreate, db: Session = Depends(get_db)):
    appointment = Appointment(patient_id=payload.patient_id, doctor_id=payload.doctor_id, start_time=payload.start_time, end_time=payload.end_time)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

@router.post("/ai/summarize")
def ai_summarize(payload: AiSummaryRequest):
    safety = evaluate_safety(payload.summary)
    return {"summary": payload.summary, "safety_flags": safety["flags"], "needs_human_review": safety["needs_human_review"]}
