from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from app.Models.create_models import *
from app.database import get_db

router = APIRouter()

@router.get("/api/v1/get_specializations/")
def get_specializations(db: Session = Depends(get_db)):
    specializations = db.query(Specialization).all()
    return JSONResponse(content={"specializations": specializations}, status_code=200)

@router.get("/api/v1/get_groups/")
def get_groups(db: Session = Depends(get_db)):
    groups = db.query(Group).all()
    return JSONResponse(content={"groups": groups}, status_code=200)

@router.get("/api/v1/get_programs/")
def get_programs(db: Session = Depends(get_db)):
    programs = db.query(Program).all()
    return JSONResponse(content={"programs": programs}, status_code=200)

@router.get("/api/v1/get_students/")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return JSONResponse(content={"students": students}, status_code=200)

@router.get("/api/v1/get_teachers/")
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    return JSONResponse(content={"teachers": teachers}, status_code=200)

@router.get("/api/v1/get_subjects/")
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return JSONResponse(content={"subjects": subjects}, status_code=200)

@router.get("/api/v1/get_attendance_logs/")
def get_attendance_logs(db: Session = Depends(get_db)):
    attendance_logs = db.query(AttendanceLog).all()
    return JSONResponse(content={"attendance_logs": attendance_logs}, status_code=200)

@router.get("/api/v1/get_attendance/")
def get_attendance(db: Session = Depends(get_db)):
    attendance = db.query(Attendance).all()
    return JSONResponse(content={"attendance": attendance}, status_code=200)

