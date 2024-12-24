from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Time
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

    id_specialization = Column(Integer, ForeignKey('Specializations.id'), nullable=False)

    

    specialization = relationship("Specialization")


class Program(Base):

    __tablename__ = 'Programs'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(255), nullable=False)

    id_specialization = Column(Integer, ForeignKey('Specializations.id'), nullable=False)
    
    id_subject = Column(Integer, ForeignKey('Subjects.id'), nullable=False)

    hours = Column(Integer, nullable=False)

    
    subject = relationship("Subject")
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

    id_teacher = Column(Integer, ForeignKey('Teachers.id'), nullable=False)


    teacher = relationship("Teacher")



class Attendance(Base):

    __tablename__ = 'Attendance'

    

    id = Column(Integer, primary_key=True, autoincrement=True)

    id_schedule = Column(Integer, ForeignKey('Schedules.id'), nullable=False)
    
    id_student = Column(Integer, ForeignKey('Students.id'), nullable=False)

    status = Column(Text)

    
    schedule = relationship("Schedule")
    student = relationship("Student")

class Schedule(Base):

    __tablename__ = 'Schedules'


    id = Column(Integer, primary_key=True, autoincrement=True)

    

    id_subject = Column(Integer, ForeignKey('Subjects.id'), nullable=False)

    id_group = Column(Integer, ForeignKey('Groups.id'), nullable=False)

    lesson_number = Column(Integer, nullable=False)
    
    date_of_lesson = Column(Date, nullable=False)


    subject = relationship("Subject")

    group = relationship("Group")