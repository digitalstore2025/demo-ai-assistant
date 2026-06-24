from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import User


def create_user_record(db: Session, email: str | None, phone: str | None, role: str, language: str) -> User:
    if email:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")
    user = User(email=email, phone=phone, role=role, language=language)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str | None, phone: str | None) -> User:
    if email:
        user = db.query(User).filter(User.email == email).first()
        if user:
            return user
    if phone:
        user = db.query(User).filter(User.phone == phone).first()
        if user:
            return user
    raise HTTPException(status_code=404, detail="User not found")
