import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from students.models import Student
from datetime import time
from rest_framework.response import Response
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class StudentAPITest(TestCase):
    def setUp(self):
        Student.objects.all().delete()
        User.objects.all().delete()
        Token.objects.all().delete()
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token, __ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.student_data = {
            "first_name": "Ezra",
            "last_name": "Bett",
            "email": "ezra@example.com",
            "birth_date": "2000-1-1",
            "enrollment_date": "2025-1-1"
        }
        Student.objects.all().delete()
    
    def test_create_and_get_student(self):

        # POST request to create a student

        response = self.client.post("/api/students/", data=json.dumps(self.student_data), content_type="application/json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

        # GET request to fetch students

        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0] ["first_name"], "Ezra")


