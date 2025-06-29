from pydantic import BaseModel
from datetime import datetime

class ViolationOut(BaseModel):
    label: str                   # e.g., NoHelmet, NoVest
    confidence: float            # e.g., 0.87
    face_path: str               # path to cropped face image
    timestamp: datetime          # time of detection
    person_id: str               # unique ID per person
    image_id: str                # ID of the image submitted

    class Config:
        orm_mode = True          # enables compatibility with SQLAlchemy models
