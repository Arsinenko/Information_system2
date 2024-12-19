from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base




class Specialization(Base):

    __tablename__ = 'Specializations'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(255), nullable=False, unique=True)


class Group(Base):

    __tablename__ = 'Groups'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    group_name = Column(String(255), nullable=False, unique=True)

    size = Column(Integer, nullable=False, default=0)

    id_specialization = Column(Integer, ForeignKey('Specializations.id'), nullable=False)

    

    specialization = relationship("Specialization")


class Program(Base):

    __tablename__ = 'Programs'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(255), nullable=False)

    id_specialization = Column(Integer, ForeignKey('Specializations.id'), nullable=False)

    hours = Column(Integer, nullable=False)

    

    specialization = relationship("Specialization")


class Student(Base):

    __tablename__ = 'Students'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String(255), nullable=False)

    middle_name = Column(String(255))

    last_name = Column(String(255), nullable=False)

    id_group = Column(Integer, ForeignKey('Groups.id'), nullable=False)

    

    group = relationship("Group")


class Teacher(Base):

    __tablename__ = 'Teachers'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String(255), nullable=False)

    middle_name = Column(String(255))

    last_name = Column(String(255), nullable=False)


class Subject(Base):

    __tablename__ = 'Subjects'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(255), nullable=False)

    id_program = Column(Integer, ForeignKey('Programs.id'), nullable=False)

    id_teacher = Column(Integer, ForeignKey('Teachers.id'), nullable=False)

    

    program = relationship("Program")

    teacher = relationship("Teacher")


class AttendanceLog(Base):

    __tablename__ = 'Attendance_logs'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    id_subject = Column(Integer, ForeignKey('Subjects.id'), nullable=False)

    date = Column(Date, nullable=False)

    

    subject = relationship("Subject")


class Attendance(Base):

    __tablename__ = 'Attendance'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    id_attendance_log = Column(Integer, ForeignKey('Attendance_logs.id'), nullable=False)

    id_student = Column(Integer, ForeignKey('Students.id'), nullable=False)

    status = Column(Text)

    

    attendance_log = relationship("AttendanceLog")

    student = relationship("Student")