# Student Management REST API

A learning project built with Python, Django, Django REST Framework, SQLite, JWT authentication, filtering, searching, pagination and OpenAPI/Swagger documentation.

## Setup (Windows PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If PowerShell blocks activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## URLs

- Admin: http://127.0.0.1:8000/admin/
- Register: POST http://127.0.0.1:8000/api/register/
- Obtain JWT: POST http://127.0.0.1:8000/api/token/
- Refresh JWT: POST http://127.0.0.1:8000/api/token/refresh/
- Students: http://127.0.0.1:8000/api/students/
- Swagger docs: http://127.0.0.1:8000/api/docs/
- OpenAPI schema: http://127.0.0.1:8000/api/schema/

## Register example

```json
{
  "username": "aliza",
  "email": "aliza@example.com",
  "password": "StrongPass123!"
}
```

## Login example

POST `/api/token/`:
```json
{
  "username": "aliza",
  "password": "StrongPass123!"
}
```

Copy `access` from the response. In Postman choose Authorization > Bearer Token and paste it.

## Student example

POST `/api/students/`:
```json
{
  "name": "Aliza Aabdi",
  "email": "aliza.student@example.com",
  "roll_number": "CSE2027-01",
  "course": "CSE",
  "age": 21
}
```

## Endpoints

| Method | URL | Purpose |
|---|---|---|
| POST | `/api/register/` | Create user |
| POST | `/api/token/` | Login / get JWT |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/api/students/` | List own students |
| POST | `/api/students/` | Create student |
| GET | `/api/students/{id}/` | Retrieve student |
| PUT | `/api/students/{id}/` | Full update |
| PATCH | `/api/students/{id}/` | Partial update |
| DELETE | `/api/students/{id}/` | Delete student |

List options:
- Search: `/api/students/?search=Aliza`
- Filter: `/api/students/?course=CSE`
- Ordering: `/api/students/?ordering=-created_at`
- Pagination: `/api/students/?page=2`

## Run tests

```powershell
python manage.py test
```

## Learning notes

- `models.py`: database table definition.
- `serializers.py`: validates incoming data and converts model instances to JSON-friendly data.
- `views.py`: handles API requests and responses.
- `permissions.py`: controls who can modify records.
- `urls.py`: maps URLs to views.
- `settings.py`: enables DRF, JWT, filters, pagination and API docs.

This is a local learning project. Before production, replace the development secret key, set `DEBUG=False`, configure allowed hosts, use HTTPS, review password/token policies, and configure a production database.
