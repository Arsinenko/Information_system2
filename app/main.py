from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app.models import Specialization, Group, Program, Student, Teacher, Subject, AttendanceLog, Attendance  # Импортируйте ваши модели
import uvicorn
from app.schemas import *
from app.routers import create, read, update, delete
# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(create.router)
app.include_router(read.router)
# app.include_router(update.router)
app.include_router(delete.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


