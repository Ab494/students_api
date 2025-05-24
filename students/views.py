from re import search
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
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

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [IsAuthenticated]

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']

class AttendanceReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, student_id):
        report = Attendance.objects.filter(student_id=student_id)
        if not report.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        data = report.values('status').annotate(count=Count('status'))
        return Response(data)
