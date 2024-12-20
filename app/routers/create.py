from fastapi.responses import JSONResponse
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.Models.create_models import *
from app.database import get_db
from app.schemas.schemas import *

router = APIRouter()
### Create
@router.post("/api/v1/create_specializations/")
async def create_specialization(specialization: SpecializationModel, db: Session = Depends(get_db)):
    try:    
        db_specialization = Specialization(name=specialization.name)
        db.add(db_specialization)
        db.commit()
        db.refresh(db_specialization)
        return JSONResponse(content={"message": "Specialization created successfully"}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating specialization: {e}"}, status_code=500)


@router.post("/api/v1/create_groups/")
async def create_group(group: GroupModel, db: Session = Depends(get_db)):
    try:
        db_group = Group(
            group_name=group.group_name,
            size=group.size,
            id_specialization=group.id_specialization
        )
        db.add(db_group)
        db.commit()
        db.refresh(db_group)
        return db_group
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating group: {e}"}, status_code=500)

@router.post("/api/v1/create_programs/")
async def create_program(program: ProgramModel, db: Session = Depends(get_db)):
    try:
        db_program = Program(
            name=program.name,
            id_specialization=program.id_specialization,
            hours=program.hours
        )
        db.add(db_program)
        db.commit()
        db.refresh(db_program)
        return db_program
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating program: {e}"}, status_code=500)


@router.post("/api/v1/create_students/")
async def create_student(student: StudentModel, db: Session = Depends(get_db)):
    try:
        db_student = Student(
            first_name=student.first_name,
            middle_name=student.middle_name,
            last_name=student.last_name,
            id_group=student.id_group
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating student: {e}"}, status_code=500)

@router.post("/api/v1/create_teachers/")
async def create_teacher(teacher: TeacherModel, db: Session = Depends(get_db)):
    try:
        db_teacher = Teacher(
            first_name=teacher.first_name,
            middle_name=teacher.middle_name,
            last_name=teacher.last_name
        )
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating teacher: {e}"}, status_code=500)

@router.post("/api/v1/create_subjects/")
async def create_subject(subject: SubjectModel, db: Session = Depends(get_db)):
    try:
        db_subject = Subject(
            name=subject.name,
            id_program=subject.id_program,
            id_teacher=subject.id_teacher
        )
        db.add(db_subject)
        db.commit()
        db.refresh(db_subject)
        return db_subject
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating subject: {e}"}, status_code=500)

@router.post("/api/v1/create_attendance_logs/")
async def create_attendance_log(attendance_log: AttendanceLogModel, db: Session = Depends(get_db)):
    try:
        db_attendance_log = AttendanceLog(
            id_subject=attendance_log.id_subject,
            date=attendance_log.date
        )
        db.add(db_attendance_log)
        db.commit()
        db.refresh(db_attendance_log)
        return db_attendance_log
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating attendance log: {e}"}, status_code=500)

@router.post("/api/v1/create_attendance/")
async def create_attendance(attendance: AttendanceModel, db: Session = Depends(get_db)):
    try:
        db_attendance = Attendance(
            id_attendance_log=attendance.id_attendance_log,
            id_student=attendance.id_student,
            status=attendance.status
        )
        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)
        return db_attendance
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating attendance: {e}"}, status_code=500)
