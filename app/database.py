from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Замените на вашу строку подключения
DATABASE_URL = "sqlite:///database.db"  # Пример для SQLite

# Создание движка базы данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Для SQLite

# Создание базового класса
Base = declarative_base()

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()