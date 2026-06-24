from sqlalchemy.orm import Session

from .auth import create_user_record
from .models import Appointment, ChatSession, DoctorProfile, Message, User


def ensure_seed_data(db: Session) -> None:
    if db.query(User).count() > 0:
        return

    patient = create_user_record(
        db=db,
        email="patient@example.com",
        phone="+905551112233",
        role="patient",
        language="ar",
        password="seed123",
    )
    doctor = create_user_record(
        db=db,
        email="doctor@example.com",
        phone="+905552223344",
        role="doctor",
        language="en",
        password="seed123",
    )

    doctor_profile = DoctorProfile(
        user_id=doctor.id,
        specialty="internal_medicine",
        license_status="verified",
        verified="true",
    )
    db.add(doctor_profile)

    appointment = Appointment(
        patient_id=patient.id,
        doctor_id=doctor.id,
        start_time="2026-06-24T10:00:00",
        end_time="2026-06-24T10:30:00",
        status="confirmed",
    )
    db.add(appointment)

    chat = ChatSession(appointment_id=appointment.id, status="open")
    db.add(chat)
    db.flush()

    message = Message(session_id=chat.id, sender_role="patient", content="I have mild headache and dizziness for two days.")
    db.add(message)
    db.commit()
