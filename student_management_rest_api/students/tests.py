from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student

class StudentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="aliza", password="TestPass123!")
        self.client.force_authenticate(user=self.user)

    def test_create_student(self):
        payload = {
            "name": "Test Student",
            "email": "test@example.com",
            "roll_number": "CSE101",
            "course": "CSE",
            "age": 21,
        }
        response = self.client.post("/api/students/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)

    def test_list_students(self):
        Student.objects.create(
            owner=self.user, name="A Student", email="a@example.com",
            roll_number="A1", course="CSE", age=20
        )
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
