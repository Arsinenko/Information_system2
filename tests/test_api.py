import aiohttp
import asyncio
import random

# Определите header перед использованием
header = {
    "Content-Type": "application/json"
}

async def create_attendance(session, id_schedule, id_student, header):
    data = {
        "id_schedule": id_schedule,
        "id_student": id_student,
        "status": random.choices(["present", "absent"], weights=[0.7, 0.3], k=1)[0]
    }
    async with session.post("http://localhost:8000/api/v1/create_attendance", 
                             headers=header, 
                             json=data) as response:
        return await response.json()

async def get_students_by_group(session, id_group):
    # Асинхронный метод получения студентов 
    # Замените на ваш реальный метод
    async with session.get(f"http://localhost:8000/api/v1/students_by_group/{id_group}") as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        # Получаем расписание 
        async with session.get("http://localhost:8000/api/v1/get_schedules") as response:
            schedules = await response.json()
        
        # Список задач для выполнения
        tasks = []
        
        for schedule in schedules["message"]:
            id_schedule = schedule["id"]
            students = await get_students_by_group(session, schedule["id_group"])
            
            # Создаем задачи для каждого студента
            for student in students:
                task = asyncio.create_task(
                    create_attendance(session, id_schedule, student, header)
                )
                tasks.append(task)
        
        # Ждем завершения всех задач
        await asyncio.gather(*tasks)

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(main())