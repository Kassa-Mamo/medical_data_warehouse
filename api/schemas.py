from pydantic import BaseModel
from datetime import datetime

class MedicalDataBase(BaseModel):
    channel: str
    text: str
    date: datetime

class MedicalDataCreate(MedicalDataBase):
    pass

class MedicalData(MedicalDataBase):
    id: int

    class Config:
        orm_mode = True
