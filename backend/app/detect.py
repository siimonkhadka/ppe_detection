from ultralytics import YOLO
import cv2
import os
import uuid
from app.database import SessionLocal
from app import crud

# Load your trained model
model = YOLO('C:/Users/user/minor_project/runs/train/my_yolov8_model3/weights/best.pt')

COLOR_MAP = {
    'Helmet': (0, 255, 0),
    'Vest': (0, 255, 0),
    'NoHelmet': (0, 0, 255),
    'NoVest': (0, 0, 255),
    'Person': (255, 255, 0)
}

violation_labels = ["NoHelmet", "NoVest"]

def detect_ppe(image_path: str):
    frame = cv2.imread(image_path)
    return _detect_logic(frame, image_path)

def detect_from_webcam(save_violations_to_db=True):
    cap = cv2.VideoCapture(0)
    os.makedirs("static/faces", exist_ok=True)

    db = SessionLocal() if save_violations_to_db else None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        pred_img, violations = _detect_logic(frame)

        # Save violations to DB if enabled
        if save_violations_to_db and db:
            for v in violations:
                crud.create_violation(db, v)

        cv2.imshow("Webcam PPE Detection", pred_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if db:
        db.close()

def _detect_logic(frame, save_image_path=None):
    results = model(frame)

    os.makedirs("static/faces", exist_ok=True)
    violations = []
    pred_img = frame.copy()
    occupied_regions = []

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        conf = float(box.conf[0])

        if cls_name == 'Person':
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        color = COLOR_MAP.get(cls_name, (255, 255, 255))
        label = f"{cls_name} {conf:.2f}"

        # Draw bounding box
        cv2.rectangle(pred_img, (x1, y1), (x2, y2), color, 2)

        # Calculate label position
        text_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        text_w, text_h = text_size
        y_text = y1 - 10 if y1 - 10 > text_h else y1 + text_h + 10
        x_text = max(0, min(x1, pred_img.shape[1] - text_w))

        for (ox1, oy1, ox2, oy2) in occupied_regions:
            if (x_text < ox2 and x_text + text_w > ox1) and (y_text < oy2 and y_text + text_h > oy1):
                y_text = oy2 + 5

        occupied_regions.append((x_text, y_text, x_text + text_w, y_text + text_h))

        cv2.putText(pred_img, label, (x_text, y_text), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Crop face for violations only
        if cls_name in violation_labels:
            face_top = y1
            face_bottom = y1 + int((y2 - y1) * 0.4)  # Top 40% for face
            face_left = x1
            face_right = x2

            face_crop = frame[face_top:face_bottom, face_left:face_right]

            if face_crop.size > 0:
                face_id = str(uuid.uuid4())
                face_path = f"static/faces/{face_id}.jpg"
                cv2.imwrite(face_path, face_crop)

                violations.append({
                    "label": cls_name,
                    "confidence": f"{conf:.2f}",
                    "face_path": face_path,
                    "person_id": face_id
                })

    if save_image_path:
        cv2.imwrite(save_image_path, pred_img)

    return pred_img, violations


if __name__ == "__main__":
    detect_from_webcam()
