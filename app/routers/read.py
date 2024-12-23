from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from app.Models.create_models import *
from app.database import get_db

router = APIRouter()

@router.get("/api/v1/get_specializations")
def get_specializations(db: Session = Depends(get_db)):
    specializations = db.query(Specialization).all()
    result = [{"id": s.id, "name": s.name} for s in specializations]
    return JSONResponse(content={"specializations": specializations}, status_code=200)

@router.get("/api/v1/get_groups/")
def get_groups(db: Session = Depends(get_db)):
    groups = db.query(Group).all()
    groups_list = [{"id": group.id, "name": group.group_name} for group in groups]
    return JSONResponse(content={"groups": groups_list}, status_code=200)

@router.get("/api/v1/get_programs/")
def get_programs(db: Session = Depends(get_db)):
    programs = db.query(Program).all()
    result = [{"id": group.id, "name": group.name, "specialization_id": group.id_specialization} for group in programs]
    return JSONResponse(content={"programs": result}, status_code=200)

@router.get("/api/v1/get_students/")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    result = [{"id": student.id,
               "first_name": student.first_name,
               "middle_name": student.middle_name,
               "last_name": student.last_name,
               "group_id": student.id_group,
               } for student in students]
    return JSONResponse(content={"students": result}, status_code=200)

@router.get("/api/v1/get_teachers/")
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    result = [{"id": teacher.id,
               "first_name": teacher.first_name,
               "middle_name": teacher.middle_name,
               "last_name": teacher.last_name} for teacher in teachers]
    return JSONResponse(content={"teachers": result}, status_code=200)

@router.get("/api/v1/get_subjects/")
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    result = [{"id": subject.id,
               "name": subject.name,
               "id_program": subject.id_program,
               "id_teacher": subject.id_teacher} for subject in subjects]
    return JSONResponse(content={"subjects": result}, status_code=200)

@router.get("/api/v1/get_attendance_logs/")
def get_attendance_logs(db: Session = Depends(get_db)):
    attendance_logs = db.query(AttendanceLog).all()
    result = [{"id": log.id,
              "id_subject": log.id_subject,
              "date": log.date} for log in attendance_logs]
    return JSONResponse(content={"attendance_logs": result}, status_code=200)

@router.get("/api/v1/get_attendance/")
def get_attendance(db: Session = Depends(get_db)):
    attendance = db.query(Attendance).all()
    result = [{"id": a.id,
               "id_attendance_log": a.id_attendance_log,
               "id_student": a.id_student,
               "status": a.status} for a in attendance]
    return JSONResponse(content={"attendance": result}, status_code=200)

