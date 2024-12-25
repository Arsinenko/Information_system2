from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from app.Models.create_models import *
from app.database import get_db
from app.schemas.schemas import GetStudentsByGroup, GetStudentAttendance

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

@router.get("/api/get_subjects")
async def get_subjects(db: Session = Depends(get_db)):
    try:
        subjects = db.query(Subject).all()
        result = [{"id": subject.id, "name": subject.name} for subject in subjects]
        return JSONResponse(content={"message": result}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=500)
    
@router.get("/api/v1/get_programs")
async def get_programs(db: Session = Depends(get_db)):
    try:
        programs = db.query(Program).all()
        result = [{"id": program.id, "name": program.name, "id_specialization": program.id_specialization, "id_subject":program.id_subject, "hours": program.hours} for program in programs]
        return JSONResponse(content={"message": result}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)})
    


@router.get("/api/v1/get_students_by_group_id")
async def get_students_by_group(model: GetStudentsByGroup, db: Session = Depends(get_db)):
    try:
        students = db.query(Student).filter(Student.id_group == model.id_group).all()
        result = [{
            "id": student.id,
            "first_name": student.first_name,
            "middle_name": student.middle_name,
            "last_name": student.last_name
            } for student in students]
        return JSONResponse(content={"message": result}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=500)  

@router.get("/api/v1/get_schedules")
async def get_schedules(db: Session = Depends(get_db)):
    try:
        schedules = db.query(Schedule).all()
        result = [{
            "id": elem.id,
            "id_subject": elem.id_subject,
            "id_group": elem.id_group,
            "lesson_number": elem.lesson_number,
            "date_of_lesson": str(elem.date_of_lesson)
            } for elem in schedules]
        return JSONResponse(content={"message": result}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)})
    
@router.get("/api/v1/get_student_attendance")
async def get_student_attendance(model: GetStudentAttendance, db: Session = Depends(get_db)):
    try:
        student_exists = db.query(Student).filter(Student.id == model.id_student).first()
        if not student_exists:
            return JSONResponse(content={"message": "Student not found!"})
        attendance = db.query(Attendance).filter(Attendance.id_student == model.id_student).join(Schedule).join()

        