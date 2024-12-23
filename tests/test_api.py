import requests
from faker import Faker 

BASE_URL = "http://localhost:8000"  # Update with the correct base URL for your API
header = header = {"Content-Type": "application/json"}

def test_create_specialization():
    response = requests.post(f"{BASE_URL}/api/v1/create_specialization/", headers=header, json={
        "name": "Test Specialization"
    })
    print("Create Specialization Status Code:", response.status_code)

def test_create_student():
    response = requests.post(f"{BASE_URL}/api/v1/create_student/", headers=header, json={
        "first_name": "Test",
        "middle_name": "Student",
        "last_name": "Example",
        "id_group": 1  # Assuming this ID exists
    })
    print("Create Student Status Code:", response.status_code)

def test_create_teacher():
    response = requests.post(f"{BASE_URL}/api/v1/create_teacher/", headers=header, json={
        "first_name": "Test",
        "middle_name": "Teacher",
        "last_name": "Example"
    })
    print("Create Teacher Status Code:", response.status_code)

if __name__ == "__main__":
    test_create_specialization()
    test_create_student()
    test_create_teacher()
