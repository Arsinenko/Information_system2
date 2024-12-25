from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, case
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
async def get_student_attendance_statistics(model: GetStudentAttendance, db: Session = Depends(get_db)):
    try:
        student_exists = db.query(Student).filter(Student.id == model.id_student).first()
        if not student_exists:
            return JSONResponse(content={"message": "Student not found!"}, status_code=404)

        total_attendance = db.query(Attendance).filter(Attendance.id_student == model.id_student).count()
        present_count = db.query(Attendance).filter(Attendance.id_student == model.id_student, Attendance.status == "present").count()
        absent_count = max(0, total_attendance - present_count)  # Избегаем отрицательных значений

        present_percentage = (present_count / total_attendance * 100) if total_attendance > 0 else 0
        absent_percentage = (absent_count / total_attendance * 100) if total_attendance > 0 else 0

        subjects_attendance = db.query(
            Subject.name,
            func.count(Attendance.id).label("total"),
            func.sum(case((Attendance.status == "present", 1), else_=0)).label("present_count"),
            func.sum(case((Attendance.status == "absent", 1), else_=0)).label("absent_count")
        ).select_from(Attendance)\
        .join(Schedule, Attendance.id_schedule == Schedule.id)\
        .join(Subject, Schedule.id_subject == Subject.id)\
        .filter(Attendance.id_student == model.id_student)\
        .group_by(Subject.id, Subject.name).all()

        result = {
            "total_attendance": total_attendance,
            "present_count": present_count,
            "absent_count": absent_count,
            "present_percentage": present_percentage,
            "absent_percentage": absent_percentage,
            "subjects_attendance": [
                {
                    "subject_name": subject.name,
                    "total": subject.total,
                    "present": subject.present_count,
                    "absent": subject.absent_count
                } for subject in subjects_attendance
            ]
        }
        return JSONResponse(content=result, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=500)
        

        

        