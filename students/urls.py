from turtle import title
from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SubjectViewSet, AttendanceViewSet, AttendanceReportView, GradeViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'courses',CourseViewSet)
router.register(r'grades', GradeViewSet)



urlpatterns = [
    path("api/", include(router.urls)),
    path("attendance-report/<int:student_id>/", AttendanceReportView.as_view()),
    
]
