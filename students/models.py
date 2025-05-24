from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    enrollment_date = models.DateField()
   

    def str(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name  
      
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    def str(self):
        return self.name
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'subject', 'date')

    def __str__(self):
        return f"{self.student} - {self.subject} on {self.date}"
    



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student} - {self.subject} on {self.score}"