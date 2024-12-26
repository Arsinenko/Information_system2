
# API Documentation

This document provides detailed information about the available API endpoints.

## Base URL
All endpoints are relative to: `http://localhost:8000`

## API Endpoints

### Specializations

#### Get All Specializations
```http
GET /api/v1/get_specializations
```
Returns a list of all specializations.

**Response**
```json
{
    "specializations": [
        {
            "id": integer,
            "name": string
        }
    ]
}
```

#### Create Specialization
```http
POST /api/v1/create_specialization
```
Creates a new specialization.

**Request Body**
```json
{
    "name": string
}
```

**Response**
```json
{
    "message": "Specialization created successfully"
}
```

### Groups

#### Get All Groups
```http
GET /api/v1/get_groups
```
Returns a list of all groups.

**Response**
```json
{
    "groups": [
        {
            "id": integer,
            "name": string
        }
    ]
}
```

#### Create Group
```http
POST /api/v1/create_group
```
Creates a new group.

**Request Body**
```json
{
    "group_name": string,
    "id_specialization": integer
}
```

### Students

#### Get All Students
```http
GET /api/v1/get_students
```
Returns a list of all students.

**Response**
```json
{
    "students": [
        {
            "id": integer,
            "first_name": string,
            "middle_name": string,
            "last_name": string,
            "group_id": integer
        }
    ]
}
```

#### Get Students by Group ID
```http
GET /api/v1/get_students_by_group_id
```
Returns students in a specific group.

**Request Body**
```json
{
    "id_group": integer
}
```

#### Create Student
```http
POST /api/v1/create_student
```
Creates a new student.

**Request Body**
```json
{
    "first_name": string,
    "middle_name": string,
    "last_name": string,
    "id_group": integer
}
```

### Teachers

#### Get All Teachers
```http
GET /api/v1/get_teachers
```
Returns a list of all teachers.

**Response**
```json
{
    "teachers": [
        {
            "id": integer,
            "first_name": string,
            "middle_name": string,
            "last_name": string
        }
    ]
}
```

#### Create Teacher
```http
POST /api/v1/create_teacher
```
Creates a new teacher.

**Request Body**
```json
{
    "first_name": string,
    "middle_name": string,
    "last_name": string
}
```

### Subjects

#### Get All Subjects
```http
GET /api/get_subjects
```
Returns a list of all subjects.

**Response**
```json
{
    "message": [
        {
            "id": integer,
            "name": string
        }
    ]
}
```

#### Create Subject
```http
POST /api/v1/create_subject
```
Creates a new subject.

**Request Body**
```json
{
    "name": string,
    "id_teacher": integer
}
```

### Programs

#### Get All Programs
```http
GET /api/v1/get_programs
```
Returns a list of all programs.

**Response**
```json
{
    "message": [
        {
            "id": integer,
            "name": string,
            "id_specialization": integer,
            "id_subject": integer,
            "hours": integer
        }
    ]
}
```

#### Create Program
```http
POST /api/v1/create_program
```
Creates a new program.

**Request Body**
```json
{
    "name": string,
    "id_specialization": integer,
    "id_subject": integer,
    "hours": integer
}
```

### Schedules

#### Get All Schedules
```http
GET /api/v1/get_schedules
```
Returns a list of all schedules.

**Response**
```json
{
    "message": [
        {
            "id": integer,
            "id_subject": integer,
            "id_group": integer,
            "lesson_number": integer,
            "date_of_lesson": string
        }
    ]
}
```

#### Create Schedule
```http
POST /api/v1/create_schedule
```
Creates a new schedule entry.

**Request Body**
```json
{
    "id_subject": integer,
    "id_group": integer,
    "lesson_number": integer,
    "date_of_lesson": string
}
```

### Attendance

#### Get Student Attendance
```http
GET /api/v1/get_student_attendance
```
Returns attendance statistics for a specific student.

**Request Body**
```json
{
    "id_student": integer
}
```

**Response**
```json
{
    "total_attendance": integer,
    "present_count": integer,
    "absent_count": integer,
    "present_percentage": float,
    "absent_percentage": float,
    "subjects_attendance": [
        {
            "subject_name": string,
            "total": integer,
            "present": integer,
            "absent": integer
        }
    ]
}
```

#### Create Attendance
```http
POST /api/v1/create_attendance
```
Creates a new attendance record.

**Request Body**
```json
{
    "id_schedule": integer,
    "id_student": integer,
    "status": string
}
```

## Error Responses

All endpoints may return the following error responses:

- `400 Bad Request`: When the request is malformed or contains invalid data
- `404 Not Found`: When the requested resource doesn't exist
- `500 Internal Server Error`: When an unexpected server error occurs

Error responses follow this format:
```json
{
    "message": "Error description"
}
```
```