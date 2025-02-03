from sqlalchemy.orm import Session
from . import models, schemas

def get_medical_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MedicalData).offset(skip).limit(limit).all()

def create_medical_data(db: Session, medical_data: schemas.MedicalDataCreate):
    db_medical_data = models.MedicalData(**medical_data.dict())
    db.add(db_medical_data)
    db.commit()
    db.refresh(db_medical_data)
    return db_medical_data
