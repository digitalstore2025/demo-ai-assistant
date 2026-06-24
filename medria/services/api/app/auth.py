import hashlib
import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .database import get_db
from .models import User

JWT_SECRET = os.getenv("JWT_SECRET", "medria-dev-secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password: str) -> str:
    salt = os.getenv("PASSWORD_SALT", "medria-dev-salt").encode("utf-8")
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000).hex()


def verify_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)


def create_user_record(db: Session, email: Optional[str], phone: Optional[str], role: str, language: str, password: Optional[str]) -> User:
    if email:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")
    user = User(
        email=email,
        phone=phone,
        role=role,
        language=language,
        password_hash=hash_password(password) if password else None,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: Optional[str], phone: Optional[str], password: Optional[str]) -> User:
    if not password:
        raise HTTPException(status_code=400, detail="Password is required")
    if email:
        user = db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.password_hash or ""):
            return user
    if phone:
        user = db.query(User).filter(User.phone == phone).first()
        if user and verify_password(password, user.password_hash or ""):
            return user
    raise HTTPException(status_code=404, detail="Invalid credentials")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(status_code=401, detail="Token expired") from exc
    except jwt.PyJWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
