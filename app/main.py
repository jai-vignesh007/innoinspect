from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="InnoInspect Backend")

# Create all tables
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok", "message": "Postgres is connected!"}
