from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app.Models.create_models import Specialization, Group, Program, Student, Teacher, Subject, Attendance  # Импортируйте ваши модели
import uvicorn
from app.schemas.schemas import *
from app.routers import create, read, update, delete

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(create.router)
app.include_router(read.router)
# app.include_router(update.router)
app.include_router(delete.router)

@app.get("/")
async def index():
    return FileResponse("app/ui/index.html", media_type="text/html")
@app.get("/groups")
async def groups_page():
    return FileResponse("app/ui/groups.html", media_type="text/html")

@app.get("/group/{group_id}/{name}")
async def group_page(group_id: int, name: str):
    return FileResponse("app/ui/group.html", media_type="text/html")

@app.get("/students/")
async def students_page():
    return FileResponse("app/ui/students.html", media_type="text/html")

@app.get("/student_attendance/{id}")
async def student_attendance(id: int):
    return FileResponse("app/ui/student_attendance.html", media_type="text/html")

@app.get("/subjects")               
async def subjects_page():
    return FileResponse("app/ui/subjects.html", media_type="text/html")

@app.get("/admin_page")
async def admin_page():
    return FileResponse("app/ui/admin_page.html", media_type="text/html")

@app.get("/specializations")
async def specializations_page():
    return FileResponse("app/ui/specializations.html", media_type="text/html")

@app.get("/create_group")
async def create_group_page():
    return FileResponse("app/ui/create_group.html", media_type="text/html")

@app.get("/create_student")
async def create_student_page():
    return FileResponse("app/ui/create_student.html", media_type="text/html")

@app.get("/create_subject")
async def create_subject_page():
    return FileResponse("app/ui/create_subject.html", media_type="text/html")

@app.get("/create_teacher")
async def create_teacher_page():
    return FileResponse("app/ui/create_teacher.html", media_type="text/html")

@app.get("/create_specialization")
async def create_specialization_page():
    return FileResponse("app/ui/create_specialization.html")

@app.get("/create_report")
async def create_report_page():
    return FileResponse("app/ui/create_report.html")



    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


