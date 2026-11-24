# Student Management REST API

A RESTful API built using **Python, Django REST Framework, and JWT Authentication** to manage student records efficiently. This project provides secure CRUD operations, allowing users to create, retrieve, update, and delete student information.

# Features

- User Registration
- JWT Authentication (Access and Refresh Tokens)
- Create New Student Records
- Retrieve All Students
- Retrieve Student Details by ID
- Update Student Information
- Partial Update of Student Records
- Delete Student Records
- API Documentation using Swagger UI

#Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- Swagger / OpenAPI
- Git & GitHub

##API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/register/` | Register a new user |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/api/students/` | Get all students |
| POST | `/api/students/` | Create a student |
| GET | `/api/students/{id}/` | Get student by ID |
| PUT | `/api/students/{id}/` | Update student |
| PATCH | `/api/students/{id}/` | Partially update student |
| DELETE | `/api/students/{id}/` | Delete student |

#Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/aabdi-aliza/student_management_rest_api.git
```

### 2. Navigate to the project directory

```bash
cd student_management_rest_api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies
