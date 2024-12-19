from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Specialization, Group, Program, Student, Teacher, Subject, AttendanceLog, Attendance  # Импортируйте ваши модели
import uvicorn
# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Пример маршрута для получения всех специализаций
@app.get("/specializations/")
def read_specializations(db: Session = Depends(get_db)):
    return db.query(Specialization).all()

# Добавьте другие маршруты по мере необходимости
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

