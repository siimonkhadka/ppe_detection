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
cd minor-project-backend

##. (Optional) Create and activate a virtual environment:

python -m venv venv
 # Linux/Mac
source venv/bin/activate
 # Windows
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Start the backend server:
"uvicorn app.main:app --reload"
The backend will run at http://127.0.0.1:8000.

## Frontend Setup
  Prerequisites
   1. Node.js
   2. npm

Steps
1. Navigate to the frontend folder:
cd minor

2. Install dependencies:
npm install

3. Start the frontend:
npm start
The frontend will run at http://localhost:3000.

🚀 Usage
                      👤 For Users

1. Open the frontend in your browser.

2. Login or create a new user account.

3. Perform PPE detection by uploading an image or video.

4. View real-time feedback on your dashboard:

      ✅ All PPE worn: "You are good to go"

      ⚠️ Missing PPE: "Danger! Please wear missing PPE"

5. Each detection automatically logs the time, date, and PPE status.

                     🧑‍💼 For Managers

  1. Login as a manager.

  2. Monitor all users’ PPE compliance records.

  3. Create or delete users as needed.

  4. Ensure overall safety compliance in your organization.

📈 Future Enhancements

   1. Add support for more PPE types (gloves, masks, safety shoes).

   2. Real-time video monitoring with alert notifications.

   3. Advanced analytics dashboard for managers.
