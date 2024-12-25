from fastapi.responses import JSONResponse
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.Models.create_models import *
from app.database import get_db
from app.schemas.schemas import *
import datetime as dt

router = APIRouter()
### Create
@router.post("/api/v1/create_specialization/")
async def create_specialization(specialization: SpecializationModel, db: Session = Depends(get_db)):
    try:    
        db_specialization = Specialization(name=specialization.name)
        db.add(db_specialization)
        db.commit()
        db.refresh(db_specialization)
        return JSONResponse(content={"message": "Specialization created successfully"}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating specialization: {e}"}, status_code=500)


@router.post("/api/v1/create_group/")
async def create_group(group: GroupModel, db: Session = Depends(get_db)):
    try:
        db_group = Group(
            group_name=group.group_name,
            id_specialization=group.id_specialization
        )
        # Check if the specialization exists
        specialization_exists = db.query(Specialization).filter(Specialization.id == group.id_specialization).first()
        if not specialization_exists:
            return JSONResponse(content={"message": "Error: Specialization does not exist."}, status_code=400)

        db.add(db_group)
        db.commit()
        db.refresh(db_group)
        return db_group
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating group: {e}"}, status_code=500)

@router.post("/api/v1/create_program/")
async def create_program(program: ProgramModel, db: Session = Depends(get_db)):
    try:
        spec_exests = db.query(Specialization).filter(Specialization.id == program.id_specialization).first()
        if not spec_exests:
            return JSONResponse(content={"message": "Specialization does not exist."}, status_code=400)
        subject_exists = db.query(Subject).filter(Subject.id == program.id_subject).first()
        if not subject_exists:
            return JSONResponse(content={"message": "Subject does not exist"}, status_code=400)
        db_program = Program(
            name=program.name,
            id_specialization=program.id_specialization,
            id_subject=program.id_subject,
            hours=program.hours
        )
        
        db.add(db_program)
        db.commit()
        db.refresh(db_program)
        return db_program
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating program: {e}"}, status_code=500)


@router.post("/api/v1/create_student/")
async def create_student(student: StudentModel, db: Session = Depends(get_db)):
    try:
        # Check if the group exists
        group_exists = db.query(Group).filter(Group.id == student.id_group).first()
        if not group_exists:
            return JSONResponse(content={"message": "Error: Group does not exist."}, status_code=400)

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

@router.post("/api/v1/create_teacher/")
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

@router.post("/api/v1/create_subject/")
async def create_subject(subject: SubjectModel, db: Session = Depends(get_db)):
    try:
        teacher_exists = db.query(Teacher).filter(Teacher.id == subject.id_teacher).first()
        if teacher_exists == None:
            return JSONResponse(content={"message": "Error: Teacher does not exist."}, status_code=400)
        db_subject = Subject(
            name=subject.name,
            id_teacher=subject.id_teacher
        )

        db.add(db_subject)
        db.commit()
        db.refresh(db_subject)
        return db_subject
    except Exception as e:
        return JSONResponse(content={"message": f"Error creating subject: {e}"}, status_code=500)


# @router.post("/api/v1/create_attendance/")
# async def create_attendance(attendance: AttendanceModel, db: Session = Depends(get_db)):
#     try:
#         db_attendance = Attendance(
#             id_attendance_log=attendance.id_attendance_log,
#             id_student=attendance.id_student,
#             status=attendance.status
#         )
#         # Check if the attendance log and student exist
#         attendance_log_exists = db.query(AttendanceLog).filter(AttendanceLog.id == attendance.id_attendance_log).first()
#         if not attendance_log_exists:
#             return JSONResponse(content={"message": "Error: Attendance log does not exist."}, status_code=400)

#         student_exists = db.query(Student).filter(Student.id == attendance.id_student).first()
#         if not student_exists:
#             return JSONResponse(content={"message": "Error: Student does not exist."}, status_code=400)

#         db.add(db_attendance)
#         db.commit()
#         db.refresh(db_attendance)
#         return db_attendance
#     except Exception as e:
#         return JSONResponse(content={"message": f"Error creating attendance: {e}"}, status_code=500)

@router.post("/api/v1/create_schedule")
async def create_schedule(schedule: ScheduleModel, db: Session = Depends(get_db)):
    try:
        subject_exiests = db.query(Subject).filter(Subject.id == schedule.id_subject).first()
        if not subject_exiests:
            return JSONResponse(content={"message": "Subject does not exists"}, status_code=400)
        group_exists = db.query(Group).filter(Group.id == schedule.id_group).first()
        if not group_exists:
            return JSONResponse({"message": "Group does not exists"}, status_code=400)
        
        db_schedule = Schedule(id_subject=schedule.id_subject, id_group=schedule.id_group, lesson_number=schedule.lesson_number, date_of_lesson=dt.datetime.strptime(schedule.date_of_lesson, "%Y-%m-%d").date())
        db.add(db_schedule)
        db.commit()
        db.refresh(db_schedule)
        return db_schedule
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=500)

@router.post("/api/v1/create_attendance")
async def create_attendance(attendance: AttendanceModel, db: Session = Depends(get_db)):
    try:
        schedule_exists = db.query(Schedule).filter(Schedule.id == attendance.id_schedule).first()
        if not schedule_exists:
            return JSONResponse(content={"message": "Schedule does not exists"}, status_code=400)
        student_exists = db.query(Student).filter(Student.id == attendance.id_student).first()
        if not student_exists:
            return JSONResponse(content={"messsage": "Student does not exists"}, status_code=400)
        db_attendance = Attendance(id_schedule=attendance.id_schedule, id_student=attendance.id_student, status=attendance.status)
        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)
        return db_attendance
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=500)