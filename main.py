from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import date

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change "*" to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (replace with DB later)
reports = [
    {"id": 1, "dept": "Computer Science", "title": "Annual Report 2024", "date": "2024-12-15", "status": "approved"},
    {"id": 2, "dept": "Mathematics", "title": "Department Report 2024", "date": "2024-12-10", "status": "pending"},
    {"id": 3, "dept": "Physics", "title": "Research Summary 2024", "date": "2024-12-08", "status": "submitted"},
]

users = {
    "admin": {"password": "admin123", "role": "Administrator"},
    "faculty1": {"password": "fac123", "role": "Faculty"},
    "hod1": {"password": "hod123", "role": "Department Head"}
}

# Routes
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username in users and users[username]["password"] == password:
        return {"success": True, "role": users[username]["role"]}
    return {"success": False, "message": "Invalid credentials"}

@app.get("/reports")
def get_reports():
    return {"reports": reports}

@app.post("/upload-report")
async def upload_report(
    dept: str = Form(...),
    title: str = Form(...),
    file: UploadFile = None
):
    new_report = {
        "id": len(reports) + 1,
        "dept": dept,
        "title": title,
        "date": str(date.today()),
        "status": "submitted"
    }
    reports.append(new_report)
    return {"message": "Report uploaded successfully", "report": new_report}
