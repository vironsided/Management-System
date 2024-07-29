from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class StudentLeaveApp(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    to_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Leave application from {self.user}"


class AppStatus(models.Model):
    leaveApp = models.ForeignKey(StudentLeaveApp, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Status for leave application {self.leaveApp}"


class TeachLeaveApp(models.Model):
    user = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    to_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Leave application from {self.user}"
