from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class MedicalData(Base):
    __tablename__ = "medical_data"
    
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String, index=True)
    text = Column(String)
    date = Column(DateTime)
