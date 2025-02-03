from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
import uvicorn

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical Data Warehouse API")

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/medical_data/", response_model=list[schemas.MedicalData])
def read_medical_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_medical_data(db, skip=skip, limit=limit)
    return data

@app.post("/medical_data/", response_model=schemas.MedicalData)
def create_medical_data(medical_data: schemas.MedicalDataCreate, db: Session = Depends(get_db)):
    return crud.create_medical_data(db, medical_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
