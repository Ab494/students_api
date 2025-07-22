# students/views.py
# This file contains the views for the students application, including viewsets for various models and an API view for attendance reports.
from re import search
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from students import serializers
from .models import Student, Subject, Attendance, Grade, Course
from .serializers import StudentSerializer, SubjectSerializer, AttendanceSerializer, GradeSerializer, CourseSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

# ViewSet fo Student model with no authentication and permission for public 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [AllowAny]


# ViewSet for subject model no [authentication/permissions set ]
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [AllowAny]

# ViewSet for Attendance model with no authentication and permission for public
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [AllowAny]

# ViewSet for Grade model with no authentication and permission for public
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    

# ViewSet for Course model with no authentication and permission for public
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
# ViewSet for Student model with authentication and permission for authenticated users
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']

# AttendanceReportView to get attendance report for a specific student
class AttendanceReportView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, student_id):
        report = Attendance.objects.filter(student_id=student_id)
        if not report.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        data = report.values('status').annotate(count=Count('status'))
        return Response(data)


