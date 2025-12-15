# PPE Detection System

This project is a **Personal Protective Equipment (PPE) Detection System** designed to ensure workplace safety by detecting whether users are wearing vests and helmets. The system integrates a **YOLOv8-based AI model**, a **FastAPI backend**, a **React frontend**, and an **SQLite database**.

---

## Features

### For Users
- Personal dashboard for each user.
- Perform daily PPE checks using **images or videos**.
- Detects whether the user is wearing:
  - Vest
  - Helmet
- Real-time feedback:
  - ✅ "You are good to go" if all PPE is present.
  - ⚠️ "Danger! Please wear missing PPE" if any equipment is missing.
- Records **time, date, and PPE status** for each check.

### For Managers
- Oversee all users’ PPE compliance.
- View records with **time, date, and PPE status**.
- Create or delete users.
- Ensure safety compliance across the organization.

---

## Tech Stack
- **Model:** YOLOv8 for PPE detection
- **Backend:** FastAPI
- **Frontend:** React
- **Database:** SQLite

---

## Backend Setup

### Prerequisites
- Python 3.10+
- pip
- Virtual environment (recommended)

### Steps
1. Navigate to the backend folder:

```bash
cd minor-project-backend
(Optional) Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Start the backend server:

bash
Copy code
uvicorn app.main:app --reload
The backend will run at http://127.0.0.1:8000.

Frontend Setup
Prerequisites
Node.js

npm

Steps
Navigate to the frontend folder:

bash
Copy code
cd minor
Install dependencies:

bash
Copy code
npm install
Start the frontend:

bash
Copy code
npm start
The frontend will run at http://localhost:3000.

Usage
For Users
Open the frontend in your browser.

Login or create a new user account.

Perform PPE detection by uploading an image or video.

View detection results and feedback in your personal dashboard:

✅ All PPE worn: "You are good to go"

⚠️ Missing PPE: "Danger! Please wear missing PPE"

Each detection automatically records the time, date, and PPE status.

## For Managers
Login as a manager.

View all users’ PPE compliance records.

Create new users or delete users if needed.

Ensure overall safety compliance in the organization.


Copy code
User → Upload Image/Video → YOLOv8 PPE Detection → Feedback (Good/Danger) → Records Saved → Manager Oversight
(Optional: Replace with an actual visual diagram for better presentation.)

License
This project is licensed under the MIT License.
