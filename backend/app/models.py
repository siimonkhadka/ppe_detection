from sqlalchemy import Column, String, DateTime, Float
from app.database import Base
import datetime

class Violation(Base):
    __tablename__ = "violations"

    id: str = Column(String, primary_key=True, index=True)  # Unique ID
    label: str = Column(String)                             # Detected label (e.g., NoHelmet)
    confidence: float = Column(Float)                       # Confidence score
    face_path: str = Column(String)                         # Path to cropped face image
    timestamp: datetime.datetime = Column(DateTime, default=datetime.datetime.utcnow)  # Time of violation
    person_id: str = Column(String)                         # Unique ID for detected person
    image_id: str = Column(String)                          # Reference to original image
