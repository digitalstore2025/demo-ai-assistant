from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .ai_safety import evaluate_safety
from .auth import authenticate_user, create_user_record
from .database import get_db
from .models import Appointment, ChatSession, DoctorProfile, Message, User
from .schemas import (
    AiSummaryRequest,
    AppointmentCreate,
    AppointmentResponse,
    ChatSessionCreate,
    ChatSessionResponse,
    DoctorProfileCreate,
    DoctorProfileResponse,
    MessageCreate,
    MessageResponse,
    UserCreate,
    UserLogin,
    UserResponse,
)

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "medria-api"}


@router.get("/")
def root() -> dict[str, str]:
    return {"message": "Medria AI API is up"}


@router.post("/auth/signup", response_model=UserResponse)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    user = create_user_record(
        db=db,
        email=str(payload.email) if payload.email else None,
        phone=payload.phone,
        role=payload.role,
        language=payload.language,
    )
    return user


@router.post("/auth/login")
def login(payload: UserLogin, db: Session = Depends(get_db)):
    if not payload.email and not payload.phone:
        raise HTTPException(status_code=400, detail="Provide email or phone")
    user = authenticate_user(db=db, email=payload.email, phone=payload.phone)
    return {
        "access_token": f"demo-token-{user.id}",
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "language": user.language,
        },
    }


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/doctors/profile", response_model=DoctorProfileResponse)
def create_doctor_profile(payload: DoctorProfileCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    profile = DoctorProfile(
        user_id=payload.user_id,
        specialty=payload.specialty,
        license_status=payload.license_status,
        verified=payload.verified,
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


@router.post("/appointments", response_model=AppointmentResponse)
def create_appointment(payload: AppointmentCreate, db: Session = Depends(get_db)):
    appointment = Appointment(
        patient_id=payload.patient_id,
        doctor_id=payload.doctor_id,
        start_time=payload.start_time,
        end_time=payload.end_time,
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment


@router.post("/chat/sessions", response_model=ChatSessionResponse)
def create_chat_session(payload: ChatSessionCreate, db: Session = Depends(get_db)):
    session = ChatSession(appointment_id=payload.appointment_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.post("/chat/sessions/{session_id}/messages", response_model=MessageResponse)
def add_message(session_id: str, payload: MessageCreate, db: Session = Depends(get_db)):
    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")

    message = Message(session_id=session_id, sender_role=payload.sender_role, content=payload.content)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


@router.get("/chat/sessions/{session_id}/messages", response_model=list[MessageResponse])
def list_messages(session_id: str, db: Session = Depends(get_db)):
    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    return db.query(Message).filter(Message.session_id == session_id).order_by(Message.created_at).all()


@router.post("/ai/summarize")
def ai_summarize(payload: AiSummaryRequest):
    safety = evaluate_safety(payload.summary)
    return {
        "summary": payload.summary,
        "safety_flags": safety["flags"],
        "needs_human_review": safety["needs_human_review"],
    }
