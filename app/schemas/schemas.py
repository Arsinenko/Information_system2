from pydantic import BaseModel
import datetime as dt

### Create models
class SpecializationModel(BaseModel):
    name: str

class GroupModel(BaseModel):
    group_name: str
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
    
###Update models
    
class UpdateSpecializationModel(BaseModel):
    id: int
    name: str

class UpdateGroupModel(BaseModel):
    id: int
    group_name: str
    size: int
    id_specialization: int

class UpdateProgramModel(BaseModel):
    id: int
    name: str
    id_specialization: int
    hours: int

class UpdateStudentModel(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    id_group: int

class UpdateTeacherModel(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str

class UpdateSubjectModel(BaseModel):
    id: int
    name: str
    id_program: int
    id_teacher: int

class UpdateAttendanceLogModel(BaseModel):
    id: int
    id_subject: int
    date: dt.date

class UpdateAttendanceModel(BaseModel):
    id: int
    id_attendance_log: int
    id_student: int
    status: str

class UpdateSpecialization(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True

