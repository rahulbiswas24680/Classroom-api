from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime


""" User's all model """

class User(AbstractUser):

    USER_CHOICES = [
    ('TEACHER', 'Teacher'),
    ('STUDENT', 'Student'),
    ]

    user_profession = models.CharField(max_length=7, choices=USER_CHOICES, default='STUDENT')

    def __str__(self):
        return self.username



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





""" classroom's all model """

class Classroom(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.DO_NOTHING)


""" Assignments's all model """

class CreatedAssignment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(Teacher, 
          on_delete = models.CASCADE, default=2)
    completed = models.BooleanField(default=False, null=True)




class CompletedAssignment(models.Model):
    assignment = models.ForeignKey(CreatedAssignment, on_delete=models.CASCADE, default=1, related_name="stored_assignments")
    title = models.CharField(max_length=250)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/', null=True)
    pdffile = models.FileField(upload_to ='uploads/', null=True)
    completed_by = models.OneToOneField(Student, 
          on_delete = models.CASCADE, default=1)


""" Notice's all model """

class Notice(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today, blank=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.title