from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app import detect, crud, models, schemas
from app.database import Base, engine, SessionLocal
import os
import cv2
import numpy as np
import uuid
import base64
import threading

app = FastAPI()

# Enable CORS for all origins (use your frontend domain in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables on startup
Base.metadata.create_all(bind=engine)

@app.post("/detect/")
async def detect_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static/faces", exist_ok=True)

    image_id = str(uuid.uuid4())
    image_path = f"uploads/{image_id}.jpg"
    cv2.imwrite(image_path, frame)

    annotated, violations = detect.detect_ppe(image_path)

    db = SessionLocal()
    try:
        for v in violations:
            v['image_id'] = image_id
            crud.create_violation(db, v)
    finally:
        db.close()

    success, encoded_img = cv2.imencode(".jpg", annotated)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to encode image")

    encoded_str = base64.b64encode(encoded_img).decode('utf-8')

    return JSONResponse({
        "image_id": image_id,
        "annotated_image_base64": encoded_str
    })

@app.get("/violations/{image_id}", response_model=list[schemas.ViolationOut])
def get_violations_by_image(image_id: str):
    db = SessionLocal()
    try:
        violations = crud.get_violations_by_image_id(db, image_id)
        if not violations:
            raise HTTPException(status_code=404, detail="No violations found for this image_id")
        return violations
    finally:
        db.close()

@app.get("/webcam/")
def webcam_page():
    def run_webcam():
        # This function should implement your webcam PPE detection logic.
        # The argument save_violations_to_db=True will store violations in DB.
        detect.detect_from_webcam(save_violations_to_db=True)

    # Start webcam detection in a background daemon thread
    thread = threading.Thread(target=run_webcam, daemon=True)
    thread.start()

    # Return simple HTML informing user that webcam feed window opened
    return HTMLResponse("""
    <html>
        <head><title>Webcam PPE Detection</title></head>
        <body>
            <h1>Webcam Detection Running</h1>
            <p>A window with live webcam feed is open. Press <b>Q</b> in that window to quit.</p>
        </body>
    </html>
    """)
