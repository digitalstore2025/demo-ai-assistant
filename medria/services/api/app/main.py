from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine
from .routes import router
from .seed import ensure_seed_data

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medria AI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_event() -> None:
    db: Session = SessionLocal()
    try:
        ensure_seed_data(db)
    finally:
        db.close()
