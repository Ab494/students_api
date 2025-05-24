from os import name
from django.test import TestCase
from .models import Student
from datetime import date
class StudentModelTest(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Ezra", last_name="Bett", birth_date=date(2000, 1, 1), enrollment_date=date(2025, 1, 1))
    def test_student_creation(self):
        student = Student.objects.get(first_name="Ezra")
        self.assertEqual(student.first_name, "Ezra")
        self.assertEqual(student.last_name, "Bett")
        self.assertEqual(student.birth_date, date(2000, 1, 1))
        self.assertEqual(student.enrollment_date, date(2025, 1, 1))