from django.db import models

from testdocker.common.models.Choices import Gender
from testdocker.common.models.Mixins import TimeStamMixin
from testdocker.common.models.Utils import generate_college_id, generate_student_id, generate_teacher_id

# Create your models here.

    
class College(TimeStamMixin):
    college_id = models.CharField(default=generate_college_id, max_length=50, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Teacher(TimeStamMixin):
    name = models.CharField(max_length=50, blank=True, null=True)
    teacher_id = models.CharField(default=generate_teacher_id, max_length=50, unique=True)
    age = models.IntegerField(blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True, related_name='college_teachers')

    def __str__(self):
        return self.name

class Student(TimeStamMixin):
    name = models.CharField(max_length=50, blank=True, null=True)
    student_id = models.CharField(default=generate_student_id, max_length=50, unique=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices(), blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True, related_name='college_students')

    def __str__(self):
        return self.name

    
    
    