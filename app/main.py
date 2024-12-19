from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Specialization, Group, Program, Student, Teacher, Subject, AttendanceLog, Attendance  # Импортируйте ваши модели
import uvicorn
from schemas import *
# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
### Create
@app.post("/api/v1/create_specializations/")
def create_specialization(specialization: SpecializationModel, db: Session = Depends(get_db)):
    db_specialization = Specialization(name=specialization.name)
    db.add(db_specialization)
    db.commit()
    db.refresh(db_specialization)
    return JSONResponse(content={"message": "Specialization created successfully"}, status_code=201)

@app.post("/api/v1/create_groups/")
def create_group(group: GroupModel, db: Session = Depends(get_db)):
    db_group = Group(
        group_name=group.group_name,
        size=group.size,
        id_specialization=group.id_specialization
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.post("/api/v1/create_programs/")
def create_program(program: ProgramModel, db: Session = Depends(get_db)):
    db_program = Program(
        name=program.name,
        id_specialization=program.id_specialization,
        hours=program.hours
    )
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

@app.post("/api/v1/create_students/")
def create_student(student: StudentModel, db: Session = Depends(get_db)):
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

@app.post("/api/v1/create_teachers/")
def create_teacher(teacher: TeacherModel, db: Session = Depends(get_db)):
    db_teacher = Teacher(
        first_name=teacher.first_name,
        middle_name=teacher.middle_name,
        last_name=teacher.last_name
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.post("/api/v1/create_subjects/")
def create_subject(subject: SubjectModel, db: Session = Depends(get_db)):
    db_subject = Subject(
        name=subject.name,
        id_program=subject.id_program,
        id_teacher=subject.id_teacher
    )
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@app.post("/api/v1/create_attendance_logs/")
def create_attendance_log(attendance_log: AttendanceLogModel, db: Session = Depends(get_db)):
    db_attendance_log = AttendanceLog(
        id_subject=attendance_log.id_subject,
        date=attendance_log.date
    )
    db.add(db_attendance_log)
    db.commit()
    db.refresh(db_attendance_log)
    return db_attendance_log

@app.post("/api/v1/create_attendance/")
def create_attendance(attendance: AttendanceModel, db: Session = Depends(get_db)):
    db_attendance = Attendance(
        id_attendance_log=attendance.id_attendance_log,
        id_student=attendance.id_student,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance




# Добавьте другие маршруты по мере необходимости
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

