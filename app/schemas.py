from pydantic import BaseModel
import datetime as dt

### Create models
class SpecializationModel(BaseModel):
    name: str

class GroupModel(BaseModel):
    group_name: str
    size: int
    id_specialization: int

class ProgramModel(BaseModel):
    name: str
    id_specialization: int
    hours: int

class StudentModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    id_group: int

class TeacherModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    
class SubjectModel(BaseModel):
    name: str
    id_program: int
    id_teacher: int
    
class AttendanceLogModel(BaseModel):
    id_subject: int
    date: dt.date

class AttendanceModel(BaseModel):
    id_attendance_log: int
    id_student: int
    status: str


### Delete entities
class DeleteByIdModel(BaseModel):
    id: int
