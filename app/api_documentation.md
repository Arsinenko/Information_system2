# API Documentation

## Endpoints

### GET Endpoints

- **GET /api/v1/get_specializations/**
  - Description: Retrieve a list of specializations.

- **GET /api/v1/get_groups/**
  - Description: Retrieve a list of groups.

- **GET /api/v1/get_programs/**
  - Description: Retrieve a list of programs.

- **GET /api/v1/get_students/**
  - Description: Retrieve a list of students.

- **GET /api/v1/get_teachers/**
  - Description: Retrieve a list of teachers.

- **GET /api/v1/get_subjects/**
  - Description: Retrieve a list of subjects.

- **GET /api/v1/get_attendance_logs/**
  - Description: Retrieve attendance logs.

- **GET /api/v1/get_attendance/**
  - Description: Retrieve attendance information.

### POST Endpoints

- **POST /api/v1/create_specialization/**
  - Description: Create a new specialization.
  - Request Body: 
    ```json
    {
      "name": "string",
      "description": "string"
    }
    ```

- **POST /api/v1/create_group/**
  - Description: Create a new group.
  - Request Body: 
    ```json
    {
      "name": "string",
      "specialization_id": "integer"
    }
    ```

- **POST /api/v1/create_program/**
  - Description: Create a new program.
  - Request Body: 
    ```json
    {
      "name": "string",
      "duration": "integer"
    }
    ```

- **POST /api/v1/create_student/**
  - Description: Create a new student.
  - Request Body: 
    ```json
    {
      "name": "string",
      "group_id": "integer"
    }
    ```

- **POST /api/v1/create_teacher/**
  - Description: Create a new teacher.
  - Request Body: 
    ```json
    {
      "name": "string",
      "subject_id": "integer"
    }
    ```

- **POST /api/v1/create_subject/**
  - Description: Create a new subject.
  - Request Body: 
    ```json
    {
      "name": "string",
      "credits": "integer"
    }
    ```

- **POST /api/v1/create_attendance_log/**
  - Description: Create a new attendance log.
  - Request Body: 
    ```json
    {
      "student_id": "integer",
      "date": "string",
      "status": "string"
    }
    ```

- **POST /api/v1/create_attendance/**
  - Description: Create attendance for a student.
  - Request Body: 
    ```json
    {
      "student_id": "integer",
      "subject_id": "integer",
      "date": "string"
    }
    ```

### PUT Endpoints

- **POST /api/v1/update_specialization**
  - Description: Update an existing specialization.
  - Request Body: 
    ```json
    {
      "id": "integer",
      "name": "string",
      "description": "string"
    }
    ```

- **POST /api/v1/update_group**
  - Description: Update an existing group.
  - Request Body: 
    ```json
    {
      "id": "integer",
      "name": "string"
    }
    ```

### DELETE Endpoints

- **DELETE /api/v1/delete_specialization/**
  - Description: Delete a specialization by ID.
  - Request Body: 
    ```json
    {
      "id": "integer"
    }
    ```

## Notes
- Ensure to replace placeholder values in the request body with actual data when making requests.
