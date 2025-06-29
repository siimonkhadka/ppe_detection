from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models
import uuid
import datetime

def create_violation(db: Session, violation: dict):
    db_violation = models.Violation(
        id=str(uuid.uuid4()),
        label=violation['label'],
        confidence=float(violation['confidence']),
        face_path=violation['face_path'],
        timestamp=datetime.datetime.utcnow(),
        person_id=violation['person_id'],
        image_id=violation.get('image_id', None)
    )
    db.add(db_violation)
    db.commit()
    db.refresh(db_violation)
    return db_violation

def get_all_violations(db: Session):
    return db.query(models.Violation).all()

def get_violations_by_image_id(db: Session, image_id: str):
    return db.query(models.Violation).filter(models.Violation.image_id == image_id).all()

def get_violations_by_person(db: Session):
    results = db.query(
        models.Violation.person_id,
        func.count(models.Violation.id).label("violation_count")
    ).group_by(models.Violation.person_id).all()

    return [{"person_id": r.person_id, "violation_count": r.violation_count} for r in results]
